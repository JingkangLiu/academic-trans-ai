import anthropic
import time
import random
from pathlib import Path
import os

# Token费用计算参考值（美元/1K tokens）
INPUT_COST_PER_1K = 0.003  # $3 per million = $0.003 per 1K
OUTPUT_COST_PER_1K = 0.015  # $15 per million = $0.015 per 1K

# 初始化文件夹路径
WORK_DIR = Path("workmd")
OUTPUT_DIR = Path("outputmd")

# 确保输出目录存在
OUTPUT_DIR.mkdir(exist_ok=True)

# 客户端初始化
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_KEY")
)


class TokenCounter:
    def __init__(self):
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.call_count = 0
        self.file_count = 0

    def add_usage(self, input_tokens, output_tokens):
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        self.call_count += 1

    def add_file(self):
        self.file_count += 1

    def print_summary(self):
        input_cost = (self.total_input_tokens / 1000) * INPUT_COST_PER_1K
        output_cost = (self.total_output_tokens / 1000) * OUTPUT_COST_PER_1K
        total_cost = input_cost + output_cost

        print("\n=== Token 使用统计 ===")
        print(f"处理文件数: {self.file_count}")
        print(f"API调用次数: {self.call_count}")
        print(f"总输入tokens: {self.total_input_tokens:,}")
        print(f"总输出tokens: {self.total_output_tokens:,}")
        print(f"总tokens: {self.total_input_tokens + self.total_output_tokens:,}")
        print("\n=== 成本统计（美元）===")
        print(f"输入成本: ${input_cost:.4f}")
        print(f"输出成本: ${output_cost:.4f}")
        print(f"总成本: ${total_cost:.4f}")
        print(f"使用prompt caching节省成本: ${total_cost * 0.9:.4f}")
        print(f"平均每个文件成本: ${total_cost / self.file_count:.4f}")


def get_translation_prompt():
    """定义固定的翻译提示模板"""
    return """你是一个专门从事将学术的markdown文本翻译成学术中文的AI助手并且精通数学。
    最重要的要求：将全部文本翻译完后，再生成提示"本次翻译任务完成"，一定确保全部翻译完后再回复，绝对不要提前回复。
    重要的基本要求:
    1. 对于markdown文档的处理，保持markdown内联latex的格式，公式块使用双美元符$$ $$，双美元符公式块需要单独成行，行内公式使用单美元符$ $。正文使用中文全角标点符号，数学文本中使用英文半角标点符号。
    3. 你不会生成任何除了翻译内容以外的其他文本，由于我一次给你的文本很长，你可能不能通过一次回答完整，不用担心，你的单次回答被截断后，我会提示你继续。
    2. 图片的插入代码保持不变，但将文本中HTML格式的表格转换为markdown内联表格的形式，并且保持表格中的内容不变。
    翻译的细节要求:
    1. 英文的长句翻译通常不会直接对应中文句式，你需要作出逻辑叙述的调整。
    3. 为照顾汉语的习惯，采用一词两译的做法。例如"set"在汉语中有时译成"集合"有时译成"集"，单独使用时常译成"集合"，而在与其他词汇连用时则译成"集"（如可数集等）。
    4. 汉语"是"通常有两种含义，一是"等于"，二是"属于"。在本书中"是"只表示等于的意思，而属于的意思则用"是一个"来表示。例如，不说"X是拓扑空间"，而说"X是一个拓扑空间"。
    5. 在汉语中，长的词组常容易发生歧义。例如"一个可数邻域的族"可能会有以下几种理解方式：
       (1) 一个族，这个族的成员是邻域，每一个邻域是可数集。
       (2) 一个族，这个族只有一个邻域为其成员，这个邻域是可数集。
       (3) 一个族，这个族是可数的，它的每一个成员是邻域。对于不满足结合律的翻译对象是不能省掉括号的。
       遇到这种情形，你需要宁可多用几个字翻译，也尽量避免歧义的可能。
    6. 在汉语中常难于区别单数和复数，而在英语的表达中又常常对于名词的复数形式与集合名词不加区别。对于这种情形，简单地翻译可能会导致误解。因此，你需要宁可啰嗦一点，以保证不被误解。

    参考术语表：
- (余)切向量丛 | (Co)-Tangent vector bundle
- 2维球面 | 2-Sphere
- 阿贝尔联络 | Abelian connection
- 阿贝尔李代数 | Abelian Lie algebra
- 阿贝尔LV模型 | Abelian LV model
- 适应过程 | Adapted process
- 近似马尔可夫Libor市场模型 | Almost Markov Libor Market Model
- 几乎必然（a.s） | Almost surely (a.s)
- 美式期权 | American option
- CEV模型的解析看涨期权 | Analytical call option for the CEV model
- 湮灭-创造代数 | Annihilation-creation algebra
- 反极 | Antipode
- 套利 | Arbitrage
- 亚式期权 | Asian option
- 资产 | Asset
- 可实现收益 | Attainable payoff
- 巴舍利耶模型 | Bachelier model
- 障碍期权 | Barrier option
- 篮子隐含波动率 | Basket implied volatility
- 篮子期权 | Basket option
- Benaim-Friz定理 | Benaim-Friz theorem
- 百慕大期权 | Bermudan option
- 布莱克-斯科尔斯偏微分方程 | Black-Scholes PDE
- 债券 | Bond
- 博雷尔$\sigma$代数 | Borel $\sigma$ -algebra
- 有界线性算子 | Bounded Linear operator
- 盈亏平衡波动率 | Break-even volatility
- 布朗滤子 | Brownian filtration
- 布朗片 | Brownian sheet
- 卡梅伦-马丁空间 | Cameron-Martin space
- 上限期权 | Caplet
- 卡拉泰奥多里定理 | Carathéodory theorem
- 卡尔坦-阿达马流形 | Cartan-Hadamard manifold
- 图表 | Chart
- 陈级数 | Chen series
- 乔列斯基分解 | Cholesky decomposition
- 克里斯托弗符号 | Christoffel symbol
- 固定收益期权 | Cliquet option
- 可闭算子 | Closable operator
- 余循环条件 | Co-cycle condition
- 余乘积 | Co-product
- 同到期权 | Co-terminal swaption
- 余单位 | Co-unit
- 商品担保债务 | Collaterized Commodity Obligation
- 债务担保证券 | Collaterized Debt Obligation
- 完备市场 | Complete market
- 完备概率空间 | Complete probability space
- 条件期望 | Conditional expectation
- 合流超几何势 | Confluent hypergeometric potential
- 联络 | Connection
- 常弹性方差模型(CEV) | Constant Elasticity of Variance (CEV)
- 控制距离 | Control distance
- 凸性调整 | Convexity adjustment
- 相关矩阵 | Correlation matrix
- 相关性微笑 | Correlation smile
- 走廊方差互换 | Corridor variance swap
- 余切空间 | Cotangent space
- 协变导数 | Covariant derivative
- 累积正态分布 | Cumulative normal distribution
- 曲率 | Curvature
- 割迹 | Cut-locus
- 截断函数 | Cut-off function
- 循环向量 | Cyclic vector
- 柱状函数 | Cylindrical function
- DeWitt-Gilkey-Pleijel-Minakshisundaram展开 | DeWitt-Gilkey-Pleijel-Minakshisundaram
- 亏格指标 | Deficiency indices
- Delta值 | Delta
- Delta对冲 | Delta hedging
- 密度丛 | Density bundle
- 导子 | Derivation
- 扩散过程 | Diffusion
- 贴现因子 | Discount factor
- 线性算子定义域 | Domain of a linear operator
- 向下敲出看涨期权 | Down-and-out call option
- 漂移项 | Drift
- 杜皮尔局部波动率 | Dupire local volatility
- 有效向量场 | Effective vector field
- 爱因斯坦求和约定 | Einstein summation convention
- 弹性参数 | Elasticity parameter
- 股票混合模型 | Equity hybrid model
- 等价局部鞅测度 | Equivalent local martingale
- 等价测度 | Equivalent measure
- 欧氏薛定谔方程 | Euclidean Schrödinger equation
- 欧拉格式 | Euler scheme
- 欧式看涨期权 | European call option
- 欧式看跌期权 | European put option
- CEV模型的精确条件概率 | Exact conditional probability for the CEV model
- 期望 | Expectation
- 指数映射 | Exponential map
- 外微分$d$ | Exterior derivative $d$
- 费勒边界分类 | Feller boundary classification
- 费勒非爆炸检验 | Feller non-explosion test
- 费曼路径积分 | Feynman path integral
- 费曼-卡克公式 | Feynman-Kac
- 纤维 | Fiber
- 滤子 | Filtration
- 随机波动率模型隐含波动率一阶渐近 | First-order asymptotics of implied volatility for SVMs
- 流 | Flow
- 福克空间 | Fock space
- 福克-普朗克方程 | Fokker-Planck
- 远期 | Forward
- 远期隐含波动率 | Forward implied volatility
- 前向柯尔莫戈洛夫方程 | Forward Kolmogorov
- 远期测度 | Forward measure
- 远期开始期权 | Forward-start option
- 自由李代数 | Free Lie algebra
- 冻结论证 | Freezing argument
- 弗洛贝尼乌斯定理 | Frobenius theorem
- 泛函导数 | Functional derivative
- 泛函积分 | Functional integration
- 泛函空间${\mathbb{D}}_{1,2}$ | Functional space ${\mathbb{D}}_{1,2}$
- 资产定价基本定理 | Fundamental theorem of Asset pricing
- 规范变换 | Gauge transformation
- 高斯超几何势 | Gauss hypergeometric potential
- 高斯界 | Gaussian bounds
- 高斯估计 | Gaussian estimates
- 广义方差互换 | Generalized Variance swap
- 测地线曲线 | Geodesic curve
- ${\mathbb{H}}^{n}$上的测地线距离 | Geodesic distance on ${\mathbb{H}}^{n}$
- 测地线方程 | Geodesic equation
- 测地线 | Geodesics
- 几何布朗运动 | Geometric Brownian
- 吉尔萨诺夫定理 | Girsanov
- 群类元素 | Grouplike element
- 杰永定理 | Gyöngy theorem
- 赫尔曼德形式 | Hörmander form
- 赫尔曼德定理 | Hörmander's theorem
- 哈密顿-雅可比-贝尔曼方程 | Hamilton-Jacobi-Bellman equation
- 哈斯明斯基非爆炸检验 | Hasminskii non-explosion test
- 热核 | Heat kernel
- 热核系数 | Heat kernel coefficients
- ${\mathbb{H}}^{2}$上的热核 | Heat kernel on ${\mathbb{H}}^{2}$
- ${\mathbb{H}}^{3}$上的热核 | Heat kernel on ${\mathbb{H}}^{3}$
- 海森堡群上的热核 | Heat kernel on Heisenberg group
- 热核半群 | Heat kernel semigroup
- 对冲策略 | Hedging strategy
- 海森堡李代数 | Heisenberg Lie algebra
- 埃尔米特多项式 | Hermite polynomials
- 赫斯顿模型 | Heston model
- 赫斯顿解 | Heston solution
- 希尔伯特空间 | Hilbert space
- HJM模型 | HJM model
- 何-李模型 | Ho-Lee model
- 霍普夫代数 | Hopf algebra
- 赫尔-怀特双因子模型 | Hull-White 2-factor model
- 赫尔-怀特分解 | Hull-White decomposition
- 混合期权 | Hybrid option
- 双曲流形${\mathbb{H}}^{n}$ | Hyperbolic manifold ${\mathbb{H}}^{n}$
- 双曲庞加莱平面 | Hyperbolic Poincaré plane
- 双曲面 | Hyperbolic surface
- 亚椭圆 | hypo-elliptic
- 隐含波动率 | Implied volatility
- 不完备市场 | Incomplete market
- 单射半径 | Injectivity radius
- 等温坐标 | Isothermal coordinates
- 伊藤等距 | Itô isometry
- 伊藤引理 | Itô lemma
- 伊藤过程 | Itô process
- 伊藤-田中公式 | Itô-Tanaka
- 延森不等式 | Jensen inequality
- 加藤类 | Kato class
- 杀死向量 | Killing vector
- 国田定理 | Kunita theorem
- 莱维面积公式 | Lévy area formula
- 拉普拉斯方法 | Laplace method
- 拉普拉斯-贝尔特拉米算子 | Laplace-Beltrami
- 拉普拉斯热核 | Laplacian heat kernel
- 大型交易者 | Large traders
- LCEV模型 | LCEV model
- 微分算子的主符号 | Leading symbol of a differential operator
- 勒贝格-斯蒂尔杰斯积分 | Lebesgue-Stieltjes integral
- 李矩公式 | Lee moment formula
- 长度曲线 | Length curve
- 列维-奇维塔联络 | Levi-Cevita connection
- Libor市场模型 | Libor market model
- Libor市场模型(LMM) | Libor market model (LMM)
- Libor波动率三角 | Libor volatility triangle
- 李代数 | Lie algebra
- 线丛 | Line bundle
- 线性算子 | Linear operator
- 局部鞅 | Local martingale
- 局部偏度 | Local skew
- 局部维加 | Local Vega
- 局部化费曼-卡克 | Localized Feynman-Kac
- 对数正态SABR模型 | Log-normal SABR model
- 马利亚万导数 | Malliavin derivative
- 马利亚万分部积分 | Malliavin Integration by parts
- 流形 | Manifold
- H3流形 | Manifold H3
- 市场模型 | Market model
- 马尔可夫Libor市场模型 | Markov Libor Market Model
- 马尔可夫实现 | Markovian realization
- 鞅 | Martingale
- 到期日 | Maturity
- 可测函数 | Measurable function
- 可测空间 | Measurable space
- 梅勒公式 | Mehler formula
- 默顿模型 | Merton model
- 度量 | Metric
- 米尔斯坦格式 | Milstein scheme
- 闵可夫斯基伪球面 | Minkowski pseudo-sphere
- 混合局部-随机波动率模型 | Mixed local-stochastic volatility model
- 混合解 | Mixing solution
- 莫比乌斯变换 | Moebius transformation
- 货币市场账户 | Money market account
- 拿破仑期权 | Napoleon option
- 纳坦松势 | Natanzon potential
- 可忽略集 | Negligible sets
- 幂等步骤1 LV模型 | Nilpotent step 1 LV model
- 非自治加藤类 | Non-autonomous Kato class
- 非爆炸性 | Non-explosion
- 非线性布莱克-斯科尔斯偏微分方程 | Non-linear Black-Scholes PDE
- 范数 | Norm
- 正态SABR模型 | Normal SABR model
- 诺维科夫条件 | Novikov condition
- 计价单位 | Numéraire
- 数算子 | Number operator
- 一形式 | One-form
- 稠密定义算子 | Operator densely defined
- 奥恩斯坦-乌伦贝克过程 | Ornstein-Uhlenbeck
- 奥恩斯坦-乌伦贝克算子 | Ornstein-Uhlenbeck operator
- 损益θ-Γ | P&L Theta-Gamma
- 平行规范传输 | Parallel gauge transport
- 单位分解 | Partition of unity
- 路径空间 | Path space
- 收益 | Payoff
- 庞加莱圆盘 | Poincaré disk
- 预测-校正器 | Predictor-corrector
- 本原元素 | Primitive element
- 概率测度 | Probability measure
- 回拉丛 | Pullback bundle
- 回拉联络 | Pullback connection
- 看涨-看跌对偶性 | Put-call duality
- 看涨-看跌平价 | Put-call parity
- 看涨-看跌对称性 | Put-call symmetry
- 二次变差 | Quadratic variation
- 拟随机数 | Quasi-random number
- 拉东-尼科迪姆 | Radon-Nikodym
- 随机变量 | Random variables
- Rebonato参数化 | Rebonato parametrization
- 约化方法 | Reduction method
- 正则值 | Regular value
- 正则变化函数 | Regularly varying function
- 单位分解 | Resolution of the identity
- 预解式 | Resolvent
- 黎奇张量 | Ricci tensor
- 黎曼张量 | Riemann tensor
- 黎曼一致化定理 | Riemann Uniformization theorem
- 风险中性测度 | Risk-neutral measure
- SABR公式 | SABR formula
- SABR-LMM | SABR-LMM
- 鞍点法 | Saddle-point
- 标量曲率 | Scalar curvature
- 薛定谔-布莱克方程 | Scholes-Black equation
- 二阶矩匹配 | Second moment matching
- 资产定价第二定理 | Second theorem of asset pricing
- 二阶椭圆算子 | Second-order elliptic operator
- 截面 | Section
- 自伴随扩张 | Self-adjoint extension
- 自伴随算子 | Self-adjoint operator
- 自融资组合 | Self-financing portfolio
- 可分希尔伯特空间 | Separable Hilbert space
- 可分离局部波动率模型 | Separable local volatility model
- 短期利率模型 | Short-rate model
- 偏度 | Skew
- 平值偏度 | Skew at-the-money
- 远期平值偏度 | Skew at-the-money forward
- 偏度平均 | Skew averaging
- 斯科霍罗德积分 | Skorohod integral
- 小型交易者 | Small traders
- 即期 | Spot
- 即期Libor测度 | Spot Libor measure
- 静态复制 | Static replication
- 粘性规则 | Sticky rules
- 斯蒂尔杰斯函数 | Stiejles function
- 随机波动率Libor市场模型 | Stochastic volatility Libor market model
- 随机波动率模型 | Stochastic volatility Model
- 随机完备 | Stochastically complete
- 斯特拉托诺维奇积分 | Stratonovich integral
- 执行价格 | Strike
- 强收敛 | Strong convergence
- 强收敛阶 | Strong order of convergence
- 强解 | Strong solution
- 超荷算子 | Supercharge operators
- 超势 | Superpotential
- 随机波动率模型(SVM) | SVM
- 互换 | Swap
- 掉期期权 | Swaption
- 掉期期权隐含波动率 | Swaption implied volatility
- 切向过程 | Tangent process
- 切空间 | Tangent space
- 泰勒-斯特拉托诺维奇展开 | Taylor-Stratonovich expansion
- $(r,p)$型张量 | Tensor of type $(r,p)$
- 张量向量丛 | Tensor vector bundle
- 时变热核展开 | Time-dependent heat kernel expansion
- 扭率 | Torsion
- 平凡向量丛 | Trivial vector bundle
- 无界线性算子 | Unbounded Linear operator
- 一致化定理 | Uniformization theorem
- 解的唯一性 | Unique in law
- 上半平面 | Upper half-plane
- 方差互换 | Variance swap
- 向量丛 | Vector bundle
- 向量场 | Vector field
- 波动率的波动率 | Volatility of volatility (vol of vol)
- 波动率互换 | Volatility swap
- 弱导数 | Weak derivative
- 弱收敛阶 | Weak order of convergence
- 弱解 | Weak solution
- 白噪声 | White noise
- 维克恒等式 | Wick identity
- 维克乘积 | Wick product
- 维纳混沌 | Wiener chaos
- 维纳测度 | Wiener measure
- 山本定理 | Yamato theorem
    以下是需要翻译的内容：
    {content}"""


def get_retry_delay(retry_count):
    """计算指数退避延迟时间"""
    base_delay = 5  # 基础延迟5秒
    max_delay = 120  # 最大延迟120秒
    delay = min(base_delay * (2 ** retry_count), max_delay)
    jitter = random.uniform(0, 0.1 * delay)  # 添加随机抖动
    return delay + jitter


def translate_markdown(input_file: Path, output_file: Path, token_counter: TokenCounter):
    """翻译单个markdown文件的函数"""
    print(f"\n开始处理文件: {input_file.name}")

    # 读取文件内容
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 准备输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("")

    max_retries = 20
    retry_count = 0
    accumulated_translation = ""

    while True:
        try:
            print(f"发送翻译请求...")

            response = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=8192,
                system=get_translation_prompt(),
                messages=[
                    {"role": "user", "content": content}
                ] if not accumulated_translation else [
                    {"role": "user", "content": content},
                    {"role": "assistant", "content": accumulated_translation},
                    {"role": "user", "content": "继续翻译剩余内容，一次尽可能多地翻译内容，避免生成其他文本"}
                ]
            )

            reply = response.content[0].text.strip()
            accumulated_translation += reply

            token_counter.add_usage(
                response.usage.input_tokens,
                response.usage.output_tokens
            )

            input_cost = (response.usage.input_tokens / 1000) * INPUT_COST_PER_1K
            output_cost = (response.usage.output_tokens / 1000) * OUTPUT_COST_PER_1K

            print(f"\n当前请求token使用:")
            print(f"输入tokens: {response.usage.input_tokens:,}")
            print(f"输出tokens: {response.usage.output_tokens:,}")
            print(f"成本: ${input_cost + output_cost:.4f}")
            print(f"收到回复，长度：{len(reply)}")

            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(reply + "\n\n")

            if "本次翻译任务完成" in reply:
                print(f"文件 {input_file.name} 翻译完成")
                token_counter.add_file()
                break

            retry_count = 0

        except anthropic.APIError as e:
            if "overloaded_error" in str(e) or "529" in str(e):
                print(f"服务器过载，等待重试...")
                retry_delay = get_retry_delay(retry_count)
                print(f"将在 {retry_delay:.1f} 秒后重试")
                time.sleep(retry_delay)
                retry_count += 1
                if retry_count > max_retries:
                    print("超过最大重试次数，任务终止。")
                    return False
                continue

            print(f"API错误: {e}")
            retry_count += 1
            if retry_count > max_retries:
                print("超过最大重试次数，任务终止。")
                return False
            retry_delay = get_retry_delay(retry_count)
            print(f"重试第 {retry_count} 次，将在 {retry_delay:.1f} 秒后重试...")
            time.sleep(retry_delay)

        except (anthropic.RateLimitError, anthropic.APIConnectionError) as e:
            print(f"连接错误或速率限制: {e}")
            retry_count += 1
            if retry_count > max_retries:
                print("超过最大重试次数，任务终止。")
                return False
            retry_delay = get_retry_delay(retry_count)
            print(f"重试第 {retry_count} 次，将在 {retry_delay:.1f} 秒后重试...")
            time.sleep(retry_delay)

        except Exception as e:
            print(f"未预期的错误: {str(e)}")
            retry_count += 1
            if retry_count > max_retries:
                print("超过最大重试次数，任务终止。")
                return False
            retry_delay = get_retry_delay(retry_count)
            print(f"重试第 {retry_count} 次，将在 {retry_delay:.1f} 秒后重试...")
            time.sleep(retry_delay)

    return True


def process_markdown_files():
    """处理文件夹中的所有markdown文件"""
    # 获取所有markdown文件
    md_files = list(WORK_DIR.glob("*.md"))
    if not md_files:
        print("workmd文件夹中没有找到markdown文件")
        return

    print(f"找到 {len(md_files)} 个markdown文件")

    # 初始化计数器
    token_counter = TokenCounter()

    # 遍历处理每个文件
    for i, input_file in enumerate(md_files, 1):
        print(f"\n=== 处理第 {i}/{len(md_files)} 个文件 ===")

        # 构建输出文件路径
        output_file = OUTPUT_DIR / f"translated_{input_file.name}"

        try:
            success = translate_markdown(input_file, output_file, token_counter)
            if not success:
                print(f"文件 {input_file.name} 处理失败")
                continue

        except Exception as e:
            print(f"处理文件 {input_file.name} 时发生错误: {e}")
            continue

    # 打印总体统计信息
    print("\n=== 批量处理完成 ===")
    token_counter.print_summary()


def main():
    try:
        # 检查工作目录是否存在
        if not WORK_DIR.exists():
            print(f"错误：工作目录 {WORK_DIR} 不存在")
            return

        process_markdown_files()

    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"发生未预期的错误: {str(e)}")


if __name__ == "__main__":
    main()