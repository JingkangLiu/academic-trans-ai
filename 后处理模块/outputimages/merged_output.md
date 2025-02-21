# 第一部分 定价与估值（传统）

## 第1章 随机过程与定价

衍生品定价的核心前提是标的资产（如股票、商品、利率或汇率）的变动遵循一个随机过程。

本章深入探讨了在不同市场中常用的随机过程来模拟资产价格。进一步讨论了基于这些资产的衍生合约的估值。在此过程中，我们将介绍对衍生品定价至关重要的计算技术，并评估这些技术在不同随机过程假设下的应用。作为基础知识，后续章节将回到这里阐述的原则。

我们的旅程从介绍期权及其合约开始。我们将探讨期权的必要性、内在定义以及最直观和视觉化的定价方法。随后，我们将深入回顾基本概率，重点关注其与随机过程特征函数构建的相互作用。通过这一点，我们将了解这些函数如何描绘出结果分布的矩，并详细介绍不同过程中特征函数的推导技术。特别强调与流行分布相关的特征函数。

接下来的部分展示了在衍生品定价领域中常用的随机过程的详尽集合。虽然列表很全面，但值得注意的是，并非所有实际应用中的随机过程都包括在内。对于每个过程，我们力求提供精确的数学表示，阐明可用的闭式特征函数和相关的随机微分方程（SDE）（如果存在的话）。

为了总结，本章概述了风险中性定价与测度变换概念的交织。当与描述标的资产随机演变的模型结合时，这些原则为本书中详细分析的衍生品定价算法奠定了基础。

### 1.1 期权概述

在本节中，我们将首先介绍期权，这是一种衍生证券。之所以称为“衍生”，是因为期权的价格是从另一种资产（称为标的资产）的价格派生出来的。期权主要有两种类型：看涨期权和看跌期权。

看涨期权，也称为普通或欧式看涨期权，赋予买方在到期时以事先确定的价格（称为执行价格）从卖方购买标的资产的权利（但不是义务）。如果买方选择行使期权，卖方有义务将标的资产出售给买方。买方在期权合约开始时支付一笔费用，称为期权费，以获得这一权利。看涨期权的收益由以下公式确定：

$$
\left( S_T - K \right)^+ = \max \left( S_T - K, 0 \right) \tag{1.1}
$$

这里，$K$ 表示执行价格，$S_T$ 表示到期时的股票价格。

普通或欧式看跌期权是一种衍生品，买方有权（但不是义务）在到期时以特定价格（称为执行价格）将标的资产出售给卖方。卖方有义务在买方行使期权时从买方处购买标的资产。买方在购买时支付一笔费用（期权费）以获得这一权利。看跌期权的收益由以下公式给出：

$$
\left( K - S_T \right)^+ = \max \left( K - S_T, 0 \right) \tag{1.2}
$$

从收益表达式来看，买方的激励与卖方的激励似乎相反。但这并不是那么简单，它取决于买方和卖方的立场。如果我们持有某公司的股票，并希望保护我们的头寸不受大幅下跌的影响，我们需要进行对冲。如果我们对某公司的股票走势有投机性判断，我们可能会购买期权。

如果期权的执行价格等于今天的股票价格，即即期价格，我们说这个期权是平值的。对于看跌/看涨期权，如果执行价格高于/低于即期价格，我们说这个期权是虚值的；如果执行价格低于/高于即期价格，我们说这个期权是实值的。虚值期权通常比实值期权更具有流动性，虚值期权的买卖价差也更小。

前美联储主席艾伦·格林斯潘曾对衍生品发表过这样的评论：“多年来，我们在市场上发现，衍生品是一个极其有用的工具，可以将风险从不应承担风险的人转移到愿意并且有能力承担风险的人。” 一般来说，期权合约的买方和卖方是套期保值者和投机者。套期保值者拥有标的资产。另一方面，投机者通常不拥有标的资产，而是对标的资产的未来走势进行投机。他们共同为市场提供流动性。

期权的价格由供求关系决定。这引发了一个问题，如果价格是由供求关系决定的，为什么我们还要费力开发随机过程和数学模型来定价衍生品？我们知道市场并不遵循任何数学模型，但就像任何其他物理现象一样，目标是找到能够模拟市场行为的模型或过程。通过这样做，可以推测不同执行价格和/或到期日的期权价格，并且还可以估算非普通或奇异型衍生品的价格，这将在其他章节中详细讨论。

欧洲或普通期权设计为只能在到期或到期日行使。然而，还有其他类型的期权可供选择。例如，百慕大期权可以在特定的预设时间行使，而美式期权可以在到期前的任何时间行使。此外，期权可以有各种类型的收益，如二元或数字期权，这取决于特定条件的满足。还有敲出期权，其收益取决于标的资产是否触及上或下障碍水平。还有一些期权，如亚式期权，其收益基于在监测时间点的标的资产水平的平均值，而不是到期时的标的资产水平，以及其他变体。以下是不同期权收益的几个例子：

$$
\text{- 欧式/普通看涨期权} - \left( S_T - K \right)^+
$$

$$
\text{- 欧式/普通看跌期权} - \left( K - S_T \right)^+
$$

- 数字看涨期权 $- \mathbb{1}_{\{ S_T > K \}}$

- 数字看跌期权 $- \mathbb{1}_{\{ S_T < K \}}$

- 上敲出看涨期权 $- \left( S_T - K \right)^+ \times \mathbb{1}_{\{ M_S < H \}}$，其中 $M_S = \max_{0 \leq t \leq T} S_t$ 且 $H$ 是一个上障碍

- 下敲出看跌期权 $- \left( K - S_T \right)^+ \times \mathbb{1}_{\{ m_S > L \}}$，其中 $m_S = \min_{0 \leq t \leq T} S_t$ 且 $L$ 是一个下障碍

- 平均看涨期权 $- \left( \frac{1}{m} \sum_{j = 1}^{m} S_{t_j} - K \right)^+$，监测时间点为 $0 < t_1 < \cdots < t_m = T$

- 平均看跌期权 $- \left( K - \frac{1}{m} \sum_{j = 1}^{m} S_{t_j} \right)^+$，监测时间点为 $0 < t_1 < \cdots < t_m = T$

- 美式看涨期权 $- \max_{0 < \tau < T} \left( S_\tau - K, 0 \right)$

- 美式看跌期权 $- \max_{0 < \tau < T} \left( K - S_\tau, 0 \right)$

#### 1.1.1 使用期权进行对冲：一个简单的示例

让我们从一个非常简单的例子开始，说明如何使用看跌期权来对冲大幅下跌的风险。假设你是一位投资者，持有X公司的股票。你相信公司的长期潜力，但担心短期内市场波动可能导致股价大幅下跌。为了保护你的投资，你决定使用看跌期权作为对冲。我们将考虑股价大幅下跌和股价保持稳定或上涨两种情景，并评估使用看跌期权对冲的优势。

示例1（对冲者示例）假设我们在投资组合中持有1,000股A公司的股票，每股价格为210美元。显然，今天投资组合的价值为210,000美元。表1.1展示了未来六个月的五种假设价格情景。这是没有任何对冲或保护措施的情况。为了对冲下行风险，可以购买看跌合约。通过购买看跌合约，投资者可以对冲其头寸，因为无论股价跌到多低，投资组合的价值都不会低于某个水平，如表1.2所示。在这种情况下，我们假设投资者购买了一个执行价格为190美元、六个月到期的看跌合约，并支付了7美元的期权费。我们将在稍后讨论期权费的价值和计算方法。从表中可以看出，无论股价跌到多低，投资组合的价值都不会低于183,000美元。

表1.1: 无任何对冲或保护措施的未来投资组合价值

| 情景 | 今天价格 | 未来价格 | 未来投资组合价值 |
|------|----------|----------|-----------------|
| 1    | 210美元  | 130美元  | 130,000美元     |
| 2    | 210美元  | 170美元  | 170,000美元     |
| 3    | 210美元  | 210美元  | 210,000美元     |
| 4    | 210美元  | 250美元  | 240,000美元     |
| 5    | 210美元  | 290美元  | 290,000美元     |

表1.2: 对冲者购买了6个月到期、执行价格为190美元的看跌期权，并支付了7美元的期权费

| 情景 | 今天价格 | 未来价格 | 收益 | 未来投资组合价值 |
|------|----------|----------|------|-----------------|
| 1    | 210美元  | 130美元  | 60,000美元 | 130,000 + 60,000 - 7,000 = 183,000美元 |
| 2    | 210美元  | 170美元  | 20,000美元 | 170,000 + 20,000 - 7,000 = 183,000美元 |
| 3    | 210美元  | 210美元  | 0    | 210,000 - 7,000 = 203,000美元 |
| 4    | 210美元  | 250美元  | 0    | 250,000 - 7,000 = 243,000美元 |
| 5    | 210美元  | 290美元  | 0    | 290,000 - 7,000 = 283,000美元 |

表1.3: 投机者以105美元购买了1000股ABC股票

| 情景 | 今天价格 | 未来价格 | 盈亏（P&L） |
|------|----------|----------|-------------|
| 1    | 105美元  | 75美元   | (75 - 105) × 1,000 = -30,000美元 |
| 2    | 105美元  | 90美元   | (90 - 105) × 1,000 = -15,000美元 |
| 3    | 105美元  | 105美元  | (105 - 105) × 1,000 = 0         |
| 4    | 105美元  | 120美元  | (125 - 105) × 1,000 = +15,000美元 |
| 5    | 105美元  | 135美元  | (135 - 105) × 1,000 = +30,000美元 |

表1.4: 投机者购买了10个执行价格为115美元的看涨期权，并支付了每份4美元的期权费

| 情景 | 今天价格 | 未来价格 | 收益 | 盈亏（P&L） |
|------|----------|----------|------|-------------|
| 1    | 105美元  | 75美元   | 0    | 0 - 4,000 = -4,000美元 |
| 2    | 105美元  | 90美元   | 0    | 0 - 4,000 = -4,000美元 |
| 3    | 105美元  | 105美元  | 0    | 0 - 4,000 = -4,000美元 |
| 4    | 105美元  | 120美元  | 5,000美元 | 5,000 - 4,000 = 1,000美元 |
| 5    | 105美元  | 135美元  | 20,000美元 | 20,000 - 4,000 = 16,000美元 |

示例2（投机者示例）现在我们考虑一个简单的投机者示例。假设一位投资组合经理推测ABC公司的股票价值将在几个月内上涨。她可以选择购买股票并持有，或者在不持有股票的情况下购买看涨期权。假设今天股票的价值为105美元。我们将比较以下两种情况的盈亏（P&L）：(a) 她以105美元购买1,000股公司股票，(b) 她购买10个看涨期权（每个期权对应100股），5个月到期，执行价格为115美元，并支付每份4美元的期权费。购买10个看涨期权相对于购买1,000股股票的最大损失较低，如表1.3和1.4所示。如果直接购买股票，盈亏将是5个月后的价格与今天价格之间的差额；如果购买期权，盈亏将是期权收益（如果有）与购买期权的成本之间的差额。

#### 1.1.2 期权定价的可视化方法

现在是时候问如何对期权进行定价了。让我们回到示例1，即对冲者示例。对于该示例，假设五种假设情景的概率相等；即，股票跌至130美元的概率为20%，股票跌至170美元的概率为20%，股票保持今天价值210美元的概率为20%，股票涨至250美元的概率为20%，最后，股票在6个月内跳涨至290美元的概率为20%。自然地，看跌期权的价值可以通过这些情景的收益的加权平均值来计算，即

$$
0.20 \times 60 + 0.20 \times 20 + 0.20 \times 0 + 0.20 \times 0 + 0.20 \times 0 = 16美元
$$

上述计算中缺少贴现。收益发生在到期日 $T$，但我们在寻找今天的期权价值，因此需要将其贴现回今天。目前我们假设零利率，稍后将在计算中引入贴现因子。

让我们考虑一个不同的情景，而不是假设等概率。现在我们假设股票下跌或下跌的概率显著低于股票上涨或跳涨的概率。这个情景如表1.6所示。在这种情况下，假设零利率，今天看跌期权收益的加权平均值为

$$
0.08 \times 60 + 0.11 \times 20 + 0.20 \times 0 + 0.35 \times 0 + 0.26 \times 0 = 7美元
$$

后一种情景是为了使计算出的期权费与对冲者示例中使用的期权费相匹配而制造的。假设 $m$ 个不同情景，每个情景的概率为 $p_i > 0$，其中 $i = 1, \ldots, m$ 且 $\sum_{i} p_i = 1$。设 $S_T^{(i)}$ 是以概率 $p_i$ 发生的到期日 $T$ 的股票价格。我们可以将看跌期权收益的加权平均值写为

$$
\sum_{i = 1}^{m} p_i \left( K - S_T^{(i)} \right)^+
$$

假设 $m$ 个不同情景过于简单且不现实。实际上，股票的未来价值 $S_T$ 是未知的，$S_T$ 可能有无限多种不同的值，因此我们将假设股票未来价值的连续概率分布，而不是迄今为止假设的离散情况。尽管如此，提供的离散示例提供了一个基础，可以帮助我们写出期权定价的表达式。

很容易看出，对于给定的执行价格，标的资产价格如何影响期权价格。对于看涨期权，随着标的资产价格的增加/减少，期权价格也增加/减少，因为收益上升/下降。对于看跌期权，情况相反，随着标的资产价格的增加/减少，期权价格减少/增加，因为收益下降/上升。这与模型选择无关，只是收益变化的幅度与模型规范和参数有关。这将在其他章节中讨论。表1.7总结了这种关系。

表1.7: 股票价格与期权价格之间的关系

| 股票价格 | 看涨价格 | 看跌价格 |
|----------|----------|----------|
| ↑        | ↑        | ↓        |
| ↓        | ↓        | ↑        |

在定价之前，我们应该考虑在众多连续分布函数中，哪一个是最合适的。当我们观察市场价格时，我们可能能够找到一个模型或过程，通过调整其参数，我们可以使模型价格与市场价格紧密匹配，这就是校准的本质。这一程序将在第9章和第10章中详细讨论。

此时，我们希望以可视化的方式来看待定价，而不涉及任何模型/过程的规范。假设我们有两模型来模拟股票价格的演变。在第一个模型中，股票在达到时间 $T$ 之前缓慢上下波动，没有任何跳跃。而在第二个模型中，股票不断上下跳跃，主要是较小的跳跃，但也可能有一些较大的跳跃我们不知道这两个模型的任何细节，但假设可以轻松地通过时间模拟股票价格的演变。图1.1显示了这两个模型的模拟路径，即爬行模型与跳跃模型。很容易通过肉眼观察到两种模拟路径之间的差异。对于每个模拟路径，终点相同，即即期价格和到期日 $T$，可以将这些终点分箱，并构建一个经验（条件）分布。在图1.2中，我们展示了这两个模型的条件概率分布。可以看出，具有跳跃的模型具有更胖的尾部分布。最后，在图1.3中，我们将这两个分布与看涨和看跌期权的收益绘制在一起。很容易观察到，在更大的区域内，跳跃模型对看涨和看跌期权的收益都有暴露。这将在计算期权费时再次讨论。

<img src="./images/0195247f-2f23-7bdd-9335-9204d62fe613_30_196_1495_1226_523_0.jpg" alt="0195247f-2f23-7bdd-9335-9204d62fe613_30_196_1495_1226_523_0.jpg" style="zoom:50%;" />

图1.1: 爬行模型与跳跃模型的股票价格模拟路径

<img src="./images/0195247f-2f23-7bdd-9335-9204d62fe613_31_441_155_742_542_0.jpg" alt="0195247f-2f23-7bdd-9335-9204d62fe613_31_441_155_742_542_0.jpg" style="zoom:50%;" />

图1.2: 爬行模型与跳跃模型的概率分布

<img src="./images/0195247f-2f23-7bdd-9335-9204d62fe613_31_175_818_1291_544_0.jpg" alt="0195247f-2f23-7bdd-9335-9204d62fe613_31_175_818_1291_544_0.jpg" style="zoom:50%;" />

图1.3: 看涨和看跌期权的收益与条件分布的对比

回到期权定价，如前所述，可以通过计算加权平均收益并将其贴现回今天的值来获得。我们需要知道到期时间 $T$ 时的股票价格 $S_T$。我们所知道的是时间 $t = 0$ 时的即期价格或当前价格，即 $S_0$。此时，我们不假设任何股票价格演变过程，而是假设给定今天的股票价格 $S_0$ 时 $S_T$ 的分布；我们称之为（条件）概率分布函数，即 $f(S_T \mid S_0)$。看涨期权费的数学公式如下：

$$
C_0(K, T) = e^{-rT} \mathbb{E}_0 \left[ \left( S_T - K \right)^+ \right]= e^{-rT} \int_{0}^{\infty} \left( S_T - K \right)^+ f(S_T \mid S_0) dS_T= e^{-rT} \int_{K}^{\infty} \left( S_T - K \right) f(S_T \mid S_0) dS_T
$$

注意贴现因子 $e^{-rT}$。由于收益发生在时间 $T$，而我们在寻找时间 $t = 0$ 时的价格，因此必须通过乘以贴现因子 $e^{-rT}$ 将积分贴现回时间 $t = 0$，其中 $r$ 是无风险利率。还需注意，加权平均收益是在给定分布下的期望值。对于看跌期权，我们可以数学地写为：

$$
P_0(K, T) = e^{-rT} \mathbb{E}_0 \left[ \left( K - S_T \right)^+ \right]= e^{-rT} \int_{0}^{\infty} \left( K - S_T \right)^+ f(S_T \mid S_0) dS_T= e^{-rT} \int_{0}^{K} \left( K - S_T \right) f(S_T \mid S_0) dS_T
$$

<img src="./images/0195247f-2f23-7bdd-9335-9204d62fe613_32_131_177_1322_533_0.jpg" alt="0195247f-2f23-7bdd-9335-9204d62fe613_32_131_177_1322_533_0.jpg" style="zoom:50%;" />

图1.4: 看涨期权收益与条件pdf的对比

<img src="./images/0195247f-2f23-7bdd-9335-9204d62fe613_32_128_836_1322_536_0.jpg" alt="0195247f-2f23-7bdd-9335-9204d62fe613_32_128_836_1322_536_0.jpg" style="zoom:50%;" />

图1.5: 看跌期权收益与条件pdf的对比

在图1.4中，我们将看涨期权的收益与 $f(S_T \mid S_0)$ 对比。如果我们用条件分布乘以收益并进行积分，我们将得到平均收益。对于看跌期权，我们做同样的事情，如图1.5所示。从图1.4和1.5的右图中，我们可以看到如何评估欧式期权的价格。对于看涨期权，我们首先将其转换为一个定积分，选择一个上限 $B$。上限 $B$ 是看涨期权的两个超参数之一，选择方式使得被舍弃的积分值非常小。

$$
C_0(K, T) = e^{-rT} \int_{K}^{\infty} \left( S_T - K \right) f(S_T) dS_T\approx e^{-rT} \int_{K}^{B} \left( S_T - K \right) f(S_T) dS_T \tag{1.3}
$$

然后，我们将 $N$（另一个超参数）设置为长度为 $\eta$ 的等分区间，其中

$$
\eta = \frac{B - K}{N}
$$

网格点设置为

$$
s_j = K + (j - 1) \eta \text{ for } j = 1, \ldots, N + 1
$$

通过构造，上限将是 $B = s_{N + 1} = K + N\eta$。

重写1.3，我们得到

$$
C_0(K, T) \approx e^{-rT} \sum_{j = 1}^{N} \int_{s_j}^{s_{j + 1}} \left( S_T - K \right) f(S_T) dS_T
$$

使用梯形法则可以近似每个子积分并将其相加

$$
\int_{s_j}^{s_{j + 1}} \left( S_T - K \right) f(S_T) dS_T \approx \frac{\eta}{2} \left( \left( s_j - K \right) f(s_j) + \left( s_{j + 1} - K \right) f(s_{j + 1}) \right)
$$

代入以得到

$$
C_0(K, T) \approx e^{-rT} \sum_{j = 1}^{N} \int_{s_j}^{s_{j + 1}} \left( S_T - K \right) f(S_T) dS_T\approx e^{-rT} \sum_{j = 1}^{N} \frac{\eta}{2} \left( \left( s_j - K \right) f(s_j) + \left( s_{j + 1} - K \right) f(s_{j + 1}) \right)
\\
= e^{-rT} \frac{\eta}{2} \left( \left( s_1 - K \right) f(s_1) + \left( s_2 - K \right) f(s_2) + \left( s_2 - K \right) f(s_2) + \left( s_3 - K \right) f(s_3) + \cdots \right.
\\
\left. + \left( s_{N - 1} - K \right) f(s_{N - 1}) + \left( s_N - K \right) f(s_N) + \left( s_N - K \right) f(s_N) + \left( s_{N + 1} - K \right) f(s_{N + 1}) \right)
\\
= e^{-rT} \left( \frac{\eta}{2} \left( s_1 - K \right) f(s_1) + \eta \left( \left( s_2 - K \right) f(s_2) + \cdots + \left( s_N - K \right) f(s_N) \right) \right)\left. + \frac{\eta}{2} \left( s_{N + 1} - K \right) f(s_{N + 1}) \right)
$$

我们注意到，除了第一项和最后一项，系数将是 $\eta$。进一步假设函数 $f(s_{N + 1})$ 是不显著的，我们将其舍去，并写出近似的看涨期权公式

$$
C_0(K, T) \approx e^{-rT} \sum_{j = 1}^{N} \left( s_j - K \right) f(s_j \mid S_0) w_j
$$

其中

$$
w_j = \left\{ \begin{matrix} \frac{1}{2}\eta & j = 1 \\ \eta & \text{ otherwise } \end{matrix} \right.
$$

<img src="./images/0195247f-2f23-7bdd-9335-9204d62fe613_34_379_235_819_624_0.jpg" alt="0195247f-2f23-7bdd-9335-9204d62fe613_34_379_235_819_624_0.jpg" style="zoom:50%;" />

图1.6: 不同即期价格下的对数正态分布

知道需要 $N$ 个函数值，这种方法的计算成本为 O(N)。对于看跌期权，另一方面，上限是已知的，即 $K$，只需选择 $N$ 并设置 $\eta = \frac{K}{N}$。网格点为

$$
s_j = (j - 1) \eta \text{ for } j = 1, \ldots, N + 1
$$

遵循相同的程序，看跌期权的近似值为

$$
P_0(K, T) \approx e^{-rT} \sum_{j = 1}^{N} \left( K - s_j \right) f(s_j \mid S_0) w_j
$$

其中

$$
w_j = \left\{ \begin{matrix} \frac{1}{2}\eta & j = 1 \\ \eta & \text{ otherwise } \end{matrix} \right.
$$

其计算成本为 O(N)，与看涨期权相同。

示例3（对数正态分布）我们假设条件概率分布是对数正态分布。对数正态分布由以下公式给出：

$$
f(S_T \mid S_0) = \frac{e^{-\frac{1}{2} \left( \frac{\ln S_T - \ln S_0 - \left( r - q - \frac{\sigma^2}{2} \right) T}{\sigma \sqrt{T}} \right)^2}}{\sigma S_T \sqrt{2\pi T}}
$$

在图1.6中，我们展示了不同即期价格下的对数正态分布，如图例所示。对于这个示例，我们假设以下参数：即期价格 $S_0 = 100美元$，无风险利率 $r = 5\%$，股息率 $q = 1\%$，到期日 $T = 1$ 年，波动率 $\sigma = 30\%$，执行价格 $K = 140美元$。

表1.8: 执行价格为 $K = 140美元$（虚值）时，不同 $\eta$ 和 $N$ 值下的看涨期权价格

| $N$ | $\eta$ 0.25 | $\eta$ 0.5 | $\eta$ 1.0 |
|-----|-------------|------------|------------|
| $2^8$ | 2.2247      | 2.8446     | 2.9130     |
| $2^9$ | 2.8450      | 2.9133     | 2.9136     |
| $2^{10}$ | 2.9134     | 2.9139     | 2.9136     |
| $2^{11}$ | 2.9140     | 2.9139     | 2.9136     |
| $2^{12}$ | 2.9140     | 2.9139     | 2.9136     |
| $2^{13}$ | 2.9140     | 2.9139     | 2.9136     |

表1.9: 执行价格为 $K = 140美元$（实值）时，不同 $N$ 值下的看跌期权价格

| $N$ | 隐含 $\eta$ | | 看跌期权费 |
|-----|-------------|---|------------|
| $2^8$ | 0.546       | | 37.0810    |
| $2^9$ | 0.273       | | 37.0811    |
| $2^{10}$ | 0.136      | | 37.0811    |
| $2^{11}$ | 0.068      | | 37.0811    |
| $2^{12}$ | 0.034      | | 37.0811    |
| $2^{13}$ | 0.017      | | 37.0811    |

让我们通过询问这种近似有多好来评估这种方法。似乎对于适当的 $N$ 和 $\eta$ 选择，这种近似实际上相当好，但考虑到通常 $f(S_T \mid S_0)$ 无法以积分形式获得，这种方法在实际中是可行的。在接下来的章节中，我们将介绍定价衍生品的替代方法和更通用的方法。

图1.4和1.5可视化了期权的定价。在第2章、第3章和第4章中，我们将学习期权定价的通用方程以及如何数值求解这些方程。在第6章中，我们将使用蒙特卡洛模拟来求解这些方程。在第9章和第10章中，我们将使用校准和估计来获取这些方程中参数的值。

#### 1.1.3 看涨-看跌期权平价

为了说明看涨-看跌期权平价如何工作，我们简单地从具有相同执行价格的看涨期权收益中减去看跌期权收益，得到

$$
\left( S_T - K \right)^+ - \left( K - S_T \right)^+ = S_T - K
$$

通过取期望值并贴现回今天，即乘以 $e^{-rT}$，我们得到其今天的值

$$
\left( S_T - K \right)^+ - \left( K - S_T \right)^+ = S_T - K
$$

$$
e^{-rT} \mathbb{E}_0 \left( \left( S_T - K \right)^+ \right) - e^{-rT} \mathbb{E}_0 \left( \left( K - S_T \right)^+ \right) = e^{-rT} \mathbb{E}_0 \left( S_T \right) - e^{-rT} K
$$

$$
C_0(K, T) - P_0(K, T) = S_0 - e^{-rT} K
$$

简而言之，具有相同执行价格的看涨期权和看跌期权价格之间的差异等于今天的即期价格减去贴现后的执行价格，这种关系称为看涨-看跌期权平价。

$$
C_0(K, T) - P_0(K, T) = S_0 - e^{-rT} K
$$

实际上，由于市场摩擦和交易成本，这种关系并不总是成立的，但同时它应该在市场买卖价差内成立，否则市场中将存在套利机会。


---

### 1.2 特征函数

本节提供了一个关于分布或过程的特征函数的基本回顾。这些概念将在本章中我们推导随机过程的特征函数时变得至关重要。

定义 1 傅里叶变换和逆傅里叶变换

对于函数 $f\left( x\right)$ ，其傅里叶变换定义为

$$
\Phi \left( \nu \right)  = {\int }_{-\infty }^{\infty }{e}^{i\nu x}f\left( x\right) {dx} \tag{1.4}
$$

其中 $i = \sqrt{-1}$ 是虚数单位。已知一个函数的傅里叶变换 $\Phi \left( \nu \right)$ ，该函数 $f\left( x\right)$ 可以通过逆傅里叶变换恢复

$$
f\left( x\right)  = \frac{1}{2\pi }{\int }_{-\infty }^{\infty }{e}^{-{i\nu x}}\Phi \left( \nu \right) {d\nu } \tag{1.5}
$$

定义 2 特征函数

如果 $f\left( x\right)$ 是一个随机变量 $X$ 的概率密度函数 (PDF)，其傅里叶变换被称为特征函数

$$
\Phi \left( \nu \right)  = {\int }_{-\infty }^{\infty }{e}^{i\nu x}f\left( x\right) {dx} \tag{1.6}
$$

$$
= \mathbb{E}\left( {e}^{i\nu X}\right)  \tag{1.7}
$$

并且，如前所述，其概率密度函数 $f\left( x\right)$ 可以通过逆傅里叶变换从其特征函数中恢复。

#### 1.2.1 通过特征函数计算累积分布函数

如上所述，PDF 可以从特征函数中恢复。通过积分 PDF，我们可以恢复累积分布函数 (CDF)。因此，已知特征函数 $\Phi \left( u\right)  = {\int }_{-\infty }^{+\infty }{e}^{iux}f\left( x\right) {dx}$ ，概率密度函数 $f\left( x\right)$ 可以通过逆 $\Phi \left( u\right)$ 来计算。

$$
f\left( x\right)  = \frac{1}{2\pi }{\int }_{-\infty }^{+\infty }{e}^{-{iux}}\Phi \left( u\right) {du}
$$

累积分布函数 $F\left( x\right)$ 可以计算为：

$$
F\left( x\right)  = {\int }_{-\infty }^{x}f\left( \eta \right) {d\eta }= \frac{1}{2\pi }{\int }_{-\infty }^{x}{\int }_{-\infty }^{\infty }{e}^{-{iu\eta }}\Phi \left( u\right) {dud\eta }
$$

然而，在大多数情况下，PDF 无法以解析形式或封闭形式恢复。因此，恢复 CDF 通常需要对 PDF 的参数形式进行数值积分。我们更希望直接从特征函数 $\Phi \left( u\right)$ 恢复累积分布函数 $F\left( x\right)$ ，以避免两次进行数值积分。为此，我们不直接使用傅里叶变换，因为这会导致不收敛${}^{1}$，而是使用 ${e}^{-{\alpha x}}F\left( x\right)$ 的傅里叶变换，其中 ${e}^{-{\alpha x}}$ 是一个衰减因子，且 $\alpha  > 0$ 。

$$
{\int }_{-\infty }^{+\infty }{e}^{iux}{e}^{-{\alpha x}}F\left( x\right) {dx} = {\int }_{-\infty }^{+\infty }{e}^{-\left( {\alpha  - {iu}}\right) x}F\left( x\right) {dx}
$$

对 ${\int }_{-\infty }^{+\infty }{e}^{-\left( {\alpha  - {iu}}\right) x}F\left( x\right) {dx}$ 使用分部积分，并注意到第一项消失，我们得到

$$
{\int }_{-\infty }^{+\infty }{e}^{-\left( {\alpha  - {iu}}\right) x}F\left( x\right) {dx} = \frac{1}{\alpha  - {iu}}{\int }_{-\infty }^{+\infty }{e}^{-\left( {\alpha  - {iu}}\right) x}f\left( x\right) {dx}= \frac{1}{\alpha  - {iu}}{\int }_{-\infty }^{+\infty }{e}^{i\left( {u + {i\alpha }}\right) x}f\left( x\right) {dx}= \frac{1}{\alpha  - {iu}}\Phi \left( {u + {i\alpha }}\right)
$$

因此

$$
{\int }_{-\infty }^{+\infty }{e}^{iux}\overline{{e}^{-{\alpha x}}F\left( x\right) }{dx} = \frac{1}{\alpha  - {iu}}\Phi \left( {u + {i\alpha }}\right)
$$

使用傅里叶逆变换，我们得到

$$
{e}^{-{\alpha x}}F\left( x\right)  = \frac{1}{2\pi }{\int }_{-\infty }^{\infty }{e}^{-{iux}}\frac{1}{\alpha  - {iu}}\Phi \left( {u + {i\alpha }}\right) {du}
$$

或者等价地

$$
F\left( x\right)  = \frac{1}{2\pi }{e}^{\alpha x}{\int }_{-\infty }^{\infty }{e}^{-{iux}}\frac{1}{\alpha  - {iu}}\Phi \left( {u + {i\alpha }}\right) {du}
$$

因此，我们可以直接从特征函数中通过一次数值积分恢复累积分布函数。

#### 1.2.2 通过特征函数计算随机变量的矩

概率分布的特征函数的另一个有用性质是，它允许我们恢复该分布的任意数量的矩。

---

${}^{1}$ 不收敛的问题将在第 2 章中讨论。

---

定义 3 (矩) 矩用于描述函数图形的形状。概率函数的一阶矩是其均值，二阶矩是其方差，三阶矩是其偏度，四阶矩是其峰度 [255]。

假设我们有一个随机变量 $X$ 的特征函数

$$
\phi \left( u\right)  = \mathbb{E}\left\lbrack  {e}^{iuX}\right\rbrack  \tag{1.8}
$$

很容易看出 $\phi \left( u\right)$ 的 ${n}^{th}$ 阶导数由下式给出

$$
{\phi }^{\left( n\right) }\left( u\right)  = \mathbb{E}\left\lbrack  {{\left( iX\right) }^{n}{e}^{iuX}}\right\rbrack  \tag{1.9}
$$

为了找到其矩，将 $u$ 替换为零，得到

$$
{\phi }^{\left( n\right) }\left( 0\right)  = \mathbb{E}\left\lbrack  {{\left( iX\right) }^{n}{e}^{i\left( 0\right) X}}\right\rbrack= \mathbb{E}\left\lbrack  {\left( iX\right) }^{n}\right\rbrack= {i}^{n}\mathbb{E}\left\lbrack  {X}^{n}\right\rbrack
$$

因此

$$
\mathbb{E}\left\lbrack  {X}^{n}\right\rbrack  = {i}^{-n}{\phi }^{\left( n\right) }\left( 0\right)  \tag{1.10}
$$

例如，$X$ 的一阶矩，即 $X$ 的均值，为

$$
\mathbb{E}\left\lbrack  X\right\rbrack  =  - i{\phi }^{\prime }\left( 0\right)
$$

#### 1.2.3 去均值随机变量的特征函数

假设对于一个随机变量 $X$，其特征函数已知并给出。如果我们感兴趣于找到去均值随机变量的特征函数，即 $Y = X - \mathbb{E}\left\lbrack  X\right\rbrack$，可以使用 1.2.2 节的结果如下进行：

$$
E\left\lbrack  {e}^{iuY}\right\rbrack  = E\left\lbrack  {e}^{{iu}\left( {X - E\left\lbrack  X\right\rbrack  }\right) }\right\rbrack= E\left\lbrack  {e}^{{iu}\left( {X + i{\phi }^{\prime }\left( 0\right) }\right) }\right\rbrack= {e}^{-u{\phi }^{\prime }\left( 0\right) }E\left\lbrack  {e}^{iuX}\right\rbrack= {e}^{-u{\phi }^{\prime }\left( 0\right) }\phi \left( u\right)
$$

#### 1.2.4 计算詹森不等式的校正

我们通常可以使用以下几何定律表达标的资产价格过程 ${S}_{t}$ 的演化：

$$
{S}_{t} = {S}_{0}{e}^{\left( {r - q}\right) t + {\omega t} + {X}_{t}}
$$

其中 $r - q$ 是在风险中性测度下资产的平均收益率，${X}_{t}$ 是标的资产收益的随机过程，该过程可能遵循本章讨论的任何随机过程。我们假设已知过程的特征函数 $\phi \left( u\right)  = \mathbb{E}\left( {e}^{{iu}{X}_{t}}\right)$。最后一项 $\omega$ 是所谓的詹森不等式校正，以确保在风险中性测度下资产的平均收益率为 $r - q$。正如下一章将要展示的，在衍生品定价的几乎所有应用中，我们需要标的资产过程对数的特征函数，而不是标的资产过程本身的特征函数。使用以下推导，我们可以得到 $\omega$ 并计算标的资产过程对数的特征函数：

$$
\Psi \left( u\right)  = \mathbb{E}\left( {e}^{{iu}\ln {S}_{t}}\right)= \mathbb{E}\left( {e}^{{iu}\left( {\ln {S}_{0} + \left( {r - q}\right) t + {\omega t} + {X}_{t}}\right) }\right)= {e}^{{iu}\left( {\ln {S}_{0} + \left( {r - q}\right) t + {\omega t}}\right) }\mathbb{E}\left( {e}^{{iu}{X}_{t}}\right)= {e}^{{iu}\left( {\ln {S}_{0} + \left( {r - q}\right) t + {\omega t}}\right) }\phi \left( u\right)
$$

将 $- i$ 替换为 $u$，我们得到

$$
\mathbb{E}\left( {S}_{t}\right)  = {S}_{0}{e}^{\left( {r - q}\right) t}{e}^{\omega t}\phi \left( {-i}\right) .
$$

已知在风险中性测度下

$$
\mathbb{E}\left( {S}_{t}\right)  = {S}_{0}{e}^{\left( {r - q}\right) t}
$$

比较两个方程，我们得到

$$
{e}^{\omega t}\phi \left( {-i}\right)  = 1
$$

或者等价地

$$
\omega  =  - \frac{1}{t}\ln \left( {\phi \left( {-i}\right) }\right)
$$

以及标的资产过程对数的特征函数

$$
\Psi \left( u\right)  = \mathbb{E}\left( {e}^{{iu}\ln {S}_{t}}\right)= {e}^{{iu}\left( {\ln {S}_{0} + \left( {r - q}\right) t}\right) }\frac{\phi \left( u\right) }{\phi \left( {-i}\right) }
$$

#### 1.2.5 计算鞅的对数的特征函数

假设随机变量 ${M}_{t}$ 在某个概率测度下是一个鞅${}^{2}$，我们希望找到 ${M}_{t}$ 的对数在该测度下的特征函数，即 $\Psi \left( u\right)  = \mathbb{E}\left( {e}^{{iu}\ln {M}_{t}}\right)$。观察到，如果我们将 $- i$ 替换为 $u$，我们得到：

$$
\Psi \left( {-i}\right)  = \mathbb{E}\left( {e}^{i\left( {-i}\right) \ln {M}_{t}}\right)= \mathbb{E}\left( {M}_{t}\right)= {M}_{0} \tag{1.11}
$$

设 $\ln {M}_{t} = {N}_{t} + {A}_{t}$，其中 ${A}_{t}$ 和 ${N}_{t}$ 分别是过程的确定性和随机成分。假设过程的随机成分已知，但确定性成分的确切表达式未知，这是通常的情况。此外，我们假设随机成分的特征函数

$$
{\Phi }_{N}\left( u\right)  = \mathbb{E}\left( {e}^{{iu}{N}_{t}}\right)
$$

---

${}^{2}$ 这意味着其未来值的条件期望等于其当前值，而与先前的值无关。

---

是已知的。我们可以如下推导确定性成分：

$$
\Psi \left( u\right)  = \mathbb{E}\left( {e}^{{iu}\ln {M}_{t}}\right)= \mathbb{E}\left( {e}^{{iu}{N}_{t} + {iu}{A}_{t}}\right)= {e}^{{iu}{A}_{t}}\mathbb{E}\left( {e}^{{iu}{N}_{t}}\right)= {e}^{{iu}{A}_{t}}{\Phi }_{N}\left( u\right)
$$

其中 ${\Phi }_{N}\left( u\right)$ 是 ${N}_{t}$ 的特征函数。在 $\Psi \left( u\right)$ 中将 $- i$ 替换为 $u$，我们得到

$$
\Psi \left( {-i}\right)  = {e}^{{A}_{t}}{\Phi }_{N}\left( {-i}\right)  \tag{1.12}
$$

因此 (1.11) 和 (1.12) 意味着

$$
{M}_{0} = {\Phi }_{N}\left( {-i}\right) {e}^{{A}_{t}}
$$

解 ${A}_{t}$，我们得到

$$
{A}_{t} = \ln \frac{{M}_{0}}{{\Phi }_{N}\left( {-i}\right) }
$$

将 ${A}_{t}$ 代入，我们最终得到 ${M}_{t}$ 的对数的特征函数的表达式：

$$
\mathbb{E}\left( {e}^{{iu}\ln {M}_{t}}\right)  = {\Phi }_{N}\left( u\right) {e}^{{iu}{A}_{t}}= {\Phi }_{N}\left( u\right) {\left( \frac{{M}_{0}}{{\Phi }_{N}\left( {-i}\right) }\right) }^{iu}
$$

#### 1.2.6 指数分布

均值为 $\lambda$ 的指数分布是速率参数为 $\frac{1}{\lambda }$ 的泊松过程之间的跳跃时间的分布。它具有以下概率分布函数：

$$
f\left( x\right)  = \lambda {e}^{-{\lambda x}},\;x \geq  0 \tag{1.13}
$$

以及累积分布函数：

$$
F\left( x\right)  = 1 - {e}^{-{\lambda x}},\;x \geq  0 \tag{1.14}
$$

其特征函数为

$$
\phi \left( u\right)  = \mathbb{E}\left( {e}^{iuX}\right)= {\int }_{0}^{\infty }{e}^{iux}\lambda {e}^{-{\lambda x}}{dx}
$$

这是一个复积分，如 [155] 所述，其解依赖于如何在 ${\mathbb{R}}^{2}$ 上积分轮廓。通过将 ${e}^{iux}$ 写作

$$
{e}^{iux} = \cos \left( {ux}\right)  + i\sin \left( {ux}\right)  \tag{1.15}
$$

并分别积分实部和虚部${}^{3}$，我们可以得到特征函数的以下表达式：

$$
\phi \left( u\right)  = \frac{\lambda }{\lambda  - {iu}}
$$

如 [155] 所述，即使在这种情况下，将 $i$ 视为实数的不当方法也会得出正确的答案，但不应陷入这种陷阱。

---

${}^{3}$ 推导的详细内容见附录 D.1。

---

#### 1.2.7 泊松分布

随机变量 $x \in  {\mathbb{N}}^{ + }$ 如果满足以下条件，则具有泊松分布：

$$
f\left( x\right)  = {e}^{-\lambda }\frac{{\lambda }^{x}}{x!}
$$

泊松随机变量的均值和方差分别为 $\mathbb{E}\left( X\right)  = \lambda$ 和 $\operatorname{var}\left( X\right)  = \lambda$。

#### 1.2.8 伽玛分布

伽玛随机变量具有以下概率分布函数：

$$
f\left( x\right)  = \frac{1}{\Gamma \left( \alpha \right) {\beta }^{\alpha }}{x}^{\alpha  - 1}{e}^{-\frac{x}{\beta }}
$$

其中 $\alpha$ 是形状参数，$\beta$ 是尺度参数，我们将其记为 $x \sim$ 伽玛 $\left( {\alpha ,\beta }\right)$。伽玛过程的特征函数可以通过评估以下复积分得到：

$$
\phi \left( u\right)  = \mathbb{E}\left( {e}^{iux}\right)  = {\int }_{0}^{\infty }{e}^{iux}\frac{1}{\Gamma \left( \alpha \right) {\beta }^{\alpha }}{x}^{\alpha  - 1}{e}^{-\frac{x}{\beta }}{dx}
$$

对于伽玛分布，常规的复分析方法 [155] 得出

$$
\phi \left( u\right)  = {\left( \frac{1}{1 - {iu\beta }}\right) }^{\alpha } \tag{1.16}
$$

这与指数分布的结果相似，这并不令人惊讶，因为如果 $\alpha$ 是整数，则伽玛 $\left( {\alpha ,\beta }\right)$ 表示 $\alpha$ 个独立的指数随机变量的和，每个变量的均值为 $\beta$，即速率参数为 $\frac{1}{\beta }$。

#### 1.2.9 卡方分布

卡方分布 ${\chi }^{2}\left( d\right)$ 实际上是伽玛分布的一个特例，即伽玛 $\left( {\frac{1}{2}d,2}\right)$，因此其特征函数可以从前面的结果中轻松推导。

$$
\phi \left( u\right)  = {\left( \frac{1}{1 - {2iu}}\right) }^{d/2} \tag{1.17}
$$

#### 1.2.10 标准正态分布

金融领域中最重要的分布之一是标准正态分布，均值为零，标准差为一，我们将其记为 $\mathcal{N}\left( {0,1}\right)$。它是扩散过程${}^{4}$的主要组成部分，因此在我们将要讨论的大多数模型中占据核心地位。如果 $Z \sim  \mathcal{N}\left( {0,1}\right)$，则其特征函数计算如下：

$$
{\Phi }_{Z}\left( \nu \right)  = \mathbb{E}\left( {e}^{i\nu Z}\right)  = {\int }_{-\infty }^{\infty }\frac{1}{\sqrt{2\pi }}\exp \left( {{i\nu z} - \frac{1}{2}{z}^{2}}\right) {dz}
$$

---

${}^{4}$ 在概率论和统计学中，扩散过程是一类具有几乎确定连续样本路径的连续时间马尔可夫过程。我们使用某种扩散过程来模拟标的资产的演化，该过程没有跳跃。

---

根据 [155] 中的论点，我们考虑以下积分：

$$
\mathbb{E}\left( {e}^{sZ}\right)  = {\int }_{-\infty }^{\infty }\frac{1}{\sqrt{2\pi }}\exp \left( {{sz} - \frac{1}{2}{z}^{2}}\right) {dz}
$$

在被积函数中完成平方

$$
{\int }_{-\infty }^{\infty }\frac{1}{\sqrt{2\pi }}\exp \left( {{sz} - \frac{1}{2}{z}^{2}}\right) {dz} = {\int }_{-\infty }^{\infty }\frac{1}{\sqrt{2\pi }}\exp \left( {-\frac{1}{2}\left( {{z}^{2} - {2sz}}\right) }\right) {dz}
\\
= {\int }_{-\infty }^{\infty }\frac{1}{\sqrt{2\pi }}\exp \left( {-\frac{1}{2}{\left( z - s\right) }^{2} + \frac{1}{2}{s}^{2}}\right) {dz}= \frac{1}{\sqrt{2\pi }}{e}^{\frac{1}{2}{s}^{2}}{\int }_{-\infty }^{\infty }\exp \left( {-\frac{1}{2}{\left( z - s\right) }^{2}}\right) {dz}
$$

利用

$$
{\int }_{-\infty }^{\infty }{e}^{-\frac{1}{2}{u}^{2}{du}} = \sqrt{2\pi }
$$

我们得到

$$
\mathbb{E}\left( {e}^{sZ}\right)  = \exp \left( \frac{{s}^{2}}{2}\right)
$$

如 [155] 所述，通过复变量函数的解析延拓理论，我们可以将 ${i\nu }$ 替换为 $s$，得到

$$
{\Phi }_{Z}\left( \nu \right)  = \mathbb{E}\left( {e}^{i\nu Z}\right)  = {e}^{-\frac{{\nu }^{2}}{2}}
$$

#### 1.2.11 正态分布

均值为 $\mu$，标准差为 $\sigma$ 的正态随机变量可以通过从标准正态变量构造得到，只需设置 $X = \mu  + {\sigma Z}$，使得 $X \sim  \mathcal{N}\left( {\mu ,{\sigma }^{2}}\right)$。因此，其特征函数可以如下推导：

$$
{\Phi }_{X}\left( \nu \right)  = \mathbb{E}\left( {e}^{i\nu X}\right)= \mathbb{E}\left( {e}^{{i\nu }\left( {\mu  + {\sigma Z}}\right) }\right)= {e}^{i\nu \mu }\mathbb{E}\left( {e}^{i\nu \sigma Z}\right)= {e}^{i\nu \mu }{e}^{-\frac{{\left( \sigma \nu \right) }^{2}}{2}}= {e}^{{i\mu \nu } - \frac{{\sigma }^{2}{\nu }^{2}}{2}}
$$

布朗运动 ${W}_{t}$ 是许多资产价格模型的关键组成部分。我们知道

$$
{W}_{t} - {W}_{0} = {W}_{t} \sim  \mathcal{N}\left( {0, t}\right)
$$

因此，如果 ${X}_{t} = {W}_{t}$，其特征函数为

$$
\mathbb{E}\left( {e}^{{i\nu }{X}_{t}}\right)  = \mathbb{E}\left( {e}^{{i\nu }{W}_{t}}\right)  = \mathbb{E}\left( {e}^{{i\nu }\sqrt{t}Z}\right)  = {e}^{-\frac{{\nu }^{2}t}{2}} \tag{1.18}
$$

#### 1.2.12 莱维过程

基于莱维过程的金融模型在描述资产收益的厚尾和匹配期权市场中的隐含波动率${}^{5}$曲面方面，比扩散模型表现更好，因为莱维过程不仅考虑了高斯运动，还考虑了跳跃。一些例子${}^{6}$包括方差伽玛 (VG) 模型 [236]、正态逆高斯 (NIG) 模型 [29]、温控稳定过程（也称为 CGMY 模型 [59]）、默顿跳跃扩散模型 [239] 和库双指数跳跃扩散模型 [217]。

莱维过程类包括所有具有平稳独立增量的随机过程 [265]。莱维-辛钦定理 [191] 提供了莱维过程的特征，通过描述底层过程的特征。该定理指出，存在一个测度 $\nu$，使得对于所有 $u \in  \mathbb{R}$ 和非负 $t$，莱维过程的特征函数可以写为：

$$
\mathbb{E}\left( {e}^{{iz}{X}_{t}}\right)  = {e}^{{t\phi }\left( z\right) } \tag{1.19}
$$

其中

$$
\phi \left( z\right)  = {i\gamma z} - \frac{{\sigma }^{2}{z}^{2}}{2} + {\int }_{-\infty }^{\infty }\left( {{e}^{izx} - 1 - {izx}{\mathbb{1}}_{\left| x\right|  \leq  1}}\right) {d\nu }\left( x\right)  \tag{1.20}
$$

其中 $\sigma$ 是非负的，$\gamma  \in  \mathbb{R}$，且 $\nu$ 是一个在 $\mathbb{R}$ 上的测度，满足 $\nu \left( 0\right)  = 0$ 且

$$
{\int }_{-\infty }^{\infty }\min \left( {1,{x}^{2}}\right) {d\nu }\left( x\right)
$$

是有界的。

根据莱维-辛钦定理，过程 ${\left\{  {X}_{t}\right\}  }_{t \geq  0}$ 完全由其特征成分确定

$$
\psi \left( u\right)  =  - \frac{{s}^{2}}{2}{u}^{2} + {i\gamma u} + {\int }_{\mathbb{R}}\left( {{e}^{iuy} - 1 - {iuy}{1}_{\left| y\right|  \leq  1}}\right) m\left( {dy}\right)
$$

满足 $\mathbb{E}\left( {e}^{{iu}{X}_{t}}\right)  = {e}^{{t\psi }\left( u\right) }$。这里 $s \geq  0$ 和 $\gamma$ 是实常数。莱维测度 $m$ 是一个在 $\mathbb{R}$ 上的正测度，满足 ${\int }_{\mathbb{R}}\min \left( {1,{y}^{2}}\right) m\left( {dy}\right)  < \infty$。

如果 $m$ 满足 ${\int }_{\left| y\right|  > 1}\left| y\right| m\left( {dy}\right)  < \infty$，特征成分可以写为

$$
\psi \left( u\right)  =  - \frac{{s}^{2}}{2}{u}^{2} + i\widetilde{\gamma }u + {\int }_{\mathbb{R}}\left( {{e}^{iuy} - 1 - {iuy}}\right) m\left( {dy}\right)
$$

其中 $\widetilde{\gamma } = \gamma  + {\int }_{\left| y\right|  > 1}{ym}\left( {dy}\right)$。

在以下例子中，莱维测度 $m$ 具有密度，即 $m\left( {dy}\right)  = k\left( y\right) {dy}$，其中 $k\left( y\right)$ 称为莱维密度。

此外，在风险中性的股票价格过程 (5.1) 中，${X}_{t} + {\omega t}$ 也是一个莱维过程。其特征函数为

$$
\mathbb{E}\left( {e}^{{iu}\left( {{X}_{t} + {\omega t}}\right) }\right)  = {e}^{{t\psi }\left( u\right)  - \psi \left( {-i}\right) {uit}}
$$

其特征成分为

$$
\widetilde{\psi }\left( u\right)  = \psi \left( u\right)  - \psi \left( {-i}\right) {ui}=  - \frac{{s}^{2}}{2}{u}^{2} + {\int }_{\mathbb{R}}\left( {{e}^{iuy} - 1 - {iuy}}\right) m\left( {dy}\right)  - \left( {\frac{{s}^{2}}{2} + {\int }_{\mathbb{R}}\left( {{e}^{y} - 1 - y}\right) m\left( {dy}\right) }\right) {ui}
$$

---

${}^{5}$ 隐含波动率是指使模型价格与市场报价相匹配的波动率。

${}^{6}$ 本书后续将详细探讨这些模型。

---

我们可以看到，在 $\psi \left( u\right)$ 中的 $\widetilde{\gamma }$ 在 $\widetilde{\psi }\left( u\right)$ 中被抵消，对风险中性的股票价格过程 ${S}_{t}$ 没有影响。因此，在例子中将省略 $\widetilde{\gamma }$。

### 1.3 利率的随机模型

在随机模型领域，我们将这些模型分为两大类：均值回归模型和趋势跟随模型。通常，市场如利率、货币汇率和商品价格表现出均值回归行为，即值倾向于随时间回归到长期平均值。因此，用于这些市场的随机模型预计会捕捉这种均值回归特性。我们的讨论从 Black-Derman-Toy (BDT) 模型开始，追溯其发展及其对市场动态的适应。

对于某些模型，我们将提供非常简要的高级概述，而对于其他模型，我们将深入探讨其细节，如存在的话的封闭形式解、特征函数等，因为它们是本书的基础概念。我们将在第 9 章中重新讨论这些模型。

#### 1.3.1 Black-Derman-Toy (BDT) 模型

Black-Derman-Toy (BDT) 模型 [36] 是一个对数正态二叉利率过程。在连续时间中，可以证明 BDT 可以写为：

$$
d\ln \left( {r}_{t}\right)  = \left( {\theta \left( t\right)  + \frac{{\sigma }^{\prime }\left( t\right) }{\sigma \left( t\right) }\ln \left( {r}_{t}\right) }\right) {dt} + \sigma \left( t\right) d{W}_{t} \tag{1.21}
$$

其中 ${r}_{t}$ 是时间 $t$ 的短期利率，$\theta \left( t\right)$ 是短期利率的漂移，$\sigma \left( t\right)$ 是短期利率波动性的期限结构。为了显示均值回归，波动性应随时间下降，即 ${\sigma }^{\prime }\left( t\right)  < 0$。

#### 1.3.2 Black-Karasinski (BK) 模型

Black-Karasinski 模型 [37] 给出如下：

$$
d\ln \left( {r}_{t}\right)  = \kappa \left( t\right) \left( {\theta \left( t\right)  - \ln \left( {r}_{t}\right) }\right) {dt} + \sigma \left( t\right) d{W}_{t} \tag{1.22}
$$

Black-Karasinski 模型通过指定短期利率的中心趋势及其回归到该中心趋势的速度，明确地建模均值回归。Black-Karasinski 模型的随机微分方程 (SDE) 通过数值方法求解。

对于像 BDT 和 BK 这样的对数正态模型，存在一个问题，即短期衍生品在长期债券上的定价，树状结构必须在整个标的资产的生命周期内构建，而不是在衍生品的生命周期内构建。

#### 1.3.3 奥恩斯坦-乌伦贝克过程

奥恩斯坦-乌伦贝克 (OU) 过程是一个高斯过程的实例，该过程具有有界的方差并允许平稳的概率分布，与维纳过程不同。两者之间的区别在于它们的漂移项。对于维纳过程，漂移项是常数，而对于 OU 过程，漂移项依赖于过程的当前值：如果过程的当前值小于（长期）均值，漂移将为正；如果过程的当前值大于（长期）均值，漂移将为负。换句话说，均值充当过程的平衡水平。这赋予了过程均值回归的特性。奥恩斯坦-乌伦贝克 (OU) 过程是一个流行的模型，被从业者用作基准模型。

##### 1.3.3.1 奥恩斯坦-乌伦贝克过程 - 随机微分方程

奥恩斯坦-乌伦贝克 (OU) 过程是一个随机过程 ${r}_{t}$，可以通过以下随机微分方程描述：

$$
d{x}_{t} = \kappa \left( {\eta  - {x}_{t}}\right) {dt} + {\lambda d}{W}_{t}
$$

其中 $\kappa  > 0,\eta$ 和 $\lambda  > 0$ 是模型参数，${W}_{t}$ 表示维纳过程。

参数 $\eta$ 代表由基本面支持的均衡或均值，$\lambda$ 是由于冲击导致的围绕均值的波动程度，$\kappa$ 是这些冲击消散的速度以及变量回归到均值的速度。

##### 1.3.3.2 瓦西克模型

金融领域中最古老且最直接应用的 OU 过程是瓦西克模型。在这个模型下，瞬时现货利率（短期利率）遵循 OU 过程。

$$
d{r}_{t} = \kappa \left( {\eta  - {r}_{t}}\right) {dt} + {\lambda d}{W}_{t}
$$

该模型的优势在于，与几何布朗运动不同，短期利率围绕一个长期均值波动，这与市场利率的历史表现一致。这导致长期方差是有界的，这也是利率市场的实证特征；市场利率很少会呈指数增长到非常高的水平。使用该过程建模利率的缺点是它允许短期利率变为负值，这种情况在市场中很少见。

应用伊藤引理到 ${r}_{t}{e}^{\kappa t}$，我们可以解随机微分方程得到：

$$
{r}_{t} = {r}_{0}{e}^{-{\kappa t}} + \eta \left( {1 - {e}^{-{\kappa t}}}\right)  + \lambda {e}^{-{\kappa t}}{\int }_{0}^{t}{e}^{\kappa s}d{W}_{s} \tag{1.23}
$$

在大多数情况下，我们最感兴趣的通常是随机变量或其对数的特征函数，而在建模瞬时利率时，过程在时间上的积分是最关键的组成部分。如果 $r\left( t\right)$ 是瞬时利率，则实现的利率由 $R\left( t\right)$ 给出，其中

$$
R\left( t\right)  = {\int }_{0}^{t}r\left( u\right) {du}.
$$

可以证明 ${R}_{t} \sim  \mathcal{N}\left( {\mu ,{\sigma }^{2}}\right)$，其中

$$
\mu  = \frac{\eta  - {r}_{0}}{\kappa }\left( {{e}^{-{\kappa t}} - 1}\right)  + {\eta t}
$$

$$
{\sigma }^{2} = \frac{{\lambda }^{2}}{2{\kappa }^{2}}\left( {\frac{4{e}^{-{\kappa t}} - {e}^{-{2\kappa t}} - 3}{2\kappa } + t}\right)
$$

我们知道正态随机变量 $\mathcal{N}\left( {\mu ,{\sigma }^{2}}\right)$ 的特征函数为

$$
\phi \left( u\right)  = \mathbb{E}\left( {e}^{{iu}{X}_{t}}\right)  \tag{1.24}
$$

$$
= {e}^{{i\mu u} - \frac{{\sigma }^{2}{u}^{2}}{2}} \tag{1.25}
$$

将 $\mu$ 和 $\sigma$ 代入上述方程，我们得到 $R\left( t\right)$ 的特征函数为

$$
\mathbb{E}\left( {e}^{{iuR}\left( t\right) }\right)  = {e}^{A\left( {t, u}\right)  - B\left( {t, u}\right) r\left( 0\right) }
$$

其中

$$
A\left( {t, u}\right)  = \left( {\eta  + \frac{{\lambda }^{2}}{2{\kappa }^{2}}{iu}}\right) \left( {B\left( {t, u}\right)  + {iut}}\right)  - \frac{{\lambda }^{2}}{4\kappa }{B}^{2}\left( {t, u}\right)
$$

$$
B\left( {t, u}\right)  = \left( \frac{{e}^{-{\kappa t}} - 1}{\kappa }\right) {iu}
$$

如果我们感兴趣于计算瓦西克模型中的债券价格期限结构 $P\left( {0, T}\right)$，我们可以使用

$$
P\left( {0, T}\right)  = \mathbb{E}\left( {e}^{-{\int }_{0}^{T}{r}_{u}{du}}\right)  = \mathbb{E}\left( {e}^{-R\left( T\right) }\right)  \tag{1.26}
$$

这可以通过在特征函数中将 $- i$ 替换为 $u$ 得到。方程 (1.26) 可以很容易地扩展为计算：

$$
P\left( {t, T}\right)  = {\mathbb{E}}_{t}\left( {e}^{-{\int }_{t}^{T}{r}_{u}{du}}\right)
$$

##### 1.3.3.3 扩展的瓦西克模型

扩展的瓦西克模型是瓦西克模型的一个简单扩展，具体如下：

$$
d{r}_{t} = \left( {\theta \left( t\right)  - a\left( t\right) {r}_{t}}\right) {dt} + \sigma \left( t\right) d{W}_{t} \tag{1.27}
$$

这是一个正态模型，$\theta \left( t\right)$ 允许精确拟合当前的即期利率曲线，可以尝试每个期权的不同 $a$ 和 $\sigma$ 值，或者为所有期权使用一个共同的 $a$ 值但不同的 $\sigma$ 值，任何一种方法都可以精确匹配所有期权价格。

#### 1.3.4 Cox-Ingersoll-Ross 模型

Cox-Ingersoll-Ross (CIR) 模型是瓦西克模型的一个修改版本，旨在保持其所有优势的同时防止短期利率变为负值。为此，在 SDE 的波动项中添加了一个 $\sqrt{{r}_{t}}$ 项。这导致当过程接近零时，波动性也趋于零，从而防止过程产生负利率。

##### 1.3.4.1 随机微分方程

因此，描述 CIR 模型的随机微分方程如下：

$$
d{r}_{t} = \kappa \left( {\eta  - {r}_{t}}\right) {dt} + \lambda \sqrt{{r}_{t}}d{W}_{t}
$$

其中 $W\left( t\right)$ 是在风险中性测度 $\mathbb{Q}$ 下的布朗运动，$\eta$ 是长期利率，$\kappa$ 是均值回归的速度，$\lambda$ 是短期利率的波动性。

##### 1.3.4.2 实现利率的特征函数

与瓦西克模型一样，我们对实现的利率 $R\left( t\right)$ 的特征函数感兴趣，其中

$$
R\left( t\right)  = {\int }_{0}^{t}r\left( u\right) {du}.
$$

可以证明 $R\left( t\right)$ 的特征函数为

$$
\mathbb{E}\left( {e}^{{iuR}\left( t\right) }\right)  = \phi \left( {u, t, r\left( 0\right) ,\kappa ,\eta ,\lambda }\right)= A\left( {t, u}\right) {e}^{B\left( {t, u}\right) r\left( 0\right) }
$$

其中

$$
A\left( {t, u}\right)  = \frac{\exp \left( \frac{{\kappa }^{2}{\eta t}}{{\lambda }^{2}}\right) }{{\left( \cosh \left( \gamma t/2\right)  + \frac{\kappa }{\gamma }\sinh \left( \gamma t/2\right) \right) }^{{2\kappa \eta }/{\lambda }^{2}}}
$$

$$
B\left( {t, u}\right)  = \frac{2iu}{\kappa  + \gamma \coth \left( {{\gamma t}/2}\right) }
$$

其中

$$
\gamma  = \sqrt{{\kappa }^{2} - 2{\lambda }^{2}{iu}}
$$

与瓦西克模型一样，如果我们感兴趣于计算 CIR 模型中的债券价格期限结构，我们可以使用

$$
P\left( {0, T}\right)  = \mathbb{E}\left( {e}^{-{\int }_{0}^{T}{r}_{u}{du}}\right)  = \mathbb{E}\left( {e}^{-R\left( T\right) }\right)  \tag{1.28}
$$

并通过在特征函数中将 $- i$ 替换为 $u$ 来计算。如前所述，方程 (1.28) 可以很容易地扩展为

$$
P\left( {t, T}\right)  = {\mathbb{E}}_{t}\left( {e}^{-{\int }_{t}^{T}{r}_{u}{du}}\right)
$$

#### 1.3.5 Heath-Jarrow-Morton (HJM) 模型

瞬时远期利率的演化模型是由 Heath, Jarrow 和 Morton 引入的，这类模型被称为远期利率模型或 HJM 模型。HJM 模型描述了远期利率的演化形式如下：

$$
{df}\left( {t, s}\right)  = \mu \left( {t, s}\right) {dt} + \sigma {\left( t, s\right) }^{\top }d{W}_{t}
$$

其中 ${W}_{t}$ 是在风险中性测度 $\mathbb{Q}$ 下的 $d$ 维布朗运动。然而，与短期利率模型相比，我们在指定模型参数时的自由度较小。无套利约束规定了漂移项的以下限制 [164]：

$$
\mu \left( {t, s}\right)  = \sigma {\left( t, s\right) }^{\top }{\int }_{t}^{s}\sigma \left( {t, u}\right) {du}
$$

因此，远期利率的演化描述为

$$
{df}\left( {t, s}\right)  = \left( {\sigma {\left( t, s\right) }^{\top }{\int }_{t}^{s}\sigma \left( {t, u}\right) {du}}\right) {dt} + \sigma {\left( t, s\right) }^{\top }d{W}_{t}
$$

在 HJM 模型中，我们应该指定初始远期利率曲线和远期利率波动结构，后者描述了每个远期利率在给定到期日的波动性。与广泛使用的 Black-Merton-Scholes 衍生品定价模型类似，HJM 模型既不假设风险偏好，也不假设远期利率的漂移。

Oren Cheyette [75] 提出的 Heath-Jarrow-Morton 模型的马尔可夫表示是 HJM 框架的一个子类，旨在克服 HJM 框架的某些限制。

#### 1.3.6 Brace-Gatarek-Musiela (BGM) 模型

Brace-Gatarek-Musiela 模型或市场模型使用可观察的利率，例如 LIBOR 利率和互换利率，与 Black 模型一致，后者是广泛使用的 Black-Merton-Scholes 衍生品定价模型的一个变体。在 LIBOR 市场模型中，一组 $n$ 个 LIBOR 利率被建模为扩散过程 ${L}_{i}\left( t\right)$，其中 $i = 1,\ldots , n$，如下所示：

$$
d{L}_{i}\left( t\right)  = {\mu }_{i}\left( t\right) {L}_{i}\left( t\right) {dt} + {L}_{i}\left( t\right) {\sigma }_{i}{\left( t\right) }^{\top }d{W}_{t}
$$

在这个模型下，我们可以解析地定价上限/下限，并使用对数正态近似来定价互换期权 [57]。校准问题在于找到一个对称半正定矩阵 $\sigma$，使得模型价格与市场价格紧密匹配。这个问题可以重新表述为一个半正定规划问题 [100]。

#### 1.3.7 仿射期限结构模型 (ATSMs)

与 HJM 和 BGM 不同，ATSMs 是简约的，收益率曲线是模型内生的。ATSMs 假设短期利率具有以下仿射形式：

$$
{r}_{t} = {a}_{r} + {b}_{r}^{\top }{x}_{t} \tag{1.29}
$$

其中 ${a}_{r}$ 是一个标量，${b}_{r}$ 是一个与 ${x}_{t}$ 大小一致的向量。

##### 1.3.7.1 连续时间下的仿射期限结构模型

在连续时间下，${x}_{t}$ 遵循矩阵 ${OU}$ 方程。对于常数波动性

$$
d{x}_{t} = \left( {{b}_{\gamma } - B{x}_{t}}\right) {dt} + {\sum d}{W}_{t} \tag{1.30}
$$

在随机波动性情况下，我们假设，如 [165] 所示

$$
d{x}_{t} = \left( {-{b}_{\gamma } - B{x}_{t}}\right) {dt} + \sum \sqrt{{v}_{t}}d{W}_{t} \tag{1.31}
$$

$$
d{v}_{t} = \kappa \left( {\theta  - {v}_{t}}\right) {dt} + \lambda \sqrt{{v}_{t}}{dZ} \tag{1.32}
$$

##### 1.3.7.2 离散时间下的仿射期限结构模型

在 [173] 中，作者提出了一种离散时间的随机波动性模型。他们称之为离散时间下的双伽玛随机波动性模型。该过程如下：

$$
{x}_{t + 1} = {x}_{t} + {b}_{\gamma } - B{x}_{t}{\Delta t} + \sum \sqrt{{v}_{t + 1}{\Delta t}}{z}_{t + 1} \tag{1.33}
$$

其中

$$
{v}_{t + 1} \sim  \operatorname{Gamma}\left( {\lambda {v}_{t} + {y}_{t + 1}, d}\right)  \tag{1.34}
$$

$$
{y}_{t + 1} \sim  \operatorname{Gamma}\left( {\gamma , c}\right)  \tag{1.35}
$$

在 [179] 和 [173] 中，作者推导了在远期测度和互换测度下对数互换利率的特征函数。有了特征函数，他们使用变换技术来定价上限、下限和互换期权。在第 10 章中，我们将详细讨论其参数的估计。


---

### 1.4 资产价格的随机模型

为了对任何衍生品定价，我们需要在每一个构成支付日期或需要做出投资决策的日期，对资产的统计特性进行建模。实际上，这意味着使用随机过程来描述资产价格的演变，存在多种不同的资产价格随机模型，以准确地对不同市场中的不同衍生品进行定价。在本节中，我们将概述一些最常见的资产价格模型。

#### 1.4.1 巴切利耶模型

巴切利耶模型是在布朗运动下对资产价格进行建模的一个模型，由以下随机微分方程（SDE）表示：

$$
d{S}_{t} = r{S}_{t}{dt} + {\sigma d}{W}_{t} \tag{1.36}
$$

其中 $r$ 和 $\sigma$ 分别是连续无风险利率和瞬时波动率。该模型以路易·巴切利耶命名，他在 1900 年发表的博士论文《投机理论》中提出了这一模型。它也被称为正态模型（与对数正态模型或 Black-Merton-Scholes 模型相对，后者将在下文中讨论）。巴切利耶模型不被使用的原因是标的资产价格可能变为负数，这不适用于股票价格的演变。

#### 1.4.2 几何布朗运动 - Black-Merton-Scholes 模型

金融中最早和最常用的资产价格模型之一是几何布朗运动。Black-Merton-Scholes 模型于 1973 年提出，基于几何布朗运动。该模型的创建是量化金融中的一个关键转折点，是大多数现代衍生品定价模型的评判标准。它的发明帮助创建了一个庞大且流动性强的期权市场，并扩展到了现代衍生品市场的数万亿美元。在本节中，我们将简要描述模型的推导过程、其随机微分方程及其特征函数。

##### 1.4.2.1 随机微分方程

使用此模型对资产价格建模时，我们假设资产价格 ${S}_{t}$ 在时间 $t$ 时满足以下随机微分方程，即所谓的 Black-Scholes SDE：

$$
d{S}_{t} = \left( {r - q}\right) {S}_{t}{dt} + \sigma {S}_{t}d{W}_{t} \tag{1.37}
$$

其中 $r, q$ 和 $\sigma$ 分别是连续无风险利率、连续股息率和瞬时波动率。这个方程将资产的对数收益建模为以恒定速率 $r - q$ 增长，并具有 $\sigma$ 的波动率。

---

${}^{7}$ 在使用该模型描述汇率演变时，我们将用 ${r}_{d}$ 替换 $r$ ，即国内利率，用 ${r}_{f}$ 替换 $q$ ，即外国利率。

---

通过伊藤引理，${}^{8}$ 随机微分方程的解可以表示为

$$
{S}_{T} = {S}_{0}{e}^{\left( {r - q - \frac{{\sigma }^{2}}{2}}\right) T + \sigma {W}_{T}}= {S}_{0}{e}^{\left( {r - q - \frac{{\sigma }^{2}}{2}}\right) T + \sigma \sqrt{T}Z}
$$

或者等价地

$$
{s}_{T} = \ln {S}_{T} = {s}_{0} + \left( {r - q - \frac{{\sigma }^{2}}{2}}\right) T + \sigma \sqrt{T}Z
$$

其中 ${s}_{0} = \ln {S}_{0}$ ；因此

$$
{s}_{T} \sim  \mathcal{N}\left( {{s}_{0} + \left( {r - q - \frac{{\sigma }^{2}}{2}}\right) T,{\sigma }^{2}T}\right)
$$

##### 1.4.2.2 Black-Scholes 偏微分方程

Black-Scholes 偏微分方程（1.38）用于对标的资产遵循几何布朗运动的衍生品进行定价。Black-Scholes 方程的推导方法有多种。报告 [214] 概述了通过 (a) 通过构建复制组合的标准推导 Black-Scholes 方程 [238]，(b) 使用资本资产定价模型的另一种推导方法，(c) 使用套利定价理论的回报形式，以及 (d) 使用风险中性定价的另一种推导方法。得到的偏微分方程如下：

$$
\frac{\partial v}{\partial t} + \frac{{\sigma }^{2}{S}^{2}}{2}\frac{{\partial }^{2}v}{\partial {S}^{2}} + \left( {r - q}\right) S\frac{\partial v}{\partial S} = {rv}\left( {S, t}\right)  \tag{1.38}
$$

对于各种衍生品合约，该方程的闭式解是可用的（例如，参见 [38] 和 [273] 关于欧洲看涨期权的讨论）。

##### 1.4.2.3 几何布朗运动的对数的特征函数

我们已经解出了几何布朗运动的 SDE，得到：

$$
{s}_{T} \sim  \mathcal{N}\left( {{s}_{0} + \left( {r - q - \frac{{\sigma }^{2}}{2}}\right) T,{\sigma }^{2}T}\right)  \tag{1.39}
$$

使用正态随机变量的特征函数，我们可以轻松推导出资产价格对数的特征函数：

$$
{\Phi }_{{s}_{T}}\left( \nu \right)  = {e}^{i\left( {{s}_{0} + \left( {r - q - \frac{{\sigma }^{2}}{2}}\right) T}\right) \nu  - \frac{{\sigma }^{2}{\nu }^{2}}{2}T} \tag{1.40}
$$

其中 ${s}_{0} = \ln {S}_{0}$ 且 ${s}_{T} = \ln {S}_{T}$ 。

---

${}^{8}$ 伊藤引理 [245] — 假设 ${X}_{t}$ 满足

$$
d{X}_{t} = {\mu dt} + {\sigma d}{B}_{t}
$$

设 $g\left( {t, x}\right)  \in  {C}^{2}\left( {\lbrack 0,\infty ) \times  \mathbb{R}}\right)$ 。那么

$$
{Y}_{t} = g\left( {t,{X}_{t}}\right)
$$

是一个随机积分，并且

$$
d{Y}_{t} = \frac{\partial g}{\partial t}\left( {t,{X}_{t}}\right) {dt} + \frac{\partial g}{\partial x}\left( {t,{X}_{t}}\right) d{X}_{t} + \frac{1}{2}\frac{{\partial }^{2}g}{\partial {x}^{2}}\left( {t,{X}_{t}}\right) {\left( d{X}_{t}\right) }^{2}
$$

其中

$$
{\left( dt\right) }^{2} = {dt} \cdot  d{B}_{t} = d{B}_{t} \cdot  {dt} = 0, d{B}_{t} \cdot  d{B}_{t} = {dt}
$$

---

##### 1.4.2.4 隐含波动率

市场从业者确定每个报价期权价格的隐含波动率，即与 Black-Merton-Scholes 价格相匹配的波动率值，以符合报价的期权价格。所有执行价格和到期日对的隐含波动率的集合，通常被称为隐含波动率曲面。

#### 1.4.3 局部波动率模型 - 德曼和卡尼

尽管 Black-Scholes 模型仍然是期权定价中最广泛使用的基准模型，以至于许多市场以该模型的隐含波动率来报价期权价格。然而，其对标的资产波动率恒定的假设与市场价格不兼容，导致了不同期权执行价格和到期日的隐含波动率曲面的出现。虽然 Black-Scholes 模型与波动率曲面一起足以对普通期权进行定价，但为了更好地捕捉市场隐含波动率，以便对更复杂的衍生品进行定价，需要更复杂的方法。局部波动率模型是最简单的 Black-Scholes 扩展，它放松了波动率恒定的假设，允许波动率是时间和资产价格的函数。

以下是德曼、伊拉吉·卡尼和邹 [109] 在《局部波动率曲面：解锁指数期权价格中的信息》中摘录的部分，阐述了远期利率与局部波动率之间的类比（1995 年 12 月）：

远期利率与局部波动率之间的类比

---

| 目标 | 评估非活跃国债的价格： | 评估奇异指数期权的价格： |
| --- | --- | --- |
| 旧方法 | 你使用简单的到期收益率来折现所有未来的息票和本金。 | 你使用简单的隐含波动率来计算未来支付的风险中性概率。 |
| 新方法 | 使用从活跃国债价格构建的零息远期利率来折现所有未来的息票和本金。 | 使用从活跃标准期权价格构建的局部波动率来计算未来支付的风险中性概率。 |

---

##### 1.4.3.1 随机微分方程

局部波动率模型下的随机微分方程几乎与几何布朗运动的 SDE 完全相同。唯一的不同之处在于：首先，波动率现在参数化为资产价格和时间的函数；其次，漂移成分现在参数化为时间的函数。

$$
d{S}_{t} = \left( {r\left( t\right)  - q\left( t\right) }\right) {S}_{t}{dt} + \sigma \left( {{S}_{t}, t}\right) {S}_{t}d{W}_{t} \tag{1.41}
$$

##### 1.4.3.2 通用 Black-Merton-Scholes 方程

通用 Black-Scholes 偏微分方程（1.42）用于对标的资产遵循局部波动率模型的衍生品进行定价。它也紧密跟随标准的 Black-Scholes 方程，只是增加了额外的参数化。

$$
\frac{\partial v}{\partial t} + \frac{1}{2}{\sigma }^{2}\left( {{S}_{t}, t}\right) {S}_{t}^{2}\frac{{\partial }^{2}v}{\partial {S}_{t}^{2}} + \left( {r\left( t\right)  - q\left( t\right) }\right) {S}_{t}\frac{\partial v}{\partial {S}_{t}} = r\left( t\right) v\left( {S, t}\right)  \tag{1.42}
$$

##### 1.4.3.3 特征函数

一般来说，局部波动率模型的特征函数没有解析形式，因为 SDE 成分的额外参数化排除了这一点。

##### 1.4.3.4 探索波动率建模：从隐含波动率到局部波动率及反之

在探索波动率建模时，我们遇到了一系列研究论文和主题，每个都揭示了这个迷人领域的一个不同方面。以下是某些关键领域的摘要，以及相关参考文献。请注意，这个列表并不全面，但它提供了一个关于该领域研究广度的概览。

1. 局部波动率模型：如前所述，德曼和卡尼引入了局部波动率模型 [109]，这是波动率建模中的一个基本概念。
2. 波动率微笑：德曼和卡尼在后续论文 [108] 中讨论了波动率微笑及其隐含树，而杜普尔 [120] 在《微笑风险定价》中探讨了期权曲面与局部波动率曲面之间的联系。
3. 隐含波动率与局部波动率：盖瑟尔等人在《从局部波动率到隐含波动率：路径积分方法》中介绍了一种将隐含波动率与局部波动率关联的方法 [294]。
4. 有限差分方法：安德森等人提出了用于建模股票期权波动率微笑的隐式有限差分方法 [13]。
5. 波动率曲面校准：马尔科·阿韦兰尼达通过相对熵最小化探索了波动率曲面的校准 [22]。盖瑟尔和雅克展示了如何校准广泛使用的随机波动率启发（SVI）参数化隐含波动率微笑，以避免静态套利 [142]。
6. 隐含波动率动态：罗杰·W·李调查了关于隐含波动率的概率解释、作为执行价格和到期日函数的行为，以及随时间的演变的研究 [227]。
7. 前瞻和未来隐含波动率：格拉斯曼和于在他们的工作中考虑了前瞻和未来隐含波动率 [149]。
8. 半鞅模型中的局部波动率：作者在 [170] 中展示了如何在半鞅模型中重新设计局部波动率。
9. 奇异期权的前向 PDE 和 PIDES：卡尔和希萨扩展了杜普尔的工作，推导了奇异期权的前向 PDE 和 PIDES [63] 和 [64]。在本书中，我们将更深入地探讨这些主题，提供对波动率建模动态世界的见解。

#### 1.4.4 带随机波动率的几何布朗运动 - Heston 模型

尽管局部波动率模型可以比标准的 Black-Scholes 模型更现实地拟合期权价格的波动率曲面，但波动率函数可能非常复杂，因此在使用变量方面不够简洁。为了在不完全指定波动率函数的情况下对波动率进行建模，这导致了 Heston 随机波动率模型的创建。

##### 1.4.4.1 Heston 随机波动率模型 - 随机微分方程

在 Heston 随机波动率模型下，资产价格 ${S}_{t}$ 遵循由以下一组 SDE 描述的随机过程：

$$
d{S}_{t} = r{S}_{t}{dt} + \sqrt{{v}_{t}}{S}_{t}d{W}_{t}^{\left( 1\right) }
$$

$$
d{v}_{t} = \kappa \left( {\theta  - {v}_{t}}\right) {dt} + \sigma \sqrt{{v}_{t}}d{W}_{t}^{\left( 2\right) }
$$

其中两个布朗成分 ${W}_{t}^{\left( 1\right) }$ 和 ${W}_{t}^{\left( 2\right) }$ 以 $\rho$ 的相关率相关。变量 ${v}_{t}$ 表示均值回归的随机波动率，其中 $\theta$ 是长期方差，$\kappa$ 是均值回归速度，$\sigma$ 是方差的波动率。扩散成分中的 $\sqrt{{v}_{t}}$ 项防止波动率变为负数，当波动率接近零时，通过将扩散成分强制为零来实现。

##### 1.4.4.2 Heston 模型 - 资产价格对数的特征函数

在 Heston 随机波动率模型下，资产价格对数的特征函数由下式给出：

$$
\Phi \left( u\right)  = \mathbb{E}\left( {e}^{{iu}\ln {S}_{t}}\right)= \frac{\exp \left\{  {{iu}\ln {S}_{0} + {iu}\left( {r - q}\right) t + \frac{{\kappa \theta t}\left( {\kappa  - {i\rho \sigma u}}\right) }{{\sigma }^{2}}}\right\}  }{{\left( \cosh \frac{\gamma t}{2} + \frac{\kappa  - {i\rho \sigma u}}{\gamma }\sinh \frac{\gamma t}{2}\right) }^{\frac{2\kappa \theta }{{\sigma }^{2}}}}\exp \left\{  \frac{-\left( {{u}^{2} + {iu}}\right) {v}_{0}}{\gamma \coth \frac{\gamma t}{2} + \kappa  - {i\rho \sigma u}}\right\}
$$

其中 $\gamma  = \sqrt{{\sigma }^{2}\left( {{u}^{2} + {iu}}\right)  + {\left( \kappa  - i\rho \sigma u\right) }^{2}}$，${S}_{0}$ 和 ${v}_{0}$ 分别是价格过程和波动率过程的初始值。请参阅附录 D. 2 以获得详细的证明。附录 D. 2 中提供的证明相当通用，可以用于推导各种不同过程下资产价格对数的特征函数。

#### 1.4.5 混合模型 - 随机局部波动率（SLV）模型

随机局部波动率模型是局部波动率模型的一个扩展，它引入了一个独立的随机成分来描述波动率（例如 [197]，[257]，[286] 和 [229]）。独立的随机成分由一个随机过程 $\left( {V\left( t\right) , t \geq  0}\right)$ 描述，该过程从 1 开始。在这个模型中，股票价格的演变由下式给出：

$$
d{S}_{t} = \left( {r - q}\right) {S}_{t}{dt} + L\left( {{S}_{t}, t}\right) V\left( t\right) {S}_{t}d{W}_{t}^{\left( 1\right) }
$$

其中 $\left( {{W}_{t}^{\left( 1\right) }, t \geq  0}\right)$ 是标准布朗运动，$L\left( {{S}_{t}, t}\right)$ 是股票价格和日历时间的确定性函数，表示平均波动率。在 [257] 中，他们假设

$V\left( t\right)$ 遵循均值回归的对数正态分布

$$
d\ln {V}_{t} = \kappa \left( {\theta \left( t\right)  - \ln {V}_{t}}\right) {dt} + {\lambda d}{W}_{t}^{\left( 2\right) }
$$

其中 $\kappa$ 是均值回归速度，$\theta \left( t\right)$ 是长期确定性漂移，$\lambda$ 是波动率的波动率。考虑到 ${\sigma }^{2}\left( {{S}_{t}, t}\right)$ 被解释为平均局部方差，他们对 ${V}^{2}\left( t\right)$ 的无条件期望值施加了一个约束，使其为 1，这意味着

$$
\theta \left( t\right)  = \frac{{\lambda }^{2}}{2\kappa }\left( {1 + {e}^{-{2\kappa t}}}\right)
$$

在 [286] 中，他们考虑了 ${V}_{t}$ 的以下过程

$$
d{V}_{t} = \kappa \left( {\theta \left( t\right)  - {V}_{t}}\right) {dt} + \lambda {V}_{t}d{W}_{t}^{\left( 2\right) }
$$

可以假设驱动波动率随机成分的布朗运动与驱动股票价格的布朗运动之间存在相关性。然而，在 [257] 中，为了简化，他们假设零相关性。注意，如果 $L\left( {{S}_{t}, t}\right)$ 与股票价格无关，该模型非常类似于 Heston 模型，通过令 $\lambda  = 0$，该模型退化为局部波动率模型。

尽管几何布朗运动、局部波动率和随机波动率模型在对标的资产波动率建模方面非常流行，但它们的恒定漂移假设与市场中长期价格变动回归长期均值的市场价格不兼容。在均值回归是常见特征的市场中，包括利率、货币汇率和商品价格，Ornstein-Uhlenbeck (OU) 过程是一个流行的模型。

#### 1.4.6 方差伽玛模型

在前面讨论的所有模型中，我们集中于修改标的资产过程的波动率，以更好地捕捉动态波动结构，或修改漂移以引入市场观察到的均值回归行为。然而，真实的金融市场包含的价格和利率并不是平滑地随时间变化，而是瞬间跳跃到不同的水平。这些类型的价格变动在期权市场价格中可以观察到。事实上，领域内的专家指出，在建模股票价格动态时引入跳跃成分的重要性，他们认为，纯扩散模型在解释短期期权价格的非常陡峭的微笑效应方面存在困难。因此，已经做出了努力来设计允许价格跳跃的模型，跳扩散模型中的泊松型跳跃成分就是为了应对这些关切而设计的。

方差伽玛 (VG) 过程是一个纯跳跃过程，通过在任何时间间隔内具有无限多个跳跃来保持高活动性，同时保持与正态分布的一致性。与许多其他跳跃模型不同，VG 过程不需要引入扩散成分，因为 Black-Scholes 模型已经是一个参数化的特殊情况，高活动性已经得到考虑。与正常扩散不同，VG 过程的绝对对数价格变化之和是有限的。由于 VG 具有有限变差 [252]，它可以表示为两个递增过程的差，第一个过程解释了价格的增加，而第二个过程解释了价格的减少。在 VG 过程的情况下，这两个递增过程之差所得到的 VG 过程本身是伽玛过程。

##### 1.4.6.1 随机微分方程

方差伽玛过程是布朗运动的三参数推广，作为某些标的市场变量对数动态的模型。方差伽玛过程通过在随机时间变化下评估具有恒定漂移和恒定波动率的布朗运动来获得，该随机时间变化由伽玛过程给出，即

$$
b\left( {t,\sigma ,\theta }\right)  = {\theta t} + {\sigma W}\left( t\right)
$$

$$
X\left( {t;\sigma ,\nu ,\theta }\right)  = b\left( {\gamma \left( {t;1,\nu }\right) ,\sigma ,\theta }\right)= {\theta \gamma }\left( {t;1,\nu }\right)  + {\sigma W}\left( {\gamma \left( {t;1,\nu }\right) }\right)
$$

每个单位的日历时间可以被视为具有由独立随机变量给出的经济相关时间长度，该随机变量具有单位均值和正方差，$\nu  > 0$，我们将其表示为 $\gamma \left( {t;1,\nu }\right)$。因此，我们可以将此模型视为在不同时间段内考虑不同交易活动水平的模型。如 [61] 所述，随机时间变化方法的经济直觉来源于布朗缩放性质。这一性质将尺度变化与时间变化联系起来，因此随机波动率的变化可以通过随机时间的变化来捕捉。因此，方差伽玛模型的随机时间变化是纯跳跃过程中表示随机波动率的一种替代方法。

在方差伽玛模型下，单位期连续复利收益在随机过程实现的条件下是正态分布的，即随机时间具有伽玛密度。所得过程及其相关定价模型为我们提供了一个标准布朗运动模型的稳健三参数推广。方差伽玛模型下资产价格过程的对数由下式给出：

$$
\ln {S}_{t} = \ln {S}_{0} + \left( {r - q + \omega }\right) t + X\left( {t;\sigma ,\nu ,\theta }\right)
$$

或者等价地：

$$
{S}_{t} = {S}_{0}{e}^{\left( {r - q + \omega }\right) t + X\left( {t;\sigma ,\nu ,\theta }\right) }
$$

$\omega$ 被确定为：

$$
\mathbb{E}\left( {S}_{t}\right)  = {S}_{0}{e}^{\left( {r - q}\right) t}
$$

在方差伽玛模型下，时间 $t$ 时资产价格对数的密度可以表示为条件于伽玛时间变化 $g$ 的正态密度函数。然后，无条件密度可以通过积分 $g$ 获得：

$$
f\left( {x;\sigma ,\nu ,\theta }\right)  = {\int }_{0}^{\infty }\phi \left( {{\theta g},{\sigma }^{2}g}\right)  \times  \operatorname{gamma}\left( {\frac{t}{\nu },\nu }\right) {dg}= {\int }_{0}^{\infty }\frac{1}{\sigma \sqrt{2\pi g}}\exp \left( {-\frac{{\left( x - \theta g\right) }^{2}}{2{\sigma }^{2}g}}\right) \frac{{g}^{t/\nu  - 1}{e}^{-g/\nu }}{{\nu }^{t/\nu }\Gamma \left( {t/\nu }\right) }{dg}
$$

该模型的推广允许参数不仅控制布朗运动的波动率，还控制 (i) 收益分布的峰度，即相对于正态分布的左右尾概率的对称增加，以及 (ii) 收益密度左右尾的不对称性。VG 的一个额外吸引人的特点是它将对数正态密度和 Black-Scholes 公式作为参数化的特殊情况包含在内。

##### 1.4.6.2 VG 过程的特征函数

VG 过程的特征函数可以通过首先条件于伽玛时间 $g$ 来获得：

$$
\mathbb{E}\left( {{e}^{{iu}{X}_{t}} \mid  g}\right)  = \mathbb{E}\left( {e}^{{iu}\left( {{\theta g} + \sigma {W}_{g}}\right) }\right)= {e}^{iu\theta g}\mathbb{E}\left( {e}^{{iu\sigma }{W}_{g}}\right)= {e}^{{iu}{\theta g}}\mathbb{E}\left( {e}^{{iu\sigma }\sqrt{g}Z}\right)= {e}^{iu\theta g}{e}^{-\frac{{\left( u\sigma \sqrt{g}\right) }^{2}}{2}}= {e}^{iu\theta g}{e}^{\frac{-{u}^{2}{\sigma }^{2}g}{2}}= {e}^{i\left( {{u\theta } + i\frac{{u}^{2}{\sigma }^{2}}{2}}\right) g}
$$

现在，为了计算 VG 过程的特征函数，我们需要对 $g$ 进行积分：

$$
\mathbb{E}\left( {e}^{{iu}{X}_{t}}\right)  = {\mathbb{E}}_{g}\left( {e}^{i\left( {{u\theta } + i\frac{{u}^{2}{\sigma }^{2}}{2}}\right) g}\right)= {\int }_{0}^{\infty }{e}^{iu\theta g}{e}^{\frac{-{u}^{2}{\sigma }^{2}g}{2}}\frac{{g}^{t/\nu  - 1}{e}^{-g/\nu }}{{\nu }^{t/\nu }\Gamma \left( {t/\nu }\right) }{dg}
$$

这是形状参数为 $\frac{t}{\nu }$ 且尺度参数为 $\nu$ 的伽玛过程的特征函数，在 ${u\theta } + i\frac{{u}^{2}{\sigma }^{2}}{2}$ 处评估。根据方程 (1.16) 中的表达式，我们得到：

$$
{\mathbb{E}}_{g}\left( {e}^{i\left( {{u\theta } + i\frac{{u}^{2}{\sigma }^{2}}{2}}\right) g}\right)  = {\left( \frac{\frac{1}{\nu }}{\frac{1}{\nu } - i\left( {{u\theta } + i\frac{{u}^{2}{\sigma }^{2}}{2}}\right) }\right) }^{\frac{t}{\nu }}= {\left( \frac{1}{1 - {iu\theta \nu } + \frac{{u}^{2}{\sigma }^{2}\nu }{2}}\right) }^{\frac{t}{\nu }} \tag{1.43}
$$

因此，参数为 $\sigma ,\nu$ 和 $\theta$ 的 VG 过程在时间 $t$ 时的特征函数由下式给出：

$$
\mathbb{E}\left( {e}^{{iuX}\left( t\right) }\right)  = {\left( \frac{1}{1 - {iu\theta \nu } + {\sigma }^{2}{u}^{2}\nu /2}\right) }^{\frac{t}{\nu }} \tag{1.44}
$$

在 VG 模型下，股票过程对数的特征函数为：

$$
\mathbb{E}\left( {e}^{{iu}\ln {S}_{t}}\right)  = \exp \left( {{iu}\left( {\ln {S}_{0} + \left( {r - q + \omega }\right) t}\right) }\right) {\left( \frac{1}{1 - {iu\theta \nu } + {\sigma }^{2}{u}^{2}\nu /2}\right) }^{\frac{t}{\nu }}
$$

其中

$$
\omega  = \frac{1}{\nu }\log \left( {1 - {\theta \nu } - {\sigma }^{2}\nu /2}\right)
$$

在后续章节中，我们将根据所考虑的期权类型，通过变换方法和部分积分微分方程的数值解，覆盖在 VG 模型下对衍生品定价的内容。然而，此时应该明显的是，在 VG 模型下对欧洲期权定价涉及首先条件于随机时间 $g$，然后简单地使用类似 Black-Scholes 的公式来解决条件期权价值。因此，VG 欧式期权价格 $C\left( {{S}_{0}, K, T}\right)$ 通过相对于伽玛密度的积分获得：

$$
C\left( {{S}_{0}, K, T}\right)  = {\int }_{0}^{\infty }\text{ Black-Scholes }\left( {{S}_{0}, K, g}\right) \frac{{g}^{t/\nu  - 1}{e}^{-g/\nu }}{{\nu }^{t/\nu }\Gamma \left( {t/\nu }\right) }{dg}
$$

此外，通过应用 Lévy-Khintchine 定理 [191] 中的方程 (1.19) 和 (1.20)，可以证明方差伽玛过程的 Lévy 测度可以写为 ${d\nu }\left( x\right)  = k\left( x\right) {dx}$，其中 $k\left( x\right)$ 由下式给出：

$$
{d\nu }\left( x\right)  = k\left( x\right) {dx}
$$

$$
k\left( x\right)  = \frac{{e}^{-{\lambda }_{p}x}}{\nu x}{\mathbb{1}}_{x > 0} + \frac{{e}^{-{\lambda }_{n}\left| x\right| }}{\nu \left| x\right| }{\mathbb{1}}_{x < 0}
$$

$$
{\lambda }_{p} = {\left( \frac{{\theta }^{2}}{{\sigma }^{4}} + \frac{2}{{\sigma }^{2}\nu }\right) }^{\frac{1}{2}} - \frac{\theta }{{\sigma }^{2}}
$$

$$
{\lambda }_{n} = {\left( \frac{{\theta }^{2}}{{\sigma }^{4}} + \frac{2}{{\sigma }^{2}\nu }\right) }^{\frac{1}{2}} + \frac{\theta }{{\sigma }^{2}}
$$

在 VG 过程 [236] 中，有三个模型参数：$\sigma  > 0,\theta  \in  \mathbb{R}$ 和 $\nu  > 0$。Lévy 密度由下式给出：

$$
k\left( y\right)  = \frac{{e}^{-{My}}}{\nu y}{1}_{y > 0} + \frac{{e}^{-G\left| y\right| }}{\nu \left| y\right| }{1}_{y < 0}
$$

其中

$$
M = \sqrt{{\theta }^{2}/{\sigma }^{4} + 2/\left( {{\sigma }^{2}\nu }\right) } - \theta /{\sigma }^{2} \tag{1.45}
$$

和

$$
G = \sqrt{{\theta }^{2}/{\sigma }^{4} + 2/\left( {{\sigma }^{2}\nu }\right) } + \theta /{\sigma }^{2}. \tag{1.46}
$$

特征指数由下式给出：

$$
\psi \left( u\right)  =  - \ln \left( {1 + {\sigma }^{2}\nu {u}^{2}/2 - \mathrm{i}{\theta \nu u}}\right) /\nu
$$

其中在特征指数中 $s = 0$。

#### 1.4.7 CGMY 模型

在本书中，我们考虑了许多不同的模型，一些纯扩散模型（例如 Black-Scholes 模型），一些纯跳跃模型（例如 VG 模型），还有一些结合了两者。CGMY 模型试图通过引入参数化模型来适应所有这些行为，允许纯扩散或纯跳跃，无限或有限变差，以及无限或有限到达率。

CGMY 过程 [60] 由其 Lévy 测度定义，可以写为：${d\nu }\left( x\right)  =$ $k\left( x\right) {dx}$，其中 $k\left( x\right)$ 由下式给出：

$$
{d\nu }\left( x\right)  = k\left( x\right) {dx}
$$

$$
k\left( x\right)  = C\frac{{e}^{-{Gx}}}{{x}^{1 + Y}}{\mathbb{1}}_{x > 0} + \frac{{e}^{-M\left| x\right| }}{{\left| x\right| }^{1 + Y}}{\mathbb{1}}_{x < 0}
$$

对于常数 $C > 0, G \geq  0, M \geq  0$对于常数 $C > 0, G \geq  0, M \geq  0$，以及 $Y < 2$。

我们可以证明 CGMY 模型推广了 Kou 的跳跃扩散模型 [216] $\left( {Y =  - 1}\right)$ 和方差伽玛模型 [235] $\left( {Y = 0}\right)$。CGMY 过程是 Boyarchenko 和 Levendorskii 在 [42] 中以及 Carr, Geman, Madan 和 Yor 在 [61] 中研究的 Kobol 过程的一个特例，其中常数 $C$ 允许在正半轴和负半轴上取不同的值。对 VG 的扩展非常有趣，因为它允许控制大跳跃和小跳跃的符号。

通过将 $Y$ 提高到零以上，可以在接近零的地方诱导更多的活动，而在远离零的地方减少活动。还有一些关键值 $Y$ 值值得关注：

(a) $Y = 1$ 将有限变差 $Y < 1$ 与无限变差 $Y > 1$ 分开，

(b) $Y = 0$ 将有限到达率 $Y < 0$ 与无限到达率 $Y > 0$ 分开，

(c) $Y =  - 1$ 将活动集中在远离零的 $Y <  - 1$ 与活动集中在零附近的 $Y >  - 1$ 分开。

对于 $Y >  - 1$，我们有一个完全单调的 Lévy 测度 [40]。

##### 1.4.7.1 特征函数

CGMY 过程模型过于通用，无法通过单一的 SDE 来描述；其描述仅通过特征函数已知。参数为 $C, G, M$ 和 $Y$ 的 CGMY 过程的特征函数可以显式计算为 [60]：

$$
\mathbb{E}\left\lbrack  {e}^{{iu}{X}_{t}}\right\rbrack   = {e}^{{Ct\Gamma }\left( {-Y}\right) \left( {{\left( M - iu\right) }^{Y} - {M}^{Y} + {\left( G + iu\right) }^{Y} - {G}^{Y}}\right) }
$$

CGMY 过程 [59] 是 VG 过程的一个推广。有四个模型参数：$\sigma  > 0,\theta  \in  \mathbb{R},\nu  > 0$ 和 $0 \leq  Y < 2$。Lévy 密度由下式给出：

$$
k\left( y\right)  = \frac{C{e}^{-{My}}}{{y}^{1 + Y}}{1}_{y > 0} + \frac{C{e}^{-G\left| y\right| }}{{\left| y\right| }^{1 + Y}}{1}_{y < 0}
$$

其中 $M$ 和 $G$ 遵循方程 (1.45) 和 (1.46) 中的定义，且 $C = 1/\nu$。

当 $Y = 0$ 时，特征指数在 VG 模型中给出。否则，特征指数由下式给出：

$$
\psi \left( u\right)  = \left\{  \begin{array}{ll} {C\Gamma }\left( {-Y}\right) \left( {{\left( G + iu\right) }^{Y} - {G}^{Y} + {\left( M - iu\right) }^{Y} - {M}^{Y}}\right) , & Y \neq  0, \\  C\left( {\left( {G + {iu}}\right) \ln \left( {G + {iu}}\right)  - G\ln G + \left( {M - {iu}}\right) \ln \left( {M - {iu}}\right)  - M\ln M}\right) , & Y = 1 \end{array}\right.
$$

其中 $\Gamma \left( \cdot \right)$ 是伽玛函数，且在特征指数中 $s = 0$。

#### 1.4.8 正态逆高斯 (NIG) 模型

正态逆高斯 (NIG) 分布和过程由 Barndorff-Nielsen 在 [28] 和 [29] 中引入。该过程是一个带有漂移的布朗运动的时间变化过程，时间变化通过逆伽玛过程生成，与 VG 模型使用伽玛过程不同。这使得 NIG 成为一个具有无限变差的纯跳跃 Lévy 过程，而 VG 过程具有有限变差。该过程的参数是布朗运动的漂移和波动率以及逆高斯分布的方差，其期望值假设为 1。在极限情况下，当方差设置为零时，NIG 过程与布朗运动重合，概率密度为正态。对于其他方差值，NIG 概率密度具有非零的超额峰度和偏度，类似于方差伽玛。因此，在大多数情况下，NIG 分布的尾部比正态分布下降得更慢。

##### 1.4.8.1 特征函数

参数为 $\sigma ,\nu$ 和 $\theta$ 的 NIG 过程的特征函数表示为：

$$
\mathbb{E}\left\lbrack  {e}^{{iu}{X}_{t}}\right\rbrack   = {e}^{\left( {\nu  - \sigma \sqrt{\frac{{\nu }^{2}}{{\sigma }^{2}} + \frac{{\theta }^{2}}{{\sigma }^{4}} - {\left( \frac{\theta }{{\sigma }^{2}} + iu\right) }^{2}}}\right) t}
$$

在 NIG 过程 [29] 中，有三个模型参数：$\alpha  > 1, - \alpha  < \beta  < \alpha  - 1$ 和 $\delta  > 0$。Lévy 密度由下式给出：

$$
k\left( y\right)  = \frac{\delta \alpha }{\pi }\frac{{e}^{\beta x}{K}_{1}\left( {\alpha \left| x\right| }\right) }{\left| x\right| }
$$

其中 ${K}_{1}\left( \cdot \right)$ 是第二类修正贝塞尔函数。特征指数由下式给出：

$$
\psi \left( u\right)  =  - \delta \left( {\sqrt{{\alpha }^{2} - {\left( \beta  + ui\right) }^{2})} - \sqrt{{\alpha }^{2} - {\beta }^{2}}}\right)
$$

此外，在特征指数中 $s = 0$。

#### 1.4.9 方差伽玛带随机到达 (VGSA) 模型

如在第 1.4.6 节中讨论的，方差伽玛模型通过使用随机时间变化来实现随机波动率。然而，VG 模型中的随机波动率不允许波动率聚集，这是许多不同市场中资产价格的一个特征。波动率聚集由 Benoit Mandelbrot 展示，它是指大变动最有可能被大变动（无论正负）跟随，小变动最有可能被小变动跟随的现象。这种模型中的波动率聚集只有在随机时间变化持续存在时才能实现，这要求时间变化率是均值回归的。均值回归的正过程的经典例子是之前讨论的 Cox-Ingersoll-Ross (CIR) 过程。为了允许聚集，方差伽玛带随机到达 (VGSA) 模型在 [61] 中被开发。我们通过取 VG 过程（一个齐次 Lévy 过程），并通过评估其在由 Cox-Ingersoll-Ross [93] (CIR) 过程的积分给出的连续时间变化来构建 VGSA 过程，该积分代表瞬时时间变化。CIR 过程的均值回归引入了通常称为波动率持久性的聚集现象。这使我们能够同时校准执行价格和到期日的期权价格曲面，而 VG 模型只能在校准执行价格时固定到期日。VGSA 过程还允许其特征函数的解析表达。

##### 1.4.9.1 随机微分方程

如前所述，我们定义 CIR 过程，$y\left( t\right)$，作为以下随机微分方程的解：

$$
d{y}_{t} = \kappa \left( {\eta  - {y}_{t}}\right) {dt} + \lambda \sqrt{{y}_{t}}d{W}_{t}
$$

其中 $W\left( t\right)$ 是布朗运动，$\eta$ 是长期时间变化率，$\kappa$ 是均值回归速度，$\lambda$ 是时间变化的波动率。过程 $y\left( t\right)$ 是瞬时时间变化率，因此时间变化由 $Y\left( t\right)$ 给出，其中：

$$
Y\left( t\right)  = {\int }_{0}^{t}y\left( u\right) {du}
$$

市场变量对数的 SDE 与上述时间变化下的 VG 过程相同。

##### 1.4.9.2 特征函数

如在第 1.3.4.2 节中所示，时间变化 $Y\left( t\right)$ 的特征函数由下式给出：

$$
\mathbb{E}\left( {e}^{{iuY}\left( t\right) }\right)  = \phi \left( {u, t, y\left( 0\right) ,\kappa ,\eta ,\lambda }\right)= A\left( {t, u}\right) {e}^{B\left( {t, u}\right) y\left( 0\right) }
$$

其中：

$$
A\left( {t, u}\right)  = \frac{\exp \left( \frac{{\kappa }^{2}{\eta t}}{{\lambda }^{2}}\right) }{{\left( \cosh \left( \gamma t/2\right)  + \frac{\kappa }{\gamma }\sinh \left( \gamma t/2\right) \right) }^{{2\kappa \eta }/{\lambda }^{2}}}
$$

$$
B\left( {t, u}\right)  = \frac{2iu}{\kappa  + \gamma \coth \left( {{\gamma t}/2}\right) }
$$

以及：

$$
\gamma  = \sqrt{{\kappa }^{2} - 2{\lambda }^{2}{iu}}
$$

随机波动率 Lévy 过程，称为 VGSA 过程，由下式定义：

$$
{Z}_{VGSA}\left( t\right)  = {X}_{VG}\left( {Y\left( t\right) ;\sigma ,\nu ,\theta }\right)
$$

其中 $\sigma ,\nu ,\theta ,\kappa ,\eta$ 和 $\lambda$ 是定义过程的六个参数。其特征函数由下式给出：

$$
\mathbb{E}\left( {e}^{{iu}{Z}_{VGSA}\left( t\right) }\right)  = \phi \left( {-i{\Psi }_{VG}\left( u\right) , t,\frac{1}{\nu },\kappa ,\eta ,\lambda }\right)
$$

其中 ${\Psi }_{VG}$ 是单位时间下方差伽玛过程的对数特征函数，即：

$$
{\Psi }_{VG}\left( u\right)  =  - \frac{1}{\nu }\log \left( {1 - {iu\theta \nu } + {\sigma }^{2}\nu {u}^{2}/2}\right)
$$

我们定义时间 $t$ 时的资产价格过程如下：

$$
S\left( t\right)  = S\left( 0\right) \frac{{e}^{\left( {r - q}\right) t + {Z}_{VGSA}\left( t\right) }}{\mathbb{E}\left\lbrack  {e}^{{Z}_{VGSA}\left( t\right) }\right\rbrack  }
$$

我们注意到：

$$
\mathbb{E}\left\lbrack  {e}^{Z\left( t\right) }\right\rbrack   = \phi \left( {-i{\Psi }_{VG}\left( {-i}\right) , t,\frac{1}{\nu },\kappa ,\eta ,\lambda }\right)
$$

因此，时间 $t$ 时资产价格对数的特征函数由下式给出：

$$
\mathbb{E}\left\lbrack  {e}^{{iu}\log {S}_{t}}\right\rbrack   = \exp \left( {{iu}\left( {\log {S}_{0} + \left( {r - q}\right) t}\right) }\right)  \times  \frac{\phi \left( {-i{\Psi }_{VG}\left( u\right) , t,\frac{1}{\nu },\kappa ,\eta ,\lambda }\right) }{\phi {\left( -i{\Psi }_{VG}\left( -i\right) , t,\frac{1}{\nu },\kappa ,\eta ,\lambda \right) }^{iu}}
$$

因此，我们得到了 VGSA 模型下资产价格对数的特征函数的闭式解。

##### 1.4.9.3 Merton 的跳跃扩散模型

在 Merton 的模型 [239] 中，有四个模型参数：$\sigma  > 0,\lambda  \geq  0,\alpha  \in  \mathbb{R}$ 和 $\delta  > 0$。Lévy 密度由下式给出：

$$
k\left( y\right)  = \frac{\lambda }{\sqrt{2\pi }\delta }{e}^{-{\left( x - \alpha \right) }^{2}/\left( {2{\delta }^{2}}\right) }
$$

特征指数由下式给出：

$$
\psi \left( u\right)  =  - {\sigma }^{2}{u}^{2}/2 + \lambda \left( {\exp \left( {{\alpha iu} - {\delta }^{2}{u}^{2}/2}\right)  - 1}\right)
$$

以及在特征指数中 $s = \sigma$。

##### 1.4.9.4 Kou 的双指数跳跃扩散模型

在 Kou 的模型 [217] 中，有五个模型参数：$\sigma  > 0,\lambda  \geq  0,0 \leq  p \leq  1,{\eta }_{1} > 0$ 和 ${\eta }_{2} > 0$。Lévy 密度由下式给出：

$$
k\left( y\right)  = {\lambda p}{\eta }_{1}{e}^{-{\eta }_{1}y}{1}_{y > 0} + \lambda \left( {1 - p}\right) {\eta }_{2}{e}^{{\eta }_{2}y}{1}_{y < 0}
$$

特征指数由下式给出：

$$
\psi \left( u\right)  =  - \frac{{\sigma }^{2}{u}^{2}}{2} + \lambda \left( {\frac{p{\eta }_{1}}{{\eta }_{1} - {iu}} + \frac{\left( {1 - p}\right) {\eta }_{2}}{{\eta }_{2} + {iu}} - 1}\right)
$$

以及在特征指数中 $s = \sigma$。

#### 1.4.10 股票模型及其对应的利率模型

在前面的章节中，我们简要讨论了利率和股票价格演变的模型。在本书的后续章节中，我们将进一步讨论这些模型的应用、定价和校准。为了提供一些视角，我们总结了一些模型及其等价性，即股票模型与其对应的利率模型。表 1.10 提供了这种比较 ${}^{9}$ 。

---

${}^{9}$ 在使用该模型描述汇率演变时，我们将用 ${r}_{d}$ 替换 $r$，即国内利率，用 ${r}_{f}$ 替换 $q$，即外国利率。

---



---

### 1.5 在不同测度下对衍生品的估值

我们从风险中性测度下的衍生品合约定价开始。然后，我们覆盖了在前向测度下的定价，这在定价地板期权/上限期权时使用。接下来，我们讨论在互换测度下的定价，用于定价互换期权/跨式期权，最后是份额测度下的定价。在金融数学中，风险中性测度，也称为等价鞅测度，是一种概率测度，使得在这种测度下资产未来价值的折现期望等于其当前价值。对于更多细节，我们建议读者参阅 [180]。

#### 1.5.1 风险中性测度下的定价

在前面的章节中，我们描述了资产价格的多种不同模型及其各种表示。然而，对衍生品的估值不仅仅需要一个资产价格模型。衍生品的价值可以通过计算所有可能影响收益的资产价格路径上的衍生品收益的期望来得到。这种期望所采用的测度是关键的，决定了衍生品定价是否与几乎所有的衍生品定价模型中存在的标准无套利假设一致。资产定价的基本定理 [103] 告诉我们，一个完整的市场是无套利的当且仅当至少存在一个风险中性概率测度 ${}^{10}$ 在这样的测度下，所有资产的预期回报率等于无风险利率。

风险中性定价的发展历史跨越了几十年，主要跟随了量化金融的发展。我们不会在这篇文章中全面介绍这些发展，但建议读者参阅 [114] 和 [285] 以获得更多的阐述。

---

${}^{9}$ 非常感谢 Alireza Javaheri 的贡献

${}^{10}$ 风险中性测度也称为等价鞅测度或均衡测度。

---

表 1.10: 股票与利率的比较

| 股票与利率 | 股票 | 利率 |
| --- | --- | --- |
| 方差互换 $V\left( t, T\right)$ | 折现因子 $p\left( t, T\right)$ | |
| 前向方差互换 $V\left( t, T_1, T_2\right) = \frac{\left( T_2 - t\right) V\left( t, T_2\right) - \left( T_1 - t\right) V\left( t, T_1\right)}{\left( T_2 - T_1\right)}$ | 前向利率 $L\left( t, T_1, T_2\right) = \frac{1}{T_2 - T_1}\left( \frac{p\left( t, T_1\right)}{p\left( t, T_2\right)} - 1\right)$ | |
| 即时前向方差 $\xi \left( t, T\right) = \frac{\partial \left( T - t\right) V\left( t, T\right)}{\partial T}$ | 即时前向利率 $f\left( t, T\right) = - \frac{\partial \ln p\left( t, T\right)}{\partial T}$ | |
| $V\left( t, T\right) = \frac{1}{T - t}\int_{t}^{T}\xi \left( t, u\right) du$ | $p\left( t, T\right) = \exp \left( -\int_{t}^{T}f\left( t, u\right) du\right)$ | |
| 即时方差 $v\left( t\right) = \xi \left( t, t\right)$ | 短期利率 $r\left( t\right) = f\left( t, t\right)$ | |
| 忽略利率和股息 $\frac{dS_t}{S_t} = \sqrt{v_t}dW_t^Q$ | 利率中没有等价的 $S\left( t\right)$！ | |
| $\xi \left( t, T\right) = \mathbb{E}_t^Q\left[ v\left( T\right)\right]$ | $f\left( t, T\right) = \mathbb{E}_t^{Q^T}\left[ r\left( T\right)\right]$ | |
| 对数正态 $\frac{d\xi \left( t, T\right)}{\xi \left( t, T\right)} = \sigma \left( t, T\right) dW_t^Q$ | 正态 $df\left( t, T\right) = \alpha \left( t, T\right) dt + \sigma \left( t, T\right) dW_t^Q$ | |
| 马尔可夫子类 $\sigma \left( t, T\right) = \sigma \exp \left( -\kappa \left( T - t\right)\right)$ 方差曲线（Bergomi） | 扩展的 Vasicek | |
| $v\left( t\right)$ 对数正态且始终为正 | $r\left( t\right)$ 正态且可能变为负 | |
| 局部波动率 ${\sigma }_{loc}^{2}\left( K, T\right) = \mathbb{E}_t^Q\left[ v\left( T\right) \mid S\left( T\right) = K\right]$ ${\sigma }_{loc}^{2}\left( K, T\right) = 2\frac{\partial C\left( K, T\right) /\partial T}{{K}^{2}{\partial }^{2}C\left( K, T\right) /\partial {K}^{2}}$ | 没有等价于交易的 $S\left( t\right)$ | |
| $dS_t/S_t = \sqrt{v_t}dW_t^Q$ 在局部波动率模型下，$v_t$ 存储了 $0 \leq t \leq T$ 期间的期权信息（Dupire） | 利率中不需要 $S\left( t\right)$，因为没有等价于 $S\left( t\right)$ 的东西，只有 $p\left( t, T\right)$ | |

在风险中性框架下，对仅依赖于标的资产到期价格的衍生品的最通用的风险中性定价表达式可以表述如下：

$S_T$ 是标的证券在时间 $T$ 的价格

$f\left( S_T\right) \equiv f\left( S_T \mid S_t\right)$ 是给定 $S_t$ 时 $S_T$ 的（条件）风险中性密度

$V\left( S_T\right)$ 是到期时间为 $T$ 的衍生品合约在时间 $T$ 的收益

$C_t$ 是到期时间为 $T$ 的衍生品合约在时间 $t$ 的价格

我们可以使用风险中性定价来表达衍生品价格如下：

$$
C_t = e^{-r\left( T - t\right)}\mathbb{E}^{\mathbb{Q}}\left[ V\left( S_T\right)\right]= e^{-r\left( T - t\right)}\int_{-\infty}^{\infty}V\left( S_T\right) f\left( S_T\right) dS_T
$$

在风险中性框架下定价的第一个衍生品是欧洲看涨期权，我们将在此处说明其构建。设 $\mathbb{Q}$ 是与现金账户 ${B}_t = e^{\int_{0}^{t}r_u du}$ 相对应的等价鞅测度，作为计价单位，这意味着在 $\mathbb{Q}$ 下任何交易的证券除以 ${B}_t$ 都是一个鞅，或者等价地说任何证券的回报率等于现金账户。这意味着在时间 $t$，到期时间为 $T$，执行价格为 $K$ 的看涨期权价格为：

$$
\frac{C_t\left( K\right)}{B_t} = \mathbb{E}_t^{\mathbb{Q}}\left( \frac{\left( S_T - K\right)^+}{B_T}\right)
$$

假设无风险利率是常数，时间 $t$ 的看涨期权价格可以写成：

$$
C_t\left( K\right) = e^{-r\left( T - t\right)}\mathbb{E}_t^{\mathbb{Q}}\left( \left( S_T - K\right)^+\right) \tag{1.47}
$$

#### 1.5.2 概率测度的变换

风险中性测度提供了完整市场中无套利条件与衍生品定价之间的基本联系。然而，对于许多定价算法而言，直接在风险中性测度下工作是不方便的。在这种情况下，我们应用测度变换，以便在更方便的测度下取期望，同时仍然与风险中性定价保持一致。

设 $\mathbb{Q}$ 是给定的概率测度，${M}_t$ 是一个严格正的 $\mathbb{Q}$-鞅，使得 ${\mathbb{E}}^{\mathbb{Q}}\left[ M_t\right] = 1$ 对所有 $t \in \left[ 0, T\right]$ 成立。然后，我们可以定义一个新的等价概率测度 $\mathbb{P}$，通过定义：

$$
\mathbb{P}\left( A\right) = \mathbb{E}_t^{\mathbb{Q}}\left[ M_T \mathbb{1}_A\right] = \int M_T\left( \omega \right) \mathbb{1}_A d\mathbb{Q}\left( \omega \right) = \int_{A} M_T\left( \omega \right) d\mathbb{Q}\left( \omega \right)
$$

或者简写为 $d\mathbb{P} = M_T d\mathbb{Q}$，注意到 $\mathbb{P}\left( \Omega \right) = 1$。相对于 $\mathbb{P}$ 的期望满足：

$$
\mathbb{E}^{\mathbb{P}}\left( X\right) = \int X\left( \omega \right) d\mathbb{P}\left( \omega \right)= \int X\left( \omega \right) M_T\left( \omega \right) d\mathbb{Q}\left( \omega \right)= \mathbb{E}^{\mathbb{Q}}\left[ M_T X\right]
$$

当我们以这种方式定义测度变换时，我们使用符号 $\frac{d\mathbb{P}}{d\mathbb{Q}}$ 来指代 $M_T$，因此我们通常写成：

$$
\mathbb{E}^{\mathbb{P}}\left( X\right) = \mathbb{E}^{\mathbb{Q}}\left( \frac{d\mathbb{P}}{d\mathbb{Q}} X\right)
$$

以下结果解释了如何在取条件期望时在 $\mathbb{Q}$ 和 $\mathbb{P}$ 之间切换：

$$
\mathbb{E}_t^{\mathbb{P}}\left( X\right) = \frac{\mathbb{E}_t^{\mathbb{Q}}\left( \frac{d\mathbb{P}}{d\mathbb{Q}} X\right)}{\mathbb{E}_t^{\mathbb{Q}}\left( \frac{d\mathbb{P}}{d\mathbb{Q}}\right)}= \frac{\mathbb{E}_t^{\mathbb{Q}}\left( \frac{d\mathbb{P}}{d\mathbb{Q}} X\right)}{\mathbb{E}_t^{\mathbb{Q}}\left( M_T\right)}= \frac{\mathbb{E}_t^{\mathbb{Q}}\left( \frac{d\mathbb{P}}{d\mathbb{Q}} X\right)}{M_t}
$$

给定 $M_t$ 是一个 $\mathbb{Q}$-鞅。

#### 1.5.3 前向测度下的定价

虽然风险中性测度是在衍生品定价中最常用的测度，但它并不是唯一被使用的测度。当我们可以消除 $\mathbb{Q}$ 下期望中的所有项，除了 ${\left( X_T - K\right)^+}$（对于看涨期权）时，带有随机利率的模型下的衍生品定价变得可行。因此，我们需要进行一些操作以消除期望中的其他项，我们通过改变概率测度来实现这一点。

我们从假设 $P\left( t, T\right)$ 是到期时间为 $T \geq t$ 的零息债券在时间 $t$ 的价格，面值为 $1$ 美元开始。假设 ${B}_0 = 1$ 美元，现在使用 $P\left( t, T\right)$ 作为计价单位来定义一个新的概率测度；因此我们可以写成：

$$
\frac{C_t}{P\left( t, T\right)} = \mathbb{E}_t^{\mathbb{P}^T}\left[ \frac{C_T}{P\left( T, T\right)}\right] \tag{1.48}
$$

我们称新的概率测度 $\mathbb{P}^T$ 为 $T$-前向概率测度。我们可以通过注意到以下内容来计算从风险中性测度到 $\mathbb{P}^T$ 的测度变换：

$$
\mathbb{E}_0^{\mathbb{Q}}\left[ \frac{P\left( T, T\right)}{B_T}\right] = \frac{P\left( 0, T\right)}{B_0}
$$

由于 $P\left( T, T\right) = 1$，${B}_0 = 1$ 且 $P\left( 0, T\right)$ 在时间零时已知，我们得到：

$$
\mathbb{E}_0^{\mathbb{Q}}\left[ \frac{1}{B_T P\left( 0, T\right)}\right] = 1 \tag{1.49}
$$

其中 $\frac{1}{B_T P\left( 0, T\right)} > 0$。因此我们设：

$$
M_T = \frac{d\mathbb{P}^T}{d\mathbb{Q}} = \frac{1}{B_T P\left( 0, T\right)}
$$

我们还注意到：

$$
\mathbb{E}_t^{\mathbb{Q}}\left[ \frac{P\left( T, T\right)}{B_T}\right] = \frac{P\left( t, T\right)}{B_t}
$$

再次由于 $P\left( T, T\right) = 1$ 且 $P\left( 0, T\right)$ 在时间零时已知，我们有：

$$
\mathbb{E}_t^{\mathbb{Q}}\left[ \frac{1}{P\left( 0, T\right) B_T}\right] = \frac{P\left( t, T\right)}{P\left( 0, T\right) B_t} \tag{1.50}
$$

现在设 ${C}_t$ 表示到期时间为 $T$ 的衍生品在时间 $t$ 的价格。根据第 (1.5.2) 节的讨论，我们有：

$$
\frac{C_t}{B_t} = \mathbb{E}_t^{\mathbb{Q}}\left[ \frac{C_T}{B_T}\right]
$$

$$
C_t = B_t \mathbb{E}_t^{\mathbb{Q}}\left[ \frac{C_T}{B_T}\right]= B_t \frac{\mathbb{E}_t^{\mathbb{P}^T}\left[ \frac{d\mathbb{Q}}{d\mathbb{P}^T} \frac{C_T}{B_T}\right]}{\mathbb{E}_t^{\mathbb{P}^T}\left[ \frac{d\mathbb{Q}}{d\mathbb{P}^T}\right]} \tag{1.51}
$$

$$
= B_t \frac{\mathbb{E}_t^{\mathbb{P}^T}\left[ B_T P\left( 0, T\right) \frac{C_T}{B_T}\right]}{\mathbb{E}_t^{\mathbb{P}^T}\left[ B_T P\left( 0, T\right)\right]}= B_t P\left( 0, T\right) \frac{\mathbb{E}_t^{\mathbb{P}^T}\left[ C_T\right]}{\mathbb{E}_t^{\mathbb{P}^T}\left[ B_T P\left( 0, T\right)\right]}
$$

$$
= B_t P\left( 0, T\right) \frac{\mathbb{E}_t^{\mathbb{P}^T}\left[ C_T\right]}{\mathbb{E}_t^{\mathbb{Q}}\left[ 1\right] / \mathbb{E}_t^{\mathbb{Q}}\left[ 1/B_T P\left( 0, T\right)\right]}= P\left( t, T\right) \mathbb{E}_t^{\mathbb{P}^T}\left[ C_T\right] \tag{1.52}
$$

我们现在可以通过公式 (1.51) 或公式 (1.52) 来计算时间 $t$ 的衍生品价值 ${C}_t$，其中我们使用现金账户作为计价单位。通过 (1.51) 计算 ${C}_t$ 是我们通常采用的方法，通常非常方便。例如，在定价股票衍生品时，我们通常假设利率，因此现金账户是确定的。这意味着 (1.51) 中的因子 $\frac{1}{B_T}$ 可以从期望中提取出来，因此只需要 $\mathbb{Q}$ 下的 ${C}_T$ 分布来计算 ${C}_t$。当利率是随机的时，我们不能在 (1.51) 中将因子 $\frac{1}{B_T}$ 从期望中提取出来，因此我们需要找到 $\left( B_T, C_T\right)$ 的联合 $\mathbb{Q}$ 分布来计算 ${C}_t$。另一方面，如果我们使用公式 (1.52) 来计算 ${C}_t$，那么我们只需要 ${\mathbb{P}}^T$ 下的 ${C}_T$ 分布，无论利率是否随机。

处理单变量分布通常比处理双变量分布容易得多，因此如果我们能够轻松找到 ${\mathbb{P}}^T$ 下的 ${C}_T$ 分布，那么使用这个分布通常是非常有利的。因此，前向测度在研究期限结构模型时特别有用。

##### 1.5.3.1 地板期权/上限期权的价格

为了展示前向测度的实用性，我们将通过前向测度下的期望来推导地板期权的价格，这将说明测度变换如何使地板期权定价变得更加可行。

我们知道，前向 LIBOR 利率可以用前向零息债券价格来描述：
$$
\operatorname{LIBOR}\left( T, T + h\right) = \frac{1}{h}\left( \frac{1}{P\left( T, T + h\right)} - 1\right)
$$
其中，$P\left( t, T\right)$ 是到期时间为 $T$ 的零息债券在时间 $t$ 的价格，$\operatorname{LIBOR}\left( t, T\right)$ 是时间 $t$ 的 LIBOR 利率，期限为 $\left[ t, T\right]$。

我们假设支付是在期后进行的，名义金额为 $L$，因此时间 $t$ 的地板期权价值为：
$$
\text{floorlet}_t^i = L \mathbb{E}_t^{\mathbb{Q}}\left[ e^{-\int_{t}^{T + h} r\left( s\right) ds} h \left( k - \operatorname{LIBOR}\left( T, T + h\right)\right)^+\right]= L \mathbb{E}_t^{\mathbb{Q}}\left[ e^{-\int_{t}^{T} r\left( s\right) ds} e^{-\int_{T}^{T + h} r\left( s\right) ds} h \left( k - \operatorname{LIBOR}\left( T, T + h\right)\right)^+\right]
$$

通过迭代期望定律，我们得到：
$$
\text{floorlet}_t^i = L \mathbb{E}_t^{\mathbb{Q}}\left\{ e^{-\int_{t}^{T} r\left( s\right) ds} \mathbb{E}_T^{\mathbb{Q}}\left[ e^{-\int_{T}^{T + h} r\left( s\right) ds}\right] h \left[ k - \frac{1}{h}\left( \frac{1}{P\left( T, T + h\right)} - 1\right) \right]^+\right\}
\\
= L \mathbb{E}_t^{\mathbb{Q}}\left\{ e^{-\int_{t}^{T} r\left( s\right) ds} P\left( T, T + h\right) \left[ hk - \left( \frac{1}{P\left( T, T + h\right)} - 1\right) \right]^+\right\}
\\
= L \mathbb{E}_t^{\mathbb{Q}}\left\{ e^{-\int_{t}^{T} r\left( s\right) ds} \left[ \left( 1 + hk\right) P\left( T, T + h\right) - 1\right]^+\right\}= \left( 1 + hk\right) L \mathbb{E}_t^{\mathbb{Q}}\left\{ e^{-\int_{t}^{T} r\left( s\right) ds} \left[ P\left( T, T + h\right) - \frac{1}{1 + hk}\right]^+\right\}
$$

设 ${k}^* = \frac{1}{1 + hk}$，我们有：
$$
\text{floorlet}_t^i = \left( 1 + hk\right) L \mathbb{E}_t^{\mathbb{Q}}\left\{ e^{-\int_{t}^{T} r\left( s\right) ds} \left[ P\left( T, T + h\right) - {k}^*\right]^+\right\} \tag{1.53}
$$
根据前面的例子，通过将 $\mathbb{Q}$ 测度变换为前向测度 ${\mathbb{P}}^T$，我们得到：
$$
\text{floorlet}_t^i = \left( 1 + hk\right) L P\left( t, T\right) \mathbb{E}_t^{\mathbb{P}^T}\left[ \left( P\left( T, T + h\right) - {k}^*\right)^+\right] \tag{1.54}
$$
其中 $\mathbb{E}_t^{\mathbb{P}^T}\left[ \cdot\right]$ 表示在前向测度 $\mathbb{P}^T$ 下的期望。

定义前向折现因子 ${\kappa}_{t, T}$ 为：
$$
{\kappa}_{t, T} = \frac{P\left( t, T + h\right)}{P\left( t, T\right)} \tag{1.55}
$$

$$
= \frac{1}{1 + h L\left( t, T\right)} \tag{1.56}
$$
那么未来的前向折现因子 ${\kappa}_{T, T} = P\left( T, T + h\right)$，因此：
$$
\text{floorlet}_t^i = \left( 1 + hk\right) L P\left( t, T\right) \mathbb{E}_t^{\mathbb{P}^T}\left[ \left( {\kappa}_{T, T} - {k}^*\right)^+\right] \tag{1.57}
$$
因此，期望表示的是在前向测度 $\mathbb{P}^T$ 下，以 ${\kappa}_{t, T}$ 为标的，执行价格为 ${k}^*$ 的看涨期权。

#### 1.5.4 互换测度下的定价

另一个有用的测度是互换测度，${\mathbb{P}}^{n + 1, N}$，它使用 ${P}_{n + 1, N}\left( t\right)$ 作为计价单位，即前向零息债券价格，这在推导互换期权定价的可行解时非常有帮助，因此得名。为了说明互换测度的使用，我们将构建互换期权定价，使其成为一个在互换测度下的简单香草期权定价问题，这大大简化了可以用于定价互换期权的算法。

前向平价互换利率，${y}_{n, N}\left( t\right)$，定义为：
$$
{y}_{n, N}\left( t\right) = \frac{P\left( t, T_n\right) - P\left( t, T_N\right)}{\sum_{j = n + 1}^{N} \delta P\left( t, T_j\right)} = \frac{P\left( t, T_n\right) - P\left( t, T_N\right)}{{P}_{n + 1, N}\left( t\right)}
$$
其中 ${P}_{n + 1, N}\left( t\right)$ 被称为基点现值（PVBP）。

互换期权赋予持有人进入特定互换合约的权利，但不是义务。一个具有期权到期时间 ${T}_n$ 和互换到期时间 ${T}_N$ 的互换期权被称为 ${T}_n \times {T}_N$-互换期权。与互换期权相关的总期限互换是 ${T}_n + {T}_N$。一个支付者互换期权赋予持有人进入支付者互换的权利，而不是义务，可以看作是互换利率的看涨期权。该期权在时间 ${T}_n$，即期权到期时间，的收益为：
$$
\left[ V_{n, N}^{\text{Payer }}\left( T_n\right)\right]^+ = \left[ \left\{ 1 - P\left( T_n, T_N\right)\right\} - \kappa \sum_{j = n + 1}^{N} \delta P\left( T_n, T_j\right)\right]^+= \left[ y_{n, N}\left( T_n\right) P_{n + 1, N}\left( T_n\right) - \kappa P_{n + 1, N}\left( T_n\right)\right]^+= P_{n + 1, N}\left( T_n\right) \left[ y_{n, N}\left( T_n\right) - \kappa\right]^+
$$

其中 $\kappa$ 表示互换期权的执行利率。第二行直接从前向互换利率的定义得出。设 ${B}_t = \exp \left( \int_{0}^{t} r_s ds\right)$ 是时间 $t$ 的货币市场账户。假设不存在套利，支付者互换期权在时间 $t < T_n$ 的价值，记为 ${\mathbf{PS}}_t$，可以通过以下风险中性的条件期望来表示：
$$
\frac{{\mathbf{PS}}_t}{B_t} = \mathbb{E}_t^{\mathbb{Q}}\left\{ \frac{\left[ V_{n, N}^{\text{Payer }}\left( T_n\right)\right]^+}{B_{T_n}}\right\}= \mathbb{E}_t^{\mathbb{Q}}\left\{ \frac{P_{n + 1, N}\left( T_n\right)}{B_{T_n}} \left[ y_{n, N}\left( T_n\right) - K\right]^+\right\}
$$

我们使用 ${P}_{n + 1, N}\left( t\right)$ 作为计价单位来找到一个新的概率测度，${\mathbb{P}}^{n + 1, N}$，我们称之为互换测度。在互换测度下，我们可以证明：
$$
{\mathbf{PS}}_t = P_{n + 1, N}\left( t\right) \mathbb{E}_t^{\mathbb{P}^{n + 1, N}}\left\{ \left[ y_{n, N}\left( T_n\right) - K\right]^+\right\}
$$
注意，在这个互换测度下，相应的互换利率 ${y}_{n, N}\left( t\right)$ 是一个鞅。计价单位的变换明确地解释了为什么互换期权可以被看作是互换利率的看涨期权。

#### 1.5.5 份额测度下的定价

当计价单位是标的资产价格 ${S}_t$ 时，所使用的测度称为份额测度，记为 $\mathbb{S}$。因此，任何可交易的证券除以 ${S}_t$ 后，在份额测度下都是一个鞅。这意味着：
$$
\frac{C_t}{S_t} = \mathbb{E}_t^{\mathbb{S}}\left( \frac{C_T}{S_T}\right) \tag{1.58}
$$
对于执行价格为 $K$ 的看涨期权，我们可以写成：
$$
\frac{C\left( K\right)}{S_0} = \mathbb{E}^{\mathbb{S}}\left( \frac{\left( S_T - K\right)^+}{S_T}\right) \tag{1.59}
$$
如果我们假设证券价格 ${S}_T$ 始终为正，我们得到：
$$
\frac{C\left( K\right)}{S_0} = \mathbb{E}^{\mathbb{S}}\left( \left( 1 - \frac{K}{S_T}\right)^+\right) \tag{1.60}
$$
我们定义 $y = \ln \left( \frac{S_T}{K}\right)$，这意味着 $\frac{K}{S_T} = e^{-y}$，使用这个定义，我们可以将归一化的看涨期权价格重写如下：
$$
\frac{C\left( K\right)}{S_0} = \int_{0}^{\infty} \left( 1 - e^{-y}\right) f\left( y\right) dy \tag{1.61}
$$
其中 $f\left( y\right)$ 是 $y = \ln \left( S/K\right)$ 在份额测度下的概率密度函数。我们通过分部积分得到：
$$
\frac{C\left( K\right)}{S_0} = \int_{0}^{\infty} \left( 1 - e^{-y}\right) f\left( y\right) dy= \left. \left( 1 - e^{-y}\right) F\left( y\right) \right|_{0}^{\infty} - \int_{0}^{\infty} e^{-y} F\left( y\right) dy
\\
= \left. \left( F\left( y\right) - F\left( y\right) e^{-y}\right) \right|_{0}^{\infty} - \int_{0}^{\infty} e^{-y} F\left( y\right) dy= 1 - \int_{0}^{\infty} e^{-y} F\left( y\right) dy= \int_{0}^{\infty} e^{-y} dy - \int_{0}^{\infty} e^{-y} F\left( y\right) dy= \int_{0}^{\infty} \left( 1 - F\left( y\right)\right) e^{-y} dy
$$

因此，我们有：
$$
\frac{C\left( K\right)}{S_0} = \int_{0}^{\infty} \left( 1 - F\left( y\right)\right) e^{-y} dy
$$
对于给定的 $y$，表达式 $1 - F\left( y\right)$ 是 $\ln \left( S/K\right)$ 大于 $y$ 的概率。考虑到 $e^{-y}$ 是参数为 $\lambda = 1$ 的正指数随机变量的概率密度函数，归一化的看涨期权价格是在份额测度下股票价格的对数超过执行价格的对数加上一个独立的指数变量的概率 [70]，或者等价地：
$$
\frac{C\left( K\right)}{S_0} = P\left( \ln \left( S/K\right) > Y\right) \tag{1.62}
$$

$$
= P\left( \ln S - \ln K > Y\right) \tag{1.63}
$$

$$
= P\left( X - Y > \ln K\right) \tag{1.64}
$$

其中 $X$ 是在份额测度下股票的对数，$Y$ 是一个独立的指数变量，$K$ 是执行价格。

### 1.6 衍生品定价技术

衍生品是多面的金融工具，具有广泛的特点。它们的分类涉及多个因素，如欧洲期权与美国期权、路径依赖性以及多样的收益结构。本书旨在引导读者通过多种方法了解不同衍生品的定价复杂性。虽然我们无法讨论每一种衍生品结构，但我们将深入探讨最突出的几种。

#### 1.6.1 衍生品定价方法的总结

- 变换方法：当资产对数的特征函数可用时，这种方法适用，适用于具有欧洲收益结构或某些路径依赖结构（如单次敲出）的衍生品。

- 数值解法：用于马尔可夫过程，特别是在特征函数不可用或衍生品价格路径依赖时。这包括对偏微分方程（PDEs）和偏积分-微分方程（PIDEs）的解法。

- 蒙特卡洛模拟：对于非马尔可夫过程或高维过程以及表现出复杂路径依赖性的衍生品至关重要。

- 深度神经网络：这种方法可以以两种方式应用：

- 监督学习：网络使用包含参数集及其相应价格的- 监督学习：网络使用包含参数集及其相应价格的标记数据进行训练。

- 无监督学习：这种技术将神经网络集成到 PDE/PIDE 中，以确保其与任何参数集的一致性。

每种方法的优缺点将在第 7 章和第 8 章中详细探讨，以使读者对其应用有清晰的理解。

#### 1.6.2 定价模型的分类

- 无模型方法：变换方法和深度神经网络中的监督学习是这一类别的典型代表。这些方法在设置后基本上是通用的，且与模型无关。

- 模型依赖技术：这包括 PDE/PIDE 的数值解法、蒙特卡洛模拟和神经网络的无监督学习。深入理解这些方法的底层机制是必要的。

在优化定价模型的参数和微调过程中，我们将探讨优化例程和滤波技术，这些内容将在专门的一章中详细讨论。

#### 1.6.3 特殊主题

- 曲线构建：在信用和利率建模中至关重要，曲线构建技术有助于建立收益率曲线或互换曲线等。

- 期限结构模型：我们讨论了使今天的曲线内生化的过程，如仿射期限结构模型（ATSMs），这消除了对其显式考虑的必要性。

在整个本书中，我们的目标是提供一个全面的视角，展示每种定价方法如何与不同的金融模型和产品对齐，帮助你在动态的衍生品世界中取得成功。

### 问题

1. 推导 ${r}_t = \ln \left( {S}_t / {S}_0\right)$ 的特征函数，其中 ${r}_t$ 有两种可能性：(a) $a\%$，概率为 0.52；(b) $-a\%$，概率为 0.48。

2. 使用类似于推导 Heston 随机波动率模型特征函数的方法，推导 CIR 过程的特征函数。

3. 使用类似于推导方差伽玛过程特征函数的方法，推导正态逆高斯（NIG）过程的特征函数。

4. 推导 Heston 随机波动率模型特征函数的一种替代且简便的方法是首先：

(a) 证明 Heston 随机波动率模型是具有随机到达的几何布朗运动（因此 Heston 随机波动率可以称为 GBMSA）。

(b) 在验证这一点后，利用用于推导 VGSA 特征函数的方法来计算 Heston 随机波动率下标的对数过程的特征函数。

5. 利用问题 3 中得到的正态逆高斯过程的特征函数，利用用于推导 VGSA 特征函数的方法来计算 NIGSA 下标的对数过程的特征函数。

6. CGMY 的特征函数在第 1.4.7 节中给出。利用用于推导 VGSA 特征函数的方法来计算 CGMYSA 下标的对数过程的特征函数。

7. 通过重新计算示例 3 中的近似看涨期权，评估超参数 $B$ 对更长期限的敏感性，例如 $T = 5$。


---

## 第 2 章 通过变换技术定价衍生品

在本章中，我们将讨论使用变换技术为衍生品定价的方法。正如在第 1.2 节中所讨论的，给定资产价格分布的主要表示之一是其特征函数。资产价格分布的特征函数仅仅是其概率分布函数（PDF）的傅里叶变换。因此，可以通过傅里叶逆变换从特征函数中恢复其概率分布函数。这一点对于许多类模型尤为重要，正如在第 1.4 节中所讨论的，这些模型只有在特征函数表示下才有闭式解。我们将概述在各种不同模型下使用变换方法为衍生品定价的技术，重点介绍基于快速傅里叶变换（FFT）的技术、分数快速傅里叶变换以及最近开发的傅里叶余弦（COS）方法。最后，我们将考虑鞍点方法。

### 2.1 通过快速傅里叶变换定价衍生品

使用傅里叶变换为衍生品定价的第一个重要发展是由 Carr 和 Madan [69] 提出的。这一技术${}^{1}$涉及推导出在风险中性分布下衍生品预期价值的傅里叶变换，将这种变换表示为已知的特征函数和某些常数，并应用傅里叶逆变换以恢复衍生品价格。

虽然这种方法在数值期权定价方面是一个重要的突破，但正如本书中讨论的大多数方法一样，快速傅里叶变换（FFT）定价方法涉及多个权衡。这种方法非常有用，因为它允许我们在任何具有已知特征函数的模型下高效地为衍生品定价，这涵盖了第 1.4 节中讨论的大多数模型。此外，当使用基于 FFT 的傅里叶逆变换时，这种方法非常快，可以在 $O\left( {n\ln \left( n\right) }\right)$ 时间内解决期权定价问题，不仅包括在所需执行价格处的期权价格，还包括在 $n$ 个不同执行价格处的期权价格。虽然有一些限制，即哪些期权价格可以免费计算，但我们能够从这种方法中提取比其他许多方法更多的信息，这对于校准非常重要。

然而，这种方法不能用于为所有衍生品定价。特别是，如最初提出的方法仅限于完全路径无关的欧式衍生品定价。此外，这种方法的推导非常依赖于收益类型，最初的文章中只提出了两种收益类型。因此，我们仅限于一个虽小但重要的衍生品收益子集。此外，为了使这种方法生效，我们需要定义一个阻尼因子 $\alpha$，其最优值必须确定。最后，当待定价的期权变得非常价外时，这种方法的准确性会下降${}^{2}$。

---

${}^{1}$ 在 Carr 和 Madan [69] 的工作之前，Bakshi 等人 [25] 开发了一种定价算法，涉及计算从各自特征函数的逆变换中恢复的风险中性概率 ${\Pi }_{1}$ 和 ${\Pi }_{2}$。在这个框架下的定价涉及两次逆变换，而不是一次 [69]，并且特征函数的计算不如 [69] 中的情况直接。类似的处理可以在 [167]、[32] 和 [268] 中看到。

---

模型：

所有存在资产价格分布特征函数的模型。

期权类型：

严格路径无关的欧式期权。有限的到期收益集。

**优点**

1. 允许在任何具有特征函数的模型下定价
2. 快速，$n$ 个期权价格在 $O\left( {n\ln \left( n\right) }\right)$ 时间内计算
3. 一次运行生成 $n$ 个期权价格

**缺点**

1. 仅限于路径无关的欧式期权
2. 有限的到期收益集，每种收益都需要重新推导
3. 需要估计适当的 $\alpha$
4. 对于高度价外的期权，准确性较低

#### 2.1.1 通过傅里叶变换定价看涨期权

正如在第 1.5 节中观察到的，对于具有已知概率密度函数（PDF）的风险中性价格分布的证券，我们可以将收益与 PDF 积分，并通过某种数值积分程序近似该积分下的面积，从而获得近似的期权价格。在大多数情况下，我们不知道 PDF 的解析形式或积分形式。然而，我们通常可以找到标的证券的特征函数，或者更准确地说，是标的证券对数的特征函数，无论是解析形式还是半解析形式。[69] 中显示，如果我们有特征函数的解析形式，我们可以通过傅里叶逆变换高效地获得期权溢价。根据 [69] 中的工作，我们首先通过标的证券对数价格的密度来构建欧式看涨期权的定价问题，这使我们能够使用傅里叶变换来获得期权溢价。

正如在第 1.5 节中所示，许多衍生工具，包括普通期权、上限、下限和互换期权，都可以表示为简单的看涨或看跌期权。因此，我们的设置以通用形式呈现。

---

${}^{2}$ 当看涨期权的标的资产价格低于看涨期权的执行价格时，看涨期权变为价外。当看跌期权的标的资产价格高于看跌期权的执行价格时，看跌期权变为价外。

---

##### 2.1.1.1 几何情况

在几何情况下，标的证券的价格遵循几何过程，这意味着在整个证券的生命周期中价格保持正值，因此我们将使用标的证券对数的特征函数。我们从以下符号和定义开始：

- ${X}_{0}$ 为今天的标的证券价格
- ${X}_{T}$ 为 $T$ 时刻的标的证券价格
- $f\left( {X}_{T}\right)  \equiv  f\left( {{X}_{T} \mid  {X}_{0}}\right)$ 为 ${X}_{T}$ 在某个等价鞅测度下的概率密度函数${}^{3}$
- $q\left( {x}_{T}\right)  \equiv  q\left( {{x}_{T} \mid  {x}_{0}}\right)$ 为标的证券对数 ${x}_{T} = \ln \left( {X}_{T}\right)$ 的概率密度
- $k = \ln \left( K\right)$ 为执行价格的对数
- ${C}_{T}\left( k\right)$ 为执行价格 $K = {e}^{k}$ 的 $T$ 时刻到期看涨期权的价格
- $\Phi \left( \nu \right)$ 为标的证券对数 ${x}_{T}$ 的特征函数，即

$$
\Phi \left( \nu \right)  = {\int }_{-\infty }^{\infty }{e}^{{i\nu }{x}_{T}}q\left( {x}_{T}\right) d{x}_{T}
$$

欧式看涨期权价格 ${C}_{T}\left( k\right)$ 可以表示为

$$
\mathrm{C}{\mathbb{E}}_{0}\left\lbrack  {\left( {X}_{T} - K\right) }^{ + }\right\rbrack   = \mathrm{C}{\int }_{K}^{\infty }\left( {{X}_{T} - K}\right) f\left( {X}_{T}\right) d{X}_{T}= \mathrm{C}{\int }_{k}^{\infty }\left( {{e}^{{x}_{T}} - {e}^{k}}\right) q\left( {x}_{T}\right) d{x}_{T}= \mathrm{C}{\int }_{k}^{\infty }\left( {{e}^{x} - {e}^{k}}\right) q\left( x\right) {dx}= {C}_{T}\left( k\right)
$$

其中常数系数 $\mathrm{C}$ 取决于我们所取期望的等价鞅测度；见第 1.5 节。注意，为了简化，我们在最后一个积分方程中省略了下标 $T$。现在我们已经将期权价格 ${C}_{T}\left( k\right)$ 表示为对数价格密度的形式，我们使用这种表示来计算 ${C}_{T}\left( k\right)$ 的傅里叶变换，我们将其定义为 ${\Psi }_{T}\left( \nu \right)$。

$$
{\Psi }_{T}\left( \nu \right)  = {\int }_{-\infty }^{\infty }{e}^{i\nu k}{C}_{T}\left( k\right) {dk}= {\int }_{-\infty }^{\infty }{e}^{i\nu k}\left( {\mathrm{C}{\int }_{k}^{\infty }\left( {{e}^{x} - {e}^{k}}\right) q\left( x\right) {dx}}\right) {dk}
\\
= \mathrm{C}{\int }_{-\infty }^{\infty }{\int }_{-\infty }^{x}{e}^{i\nu k}\left( {{e}^{x} - {e}^{k}}\right) q\left( x\right) {dkdx}= \mathrm{C}{\int }_{-\infty }^{\infty }q\left( x\right) \left( {{\int }_{-\infty }^{x}{e}^{i\nu k}\left( {{e}^{x} - {e}^{k}}\right) {dk}}\right) {dx} \tag{2.1}
$$

在这里，我们使用了富比尼定理来改变上述推导中的积分顺序。这使我们能够评估内积分

$$
{\int }_{-\infty }^{x}{e}^{i\nu k}\left( {{e}^{x} - {e}^{k}}\right) {dk} = {\int }_{-\infty }^{x}{e}^{i\nu k}{e}^{x}{dk} - {\int }_{-\infty }^{x}{e}^{i\nu k}{e}^{k}{dk} = {\left. {e}^{x}\frac{{e}^{i\nu k}}{i\nu }\right| }_{-\infty }^{x} - {\left. \frac{{e}^{\left( {{i\nu } + 1}\right) k}}{{i\nu } + 1}\right| }_{-\infty }^{x}
$$

我们看到第一个积分不收敛，因此第一个项是未定义的。正如在 [69] 中讨论的，我们通过定义

$$
{\mathrm{c}}_{T}\left( k\right)  = {e}^{\alpha k}{C}_{T}\left( k\right)
$$

即期权溢价乘以执行价格的指数，来重新表述问题。这在内积分中成为一个阻尼成分，强制收敛并允许计算傅里叶变换。我们重新定义 ${\Psi }_{T}\left( \nu \right)$ 为修改后的期权价格 ${c}_{T}\left( k\right)$ 的傅里叶变换，并重新推导，我们得到

$$
{\Psi }_{T}\left( \nu \right)  = {\int }_{-\infty }^{\infty }{e}^{i\nu k}{\mathrm{c}}_{T}\left( k\right) {dk}= {\int }_{-\infty }^{\infty }{e}^{i\nu k}\left( {\mathrm{C}{e}^{\alpha k}{\int }_{k}^{\infty }\left( {{e}^{x} - {e}^{k}}\right) q\left( x\right) {dx}}\right) {dk}
\\
= \mathrm{C}{\int }_{-\infty }^{\infty }{\int }_{-\infty }^{x}{e}^{\left( {\alpha  + {i\nu }}\right) k}\left( {{e}^{x} - {e}^{k}}\right) q\left( x\right) {dkdx}= \mathrm{C}{\int }_{-\infty }^{\infty }q\left( x\right) \left( {{\int }_{-\infty }^{x}{e}^{\left( {\alpha  + {i\nu }}\right) k}\left( {{e}^{x} - {e}^{k}}\right) {dk}}\right) {dx} \tag{2.1}
$$

引入阻尼因子后，内积分现在收敛。

$$
{\int }_{-\infty }^{x}{e}^{\left( {\alpha  + {i\nu }}\right) k}\left( {{e}^{x} - {e}^{k}}\right) {dk} = {\left. {e}^{x}\frac{{e}^{\left( {\alpha  + {i\nu }}\right) k}}{\left( \alpha  + i\nu \right) }\right| }_{-\infty }^{x} - {\left. \frac{{e}^{\left( {\alpha  + {i\nu } + 1}\right) k}}{\left( \alpha  + i\nu  + 1\right) }\right| }_{-\infty }^{x}
$$

对于 $\alpha  > 0$，两个项在负无穷处都消失，因此我们有

$$
{\int }_{-\infty }^{x}{e}^{\left( {\alpha  + {i\nu }}\right) k}\left( {{e}^{x} - {e}^{k}}\right) {dk} = {e}^{x}\frac{{e}^{\left( {\alpha  + {i\nu }}\right) x}}{\left( \alpha  + i\nu \right) } - \frac{{e}^{\left( {\alpha  + {i\nu } + 1}\right) x}}{\left( \alpha  + i\nu  + 1\right) }= \frac{{e}^{\left( {\alpha  + {i\nu } + 1}\right) x}}{\left( {\alpha  + {i\nu }}\right) \left( {\alpha  + {i\nu } + 1}\right) } \tag{2.2}
$$

评估了内积分后，我们可以使用标的证券对数的特征函数 $\Phi \left( \nu \right)$ 来计算修改后的期权溢价的傅里叶变换。将 (2.2) 代入 (2.1)，我们得到

$$
{\Psi }_{T}\left( \nu \right)  = \mathrm{C}{\int }_{-\infty }^{\infty }q\left( x\right) \frac{{e}^{\left( {\alpha  + {i\nu } + 1}\right) x}}{\left( {\alpha  + {i\nu }}\right) \left( {\alpha  + {i\nu } + 1}\right) }{dx}= \frac{\mathrm{C}}{\left( {\alpha  + {i\nu }}\right) \left( {\alpha  + {i\nu } + 1}\right) }{\int }_{-\infty }^{\infty }{e}^{\left( {\alpha  + {i\nu } + 1}\right) x}q\left( x\right) {dx}
\\
= \frac{\mathrm{C}}{\left( {\alpha  + {i\nu }}\right) \left( {\alpha  + {i\nu } + 1}\right) }{\int }_{-\infty }^{\infty }{e}^{i\left( {\nu  - \left( {\alpha  + 1}\right) i}\right) x}q\left( x\right) {dx}= \frac{\mathrm{C}}{\left( {\alpha  + {i\nu }}\right) \left( {\alpha  + {i\nu } + 1}\right) }\Phi \left( {\nu  - \left( {\alpha  + 1}\right) i}\right)
$$

因此，如果我们有标的证券对数的特征函数 $\Phi \left( \nu \right)$，我们可以通过傅里叶逆变换解析地计算修改后的看涨期权的傅里叶变换 ${\Psi }_{T}\left( \nu \right)$

$$
{\Psi }_{T}\left( \nu \right)  = {\int }_{-\infty }^{\infty }{e}^{i\nu k}{\mathrm{c}}_{T}\left( k\right) {dk}= \frac{\mathrm{C}}{\left( {\alpha  + {i\nu }}\right) \left( {\alpha  + {i\nu } + 1}\right) }\Phi \left( {\nu  - \left( {\alpha  + 1}\right) i}\right)  \tag{2.3}
$$

有了 ${\Psi }_{T}\left( \nu \right)$ 的解析形式，并且知道它是修改后的看涨期权价格的傅里叶变换，我们可以使用傅里叶逆变换来获得 ${C}_{T}\left( k\right)$ 的表达式，即

$$
{C}_{T}\left( k\right)  = \frac{{e}^{-{\alpha k}}}{2\pi }{\int }_{-\infty }^{\infty }{e}^{-{i\nu k}}{\Psi }_{T}\left( \nu \right) {d\nu } \tag{2.4}
$$

我们知道 ${C}_{T}\left( k\right)$ 是一个实数，这意味着它的傅里叶变换 ${\Psi }_{T}\left( \nu \right)$ 在实部是偶函数，在虚部是奇函数。由于我们只对期权价格的实部感兴趣，我们可以将其视为一个偶函数，因此我们得到

$$
{C}_{T}\left( k\right)  = \frac{{e}^{-{\alpha k}}}{\pi }{\int }_{0}^{\infty }{e}^{-{i\nu k}}{\Psi }_{T}\left( \nu \right) {d\nu } \tag{2.5}
$$

这是看涨期权溢价，其中 ${\Psi }_{T}\left( \nu \right)$ 是由 (2.3) 给出的已知函数，$\alpha$ 是某个合适的参数 $\alpha  > 0$。

##### 2.1.1.2 算术情况

在算术情况下，标的物遵循一个算术过程，这可以是两个或多个证券之间的差值，例如在价差期权的情况下，标的物的价格在其生命周期中可以正负变化。因此，我们使用标的物的特征函数，而不是其对数的特征函数。我们从以下符号和定义开始：

- ${X}_{0}$ 为今天的标的物价值
- ${X}_{T}$ 为 $T$ 时刻的标的物价值
- $f\left( {X}_{T}\right)  \equiv  f\left( {{X}_{T} \mid  {X}_{0}}\right)$ 为 ${X}_{T}$ 在某个等价鞅测度下的概率密度函数
- $K$ 为标的物合约的执行价值
- ${C}_{T}\left( K\right)$ 为执行价格 $K$ 的 $T$ 时刻到期看涨期权的价格
- $\phi \left( \nu \right)$ 为标的物 ${X}_{T}$ 的特征函数，即

$$
\phi \left( \nu \right)  = {\int }_{-\infty }^{\infty }{e}^{{i\nu }{X}_{T}}f\left( {X}_{T}\right) d{X}_{T}
$$

欧式看涨期权价格 ${C}_{T}\left( K\right)$ 可以表示为

$$
\mathrm{C}{\mathbb{E}}_{t}\left\lbrack  {\left( {X}_{T} - K\right) }^{ + }\right\rbrack   = \mathrm{C}{\int }_{K}^{\infty }\left( {{X}_{T} - K}\right) f\left( {X}_{T}\right) d{X}_{T}= {C}_{T}\left( K\right)
$$

与几何情况一样，我们通过乘以一个阻尼因子来定义修改后的期权价格 ${\mathrm{c}}_{T}\left( K\right)$

$$
{\mathrm{c}}_{T}\left( K\right)  = {e}^{\alpha K}{C}_{T}\left( K\right)
$$

修改后的期权价格的傅里叶变换 ${\psi }_{T}\left( \nu \right)$ 可以如下推导

$$
{\psi }_{T}\left( \nu \right)  = {\int }_{-\infty }^{\infty }{e}^{i\nu K}{\mathrm{c}}_{T}\left( K\right) {dK}= {\int }_{-\infty }^{\infty }{e}^{i\nu K}\left( {\mathrm{C}{e}^{\alpha K}{\int }_{K}^{\infty }\left( {{X}_{T} - K}\right) f\left( {X}_{T}\right) d{X}_{T}}\right) {dK}
\\
= \mathrm{C}{\int }_{-\infty }^{\infty }{\int }_{-\infty }^{{X}_{T}}{e}^{\left( {\alpha  + {i\nu }}\right) K}\left( {{X}_{T} - K}\right) f\left( {X}_{T}\right) {dKd}{X}_{T}= \mathrm{C}{\int }_{-\infty }^{\infty }f\left( {X}_{T}\right) \left( {{\int }_{-\infty }^{{X}_{T}}{e}^{\left( {\alpha  + {i\nu }}\right) K}\left( {{X}_{T} - K}\right) {dK}}\right) d{X}_{T}
$$

内积分可以通过分部积分法求解，如下所示

$$
{\int }_{-\infty }^{X}{e}^{\left( {\alpha  + {i\nu }}\right) K}\left( {X - K}\right) {dK} = {\left. X\frac{{e}^{\left( {\alpha  + {i\nu }}\right) K}}{\left( \alpha  + i\nu \right) }\right| }_{-\infty }^{X} - {\int }_{-\infty }^{X}K{e}^{\left( {\alpha  + {i\nu }}\right) K}{dK}= X\frac{{e}^{\left( {\alpha  + {i\nu }}\right) X}}{\left( \alpha  + i\nu \right) } - \left( {{\left. K\frac{{e}^{\left( {\alpha  + {i\nu }}\right) K}}{\left( \alpha  + i\nu \right) }\right| }_{-\infty }^{X} - {\int }_{-\infty }^{X}\frac{{e}^{\left( {\alpha  + {i\nu }}\right) K}}{\alpha  + {i\nu }}{dK}}\right)
$$

当 $K$ 接近 $- \infty$ 时，可以使用洛必达法则来证明 $K{e}^{\left( {\alpha  + {i\nu }}\right) K}$ 变为零

$$
\mathop{\lim }\limits_{{K \rightarrow   - \infty }}K{e}^{\left( {\alpha  + {i\nu }}\right) K} = \mathop{\lim }\limits_{{K \rightarrow   - \infty }}\frac{K}{{e}^{-\left( {\alpha  + {i\nu }}\right) K}}= \mathop{\lim }\limits_{{K \rightarrow   - \infty }}\frac{1}{-\left( {\alpha  + {i\nu }}\right) {e}^{-\left( {\alpha  + {i\nu }}\right) K}}= 0
$$

因此，内积分的最终解可以写为

$$
{\int }_{-\infty }^{X}{e}^{\left( {\alpha  + {i\nu }}\right) K}\left( {X - K}\right) {dK} = {\left. X\frac{{e}^{\left( {\alpha  + {iv}}\right) K}}{\alpha  + {iv}} - K\frac{{e}^{\left( {\alpha  + {iv}}\right) K}}{\left( \alpha  + iv\right) } + \frac{{e}^{\left( {\alpha  + {iv}}\right) K}}{{\left( \alpha  + iv\right) }^{2}}\right| }_{-\infty }^{X}= \frac{{e}^{\left( {\alpha  + {i\nu }}\right) X}}{{\left( \alpha  + i\nu \right) }^{2}}
$$

因此，使用标的物的特征函数 $\phi \left( \nu \right)$，修改后的期权溢价的特征函数 ${\psi }_{T}\left( \nu \right)$ 为

$$
{\psi }_{T}\left( \nu \right)  = \frac{\mathrm{C}}{{\left( \alpha  + i\nu \right) }^{2}}{\int }_{-\infty }^{\infty }{e}^{\left( {\alpha  + {i\nu }}\right) X}f\left( X\right) {dX}= \frac{\mathrm{C}}{{\left( \alpha  + i\nu \right) }^{2}}{\int }_{-\infty }^{\infty }{e}^{i\left( {\nu  - {\alpha i}}\right) X}f\left( X\right) {dX}= \frac{\mathrm{C}}{{\left( \alpha  + i\nu \right) }^{2}}\phi \left( {\nu  - {\alpha i}}\right)
$$

遵循与几何情况相同的论点，我们得到

$$
{C}_{T}\left( K\right)  = \frac{{e}^{-{\alpha K}}}{\pi }{\int }_{0}^{\infty }{e}^{-{i\nu k}}{\psi }_{T}\left( \nu \right) {d\nu } \tag{2.6}
$$

这是看涨期权溢价，其中 ${\psi }_{T}\left( \nu \right)$ 是已知函数，$\alpha$ 是某个合适的参数 $\alpha  > 0$。

#### 2.1.2 通过傅里叶变换定价看跌期权

看跌期权的价格也可以通过傅里叶变换以类似的方式计算。有人可能会疑惑为什么需要这种表述，因为看跌期权的价格应该可以通过看涨期权的价格和标的物的前向价格通过看涨-看跌平价关系恢复。然而，看涨和看跌期权都有买卖报价，因此看涨-看跌平价关系并不完全成立。事实上，对于这两种合约，都有一个可能的真实价格范围。因此，看跌期权的表述变得必要。

##### 2.1.2.1 几何形式

使用相同的符号，${P}_{T}\left( k\right)$ 为执行价格 $K = {e}^{k}$ 的 $T$ 时刻到期看跌期权的价格，可以表示如下：

$$
\mathrm{C}{\mathbb{E}}_{t}\left\lbrack  {\left( K - {X}_{T}\right) }^{ + }\right\rbrack   = \mathrm{C}{\int }_{0}^{K}\left( {K - {X}_{T}}\right) f\left( {X}_{T}\right) d{X}_{T}= \mathrm{C}{\int }_{-\infty }^{k}\left( {{e}^{k} - {e}^{{x}_{T}}}\right) q\left( {x}_{T}\right) d{x}_{T}= \mathrm{C}{\int }_{-\infty }^{k}\left( {{e}^{k} - {e}^{x}}\right) q\left( x\right) {dx}= {P}_{T}\left( k\right)
$$

与之前一样，我们通过定义修改后的看跌期权来重新表述问题

$$
{p}_{T}\left( k\right)  = {e}^{\alpha k}{P}_{T}\left( k\right)
$$

我们重新定义 ${\Psi }_{T}\left( \nu \right)$ 为修改后的期权价格 ${p}_{T}\left( k\right)$ 的特征函数，并进行相同的推导，我们得到

$$
{\Psi }_{T}\left( \nu \right)  = {\int }_{-\infty }^{\infty }{e}^{i\nu k}{p}_{T}\left( k\right) {dk}
= \mathrm{C}{\int }_{-\infty }^{\infty }{e}^{i\nu k}\left( {{e}^{\alpha k}{\int }_{-\infty }^{k}\left( {{e}^{k} - {e}^{x}}\right) q\left( x\right) {dx}}\right) {dk}
\\
= \mathrm{C}{\int }_{-\infty }^{\infty }{\int }_{x}^{\infty }{e}^{\left( {\alpha  + {i\nu }}\right) k}\left( {{e}^{k} - {e}^{x}}\right) q\left( x\right) {dkdx}= \mathrm{C}{\int }_{-\infty }^{\infty }q\left( x\right) \left( {{\int }_{x}^{\infty }{e}^{\left( {\alpha  + {i\nu }}\right) k}\left( {{e}^{k} - {e}^{x}}\right) {dk}}\right) {dx}
$$

引入阻尼因子后，内积分收敛，我们得到

$$
{\int }_{x}^{\infty }{e}^{\alpha k}{e}^{i\nu k}\left( {{e}^{k} - {e}^{x}}\right) {dk} = {\int }_{x}^{\infty }{e}^{\left( {\alpha  + {i\nu }}\right) k}\left( {{e}^{k} - {e}^{x}}\right) {dk}= {\left. \frac{{e}^{\left( {\alpha  + {i\nu } + 1}\right) k}}{\left( \alpha  + i\nu  + 1\right) }\right| }_{x}^{\infty } - {\left. {e}^{x}\frac{{e}^{\left( {\alpha  + {i\nu }}\right) k}}{\left( \alpha  + i\nu \right) }\right| }_{x}^{\infty }
$$

对于 $\alpha  < 0$，两个项在无穷远处都消失，因此我们有

$$
{\int }_{x}^{\infty }{e}^{\left( {\alpha  + {i\nu }}\right) k}\left( {{e}^{k} - {e}^{x}}\right) {dk} =  - \frac{{e}^{\left( {\alpha  + {i\nu } + 1}\right) x}}{\left( \alpha  + i\nu  + 1\right) } + {e}^{x}\frac{{e}^{\left( {\alpha  + {i\nu }}\right) x}}{\left( \alpha  + i\nu \right) }= \frac{{e}^{\left( {\alpha  + {i\nu } + 1}\right) x}}{\left( {\alpha  + {i\nu }}\right) \left( {\alpha  + {i\nu } + 1}\right) }
$$

与看涨期权的情况一样，我们可以使用标的物对数价格的特征函数 $\Phi \left( \nu \right)$ 来计算修改后的期权溢价的特征函数。

$$
{\Psi }_{T}\left( \nu \right)  = \mathrm{C}{\int }_{-\infty }^{\infty }q\left( x\right) \frac{{e}^{\left( {\alpha  + {i\nu } + 1}\right) x}}{\left( {\alpha  + {i\nu }}\right) \left( {\alpha  + {i\nu } + 1}\right) }{dx}= \frac{\mathrm{C}}{\left( {\alpha  + {i\nu }}\right) \left( {\alpha  + {i\nu } + 1}\right) }{\int }_{-\infty }^{\infty }{e}^{\left( {\alpha  + {i\nu } + 1}\right) x}q\left( x\right) {dx}
\\
= \frac{\mathrm{C}}{\left( {\alpha  + {i\nu }}\right) \left( {\alpha  + {i\nu } + 1}\right) }{\int }_{-\infty }^{\infty }{e}^{i\left( {\nu  - \left( {\alpha  + 1}\right) i}\right) x}q\left( x\right) {dx}= \frac{\mathrm{C}}{\left( {\alpha  + {i\nu }}\right) \left( {\alpha  + {i\nu } + 1}\right) }\Phi \left( {\nu  - \left( {\alpha  + 1}\right) i}\right)
$$

有了标的物价格对数的特征函数 $\Phi \left( \nu \right)$，我们可以计算修改后的看跌期权的傅里叶变换 ${\Psi }_{T}\left( \nu \right)$

$$
{\Psi }_{T}\left( \nu \right)  = {\int }_{-\infty }^{\infty }{e}^{i\nu k}{p}_{T}\left( k\right) {dk}= \frac{\mathrm{C}}{\left( {\alpha  + {i\nu }}\right) \left( {\alpha  + {i\nu } + 1}\right) }\Phi \left( {\nu  - \left( {\alpha  + 1}\right) i}\right)  \tag{2.7}
$$

有了 ${\Psi }_{T}\left( \nu \right)$ 的解析形式，即修改后的看跌期权价格的傅里叶变换，我们可以通过傅里叶逆变换获得 ${P}_{T}\left( k\right)$ 的表达式，即

$$
{P}_{T}\left( k\right)  = \frac{{e}^{-{\alpha k}}}{2\pi }{\int }_{-\infty }^{\infty }{e}^{-{i\nu k}}{\Psi }_{T}\left( \nu \right) {d\nu } \tag{2.8}
$$

使用与看涨期权相同的论点，我们得到

$$
{P}_{T}\left( k\right)  = \frac{{e}^{-{\alpha k}}}{\pi }{\int }_{0}^{\infty }{e}^{-{i\nu k}}{\Psi }_{T}\left( \nu \right) {d\nu } \tag{2.9}
$$

这是看跌期权溢价，其中 ${\Psi }_{T}\left( \nu \right)$ 是由 (2.7) 给出的已知函数，$\alpha$ 是某个合适的参数 $\alpha  < 0$。

##### 2.1.2.2 算术情况

使用相同的符号，欧式看跌期权价格 ${P}_{T}\left( K\right)$ 可以表示为

$$
\mathrm{C}{\mathbb{E}}_{t}\left\lbrack  {\left( K - {X}_{T}\right) }^{ + }\right\rbrack   = \mathrm{C}{\int }_{-\infty }^{K}\left( {K - {X}_{T}}\right) f\left( {X}_{T}\right) d{X}_{T}= {P}_{T}\left( K\right)
$$

与看涨期权的推导类似，我们可以通过乘以一个阻尼因子来定义修改后的期权价格 ${p}_{T}\left( K\right)$

$$
{\mathrm{p}}_{T}\left( K\right)  = {e}^{\alpha K}{P}_{T}\left( K\right)
$$

修改后的期权价格的傅里叶变换 ${\psi }_{T}\left( \nu \right)$ 可以如下推导

$$
{\psi }_{T}\left( \nu \right)  = {\int }_{-\infty }^{\infty }{e}^{i\nu K}{\mathrm{p}}_{T}\left( K\right) {dK}= {\int }_{-\infty }^{\infty }{e}^{i\nu K}\left( {\mathrm{C}{e}^{\alpha K}{\int }_{-\infty }^{K}\left( {K - X}\right) f\left( X\right) {dX}}\right) {dK}
\\
= \mathrm{C}{\int }_{-\infty }^{\infty }{\int }_{X}^{\infty }{e}^{\left( {\alpha  + {i\nu }}\right) K}\left( {K - X}\right) f\left( X\right) {dKdX}= \mathrm{C}{\int }_{-\infty }^{\infty }f\left( X\right) \left( {{\int }_{X}^{\infty }{e}^{\left( {\alpha  + {i\nu }}\right) K}\left( {K - X}\right) {dK}}\right) {dX}
$$

内积分可以如下计算

$$
{\int }_{X}^{\infty }{e}^{\left( {\alpha  + {i\nu }}\right) K}\left( {K - X}\right) {dK} = {\int }_{X}^{\infty }K{e}^{\left( {\alpha  + {i\nu }}\right) K}{dK} - {\left. X\frac{{e}^{\left( {\alpha  + {i\nu }}\right) K}}{\left( \alpha  + i\nu \right) }\right| }_{X}^{\infty }= \left( {{\left. K\frac{{e}^{\left( {\alpha  + {i\nu }}\right) K}}{\left( \alpha  + i\nu \right) }\right| }_{X}^{\infty } - {\int }_{X}^{\infty }\frac{{e}^{\left( {\alpha  + {i\nu }}\right) K}}{\alpha  + {i\nu }}{dK}}\right)  + X\frac{{e}^{\left( {\alpha  + {i\nu }}\right) X}}{\left( \alpha  + i\nu \right) }
$$

引入阻尼因子后，内积分现在收敛

$$
{\int }_{X}^{\infty }{e}^{\left( {\alpha  + {i\nu }}\right) K}\left( {K - X}\right) {dK} = \frac{{e}^{\left( {\alpha  + {i\nu }}\right) X}}{{\left( \alpha  + i\nu \right) }^{2}}
$$

因此，使用标的物价格的特征函数 $\phi \left( \nu \right)$，修改后的期权溢价的特征函数 ${\psi }_{T}\left( \nu \right)$ 为

$$
{\psi }_{T}\left( \nu \right)  = \frac{\mathrm{C}}{{\left( \alpha  + i\nu \right) }^{2}}{\int }_{-\infty }^{\infty }{e}^{\left( {\alpha  + {i\nu }}\right) X}f\left( X\right) {dX}= \frac{\mathrm{C}}{{\left( \alpha  + i\nu \right) }^{2}}{\int }_{-\infty }^{\infty }{e}^{i\left( {\nu  - {\alpha i}}\right) X}f\left( X\right) {dX}= \frac{\mathrm{C}}{{\left( \alpha  + i\nu \right) }^{2}}\phi \left( {\nu  - {\alpha i}}\right)
$$

遵循相同的论点并跳过一些步骤，我们得到

$$
{P}_{T}\left( K\right)  = \frac{{e}^{-{\alpha K}}}{\pi }{\int }_{0}^{\infty }{e}^{-{i\nu k}}{\psi }_{T}\left( \nu \right) {d\nu } \tag{2.10}
$$

这是看跌期权溢价，其中 ${\psi }_{T}\left( \nu \right)$ 是已知函数，$\alpha$ 是某个合适的参数 $\alpha  < 0$。

#### 2.1.3 评估定价积分

我们已经将定价问题转化为一个定积分，其中被积函数是特征函数的已知函数。为了定价期权，我们只需要数值地评估这个积分。这里，我们只关注看涨期权。将其扩展到看跌期权应该是直接的。

##### 2.1.3.1 数值积分

迄今为止介绍的傅里叶技术为我们提供了一种方法，用于计算那些没有解析形式的概率密度函数（PDF）但过程的特征函数在解析形式上已知的模型/过程的期权价格。然而，我们仍然需要评估积分以获得期权溢价。有许多方法可以数值地评估定积分。我们使用梯形法则并将其扩展到辛普森法则。

我们从重写 (2.5) 开始

$$
{C}_{T}\left( k\right)  = \frac{{e}^{-{\alpha k}}}{\pi }{\int }_{0}^{\infty }{e}^{-{i\nu k}}{\Psi }_{T}\left( \nu \right) {d\nu } \tag{2.11}
$$

正如提到的，这个积分可以使用简单的数值积分技术轻松计算。首先，我们通过定义 $B$ 为积分的上限来近似这个积分。我们可以使用梯形法则数值地积分这个截断的积分。我们让 $N$ 为等间距区间的数量，${\Delta \nu } = \frac{B}{N} = \eta$ 为积分点之间的距离，${\nu }_{j} = \left( {j - 1}\right) \eta$ 为积分区间的端点，$j = 1,\ldots , N + 1$。应用梯形法则，我们得到

$$
{C}_{T}\left( k\right)  = \frac{{e}^{-{\alpha k}}}{\pi }{\int }_{0}^{\infty }{e}^{-{i\nu k}}{\Psi }_{T}\left( \nu \right) {d\nu }\approx  \frac{{e}^{-{\alpha k}}}{\pi }{\int }_{0}^{B}{e}^{-{i\nu k}}{\Psi }_{T}\left( \nu \right) {d\nu }
\\
= \frac{{e}^{-{\alpha k}}}{\pi }\mathop{\sum }\limits_{{j = 1}}^{N}{\int }_{{\nu }_{j}}^{{\nu }_{j + 1}}{e}^{-{i\nu k}}{\Psi }_{T}\left( \nu \right) {d\nu }\approx  \frac{{e}^{-{\alpha k}}}{\pi }\mathop{\sum }\limits_{{j = 1}}^{N}\frac{\eta }{2}\left( {{e}^{-i{\nu }_{j}k}{\Psi }_{T}\left( {\nu }_{j}\right)  + {e}^{-i{\nu }_{j + 1}k}{\Psi }_{T}\left( {\nu }_{j + 1}\right) }\right)
\\
= \frac{{e}^{-{\alpha k}}}{\pi }\left( {{e}^{-i{\nu }_{1}k}{\Psi }_{T}\left( {\nu }_{1}\right)  + 2{e}^{-i{\nu }_{2}k}{\Psi }_{T}\left( {\nu }_{2}\right)  + \cdots  + 2{e}^{-i{\nu }_{N}k}{\Psi }_{T}\left( {\nu }_{N}\right) }\right.\left. {+{e}^{-i{\nu }_{N + 1}k}{\Psi }_{T}\left( {\nu }_{N + 1}\right) }\right) \frac{\eta }{2}
$$

由于这些项呈指数衰减，我们可以省略最后一个项，使其适合快速傅里叶变换。因此，我们得到

$$
{C}_{T}\left( k\right)  \approx  \frac{{e}^{-{\alpha k}}}{\pi }\mathop{\sum }\limits_{{j = 1}}^{N}{e}^{-i{\nu }_{j}k}{\Psi }_{T}\left( {\nu }_{j}\right) {w}_{j} \tag{2.12}
$$

其中 ${w}_{j} = \frac{\eta }{2}\left( {2 - {\delta }_{j - 1}}\right)$ 且

$$
{\delta }_{j} = \left\{  \begin{matrix} 1 & j = 0 \\  0 & \text{ otherwise } \end{matrix}\right.
$$

为了获得更准确的结果，我们也可以使用辛普森法则，这将产生与之前相同的求和，但求和中的 ${w}_{j} = \frac{\eta }{3}\left( {3 + {\left( -1\right) }^{j} - {\delta }_{j - 1}}\right)$。通过梯形法则或辛普森法则数值地获得 ${C}_{T}\left( k\right)$ 的成本是 $O\left( N\right)$，因为它需要 $N$ 次 ${\Psi }_{T}\left( \nu \right)$ 的计算。

##### 2.1.3.2 快速傅里叶变换

如果我们只对单个执行价格的期权价格感兴趣，到目前为止我们所做的就足够了。然而，如果我们希望找到一系列执行价格的期权价格，那么逐个计算 (2.12) 以获得价格将不会高效。

由 Cooley 和 Tukey [90] 开发并由许多其他人扩展的快速傅里叶变换（FFT）算法提供了一种更高效的算法，用于计算样本点为二的幂的离散逆傅里叶变换集。这些变换具有以下形式：

$$
\omega \left( m\right)  = \mathop{\sum }\limits_{{j = 1}}^{N}{e}^{-i\frac{2\pi }{N}\left( {j - 1}\right) \left( {m - 1}\right) }x\left( j\right) \text{ for }m = 1,\ldots , N \tag{2.13}
$$

这些方程看起来需要每次逆变换 $N$ 次乘法，总共需要 ${N}^{2}$ 次乘法；然而，Cooley-Tukey FFT 算法通过使用分治算法来分解离散傅里叶变换（DFTs），可以将此减少到 $N\ln N$ 次乘法。这对于近似傅里叶积分至关重要，因为这可以大大加快使用 FFT 方法计算期权价格的速度。

我们可以通过创建一个围绕我们希望计算准确期权价格的执行价格的范围，将期权定价公式转换为 FFT 形式。一个典型的情况是一个特定标的物的平价期权，这种情况下我们定义执行价格的对数范围为 ${k}_{m} = \beta  + \left( {m - 1}\right) {\Delta k} = \beta  + \left( {m - 1}\right) \lambda$，对于 $m = 1,\ldots , N$，其中 $\beta  = \ln {X}_{0} - \frac{\lambda N}{2}$，这将使平价执行价格落在我们执行价格范围的中间。对于 ${C}_{T}\left( {k}_{m}\right)$，我们现在有

$$
{C}_{T}\left( {k}_{m}\right)  \approx  \frac{{e}^{-\alpha {k}_{m}}}{\pi }\mathop{\sum }\limits_{{j = 1}}^{N}{e}^{-i{\nu }_{j}{k}_{m}}{\Psi }_{T}\left( {\nu }_{j}\right) {w}_{j}\text{ for }m = 1,\ldots , N
\\
= \frac{{e}^{-\alpha {k}_{m}}}{\pi }\mathop{\sum }\limits_{{j = 1}}^{N}{e}^{-i\left( {j - 1}\right) \eta \left( {m - 1}\right) {\Delta k}}{e}^{-{i\beta }{\nu }_{j}}{\Psi }_{T}\left( {\nu }_{j}\right) {w}_{j}= \frac{{e}^{-\alpha {k}_{m}}}{\pi }\mathop{\sum }\limits_{{j = 1}}^{N}{e}^{-{i\lambda \eta }\left( {j - 1}\right) \left( {m - 1}\right) }{e}^{-{i\beta }{\nu }_{j}}{\Psi }_{T}\left( {\nu }_{j}\right) {w}_{j}
$$

因此，我们可以看到，如果设置 ${\lambda \eta } = \frac{2\pi }{N}$ 和 $x\left( j\right)  = {e}^{-{i\beta }{\nu }_{j}}{\Psi }_{T}\left( {\nu }_{j}\right) {w}_{j}$，其中 $\beta  = \ln {X}_{0} - \frac{\lambda N}{2}$，我们就可以回到 FFT 的原始形式 (2.13)。因此，我们可以看到，我们可以通过 FFT 方法仅使用 $O\left( {N\log N}\right)$ 次乘法生成 $N$ 个期权价格。虽然这比直接积分获得单个期权价格所需的 $O\left( N\right)$ 次乘法要慢，但在单独对一个标的物定价时，很少只定价一个期权。通过 FFT 方法，我们有一个明显的优势，即当 $N$ 个期权的 $O\left( {N\ln N}\right)$ 次乘法分摊到每个期权时，每个期权的乘法次数仅为 $O\left( {\ln N}\right)$。

然而，这 $N$ 个期权不太可能是市场交易的 $N$ 个期权。但是，由于 FFT 方法定价的执行价格由 ${k}_{m} = \beta  + \left( {m - 1}\right) {\Delta k} = \beta  + \left( {m - 1}\right) \lambda$ 确定，我们可以通过修改 $N$ 来调整 $\eta  = \frac{B}{N}$，这将改变使用 FFT 方法获得期权价格的执行价格。这使我们能够在比直接积分所需时间显著减少的情况下，提取足够的信息来插值波动率曲面，误差非常小，而直接积分对于 $N$ 个执行价格需要 $O\left( {N}^{2}\right)$ 的时间。

#### 2.1.4 快速傅里叶变换的实现

简而言之，有了标的物过程 ${X}_{t}$ 的对数的特征函数 $\Phi \left( \nu \right)$，选择 $\alpha ,\eta$ 和 $N = {2}^{n}$，计算 $\lambda  = \frac{2\pi }{N\eta }$ 和 ${\nu }_{j} = \left( {j - 1}\right) \eta$，对于 $j = 1,\ldots , N$。现在形成向量 $\mathbf{x}$ 如下：

$$
\mathbf{x} = \left( \begin{matrix} {x}_{1} \\  {x}_{2} \\  \vdots \\  {x}_{N} \end{matrix}\right)  = \left( \begin{matrix} \frac{C}{2}\frac{C}{\left( {\alpha  + i{\nu }_{1}}\right) \left( {\alpha  + i{\nu }_{1} + 1}\right) }{e}^{-i\left( {1{K}_{0} - \frac{\lambda N}{2}}\right) {\nu }_{1}}\Phi \left( {{\nu }_{1} - \left( {\alpha  + 1}\right) i}\right) \\  C\frac{C}{\left( {\alpha  + i{\nu }_{2}}\right) \left( {\alpha  + i{\nu }_{2} + 1}\right) }{e}^{-i\left( {\ln {X}_{0} - \frac{\lambda N}{2}}\right) {\nu }_{2}}\Phi \left( {{\nu }_{2} - \left( {\alpha  + 1}\right) i}\right) \\  \vdots \\  C\frac{C}{\left( {\alpha  + i{\nu }_{N}}\right) \left( {\alpha  + i{\nu }_{N} + 1}\right) }{e}^{-i\left( {\ln {X}_{0} - \frac{\lambda N}{2}}\right) {\nu }_{N}}\Phi \left( {{\nu }_{N} - \left( {\alpha  + 1}\right) i}\right)  \end{matrix}\right)  \tag{2.14}
$$
其中常数系数 $\mathrm{C}$ 取决于我们所取期望的等价鞅测度；例如，对于 $\mathbb{Q}$，我们有 $\mathrm{C} = {e}^{-{rT}}$。向量 $\mathbf{x}$ 是 FFT 例程的输入，其输出是相同大小的向量 $\mathbf{y}$，
$$
\mathbf{y} = \operatorname{FFT}\left( \mathbf{x}\right) ,
$$
然后在执行价格 ${k}_{m}$ 处的看涨期权价格为 $m = 1,\ldots , N$
$$
\left( \begin{matrix} {C}_{T}\left( {k}_{1}\right) \\  {C}_{T}\left( {k}_{2}\right) \\  \vdots \\  {C}_{T}\left( {k}_{N}\right)  \end{matrix}\right)  = \left( \begin{matrix} \frac{{e}^{-\alpha \left( {\ln {X}_{0} - \frac{N}{2}\lambda }\right) }}{\pi }\operatorname{Re}\left( {y}_{1}\right) \\  \frac{{e}^{-\alpha \left( {\ln {X}_{0} - \left( {\frac{N}{2} - 1}\right) \lambda }\right) }}{\pi }\operatorname{Re}\left( {y}_{2}\right) \\  \vdots \\  \frac{{e}^{-\alpha \left( {\ln {X}_{0} - \left( {\frac{N}{2} - \left( {N - 1}\right) }\right) \lambda }\right) }}{\pi }\operatorname{Re}\left( {y}_{N}\right)  \end{matrix}\right)
$$
其中 $\operatorname{Re}\left( {y}_{j}\right)$ 是 ${y}_{j}$ 的实部。

#### 2.1.5 阻尼因子 $\alpha$

引入阻尼因子 $\alpha$ 使得通过傅里叶变换解决期权定价问题成为可能。乍一看，$\alpha$ 似乎没有出现在被积函数的计算中，因为它隐藏在 ${\Psi }_{T}\left( \nu \right)$ 中。我们已经知道，对于看涨期权，$\alpha$ 必须是正的，而对于看跌期权，$\alpha$ 必须是负的。理论上，对于任何值的 $\alpha$，我们应该得到大致相同的结果。然而，事实并非如此。在本节中，我们将展示结果对 $\alpha$ 选择的敏感性。我们寻找其值的合适范围，并说明其对随机模型选择的依赖性。最后，我们对三个过程进行一系列实证研究，重点关注使用正 $\alpha$ 为看涨期权定价。我们将考虑的过程是 (a) 几何布朗运动，(b) Heston 随机波动率模型，(c) 方差伽玛（VG）模型。

对于几何布朗运动，我们将使用以下参数集：现货 ${S}_{0} = {100}$，执行价格 $K = {90}$，瞬时无风险利率 $r = 5\%$，到期时间 $T = 1$ 年，波动率 $\sigma  = {30}\%$。表 2.1 通过 FFT 展示了不同 $\alpha , N$ 和 $\eta$ 值的 Black-Merton-Scholes 溢价。对于这个参数集，精确的 Black-Scholes 看涨期权溢价值为 19.6974。

对于 Heston 随机波动率模型，我们将使用以下参数集：现货 ${S}_{0} = {100}$，执行价格 $K = {90}$，无风险利率 $r = 3\%$，到期时间 $T = {0.5}$ 年，$\kappa  = 2$，$\sigma  = {0.5}$，$\theta  = {0.04}$，${v}_{0} = {0.04}$，相关性 $\rho  =  - {0.7}$。表 2.2 通过 FFT 展示了不同 $\alpha , N$ 和 $\eta$ 值的 Heston 溢价。作为参考，通过蒙特卡洛模拟计算的这个参数集的 Heston 看涨期权溢价值为 13.4038。

对于方差伽玛模型，我们将使用以下参数集：现货 ${S}_{0} = {100}$，执行价格 $K = {90}$，无风险利率 $r = {10}\%$，到期时间 $T = 1/{12}$ 年，$\sigma  = {0.12}$，$\theta  =  - {0.14}$，$\nu  = {0.2}$。表 2.3 通过 FFT 展示了不同 $\alpha$，$N$ 和 $\eta$ 值的方差伽玛溢价。这个参数集的方差伽玛看涨期权溢价值为 10.8288。从表 2.1、2.2 和 2.3 中可以看出，结果显著依赖于 $\alpha$ 和 $N$。对于某些 $\alpha$ 值，结果要么没有意义，要么是不合理的。为了探究为什么阻尼因子 $\alpha$ 会对结果产生如此大的影响，我们绘制了不同参数值下的被积函数，并检查了它们的行为。

表 2.1: 通过 FFT 计算的不同 $\alpha , N$ 和 $\eta$ 值的 Black-Merton-Scholes 溢价

| $\alpha$ | $\eta = 0.15$, $N = 2^{6}$ | $\eta = 0.15$, $N = 2^{8}$ | $\eta = 0.15$, $N = 2^{10}$ | $\eta = 0.1$, $N = 2^{6}$ | $\eta = 0.1$, $N = 2^{8}$ | $\eta = 0.1$, $N = 2^{10}$ | $\eta = 0.05$, $N = 2^{6}$ | $\eta = 0.05$, $N = 2^{8}$ | $\eta = 0.05$, $N = 2^{10}$ |
| -------- | -------------------------- | -------------------------- | --------------------------- | ------------------------- | ------------------------- | -------------------------- | -------------------------- | -------------------------- | --------------------------- |
| 0.01     | 211.907                    | 211.910                    | 211.910                     | 134.048                   | 134.054                   | 134.054                    | 60.4539                    | 59.4812                    | 59.4812                     |
| 0.5      | 19.6922                    | 19.6974                    | 19.6974                     | 19.6264                   | 19.6974                   | 19.6974                    | 19.7932                    | 19                         |                             |

表 2.2: 通过 FFT 计算的不同 $\alpha , N$ 和 $\eta$ 值的 Heston 溢价

| $\alpha$ | $\eta = 0.15$, $N = 2^{6}$ | $\eta = 0.15$, $N = 2^{8}$ | $\eta = 0.15$, $N = 2^{10}$ | $\eta = 0.1$, $N = 2^{6}$ | $\eta = 0.1$, $N = 2^{8}$ | $\eta = 0.1$, $N = 2^{10}$ | $\eta = 0.05$, $N = 2^{6}$ | $\eta = 0.05$, $N = 2^{8}$ | $\eta = 0.05$, $N = 2^{10}$ |
| -------- | -------------------------- | -------------------------- | --------------------------- | ------------------------- | ------------------------- | -------------------------- | -------------------------- | -------------------------- | --------------------------- |
| 0.01     | 205.050                    | 205.413                    | 205.415                     | 127.489                   | 127.576                   | 127.559                    | 55.6651                    | 52.745                     | 52.9863                     |
| 0.5      | 12.7379                    | 13.2001                    | 13.2023                     | 12.8612                   | 13.2222                   | 13.2023                    | 14.8195                    | 12.9309                    | 13.2025                     |
| 1        | 12.6307                    | 13.1998                    | 13.2023                     | 12.5494                   | 13.2251                   | 13.2023                    | 13.5390                    | 12.9010                    | 13.2026                     |
| 1.5      | 12.5201                    | 13.1994                    | 13.2023                     | 12.2137                   | 13.2281                   | 13.2023                    | 12.2191                    | 12.8731                    | 13.2027                     |
| 2        | 12.4092                    | 13.1990                    | 13.2023                     | 11.8667                   | 13.2313                   | 13.2023                    | 10.9782                    | 12.8484                    | 13.2027                     |
| 5        | 11.9182                    | 13.1958                    | 13.2023                     | 10.1369                   | 13.2509                   | 13.2023                    | 6.6138                     | 12.8410                    | 13.2032                     |
| 10       | 12.9279                    | 13.1922                    | 13.2023                     | 10.3712                   | 13.2280                   | 13.2023                    | 5.9025                     | 13.9336                    | 13.2043                     |

表 2.3: 通过 FFT 计算的不同 $\alpha , N$ 和 $\eta$ 值的方差伽玛溢价

| $\alpha$ | $\eta = 0.15$, $N = 2^{8}$ | $\eta = 0.15$, $N = 2^{10}$ | $\eta = 0.15$, $N = 2^{12}$ | $\eta = 0.1$, $N = 2^{8}$ | $\eta = 0.1$, $N = 2^{10}$ | $\eta = 0.1$, $N = 2^{12}$ | $\eta = 0.05$, $N = 2^{8}$ | $\eta = 0.05$, $N = 2^{10}$ | $\eta = 0.05$, $N = 2^{12}$ |
| -------- | -------------------------- | --------------------------- | --------------------------- | ------------------------- | -------------------------- | -------------------------- | -------------------------- | --------------------------- | --------------------------- |
| 0.01     | 203.123                    | 203.042                     | 203.042                     | 125.055                   | 125.186                    | 125.186                    | 49.9824                    | 50.6283                     | 50.6126                     |
| 0.5      | [数据缺失]                 | [数据缺失]                  | [数据缺失]                  | [数据缺失]                | [数据缺失]                 | [数据缺失]                 | [数据缺失]                 | [数据缺失]                  | [数据缺失]                  |


| $\alpha$ | $\eta  = {0.15}$ | $\eta  = {0.1}$ | $\eta  = {0.05}$ |
| --- | --- | --- | --- |
| $N = {2}^{8}$ | 10.9172 | 10.6980 | 10.1099 |
| ${2}^{10}$ | 10.8286 | 10.8293 | 10.8444 |
| ${2}^{12}$ | 10.8288 | 10.8288 | 10.8286 |

| $\alpha$ | $\eta  = {0.15}$ | $\eta  = {0.1}$ | $\eta  = {0.05}$ |
| --- | --- | --- | --- |
| $N = {2}^{8}$ | 10.9245 | 10.6984 | 10.0150 |
| ${2}^{10}$ | 10.8285 | 10.8293 | 10.8443 |
| ${2}^{12}$ | 10.8288 | 10.8287 | 10.8285 |

| $\alpha$ | $\eta  = {0.15}$ | $\eta  = {0.1}$ | $\eta  = {0.05}$ |
| --- | --- | --- | --- |
| $N = {2}^{8}$ | 10.9323 | 10.6998 | 9.9166 |
| ${2}^{10}$ | 10.8285 | 10.8292 | 10.8440 |
| ${2}^{12}$ | 10.8288 | 10.8287 | 10.8285 |

| $\alpha$ | $\eta  = {0.15}$ | $\eta  = {0.1}$ | $\eta  = {0.05}$ |
| --- | --- | --- | --- |
| $N = {2}^{8}$ | 10.9405 | 10.7024 | 9.8154 |
| ${2}^{10}$ | 10.8284 | 10.8291 | 10.8437 |
| ${2}^{12}$ | 10.8288 | 10.8287 | 10.8282 |

| $\alpha$ | $\eta  = {0.15}$ | $\eta  = {0.1}$ | $\eta  = {0.05}$ |
| --- | --- | --- | --- |
| $N = {2}^{8}$ | 11.0009 | 10.7483 | 9.2038 |
| ${2}^{10}$ | 10.8280 | 10.8280 | 10.8382 |
| ${2}^{12}$ | 10.8287 | 10.8287 | 10.8274 |

| $\alpha$ | $\eta  = {0.15}$ | $\eta  = {0.1}$ | $\eta  = {0.05}$ |
| --- | --- | --- | --- |
| $N = {2}^{8}$ | 11.1477 | 11.0028 | 8.5421 |
| ${2}^{10}$ | 10.8265 | 10.8239 | 10.8071 |
| ${2}^{12}$ | 10.8285 | 10.8285 | 10.8223 |

在图 2.1 中，我们绘制了看涨期权值的傅里叶变换，即 ${e}^{-{i\nu k}}{\Psi }_{T}\left( \nu \right)$，对于不同的 $\alpha$ 值。为了观察尾部衰减的速度，我们在图 2.2 中绘制了不同 $\alpha$ 值下的被积函数尾部。

我们从图 2.1 和 2.2 中的图表可以看出，随着 $\alpha$ 的增大，被积函数的振荡变得更加剧烈。当 $\alpha$ 大约在 1.0 时，行为最为稳定，这与期权定价结果一致。此外，每个图表中的尾部衰减非常快，因此扩展积分的上限对积分值的影响不大。

当 $\alpha$ 很大时，被积函数的振荡非常剧烈，这会导致积分结果较差。然而，从数值上讲，如果我们能够更高效地进行积分，我们应该能够得到与使用较小 $\alpha$ 时相同的结果。更具体地说，如果我们使用辛普森法则并选择非常小的 $\alpha$ 来尽可能捕捉尾部的细节，那么我们需要一个较大的 $N$ 来提供积分的合适上限，因为 $N \times  \eta$ 给出了积分的上限。

为了验证这一点，我们取 $\alpha  = {15}$。被积函数的图表如图 2.3 所示，其尾部的图表如图 2.4 所示。对于这个 $\alpha$ 值，函数在零附近剧烈振荡。在这种情况下，如果区间太少，结果可能会完全不现实。此外，我们可以看到，合适的上限应该大于 30。我们在以下三种情况下测试了结果：

- $N = {2}^{10},\eta  = {0.05}$，对应的上限为 51.2。使用辛普森法则，结果为 1302.2，这与预期的真实值相差甚远。
- $N = {2}^{12},\eta  = {0.01}$，对应的上限为 40.96。最终结果为 355.6856。它正接近真实值，但仍然与 Black-Scholes 值相差较大。
- $N = {2}^{22},\eta  = {0.00001}$，对应的上限为 41.943。最终结果为 20.2784，这与 $\alpha  = 1$ 时的结果一致。注意，如果我们使用第三组参数，$\lambda  = {0.1498}$，这意味着对数执行价格的间距太大。更具体地说，很少有执行价格位于当前股票价格附近的期望区域内。

---

${}^{4}$ 辛普森法则是数值积分的一种技术。

---

<img src="./images/0195247f-2f23-7bdd-9335-9204d62fe613_85_234_135_1173_1164_0.jpg" alt="0195247f-2f23-7bdd-9335-9204d62fe613_85_234_135_1173_1164_0.jpg" style="zoom:50%;" />

图 2.2: 几何布朗运动中不同 $\alpha$ 值的被积函数尾部

<img src="./images/0195247f-2f23-7bdd-9335-9204d62fe613_85_466_1442_694_456_0.jpg" alt="0195247f-2f23-7bdd-9335-9204d62fe613_85_466_1442_694_456_0.jpg" style="zoom:50%;" />

图 2.3: 几何布朗运动中 $\alpha  = {15}$ 时的被积函数

<img src="./images/0195247f-2f23-7bdd-9335-9204d62fe613_86_467_164_695_458_0.jpg" alt="0195247f-2f23-7bdd-9335-9204d62fe613_86_467_164_695_458_0.jpg" style="zoom:50%;" />

图 2.4: 几何布朗运动中 $\alpha  = {15}$ 时的被积函数尾部

总之，如果使用足够大的 $N$ 和足够小的区间 $\eta$，FFT 方法可以适用于较大的阻尼变量 $\alpha$。然而，在这种情况下，我们不会得到合适的执行价格范围。

对于 Heston 模型，我们得到了类似的结果，如图 2.5 和 2.6 所示。此外，我们可以看到，与几何布朗运动模型相比，积分中存在更大的负部分，这意味着如果我们使用的积分上限太小，我们将观察到比正常更高的价格，这在 $N$ 为 ${2}^{8}$ 时尤为明显。

对于 VG 模型，结果与另外两个模型一致，如图 2.7 和 2.8 所示。我们可以看到，当 $\alpha$ 增大时，被积函数的衰减速度变慢，这意味着对于固定的 $\eta$ 值，我们需要更大的 $N$。

我们的分析表明，使用 FFT 方法为期权定价时，结果对 $\alpha$、$N$ 和 $\eta$ 的选择非常敏感。理论上，FFT 方法可以适用于任何阻尼变量 $\alpha$，但选择 $N$ 和 $\eta$ 时必须小心。如所示，最准确的结果是通过使用非常大的 $N$ 和非常小的区间 $\eta$ 获得的，但这种参数选择不仅计算成本高，而且也不会提供有用的执行价格范围。从结果中我们可以得出结论，$\alpha$ 的最优范围在 1.0 到 1.5 之间。


---

### 2.2 分数快速傅里叶变换

如前一节所述，使用标准快速傅里叶变换（FFT）方法规定了 $\lambda$ 和 $\eta$ 之间的以下关系：

$$
{\lambda \eta } = \frac{2\pi }{N} \tag{2.15}
$$

其中

$$
\eta  = \frac{B}{N} \tag{2.16}
$$

然而，我们可以看到，在考虑的四个参数中，$N, B, \eta$ 和 $\lambda$，只有两个可以自由选择，因为 $\eta$ 由 $B$ 和 $N$ 确定，最后一个参数则通过约束条件（2.15）确定。我们进一步假设有一个固定的计算预算，这决定了一个固定的积分项数 $N$。基于这些假设，我们只有两个自由变量：$B$，积分的上限，和 $\lambda  = {\Delta k}$，我们计算解的 $\log \left( K\right)$ 网格的间距，它们是成反比的。因此，我们在积分上限和行权价间距之间存在一个固有的权衡，前者决定了积分的准确性，后者则决定了我们是否能在接近市场交易行权价的行权价处获得相关的价格信息。$B$ 的选择将决定我们积分近似的准确性；然而，如果我们假设我们希望在积分点之间保持固定的间距 $\eta$ 以确保积分的给定精度，我们就会对 $\lambda$ 产生限制，这决定了我们计算解的对数行权价的间距。

<img src="./images/0195247f-2f23-7bdd-9335-9204d62fe613_87_242_137_1163_1162_0.jpg" alt="0195247f-2f23-7bdd-9335-9204d62fe613_87_242_137_1163_1162_0.jpg" style="zoom:50%;" />

图 2.5: Heston 随机波动率模型中不同 $\alpha$ 值的被积函数

例如，我们固定 $\eta$ 以确保积分的局部精度，并显示不同 $N$ 值下的隐含上限 $B$ 和隐含对数行权价间距 $\lambda$。这些结果可以在表 2.4 中看到。我们观察到，生成接近市场交易行权价的解需要相当大的 $N$。例如，为了确保在积分点之间保持固定的间距 $\eta$ 以确保积分的给定精度，我们对 $\lambda$ 产生限制，这决定了我们计算解的对数行权价的间距。

<img src="./images/0195247f-2f23-7bdd-9335-9204d62fe613_88_228_123_1176_1176_0.jpg" alt="0195247f-2f23-7bdd-9335-9204d62fe613_88_228_123_1176_1176_0.jpg" style="zoom:50%;" />

图 2.6: Heston 随机波动率模型中不同 $\alpha$ 值的被积函数尾部

我们的结果说明了积分网格间距、积分上限和对数行权价间距之间的关系。如 [77] 中所述，计算出的 4096 个期权价格中，大约有 67 个（$2 \times  \frac{20\% }{0.61\% } + 1 \approx  67$）落在了 20% 的对数行权价区间内，这对于实际应用来说是相关的，因此其余计算出的期权价格没有实际用途。考虑到我们实验中计算的 4096 个期权价格，如果我们使用 FFT 算法单独对每个期权进行定价，并且以每个期权的行权价为中心的对数行权价尺度进行计算，我们只需要 128 或 256 点的网格就能得到实际准确的价格。换句话说，使用只有 128 或 256 个网格点通常能为给定的中心行权价生成可接受的期权价格。然而，在我们的例子中，使用 256 点的网格会导致 $\lambda  = 0.0981$ 或对数行权价间距为 9.81%，这显然是不切实际的，因为它太大了。我们希望消除项数 $N$ 和对数行权价间距 $\lambda$ 之间的依赖关系。这将允许我们使用更小的 $N$，同时仍然能够生成一组准确的期权价格，并且独立选择与市场交易期权一致的对数行权价间距 $\lambda$。在 [77] 中，作者提出了一种分数 FFT 程序来实现这一点。分数 FFT 程序

<img src="./images/0195247f-2f23-7bdd-9335-9204d62fe613_89_235_143_1159_1156_0.jpg" alt="0195247f-2f23-7bdd-9335-9204d62fe613_89_235_143_1159_1156_0.jpg" style="zoom:50%;" />

图 2.7: 变异伽马模型中不同 $\alpha$ 值的被积函数

计算如下形式的和

$$
\mathop{\sum }\limits_{{j = 1}}^{N}{e}^{-{i2\pi \gamma }\left( {j - 1}\right) \left( {m - 1}\right) }x\left( j\right)  \tag{2.17}
$$

对于任何 $\gamma$ 的值。我们在前一节中研究的标准 FFT 是 $\gamma  = \frac{1}{N}$ 的特殊情况。公式（2.17）中的求和可以在不施加（2.15）中的约束条件下计算。这意味着，一个用于特征函数积分的网格间距和另一个用于对数行权价的网格间距可以独立选择。

#### 2.2.1 分数 FFT 的形成

如 [23] 和 [24] 中所述，在分数傅里叶变换（FrFFT）中，我们定义长度为 $N$ 的复数序列 $x$ 为

$$
{G}_{m}\left( {x,\gamma }\right)  = \mathop{\sum }\limits_{{j = 1}}^{N}{e}^{-{i2\pi \gamma }\left( {j - 1}\right) \left( {m - 1}\right) }x\left( j\right)  \tag{2.18}
$$

<img src="./images/0195247f-2f23-7bdd-9335-9204d62fe613_90_235_144_1168_1155_0.jpg" alt="0195247f-2f23-7bdd-9335-9204d62fe613_90_235_144_1168_1155_0.jpg" style="zoom:50%;" />

图 2.8: 变异伽马模型中不同 $\alpha$ 值的被积函数尾部

参数 $\gamma$ 实际上可以是任何复数有理数。求和可以通过三个 ${2N}$ 点的 FFT 步骤实现。对于由（2.14）给出的向量 $\mathbf{x}$ 的 $N$ 点分数 FFT，我们定义以下 ${2N}$ 点的序列：

$$
{y}_{j} = {x}_{j}{e}^{-{i\pi }{\left( j - 1\right) }^{2}\gamma }\;1 \leq  j \leq  N
$$

$$
{y}_{j} = 0\;N < j \leq  {2N}
$$

$$
{z}_{j} = {e}^{{i\pi }{\left( j - 1\right) }^{2}\gamma }\;1 \leq  j \leq  N
$$

$$
{z}_{j} = {e}^{{i\pi }{\left( 2N - j\right) }^{2}\gamma }
$$

其中 ${x}_{j}$ 是 $\mathbf{x}$ 的第 ${j}$ 个元素，$\gamma  = \frac{\lambda \eta }{2\pi }$。如 [23] 中所示，

$$
{G}_{m}\left( {x,\gamma }\right)  = \left( {e}^{-{i\pi }{\left( m - 1\right) }^{2}\gamma }\right)  \odot  {\mathrm{D}}_{m}^{-1}\left( {\mathrm{D}\left( \mathbf{y}\right)  \odot  \mathrm{D}\left( \mathbf{z}\right) }\right) \;1 \leq  m \leq  N
$$

其中 $\odot$ 表示向量的元素逐个乘法，

$$
\mathrm{D}\left( \xi \right)  = \left( \begin{matrix} {\mathrm{D}}_{1}\left( \xi \right) \\  {\mathrm{D}}_{2}\left( \xi \right) \\  \vdots \\  {\mathrm{D}}_{2N}\left( \xi \right)  \end{matrix}\right)
$$

表 2.4: 积分网格间距与对数行权价间距之间的关系

| $n$ | $N = {2}^{n}$ | $\eta$ | 上限 | $\lambda$ | 对数行权价间距 |
| --- | --- | --- | --- | --- | --- |
| 7 | 128 | 0.25 | 32 | 0.1963 | 19.0% |
| 8 | 256 | 0.25 | 64 | 0.0981 | 9.81% |
| 9 | 512 | 0.25 | 128 | 0.0491 | 4.91% |
| 10 | 1024 | 0.25 | 256 | 0.0245 | 2.45% |
| 11 | 2048 | 0.25 | 512 | 0.0122 | 1.22% |
| 12 | 4096 | 0.25 | 1024 | 0.0061 | 0.61% |
| 13 | 8192 | 0.25 | 2048 | 0.0031 | 0.30% |

其中

$$
{\eta }_{j} = {\mathrm{D}}_{j}\left( \xi \right)  = \mathop{\sum }\limits_{{m = 1}}^{{2N}}\exp \left( {-i\frac{2\pi }{2N}\left( {j - 1}\right) \left( {m - 1}\right) }\right) \xi \left( m\right) \;1 \leq  j \leq  {2N}
$$

并且

$$
{\xi }_{m} = {\mathrm{D}}_{m}^{-1}\left( \eta \right)  = \frac{1}{2N}\mathop{\sum }\limits_{{j = 1}}^{{2N}}\exp \left( {i\frac{2\pi }{2N}\left( {j - 1}\right) \left( {m - 1}\right) }\right) \eta \left( j\right) \;1 \leq  m \leq  {2N}
$$

最终逆离散傅里叶变换的剩余 $N$ 个结果被丢弃。注意，指数量不依赖于实际积分的函数，因此可以预先计算并存储。

#### 2.2.2 分数 FFT 的实现

假设我们有标的资产价格过程 ${X}_{t}$ 的对数的特征函数 $\Phi \left( \nu \right)$，我们选择 $\alpha, \eta, \lambda$（独立选择）和 $N = {2}^{n}$。计算 $\gamma  = \frac{\eta \lambda }{2\pi }$ 并设置 ${\nu }_{j} = \left( {j - 1}\right) \eta$，对于 $j = 1,\ldots , N$。构造向量 $\mathbf{x}$ 如下：

$$
\mathbf{x} = \left( \begin{matrix} {x}_{1} \\  {x}_{2} \\  \vdots \\  {x}_{N} \end{matrix}\right)  = \left( \begin{matrix} \frac{C}{2}\frac{1}{\left( {\alpha  + i{\nu }_{1}}\right) \left( {\alpha  + i{\nu }_{1} + 1}\right) }{e}^{-i\left( {1{\kappa }_{0} - \frac{\lambda N}{2}}\right) {\nu }_{1}}\Phi \left( {{\nu }_{1} - \left( {\alpha  + 1}\right) i}\right) \\  \frac{C}{\eta \left( {\alpha  + i{\nu }_{2}}\right) \left( {\alpha  + i{\nu }_{2} + 1}\right) }{e}^{-i\left( {\ln {X}_{0} - \frac{\lambda N}{2}}\right) {\nu }_{2}}\Phi \left( {{\nu }_{2} - \left( {\alpha  + 1}\right) i}\right) \\  \vdots \\  \eta \frac{C}{\left( {\alpha  + i{\nu }_{N}}\right) \left( {\alpha  + i{\nu }_{N} + 1}\right) }{e}^{-i\left( {\ln {X}_{0} - \frac{\lambda N}{2}}\right) {\nu }_{N}}\Phi \left( {{\nu }_{N} - \left( {\alpha  + 1}\right) i}\right)  \end{matrix}\right)
$$

现在构造向量 $\mathbf{y}$ 和 $\mathbf{z}$ 如下：

$$
\mathbf{y} = \left( \begin{matrix} {y}_{1} \\  {y}_{2} \\  \vdots \\  {y}_{N} \\  {y}_{N + 1} \\  {y}_{N + 2} \\  \vdots \\  {y}_{2N} \end{matrix}\right)  = \left( \begin{matrix} {x}_{1} \\  \exp \left( {-{i\pi \gamma }}\right) {x}_{2} \\  \vdots \\  \exp \left( {-{i\pi \gamma }{\left( N - 1\right) }^{2}}\right) {x}_{N} \\  0 \\  0 \\  \vdots \\  0 \end{matrix}\right) \;\mathbf{z} = \left( \begin{matrix} {z}_{1} \\  {z}_{2} \\  \vdots \\  {z}_{N} \\  {z}_{N + 1} \\  {z}_{N + 2} \\  \vdots \\  {z}_{2N} \end{matrix}\right)  = \left( \begin{matrix} 1 \\  \exp \left( {i\gamma \pi }\right) \\  \vdots \\  \exp \left( {i\gamma \pi }\right) \\  \exp \left( {{i\gamma \pi }{\left( N - 1\right) }^{2}}\right) \\  \exp \left( {{i\gamma \pi }{\left( N - 2\right) }^{2}}\right) \\  \exp \left( {{i\gamma \pi }{\left( N - 2\right) }^{2}}\right) \\  \vdots \\  1 \end{matrix}\right)
$$

向量 $\mathbf{y}$ 和 $\mathbf{z}$ 是 FFT 常规输入，其输出分别是相同大小的向量 $\widehat{\mathbf{y}}$ 和 $\widehat{\mathbf{z}}$。通过逐个元素乘法构造向量 $\xi$，即

$$
\xi  = \left( \begin{matrix} {\xi }_{1} \\  {\xi }_{2} \\  \vdots \\  {\xi }_{2N} \end{matrix}\right)  = \left( \begin{matrix} {\widehat{y}}_{1}{\widehat{z}}_{1} \\  {\widehat{y}}_{2}{\widehat{z}}_{2} \\  \vdots \\  {\widehat{y}}_{2N}{\widehat{z}}_{2N} \end{matrix}\right)
$$

向量 $\xi$ 是逆 FFT（IFFT）常规的输入，其输出是相同大小的向量 $\widehat{\xi }$。使用向量 $\widehat{\xi }$，行权价为 ${k}_{m}$ 的行权价为 ${k}_{m}$ 的看涨期权价格为 $m = 1,\ldots , N$：

$$
\left( \begin{matrix} {C}_{T}\left( {k}_{1}\right) \\  {C}_{T}\left( {k}_{2}\right) \\  \vdots \\  {C}_{T}\left( {k}_{N}\right)  \end{matrix}\right)  = \left( \begin{matrix} \frac{{e}^{-\alpha \left( {\ln {X}_{0} - \frac{N}{2}\lambda }\right) }}{\pi }\operatorname{Re}\left( {\widehat{\xi }}_{1}\right) \\  \frac{{e}^{-\alpha \left( {\ln {X}_{0} - \left( {\frac{N}{2} - 1}\right) \lambda }\right) }}{\pi }\operatorname{Re}\left( {\exp \left( {-{i\pi \gamma }}\right) {\widehat{\xi }}_{2}}\right) \\  \vdots \\  \frac{{e}^{-\alpha \left( {\ln {X}_{0} - \left( {\frac{N}{2} - \left( {N - 1}\right) }\right) \lambda }\right) }}{\pi }\operatorname{Re}\left( {\exp \left( {-{i\pi \gamma }{\left( N - 1\right) }^{2}}\right) {\widehat{\xi }}_{N}}\right)  \end{matrix}\right)
$$

其中 $\operatorname{Re}\left( z\right)$ 表示 $z$ 的实部。注意，$\widehat{\xi }$ 的最后 $N$ 个元素从未使用过，因此被丢弃。考虑到 $\lambda$ 和 $\eta$ 是独立的，我们可以选择 $\lambda$ 以生成围绕 $\ln {X}_{0}$ 的一个范围，该范围具有所需的实值性（例如，对于 25% 的实值性，我们得到 $\lambda  = \frac{2\left( {0.25}\right) }{N}$）。通常，$N = {2}^{n}$ 远小于快速傅里叶变换技术（例如，${2}^{7}$ 而不是 ${2}^{14}$）。

### 2.3 通过傅里叶余弦（COS）方法定价衍生品

尽管 FFT 方法有许多显著的优势，包括其仅需已知对数资产价格的特征函数即可定价的能力、速度以及一次运行即可生成多个期权价格的能力，但我们还看到了它存在一些显著的缺点。这些缺点包括仅限于路径独立的欧式期权，并且需要重新推导以处理有限的到期支付结构，以及对于深度价外期权的不准确性。

为了改进现有的基于傅里叶的定价方法，Fang 和 Oosterlee 在 [129] 中开发了 COS 方法。FFT 方法显式地形成了期权溢价的傅里叶变换，该变换基于对数资产价格的特征函数，因此可以通过傅里叶逆变换恢复溢价。COS 方法采取了不同的方法，首先将对数资产价格的概率密度函数表示为其傅里叶余弦展开，然后表明该展开的系数可以用对数资产价格的特征函数表示。然后，这种表示被用于风险中性定价公式中，该公式可以简化为一个可解析计算的积分和可以直接从特征函数计算的系数的和。

这种方法在多个方面改进了经典的 FFT 方法。首先，它在计算速度上有了显著的提升。尽管 COS 方法确实需要 $O\left( {n}^{2}\right)$ 次乘法，这在计算上与直接积分相同，且多于 FFT 的摊销 $O\left( {n\log n}\right)$，但余弦展开在积分非周期函数时的优越性能显著减少了为达到一定精度所需项的数量，从而使 COS 方法更快。COS 方法的另一个非常重要的优势是，它完全分离了余弦展开系数的推导与依赖于期权到期支付的项。这意味着，只要可以解析地评估期权支付项的简单余弦积分，该方法就可以用于定价任何路径独立的欧式期权。这应该适用于几乎所有支付结构。

---

${}^{5}$ 实值性是现货价格与行权价之间的绝对差，除以现货价格。

---

因此，COS 方法是对经典 FFT 方法的显著改进，但它也带有自己的几个注意事项。与 FFT 方法类似，它在原始形式下只能处理路径独立的欧式期权。此外，COS 方法涉及通过将无限积分范围截断为某个有限区间 $\left[ {a, b}\right]$ 来近似定价积分，因此 COS 展开具有有限项。这个范围的最佳值需要估计，且最终的价格对 $\left[ {a, b}\right]$ 的选择非常敏感。最后，COS 方法在尝试定价深度价外期权时也存在与 FFT 方法类似的准确性问题。

模型：

所有存在资产价格分布特征函数的模型

期权类型：

具有广泛到期支付结构的路径独立欧式期权

优点：

1. 允许在任何具有特征函数的模型下定价
2. 已知最快的基于傅里叶的定价方法
3. 将模型与支付分离，支持广泛的衍生品

缺点：

1. 仅限于路径独立的欧式期权
2. 需要估计适当的 $\left[ {a, b}\right]$
3. 对于高度价外期权不准确

#### 2.3.1 COS 方法

##### 2.3.1.1 任意函数的余弦级数展开

函数 $f\left( \theta \right)$ 在 $\left[ {0, \pi}\right]$ 上的傅里叶余弦级数展开为

$$
f\left( \theta \right)  = \frac{1}{2}{A}_{0} + \mathop{\sum }\limits_{{k = 1}}^{\infty }{A}_{k}\cos \left( {k\theta }\right)= \bar{\sum }_{k = 0}^{\infty }{A}_{k}\cos \left( {k\theta }\right)  \tag{2.19}
$$

其中傅里叶余弦系数为

$$
{A}_{k} = \frac{2}{\pi }{\int }_{0}^{\pi }f\left( \theta \right) \cos \left( {k\theta }\right) {d\theta } \tag{2.20}
$$

其中 $\bar{\sum }$ 表示求和的第一项权重为一半。${}^{6}$ 我们可以将这个定义扩展到任意有限区间上的函数。对于任何有限区间 $\left[ {a, b}\right]$ 上的函数，通过以下变量变换将 $a$ 映射到 0，将 $b$ 映射到 $\pi$，可以得到傅里叶余弦级数展开：

$$
\theta  = \frac{\pi  - 0}{b - a}\left( {x - a}\right)  = \frac{x - a}{b - a}\pi  \tag{2.21}
$$

我们用 $\theta$ 表示 $x$：

$$
x = \frac{b - a}{\pi }\theta  + a \tag{2.22}
$$

并将其代入（2.19）以得到

$$
f\left( x\right)  = \overset{\infty }{\mathop{\sum }\limits_{{k = 0}}}{A}_{k}\cos \left( {k\frac{x - a}{b - a}\pi }\right)  \tag{2.23}
$$

其中傅里叶余弦系数为

$$
{A}_{k} = \frac{2}{b - a}{\int }_{a}^{b}f\left( x\right) \cos \left( {k\frac{x - a}{b - a}\pi }\right) {dx} \tag{2.24}
$$

##### 2.3.1.2 余弦级数系数与特征函数的关系

我们已经知道，对于分布函数 $f\left( x\right)$，其特征函数为

$$
\mathbb{E}\left( {e}^{i\nu x}\right)  = \phi \left( \nu \right)  = {\int }_{-\infty }^{\infty }{e}^{i\nu x}f\left( x\right) {dx}
$$

通过在 $\nu  = \frac{k\pi }{b - a}$ 处评估特征函数，我们得到

$$
\phi \left( \frac{k\pi }{b - a}\right)  = {\int }_{-\infty }^{\infty }{e}^{i\left( \frac{k\pi }{b - a}\right) x}f\left( x\right) {dx}
$$

我们称这个积分的截断版本为 $\widehat{\phi }$，即

$$
\widehat{\phi }\left( \frac{k\pi }{b - a}\right)  = {\int }_{a}^{b}{e}^{i\left( \frac{k\pi }{b - a}\right) x}f\left( x\right) {dx} \tag{2.25}
$$

将（2.25）乘以 ${e}^{-i\frac{k\pi a}{b - a}}$，我们得到

$$
\widehat{\phi }\left( \frac{k\pi }{b - a}\right) {e}^{-i\frac{k\pi a}{b - a}} = {e}^{-i\frac{k\pi a}{b - a}}{\int }_{a}^{b}{e}^{i\left( \frac{k\pi }{b - a}\right) x}f\left( x\right) {dx}= {\int }_{a}^{b}{e}^{{ik\pi }\left( \frac{x - a}{b - a}\right) }f\left( x\right) {dx}= {\int }_{a}^{b}\left( {\cos \left( {{k\pi }\left( \frac{x - a}{b - a}\right) }\right)  + i\sin \left( {{k\pi }\left( \frac{x - a}{b - a}\right) }\right) }\right) f\left( x\right) {dx}
$$

因此，我们有

$$
\operatorname{Re}\left\{  {\widehat{\phi }\left( \frac{k\pi }{b - a}\right) \exp \left( {-i\frac{ka\pi }{b - a}}\right) }\right\}   = {\int }_{a}^{b}\cos \left( {{k\pi }\left( \frac{x - a}{b - a}\right) }\right) f\left( x\right) {dx} \tag{2.26}
$$

---

${}^{6}$ 在本节中，我们遵循 [129] 中的笔记。

---

如果我们假设 $\left[ {a, b}\right]$ 被选择为

$$
\widehat{\phi }\left( \nu \right)  = {\int }_{a}^{b}{e}^{i\nu x}f\left( x\right) {dx} \approx  {\int }_{-\infty }^{+\infty }{e}^{i\nu x}f\left( x\right) {dx} = \phi \left( \nu \right)  \tag{2.27}
$$

那么比较（2.24）和（2.26）可以得到

$$
{A}_{k} = \frac{2}{b - a}\operatorname{Re}\left\{  {\widehat{\phi }\left( \frac{k\pi }{b - a}\right) \exp \left( {-i\frac{ka\pi }{b - a}}\right) }\right\}   \tag{2.28}
$$

其中 ${A}_{k} \approx  {F}_{k}$，而

$$
{F}_{k} = \frac{2}{b - a}\operatorname{Re}\left\{  {\phi \left( \frac{k\pi }{b - a}\right) \exp \left( {-i\frac{ka\pi }{b - a}}\right) }\right\}   \tag{2.29}
$$

通过在 $f\left( x\right)$ 的傅里叶余弦级数展开中用 ${F}_{k}$ 替换 ${A}_{k}$，我们得到一个近似的余弦级数展开，该展开是 $f\left( x\right)$ 特征函数的函数。

$$
\widehat{f}\left( x\right)  = \overset{\infty }{\mathop{\sum }\limits_{{k = 0}}}{F}_{k}\cos \left( {k\frac{x - a}{b - a}\pi }\right)  \tag{2.30}
$$

通过进一步截断求和，我们得到

$$
\widetilde{f}\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{{N - 1}}{F}_{k}\cos \left( {k\frac{x - a}{b - a}\pi }\right)  \tag{2.31}
$$

##### 2.3.1.3 COS 期权定价

现在我们展示如何使用前一节的结果进行期权定价。设

$x$ 是在时间 $t$ 处的建模量，通常是对数资产价格

$y$ 是在时间 $T$ 处的建模量，通常是对数资产价格

$f\left( {y \mid  x}\right)$ 是定价测度下的概率密度函数

$v\left( {x, t}\right)$ 是在时间 $t$ 处的路径独立欧式期权的价值

$v\left( {y, T}\right)$ 是在时间 $T$ 处的期权价值，即到期支付

那么，时间 $t$ 处的期权价值可以表示为

$$
v\left( {x, t}\right)  = \mathrm{C}{\int }_{a}^{b}v\left( {y, T}\right) f\left( {y \mid  x}\right) {dy}
$$

对于适当的 C 值。从（2.23）和（2.24）中，我们有

$$
v\left( {x, t}\right)  = \mathrm{C}{\int }_{a}^{b}v\left( {y, T}\right) \overset{\infty }{\mathop{\sum }\limits_{{k = 0}}}{A}_{k}\cos \left( {k\frac{y - a}{b - a}\pi }\right) {dy}= \mathrm{c}\mathop{\sum }\limits_{{k = 0}}^{\infty }{A}_{k}\left( {{\int }_{a}^{b}v\left( {y, T}\right) \cos \left( {k\frac{y - a}{b - a}\pi }\right) {dy}}\right)
$$

定义

$$
{V}_{k} = \frac{2}{b - a}{\int }_{a}^{b}v\left( {y, T}\right) \cos \left( {{k\pi }\frac{y - a}{b - a}}\right) {dy} \tag{2.32}
$$

那么我们有

$$
v\left( {x, t}\right)  = \frac{b - a}{2}\mathrm{C}{\bar{\sum }}_{k = 0}^{\infty }{A}_{k}{V}_{k} \tag{2.33}
$$

为了使其可计算，我们进行另一个近似并截断积分

$$
v\left( {x, t}\right)  \approx  \frac{b - a}{2}\mathrm{C}\mathop{\sum }\limits_{{k = 0}}^{{N - 1}}{A}_{k}{V}_{k} \tag{2.34}
$$

代入（2.29），我们得到基于模型特征函数和根据期权支付计算的系数 ${V}_{k}$ 的期权溢价

$$
v\left( {x, t}\right)  \approx  \mathrm{C}\mathop{\sum }\limits_{{k = 0}}^{{N - 1}}\operatorname{Re}\left\{  {\phi \left( \frac{k\pi }{b - a}\right) \exp \left( {-{ik\pi }\frac{a}{b - a}}\right) }\right\}  {V}_{k} \tag{2.35}
$$

注意 $\phi \left( \frac{k\pi }{b - a}\right)$ 是 $x$ 的函数，因为它是 $f\left( {y \mid  x}\right)$ 的特征函数。

#### 2.3.2 不同支付结构下的 COS 期权定价

COS 方法下的期权价格计算为

$$
v\left( {x, t}\right)  \approx  \frac{b - a}{2}\mathrm{C}{\bar{\sum }}_{k = 0}^{N - 1}{A}_{k}{V}_{k} \tag{2.36}
$$

$$
\approx  \mathrm{C}{\bar{\sum }}_{k = 0}^{N - 1}\operatorname{Re}\left\{  {\phi \left( \frac{k\pi }{b - a}\right) \exp \left( {-{ik\pi }\frac{a}{b - a}}\right) }\right\}  {V}_{k} \tag{2.37}
$$

模型的所有信息完全包含在用特征函数表示的余弦展开系数中。系数系数 ${V}_{k}$ 包含了所有关于支付的信息，因此我们可以将 COS 方法适应于任何可以解析计算 ${V}_{k}$ 的支付结构。由于我们有

$$
{V}_{k} = \frac{2}{b - a}{\int }_{a}^{b}v\left( {y, T}\right) \cos \left( {{k\pi }\frac{y - a}{b - a}}\right) {dy} \tag{2.38}
$$

这在许多情况下是成立的，这里我们给出一些常见的例子。

##### 2.3.2.1 标准期权价格的 COS 方法

为了使用 COS 方法定价标准期权，我们首先定义以下变量：

${X}_{t}$ 是标的证券的当前价格

${X}_{T}$ 是标的证券在时间 $T$ 的价格

$K$ 是期权的行权价

$$
x = \ln \left( {{X}_{t}/K}\right)
$$

$$
y = \ln \left( {{X}_{T}/K}\right)
$$

因此，我们可以将标准欧式期权的支付表示为

$$
v\left( {y, T}\right)  = {\left\lbrack  \alpha K\left( {e}^{y} - 1\right) \right\rbrack  }^{ + }
$$

其中 $\alpha  = 1$ 表示看涨期权，$\alpha  =  - 1$ 表示看跌期权。在这种情况下，${V}_{k}$ 有一个解析形式。定义

$$
{\chi }_{k}\left( {c, d}\right)  = {\int }_{c}^{d}{e}^{y}\cos \left( {{k\pi }\frac{y - a}{b - a}}\right) {dy}
$$

$$
{\varphi }_{k}\left( {c, d}\right)  = {\int }_{c}^{d}\cos \left( {{k\pi }\frac{y - a}{b - a}}\right) {dy}
$$

然后我们得到它们的解析形式 ${}^{7}$

$$
{\chi }_{k}\left( {c, d}\right)  = \frac{1}{1 + {\left( \frac{k\pi }{b - a}\right) }^{2}}\left\lbrack  {\cos \left( {{k\pi }\frac{d - a}{b - a}}\right) {e}^{d} - \cos \left( {{k\pi }\frac{c - a}{b - a}}\right) {e}^{c}} {+\frac{k\pi }{b - a}\sin \left( {{k\pi }\frac{d - a}{b - a}}\right) {e}^{d} - \frac{k\pi }{b - a}\sin \left( {{k\pi }\frac{c - a}{b - a}}\right) {e}^{c}}\right\rbrack   \tag{2.39}
$$

和

$$
{\varphi }_{k}\left( {c, d}\right)  = \left\{  \begin{array}{ll} \left\lbrack  {\sin \left( {{k\pi }\frac{d - a}{b - a}}\right)  - \sin \left( {{k\pi }\frac{c - a}{b - a}}\right) }\right\rbrack  \frac{b - a}{k\pi } & k \neq  0 \\  \left( {d - c}\right) & k = 0 \end{array}\right.  \tag{2.40}
$$

因此，对于标准看涨和看跌期权，我们得到

$$
{V}_{k}^{\text{call }} = \frac{2}{b - a}{\int }_{a}^{b}K{\left( {e}^{y} - 1\right) }^{ + }\cos \left( {{k\pi }\frac{y - a}{b - a}}\right) {dy}= \frac{2}{b - a}K\left( {{\chi }_{k}\left( {0, b}\right)  - {\varphi }_{k}\left( {0, b}\right) }\right)  \tag{2.41}
$$

$$
{V}_{k}^{put} = \frac{2}{b - a}{\int }_{a}^{b}K{\left( 1 - {e}^{y}\right) }^{ + }\cos \left( {{k\pi }\frac{y - a}{b - a}}\right) {dy}= \frac{2}{b - a}K\left( {-{\chi }_{k}\left( {a,0}\right)  + {\varphi }_{k}\left( {a,0}\right) }\right)  \tag{2.42}
$$

##### 2.3.2.2 数字期权价格的 COS 方法

对于数字期权，结果甚至更简单。

$$
{V}_{k}^{\text{cashcall }} = \frac{2}{b - a}{\int }_{0}^{b}K\cos \left( {{k\pi }\frac{y - a}{b - a}}\right) {dy}= \frac{2}{b - a}K{\varphi }_{k}\left( {0, b}\right)  \tag{2.43}
$$

#### 2.3.3 COS 方法的截断范围

在 [129] 中，作者提出（没有证明）了以下公式，用于 COS 方法中的积分范围 $\left[ {a, b}\right]$：

$$
\left[ {a, b}\right]   = \left[ {{c}_{1} - L\sqrt{{c}_{2} + \sqrt{{c}_{4}}},{c}_{1} + L\sqrt{{c}_{2} + \sqrt{{c}_{4}}}}\right]  \;\text{ with }\;L = {10} \tag{2.44}
$$

其中 ${c}_{n}$ 表示 $x$ 的第 $n$ 个累积量 ${}^{8}$。在我们所有的数值例子中，我们将使用上述公式来确定范围 $\left[ {a, b}\right]$。确定最终价格对 $a$ 和 $b$ 选择的敏感性，以及对这个公式的证明，将在本章末尾作为简短的案例研究。

---

${}^{7}$ 注意，${\chi }_{k}\left( {c, d}\right)$ 在 $k = 0$ 时是良好定义的。

${}^{8}$ 对于随机变量 $X$，其累积量生成函数由下式给出：

$$
G\left( \omega \right)  = \log \left( {\mathbb{E}\left\lbrack  {\exp \left( {\omega X}\right) }\right\rbrack  }\right)
$$

---

#### 2.3.4 COS 方法的数值结果

在本节中，我们将展示一些 COS 方法的实证结果，并将其与分数 FFT 方法进行比较。我们将展示以下三个模型的结果：(a) 几何布朗运动，(b) Heston 随机波动率模型，(c) 变异伽马模型。

##### 2.3.4.1 几何布朗运动 (GBM)

Black-Scholes 模型在第 1.4.2 节中描述，其特征函数在第 1.4.2.3 节中描述。GBM 下的 SDE 和特征函数如下：

$$
d{S}_{t} = \left( {r - q}\right) {S}_{t}{dt} + \sigma {S}_{t}d{W}_{t} \tag{2.45}
$$

$$
\phi \left( \omega \right)  = \mathbb{E}\left( {e}^{i\omega y}\right)= \mathbb{E}\left( {e}^{{i\omega }\left\lbrack  {\ln \left( \frac{{S}_{0}}{K}\right)  + \left( {r - q - \frac{{\sigma }^{2}}{2}}\right) T + \sigma {W}_{T}}\right\rbrack  }\right)= {e}^{{i\omega }\left\lbrack  {\ln \frac{{S}_{0}}{K} + \left( {r - q - \frac{{\sigma }^{2}}{2}}\right) T}\right\rbrack   - \frac{{w}^{2}{\sigma }^{2}}{2}T} \tag{2.46}
$$

累积量为

$$
{c}_{1} = \left( {r - q}\right) T \tag{2.47}
$$

$$
{c}_{2} = {\sigma }^{2}T \tag{2.48}
$$

$$
{c}_{4} = 0 \tag{2.49}
$$

我们使用以下参数进行定价：现货价格 ${S}_{0} = {100}$，无风险利率 $r = {10}\%$，到期时间 $T = {0.1}$，波动率 $\sigma  = {0.25}$。表 2.5 显示了使用 COS 和分数 FFT 方法的结果，行权价分别为 $K = {80},{100},{120}$。参考值是使用已知的 Black–Scholes 解计算的，分别为 20.799, 3.660, 和 0.045。

##### 2.3.4.2 Heston 随机波动率模型

Heston 随机波动率模型在第 1.4.4 节中描述，其特征函数在第 1.4.4.2 节中描述。在该模型下，资产价格由以下 SDE 控制：

$$
d{S}_{t} = \left( {r - q}\right) {S}_{t}{dt} + \sqrt{{v}_{t}}{S}_{t}d{W}_{t}^{\left( 1\right) }
$$

$$
d{v}_{t} = \kappa \left( {\theta  - {v}_{t}}\right) {dt} + \sigma \sqrt{{v}_{t}}d{W}_{t}^{\left( 2\right) }
$$

其中两个布朗运动分量 ${W}_{t}^{\left( 1\right) }$ 和 ${W}_{t}^{\left( 2\right) }$ 以 $\rho$ 的速率相关。变量 ${v}_{t}$ 表示均值回归的随机波动率，其中 $\theta$ 是长期方差，$\kappa$ 是均值回归速度，$\sigma$ 是波动率的波动率。

---

假设 $X$ 的特征函数为 $\phi \left( u\right)$，那么我们可以写成

$$
G\left( \omega \right)  = \log \left( {\phi \left( {-{i\omega }}\right) }\right)
$$

其第 $n$ 个累积量是累积量生成函数在零处的第 $n$ 个导数，即 ${c}_{n} =$ ${G}^{\left( n\right) }\left( 0\right)$。例如，

$$
{c}_{1} = {G}^{\left( 1\right) }\left( 0\right)  = \frac{-i{\phi }^{\left( 1\right) }\left( 0\right) }{\phi \left( 0\right) }
$$

---

表 2.5: 几何布朗运动下的 COS 与分数 FFT 方法比较

| $K$ | $N$ | COS | 分数 FFT |
| --- | --- | --- | --- |
|  |  | 溢价 | CPU 时间 (msc) | 相对误差 | 溢价 | CPU 时间 (msc) | 相对误差 |
| 80 | 16 | 20.791 | 0.166 | 3.9e-04 | 16.867 | 2.476 | 1.9e-01 |
|  | 64 | 20.799 | 0.184 | 1.3e-06 | 20.858 | 2.631 | -2.8e-03 |
|  | 256 | 20.799 | 0.409 | 1.3e-06 | 20.799 | 2.812 | 1.3e-06 |
| 100 | 16 | 3.662 | 0.171 | -5.3e-04 | 7.287 | 2.442 | -9.9e-01 |
|  | 64 | 3.660 | 0.191 | -4.2e-07 | 3.858 | 2.677 | -5.4e-02 |
|  | 256 | 3.660 | 0.282 | -4.2e-07 | 3.660 | 2.845 | 1.6e-05 |
| 120 | 16 | 0.043 | 0.167 | 3.4e-02 | 2.697 | 2.430 | -6.0e+01 |
|  | 64 | 0.045 | 0.203 | 3.1e-07 | -0.102 | 2.642 | 3.3e+00 |
|  | 256 | 0.045 | 0.277 | 3.1e-07 | 0.045 | 2.866 | 2.7e-04 |

##### 2.3.4.3 变异伽马 (VG) 模型

变异伽马模型在第 1.4.6 节中描述，其特征函数在第 1.4.6.2 节中描述。该模型是一个时间变化的布朗运动模型，描述如下：

表 2.6: Heston 随机波动率模型下的 COS 与分数 FFT 方法比较

| $K$ | $N$ | COS | 分数 FFT |
| --- | --- | --- | --- |
|  |  | 溢价 | CPU 时间 (msc) | 相对误差 | 溢价 | CPU 时间 (msc) | 相对误差 |
| 80 | 16 | 32.582 | 1.792 | -2.1e-05 | 32.224 | 2.592 | 1.1e-02 |
|  | 64 | 32.581 | 1.903 | 0.0e+00 | 32.581 | 2.650 | 0.0e+00 |
|  | 256 | 32.581 | 2.205 | 0.0e+00 | 32.581 | 2.941 | 0.0e+00 |
| 100 | 16 | 22.578 | 1.915 | -1.2e-02 | 21.553 | 2.535 | 3.4e-02 |
|  | 64 | 22.319 | 1.887 | 0.0e+00 | 22.319 | 2.676 | 0.0e+00 |
|  | 256 | 22.319 | 1.957 | 0.0e+00 | 22.319 | 3.045 | 0.0e+00 |
| 120 | 16 | 15.192 | 1.814 | -2.6e-02 | 14.296 | 2.454 | 3.4e-02 |
|  | 64 | 14.806 | 1.958 | 0.0e+00 | 14.806 | 2.658 | 0.0e+00 |
|  | 256 | 14.806 | 2.247 | 0.0e+00 | 14.806 | 3.029 | 0.0e+00 |

##### 2.3.4.4 CGMY 模型

CGMY 模型在第 1.4.7 节中描述，其特征函数在第 1.4.7.1 节中描述。对数资产价格过程的特征函数由下式给出：

$$
\mathbb{E}\left\lbrack  {e}^{{iu}{X}_{t}}\right\rbrack   = {e}^{{Ct\Gamma }\left( {-Y}\right) \left( {{\left( M - iu\right) }^{Y} - {M}^{Y} + {\left( G + iu\right) }^{Y} - {G}^{Y}}\right) }
$$

并且 CGMY 模型的累积量为

$$
{c}_{1} = \left( {r + \omega }\right) T + {TC\Gamma }\left( {1 - Y}\right) \left( {-{M}^{Y - 1} + {G}^{Y - 1}}\right)
$$

$$
{c}_{2} = \chi  + {CT\Gamma }\left( {2 - Y}\right) \left( {{M}^{Y - 2} + {G}^{Y - 2}}\right)
$$

$$
{c}_{4} = {CT\Gamma }\left( {4 - Y}\right) \left( {{M}^{Y - 4} + {G}^{Y - 4}}\right)
$$

其中

$$
\omega  =  - {C\Gamma }\left( {-Y}\right) \left( {{\left( M - 1\right) }^{Y} + {\left( G + 1\right) }^{Y} - {M}^{Y} - {G}^{Y}}\right)
$$

$$
\chi  = \frac{8C}{\left( {\left( G + M\right) }^{2} - {\left( G - M\right) }^{2}\right) }
$$

我们使用以下参数进行定价：现货价格 ${S}_{0} = {100}$，无风险利率 $r = {10}\%$，波动率 $\sigma  = {0.12}$，$\theta  =  - {0.14}$，$\nu  = {0.2}$。表 2.7 显示了使用 COS 和分数 FFT 方法的结果，行权价分别为 $K = {90},{100},{120}$。参考值分别为 19.0944, 11.3700, 和 1.92123，这些值是使用 $N = {2}^{15}$ 点的分数 FFT 方法计算的。

表 2.7: 变异伽马模型下的 COS 与分数 FFT 方法比较

| $K$ | $N$ | COS | 分数 FFT |
| --- | --- | --- | --- |
|  |  | 溢价 | CPU 时间 (msc) | 相对误差 | 溢价 | CPU 时间 (msc) | 相对误差 |
| 90 | 16 | 19.008 | 1.785 | 4.8e-03 | 16.202 | 2.518 | 1.5e-01 |
|  | 64 | 19.099 | 1.859 | -2.6e-06 | 19.144 | 2.564 | -2.3e-03 |
|  | 256 | 19.099 | 1.979 | -2.6e-06 | 19.099 | 2.952 | -2.6e-06 |
| 100 | 16 | 11.302 | 1.777 | 6.0e-03 | 11.308 | 2.610 | 5.5e-03 |
|  | 64 | 11.370 | 1.850 | 0.0e+00 | 11.275 | 2.676 | 8.4e-03 |
|  | 256 | 11.370 | 1.957 | 0.0e+00 | 11.370 | 3.151 | 0.0e+00 |
| 120 | 16 | 2.056 | 1.968 | -7.0e-02 | 5.179 | 2.409 | -1.7e+00 |
|  | 64 | 1.921 | 2.012 | 0.0e+00 | 2.005 | 2.735 | -4.4e-02 |
|  | 256 | 1.921 | 2.041 | 0.0e+00 | 1.921 | 2.916 | 1.0e-05 |

CGMY 模型下的 COS 与分数 FFT 方法的比较作为练习留给读者。


---

### 2.4 用于路径依赖期权的余弦方法

前几节讨论的结果表明，COS方法相比之前的变换方法有了显著的改进。然而，以原始形式，它仍然局限于路径独立期权的定价。在 [130] 中，Oosterlee 和 Fang 提出了一种结合向后归纳和COS方法来定价某些类型的路径依赖期权的方法。路径依赖期权的基本余弦方法与普通期权相同，使用方程 (2.35)。路径依赖期权和普通期权定价方法之间的差异在于 ${V}_{k}$ 的计算。对于普通期权，${V}_{k}$ 有一个直接的解析形式，如前所述。对于具有提前行使特征的奇异期权，${V}_{k}$ 需要递归向后计算，因此它是时间依赖的。与FFT方法相比，COS方法不依赖于收益。当我们定价新的衍生品时，我们只需要更新 ${V}_{k}$，而不是从头开始推导FFT特征函数。

#### 2.4.1 百慕大期权

我们将要讨论的第一类路径依赖衍生品是百慕大期权，这些期权在最终到期日之前的一系列离散日期可以行使。在讨论定价之前，我们首先定义一些符号。设 ${t}_{0}$ 为初始时间，${t}_{1},\ldots ,{t}_{M}$ 为预先指定的行使日期，其中 ${t}_{0} < {t}_{1} < \cdots < {t}_{M} = T$，最终到期日，且 ${\Delta t} = {t}_{m} - {t}_{m - 1}$。不失一般性，假设行使日期是等距的。为了给百慕大期权定价，其价值被分为两部分：继续持有价值和立即行使收益。

在时间 ${t}_{m - 1}$，$v\left( {x,{t}_{m - 1}}\right)$ 的值由继续持有价值和提前行使收益价值组成。根据方程 (2.35)，假设期权在当前期间不被行使，一个近似的继续持有价值为

$$
c\left( {x,{t}_{m - 1}}\right) \approx \mathrm{C}\bar{\sum}_{k = 0}^{N - 1}\operatorname{Re}\left\{ \phi \left( \frac{k\pi }{b - a}\right) \exp \left( -ik\pi \frac{a}{b - a}\right) \right\} {V}_{k}\left( {t}_{m}\right) \tag{2.51}
$$

其中

$$
{V}_{k}\left( {t}_{m}\right) = \frac{2}{b - a}\int_{a}^{b}v\left( {y,{t}_{m}}\right) \cos \left( k\pi \frac{y - a}{b - a}\right) dy \tag{2.52}
$$

而行使收益值为 $g\left( {x,{t}_{m - 1}}\right)$

$$
g\left( {x,{t}_{m - 1}}\right) = \left[ \alpha K\left( e^{x} - 1\right) \right]^{+} \tag{2.53}
$$

这里 $x = \ln \left( {X}_{{t}_{m - 1}}/K\right)$，$y = \ln \left( {X}_{{t}_{m}}/K\right)$，且 $\alpha = 1$ 对于看涨期权，$\alpha = -1$ 对于看跌期权。因此，在时间 ${t}_{m - 1}$ 期权的价值为

$$
v\left( {x,{t}_{m - 1}}\right) = \max \left( g\left( {x,{t}_{m - 1}}\right) , c\left( {x,{t}_{m - 1}}\right) \right) \tag{2.54}
$$

这种方法的关键在于如何计算 ${V}_{k}\left( {t}_{m}\right)$。这很困难，需要向后归纳，因为下一个期间的期权价值 $v\left( {y,{t}_{m}}\right)$，以及因此的系数 ${V}_{k}\left( {t}_{m}\right)$，除了到期时，都是未知的。为了解 ${V}_{k}\left( {t}_{m}\right)$，我们首先定义

$$
{C}_{k}\left( {x}_{1},{x}_{2},{t}_{m}\right) = \frac{2}{b - a}\int_{{x}_{1}}^{{x}_{2}}c\left( {x,{t}_{m}}\right) \cos \left( k\pi \frac{x - a}{b - a}\right) dx \tag{2.55}
$$

$$
{G}_{k}\left( {x}_{1},{x}_{2}\right) = \frac{2}{b - a}\int_{{x}_{1}}^{{x}_{2}}g\left( {x,{t}_{m}}\right) \cos \left( k\pi \frac{x - a}{b - a}\right) dx \tag{2.56}
$$

这是与期间 ${t}_{m}$ 的继续持有和立即行使相关的系数。我们有 ${C}_{k}\left( {x}_{1},{x}_{2},{t}_{m}\right)$ 的如下解析形式：

$$
{C}_{k}\left( {x}_{1},{x}_{2},{t}_{m}\right) = e^{-r\Delta t}\sum_{j = 0}^{N - 1}\operatorname{Re}\left\{ \phi \left( \frac{k\pi }{b - a}\right) {V}_{j}\left( {t}_{m + 1}\right) {M}_{k, j}\left( {x}_{1},{x}_{2}\right) \right\} \tag{2.57}
$$

其中

$$
{M}_{k, j}\left( {x}_{1},{x}_{2}\right) = -\frac{i}{\pi }\left( {M}_{k, j}^{c}\left( {x}_{1},{x}_{2}\right) + {M}_{k, j}^{s}\left( {x}_{1},{x}_{2}\right) \right) \tag{2.58}
$$

以及

$$
{M}_{k, j}^{c}\left( {x}_{1},{x}_{2}\right) = \left\{ \begin{array}{l} \frac{\left( {x}_{2} - {x}_{1}\right) \pi i}{b - a} \\ \frac{\exp \left( i\left( j + k\right) \frac{\left( {x}_{2} - a\right) \pi }{b - a}\right) - \exp \left( i\left( j + k\right) \frac{\left( {x}_{1} - a\right) \pi }{b - a}\right) }{j + k} \end{array}\right. \tag{2.59}
$$

$$
{M}_{k, j}^{s}\left( {x}_{1},{x}_{2}\right) = \left\{ \begin{array}{ll} \frac{\left( {x}_{2} - {x}_{1}\right) \pi i}{b - a} & \\ \frac{\exp \left( i\left( j - k\right) \frac{\left( {x}_{2} - a\right) \pi }{b - a}\right) - \exp \left( i\left( j - k\right) \frac{\left( {x}_{1} - a\right) \pi }{b - a}\right) }{j - k} & \end{array}\right. \tag{2.60}
$$

对于 ${G}_{k}$，我们也有一个解析形式

$$
{G}_{k}\left( {x}_{1},{x}_{2}\right) = \frac{2}{b - a}\alpha K\left[ \chi_{k}\left( {x}_{1},{x}_{2}\right) - \varphi_{k}\left( {x}_{1},{x}_{2}\right) \right] \tag{2.61}
$$

其中

$$
\chi_{k}\left( {x}_{1},{x}_{2}\right) = \frac{1}{1 + \left( \frac{k\pi }{b - a}\right)^{2}}\left[ \cos \left( k\pi \frac{{x}_{2} - a}{b - a}\right) e^{{x}_{2}} - \cos \left( k\pi \frac{{x}_{1} - a}{b - a}\right) e^{{x}_{1}}\right.\left. +\frac{k\pi }{b - a}\sin \left( k\pi \frac{{x}_{2} - a}{b - a}\right) e^{{x}_{2}} - \frac{k\pi }{b - a}\sin \left( k\pi \frac{{x}_{1} - a}{b - a}\right) e^{{x}_{1}}\right] \tag{2.62}
$$

$$
\varphi_{k}\left( {x}_{1},{x}_{2}\right) = \left\{ \begin{array}{ll} \left[ \sin \left( k\pi \frac{{x}_{2} - a}{b - a}\right) - \sin \left( k\pi \frac{{x}_{1} - a}{b - a}\right) \right] \frac{b - a}{k\pi } & k \neq 0 \\ \left( {x}_{2} - {x}_{1}\right) & k = 0 \end{array}\right. \tag{2.63}
$$

${C}_{k}\left( {x}_{1},{x}_{2},{t}_{m}\right)$ 的计算可以通过快速傅里叶变换高效地进行，如 [130] 所示。

现在我们可以计算系数 ${V}_{k}\left( {t}_{m}\right)$。首先找到 ${x}_{m}^{*}$ 使得 $c\left( {x}_{m}^{*},{t}_{m}\right) = g\left( {x}_{m}^{*},{t}_{m}\right)$，其中 ${x}_{m}^{*}$ 是时间 ${t}_{m}$ 的提前行使边界，即继续持有变得比立即行使更有利或反之亦然的价格。求解这个边界价格可以通过牛顿-拉夫森法或二分法完成。然后我们可以计算系数 ${V}_{k}\left( {t}_{m}\right)$ 为

$$
{V}_{k}\left( {t}_{m}\right) = \left\{ \begin{array}{ll} {C}_{k}\left( a,{x}_{m}^{*},{t}_{m}\right) + {G}_{k}\left( {x}_{m}^{*}, b\right) & \text{对于看涨期权} \\ {C}_{k}\left( {x}_{m}^{*}, b,{t}_{m}\right) + {G}_{k}\left( a,{x}_{m}^{*}\right) & \text{对于看跌期权} \end{array}\right. \tag{2.64}
$$

对于 $m = M - 1, M - 2,\ldots ,1$。这将下一个期间的价格积分划分为继续持有区域和行使区域。对于最终条件，我们有

$$
{V}_{k}\left( {t}_{M}\right) = \left\{ \begin{array}{ll} {G}_{k}\left( 0, b\right) & \text{对于看涨期权} \\ {G}_{k}\left( a,0\right) & \text{对于看跌期权} \end{array}\right. \tag{2.65}
$$

我们首先从 ${V}_{k}\left( {t}_{M}\right)$ 开始，向后归纳地计算以得到 ${V}_{k}\left( {t}_{1}\right)$，原始期权价值表示为

$$
v\left( {x,{t}_{0}}\right) \approx \mathrm{C}\sum_{k = 0}^{N - 1}\operatorname{Re}\left\{ \phi \left( \frac{k\pi }{b - a}\right) \exp \left( -ik\pi \frac{a}{b - a}\right) \right\} {V}_{k}\left( {t}_{1}\right) \tag{2.66}
$$

#### 2.4.2 离散监测障碍期权

接下来我们将讨论的路径依赖衍生品是离散监测障碍期权，如果标的资产价格在预先指定的日期之一触及障碍，则这些期权将不再存在。障碍期权有多种类型，但在这里我们将讨论上敲出期权，其收益为

$$
V\left( {X, t}\right) = \max \left( \alpha \left( {X}_{T} - K\right) ,0\right) \left| \left( {X}_{{t}_{i}} < H\right) + R\right| \left( {X}_{{t}_{i}} \geq H\right) \tag{2.67}
$$

其中 $R$ 是回扣，${X}_{{t}_{i}}$ 是在离散监测时间的标的资产价格水平。系数 ${V}_{k}\left( {t}_{m}\right)$ 的公式再次分为一个继续持有部分，假设价格未触及障碍，以及一个表示价格已触及障碍的部分，

$$
{V}_{k}\left( {t}_{m}\right) = {C}_{k}\left( a, h,{t}_{m}\right) + e^{-r\left( T - {t}_{m - 1}\right) }\frac{2R}{b - a}\varphi_{k}\left( h, b\right) \tag{2.68}
$$

对于定价期权，我们从 ${V}_{k}\left( {t}_{M}\right)$ 开始，其中对于 $h < 0$

$$
{V}_{k}\left( {t}_{M}\right) = \left\{ \begin{array}{ll} {G}_{k}\left( 0, b\right) + \frac{2R}{b - a}\varphi \left( a, h\right) & \text{对于看涨期权} \\ {G}_{k}\left( h,0\right) + \frac{2R}{b - a}\varphi \left( a, h\right) & \text{对于看跌期权} \end{array}\right. \tag{2.69}
$$

表 2.8: 离散监测障碍期权的定价结果 - COS 与 MC

| Method | Model | $N$ | Call | Put | Time (sec) |
| --- | --- | --- | --- | --- | --- |
| COS | BS | $2^{6}$ | 1.8494 | 5.4846 | 0.1238 |
| MC | BS | $10^{6}$ | 1.8487 | 5.4794 | 1.0178 |
| COS | VG | $2^{6}$ | 4.1935 | 3.1572 | 0.1562 |
| MC | VG | $10^{6}$ | 4.1949 | 3.1557 | 10.1335 |

以及对于 $h \geq 0$

$$
{V}_{k}\left( {t}_{M}\right) = \left\{ \begin{array}{ll} {G}_{k}\left( 0, h\right) + \frac{2R}{b - a}\varphi \left( h, b\right) & \text{对于看涨期权} \\ {G}_{k}\left( a,0\right) + \frac{2R}{b - a}\varphi \left( h, b\right) & \text{对于看跌期权} \end{array}\right. \tag{2.70}
$$

##### 2.4.2.1 数值结果 - COS 与蒙特卡洛

这里我们提供了一些使用COS方法和蒙特卡洛模拟定价离散监测障碍期权的数值结果。本例中考虑的模型是Black-Scholes模型和方差伽玛模型。用于Black-Scholes模型的参数为：现货价格 ${S}_{0} = 100$，行权价 $K = 100$，到期时间 $T = 1$ 年，预先指定的监测时间 $M = 12$，等距的月障碍 $H = 120$，回扣 $R = 0$，无风险利率 $r = 5\%$，以及波动率 $\sigma = 0.2$。用于VG模型的参数相同，只是VG特定模型参数 $\sigma = 0.12$，$\nu = 0.2$，以及 $\theta = -0.14$。

表 2.8 显示了结果。正如我们观察到的，每种模型在两种方法下的溢价都非常接近。然而，COS方法比蒙特卡洛模拟显著更快。

### 2.5 鞍点方法

COS和FFT方法有许多显著的优势。例如，它们能够在给定已知特征函数的模型下定价衍生品，它们非常快，而且能够在一次运行中生成多个期权价格。特别是，COS方法在重新推导多种不同的收益（包括欧式和某些路径依赖期权）时所需的工作量非常少。然而，如前所述，这两种方法对于极度价外期权可能不准确。

在 [70] 中，Carr 和 Madan 建议了一种专门设计用于更准确地定价价外期权的替代方法。这种方法称为鞍点方法，涉及将期权价格表示为一个特别构造的随机变量超过对数行权价的随机变量的概率，然后使用修改后的Lugannani-Rice鞍点近似来求解这个概率。

鞍点方法在定价价外期权时提供了比FFT或COS方法显著更好的准确性。然而，对于平价和价内期权，该算法的准确性相比这两种方法有所不足，而且像FFT方法一样，其解必须针对每种不同的收益函数重新推导。

在 [299] 中，Yeung 和 Hirsa 延伸了 [141] 中提出的鞍点方程，以推导长时间模型隐含波动率微笑，提供了其理论基础，并研究了其在经典模型中的应用。只要特征函数在长时间内表现出Levy类型的缩放行为，该方法就允许我们分析地研究特定模型下的长时间微笑行为，并且能够达到非常广泛的无套利模型启发的参数化，类似于随机波动率启发（SVI）。

模型：

所有存在资产价格分布的累积生成函数（CGF）的模型。通过扩展，任何可以从特征函数推导出的模型。

期权类型：

路径独立的欧式期权。

优点

1. 能够非常准确地定价深度价外期权

缺点

1. 仅限于路径独立的欧式期权
2. 需要针对不同的收益函数重新推导解

#### 2.5.1 广义Lugannani-Rice近似

我们将从广义Lugannani-Rice近似的讨论开始。这些近似允许我们使用所讨论的随机变量的累积生成函数（CGF）准确地近似随机变量超过给定水平的概率。通常选择一个基础随机变量的CGF，使其在平移和缩放变换后与所讨论的随机变量相似，以及基础随机变量的累积分布函数（CDF）和概率密度函数（PDF）。

在 [234] 中提出的Lugannani-Rice鞍点公式已经被证明是独立随机变量和的累积分布函数的一个非常出色的近似。在其标准形式中，连续随机变量 $X$ 的尾概率的Lugannani-Rice近似为(2.71)

$$
P\left( X \geq y\right) = 1 - \Phi \left( \widehat{w}\right) + \phi \left( \widehat{w}\right) \left( \frac{1}{\widehat{u}} - \frac{1}{\widehat{w}}\right) \tag{2.72}
$$

---

${}^{9}$ 对于随机变量 $X$，其累积生成函数定义为

$$
G\left( \omega \right) = \log \left( \mathbb{E}\left[ \exp \left( \omega X\right) \right] \right)
$$

---

其中 $\Phi$ 和 $\phi$ 是标准正态分布的累积分布函数和概率密度函数

$$
\widehat{w} = \operatorname{sgn}\left( \widehat{t}\right) \sqrt{2\left( \widehat{t}y - K\left( \widehat{t}\right) \right)} \tag{2.73}
$$

以及

$$
\widehat{u} = \widehat{t}\sqrt{K''\left( \widehat{t}\right)} \tag{2.74}
$$

其中 $K\left( t\right)$ 是随机变量 $X$ 的累积生成函数（CGF），而 $\widehat{t}$ 是鞍点方程 $K'\left( t\right) = y$ 的唯一解。

如 [298] 所述，Lugannani-Rice近似的一个中心特征是，对于给定的 $y$ 和 $K\left( t\right)$，我们使用从 $t$ 到 $w$ 的变换，该变换由

$$
\frac{1}{2}w^{2} - \widehat{w}w = K\left( t\right) - ty \tag{2.75}
$$

确定，其中 $\widehat{w}$ 被选择使得 $\frac{1}{2}w^{2} - \widehat{w}w$ 的最小值等于 $K\left( t\right) - ty$ 的最小值。基本思想是找到一个变换，描述函数 $K\left( t\right) - ty$ 在包含 $t = \widehat{t}$ 和 $t = 0$ 的区域内的局部行为，当 $\widehat{t}$ 较小时。这样的变换为

$$
\frac{1}{2}\left( w - \widehat{w}\right)^{2} = K\left( t\right) - ty - K\left( \widehat{t}\right) + \widehat{t}y \tag{2.76}
$$

如果 $\widehat{w}$ 被选择使得

$$
K\left( \widehat{t}\right) - \widehat{t}y = -\frac{1}{2}\widehat{w}^{2} \tag{2.77}
$$

那么这变为

$$
\frac{1}{2}w^{2} - \widehat{w}w = K\left( t\right) - tK'\left( \widehat{t}\right) \tag{2.78}
$$

其中

$$
\widehat{w} = \sqrt{2\left( \widehat{t}K'\left( \widehat{t}\right) - K\left( \widehat{t}\right) \right)} \tag{2.79}
$$

所需的等式在 $\widehat{w}$ 由

$$
\widehat{w} = 2\widehat{t}\left[ K'\left( \widehat{t}\right) - K\left( \widehat{t}\right) \right]^{1/2} \tag{2.80}
$$

给出时成立。

$\frac{1}{2}w^{2} - \widehat{w}w$ 的近似形式也解释了为什么标准正态分布的CDF和PDF $\Phi$ 和 $\phi$ 会出现在方程中，因为 $\frac{1}{2}w^{2}$ 是标准正态分布的CGF。

然而，没有特别的理由必须在方程中使用 $\frac{1}{2}w^{2}$；任何在原点解析的CGF都可以工作。假设 $G\left( w\right)$ 是基础分布的CGF。对于每个 $\xi$，${w}_{\xi}$ 是鞍点方程 ${G}'\left( w\right) = \xi$ 的唯一解。定义 $\widehat{t}$ 为方程

$$
{K}'\left( t\right) = y \tag{2.81}
$$

的解。然后通过类似的近似，我们找到

$$
G\left( {w}_{\xi}\right) - \xi {w}_{\xi} = K\left( \widehat{t}\right) - \widehat{t}y \tag{2.82}
$$

现在 $G\left( {w}_{\xi}\right) - \xi {w}_{\xi}$ 是 $G$ 的Legendre-Fenchel变换，因此左侧是 $\xi$ 的凹函数。对于固定的 $y$，在 $\xi$ 中最多有两个解。

$$
{\xi}_{-} = {\xi}_{-}\left( y\right) < {G}'\left( 0\right) < {\xi}_{+} = {\xi}_{+}\left( y\right) \tag{2.83}
$$

因此，如果 $y < {K}'\left( 0\right)$，我们选择 $\widehat{\xi} = {\xi}_{-}$；如果 $y \geq {K}'\left( 0\right)$，我们选择 $\widehat{\xi} = {\xi}_{+}$。假设 $\Gamma$ 和 $\gamma$ 是CGF为 $G$ 的分布的CDF和PDF。那么随机变量 $X$ 的修改后的Lugannani-Rice公式为

$$
P\left( X > y\right) = 1 - \Gamma \left( \widehat{\xi}\right) + \gamma \left( \widehat{\xi}\right) \left( \frac{1}{{\widehat{u}}_{\widehat{\xi}}} - \frac{1}{{\omega}_{\widehat{\xi}}}\right) \tag{2.84}
$$

其中

$$
\widehat{u} = \widehat{t}\left( K''\left( \widehat{t}\right) \right)^{1/2} \tag{2.85}
$$

$$
{\widehat{u}}_{\widehat{\xi}} = \frac{\widehat{u}}{\left( {G}''\left( {w}_{\widehat{\xi}}\right) \right)^{1/2}} \tag{2.86}
$$

这个推导在 [298] 中有概述。注意，如果 $G = K$，那么 ${w}_{\widehat{\xi}} = {\widehat{u}}_{\widehat{\xi}} = \widehat{t}$，在这种情况下，近似是精确的。

#### 2.5.2 期权价格作为尾概率

如果我们打算使用Lugannani-Rice近似来改进远期价外期权的定价，我们必须首先将期权价格表示为尾概率。在本节中，我们将概述如何做到这一点。

我们用 ${S}_{t}$ 表示期权标的在时间 $t$ 的价格，用 ${B}_{t}$ 表示时间 $t$ 的现金账户价值。我们知道，在风险中性定价原则下，如果我们使用 ${B}_{t}$ 作为计价单位，任何可交易证券在风险中性测度 $\mathbb{Q}$ 下除以 ${B}_{t}$ 是一个鞅。我们定义一个新的测度，即份额测度 $\mathbb{S}$，其中 ${S}_{t}$ 是计价单位。因此，任何可交易证券在份额测度下除以 ${S}_{t}$ 都是一个鞅。这意味着

$$
\frac{{C}_{t}}{{S}_{t}} = \mathbb{E}_{t}^{\mathbb{S}}\left( \frac{{C}_{T}}{{S}_{T}}\right) \tag{2.87}
$$

对于行权价为 $K$ 的看涨期权，我们可以写为

$$
\frac{C\left( K\right)}{{S}_{0}} = \mathbb{E}^{\mathbb{S}}\left( \frac{\left( {S}_{T} - K\right)^{+}}{{S}_{T}}\right) \tag{2.88}
$$

如果我们假设证券价格 ${S}_{T}$ 始终为正，我们得到

$$
\frac{C\left( K\right)}{{S}_{0}} = \mathbb{E}^{\mathbb{S}}\left( \left( 1 - \frac{K}{{S}_{T}}\right)^{+}\right) \tag{2.89}
$$

我们定义 $y = \log \left( \frac{{S}_{T}}{K}\right)$，这意味着 $\frac{K}{{S}_{T}} = e^{-y}$，使用这个定义，我们可以将标准化的看涨期权价格重写为

$$
\frac{C\left( K\right)}{{S}_{0}} = \int_{0}^{\infty}\left( 1 - e^{-y}\right) f\left( y\right) dy \tag{2.90}
$$

其中 $f\left( y\right)$ 是 $y = \ln \left( {S/K}\right)$ 在份额测度下的概率密度函数。我们通过分部积分得到

$$
\frac{C\left( K\right)}{{S}_{0}} = \int_{0}^{\infty}\left( 1 - e^{-y}\right) f\left( y\right) dy= \left. \left( 1 - e^{-y}\right) F\left( y\right) \right|_{0}^{\infty} - \int_{0}^{\infty}e^{-y}F\left( y\right) dy
\\
= \left. \left( F\left( y\right) - F\left( y\right) e^{-y}\right) \right|_{0}^{\infty} - \int_{0}^{\infty}e^{-y}F\left( y\right) dy= 1 - \int_{0}^{\infty}e^{-y}F\left( y\right) dy= \int_{0}^{\infty}e^{-y}dy - \int_{0}^{\infty}e^{-y}F\left( y\right) dy= \int_{0}^{\infty}\left( 1 - F\left( y\right) \right) e^{-y}dy
$$

因此，我们有

$$
\frac{C\left( K\right)}{{S}_{0}} = \int_{0}^{\infty}\left( 1 - F\left( y\right) \right) e^{-y}dy
$$

对于给定的 $y$，表达式 $1 - F\left( y\right)$ 是 $\ln \left( {S/K}\right)$ 大于 $y$ 的概率。考虑到 $e^{-y}$ 是一个正指数随机变量（$\lambda = 1$）的概率密度函数，标准化的看涨期权价格是份额测度下股票价格的对数超过行权价的对数加上一个独立的指数变量的概率 [70]，或者等价地

$$
\frac{C\left( K\right)}{{S}_{0}} = P\left( \ln \left( {S/K}\right) > Y\right) \tag{2.91}
$$

$$
= P\left( \ln S - \ln K > Y\right) \tag{2.92}
$$

$$
= P\left( X - Y > \ln K\right) \tag{2.93}
$$

其中 $X$ 是份额测度下股票的对数，$Y$ 是一个独立的指数变量，$K$ 是行权价。

一旦我们知道随机变量 $X - Y$ 的累积生成函数 $K\left( x\right)$ 及其前两个导数，即 $K'\left( x\right)$ 和 $K''\left( x\right)$，鞍点方法就给出了 $P\left( X - Y > \ln K\right)$ 的近似值。

假设 ${K}_{0}\left( x\right)$ 是某个风险中性测度下股票价格对数的CGF，那么份额测度下股票价格对数减去一个指数变量的CGF由

$$
K\left( x\right) = {K}_{0}\left( x + 1\right) - {K}_{0}\left( 1\right) - \ln \left( 1 + x\right) \tag{2.94}
$$

给出。其前两个导数可以容易地计算并给出为

$$
K'\left( x\right) = {K}_{0}'\left( x + 1\right) - \frac{1}{1 + x} \tag{2.95}
$$

$$
K''\left( x\right) = {K}_{0}''\left( x + 1\right) + \frac{1}{\left( 1 + x\right)^{2}} \tag{2.96}
$$

#### 2.5.3 Lugannani-Rice近似用于期权定价

在上一节中，我们展示了可以用来表示看涨期权价格为尾概率的密度是一个高斯随机变量减去一个独立的指数随机变量。因此，我们将考虑一个形式相同的基础Lugannani-Rice分布，使用 $Z \sim N\left( 0,1\right)$，一个标准高斯分布，以及 $Y \sim \exp \left( \lambda \right)$，一个指数分布。我们定义基础分布为

$$
Z + \frac{1}{\lambda} - Y \tag{2.97}
$$

该基础分布的累积生成函数为

$$
G\left( w\right) = \frac{w^{2}}{2} + \frac{w}{\lambda} - \ln \left( \frac{\lambda + w}{\lambda}\right)= \frac{w^{2}}{2} + \frac{w}{\lambda} - \ln \left( \lambda + w\right) + \ln \left( \lambda \right)
$$

其前两个导数为

$$
G'\left( w\right) = w + \frac{1}{\lambda} - \frac{1}{\lambda + w}
$$

$$
G''\left( w\right) = 1 + \left( \frac{1}{\lambda + w}\right)^{2}
$$

该分布的CDF和PDF在 [70] 中显示为

$$
\widetilde{\Phi}\left( y\right) = N\left( \frac{1}{\lambda} - y\right) - \exp \left( \lambda y - 1 + \frac{\lambda^{2}}{2}\right) N\left( \frac{1}{\lambda} - y - \lambda \right) \tag{2.98}
$$

$$
\widetilde{\phi}\left( y\right) = n\left( \frac{1}{\lambda} - y\right) + \lambda \exp \left( \lambda y - 1 + \frac{\lambda^{2}}{2}\right) N\left( \frac{1}{\lambda} - y - \lambda \right)- \exp \left( \lambda y - 1 + \frac{\lambda^{2}}{2}\right) n\left( \frac{1}{\lambda} - y - \lambda \right) \tag{2.99}
$$

其中 $N\left( x\right)$ 和 $n\left( x\right)$ 分别是标准正态分布 $\mathcal{N}\left( 0,1\right)$ 的累积分布函数和概率密度函数。我们定义 $y$ 为行权价的对数，算法的第一步是通过求解

$$
\begin{array}{r} K'\left( \widehat{t}\right) = y \\ \lambda = \sqrt{K''\left( \widehat{t} + 1\right)} \end{array} \tag{2.101}
$$

来确定 $\widehat{t}$ 和 $\lambda$。

然后我们必须通过求解

$$
K\left( \widehat{t}\right) - \widehat{t}y = G\left( \omega_{\widehat{\xi}}\right) - \widehat{\xi} \omega_{\widehat{\xi}} \tag{2.103}
$$

$$
G'\left( \omega_{\widehat{\xi}}\right) = \widehat{\xi} \tag{2.104}
$$

来求解 $\widehat{\xi}$ 和 $\omega_{\widehat{\xi}}$，其中高斯-芬谢尔变换为

$$
\omega_{\widehat{\xi}} = -\lambda + \frac{c}{2} + \sqrt{\frac{c^{2}}{4} + 1} \tag{2.105}
$$

$$
c = \widehat{\xi} - \frac{1}{\lambda} + \lambda \tag{2.106}
$$

对于 $\widehat{\xi}$ 有两个解，如果 $y < K'\left( 0\right)$，我们选择 $\widehat{\xi} < G'\left( 0\right)$；如果 $y \geq K'\left( 0\right)$，我们选择 $\widehat{\xi} \geq G'\left( 0\right)$。如果我们定义

$$
\widehat{u} = \widehat{t} \sqrt{K''\left( \widehat{t}\right)}
$$

$$
\widehat{u}_{\widehat{\xi}} = \frac{\widehat{u}}{\sqrt{G''\left( \omega_{\widehat{\xi}}\right)}}
$$

那么根据标准的Lugannani-Rice方法，我们可以计算互补概率如下：

$$
P\left( X - Y > y\right) = \widetilde{\Phi}\left( \widehat{\xi}\right) + \widetilde{\phi}\left( \widehat{\xi}\right) \left( \frac{1}{\widehat{u}_{\widehat{\xi}}} - \frac{1}{\omega_{\widehat{\xi}}}\right)
$$

#### 2.5.4 鞍点近似的实现

在本节中，我们将描述鞍点近似的逐步实现。我们从以下步骤开始：

- 使用二分法求解 $\widehat{t}$ 的方程

$$
K'\left( \widehat{t}\right) = y \tag{2.107}
$$

其中 $y = \log \left( K\right)$，$K$ 是行权价。

- 求解

$$
G'\left( \omega_{\widehat{\xi}}\right) = \widehat{\xi} \tag{2.108}
$$

其中我们有

$$
\omega_{\widehat{\xi}} = -\lambda + \frac{c}{2} + \sqrt{\frac{c^{2}}{4} + 1} \tag{2.109}
$$

$$
c = \widehat{\xi} - \frac{1}{\lambda} + \lambda \tag{2.110}
$$

- 再次使用二分法结合 (2.109) 和 (2.110) 求解

$$
K\left( \widehat{t}\right) - \widehat{t}y = G\left( \omega_{\widehat{\xi}}\right) - \widehat{\xi} \omega_{\widehat{\xi}} \tag{2.111}
$$

注意，对于 $\widehat{\xi}$ 有两个解，如果 $y < K'\left( 0\right)$，我们选择 $\widehat{\xi} < G'\left( 0\right)$；如果 $y \geq K'\left( 0\right)$，我们选择 $\widehat{\xi} \geq G'\left( 0\right)$。

- 如果我们定义

$$
\widehat{u} = \widehat{t} \sqrt{K''\left( \widehat{t}\right)}
$$

$$
\widehat{u}_{\widehat{\xi}} = \frac{\widehat{u}}{\sqrt{G''\left( \omega_{\widehat{\xi}}\right)}}
$$

那么根据标准的Lugannani-Rice方法，我们可以计算互补概率如下：

$$
P\left( X > y\right) = \widetilde{\Phi}\left( \widehat{\xi}\right) + \phi \left( \widehat{\xi}\right) \left( \frac{1}{\widehat{u}_{\widehat{\xi}}} - \frac{1}{\omega_{\widehat{\xi}}}\right)
$$

其中

$$
\widetilde{\Phi}\left( x\right) = N\left( \frac{1}{\lambda} - x\right) - \exp \left( \lambda x - 1 + \frac{\lambda^{2}}{2}\right) N\left( \frac{1}{\lambda} - x - \lambda \right)
$$

$$
\phi \left( x\right) = n\left( \frac{1}{\lambda} - x\right) + \lambda \exp \left( \lambda x - 1 + \frac{\lambda^{2}}{2}\right) N\left( \frac{1}{\lambda} - x - \lambda \right)- \exp \left( \lambda x - 1 + \frac{\lambda^{2}}{2}\right) n\left( \frac{1}{\lambda} - x - \lambda \right)
$$

而 $n\left( x\right)$ 和 $N\left( x\right)$ 分别是标准正态分布的PDF和CDF。

- 然后，看涨期权的价格可以通过以下公式近似

$$
C = S_{0} \times P\left( X > \ln K\right) \tag{2.112}
$$

其中 $X$ 是份额测度下股票的对数减去一个独立的指数变量，$K$ 是行权价。

如果我们使用上述的基础模型，那么 $G\left( w\right)$ 和 $K\left( x\right)$ 的公式如下：

$$
G\left( w\right) = \frac{w^{2}}{2} + \frac{w}{\lambda} - \ln \left( \lambda + w\right) + \ln \lambda \tag{2.113}
$$

$$
G'\left( w\right) = w + \frac{1}{\lambda} - \frac{1}{\lambda + w} \tag{2.114}
$$

$$
G''\left( w\right) = 1 + \left( \frac{1}{\lambda + w}\right)^{2} \tag{2.115}
$$

以及

$$
K\left( x\right) = K_{0}\left( x + 1\right) - K_{0}\left( 1\right) - \ln \left( 1 + x\right) \tag{2.116}
$$

$$
K'\left( x\right) = K_{0}'\left( x + 1\right) - \frac{1}{1 + x} \tag{2.117}
$$

$$
K''\left( x\right) = K_{0}''\left( x + 1\right) + \frac{1}{\left( 1 + x\right)^{2}} \tag{2.118}
$$

其中 $K_{0}$ 是风险中性测度下股票对数的CGF，这在不同的模型中有所不同。

在提供的解中，我们选择

$$
\lambda = \sqrt{K''\left( \widehat{t} + 1\right)}
$$

#### 2.5.5 鞍点方法的数值结果

在本节中，我们展示了一些使用快速傅里叶变换、分数傅里叶变换、COS和鞍点技术在几何布朗运动、Heston随机波动率、方差伽玛和CGMY模型下对各种行权价的欧式看涨期权定价的比较结果。表格旨在为读者提供一些实证结果，并说明鞍点方法在价外期权定价中的准确性。

##### 2.5.5.1 几何布朗运动（GBM）

GBM过程遵循以下随机微分方程（SDE）：

$$
dS_{t} = \left( r - q\right) S_{t} dt + \sigma S_{t} dW_{t} \tag{2.119}
$$

其CGF及其前两个导数为

$$
K_{0}\left( x\right) = x\left( \ln S_{0} + \left( r - q - \frac{\sigma^{2}}{2}\right) t\right) + \frac{x^{2} \sigma^{2}}{2} t \tag{2.120}
$$

$$
K_{0}'\left( x\right) = \ln \left( S_{0}\right) + \left( r - q - \frac{\sigma^{2}}{2}\right) t + \sigma^{2} x t \tag{2.121}
$$

$$
K_{0}''\left( x\right) = \sigma^{2} t \tag{2.122}
$$

表 2.9: 通过各种变换技术对不同行权价的GBM欧式看涨期权定价结果

| $K$ | BS | COS | FrFFT | FFT | SP |
| --- | --- | --- | --- | --- | --- |
| 10 | 90.0830 | 94.4112 | 90.0829 | 90.0830 | 90.0832 |
| 20 | 80.1660 | 82.5614 | 80.1660 | 80.1660 | 80.1483 |
| 30 | 70.2490 | 70.2490 | 70.2490 | 70.2490 | 69.0518 |
| 40 | 60.3319 | 60.3319 | 60.3319 | 60.3319 | 60.3529 |
| 50 | 50.4149 | 50.4149 | 50.4149 | 50.4149 | 50.4144 |
| 60 | 40.4979 | 40.4979 | 40.4979 | 40.4979 | 40.4977 |
| 70 | 30.5809 | 30.5809 | 30.5808 | 30.5809 | 30.5809 |
| 80 | 20.6651 | 20.6651 | 20.6650 | 20.6651 | 20.6650 |
| 90 | 10.9147 | 10.9147 | 10.9149 | 10.9147 | 10.9148 |
| 100 | 3.3006 | 3.3006 | 3.3004 | 3.3006 | 3.3004 |
| 110 | 0.4182 | 0.4182 | 0.4182 | 0.4182 | 0.4182 |
| 120 | 0.0207 | 0.0207 | 0.0207 | 0.0207 | 0.0207 |
| 130 | 4.42e-04 | 4.42e-04 | 4.52e-04 | 4.42e-04 | 4.42e-04 |
| 140 | 4.69e-06 | 4.42e-06 | -2.05e-05 | 4.57e-06 | 4.69e-06 |
| 150 | 2.82e-08 | -3.49e-05 | 2.85e-05 | 2.29e-07 | 2.82e-08 |
| 160 | 1.08e-10 | -1.57e-03 | -1.55e-05 | -4.47e-08 | 1.08e-10 |
| 170 | 2.86e-13 | -2.93e-02 | -3.82e-06 | -7.30e-08 | 2.89e-13 |
| 180 | 5.72e-16 | -2.66e-01 | 1.18e-05 | 1.10e-07 | 2.57e-21 |
| 190 | 9.13e-19 | -1.36e+00 | -3.11e-06 | -1.06e-07 | -4.11e-24 |
| 200 | 1.22e-21 | -4.45e+00 | -6.58e-06 | 9.37e-08 | 2.39e-27 |

我们使用以下参数进行定价：现货价格 ${S}_{0} = 100$，无风险利率 $r = 5\%$，到期时间 $T = 1/12$，波动率 $\sigma = 0.25$。表 2.9 显示了使用Black-Scholes公式、Fourier余弦（COS）、分数FFT（FrFFT）、快速傅里叶变换（FFT）和鞍点（SP）方法对行权价从10到200的期权定价结果。

##### 2.5.5.2 Heston随机波动率模型

Heston随机波动率模型遵循以下随机微分方程（SDE）：

$$
dS_{t} = r S_{t} dt + \sqrt{v_{t}} S_{t} dW_{1t} \tag{2.123}
$$

$$
dv_{t} = \kappa \left( \theta - v_{t}\right) dt + \sigma \sqrt{v_{t}} dW_{2t} \tag{2.124}
$$

其CGF为

$$
K_{0}\left( x\right) = \left( \ln S_{0} + r t\right) x + \frac{\kappa \theta t \left( \kappa - \rho \sigma x\right)}{\sigma^{2}} - \frac{2 \kappa \theta}{\sigma^{2}} \ln \alpha \left( x\right)+ \frac{\left( x^{2} - x\right) v_{0}}{\gamma \left( x\right) \alpha \left( x\right)} \sinh \frac{\gamma \left( x\right) t}{2} \tag{2.125}
$$

其中

$$
\gamma \left( x\right) = \sqrt{\sigma^{2} \left( -x^{2} + x\right) + \left( \kappa - x \rho \sigma \right)^{2}} \tag{2.126}
$$

$$
\alpha \left( x\right) = \cosh \frac{\gamma \left( x\right) t}{2} + \frac{\kappa - x \rho \sigma}{\gamma \left( x\right)} \sinh \frac{\gamma \left( x\right) t}{2} \tag{2.127}
$$

表 2.10: 通过各种变换技术对不同行权价的Heston欧式看涨期权溢价

| $K$ | MC | COS | FrFFT | FFT | SP |
| --- | --- | --- | --- | --- | --- |
| 10 | 91.5068 | 90.6275 | 90.1489 | 90.1489 | 90.1010 |
| 20 | 81.5068 | 80.3014 | 80.2978 | 80.2977 | 80.1590 |
| 30 | 71.5068 | 70.4467 | 70.4467 | 70.4467 | 69.8742 |
| 40 | 61.5081 | 60.5965 | 60.5967 | 60.5967 | 54.2022 |
| 50 | 51.5170 | 50.7539 | 50.7541 | 50.7541 | 50.3408 |
| 60 | 41.5600 | 40.9446 | 40.9449 | 40.9449 | 40.7358 |
| 70 | 31.7184 | 31.2484 | 31.2486 | 31.2487 | 31.1377 |
| 80 | 22.1918 | 21.8620 | 21.8622 | 21.8622 | 21.8040 |
| 90 | 13.4038 | 13.2020 | 13.2023 | 13.2022 | 13.1275 |
| 100 | 6.1522 | 6.0552 | 6.0555 | 6.0554 | 5.9538 |
| 110 | 1.6659 | 1.6368 | 1.6371 | 1.6371 | 1.6043 |
| 120 | 2.41e-01 | 2.34e-01 | 2.35e-01 | 2.35e-01 | 2.39e-01 |
| 130 | 2.89e-02 | 2.72e-02 | 2.75e-02 | 2.74e-02 | 2.88e-02 |
| 140 | 3.72e-03 | 3.13e-03 | 3.39e-03 | 3.36e-03 | 3.57e-03 |
| 150 | 4.28e-04 | 1.97e-04 | 4.60e-04 | 4.78e-04 | 4.84e-04 |
| 160 | 3.25e-05 | -1.94e-04 | 6.89e-05 | 7.50e-05 | 7.23e-05 |
| 170 | 0.00e+00 | -2.52e-04 | 1.13e-05 | -2.87e-06 | 1.18e-05 |
| 180 | 0.00e+00 | -2.61e-04 | 2.03e-06 | 1.51e-05 | 2.12e-06 |
| 190 | 0.00e+00 | -2.63e-04 | 3.94e-07 | -9.71e-06 | 4.11e-07 |
| 200 | 0.00e+00 | -2.63e-04 | 8.23e-08 | 8.02e-06 | 8.59e-08 |

需要注意的是，$\gamma \left( x\right)$ 和 $\alpha \left( x\right)$ 可以是复数，但 ${K}_{0}\left( x\right)$ 的公式仍然有效。我们使用数值微分来计算其前两个导数：

$$
K_{0}'\left( x\right) = \frac{K_{0}\left( x + h\right) - K_{0}\left( x - h\right)}{2h} \tag{2.128}
$$

$$
K_{0}''\left( x\right) = \frac{K_{0}\left( x + h\right) - 2K_{0}\left( x\right) + K_{0}\left( x - h\right)}{h^{2}} \tag{2.129}
$$

我们使用以下参数进行定价：现货价格 ${S}_{0} = 100$，无风险利率 $r = 3\%$，均值回归率 $\kappa = 2$，波动率的波动率 $\sigma = 0.5$，长期方差 $\theta = 0.04$，初始方差 ${v}_{0} = 0.04$，相关性 $\rho = -0.7$，到期时间 $T = 0.5$。表 2.10 显示了使用蒙特卡洛模拟 ${}^{10}$、FFT、FrFFT、COS和鞍点方法对行权价从10到200的期权定价结果。

##### 2.5.5.3 方差伽玛模型

方差伽玛模型由以下方程组描述：

$$
\ln \left( \frac{S_{t}}{S_{0}}\right) = \left( r + \omega \right) t + X_{VG}\left( t;\sigma ,\nu ,\theta \right)
$$

$$
X_{VG} = \theta G\left( t;\nu \right) + \sigma W\left( G\left( t;\nu \right) \right)
$$

$$
\omega = \frac{1}{\nu} \ln \left( 1 - \theta \nu - \frac{\sigma^{2} \nu}{2} \right)
$$

其中 $G\left( t;\nu \right)$ 是伽玛过程，$\omega$ 是凸性修正。在该模型下，CGF及其前两个导数为

$$
K_{0}\left( x\right) = x\left( \left( r + \omega \right) t + \ln S_{0} \right) - \frac{t}{\nu} \ln \left( 1 - x \theta \nu - \frac{\nu \sigma^{2} x^{2}}{2} \right)
$$

$$
K_{0}'\left( x\right) = \ln S_{0} + \left( r + \omega \right) t + t \left( \frac{\theta + \sigma^{2} x}{1 - \theta \nu x - 0.5 \nu \sigma^{2} x^{2}} \right)
$$

$$
K_{0}''\left( x\right) = \frac{t \sigma^{2}}{1 - \theta \nu x - 0.5 \nu \sigma^{2} x^{2}} + t \nu \left( \frac{\theta + \sigma^{2} x}{1 - \theta \nu x - 0.5 \nu \sigma^{2} x^{2}} \right)^{2}
$$

---

${}^{10}$ 我们将在第6章中讨论蒙特卡洛模拟。然而，我们已经使用蒙特卡洛模拟的价格作为基准。

---

表 2.11: 通过各种变换技术对不同行权价的VG欧式看涨期权溢价

| $K$ | Analytical | COS | FrFFT | FFT | SP |
| --- | --- | --- | --- | --- | --- |
| 10 | 90.0832 | 95.1859 | 90.0830 | 90.0983 | 90.0460 |
| 20 | 80.1660 | 80.8759 | 80.1660 | 80.1687 | 80.0835 |
| 30 | 70.2490 | 70.2490 | 70.2490 | 70.2388 | 70.1157 |
| 40 | 60.3320 | 60.3319 | 60.3319 | 60.3303 | 60.1560 |
| 50 | 50.4149 | 50.4149 | 50.4149 | 50.4010 | 50.2120 |
| 60 | 40.4979 | 40.4979 | 40.4979 | 40.4869 | 40.2881 |
| 70 | 30.5813 | 30.5813 | 30.5813 | 30.5969 | 30.3879 |
| 80 | 20.6702 | 20.6704 | 20.6704 | 20.6617 | 20.5189 |
| 90 | 10.8289 | 10.8289 | 10.8289 | 10.7983 | 10.7156 |
| 100 | 1.8150 | 1.8150 | 1.8151 | 1.7913 | 1.5406 |
| 110 | 0.0195 | 1.94e-02 | 1.95e-02 | 5.29e-02 | 2.26e-02 |
| 120 | 6.9339e-04 | 5.38e-04 | 5.83e-04 | 1.15e-02 | 6.57e-04 |
| 130 | 2.7159e-05 | -1.08e-06 | 2.56e-05 | -3.43e-03 | 2.85e-05 |
| 140 | 5.7237e-06 | -1.25e-04 | 1.89e-07 | -6.44e-03 | 1.63e-06 |
| 150 | 3.90e-08 | -3.71e-04 | -1.73e-06 | 2.86e-03 | 1.16e-07 |
| 160 | 2.14e-09 | -1.53e-03 | 1.45e-06 | 1.47e-03 | 1.00e-08 |
| 170 | 0.00e+00 | -5.19e-03 | 1.37e-06 | -2.84e-03 | 1.01e-09 |
| 180 | 0.00e+00 | -1.73e-02 | -3.27e-07 | 2.61e-03 | 1.16e-10 |
| 190 | 0.00e+00 | -5.47e-02 | 7.88e-07 | -2.05e-03 | 1.51e-11 |
| 200 | 0.00e+00 | -1.68e-01 | -7.31e-07 | 1.65e-03 | 2.19e-12 |

我们使用以下参数进行定价：现货价格 ${S}_{0} = 100$，无风险利率 $r = 10\%$，到期时间 $T = 1/12$，波动率 $\sigma = 0.12$，$\theta = -0.14$，以及 $\nu = 0.2$。

表 2.11 显示了使用解析解、FFT、FrFFT、COS和鞍点方法对行权价从10到200的期权定价结果。

##### 2.5.5.4 CGMY模型

CGMY模型定义为

$$
S_{t} = S\left( 0\right) \exp \left\lbrack \left( r - q + \omega \right) t + X_{CGMY}\left( t;C, G, M, Y \right) \right\rbrack \tag{2.130}
$$

其中 $X_{CGMY}\left( t;C, G, M, Y \right)$ 是CGMY过程，$\omega$ 定义为

$$
\omega = C \Gamma \left( -Y \right) \left\lbrack \left( M - 1 \right)^{Y} - M^{Y} + \left( G + 1 \right)^{Y} - G^{Y} \right\rbrack \tag{2.131}
$$

在该模型下，CGF及其前两个导数为：

$$
K_{0}\left( x\right) = x \left( \ln S_{0} + \left( r - q + w \right) T \right) + T C \Gamma \left( -Y \right) \left( \left( M - x \right)^{Y} - M^{Y} + \left( G + x \right)^{Y} - G^{Y} \right)
$$

$$
K_{0}'\left( x\right) = \ln S_{0} + \left( r - q + w \right) T + Y T C \Gamma \left( -Y \right) \left\lbrack -\left( M - x \right)^{Y - 1} + \left( G + x \right)^{Y - 1} \right\rbrack
$$

$$
K_{0}''\left( x\right) = Y \left( Y - 1 \right) T C \Gamma \left( -Y \right) \left\lbrack \left( M - x \right)^{Y - 2} + \left( G + x \right)^{Y - 2} \right\rbrack
$$

表 2.12: 通过各种变换技术对不同行权价的CGMY欧式看涨期权溢价

| $K$ | COS | FrFFT | FFT | SP |
| --- | --- | --- | --- | --- |
| 10 | 90.1550 | 90.1489 | 90.1489 | 90.1022 |
| 20 | 80.2889 | 80.8011 | 80.5694 | 80.2066 |
| 30 | 70.4568 | 70.0928 | 70.7195 | 70.3456 |
| 40 | 60.6829 | 59.7980 | 60.9336 | 60.5796 |
| 50 | 51.0318 | 49.9905 | 51.2981 | 50.9989 |
| 60 | 41.7592 | 40.7630 | 41.9856 | 41.7455 |
| 70 | 33.0236 | 32.2781 | 33.2416 | 33.0309 |
| 80 | 25.1175 | 24.7296 | 25.3514 | 25.1301 |
| 90 | 18.2872 | 18.2849 | 18.5797 | 18.3285 |
| 100 | 12.8258 | 13.0302 | 13.0968 | 12.8267 |
| 110 | 8.7340 | 8.9707 | 8.9274 | 8.65796 |
| 120 | 5.6257 | 5.95.9822 | 5.9417 | 5.68396 |
| 130 | 3.7307 | 3.8926 | 3.9118 | 3.66418 |
| 140 | 2.2610 | 2.4923 | 2.5827 | 2.34064 |
| 150 | 1.5694 | 1.5836 | 1.7335 | 1.49278 |
| 160 | 0.8697 | 1.0064 | 1.1967 | 0.95588 |
| 170 | 0.6637 | 0.6432 | 0.8582 | 0.616932 |
| 180 | 0.4176 | 0.4153 | 0.6437 | 0.402308 |
| 190 | 0.1733 | 0.2714 | 0.5068 | 0.265448 |
| 200 | 0.2730 | 0.1810 | 0.4183 | 0.177337 |

我们使用以下参数进行定价：现货价格 ${S}_{0} = 100$，无风险利率 $r = 3\%$，股息收益率 $q = 0$，到期时间 $T = 0.5$，$C = 2$，$G = 5$，$M = 10$，以及 $Y = 0.5$。

表 2.12 显示了使用COS、FrFFT、FFT和鞍点方法对行权价从10到200的期权定价结果。


---

### 2.6 通过傅里叶变换定价幂期权或杠杆期权

正如我们在引言中提到的，傅里叶方法的一个限制是它不仅限于定价欧式期权，即使对于欧式期权，随着收益函数的变化，傅里叶变换过程也需要重新推导。有些到期收益函数我们无法应用傅里叶变换技术来定价。

一种期权，其收益基于标的资产价格的幂。这允许期权的买方/持有者对特定标的资产或其波动率采取杠杆观点。欧式幂看涨期权具有以下到期收益：

$$
{\left( {X}_{T}^{p} - K\right) }^{ + } \tag{2.132}
$$

而幂看跌期权具有：

$$
{\left( K - {X}_{T}^{p}\right) }^{ + } \tag{2.133}
$$

其推导过程几乎与普通香草期权相同。

这里我们专注于看涨期权，并开始计算幂看涨期权的溢价，以资产价格对数的分布表示。

$$
{C}_{T}^{\left( p\right) }\left( K\right)  = \mathrm{C}\mathbb{E}\left( {\left( {X}_{T}^{p} - K\right) }^{ + }\right)= \mathrm{C}{\int }_{K}^{\infty }\left( {{X}_{T}^{p} - K}\right) {f}_{T}\left( X\right) d{X}_{T}= \mathrm{C}{\int }_{k}^{\infty }\left( {{e}^{px} - {e}^{k}}\right) {q}_{T}\left( x\right) {dx}
$$

我们定义使用阻尼因子的修改后的看涨期权溢价，如下：

$$
{c}_{T}^{\left( p\right) }\left( k\right)  = {e}^{\alpha k}{C}_{T}^{\left( p\right) }\left( k\right)
$$

我们计算修改后的期权溢价的特征函数，形成一个可以解析求解的内积分。

$$
{\Psi }_{T}^{\left( p\right) }\left( \nu \right)  = {\int }_{-\infty }^{\infty }{e}^{i\nu k}{c}_{T}^{\left( p\right) }\left( k\right) {dk}= {\int }_{-\infty }^{\infty }{e}^{i\nu k}\left( {\mathrm{C}{e}^{\alpha k}{\int }_{k}^{\infty }\left( {{S}^{p} - K}\right) f\left( S\right) {dS}}\right) {dk}
\\
= {\int }_{-\infty }^{\infty }{e}^{i\nu k}\left( {\mathrm{C}{e}^{\alpha k}{\int }_{k}^{\infty }\left( {{e}^{ps} - {e}^{k}}\right) q\left( s\right) {ds}}\right) {dk}= \mathrm{C}{\int }_{-\infty }^{\infty }{\int }_{-\infty }^{s}{e}^{\left( {\alpha  + {i\nu }}\right) k}\left( {{e}^{ps} - {e}^{k}}\right) q\left( s\right) {dkds}= \mathrm{C}{\int }_{-\infty }^{\infty }q\left( s\right) \left( {{\int }_{-\infty }^{s}{e}^{\left( {\alpha  + {i\nu }}\right) k}\left( {{e}^{ps} - {e}^{k}}\right) {dk}}\right) {ds}
$$

我们评估内积分，由于加入了阻尼因子，该积分收敛。

$$
{\int }_{-\infty }^{s}{e}^{\left( {\alpha  + {i\nu }}\right) k}\left( {{e}^{ps} - {e}^{k}}\right) {dk} = {\left. {e}^{ps}\frac{{e}^{\left( {\alpha  + {i\nu }}\right) k}}{\left( \alpha  + i\nu \right) }\right| }_{-\infty }^{s} - {\left. \frac{{e}^{\left( {\alpha  + {i\nu } + 1}\right) k}}{\left( \alpha  + i\nu  + 1\right) }\right| }_{-\infty }^{s}= \frac{{e}^{\left( {\alpha  + {i\nu } + p}\right) s}}{\alpha  + {i\nu }} - \frac{{e}^{\left( {\alpha  + {i\nu } + 1}\right) s}}{\alpha  + {i\nu } + 1}
$$

最终，我们可以解出期权溢价的特征函数，以标的资产价格对数的特征函数表示，得到

$$
{\Psi }_{T}^{\left( p\right) }\left( \nu \right)  = \mathrm{C}{\int }_{-\infty }^{\infty }\left( {\frac{{e}^{\left( {\alpha  + {i\nu } + p}\right) s}}{\alpha  + {i\nu }} - \frac{{e}^{\left( {\alpha  + {i\nu } + 1}\right) s}}{\alpha  + {i\nu } + 1}}\right) q\left( s\right) {ds}= \frac{\mathrm{C}}{\alpha  + {i\nu }}{\int }_{-\infty }^{\infty }{e}^{\left( {\alpha  + {i\nu } + p}\right) s}q\left( s\right) {ds} - \frac{\mathrm{C}}{\alpha  + {i\nu } + 1}{\int }_{-\infty }^{\infty }{e}^{\left( {\alpha  + {i\nu } + 1}\right) s}q\left( s\right) {ds}
\\
= \frac{\mathrm{C}}{\alpha  + {i\nu }}{\int }_{-\infty }^{\infty }{e}^{i\left( {\nu  - \left( {\alpha  + p}\right) i}\right) s}q\left( s\right) {ds} - \frac{\mathrm{C}}{\alpha  + {i\nu } + 1}{\int }_{-\infty }^{\infty }{e}^{i\left( {\nu  - \left( {\alpha  + 1}\right) i}\right) s}q\left( s\right) {ds}= \frac{\mathrm{C}}{\alpha  + {i\nu }}\Phi \left( {\nu  - \left( {\alpha  + p}\right) i}\right)  - \frac{\mathrm{C}}{\alpha  + {i\nu } + 1}\Phi \left( {\nu  - \left( {\alpha  + 1}\right) i}\right)
$$

因此，我们得到了修改后的期权溢价的傅里叶变换的最终表达式：

$$
{\Psi }_{T}^{\left( p\right) }\left( \nu \right)  = {\int }_{-\infty }^{\infty }{e}^{i\nu k}{c}_{T}^{\left( p\right) }\left( k\right) {dk}= \frac{\mathrm{C}}{\alpha  + {i\nu }}\Phi \left( {\nu  - \left( {\alpha  + p}\right) i}\right)  - \frac{\mathrm{C}}{\alpha  + {i\nu } + 1}\Phi \left( {\nu  - \left( {\alpha  + 1}\right) i}\right)
$$

$$

$$

再次，我们可以使用特征函数的公式和 ${\Psi }_{T}^{\left( p\right) }\left( \nu \right)$ 的逆傅里叶变换来计算 ${C}_{T}^{\left( p\right) }\left( k\right)$ ，即期权的溢价。

$$
{C}_{T}^{\left( p\right) }\left( k\right)  = \frac{{e}^{-{\alpha k}}}{2\pi }{\int }_{-\infty }^{\infty }{e}^{-{i\nu k}}{\Psi }_{T}^{\left( p\right) }\left( \nu \right) {d\nu } \tag{2.134}
$$

### 问题

1. 如果你对计算特定执行价格的欧式看涨/看跌期权的溢价感兴趣，你会使用快速傅里叶变换（FFT）还是分数快速傅里叶变换（FrFFT）？为什么？

2. 用于期权定价的快速傅里叶变换（FFT）程序提供了 $N$ 个溢价。FFT 的一个缺点是以下约束：

$$
{\lambda \eta } = \frac{2\pi }{N}
$$

其中 $\eta$ 是积分域中的步长，$\lambda$ 是对数执行价格域中的步长。解释这个约束对结果的准确性或可接受性的影响。

3. 在快速傅里叶变换（FFT）中，我们定义执行价格对数的范围为：

$$
{k}_{m} = \beta  + \left( {m - 1}\right) {\Delta k} = \beta  + \left( {m - 1}\right) \lambda ,\text{ for }m = 1,\ldots , N
$$

对于某些 $\beta$ 。$\beta$ 有许多选择。其中一个选择是设置 $\beta  = \ln {S}_{0} - \frac{\lambda N}{2}$ 。这个 $\beta$ 的选择会使平价执行价格落在我们执行价格范围的中间，其中 ${S}_{0}$ 是今天的现货价格。对于这个 $\beta$ 的选择，如果你对找到 $k = \log \left( K\right)$ 的溢价感兴趣，通常会进行插值。如果你对找到特定执行价格 ${k}_{0} = \log \left( {K}_{0}\right)$ 的溢价感兴趣，而不进行任何插值

(a) 你会选择什么样的 $\beta$？对应的索引号是什么？

(b) 你会选择什么样的 $\beta$ 使得第一个条目与 ${k}_{0}$ 的溢价相吻合？

(c) 你会选择什么样的 $\beta$ 使得最后一个条目与 ${k}_{0}$ 的溢价相吻合？

4. 证明模型的累积量 ${c}_{1},{c}_{2}$ 和 ${c}_{4}$ 为

(a) 黑-斯科尔斯模型

$$
{c}_{1} = \left( {r - q}\right) T
$$

$$
{c}_{2} = {\sigma }^{2}T
$$

$$
{c}_{4} = 0
$$

(b) 赫斯顿随机波动率模型

$$
{c}_{1} = {rT} + \left( {{1.0} - {e}^{-{\kappa T}}}\right) \frac{\theta  - {v}_{0}}{2\kappa } - {0.5\theta T}
$$

$$
{c}_{2} = \frac{1}{8{\kappa }^{3}}\left( {{\sigma T\kappa }{e}^{-{\kappa T}}\left( {{v}_{0} - \theta }\right) \left( {{8\kappa \rho } - {4\sigma }}\right) }\right)+ {\kappa \rho \sigma }\left( {1 - {e}^{-{\kappa T}}\left( {{16\theta } - 8{v}_{0}}\right) }\right)
\\
+ {2\theta \kappa T}\left( {-{4\kappa \rho \sigma } + {\sigma }^{2} + 4{\kappa }^{2}}\right)+ {\sigma }^{2}\left( {\left( {\theta  - 2{v}_{0}}\right) {e}^{-{2\kappa T}} + \theta \left( {6{e}^{-{\kappa T}} - 7}\right)  + 2{v}_{0}}\right)+ 8{\kappa }^{2}\left( {{v}_{0} - \theta }\right) \left( {{1.0} - {e}^{-{\kappa T}}}\right)
$$

(c) 方差伽玛模型

$$
{c}_{1} = \left( {r + \theta }\right) T
$$

$$
{c}_{2} = \left( {{\sigma }^{2} + v{\theta }^{2}}\right) T
$$

$$
{c}_{4} = 3\left( {{\sigma }^{4}v + 2{\theta }^{4}{v}^{3} + 4{\sigma }^{2}{\theta }^{2}{v}^{2}}\right) T
$$

(d) CGMY 模型

$$
{c}_{1} = \left( {r + \omega }\right) T + {TC\Gamma }\left( {1 - Y}\right) \left( {-{M}^{Y - 1} + {G}^{Y - 1}}\right)
$$

$$
{c}_{2} = \alpha  + {CT\Gamma }\left( {2 - Y}\right) \left( {{M}^{Y - 2} + {G}^{Y - 2}}\right)
$$

$$
{c}_{4} = {CT\Gamma }\left( {4 - Y}\right) \left( {{M}^{Y - 4} + {G}^{Y - 4}}\right)
$$

其中

$$
\omega  =  - {C\Gamma }\left( {-Y}\right) \left( {\left( M - 1\right) }^{Y}\right)  + {\left( G + 1\right) }^{Y} - {M}^{Y} - {G}^{Y}
$$

$$
\alpha  = \frac{8C}{{\left( G + M\right) }^{2} - {\left( G - M\right) }^{2}}
$$

5. 在我们使用的 COS 方法中，积分范围 $\left\lbrack  {a, b}\right\rbrack$ 的公式为

$$
\left\lbrack  {a, b}\right\rbrack   = \left\lbrack  {{c}_{1} - L\sqrt{{c}_{2} + \sqrt{{c}_{4}}},{c}_{1} + L\sqrt{{c}_{2} + \sqrt{{c}_{4}}}}\right\rbrack  \;\text{ with }\;L = {10} \tag{2.135}
$$

其中 ${c}_{n}$ 表示 $\ln \left( {{X}_{T}/K}\right)$ 的第 $n$ 个累积量。检查表 2.5、2.6 和 2.7 中结果对 $a$ 和 $b$ 选择的敏感性，并比较结果得出结论。

6. 假设我们有一个模型下的风险中性测度下的股票价格对数的累积量生成函数 ${K}_{0}\left( x\right)$ 。证明股票价格对数在份额测度下减去一个指数的累积量生成函数为

$$
K\left( x\right)  = {K}_{0}\left( {x + 1}\right)  - {K}_{0}\left( 1\right)  - \ln \left( {1 + x}\right)
$$

7. 下面的推导是我们通过 FFT 定价欧式看涨期权的一部分：

$$
{\int }_{-\infty }^{\infty }{e}^{\left( {\alpha  + {i\nu }}\right) k}\left( {{e}^{-{rT}}{\int }_{k}^{\infty }\left( {{e}^{s} - {e}^{k}}\right) q\left( s\right) {ds}}\right) {dk}
\\
= {e}^{-{rT}}{\int }_{-\infty }^{\infty }{\int }_{-\infty }^{s}{e}^{\left( {\alpha  + {i\nu }}\right) k}\left( {{e}^{s} - {e}^{k}}\right) q\left( s\right) {dkds}= {e}^{-{rT}}{\int }_{-\infty }^{\infty }q\left( s\right) \left( {{\int }_{-\infty }^{s}{e}^{\left( {\alpha  + {i\nu }}\right) k}\left( {{e}^{s} - {e}^{k}}\right) {dk}}\right) {ds} \tag{2.136}
$$

方框中的项可以很容易地解析求解。求解后并代入公式 (2.136) 中，我们得到

$$
{e}^{-{rT}}{\int }_{-\infty }^{\infty }q\left( s\right) \left( {{\int }_{-\infty }^{s}{e}^{\left( {\alpha  + {i\nu }}\right) k}\left( {{e}^{s} - {e}^{k}}\right) {dk}}\right) {ds} = \frac{{e}^{-{rT}}}{\left( {\alpha  + {i\nu }}\right) \left( {\alpha  + {i\nu } + 1}\right) }\Phi \left( {\nu  - \left( {\alpha  + 1}\right) i}\right)
$$

其中 $\Phi \left( u\right)$ 表示 $S$ 的对数过程的特征函数，即

$$
\Phi \left( u\right)  = \mathbb{E}\left( {e}^{ius}q\left( s\right) {ds}\right)
$$

上述推导是针对 $s = \ln S$ 和 $k = \ln K$ 进行的。对于 $S$ 和 $K$ 重复上述推导，即

$$
{\int }_{-\infty }^{\infty }{e}^{\left( {\alpha  + {i\nu }}\right) K}\left( {{e}^{-{rT}}{\int }_{K}^{\infty }\left( {S - K}\right) f\left( S\right) {dS}}\right) {dK}
$$

在这个情况下，$S$ 和 $K$ 都是实数（这意味着它们可以是负数）。将你的最终结果表示为

$$
\phi \left( u\right)  = {\int }_{-\infty }^{\infty }{e}^{iuS}f\left( S\right) {dS}
$$

的形式，其中 $\phi \left( u\right)$ 是 $S$ 的特征函数。

8. 数字期权或二元期权是具有以下到期收益的期权：数字看涨期权

$$
{\mathbb{1}}_{{\left( {S}_{T} - K\right) }^{ + }},
$$

数字看跌期权

$$
{\mathbb{1}}_{{\left( K - {S}_{T}\right) }^{ + }}
$$

我们能否使用标的资产的特征函数和傅里叶变换技术来定价数字期权？如果可以，推导它。如果不可以，解释为什么不可以。

案例研究

1. 考虑以下八个模型/过程：

(a) 几何布朗运动（GBM）：在 Black-Merton-Scholes 框架下，股票价格对数的特征函数由下式给出

$$
\mathbb{E}\left( {e}^{{iu}\ln {S}_{t}}\right)  = \mathbb{E}\left( {e}^{{iu}{s}_{t}}\right)= \exp \left( {i\left( {{s}_{0} + \left( {r - q - {\sigma }^{2}/2}\right) t}\right) u - \frac{1}{2}{\sigma }^{2}{u}^{2}t}\right)
$$

在整个案例研究中，假设 $\sigma  = {40}\%$ 。

(b) 赫斯顿随机波动率模型：股票价格遵循以下过程：

$$
d{S}_{t} = r{S}_{t}{dt} + \sqrt{{v}_{t}}{S}_{t}d{W}_{t}^{\left( 1\right) },
$$

$$
d{v}_{t} = \kappa \left( {\theta  - {v}_{t}}\right) {dt} + \sigma \sqrt{{v}_{t}}d{W}_{t}^{\left( 2\right) },
$$

其中两个布朗运动分量 ${W}_{t}^{\left( 1\right) }$ 和 ${W}_{t}^{\left( 2\right) }$ 以速率 $\rho$ 相关。参数 $\kappa ,\theta$ 和 $\sigma$ 具有特定的物理意义：$\kappa$ 是均值回归速度，$\theta$ 是长期方差，$\sigma$ 是波动率的波动率。股票价格对数过程的特征函数由下式给出

$$
\Phi \left( u\right)  = \mathbb{E}\left( {e}^{{iu}\ln {S}_{t}}\right)= \frac{\exp \left\{  {\frac{{\kappa \theta t}\left( {\kappa  - {i\rho \sigma u}}\right) }{{\sigma }^{2}} + {iutr} + {iu}\ln {S}_{0}}\right\}  }{{\left( \cosh \frac{\gamma t}{2} + \frac{\kappa  - {i\rho \sigma u}}{\gamma }\sinh \frac{\gamma t}{2}\right) }^{\frac{2\kappa \theta }{{\sigma }^{2}}}}\exp \left\{  {-\frac{\left( {{u}^{2} + {iu}}\right) {v}_{0}}{\gamma \coth \frac{\gamma t}{2} + \kappa  - {i\rho \sigma u}}}\right\}  ,
$$

其中 $\gamma  = \sqrt{{\sigma }^{2}\left( {{u}^{2} + {iu}}\right)  + {\left( \kappa  - i\rho \sigma u\right) }^{2}}$ ，${S}_{0}$ 和 ${v}_{0}$ 分别是价格过程和波动率过程的初始值。在整个案例研究中，假设波动率的波动率 $\sigma  = {40}\% ;\kappa  = 1;\theta  = {0.08};\rho  =  - {0.8}$ ; ${v}_{0} = {0.05}$ 。

(c) 方差伽玛模型：设 $b\left( {t;\theta ,\sigma }\right)  \equiv  {\theta t} + {\sigma W}\left( t\right)$ 是具有恒定漂移率 $\theta$ 和波动率 $\sigma$ 的布朗运动，其中 $W\left( t\right)$ 是标准布朗运动。记 $\gamma \left( {t;\nu }\right)$ 为在长度为 $h$ 的非重叠区间内具有独立伽玛增量的伽玛过程，其均值为 $h$ ，方差为 ${\nu h}$ 。三参数 ${VG}$ 过程 $X\left( {t;\sigma ,\theta ,\nu }\right)$ 定义为

$$
X\left( {t;\sigma ,\theta ,\nu }\right)  = b\left( {\gamma \left( {t;\nu }\right) ,\theta ,\sigma }\right) .
$$

我们看到过程 $X\left( t\right)$ 是在伽玛时间变化下评估的具有漂移的布朗运动。时间 $t$ 的 VG 过程的特征函数为

$$
{\phi }_{X\left( t\right) }\left( u\right)  = \mathbb{E}\left( {e}^{{iuX}\left( t\right) }\right)  = {\left( \frac{1}{1 - {iu\theta \nu } + {\sigma }^{2}{u}^{2}\nu /2}\right) }^{\frac{t}{\nu }}. \tag{2.137}
$$

VG 模型下的股票价格动态与几何布朗运动模型下的股票价格动态相似，后者在一个具有连续股息收益率 $q$ 和恒定连续复利利率 $r$ 的经济中支付股息。股票价格的风险中性漂移率为 $r - q$ ，前向股票价格被建模为 VG 过程的指数，归一化为期望值。设 $S\left( t\right)$ 为时间 $t$ 的股票价格。股票价格的 VG 风险中性过程由下式给出

$$
S\left( t\right)  = S\left( 0\right) {e}^{\left( {r - q}\right) t + X\left( t\right)  + {\omega t}}, \tag{2.138}
$$

其中归一化因子 ${e}^{\omega t}$ 确保 ${\mathbb{E}}_{0}\left\lbrack  {S\left( t\right) }\right\rbrack   = S\left( 0\right) {e}^{\left( {r - q}\right) t}$ 。从特征函数在 $- i$ 处的评估结果可以得出

$$
\omega  = \frac{1}{\nu }\ln \left( {1 - {\sigma }^{2}\nu /2 - {\theta \nu }}\right) .
$$

根据风险中性的定义，具有执行价格 $K$ 和到期时间 $T$ 的欧式看跌期权的价格为

$$
p\left( {S\left( 0\right) ;K, t}\right)  = {e}^{-{rT}}{\mathbb{E}}_{0}\left( {\left( K - S\left( T\right) \right) }^{ + }\right) .
$$

在整个案例研究中，假设 $\sigma  = {30}\% ,\nu  = {0.50},\theta  =  - {0.35}$ 。

(d) Carr-Geman-Madan-Yor (CGMY) 过程：参数为 $C, G, M$ 和 $Y$ 的 CGMY 过程的特征函数由下式给出

$$
\mathbb{E}\left\lbrack  {e}^{{iu}{X}_{t}}\right\rbrack   = {e}^{{Ct\Gamma }\left( {-Y}\right) \left( {{\left( M - iu\right) }^{Y} - {M}^{Y} + {\left( G + iu\right) }^{Y} - {G}^{Y}}\right) }
$$

股票价格的 CGMY 风险中性过程由下式给出

$$
S\left( t\right)  = S\left( 0\right) {e}^{\left( {r - q}\right) t + X\left( t\right)  + {\omega t}}, \tag{2.139}
$$

其中归一化因子 ${e}^{\omega t}$ 确保 ${\mathbb{E}}_{0}\left\lbrack  {S\left( t\right) }\right\rbrack   = S\left( 0\right) {e}^{\left( {r - q}\right) t}$ 。从特征函数在 $- i$ 处的评估结果可以得出

$$
\omega  =  - {C\Gamma }\left( {-Y}\right) \left\{  {{\left( M - 1\right) }^{Y} - {M}^{Y} + {\left( G + 1\right) }^{Y} - {G}^{Y}}\right\}  .
$$

在整个案例研究中，假设 $C = 1, G = 7, M = 9$ 和 $Y = {0.5}\& {0.99}$ 。

(e) 方差伽玛随机到达 (VGSA) 过程：如第 1.4.9 节所述，为了获得 VGSA，我们取一个齐次 Lévy 过程的 VG 过程，并通过评估一个 Cox, Ingersoll 和 Ross (CIR) 过程的积分来引入随机波动率。CIR 过程的均值回归引入了通常称为波动率持续性的聚集现象。这使我们能够同时校准跨越执行价格和到期时间的市场价格曲面。该过程在特征函数的解析表达式中是可处理的。形式上，我们定义 CIR 过程 $y\left( t\right)$ 为随机微分方程的解

$$
d{y}_{t} = \kappa \left( {\eta  - {y}_{t}}\right) {dt} + \lambda \sqrt{{y}_{t}}d{W}_{t}
$$

其中 $W\left( t\right)$ 是布朗运动，$\eta$ 是时间变化的长期速率，$\kappa$ 是均值回归速率，$\lambda$ 是时间变化的波动率。过程 $y\left( t\right)$ 是瞬时时间变化率，因此时间变化由 $Y\left( t\right)$ 给出，其中

$$
Y\left( t\right)  = {\int }_{0}^{t}y\left( u\right) {du}
$$

市场变量对数的 SDE 与上述时间变化下的 VG 过程相同。时间变化 $Y\left( t\right)$ 的特征函数由下式给出

$$
\mathbb{E}\left( {e}^{{iuY}\left( t\right) }\right)  = \phi \left( {u, t, y\left( 0\right) ;\kappa ,\eta ,\lambda }\right)= A\left( {t, u}\right) {e}^{B\left( {t, u}\right) y\left( 0\right) }  \tag{2.140}
$$

其中

$$
A\left( {t, u}\right)  = \frac{\exp \left( \frac{{\kappa }^{2}{\eta t}}{{\lambda }^{2}}\right) }{{\left( \cosh \left( \gamma t/2\right)  + \frac{\kappa }{\gamma }\sinh \left( \gamma t/2\right) \right) }^{{2\kappa \eta }/{\lambda }^{2}}}
$$

$$
B\left( {t, u}\right)  = \frac{2iu}{\kappa  + \gamma \coth \left( {{\gamma t}/2}\right) }
$$

其中

$$
\gamma  = \sqrt{{\kappa }^{2} - 2{\lambda }^{2}{iu}}
$$

随机波动率 Lévy 过程，称为 VGSA 过程，定义为

$$
{Z}_{VGSA}\left( t\right)  = {X}_{VG}\left( {Y\left( t\right) ;\sigma ,\nu ,\theta }\right)
$$

其中 $\sigma ,\nu ,\theta ,\kappa ,\eta$ 和 $\lambda$ 是定义该过程的六个参数。其特征函数由下式给出

$$
\mathbb{E}\left( {e}^{{iu}{Z}_{VGSA}\left( t\right) }\right)  = \phi \left( {-i{\psi }_{VG}\left( {u;\sigma ,\nu ,\theta }\right) , t,\frac{1}{\nu };\kappa ,\eta ,\lambda }\right)
$$

其中 ${\Psi }_{VG}$ 是单位时间的方差伽玛过程的对数特征函数，即

$$
{\psi }_{VG}\left( {u;\sigma ,\nu ,\theta }\right)  =  - \frac{1}{\nu }\log \left( {1 - {iu\theta \nu } + {\sigma }^{2}\nu {u}^{2}/2}\right)
$$

我们定义时间 $t$ 的资产价格过程如下：

$$
S\left( t\right)  = S\left( 0\right) \frac{{e}^{\left( {r - q}\right) t + Z\left( t\right) }}{\mathbb{E}\left\lbrack  {e}^{Z\left( t\right) }\right\rbrack  }
$$

我们注意到

$$
\mathbb{E}\left\lbrack  {e}^{Z\left( t\right) }\right\rbrack   = \phi \left( {-i{\psi }_{VG}\left( {-i;\sigma ,\nu ,\theta }\right) , t,\frac{1}{\nu };\kappa ,\eta ,\lambda }\right)
$$

因此，时间 $t$ 的资产价格对数的特征函数由下式给出

$$
\Phi \left( u\right)  = \mathbb{E}\left( {e}^{{iu}\ln {S}_{t}}\right)= \exp \left( {{iu}\left( {\log {S}_{0} + \left( {r - q}\right) t}\right) }\right)  \times  \frac{\phi \left( {-i{\psi }_{VG}\left( {u;\sigma ,\nu ,\theta }\right) , t,\frac{1}{\nu };\kappa ,\eta ,\lambda }\right) }{\phi {\left( -i{\psi }_{VG}\left( -i;\sigma ,\nu ,\theta \right) , t,\frac{1}{\nu };\kappa ,\eta ,\lambda \right) }^{iu}}
$$

其中 $\phi \left( {u, t, y;\kappa ,\eta ,\lambda }\right)$ 由公式 2.140 提供。在整个案例研究中，假设 $\sigma  = {0.15},\nu  = {0.18},\theta  =  - {0.08},\kappa  = 8,\eta  = {2.5}$ 和 $\lambda  = {10.0}$ 。

(f) 正态逆高斯随机到达 (NIGSA)：根据第 1.4.9 节的论证，可以证明时间 $t$ 的 NIGSA 过程的特征函数显式给出为

$$
\Phi \left( u\right)  = \mathbb{E}\left( {e}^{{iu}\ln {S}_{t}}\right)= \exp \left( {{iu}\left( {\log {S}_{0} + \left( {r - q}\right) t}\right) }\right)  \times  \frac{\phi \left( {-i{\psi }_{NIG}\left( {u;1,\nu ,\theta }\right) , t,\sigma ;\kappa ,\eta ,\lambda }\right) }{\phi {\left( -i{\psi }_{NIG}\left( -i;1,\nu ,\theta \right) , t,\sigma ;\kappa ,\eta ,\lambda \right) }^{iu}}
$$

其中 ${\psi }_{NIG}\left( {u;\sigma ,\nu ,\theta }\right)$ 是以时间变化布朗运动的参数表示的单位时间对数特征函数，由下式给出

$$
{\psi }_{NIG}\left( {u;\sigma ,\nu ,\theta }\right)  = \sigma \left( {\frac{\nu }{\theta } - \sqrt{\frac{{\nu }^{2}}{{\theta }^{2}} - 2\frac{\theta iu}{{\sigma }^{2}} + {u}^{2}}}\right)
$$

而 $\phi \left( {u, t, y;\kappa ,\eta ,\lambda }\right)$ 由公式 2.140 提供。在整个案例研究中，假设 $\sigma  = {0.15},\nu  = {0.18},\theta  =  - {0.08},\kappa  = 8,\eta  = {2.5}$ 和 $\lambda  = {10.0}$ 。

(g) CGMY 随机到达 (CGMYSA)：为了获得 CGMYSA 下的股票对数的特征函数，我们遵循第 1.4.9 节的论证。可以证明时间 $t$ 的 CGMYSA 过程的特征函数显式给出为

$$
\Phi \left( u\right)  = \mathbb{E}\left( {e}^{{iu}\ln {S}_{t}}\right)= \exp \left( {{iu}\left( {\log {S}_{0} + \left( {r - q}\right) t}\right) }\right)  \times  \frac{\phi \left( {-i{\psi }_{CGMY}\left( {u;1, G, M, Y}\right) , t, C;\kappa ,\eta ,\lambda }\right) }{\phi {\left( -i{\psi }_{CGMY}\left( -i;1, G, M, Y\right) , t, C;\kappa ,\eta ,\lambda \right) }^{iu}}
$$

其中 ${\psi }_{CGMY}\left( {u;C, G, M, Y}\right)$ 是以参数表示的单位时间对数特征函数，由下式给出

$$
{\psi }_{CGMY}\left( {u;C, G, M, Y}\right)  = {C\Gamma }\left( {-Y}\right) \left( {{\left( M - iu\right) }^{Y} - {M}^{Y} + {\left( G + iu\right) }^{Y} - {G}^{Y}}\right)
$$

而 $\phi \left( {u, t, y;\kappa ,\eta ,\lambda }\right)$ 由公式 2.140 提供。在整个案例研究中，假设 $\sigma  = {0.15},\nu  = {0.18},\theta  =  - {0.08},\kappa  = 8,\eta  = {2.5}$ 和 $\lambda  = {10.0}$ 。

(h) 方差伽玛缩放自分解 (VGSSD)：VGSSD 下的股票对数的特征函数由下式给出

$$
\Phi \left( u\right)  = \mathbb{E}\left( {e}^{{iu}\ln {S}_{t}}\right)= \exp ( {iu}( \ln {S}_{0} + ( r - q) t ))  \times\frac{\phi_{X(t) }(u) }{\phi_{ X(t) }( -i) }
$$

其中 ${\phi }_{X\left( t\right) }\left( u\right)$ 由下式给出
$$
{\phi }_{X\left( t\right) }\left( u\right)  = {\phi }_{{VG}\left( 1\right) }\left( {u{t}^{\gamma }}\right)= {\left( 1 - iu{t}^{\gamma }\nu \theta  + \frac{1}{2}{u}^{2}{t}^{2\gamma }\nu {\sigma }^{2}\right) }^{-1/\nu }
$$

在整个案例研究中，假设 $\sigma  = {0.15},\nu  = {0.18},\theta  =  - {0.08},\kappa  = 8,\eta  = {2.5}$ 和 $\lambda  = {10.0}$ 。

对于以下市场/合约参数：现货价格 ${S}_{0} = \$ {100}$ ，到期时间 $T =$ 0.5 年，无风险利率 $r = {0.5}\%$ ，连续股息率 $q = {1.00}\%$ ，以及执行价格范围 $K = {30},{50},{70},{90},{100},{110},{130},{150},{170}$ ，通过以下技术为所有模型定价欧式看涨期权：

(a) 快速傅里叶变换（FFT）：考虑阻尼因子 $\alpha$ 的不同值，以及 $N = {2}^{n}$ 的不同值。

(b) 分数快速傅里叶变换（FrFFT）：考虑阻尼因子 $\alpha$ 的不同值，以及 $N = {2}^{n}$ 的不同值。

(c) 傅里叶余弦（COS）方法：考虑区间 $\left\lbrack  \begin{array}{ll} a & b \end{array}\right\rbrack$ 的不同值，并找到结果对 $\left\lbrack  \begin{array}{ll} a & b \end{array}\right\rbrack$ 选择的敏感性。

(d) 鞍点方法

比较并得出结论。
