#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ContentOptimizer - 内容优化检测器

功能：
- 检测文本是否需要算法重构/表格转换/代码优化
- 结构化输出检测结果

版本: 1.0.0
作者: Liu Jingkang
创建日期: 2025-03-20
许可证: MIT
"""
import json
from typing import Dict
from openai import OpenAI
from openai.types.chat import ChatCompletion

class ContentOptimizer:
    def __init__(self, 
                 api_key: str = "sk-enaitpvrgqtakfrhmncuaclpltlavwfepjqiljqgylzqwzgd",
                 base_url: str = "https://api.siliconflow.cn/v1/"):
        """
        初始化优化检测器
        
        :param api_key: API密钥
        :param base_url: API端点地址
        """
        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key
        )
        self.system_prompt = r"""你是一个专业的内容检测系统，请严格按以下要求判断：

【输出格式】
{"tag": true/false}

【检测标准】
你会收到一段学术markdown文本，其由pdf进行OCR识别后生成。当目前的文本涉及以下任意内容时，返回true，否则返回false
1. 算法：文本包含算法或者步骤（如未使用公式块规范的伪代码）或类似的片段
2. 表格：存在HTML表格或未格式化的表格数据
3. 代码：存文本存在代码片段或类似代码片段

【判断规则】
- 满足任意条件或不确定时即返回true
- 都不满足时返回false

【注意】
由于OCR的限制，文本中可以包括没能正确规范的算法、表格或代码，你需要判断PDF的原文是否涉及以上任意内容



"""

        self.user_prompt_template = """分析以下内容是否涉及：
        
[内容开始]
{content}
[内容结束]

只需返回严格JSON格式：{{"tag": boolean}}"""

    def check_optimization(self, content: str, max_retries: int = 3) -> Dict[str, bool]:
        """
        执行优化检测
        
        :param content: 待检测文本
        :param max_retries: 最大重试次数
        :return: 检测结果字典
        """
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": self.user_prompt_template.format(content=content)}
        ]

        for attempt in range(max_retries):
            try:
                response: ChatCompletion = self.client.chat.completions.create(
                    #model="deepseek-ai/DeepSeek-V3",
                    model="Qwen/Qwen2.5-72B-Instruct-128K",
                    messages=messages,
                    temperature=0.1,
                    max_tokens=1024,
                    response_format={"type": "json_object"}
                )

                result = json.loads(response.choices[0].message.content)
                if self._validate_result(result):
                    return result
                raise ValueError("Invalid response format")

            except Exception as e:
                if attempt == max_retries - 1:
                    return {"tag": False}
                continue

        return {"tag": False}

    def _validate_result(self, result: dict) -> bool:
        """验证结果结构有效性"""
        return isinstance(result, dict) and "tag" in result and isinstance(result["tag"], bool)

# 使用示例
if __name__ == "__main__":
    optimizer = ContentOptimizer()
    
    # 测试算法案例
    content = r'''
$$
{\gamma }_{x}\left( 0\right)  = \operatorname{var}\left( {x}_{t}\right)  = {\sigma }_{w}^{2}\frac{1}{\left( 1 - {\phi }^{2}\right) }.
$$

Thus, we must have $\left| \phi \right|  < 1$ for the process to have a positive (finite) variance. Similarly,

$$
{\gamma }_{x}\left( 1\right)  = \operatorname{cov}\left( {{x}_{t},{x}_{t - 1}}\right)  = \operatorname{cov}\left( {\phi {x}_{t - 1} + {w}_{t},{x}_{t - 1}}\right)
$$

$$
= \operatorname{cov}\left( {\phi {x}_{t - 1},{x}_{t - 1}}\right)  = \phi {\gamma }_{x}\left( 0\right) \text{.}
$$

Thus,

$$
{\rho }_{x}\left( 1\right)  = \frac{{\gamma }_{x}\left( 1\right) }{{\gamma }_{x}\left( 0\right) } = \phi ,
$$

and we see that $\phi$ is in fact a correlation, $\phi  = \operatorname{corr}\left( {{x}_{t},{x}_{t - 1}}\right)$ . To get to this point, we have made a crucial assumption of causality, as discussed below Definition 1.12; i.e., we assumed ${x}_{t - 1}$ does not depend on a future error, ${w}_{t}$ .



Now, iterate the model backward $k$ times,

$$
{x}_{t} = \phi {x}_{t - 1} + {w}_{t} = \phi \left( {\phi {x}_{t - 2} + {w}_{t - 1}}\right)  + {w}_{t}
$$

$$
= {\phi }^{2}{x}_{t - 2} + \phi {w}_{t - 1} + {w}_{t}
$$

$$
\vdots
$$

$$
= {\phi }^{k}{x}_{t - k} + \mathop{\sum }\limits_{{j = 0}}^{{k - 1}}{\phi }^{j}{w}_{t - j}.
$$

This method suggests that, by continuing to iterate backward, assuming ${x}_{t}$ is stationary and provided that $\left| \phi \right|  < 1$ , we can represent an $\mathrm{{AR}}\left( 1\right)$ model as a linear process given by ${}^{1}$

$$
{x}_{t} = \mathop{\sum }\limits_{{j = 0}}^{\infty }{\phi }^{j}{w}_{t - j}. \tag{3.7}
$$

Representation (3.7) is called the stationary solution of the model. In fact, by direct substitution of (3.7) into (3.6), we see that (3.7) is an AR(1) model,

$$
\underset{{x}_{t}}{\underbrace{\mathop{\sum }\limits_{{j = 0}}^{\infty }{\phi }^{j}{w}_{t - j}}} = \phi \left( \underset{{x}_{t - 1}}{\underbrace{\mathop{\sum }\limits_{{k = 0}}^{\infty }{\phi }^{k}{w}_{t - 1 - k}}}\right)  + {w}_{t}.
$$

The AR(1) process defined by (3.7) is stationary with mean

$$
\mathrm{E}\left( {x}_{t}\right)  = \mathop{\sum }\limits_{{j = 0}}^{\infty }{\phi }^{j}\mathrm{E}\left( {w}_{t - j}\right)  = 0,
$$

and autocovariance function,

$$
{\gamma }_{x}\left( h\right)  = \operatorname{cov}\left( {{x}_{t + h},{x}_{t}}\right)  = \mathrm{E}\left\lbrack  {\left( {\mathop{\sum }\limits_{{j = 0}}^{\infty }{\phi }^{j}{w}_{t + h - j}}\right) \left( {\mathop{\sum }\limits_{{k = 0}}^{\infty }{\phi }^{k}{w}_{t - k}}\right) }\right\rbrack
$$

$$
= \mathrm{E}\left\lbrack  {\left( {{w}_{t + h} + \cdots  + {\phi }^{h}{w}_{t} + {\phi }^{h + 1}{w}_{t - 1} + \cdots }\right) \left( {{w}_{t} + \phi {w}_{t - 1} + \cdots }\right) }\right\rbrack   \tag{3.8}
$$

$$
= {\sigma }_{w}^{2}\mathop{\sum }\limits_{{j = 0}}^{\infty }{\phi }^{h + j}{\phi }^{j} = {\sigma }_{w}^{2}{\phi }^{h}\mathop{\sum }\limits_{{j = 0}}^{\infty }{\phi }^{2j} = \frac{{\sigma }_{w}^{2}{\phi }^{h}}{1 - {\phi }^{2}},\;h \geq  0.
$$

From (3.8), the ACF of an AR(1) is

<<当前目标块>>
$$
{\rho }_{x}\left( h\right)  = \frac{{\gamma }_{x}\left( h\right) }{{\gamma }_{x}\left( 0\right) } = {\phi }^{h},\;h \geq  0, \tag{3.9}
$$

and ${\rho }_{x}\left( h\right)$ satisfies the recursion

$$
{\rho }_{x}\left( h\right)  = \phi {\rho }_{x}\left( {h - 1}\right) ,\;h = 1,2,\ldots . \tag{3.10}
$$

We will discuss the ACF of a general $\mathrm{{AR}}\left( p\right)$ model in Sect. 3.3.



---

${}^{1}$ Note that $\mathop{\lim }\limits_{{k \rightarrow  \infty }}\mathrm{E}{\left( {x}_{t} - \mathop{\sum }\limits_{{j = 0}}^{{k - 1}}{\phi }^{j}{w}_{t - j}\right) }^{2} = \mathop{\lim }\limits_{{k \rightarrow  \infty }}{\phi }^{2k}\mathrm{E}\left( {x}_{t - k}^{2}\right)  = 0$ , so (3.7) exists in the mean square sense (see Appendix A for a definition).

---

![0194db81-8b05-71d7-8d6f-c9a09f2962a0_104_203_195_1124_687_0.jpg](images/0194db81-8b05-71d7-8d6f-c9a09f2962a0_104_203_195_1124_687_0.jpg)

Fig. 3.1. Simulated $\mathrm{{AR}}\left( 1\right)$ series: $\phi  = {.9}$ (top); $\phi  =  - {.9}$ (bottom).

Example 3.2 The Sample Path of an AR(1) Process

Figure 3.1 shows a time plot of two $\mathrm{{AR}}\left( 1\right)$ processes, one with $\phi  = {.9}$ and one with $\phi  =  - {.9}$ ; in both cases, ${\sigma }_{w}^{2} = 1$ . In the first case, $\rho \left( h\right)  = {.9}^{h}$ , for $h \geq  0$ , so observations close together in time are positively correlated with each other. This result means that observations at contiguous time points will tend to be close in value to each other; this fact shows up in the top of Fig. 3.1 as a very smooth sample path for ${x}_{t}$ . Now, contrast this with the case in which $\phi  =  - {.9}$ , so that $\rho \left( h\right)  = {\left( -{.9}\right) }^{h}$ , for $h \geq  0$ . This result means that observations at contiguous time points are negatively correlated but observations two time points apart are positively correlated. This fact shows up in the bottom of Fig. 3.1, where, for example, if an observation, ${x}_{t}$ , is positive, the next observation, ${x}_{t + 1}$ , is typically negative, and the next observation, ${x}_{t + 2}$ , is typically positive. Thus, in this case, the sample path is very choppy.

Example 3.3 Explosive AR Models and Causality

For ${x}_{t} = \phi {x}_{t - 1} + {w}_{t}$ , we have discovered that if $\phi  =  \pm  1,{x}_{t}$ is not stationary, but if $\left| \phi \right|  < 1,{x}_{t}$ is stationary and not future dependent (Example 3.1). The obvious next question is if there is a stationary $\mathrm{{AR}}\left( 1\right)$ process with $\left| \phi \right|  > 1$ . Such processes are called explosive because the values of the time series quickly become large in magnitude. Clearly, because ${\left| \phi \right| }^{j}$ increases without bound as $j \rightarrow  \infty ,\mathop{\sum }\limits_{{j = 0}}^{{k - 1}}{\phi }^{j}{w}_{t - j}$ will not converge (in mean square) as $k \rightarrow  \infty$ , so the intuition used to get (3.7) will not work directly. We can, however, modify that argument to obtain a stationary model as follows. Write ${x}_{t + 1} = \phi {x}_{t} + {w}_{t + 1}$ , in which case,

$$
{x}_{t} = {\phi }^{-1}{x}_{t + 1} - {\phi }^{-1}{w}_{t + 1} = {\phi }^{-1}\left( {{\phi }^{-1}{x}_{t + 2} - {\phi }^{-1}{w}_{t + 2}}\right)  - {\phi }^{-1}{w}_{t + 1}
$$

$$
\vdots
$$

$$
= {\phi }^{-k}{x}_{t + k} - \mathop{\sum }\limits_{{j = 1}}^{k}{\phi }^{-j}{w}_{t + j}, p
$$

by iterating forward $k$ steps. Because ${\left| \phi \right| }^{-1} < 1$ , this result suggests the stationary future dependent $\mathrm{{AR}}\left( 1\right)$ model

$$
{x}_{t} =  - \mathop{\sum }\limits_{{j = 1}}^{\infty }{\phi }^{-j}{w}_{t + j} \tag{3.11}
$$

The reader can verify that this is stationary and of the $\mathrm{{AR}}\left( 1\right)$ form ${x}_{t} = \phi {x}_{t - 1} + {w}_{t}$ . Unfortunately, this model is useless because it requires us to know the future to be able to predict the future. When a process does not depend on the future, such as the $\mathrm{{AR}}\left( 1\right)$ when $\left| \phi \right|  < 1$ , we will say the process is causal. In the explosive case of this example, the process is stationary, but it is also future-dependent, and not causal.



Example 3.4 Every Explosion Has a Cause

Excluding explosive models from consideration is not a problem because the models have causal counterparts. For example, if

$$
{x}_{t} = \phi {x}_{t - 1} + {w}_{t}\;\text{ with }\;\left| \phi \right|  > 1
$$

and ${w}_{t} \sim$ iid $\mathrm{N}\left( {0,{\sigma }_{w}^{2}}\right)$ , then using (3.11), $\left\{  {x}_{t}\right\}$ is a non-causal stationary Gaussian process with $\mathrm{E}\left( {x}_{t}\right)  = 0$ and for $h \geq  0$ ,

$$
{\gamma }_{x}\left( h\right)  = \operatorname{cov}\left( {{x}_{t + h},{x}_{t}}\right)  = \operatorname{cov}\left( {-\mathop{\sum }\limits_{{j = 1}}^{\infty }{\phi }^{-j}{w}_{t + h + j}, - \mathop{\sum }\limits_{{k = 1}}^{\infty }{\phi }^{-k}{w}_{t + k}}\right)
$$

$$
= {\sigma }_{w}^{2}{\phi }^{-2}{\phi }^{-h}/\left( {1 - {\phi }^{-2}}\right) \text{.}
$$

Thus, using (3.8), the causal process defined by

$$
{y}_{t} = {\phi }^{-1}{y}_{t - 1} + {v}_{t}
$$

where ${v}_{t} \sim$ iid $\mathrm{N}\left( {0,{\sigma }_{w}^{2}{\phi }^{-2}}\right)$ is stochastically equal to the ${x}_{t}$ process (i.e., all finite distributions of the processes are the same).



For example, if

$$
{x}_{t} = 2{x}_{t - 1} + {w}_{t},\;{w}_{t}\overset{\text{ iid }}{ \sim  }\mathrm{N}\left( {0,{\sigma }_{w}^{2} = 1}\right) ,
$$

then

$$
{y}_{t} = \frac{1}{2}{y}_{t - 1} + {v}_{t},\;{v}_{t}\overset{\text{ iid }}{ \sim  }\mathrm{N}\left( {0,{\sigma }_{v}^{2} = \frac{1}{4}}\right)
$$

is an equivalent causal process (see Problem 3.3). This concept generalizes to higher orders, but it is easier to show using Chap. 4 techniques; see Example 4.10.



The technique of iterating backward to get an idea of the stationary solution of AR models works well when $p = 1$ , but not for larger orders. One technique is that of matching coefficients. Consider the $\mathrm{{AR}}\left( 1\right)$ model in operator form

$$
\phi \left( B\right) {x}_{t} = {w}_{t} \tag{3.12}
$$

where $\phi \left( B\right)  = 1 - {\phi B}$ , and $\left| \phi \right|  < 1$ . Also, write the model in equation (3.7) in operator form as

$$
{x}_{t} = \mathop{\sum }\limits_{{j = 0}}^{\infty }{\psi }_{j}{w}_{t - j} = \psi \left( B\right) {w}_{t}, \tag{3.13}
$$


'''
    print("算法案例检测结果:", optimizer.check_optimization(content))
