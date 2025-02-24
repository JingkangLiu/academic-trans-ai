#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
streaming_window.py - 滚动窗口翻译处理器

版本: 3.0.0
作者: Liu Jingkang
最后更新: 2024-02-24
创建日期: 2024-01-10  # 根据实际开发情况调整
许可证: MIT
"""
import asyncio
import os
import time
from pathlib import Path
from openai import OpenAI, RateLimitError
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple
from dotenv import load_dotenv
from Segmente import MarkdownSegmenter
from ContentOptimizer import ContentOptimizer
import httpx




# 加载配置
load_dotenv()
MAIN_API_KEYS = os.getenv("MAIN_API_KEYS", "").split(",")
BACKUP_API_KEYS = os.getenv("BACKUP_API_KEYS", "").split(",")
BASE_URL = os.getenv("BASE_URL", "https://api.siliconflow.cn/v1/")
WORK_DIR = Path("workmd")
OUTPUT_DIR = Path("outputmd")
ERROR_DIR = Path("errormd")  # 新增错误文本保存目录

# 在OUTPUT_DIR下方添加日志目录
CHATLOG_DIR = OUTPUT_DIR / "chatlogs"
CHATLOG_DIR.mkdir(exist_ok=True, parents=True)
ERROR_DIR.mkdir(exist_ok=True, parents=True)

# 系统提示词
sys_prompts = {
    "md": r"""您是中英学术翻译专家，当前正在进行分段滚动翻译（总轮次：{{total_rounds}}，当前第{{current_round}}轮）。  
【强制要求】 逐字逐句翻译，不能进行任何程度的精简。
1. 必须将所有原markdown文本和前文翻译都阅读并理解，将[前文翻译]其作为连续上下文衔接基础，从[[前文翻译]]结束位置自然衔接，避免任何遗漏或重复翻译。
2. 翻译在目标文本块末尾附近结束，使上下文连贯的自然结束，使段落语义完整，代码块、表格、或公式块完整，避免过度翻译<后文>的内容。

【翻译原则】逐字逐句、准确、专业翻译，确保翻译和原文一一对应，不生成无关内容。保持markdown内联latex的格式，公式块使用双美元符，双美元符公式块需要单独成行，行内公式使用单美元符。正文使用中文全角标点符号，数学文本中使用英文半角标点符号。插入图片的代码保持原状不要作任何改动。

【翻译的细节】

1. 英文的长句翻译通常不会直接对应中文句式，你需要作出逻辑叙述的调整。
2. 为照顾汉语的习惯，采用一词两译的做法。例如"set"在汉语中有时译成"集合"有时译成"集"，单独使用时常译成"集合"，而在与其他词汇连用时则译成"集"（如可数集等）。
3. 汉语"是"通常有两种含义，一是"等于"，二是"属于"。在本书中"是"只表示等于的意思，而属于的意思则用"是一个"来表示。例如，不说"X是拓扑空间"，而说"X是一个拓扑空间"。
4. 在汉语中常难于区别单数和复数，而在英语的表达中又常常对于名词的复数形式与集合名词不加区别。对于这种情形，你需要宁可啰嗦一点，以保证不被误解
5. 如果可能，将公式代码更简洁表示，针对括号的代码表示的简洁化，不能修改原公式的数学含义。并确保公式如有编号，必须与原文一致。
例1：
{U}^{k + 1}\left\lbrack  {\left( {j - 1}\right) \left( {N - 1}\right)  + i}\right\rbrack   = {\widetilde{U}}^{k + 1}\left\lbrack  {\left( {i - 1}\right) \left( {M - 1}\right)  + j}\right\rbrack
可以重写为
U^{k+1}\bigl[(j - 1)(N - 1) + i\bigr] = \widetilde{U}^{k+1}\bigl[(i - 1)(M - 1) + j\bigr]
翻译过程中对原文本的优化：

1.算法（伪代码）重构
例2：
对于一些算法，原文的样式如下
---

Given VG parameter $\sigma ,\nu ,\theta$

For time $T$ and spot ${S}_{0}$

Set $N$ and calculate $h = T/N$

calculate $\omega  = \frac{1}{\nu }\log \left( {1 - {\theta \nu } - {\sigma }^{2}\nu /2}\right)$

for $i = 1,\ldots , N$ do

	$z \sim  \mathcal{N}\left( {0,1}\right)$
	
	$g \sim  \mathrm{G}\left( {h/\nu ,\nu }\right)$
	
	${X}_{i} = {\theta g} + \sigma \sqrt{g}z$
	
	$\log {S}_{i} = \log {S}_{i - 1} + \left( {r - q}\right) h + {\omega h} + {X}_{i}$

end for

---

可以重写为：

$$
\begin{aligned}
\hline
&\textbf{[算法名,没有则留空]}\\[5pt]
\hline \\[-10pt]
\textbf{input:}  &\ \text{参数 } \sigma, \nu, \theta,\ \text{时间 } T,\ \text{现货价 } S_0 \\
\textbf{output:}  &\ \text{对数价格路径 } \{\log S_i\}_{i=1}^N \\[5pt]
\hline \\[-10pt]
&1. \quad \text{Set } N,\ \text{calculate } h = T/N \\
&2. \quad \text{calculate } \omega = \frac{1}{\nu}\ln\big(1 - \theta\nu - \sigma^2\nu/2\big) \\
&3. \quad \textbf{for } i = 1 ,\ldots N  \\
&4. \quad \quad z \sim \mathcal{N}(0,1) \\
&5. \quad \quad g \sim \mathrm{Gamma}(h/\nu, \nu) \\
&6. \quad \quad X_i = \theta g + \sigma\sqrt{g}z \\
&7. \quad \quad \ln S_i = \ln S_{i-1} + (r - q)h + \omega h + X_i \\
&8. \quad \textbf{endfor} \\[5pt]
\hline
\end{aligned}
$$

2.表格转换

HTML转Markdown示例

<!-- Before -->
<table><tr><td>European call</td><td>$c(S,t) = ...$</td></tr></table>

↓

<!-- After -->
| Option        | Pricing Formula                          |
|---------------|------------------------------------------|
| European call | $c(S,t)=e^{-r(T-t)}\mathbb{E}[(S_T-K)^+]$|
```

3.代码优化
翻译过程中碰到类似代码的语言（注意区别伪代码和代码，伪代码使用算法框），可以通过上下文或代码风格判断代码语言（这个示例是R语言，也可能是其他语言）
---

   tsplot(cbind(gtemp_land, gtemp_ocean), spaghetti=TRUE,

   	col=astsa.col(c(4,2),.7), pch=c(20,18), type="o", ylab="\\u00BOC",
   	
   	main="Global Surface Temperature Anomalies", addLegend=TRUE,
   	
   	location="topleft", legend=c("Land Surface","Sea Surface"))

---

   规范化如下：

   ```R
tsplot(cbind(gtemp_land, gtemp_ocean), 
       spaghetti=TRUE,
       col=astsa.col(c(4,2),.7), 
       pch=c(20,18), 
       type="o", 
       ylab="\u00B0C",
       main="Global Surface Temperature Anomalies", 
       addLegend=TRUE,
       location="topleft", 
       legend=c("Land Surface","Sea Surface"))
   ```
````
"""
}

class APIPool:
    def __init__(self, main_keys, backup_keys):
        self.main_pool = asyncio.Queue()
        self.backup_pool = asyncio.Queue()
        self.used_backup_keys = set()  # 跟踪已使用的备用key
        
        for key in main_keys:
            if key:  # 确保不添加空key
                self.main_pool.put_nowait(key)
        for key in backup_keys:
            if key:  # 确保不添加空key
                self.backup_pool.put_nowait(key)

    async def get_key(self, file_count):
        """常规获取API key，只从主池获取"""
        return await self.main_pool.get()

    async def get_backup_key(self):
        """从备用池获取key，用于处理429错误"""
        try:
            return self.backup_pool.get_nowait()
        except asyncio.QueueEmpty:
            print("所有备用API都已尝试过")
            raise

    def release_key(self, key, had_429=False):
        """释放key到对应的池"""
        if had_429:
            # 遇到429错误的key不再放回任何池
            return
        elif key in MAIN_API_KEYS:
            self.main_pool.put_nowait(key)
        else:
            self.backup_pool.put_nowait(key)

# 初始化API池
api_pool = APIPool(MAIN_API_KEYS, BACKUP_API_KEYS)

def build_dynamic_prompt(prev_seg: str, current_seg: str, next_seg: str,
                        history: str, total_rounds: int, current_round: int,
                        use_r1: bool) -> str:
    """构建动态用户提示词"""
    # 原系统提示词现在作为用户提示词的基础
    raw_user_prompt = sys_prompts["md"]
    
    # 动态插入模型特定要求
    model_specific_rules = []
    if use_r1:
        model_specific_rules.append("【着重要求】逐字逐句翻译，不能进行任何程度的精简或概括，注意可能的算法（伪代码）重构、表格转换和代码识别")
    else:
        model_specific_rules.extend([
            "【着重要求】你的输出必须严格符合上下文衔接：",
            "1. 确保翻译起始点与前文翻译的结尾完全衔接",
            "2. 当前段翻译结束位置必须与后文开头自然过渡，避免过度翻译后文内容"
        ])
    
    # 插入到用户提示词指定位置
    insert_position = raw_user_prompt.find("翻译原则：")
    if insert_position != -1:
        raw_user_prompt = (
            raw_user_prompt[:insert_position] 
            + "\n".join(model_specific_rules) + "\n\n"
            + raw_user_prompt[insert_position:]
        )

    # 变量替换
    user_prompt_base = raw_user_prompt.replace("{{total_rounds}}", str(total_rounds)) \
                                      .replace("{{current_round}}", str(current_round))
    
    # 重构后的用户提示词模板
    user_template = f"""
{user_prompt_base}

请严格遵循以下最终要求：
1. 必须将所有原markdown文本和前文翻译都阅读并理解，将[前文翻译]其作为连续上下文衔接基础，从[[前文翻译]]结束位置自然衔接，避免任何遗漏或重复翻译
2. 翻译在目标文本块末尾附近结束，使上下文连贯的自然结束，使段落语义完整，代码块、表格、或公式块完整，避免过度翻译<后文>的内容
3. 直接输出翻译后的文本

上下文信息：
```
<<前文>>
{prev_seg or "无前文"}
```

```
<<当前目标块>>
{current_seg}
```

```
<<后文>>
{next_seg or "无后文"}
```

[前文翻译] (仅供上下文参考，禁止修改)
```
{history or "无历史翻译"}
```
"""

    return user_template

def process_stream(stream):
    """处理流式响应并返回完整响应"""
    full_response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
    return full_response

def create_window(segments: List[str], index: int) -> Tuple[str, str, str]:
    """创建三窗口上下文"""
    prev = segments[index-1] if index > 0 else ""
    current = segments[index]
    next_seg = segments[index+1] if index < len(segments)-1 else ""
    return prev, current, next_seg

async def translate_with_context(
    client, 
    segments: List[str],  
    index: int,       
    history: str, 
    window: Tuple[str, str, str], 
    log_file: Path
) -> Tuple[str, bool]:
    prev_seg, current_seg, next_seg = window
    max_retries = 5  
    retry_count = 0
    current_key = client.api_key
    
    while retry_count < max_retries:
        try:
            # 合并前后文进行优化检测
            detection_content = f"{prev_seg}\n{current_seg}\n{next_seg}"
            optimizer = ContentOptimizer(api_key=client.api_key)
            optimization_result = optimizer.check_optimization(detection_content)
            use_r1 = optimization_result.get("tag", False)
            
            # 动态模型选择
            if use_r1:
                model_name = "deepseek-ai/DeepSeek-R1"
                max_tokens = 16384
            else:
                model_name = "deepseek-ai/DeepSeek-V3" 
                max_tokens = 4096

            user_prompt = build_dynamic_prompt(
                prev_seg, current_seg, next_seg,
                history,
                total_rounds=len(segments),
                current_round=index+1,
                use_r1=use_r1
            )
            
            messages = [
                {"role": "system", "content": "你是一个专业的中英学术翻译助手"},
                {"role": "user", "content": user_prompt}
            ]
            
            # 添加首尾特殊处理
            if index == 0:
                messages.append({
                    "role": "user",
                    "content": "【首轮特别提示】请从目标块起始处开始翻译，注意建立完整上下文基础"
                })
            elif index == len(segments)-1:
                messages.append({
                    "role": "user",
                    "content": "【末轮特别提示】请确保完整翻译剩余内容，并做好全文收尾工作"
                })

            # 记录请求日志
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"\n\n{'='*40} Request {time.strftime('%Y-%m-%d %H:%M:%S')} {'='*40}\n")
                f.write(f"== Retry Count: {retry_count} ==\n")
                f.write("== Messages ==\n")
                for msg in messages:
                    f.write(f"{msg['role'].upper()}:\n{msg['content']}\n\n")

            # API调用
            with ThreadPoolExecutor() as executor:
                stream = await asyncio.get_event_loop().run_in_executor(
                    executor,
                    lambda: client.chat.completions.create(
                        model=model_name,
                        max_tokens=max_tokens,
                        messages=messages,
                        temperature=0.3 if use_r1 else 0.2,
                        top_p=0.95,
                        top_k=90,
                        frequency_penalty=0,
                        stream=True
                    )
                )
                reply = process_stream(stream)
                
            # 记录响应日志
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"\n== 使用模型: {model_name} ==\n")
                f.write(f"== 最大token: {max_tokens} ==\n")
                f.write(f"== 优化需求: {use_r1} ==\n")
                f.write(f"\n== Response ==\n{reply}\n")
            
            return reply, False

        except RateLimitError as e:
            if "429" in str(e):
                print(f"API {current_key[:8]}... 遇到速率限制 (429)，切换到备用API")
                api_pool.release_key(current_key, had_429=True)
                
                try:
                    # 直接从备用池获取新的key
                    current_key = await api_pool.get_backup_key()
                    client = OpenAI(base_url=BASE_URL, api_key=current_key)
                    print(f"切换到备用API: {current_key[:8]}...")
                    continue
                except asyncio.QueueEmpty:
                    print("备用API池已耗尽，任务无法继续")
                    raise
                
        except httpx.RemoteProtocolError as e:
            if "peer closed connection without sending complete message body" in str(e):
                retry_count += 1
                print(f"连接错误: {str(e)}, 第{retry_count}次重试...")
                await asyncio.sleep(2)
                continue
            else:
                raise
                
        except Exception as e:
            raise

    # 达到最大重试次数后返回原文
    print(f"连续{max_retries}次连接错误，将使用原文...")
    return current_seg, True

async def process_segment(client, output_file: Path, segments: List[str], index: int, history: str, log_file: Path):
    """处理单个段落"""
    window = create_window(segments, index)
    
    translated, is_original = await asyncio.wait_for(
        translate_with_context(
            client, 
            segments,    
            index,       
            history, 
            window, 
            log_file
        ),
        timeout=600
    )

    # 如果是原文，同时保存到错误目录
    if is_original:
        error_file = ERROR_DIR / f"error_{output_file.name}"
        with open(error_file, 'a', encoding='utf-8') as f:
            f.write(f"\n\n=== 错误段落 {index + 1} ===\n\n")
            f.write(translated)

    # 写入翻译结果或原文
    with open(output_file, 'a', encoding='utf-8') as f:
        if index == 0:
            f.write(translated)
        else:
            f.write("\n\n" + translated)
    return translated

async def translate_file(file_path: Path):
    """处理单个文件"""
    current_key = await api_pool.get_key(len(MAIN_API_KEYS))
    try:
        client = OpenAI(
            base_url=BASE_URL,
            api_key=current_key
        )
        
        # 创建专属日志文件
        log_file = CHATLOG_DIR / f"{file_path.stem}_chatlog.txt"
        log_file.write_text("")  # 清空旧日志
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 智能分段
        segmenter = MarkdownSegmenter(max_length=4000,min_length=3000)
        segments = segmenter.segment(content)
        
        output_file = OUTPUT_DIR / f"trans_{file_path.name}"
        output_file.write_text("")  # 清空文件
        
        history = ""
        for i in range(len(segments)):
            history = await process_segment(client, output_file, segments, i, history, log_file)
            print(f"进度: {i+1}/{len(segments)} 完成")

        return history
    finally:
        api_pool.release_key(current_key)

async def main():
    """主函数"""
    # 设置并发数为主API数量
    semaphore = asyncio.Semaphore(len(MAIN_API_KEYS))
    
    async with semaphore:
        tasks = []
        # 分批次处理文件
        files = list(WORK_DIR.glob("*.md"))
        while files:
            current_batch = files[:len(MAIN_API_KEYS)]
            files = files[len(MAIN_API_KEYS):]
            
            batch_tasks = [translate_file(file) for file in current_batch]
            await asyncio.gather(*batch_tasks)
            
            if files:
                print("等待API释放以处理剩余文件...")
                await asyncio.sleep(5)  # 批次间隔

if __name__ == "__main__":
    asyncio.run(main())