#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
streaming.py - 流式学术文档翻译处理器

功能：
- 智能分段处理大文件
- 多API负载均衡
- 上下文感知翻译
- 实时保存翻译结果

版本: 1.2.0
作者: Liu Jingkang
创建日期: 2025-02-22
许可证: MIT
"""
import asyncio
import os
import traceback
from pathlib import Path
from openai import OpenAI
from concurrent.futures import ThreadPoolExecutor
from typing import List
from dotenv import load_dotenv


# 加载配置文件
load_dotenv()

# 硅基流动调用deepseek
API_KEYS = os.getenv("API_KEYS", "").split(",")
BASE_URL = os.getenv("BASE_URL", "https://api.siliconflow.cn/v1/")



# 初始化文件夹路径
WORK_DIR = Path("workmd")
OUTPUT_DIR = Path("outputmd")


# 将prompts改为sys_prompts，仅作为系统提示词
sys_prompts = {
    "txt": """你现在是一个专业的学术翻译专家，专门负责将英文学术音频转写文本翻译成中文。

核心要求：
1. 完整性和准确性是首要任务
2. 逐字逐句翻译，不得省略或简化
3. 保持专业术语的准确性
4. 确保与上下文的翻译保持连贯性

翻译规范：
1. 使用中文全角标点，数学文本使用英文半角标点
2. 行内公式使用单美元符 $ $
3. 保持专业性和可读性的平衡
4. 保留原有引用标注和格式""",

    "md": r"""你现在是一个专业的学术翻译专家.
    翻译原则：逐字逐句、准确、专业翻译，不额外生成其他内容。保持markdown内联latex的格式，公式块使用双美元符，双美元符公式块需要单独成行，行内公式使用单美元符。正文使用中文全角标点符号，数学文本中使用英文半角标点符号。插入图片的代码保持原状不要作任何改动。

翻译的细节要求:

1. 英文的长句翻译通常不会直接对应中文句式，你需要作出逻辑叙述的调整。
2. 为照顾汉语的习惯，采用一词两译的做法。例如"set"在汉语中有时译成"集合"有时译成"集"，单独使用时常译成"集合"，而在与其他词汇连用时则译成"集"（如可数集等）。
3. 汉语"是"通常有两种含义，一是"等于"，二是"属于"。在本书中"是"只表示等于的意思，而属于的意思则用"是一个"来表示。例如，不说"X是拓扑空间"，而说"X是一个拓扑空间"。
4. 在汉语中常难于区别单数和复数，而在英语的表达中又常常对于名词的复数形式与集合名词不加区别。对于这种情形，你需要宁可啰嗦一点，以保证不被误解

翻译过程中对原文本的优化：

````
1.公式优化
公式的表示可以更简洁，比如去掉不必要的花括号，使公式代码更易读。但同时确保只进行代码层面的调整，不能以任何程度修改原公式的数学含义，避免引入错误
例1：
{U}^{k + 1}\left\lbrack  {\left( {j - 1}\right) \left( {N - 1}\right)  + i}\right\rbrack   = {\widetilde{U}}^{k + 1}\left\lbrack  {\left( {i - 1}\right) \left( {M - 1}\right)  + j}\right\rbrack
可以重写为
U^{k+1}\bigl[(j - 1)(N - 1) + i\bigr] = \widetilde{U}^{k+1}\bigl[(i - 1)(M - 1) + j\bigr]
另外，若出现公式标号在公式下方如：
---
$$
{U}^{k + 1}\left\lbrack  {\left( {j - 1}\right) \left( {N - 1}\right)  + i}\right\rbrack   = {\widetilde{U}}^{k + 1}\left\lbrack  {\left( {i - 1}\right) \left( {M - 1}\right)  + j}\right\rbrack
$$
(3.44)
---
可以优化为
$$
U^{k+1}\bigl[(j - 1)(N - 1) + i\bigr] = \widetilde{U}^{k+1}\bigl[(i - 1)(M - 1) + j\bigr]\tag{3.44}
$$

2.算法重构
例2：
对于一些算法，原文的样式如下
Algorithm 11 Algorithm for simulating a VG process and log of stock price under VG

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
&\textbf{Algorithm 11: simulating a VG process and log of stock price under VG }\\[5pt]
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

3.表格转换

HTML转Markdown示例

<!-- Before -->
<table><tr><td>European call</td><td>$c(S,t) = ...$</td></tr></table>

↓

<!-- After -->
| Option        | Pricing Formula                          |
|---------------|------------------------------------------|
| European call | $c(S,t)=e^{-r(T-t)}\mathbb{E}[(S_T-K)^+]$|
```

4.代码优化
---

   tsplot(cbind(gtemp_land, gtemp_ocean), spaghetti=TRUE,

   	col=astsa.col(c(4,2),.7), pch=c(20,18), type="o", ylab="\\u00BOC",
   	
   	main="Global Surface Temperature Anomalies", addLegend=TRUE,
   	
   	location="topleft", legend=c("Land Surface","Sea Surface"))

---

   翻译过程中可以通过上下文或代码风格判断代码语言并规范化如下：

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


def process_stream(stream):
    """处理流式响应并返回完整响应"""
    full_response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
    return full_response


# 新增用于分段的函数
def split_content(content: str, max_length: int = 3000) -> List[str]:
    """使用 Segmente.py 中的 MarkdownSegmenter 进行文本分段"""
    from Segmente import MarkdownSegmenter
    segmenter = MarkdownSegmenter(max_length=max_length)
    return segmenter.segment(content)


async def translate_file(file_path: Path, api_key: str, semaphore: asyncio.Semaphore, file_type: str):
    """处理单个文件的异步函数"""
    async with semaphore:
        try:
            print(f"开始处理文件: {file_path.name}")
            
            client = OpenAI(
                base_url=BASE_URL,
                api_key=api_key
            )

            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 分段处理文本
            segments = split_content(content)
            print(f"文件 {file_path.name} 被分为 {len(segments)} 段")

            # 准备输出文件
            output_filename = file_path.stem + '.md'
            output_file = OUTPUT_DIR / output_filename
            
            # 清空输出文件
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("")
            
            # 维护最近k轮对话历史
            k = 5  # 保持最近5轮对话
            messages = []
            
            # 处理每个分段
            for i, segment in enumerate(segments, 1):
                max_retries = 5
                retry_count = 0
                
                while retry_count < max_retries:
                    try:
                        print(f"处理文件 {file_path.name} 的第 {i}/{len(segments)} 段...")
                        
                        # 构建当前对话消息
                        current_messages = [
                            {"role": "system", "content": sys_prompts[file_type]}
                        ]
                        
                        # 添加最近k轮历史对话
                        if messages:
                            current_messages.extend(messages[-2*k:])
                        
                        # 根据是否是第一段构建不同的提示词
                        prompt = "严格按照你的翻译要求，" + ("继续翻译以下文本，注意保持连贯：" if i > 1 else "翻译以下文本：")
                        user_message = {
                            "role": "user",
                            "content": f"{prompt}\n\n{segment}"
                        }
                        current_messages.append(user_message)

                        # 发送请求并获取完整响应
                        with ThreadPoolExecutor() as executor:
                            stream = await asyncio.get_event_loop().run_in_executor(
                                executor,
                                lambda: client.chat.completions.create(
                                    model='deepseek-ai/DeepSeek-R1',
                                    messages=current_messages,
                                    max_tokens=16384,
                                    temperature=0.4,
                                    top_p=0.85,
                                    stream=True,
                                    timeout=300
                                )
                            )
                            reply = await asyncio.get_event_loop().run_in_executor(
                                executor,
                                lambda: process_stream(stream)
                            )

                        # 翻译成功，将结果写入文件
                        with open(output_file, 'a', encoding='utf-8') as f:
                            f.write(reply)
                            if i < len(segments):  # 如果不是最后一段，添加分隔符
                                f.write('\n\n --- \n\n')

                        # 更新对话历史，同时保存用户提问和助手回复
                        messages.append(user_message)
                        messages.append({"role": "assistant", "content": reply})
                        
                        print(f"第 {i} 段翻译完成")
                        break
                        
                    except Exception as e:
                        retry_count += 1
                        print(f"第 {i} 段处理失败 (尝试 {retry_count}/{max_retries}):")
                        print(f"错误: {str(e)}")
                        if retry_count == max_retries:
                            print(f"段落 {i} 达到最大重试次数")
                            return False
                        await asyncio.sleep(5)

            print(f"文件 {file_path.name} 翻译完成")
            return True

        except Exception as e:
            print(f"文件 {file_path.name} 处理失败:")
            print(f"错误: {str(e)}")
            traceback.print_exc()
            return False


async def main():
    try:
        # 创建输出目录
        OUTPUT_DIR.mkdir(exist_ok=True)

        # 让用户选择文件类型
        while True:
            file_type = input("请选择要处理的文件类型 (1: markdown, 2: txt): ").strip()
            if file_type in ('1', '2'):
                break
            print("无效的选择，请重新输入")

        # 根据用户选择设置文件类型和文件匹配模式
        file_type_map = {'1': ('md', '*.md'), '2': ('txt', '*.txt')}
        file_type, glob_pattern = file_type_map[file_type]

        # 获取所有指定类型的文件
        files = list(WORK_DIR.glob(glob_pattern))
        if not files:
            print(f"workmd文件夹中没有找到{file_type}文件")
            return

        print(f"找到 {len(files)} 个{file_type}文件")

        # 创建信号量限制并发数
        semaphore = asyncio.Semaphore(len(API_KEYS))

        # 创建任务列表
        tasks = []
        for i, file_path in enumerate(files):
            api_key = API_KEYS[i % len(API_KEYS)]
            task = translate_file(file_path, api_key, semaphore, file_type)
            tasks.append(task)

        # 等待所有翻译任务完成
        results = await asyncio.gather(*tasks)

        # 统计成功和失败的数量
        success_count = sum(1 for r in results if r)
        fail_count = len(results) - success_count

        print(f"\n翻译任务完成:")
        print(f"成功: {success_count} 个文件")
        print(f"失败: {fail_count} 个文件")

    except Exception as e:
        print(f"发生未预期的错误: {str(e)}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"程序运行出错: {str(e)}")