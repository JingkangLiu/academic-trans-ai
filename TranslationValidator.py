#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TranslationValidator - 学术翻译验证器

功能：
- 验证中英翻译的逐句对应性
- 检测内容增减/格式变更
- 结构化输出验证结果

版本: 1.0.0
作者: Liu Jingkang
创建日期: 2025-03-15
许可证: MIT
"""
import re
from typing import Dict, Union
from openai import OpenAI
from openai.types.chat import ChatCompletion

class TranslationValidator:
    def __init__(self, 
                 api_key: str = "sk-enaitpvrgqtakfrhmncuaclpltlavwfepjqiljqgylzqwzgd",
                 base_url: str = "https://api.siliconflow.cn/v1/"):
        """
        初始化验证器
        
        :param api_key: API密钥，默认使用硅基流动
        :param base_url: API端点地址
        """
        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key
        )
        self.system_prompt = """你是一个专业的学术翻译质量评估专家，请严格检查以下翻译是否符合逐字逐句对应要求：

【强制格式要求】
+ 必须严格使用以下字典结构，包含且仅包含以下字段：
+ {
+   "tag": true/false,  // 是否通过验证
+   "reason": [         // 未通过原因列表（如果通过验证，则为null）
+   ]
+ }
+ 直接输出字典内容，不要包含任何代码块标记（如```）或额外说明

【验证标准】
1. 必须严格保持逐句对应，不允许出现任何内容遗漏，仅允许细微的排版层面的调整。
2. 禁止任何形式的内容删减,仅允许在原来的文本结构之外的添加了说明的补充或对原文可能的连续内容被截断缺失的补全。
3. 翻译过程中，允许对原文中的打字错误，运行按修正后翻译，并且不需要指出原文错误。

【验证步骤】
1. **段落结构对比**：确保每个段落中的句子与原文逐句对应，确认无误。
2. **信息完整性**：确保译文未删减原文信息、未无故添加内容，并且语义未发生偏移。
3. **公式和代码优化**：如果原文涉及数学公式或代码，允许优化其表示格式，如去除不必要的符号或括号，使其更简洁易读，除非原文出现错误，否则必须确保不改变原公式的数学含义。对于代码，允许对代码结构进行格式化优化（例如去除多余的空格或分行），但不得修改代码的语义或编程逻辑。
4. **不一致的地方的排查**：对于译文中与原文违背的地方，仔细判断是否是原文错误，如果是原文错误，则接受。
5. **算法部分优化**：对于涉及算法的内容，允许在不改变算法核心逻辑和步骤的情况下，优化表达格式。这包括：
   - 调整算法的排列结构，使其更加清晰易读（例如，将步骤按数字顺序排列、对齐变量等）。
   - 对输入输出部分进行适当格式化，使其更具可读性（如对"input" 和 "output"部分做适当的排版优化）。
   - 保持算法的数学表达式或逻辑顺序一致，避免修改算法的控制结构（如for、while等语句）或数学公式的核心内容。"""

        self.user_prompt_template = """请验证以下翻译，严格按指定字典格式返回结果（不要用代码块）：

[原文开始]
{original_text}
[原文结束]

[译文开始]
{translated_text}
[译文结束]"""

    def validate(self, original: str, translated: str, max_retries: int = 3) -> Dict[str, Union[bool, None, list]]:
        """
        执行翻译验证
        
        :param original: 英文原文
        :param translated: 中文译文
        :param max_retries: 最大重试次数
        :return: 验证结果字典
        """
        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            },
            {
                "role": "user",
                "content": self.user_prompt_template.format(
                    original_text=original,
                    translated_text=translated
                )
            }
        ]

        for attempt in range(max_retries):
            try:
                response: ChatCompletion = self.client.chat.completions.create(
                    model='deepseek-ai/DeepSeek-V3',
                    messages=messages,
                    temperature=0.1,
                    max_tokens=4096
                )

                raw_content = response.choices[0].message.content
                print('原始响应:', raw_content)
                
                # 直接使用正则表达式提取
                result = {
                    "tag": False,
                    "reason": self._extract_reasons(raw_content)
                }
                
                # 提取tag值
                tag_match = re.search(r'"tag"\s*:\s*(true|false)', raw_content, re.IGNORECASE)
                if tag_match:
                    result["tag"] = tag_match.group(1).lower() == "true"
                
                return result

            except Exception as e:
                if attempt == max_retries - 1:
                    return {"tag": False, "reason": [f"验证失败: {str(e)}"]}
                continue

        return {"tag": False, "reason": ["超过最大重试次数"]}

    def _extract_reasons(self, raw: str) -> list:
        """使用正则表达式直接提取原因列表"""
        reason_match = re.search(r'"reason"\s*:\s*\[(.*?)\]', raw, re.DOTALL)
        if not reason_match:
            return None
        
        # 提取带引号的内容项
        reasons = re.findall(r'"([^"]+)"', reason_match.group(1))
        return reasons if reasons else None

    def _validate_result_structure(self, result: dict) -> bool:
        """简化的结构验证"""
        return isinstance(result, dict) and "tag" in result and "reason" in result

# 使用示例
if __name__ == "__main__":
    validator = TranslationValidator()
    
    
    # 测试用例
    test_en = r'''
    Decomposing a swap into its constituent components is an interesting and insightful example of financial engineering that illustrates the special role played by simple forwards and options.

Here we will focus on a simple interest rate swap. In its simplest form, an interest rate swap between two counterparties is created as a result of the following steps: (a) counterparty A needs a $\$ 1$ million floating-rate loan, counterparty B needs a $\$ 1$ million fixed-rate loan. Because of market conditioned and their relationships with various banks, counterparty B has a comparative advantage in borrowing at a floating rate. Counterparties A and B decide to use this comparative advantage. Each borrows at the market where she had a comparative advantage, and then decides to exchange the interest payments. Counterparty A borrows $\$ 1$ million at fixed rate. The interest payments will be received from counterparty B and paid back to the lending bank. Counterparty B borrows \$1 million at the floating rate. Interest rate payments will be received from counterparty $\mathrm{A}$ and will be repaid to the lending bank.

Note that the initial sums, each being $\$ 1$ million, are identical. Therefore, they do not have to be exchanges. They are called notional principals. The interest payments are also in the same currency. Therefore, the counterparties exchange only the interest differentials. At the end both counterparties will secure lower rates and swap dealer will earn a fee.

Swap Rate in Terms of Forward Rates: a swap can be viewed as a portfolio of forward rate agreements (FRAs). Each cash flow is the cash flow of an FRA with fixed rate equal to the swap rate $s$ . Therefore, there is a no-arbitrage relation between the LIBOR curve and forward rates curve in LIBOR-based FRAs.

#### A.5.1 Terms and Payments

Most popular terms for (vanilla) swap rates are $2,5,{10}\& {30}$ years. For payments, there are two legs: (a) fixed leg and (b) floating leg. For the fixed leg, there are two semi-annual payments with fixed rate set a priori. For the floating leg, there are four quarterly payments, resetting quarterly, and 3M-LIBOR floating rate. Example 60 illustrates the cash flow analysis for a 2-year swap under a hypothetical rates.

Example 60 cash flow analysis of a 2-yr swap
'''
    test_zh = r'''
    将互换分解为其构成要素是金融工程中一个富有启发性的案例，展示了简单远期和期权所扮演的特殊角色。

此处我们重点讨论简单利率互换。其最基本形式下，两个交易对手间的利率互换通过以下步骤建立：
(a) 交易对手 A 需要 100 万美元浮动利率贷款，交易对手 B 需要 100 万美元固定利率贷款  
(b) 由于市场条件及与各银行关系，交易对手 B 在浮动利率借款方面具有比较优势  
(c) 双方决定利用此优势：各自在具有优势的市场借款后交换利息支付  

具体操作：

- 交易对手 A 以固定利率借入 100 万美元，利息支付将由 B 接收并偿还贷款银行  
- 交易对手 B 以浮动利率借入 100 万美元，利息支付将由 A 接收并偿还贷款银行  

注意到初始本金均为 100 万美元且币种相同，故无需交换本金（称为名义本金），仅需交换利差。最终双方均获得更低利率，互换交易商则赚取手续费。

**互换利率与远期利率关系**：互换可视作远期利率协议（FRA）组合，每笔现金流等价于固定利率为互换利率 $s$ 的 FRA 现金流。因此在基于 LIBOR 的 FRA 中，LIBOR 曲线与远期利率曲线间存在无套利关系。

#### A.5.1 条款与支付

（普通）互换利率最常见期限为 2 年、5 年、10 年及 30 年。支付结构包含两腿：
(a) **固定腿**：每半年支付一次，利率预先设定  
(b) **浮动腿**：每季度支付一次，利率挂钩 3 个月 LIBOR 浮动利率  

例 60 展示了假设利率下 2 年期互换的现金流分析。

**例 60**  2 年期互换现金流分析
'''

    print("验证结果：")
    print(validator.validate(test_en, test_zh))
    #print(validator.validate(r"In this appendix, we provide derivations of various rates discussed throughout the book", r"在附录中，我们提供了贯穿全书讨论的各种比率的推导。"))