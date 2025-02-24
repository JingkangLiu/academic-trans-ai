import re
from pathlib import Path
from typing import List, Dict, Tuple

class MarkdownSegmenter:
    def __init__(self, max_length=5000, min_length=4000):
        self.max_length = max_length
        self.min_length = min_length
        
        # 预编译正则表达式
        self.formula_start = re.compile(r'^\s*\$\$', re.MULTILINE)
        self.formula_end = re.compile(r'\$\$\s*$')  # 以$$结尾
        self.algorithm_start = re.compile(
            r'(?:^|\n)###*\s*Algorithm\b',
            re.IGNORECASE
        )
        self.continuation_keywords = re.compile(
            r'^\s*(where|which|with|assuming|let\b|in\b|such\s+that)',
            re.IGNORECASE
        )
        self.sentence_end = re.compile(r'[.!?]\s*$')
        self.paragraph_split = re.compile(r'(?<!#)\n\s*\n')
        self.code_block = re.compile(r'^```[^\n]*\n.*?^```', re.MULTILINE | re.DOTALL)
        self.header_pattern = re.compile(r'^#{1,6}\s+')  # 新增标题检测

    def segment(self, content: str, return_preprocessed=False) -> List[str]:
        """主分段入口"""
        blocks = self._parse_blocks(content)
        protected_blocks = self._process_protected_zones(blocks)
        segments = self._build_segments(protected_blocks)
        
        return segments  # 直接返回原始分段结果，不再进行后处理

    def _parse_blocks(self, content: str) -> List[Dict]:
        """解析文档为带元数据的块列表"""
        raw_blocks = [b for b in self.paragraph_split.split(content) if b.strip()]
        blocks = []
        in_algorithm = False

        for i, text in enumerate(raw_blocks):
            block = {
                'text': text,
                'type': 'normal',
                'protected': False,
                'continuation': False
            }

            # 新增标题块检测
            if self.header_pattern.match(text.strip()):
                block['type'] = 'header'
                block['protected'] = True

            # 检测公式块（仅匹配以$$开头的块）
            if self.formula_start.search(text) and self.formula_end.search(text):
                block['type'] = 'formula'
                block['protected'] = True

            # 检测代码块（完整匹配```...```）
            if self.code_block.fullmatch(text.strip()):
                block['type'] = 'code'
                block['protected'] = True

            # 检测算法块开始
            if self.algorithm_start.search(text):
                in_algorithm = True

            # 处理算法块内部
            if in_algorithm:
                block['type'] = 'algorithm'
                block['protected'] = True

            # 检测延续关系
            if i > 0:
                prev_text = raw_blocks[i-1]
                block['continuation'] = self._needs_continuation(prev_text, text)

            blocks.append(block)

        return blocks

    def _count_nested_blocks(self, text: str) -> int:
        """计算嵌套块层数"""
        formula_count = len(self.formula_start.findall(text))
        code_count = len(self.code_block.findall(text))
        return formula_count + code_count

    def _needs_continuation(self, prev_text: str, current_text: str) -> bool:
        """判断是否需要延续"""
        # 前导文本未结束
        if not self.sentence_end.search(prev_text):
            return True

        # 当前文本是延续关键词
        if self.continuation_keywords.match(current_text):
            return True

        return False

    def _process_protected_zones(self, blocks: List[Dict]) -> List[Dict]:
        """处理保护区域连续性"""
        processed = []
        protected_group = []
        current_protected = False
        last_protected_type = None  # 跟踪保护类型

        for block in blocks:
            if block['protected'] or block['continuation']:
                if not current_protected:
                    protected_group = []
                    current_protected = True
                protected_group.append(block)
                
                # 仅当连续同类型保护块时才合并
                if last_protected_type and block.get('type') != last_protected_type:
                    processed.append({'type': 'protected_group', 'blocks': protected_group})
                    protected_group = []
                
                last_protected_type = block.get('type')
            else:
                if current_protected:
                    processed.append({
                        'type': 'protected_group',
                        'blocks': protected_group
                    })
                    protected_group = []
                    current_protected = False
                processed.append({'type': 'normal', 'blocks': [block]})

        if protected_group:
            processed.append({'type': 'protected_group', 'blocks': protected_group})

        return processed

    def _build_segments(self, processed_blocks: List[Dict]) -> List[str]:
        """构建最终分段"""
        segments = []
        current_segment = []
        current_length = 0

        for group in processed_blocks:
            group_text = '\n\n'.join([b['text'] for b in group['blocks']])
            group_len = len(group_text)

            if group['type'] == 'protected_group':
                # 保护组强制保持完整
                if current_length + group_len > self.max_length:
                    if current_segment:
                        segments.append('\n\n'.join(current_segment))
                        current_segment = []
                        current_length = 0
                current_segment.append(group_text)
                current_length += group_len
            else:
                # 普通块处理
                if current_length + group_len > self.max_length:
                    self._split_normal_blocks(current_segment, group['blocks'])
                else:
                    current_segment.extend([b['text'] for b in group['blocks']])
                    current_length += group_len

            # 检查当前段长度
            if current_length >= self.min_length:
                segments.append('\n\n'.join(current_segment))
                current_segment = []
                current_length = 0

        if current_segment:
            segments.append('\n\n'.join(current_segment))

        return segments

    def _split_normal_blocks(self, current_segment: List[str], blocks: List[Dict]):
        """分割普通块"""
        for block in blocks:
            block_text = block['text']
            block_len = len(block_text)

            if len(current_segment) + block_len > self.max_length:
                # 寻找最佳分割点
                split_pos = self._find_split_position(block_text)
                if split_pos > 0:
                    current_segment.append(block_text[:split_pos])
                    segments.append('\n\n'.join(current_segment))
                    current_segment = [block_text[split_pos:]]
                else:
                    segments.append('\n\n'.join(current_segment))
                    current_segment = [block_text]
            else:
                current_segment.append(block_text)

    def _find_split_position(self, text: str) -> int:
        """寻找最佳分割位置"""
        # 新增标题保护
        header_match = re.search(r'\n#+\s+.*?(\n|$)', text)
        if header_match:
            return header_match.start()
        
        # 修改句子结束检测（排除公式内的句点）
        sentence_split = None
        for match in self.sentence_end.finditer(text):
            if not self._is_inside_inline_math(text, match.end()):
                sentence_split = match
                break
        
        if sentence_split:
            return sentence_split.end()
        
        # 保持其他逻辑...
        return min(len(text), self.max_length // 2)

    def _is_inside_inline_math(self, text: str, position: int) -> bool:
        """判断位置是否在内联公式中"""
        # 计算position前的$符号数量
        before = text[:position].count('$') - text[:position].count(r'\$')
        return before % 2 == 1

def save_segments(segments: List[str], output_dir: Path):
    output_dir.mkdir(exist_ok=True, parents=True)
    for i, seg in enumerate(segments, 1):
        with open(output_dir / f'segment_{i:03d}.md', 'w', encoding='utf-8') as f:
            f.write(seg)
        print(f'Segment {i:03d} created ({len(seg)} chars)')

if __name__ == '__main__':
    input_file = Path('testmd.md')
    output_dir = Path('segments')

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    segmenter = MarkdownSegmenter()
    segments = segmenter.segment(content)

    # 保存分段结果
    save_segments(segments, output_dir)
    
    print("\n" + "="*50)
    print(f'总分段数量: {len(segments)}')
