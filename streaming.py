#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
streaming.py - 流式学术文档翻译处理器

功能：
- 智能分段处理大文件
- 多API负载均衡
- 上下文感知翻译
- 实时保存翻译结果

版本: 2.0.0
作者: Liu Jingkang
最后更新: 2024-02-24
创建日期: 2023-11-15
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
from ContentOptimizer import ContentOptimizer
from TranslationValidator import TranslationValidator
import time
import random
from enum import Enum


# 加载配置文件
load_dotenv()

# 硅基流动调用deepseek
MAIN_API_KEYS = os.getenv("MAIN_API_KEYS", "").split(",")
BACKUP_API_KEYS = os.getenv("BACKUP_API_KEYS", "").split(",")
ALL_API_KEYS = MAIN_API_KEYS + BACKUP_API_KEYS
BASE_URL = os.getenv("BASE_URL", "https://api.siliconflow.cn/v1/")



# 初始化文件夹路径
WORK_DIR = Path("workmd")
OUTPUT_DIR = Path("outputmd")


# 将prompts改为sys_prompts，仅作为系统提示词
sys_prompts = {
    "txt": r"""【强制要求】必须严格保持与原文的逐句对应，禁止任何形式的：
1. 内容添加/删减
2. 格式变更（公式符号、代码结构等）
3. 主观解释
4. 示例扩展
违者将导致后续翻译中断！

你现在是一个专业的学术翻译专家，专门负责将英文学术音频转写文本翻译成中文。

核心要求：
1. 完整性和准确性是首要任务
2. 逐字逐句翻译，不得省略或简化
3. 保持专业术语的准确性
4. 确保与上下文的翻译保持连贯性

翻译规范：
1. 使用中文全角标点，数学文本使用英文半角标点
2. 行内公式使用单美元符 $ $
3. 保留原有引用标注和格式""",

    "md": r"""【强制要求】必须严格保持与原文的逐句对应，禁止任何形式的：
1. 内容添加/删减  
2. 主观解释
3. 示例扩展
违者将导致后续翻译中断！

你现在是一个专业的学术翻译专家.
    翻译原则：逐字逐句、准确、专业翻译，确保翻译和原文一一对应。不额外生成其他内容。保持markdown内联latex的格式，公式块使用双美元符，双美元符公式块需要单独成行，行内公式使用单美元符。正文使用中文全角标点符号，数学文本中使用英文半角标点符号。插入图片的代码保持原状不要作任何改动。

翻译的细节要求:

1. 英文的长句翻译通常不会直接对应中文句式，你需要作出逻辑叙述的调整。
2. 为照顾汉语的习惯，采用一词两译的做法。例如"set"在汉语中有时译成"集合"有时译成"集"，单独使用时常译成"集合"，而在与其他词汇连用时则译成"集"（如可数集等）。
3. 汉语"是"通常有两种含义，一是"等于"，二是"属于"。在本书中"是"只表示等于的意思，而属于的意思则用"是一个"来表示。例如，不说"X是拓扑空间"，而说"X是一个拓扑空间"。
4. 在汉语中常难于区别单数和复数，而在英语的表达中又常常对于名词的复数形式与集合名词不加区别。对于这种情形，你需要宁可啰嗦一点，以保证不被误解

翻译过程中对原文本的优化：

````
1.公式优化
公式的表示可以更简洁，比如去掉不必要的花括号，使公式代码更易读。但同时确保只进行代码层面的调整，不能以任何程度修改原公式包括编号在内的所有数学含义，避免引入错误
例1：
{U}^{k + 1}\left\lbrack  {\left( {j - 1}\right) \left( {N - 1}\right)  + i}\right\rbrack   = {\widetilde{U}}^{k + 1}\left\lbrack  {\left( {i - 1}\right) \left( {M - 1}\right)  + j}\right\rbrack
可以重写为
U^{k+1}\bigl[(j - 1)(N - 1) + i\bigr] = \widetilde{U}^{k+1}\bigl[(i - 1)(M - 1) + j\bigr]
2.算法重构
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
翻译过程中碰到类似代码的语言（注意区别伪代码和代码，伪代码使用算法框），可以通过上下文或代码风格判断代码语言（这个示例是R语言，也可能是其他语言）并
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


class ErrorType(Enum):
    RATE_LIMIT = 1
    CONTENT_ERROR = 2
    OTHER = 3


async def translate_file(file_path: Path, initial_api_key: str, semaphore: asyncio.Semaphore, file_type: str):
    """处理单个文件的异步函数"""
    async with semaphore:
        try:
            current_api_key = initial_api_key
            api_pool = MAIN_API_KEYS.copy()  # 优先使用主API池
            random.shuffle(api_pool)  # 随机打乱主API顺序
            using_backup = False  # 标记是否正在使用备用API
            
            # 在循环外定义优化检测结果
            optimization_needed = False
            last_optimization_check = None
            
            print(f"\n[开始处理] 文件: {file_path.name}")
            print(f"   [API密钥] {current_api_key[:8]}...")
            
            client = OpenAI(
                base_url=BASE_URL,
                api_key=current_api_key
            )

            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 分段处理文本
            segments = split_content(content)
            print(f"\n📊 文件 {file_path.name} 分割完成")
            print(f"   📝 总段落数: {len(segments)}")

            # 准备输出文件
            output_filename = file_path.stem + '.md'
            output_file = OUTPUT_DIR / output_filename
            
            # 清空输出文件
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("")
            
            # 维护最近k轮对话历史
            k = 3
            messages = []
            
            # 初始化优化器和验证器
            optimizer = ContentOptimizer(api_key=current_api_key)
            validator = TranslationValidator(api_key=current_api_key)
            
            # 处理每个分段
            for i, segment in enumerate(segments, 1):
                max_retries = 5
                retry_count = 0
                validation_attempt = 0
                error_type = ErrorType.OTHER
                
                while retry_count < max_retries:
                    try:
                        # 优化检测只在首次尝试时执行
                        if retry_count == 0:
                            print("\n[优化检测] 执行内容优化分析...")
                            last_optimization_check = optimizer.check_optimization(segment)
                            optimization_needed = last_optimization_check["tag"]
                            print(f"   优化需求: {'需要' if optimization_needed else '不需要'}")

                        if optimization_needed:
                            print(f"   使用R1模型 (内容优化需求)")
                        else:
                            print(f"   使用V3模型 (标准模式)")

                        model_name = 'deepseek-ai/DeepSeek-R1' if optimization_needed or error_type != ErrorType.CONTENT_ERROR else 'deepseek-ai/DeepSeek-V3'
                        max_tokens = 16384 if optimization_needed else 4096
                        
                        # 发生错误时切换API密钥
                        if retry_count > 0:
                            current_api_key = api_pool[(api_pool.index(current_api_key) + 1) % len(api_pool)]
                            print(f"   🔄 切换API密钥至: {current_api_key[:8]}...")

                        # 重建客户端
                        client = OpenAI(
                            base_url=BASE_URL,
                            api_key=current_api_key
                        )

                        # 构建当前对话消息
                        current_messages = [
                            {"role": "system", "content": f"{sys_prompts[file_type]}"}
                        ]
                        
                        # 添加最近k轮历史对话（仅保留assistant回复）
                        if messages:
                            # 只取最后k条assistant回复
                            assistant_history = [msg for msg in messages[-k*2:] if msg["role"] == "assistant"]
                            current_messages.extend(assistant_history[-k:])  # 最多保留k条
                        
                        # 构建用户提示词
                        prompt = "严格遵循系统要求，" + ("继续翻译并保持格式一致：" if i > 1 else "准确翻译以下内容：")
                        user_message = {
                            "role": "user",
                            "content": f"{prompt}\n\n{segment}"
                        }
                        current_messages.append(user_message)

                        # API调用前输出
                        print("\n🚀 发起API请求...")
                        print(f"   📨 消息长度: {sum(len(m['content']) for m in current_messages)} 字符")

                        # API调用部分添加错误处理
                        try:
                            with ThreadPoolExecutor() as executor:
                                stream = await asyncio.get_event_loop().run_in_executor(
                                    executor,
                                    lambda: client.chat.completions.create(
                                        model=model_name,
                                        messages=current_messages,
                                        max_tokens=max_tokens,
                                        temperature=0.4,
                                        top_p=0.95,
                                        stream=True,
                                        timeout=300
                                    )
                                )
                                reply = await asyncio.get_event_loop().run_in_executor(executor, lambda: process_stream(stream))
                        except Exception as api_error:
                            if "rate limit" in str(api_error).lower():
                                error_type = ErrorType.RATE_LIMIT
                                # 从池中移除当前失效的API
                                if current_api_key in api_pool:
                                    api_pool.remove(current_api_key)
                                if not api_pool and not using_backup and BACKUP_API_KEYS:
                                    api_pool.extend(BACKUP_API_KEYS)
                                    using_backup = True
                                    print("   主API用尽，切换到备用API池")
                                if not api_pool:
                                    raise RuntimeError("所有API密钥均已耗尽")
                                # 添加指数退避
                                delay = min(2 ** retry_count, 30)
                                print(f"   ⏳ 速率限制，等待 {delay} 秒后重试...")
                                await asyncio.sleep(delay)
                                raise
                            else:
                                error_type = ErrorType.CONTENT_ERROR
                                raise

                        # 翻译验证输出
                        print("\n✅ 翻译完成，执行质量验证...")
                        validation_result = validator.validate(segment, reply)
                        if not validation_result["tag"]:
                            error_type = ErrorType.CONTENT_ERROR
                            raise ValueError(f"翻译验证失败: {validation_result['reason']}")
                        print("🟢 验证通过")
                        
                        # 翻译成功，将结果写入文件
                        with open(output_file, 'a', encoding='utf-8', errors='replace') as f:
                            f.write(reply)
                            if i < len(segments):  # 如果不是最后一段，添加分隔符
                                f.write('\n\n --- \n\n')

                        # 更新对话历史（滑动窗口机制）
                        messages = messages[-(k*2-2):]  # 保持历史长度
                        messages.append(user_message)
                        messages.append({"role": "assistant", "content": reply})
                        
                        print(f"第 {i} 段翻译完成")
                        break
                        
                    except Exception as e:
                        # 错误分类处理
                        if "rate limit" in str(e).lower():
                            error_type = ErrorType.RATE_LIMIT
                        elif "验证失败" in str(e):
                            error_type = ErrorType.CONTENT_ERROR
                        else:
                            error_type = ErrorType.OTHER

                        # 根据错误类型处理
                        if error_type == ErrorType.CONTENT_ERROR:
                            print(f"\n[验证失败] 尝试 {validation_attempt+1}/3")
                            print(f"   失败原因: {validation_result['reason']}")
                            print(f"   问题段落: {segment[:100]}...")  # 显示前100字符方便定位
                            validation_attempt += 1
                            if validation_attempt >= 3:
                                print(f"段落 {i} 验证失败超过3次，保留原文")
                                with open(output_file, 'a', encoding='utf-8', errors='replace') as f:
                                    f.write(segment)
                                break
                            
                            # 强制切换模型
                            model_name = 'deepseek-ai/DeepSeek-R1'
                            print(f"   🚨 切换至R1模型进行修复尝试")

                        retry_count += 1
                        if retry_count >= max_retries:
                            print(f"段落 {i} 达到最大重试次数")
                            break
                        
                        # 非速率限制错误添加随机延迟
                        if error_type != ErrorType.RATE_LIMIT:
                            delay = random.uniform(1, 3)
                            await asyncio.sleep(delay)

            # 文件处理完成输出
            print(f"\n🎉 文件 {file_path.name} 翻译完成")
            print(f"   📂 输出路径: {output_file}")
            return True

        except Exception as e:
            print(f"\n💥 文件处理失败: {file_path.name}")
            print(f"   最后错误: {str(e)}")
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
        semaphore = asyncio.Semaphore(len(ALL_API_KEYS) * 2)  # 每个API key允许2个并发

        # 创建任务列表
        tasks = []
        for i, file_path in enumerate(files):
            initial_api_key = ALL_API_KEYS[i % len(ALL_API_KEYS)]
            task = translate_file(file_path, initial_api_key, semaphore, file_type)
            tasks.append(task)

        # 等待所有翻译任务完成
        results = await asyncio.gather(*tasks)

        # 统计成功和失败的数量
        success_count = sum(1 for r in results if r)
        fail_count = len(results) - success_count

        # 添加并发设置输出
        print(f"\n⚙️ 系统设置")
        print(f"   🔑 可用API密钥数: {len(ALL_API_KEYS)}")
        print(f"   🚦 最大并发数: {len(ALL_API_KEYS)*2}")
        print(f"   📁 工作目录: {WORK_DIR}")
        print(f"   📂 输出目录: {OUTPUT_DIR}")

        print(f"\n📈 任务统计:")
        print(f"   ✅ 成功文件: {success_count}")
        print(f"   ❌ 失败文件: {fail_count}")
        print(f"   ⏱️ 总处理时间: {time.time()-start_time:.2f}秒")

    except Exception as e:
        print(f"发生未预期的错误: {str(e)}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"程序运行出错: {str(e)}")