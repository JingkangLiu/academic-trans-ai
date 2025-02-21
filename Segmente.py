import re
from pathlib import Path
from typing import List, Dict, Tuple

class MarkdownSegmenter:
    def __init__(self, max_length=5000, min_length=4000):
        self.max_length = max_length
        self.min_length = min_length
        self.min_segment_length = 800  # 最小分段长度
        self.max_segment_length = 9000  # 最大分段长度
        self.small_split_threshold = 800  # 小拆分阈值
        
        # 预编译正则表达式
        self.formula_start = re.compile(r'^\s*\$\$', re.MULTILINE)
        self.algorithm_start = re.compile(
            r'(?:^|\n)###*\s*Algorithm\b|^---.*?\b(Algorithm|Pseudocode)\b',
            re.IGNORECASE
        )
        self.continuation_keywords = re.compile(
            r'^\s*(where|which|with|assuming|let\b|in\b|such\s+that)',
            re.IGNORECASE
        )
        self.sentence_end = re.compile(r'[.!?]\s*$')
        self.paragraph_split = re.compile(r'(?<!#)\n\s*\n')
        self.code_block = re.compile(r'^```.*?^```', re.MULTILINE | re.DOTALL)
        self.header_pattern = re.compile(r'^#{1,6}\s+')  # 新增标题检测

    def segment(self, content: str) -> List[str]:
        """主分段入口"""
        blocks = self._parse_blocks(content)
        protected_blocks = self._process_protected_zones(blocks)
        segments = self._build_segments(protected_blocks)
        return self._post_process_segments(segments)

    def _parse_blocks(self, content: str) -> List[Dict]:
        """解析文档为带元数据的块列表"""
        raw_blocks = [b for b in self.paragraph_split.split(content) if b.strip()]
        blocks = []
        in_algorithm = False
        algorithm_nesting = 0

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

            # 检测公式块
            if self.formula_start.match(text):
                block['type'] = 'formula'
                block['protected'] = True

            # 检测代码块
            if self.code_block.search(text):
                block['type'] = 'code'
                block['protected'] = True

            # 检测算法块开始
            if self.algorithm_start.search(text):
                in_algorithm = True
                algorithm_nesting = 0

            # 处理算法块内部
            if in_algorithm:
                block['type'] = 'algorithm'
                block['protected'] = True
                algorithm_nesting += self._count_nested_blocks(text)

                # 修正算法块结束检测
                if text.strip().startswith('---'):
                    if algorithm_nesting <= 0:
                        in_algorithm = False
                    else:
                        algorithm_nesting = max(0, algorithm_nesting - 1)

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
        # 新增公式上下文延续规则
        if re.search(r'\$\$[^$]*$', prev_text) and not re.match(r'^[!\[<]', current_text):
            return True
        if re.match(r'^\s*\$\$', current_text) and not re.search(r'[!\]>]\s*$', prev_text):
            return True
        # 前导文本未结束
        if not self.sentence_end.search(prev_text):
            return True

        # 当前文本是延续关键词
        if self.continuation_keywords.match(current_text):
            return True

        # 公式后的解释性文本
        if self.formula_start.match(prev_text) and \
           not self.paragraph_split.match(current_text):
            return True

        return False

    def _process_protected_zones(self, blocks: List[Dict]) -> List[Dict]:
        """处理保护区域连续性"""
        processed = []
        protected_group = []
        current_protected = False

        for block in blocks:
            if block['protected'] or block['continuation']:
                if not current_protected:
                    protected_group = []
                    current_protected = True
                protected_group.append(block)
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

    def _post_process_segments(self, segments: List[str]) -> List[str]:
        """对分段进行后处理"""
        if not segments:
            return segments

        # 第一步：处理过短的分段
        processed = []
        i = 0
        while i < len(segments):
            current_len = len(segments[i])
            
            if current_len < self.min_segment_length:
                # 如果是第一段，尝试与下一段合并
                if i == 0 and i + 1 < len(segments):
                    processed.append(segments[i] + "\n\n" + segments[i + 1])
                    i += 2
                # 如果是最后一段，与前一段合并
                elif i == len(segments) - 1 and processed:
                    processed[-1] = processed[-1] + "\n\n" + segments[i]
                    i += 1
                # 中间段，选择与较短的相邻段合并
                elif i > 0 and i + 1 < len(segments):
                    prev_len = len(processed[-1])
                    next_len = len(segments[i + 1])
                    if prev_len <= next_len:
                        processed[-1] = processed[-1] + "\n\n" + segments[i]
                    else:
                        processed.append(segments[i] + "\n\n" + segments[i + 1])
                        i += 1
                    i += 1
                else:
                    processed.append(segments[i])
                    i += 1
            else:
                processed.append(segments[i])
                i += 1

        # 第二步：处理过长的分段
        final_segments = []
        for i, segment in enumerate(processed):
            if len(segment) > self.max_segment_length:
                # 尝试找到合适的小拆分
                splits = self._find_small_splits(segment)
                
                if splits and i > 0 and len(final_segments[-1]) + splits[0] < self.max_segment_length:
                    # 将第一个小拆分合并到前一段
                    final_segments[-1] = final_segments[-1] + "\n\n" + segment[:splits[0]]
                    final_segments.append(segment[splits[0]:])
                elif splits and i + 1 < len(processed) and \
                     len(segment[splits[-1]:] + "\n\n" + processed[i + 1]) < self.max_segment_length:
                    # 将最后一个小拆分合并到后一段
                    final_segments.append(segment[:splits[-1]])
                    processed[i + 1] = segment[splits[-1]:] + "\n\n" + processed[i + 1]
                else:
                    # 无法优化，保持原样
                    final_segments.append(segment)
            else:
                final_segments.append(segment)

        return final_segments

    def _find_small_splits(self, text: str) -> List[int]:
        """在文本中寻找可能的小拆分位置"""
        splits = []
        
        # 使用段落分隔符查找可能的拆分点
        for match in self.paragraph_split.finditer(text):
            pos = match.start()
            # 检查拆分点前后的文本长度是否接近小拆分阈值
            if abs(pos - self.small_split_threshold) < 100:
                splits.append(pos)
            
        # 如果没有找到合适的段落分隔符，尝试在句子边界查找
        if not splits:
            for match in self.sentence_end.finditer(text):
                pos = match.end()
                if abs(pos - self.small_split_threshold) < 100:
                    splits.append(pos)
                
        return splits

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
    save_segments(segments, output_dir)
    print(f'\nTotal segments: {len(segments)}')
