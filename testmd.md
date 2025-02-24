# Part IV Appendices 
## Appendix A Interest Rate Definitions

In this appendix, we provide derivations of various rates discussed throughout the book, including both simple and continuously compounded instantaneous rates. Before delving into the derivations, it is essential to understand rates from two key perspectives: lending versus borrowing and the timing of payments or receipts in relation to zero-coupon bonds, often referred to as T-bonds.

### A.1 Borrowing and Lending Rates

We have all heard that a dollar today is not worth the same as a dollar a year from now, and this has to do with the time value of money. Consider borrowing $\$ 1$ today. How much would you need to repay a year from now? You would certainly owe more than a dollar, depending on the borrowing rate agreed upon at the time of borrowing. Conversely, if you were to lend $\$ 1$ today, you would expect to receive more than a dollar a year from now, with the additional amount determined by the lending rate. These rates are determined by market participants, including lenders and borrowers, as well as economic forecasts.

A zero-coupon bond, labeled as $P\left( {t, T}\right)$ , signifies the amount you would pay at time $t$ to receive $\$ 1$ dollar at a future time $T$ . It is worth noting that $P\left( {t, t}\right)$ equals 1 . This is often referred to as the zero-coupon bond or simply the T-bond for simplicity. For illustrative purposed we can assume a constant borrowing/lending rate for $\left\lbrack  {t, T}\right\rbrack$ for ant $T$ and the simplest form for $P\left( {t, T}\right)$ would be given by

$$
P\left( {t, T}\right)  = {e}^{-\xi \left( {T - t}\right) }
$$

Here $\xi$ is a dummy variable for the constant borrowing/lending rate. In Figure A.1, we see hypothetical zero-coupon curves for two different scenarios: one in a low-rate environment and the other in a high-rate environment. It is evident that in the high-rate environment, the curve is steep, while in the low-rate environment, it is much flatter.

Derivatives pricing models for equities, foreign exchange, and commodities are typically based on a single underlying asset. However, these models are not suitable for interest rate derivatives because their values depend on the entire yield curve or zero-coupon curve. To address this, specialized models known as term structure models are used. In these models, having the function $P\left( {t, T}\right)$ is crucial.

Calculating $P\left( {t, T}\right)$ involves using a stochastic model and highly liquid instruments as calibration tools. These instruments may include LIBOR rates, swap rates, futures, caps/floors, options on swaps (swaptions), and more. Alternatively, one can employ these instruments to construct the yield curve, as explained in Section 9.

![0195247f-2f23-7bdd-9335-9204d62fe613_570_509_144_612_498_0.jpg](images/0195247f-2f23-7bdd-9335-9204d62fe613_570_509_144_612_498_0.jpg)

FIGURE A.1: Zero-coupon curves for two different constant rates

### A.2 Forward Rate Agreement (FRA)

We start with defining forward contracts and then move on to forward rate agreement and find a link between forward rates and zero-coupon bonds.

Definition 5 (Forward Contracts) a forward contract is an obligation to buy (sell) an underlying asset at a specified forward price on a known date

Forward contracts are linear instruments that is their payoffs is a straight line. Expiration date of the contract and the forward price are written when the contract is entered into. If a forward purchase is made, the holder is said to be long in the underlying asset. On the other hand if at expiration the cash price is higher than forward price, the long position make a profit, otherwise there is a loss.

Definition 6 (Forward rate agreement) A forward rate agreement (FRA) is a tradable contract that can be used to directly trade simple forward rates. The contract involves three time instants: the current time $t$ , the expiry time $S$ where $S > t$ , and the maturity time $T$ with $T > S$ . The payoff of the contract at time $T$ is

$$
1 + \left( {T - S}\right)  \times  F\left( {t;S, T}\right)
$$

which results in a forward investment of one dollar at time $T$ .

However, we can replicate this investment using the following strategy: - at time $t$ : sell 1 S-bond and buy $\frac{P\left( {t, S}\right) }{P\left( {t, T}\right) }$ T-bonds $=$ zero net investment.

- at time $S$ : pay one dollar.

- at time $T$ : obtain $\frac{P\left( {t, S}\right) }{P\left( {t, T}\right) }$ dollars.

The net effect is a forward investment of one dollar at time $S$ yielding $\frac{P\left( {t, S}\right) }{P\left( {t, T}\right) }$ dollars at $T$ with certainty. By the no-arbitrage condition we can derive both simple and continuously compounded rates.



#### A.2.1 Simple (Simply Compounded) Forward Rate

By earlier argument, the simple (simply compounded) forward rate for $\left\lbrack  {S,{ST}}\right\rbrack$ prevailing at $t$ is given by

$$
1 + \left( {T - S}\right)  \times  F\left( {t;S, T}\right)  = \frac{P\left( {t, S}\right) }{P\left( {t, T}\right) } \tag{A.1}
$$

solving for $F\left( {t;S, T}\right)$ to obtain

$$
F\left( {t;S, T}\right)  = \frac{1}{T - S}\left( {\frac{P\left( {t, S}\right) }{P\left( {t, T}\right) } - 1}\right)  \tag{A.2}
$$

that the simple spot rate for $\left\lbrack  {t, T}\right\rbrack$ is given by

#### A.2.2 Simple Spot Rate

For the simple spot rate, we simply assume $T = t$ and from A. 2 we obtain

$$
F\left( {t, T}\right)  = F\left( {t;t, T}\right)  = \frac{1}{T - t}\left( {\frac{P\left( {t, t}\right) }{P\left( {t, T}\right) } - 1}\right)  \tag{A.3}
$$

$$
= \frac{1}{T - t}\left( {\frac{1}{P\left( {t, T}\right) } - 1}\right)
$$

This is the expression we will use to link LIBOR rates to $P\left( {t, T}\right)$

#### A.2.3 Continuously Compounded Forward Rate

By looking at the LHS of (A.1) and writing it in a continuously compounded form

$$
1 + \left( {T - S}\right)  \times  F\left( {t;S, T}\right)  = {e}^{R\left( {t;S, T}\right) \left( {T - S}\right) } \tag{A.4}
$$

where $R\left( {t;S, T}\right)$ is continuously compounded forward rate. It should be easy to see this is based on the limit definition as given in (A.5)

$$
\mathop{\lim }\limits_{{n \rightarrow  \infty }}{\left( 1 + \frac{\left( {T - S}\right)  \times  R\left( {t;S, T}\right) }{n}\right) }^{n} = {e}^{R\left( {t;S, T}\right) \left( {T - S}\right) } \tag{A.5}
$$

RHS of (A.4) and of RHS of (A.1) should be equal which implies

$$
{e}^{R\left( {t;S, T}\right) \left( {T - S}\right) } = \frac{P\left( {t, S}\right) }{P\left( {t, T}\right) }
$$

The continuously compounded forward rate for $\left\lbrack  {S, T}\right\rbrack$ prevailing at $t$ is given by

$$
{e}^{R\left( {t;S, T}\right) \left( {T - S}\right) } = \frac{P\left( {t, S}\right) }{P\left( {t, T}\right) }
$$

and solving for $R\left( {t;S, T}\right)$ we obtain

$$
R\left( {t, S, T}\right)  =  - \frac{\log P\left( {t, T}\right)  - \log P\left( {t, S}\right) }{T - S} \tag{A.6}
$$

#### A.2.4 Continuously Compounded Spot Rate

The continuously compounded spot rate for $\left\lbrack  {t, T}\right\rbrack$ is

$$
R\left( {t, T}\right)  = R\left( {t;t, T}\right)  =  - \frac{\log P\left( {t, T}\right)  - \log P\left( {t, t}\right) }{T - t}
$$

$$
=  - \frac{\log P\left( {t, T}\right) }{T - t} \tag{A.7}
$$

#### A.2.5 Instantaneous Forward Rate

The instantaneous forward rate with maturity $T$ prevailing at time $t$ is obtained by taking the limit in Equation A. 6 as $S$ approach $T$

$$
f\left( {t, T}\right)  = \mathop{\lim }\limits_{{S \uparrow  T}}R\left( {t;S, T}\right)
$$

$$
= \mathop{\lim }\limits_{{S \uparrow  T}} - \frac{\log P\left( {t, T}\right)  - \log P\left( {t, S}\right) }{T - S}
$$

$$
=  - \frac{\partial \log P\left( {t, T}\right) }{\partial T} \tag{A.8}
$$

The function $T \rightarrow  f\left( {t, T}\right)$ is called the forward curve at time $t$ .

#### A.2.6 Instantaneous Short Rate

The instantaneous short rate at time $t$ is defined by

$$
r\left( t\right)  = f\left( {t, t}\right)  = \mathop{\lim }\limits_{{t \uparrow  T}}R\left( {t, T}\right)  \tag{A.9}
$$

### A.3 Zero-Coupon Bond Price

For the zero-coupon bond price, $P\left( {t, T}\right)$ , we can solve Equation (A.8) to obtain

$$
P\left( {t, T}\right)  = \exp \left( {-{\int }_{t}^{T}f\left( {t, u}\right) {du}}\right)  \tag{A.10}
$$

where $P\left( {t, t}\right)  = 1$ . From Equation we can see having the forward curve at time $t$ for all $T > t$ , i.e., $f\left( {t, T}\right)$ we can easily calculate $P\left( {t, T}\right)$ .

### A.4 Futures Contracts

Futures and forward contracts (or in short forwards) are similar instruments. Futures, like forwards, are linear instruments. The major differences between the two are: (a) futures are traded in formalized exchanges, (b) the exchange designs a standard contract and sets some specific expiration dates, (c) forwards are custom-made and are traded over-the-counter, (d) futures exchanges are cleared through exchange clearing houses, (e) there is an intricate mechanism to reduce the default risk, (f) futures contracts are marked to market on a daily basis, and (g) everyday the contract is settled and simultaneously a new contract is written. Futures can be used as calibration instruments for constructing the yield curve. This is discussed in Section 9.6 of Chapter 9. There is a convexity correction due to difference before futures and forwards. In some case practitioners may ignore this correction.

### A.5 Swaps

Definition 7 (Swaps) A swap is the simultaneous selling and purchasing of cashflows involving various currencies, interest rates, and a number of other financial assets.

Decomposing a swap into its constituent components is an interesting and insightful example of financial engineering that illustrates the special role played by simple forwards and options.

Here we will focus on a simple interest rate swap. In its simplest form, an interest rate swap between two counterparties is created as a result of the following steps: (a) counterparty A needs a $\$ 1$ million floating-rate loan, counterparty B needs a $\$ 1$ million fixed-rate loan. Because of market conditioned and their relationships with various banks, counterparty B has a comparative advantage in borrowing at a floating rate. Counterparties A and B decide to use this comparative advantage. Each borrows at the market where she had a comparative advantage, and then decides to exchange the interest payments. Counterparty A borrows $\$ 1$ million at fixed rate. The interest payments will be received from counterparty B and paid back to the lending bank. Counterparty B borrows \$1 million at the floating rate. Interest rate payments will be received from counterparty $\mathrm{A}$ and will be repaid to the lending bank.

Note that the initial sums, each being $\$ 1$ million, are identical. Therefore, they do not have to be exchanges. They are called notional principals. The interest payments are also in the same currency. Therefore, the counterparties exchange only the interest differentials. At the end both counterparties will secure lower rates and swap dealer will earn a fee.

Swap Rate in Terms of Forward Rates: a swap can be viewed as a portfolio of forward rate agreements (FRAs). Each cash flow is the cash flow of an FRA with fixed rate equal to the swap rate $s$ . Therefore, there is a no-arbitrage relation between the LIBOR curve and forward rates curve in LIBOR-based FRAs.

#### A.5.1 Terms and Payments

Most popular terms for (vanilla) swap rates are $2,5,{10}\& {30}$ years. For payments, there are two legs: (a) fixed leg and (b) floating leg. For the fixed leg, there are two semi-annual payments with fixed rate set a priori. For the floating leg, there are four quarterly payments, resetting quarterly, and 3M-LIBOR floating rate. Example 60 illustrates the cash flow analysis for a 2-year swap under a hypothetical rates.

Example 60 cash flow analysis of a 2-yr swap

In this example, we look into payments of a 2-yr swap payments, assuming notional principal \$1,000,000. For the fixed leg, as mentioned earlier, we would have four (fixed) payments paid every six months. Assume the (fixed) rate is %2.9894, therefore

$$
{p}_{\text{fixed }} = \frac{1,{000},{000} \times  \frac{2.9894}{100}}{2} = \$ {14},{947}
$$

Throughout the life of the swap this would be the fixed payment every six months no matter what happens. For the floating leg, there would be eight (floating) payments paid every three months. These payments vary depending on the floating rate. First payment paid in three months set at the current time. Assume 3M LIBOR at the current time is 2.7012%, therefore the first payment in three months would be

$$
{p}_{\text{floating }} = \frac{1,{000},{000} \times  \frac{2.7012}{100}}{4} = \$ 6,{573}
$$

Assume 3M-LIBOR for the second payment would be 2.4293%

$$
{p}_{\text{floating }} = \frac{1,{000},{000} \times  \frac{2.8470}{100}}{4} = \$ 7,{117}
$$

There would be six more payments. Assume for the last payment 3M-LIBOR is at 4.0120% and the payment would be

$$
{p}_{\text{floating }} = \frac{1,{000},{000} \times  \frac{4.0120}{100}}{4} = \$ {10},{030}
$$

As can been the floating payments are pretty stochastic depending on the rate at the beginning of that tenor.

Assuming $n$ equidistant times $t = {T}_{0},{T}_{1},\ldots ,{T}_{n} = T$ . In can be shown that a swap rate can be written as a function of $P\left( {t, T}\right)$ as given in Equation (A.11)

$$
s\left( {t, T}\right)  = {100}\frac{P\left( {t, t}\right)  - P\left( {t,{T}_{n}}\right) }{\Delta \mathop{\sum }\limits_{{j = 1}}^{n}P\left( {t,{T}_{j}}\right) }
$$

$$
= {100}\frac{1 - P\left( {t, T}\right) }{\Delta \mathop{\sum }\limits_{{j = 1}}^{n}P\left( {t,{T}_{j}}\right) } \tag{A.11}
$$

where $\Delta  = {T}_{j} - {T}_{j - 1} = \frac{1}{2}$ for semi-annual.

## Appendix B Arbitrage Restrictions on Option Premiums

In this book, we have presented a variety of different models and a number of different methods for solving for option premiums under those models. In this chapter, we have expanded on this by presenting a number of different methods for calibrating those models to option prices in different markets. However, there are a number of different restrictions on options premia which can be derived from simple no-arbitrage arguments without the need for any modeling whatsoever. These can be used as a sanity check for options pricing and calibration procedures, as a violation of these rules would represent an immediate arbitrage opportunity.

### B.1 Simple No-arbitrage Arguments

Assume strikes indexes are in an increasing order so that ${K}_{i + 1} > {K}_{i}$ for all $i$ . The rules which can be derived this way are as follows:

- Monotonicity, for any two consecutive strikes, for calls, ask price of smaller strike is more than bid pricde of the larger strike and for puts bid price of smaller strike is smaller than ask pricde of larger strike,

Calls

$$
{C}^{\text{ask }}\left( {K}_{i}\right)  > {C}^{\text{bid }}\left( {K}_{i + 1}\right) \;\forall i
$$

Puts

$$
{P}^{\text{bid }}\left( {K}_{i}\right)  < {P}^{\text{ask }}\left( {K}_{i + 1}\right) \;\forall i
$$

- Slope, for any two consecutive strikes, for calls, ask price of smaller strike is more than bid pricde of the larger strike and for puts bid price of smaller strike is smaller than ask pricde of larger strike,

Calls

$$
{C}^{\text{bid }}\left( {K}_{i}\right)  - {C}^{\text{ask }}\left( {K}_{i + 1}\right)  < \left( {{K}_{i + 1} - {K}_{i}}\right) {e}^{-{r\tau }}\;\forall i
$$

Puts

$$
{P}^{\text{bid }}\left( {K}_{i + 1}\right)  - {P}^{\text{ask }}\left( {K}_{i}\right)  < \left( {{K}_{i + 1} - {K}_{i}}\right) {e}^{-{r\tau }}\;\forall i
$$

- Convexity, any two consecutive strikes, for calls, ask price of smaller strike is more than bid pricde of the larger strike and for puts bid price of smaller strike is smaller than ask pricde of larger strike,

Calls

$$
{C}^{\text{bid }}\left( {K}_{i + 1}\right)  < \lambda {C}^{\text{ask }}\left( {K}_{i}\right)  + \left( {1 - \lambda }\right) {C}^{\text{ask }}\left( {K}_{i + 2}\right) \;\forall i
$$

Puts

$$
{P}^{\text{bid }}\left( {K}_{i + 1}\right)  < \lambda {P}^{\text{ask }}\left( {K}_{i}\right)  + \left( {1 - \lambda }\right) {P}^{\text{ask }}\left( {K}_{i + 2}\right) \;\forall i
$$

where $\lambda  = \frac{{K}_{i + 2} - {K}_{i + 1}}{{K}_{i + 1} - {K}_{i}}$ .

## Appendix C Derivative Approximation by Finite Differences in Higher Dimensional Case

The most common finite differences formulas are relatively easy to derive. However, once we move to higher derivatives or higher order approximations, deriving the coefficients for the finite difference approximations can become cumbersome. In [122], a generic method has been developed for easily computing an approximation of ${f}^{\left( d\right) }\left( x\right)$ with an approximation order of $p$ with many examples in one-dimensional case in Chapter 3. In this appendix, we extend the methodology to the higher dimensional cases for mixed derivatives $\frac{{\partial }^{d}f\left( {{x}_{1},{x}_{2},\ldots ,{x}_{k}}\right) }{\partial {x}_{1}^{{d}_{1}}\partial {x}_{2}^{{d}_{2}}\ldots \partial {x}_{k}^{{d}_{k}}}$ for any arbitrary ${d}_{1},{d}_{2}$ , and ${d}_{k}$ of any approximation order ${p}_{1},{p}_{2}$ , and ${p}_{k}$ . An example of mixed derivatives can be seen in the Heston stochastic volatility model.

### C.1 Derivative Approximation by Finite Differences: Generic Approach in k-dimensional

Assume we have a function $f : {\mathbb{R}}^{k} \rightarrow  \mathbb{R}$ of $k$ -variables and moreover $f \in  {C}^{\infty }$ , we can write the Taylor series expansion of $f\left( {{x}_{1} + {i}_{1}{h}_{1},{x}_{2} + {i}_{2}{h}_{2},\ldots ,{x}_{k} + {i}_{k}{h}_{k}}\right)$ as follows:

$$
f\left( {{x}_{1} + {i}_{1}{h}_{1},{x}_{2} + {i}_{2}{h}_{2},\ldots ,{x}_{k} + {i}_{k}{h}_{k}}\right)
$$

$$
= \mathop{\sum }\limits_{{{n}_{1} = 0}}^{\infty }\frac{1}{{n}_{1}!}{\left( {i}_{1}{h}_{1}\right) }^{{n}_{1}}\frac{{\partial }^{{n}_{1}}f\left( {{x}_{1},{x}_{2} + {i}_{2}{h}_{2},\ldots ,{x}_{k} + {i}_{k}{h}_{k}}\right) }{\partial {x}_{1}^{{n}_{1}}}
$$

$$
= \mathop{\sum }\limits_{{{n}_{1} = 0}}^{\infty }\frac{1}{{n}_{1}!}{\left( {i}_{1}{h}_{1}\right) }^{{n}_{1}}\left( {\mathop{\sum }\limits_{{{n}_{2} = 0}}^{\infty }\frac{1}{{n}_{2}!}{\left( {i}_{2}{h}_{2}\right) }^{{n}_{2}}\frac{{\partial }^{{n}_{1} + {n}_{2}}f\left( {{x}_{1},{x}_{2},\ldots ,{x}_{k} + {i}_{k}{h}_{k}}\right) }{\partial {x}_{1}^{{n}_{1}}\partial {x}_{2}^{{n}_{2}}}}\right)
$$

$$
= \mathop{\sum }\limits_{{{n}_{1} = 0}}^{\infty }\mathop{\sum }\limits_{{{n}_{2} = 0}}^{\infty }\frac{1}{{n}_{1}!}\frac{1}{{n}_{2}!}{\left( {i}_{1}{h}_{1}\right) }^{{n}_{1}}{\left( {i}_{2}{h}_{2}\right) }^{{n}_{2}}\frac{{\partial }^{{n}_{1} + {n}_{2}}f\left( {{x}_{1},{x}_{2},\ldots ,{x}_{k} + {i}_{k}{h}_{k}}\right) }{\partial {x}_{1}^{{n}_{1}}\partial {x}_{2}^{{n}_{2}}}
$$

$$
\vdots
$$

$$
= \mathop{\sum }\limits_{{{n}_{1} = 0}}^{\infty }\mathop{\sum }\limits_{{{n}_{2} = 0}}^{\infty }\ldots \mathop{\sum }\limits_{{{n}_{k} = 0}}^{\infty }\frac{1}{{n}_{1}!}\frac{1}{{n}_{2}!}\ldots \frac{1}{{n}_{k}!}{\left( {i}_{1}{h}_{1}\right) }^{{n}_{1}}{\left( {i}_{2}{h}_{2}\right) }^{{n}_{2}}\ldots {\left( {i}_{k}{h}_{k}\right) }^{{n}_{k}}\frac{{\partial }^{n}f\left( {{x}_{1},{x}_{2},\ldots ,{x}_{k}}\right) }{\partial {x}_{1}^{{n}_{1}}\partial {x}_{2}^{{n}_{2}}\ldots \partial {x}^{{n}_{k}}}
$$

(C.1)

where $n = \mathop{\sum }\limits_{{l = 1}}^{k}{n}_{l}$ with ${i}_{1},{i}_{2},\ldots ,{i}_{k} \in  \mathbb{Z}$ and ${h}_{1},{h}_{2},\ldots ,{h}_{k} \in  {\mathbb{R}}^{ + }$ .

The approximation of $\frac{{\partial }^{d}f\left( {{x}_{1},{x}_{2},\ldots ,{x}_{k}}\right) }{\partial {x}_{1}^{{d}_{1}}\partial {x}_{2}^{{d}_{2}}\ldots \partial {x}_{k}^{{d}_{k}}}$ with approximation order ${p}_{1},\ldots ,{p}_{k}$ on ${x}_{1},\ldots$ , ${x}_{k}$ respectively is described by the following difference equation:

$$
\frac{{\partial }^{d}f\left( {{x}_{1},{x}_{2},\ldots ,{x}_{k}}\right) }{\partial {x}_{1}^{{d}_{1}}\partial {x}_{2}^{{d}_{2}}\ldots \partial {x}_{k}^{{d}_{k}}} = \mathop{\sum }\limits_{{{i}_{1} = {i}_{{l}_{1}}}}^{{i}_{{u}_{1}}}\mathop{\sum }\limits_{{{i}_{2} = {i}_{{l}_{2}}}}^{{i}_{{u}_{2}}}\ldots \mathop{\sum }\limits_{{{i}_{k} = {i}_{{l}_{k}}}}^{{i}_{{u}_{k}}}{\widehat{c}}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}}f\left( {{x}_{1} + {i}_{1}{h}_{1},{x}_{2} + {i}_{2}{h}_{2},\ldots ,{x}_{k} + {i}_{k}{h}_{k}}\right)
$$

$$
+ O\left( {h}_{1}^{{p}_{1}}\right)  + O\left( {h}_{2}^{{p}_{2}}\right)  + \cdots  + O\left( {h}_{k}^{{p}_{k}}\right)
$$

where ${\widehat{c}}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}}$ are the unknown coefficients that we are looking for, ${i}_{{l}_{j}}$ and ${i}_{{u}_{j}}$ are the number of backward and forward terms in ${x}_{j}$ -direction in our approximation . If we multiply by $\frac{{h}_{1}^{{d}_{1}}}{{d}_{1}!}\frac{{h}_{2}^{{d}_{2}}}{{d}_{2}!}\ldots \frac{{h}_{k}^{{d}_{k}}}{{d}_{k}!}$ and define ${c}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}} = {\widehat{c}}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}}\frac{{h}_{1}^{{d}_{1}}}{{d}_{1}!}\frac{{h}_{2}^{{d}_{2}}}{{d}_{2}!}\ldots \frac{{h}_{k}^{{d}_{k}}}{{d}_{k}!}$ , we get

$$
\frac{{h}_{1}^{{d}_{1}}}{{d}_{1}!}\frac{{h}_{2}^{{d}_{2}}}{{d}_{2}!}\ldots \frac{{h}_{k}^{{d}_{k}}}{{d}_{k}!}\frac{{\partial }^{d}f\left( {{x}_{1},{x}_{2},\ldots ,{x}_{k}}\right) }{\partial {x}_{1}^{{d}_{1}}\partial {x}_{2}^{{d}_{2}}\ldots \partial {x}_{k}^{{d}_{k}}} + O\left( {h}_{1}^{{p}_{1} + {d}_{1}}\right)  + O\left( {h}_{2}^{{p}_{2} + {d}_{2}}\right)  + \cdots  + O\left( {h}_{k}^{{p}_{k} + {d}_{k}}\right)
$$

$$
= \mathop{\sum }\limits_{{{i}_{1} = {i}_{{l}_{1}}}}^{{i}_{{u}_{1}}}\mathop{\sum }\limits_{{{i}_{2} = {i}_{{l}_{2}}}}^{{i}_{{u}_{2}}}\cdots \mathop{\sum }\limits_{{{i}_{k} = {i}_{{l}_{k}}}}^{{i}_{{u}_{k}}}{c}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}}f\left( {{x}_{1} + {i}_{1}{h}_{1},{x}_{2} + {i}_{2}{h}_{2},\ldots ,{x}_{k} + {i}_{k}{h}_{k}}\right)  \tag{C.2}
$$

Substituting (C.1) into (C.2) we obtain

$$
\frac{{h}_{1}^{{d}_{1}}}{{d}_{1}!}\frac{{h}_{2}^{{d}_{2}}}{{d}_{2}!}\ldots \frac{{h}_{k}^{{d}_{k}}}{{d}_{k}!}\frac{{\partial }^{d}f\left( {{x}_{1},{x}_{2},\ldots ,{x}_{k}}\right) }{\partial {x}_{1}^{{d}_{1}}\partial {x}_{2}^{{d}_{2}}\ldots \partial {x}_{k}^{{d}_{k}}} + O\left( {h}_{1}^{{p}_{1} + {d}_{1}}\right)  + O\left( {h}_{2}^{{p}_{2} + {d}_{2}}\right)  + \cdots  + O\left( {h}_{k}^{{p}_{k} + {d}_{k}}\right)
$$

$$
= \mathop{\sum }\limits_{{{i}_{1} = {i}_{{l}_{1}}}}^{{i}_{{u}_{1}}}\cdots \mathop{\sum }\limits_{{{i}_{k} = {i}_{{l}_{k}}}}^{{i}_{{u}_{k}}}{c}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}}\mathop{\sum }\limits_{{{n}_{1} = 0}}^{\infty }\cdots \mathop{\sum }\limits_{{{n}_{k} = 0}}^{\infty }\frac{1}{{n}_{1}!}\ldots \frac{1}{{n}_{k}!}{\left( {i}_{1}{h}_{1}\right) }^{{n}_{1}}\ldots {\left( {i}_{k}{h}_{k}\right) }^{{n}_{k}}\frac{{\partial }^{n}f\left( {{x}_{1},\ldots ,{x}_{k}}\right) }{\partial {x}_{1}^{{n}_{1}}\cdots \partial {x}_{k}^{{n}_{k}}}
$$

$$
= \mathop{\sum }\limits_{{{i}_{1} = {i}_{{l}_{1}}}}^{{i}_{{u}_{1}}}\cdots \mathop{\sum }\limits_{{{i}_{k} = {i}_{{l}_{k}}}}^{{i}_{{u}_{k}}}{c}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}}\mathop{\sum }\limits_{{{n}_{1} = 0}}^{{{p}_{1} + {d}_{1} - 1}}\cdots \mathop{\sum }\limits_{{{n}_{k} = 0}}^{{{p}_{k} + {d}_{k} - 1}}\frac{1}{{n}_{1}!}\ldots \frac{1}{{n}_{k}!}{\left( {i}_{1}{h}_{1}\right) }^{{n}_{1}}\ldots {\left( {i}_{k}{h}_{k}\right) }^{{n}_{k}}
$$

$$
\times  \frac{{\partial }^{n}f\left( {{x}_{1},\ldots ,{x}_{k}}\right) }{\partial {x}_{1}^{{n}_{1}}\cdots \partial {x}_{k}^{{n}_{k}}} + O\left( {h}_{1}^{{p}_{1} + {d}_{1}}\right)  + \cdots  + O\left( {h}_{k}^{{p}_{k} + {d}_{k}}\right)
$$

multiplying by $\frac{{d}_{1}!}{{h}_{1}^{{d}_{1}}}\frac{{d}_{2}!}{{h}_{2}^{{d}_{2}}}\ldots \frac{{d}_{k}!}{{h}_{k}^{{d}_{k}}}$ we can see that

$$
\frac{{\partial }^{d}f\left( {{x}_{1},{x}_{2},\ldots ,{x}_{k}}\right) }{\partial {x}_{1}^{{d}_{1}}\partial {x}_{2}^{{d}_{2}}\ldots \partial {x}_{k}^{{d}_{k}}}
$$

$$
= \frac{{d}_{1}!}{{h}_{1}^{{d}_{1}}}\cdots \frac{{d}_{k}!}{{h}_{k}^{{d}_{k}}}\mathop{\sum }\limits_{{{i}_{1} = {i}_{{l}_{1}}}}^{{i}_{{u}_{1}}}\cdots \mathop{\sum }\limits_{{{i}_{k} = {i}_{{l}_{k}}}}^{{i}_{{u}_{k}}}{c}_{{i}_{1},\ldots ,{i}_{k}}\mathop{\sum }\limits_{{{n}_{1} = 0}}^{{{p}_{1} + {d}_{1} - 1}}\cdots \mathop{\sum }\limits_{{{n}_{k} = 0}}^{{{p}_{k} + {d}_{k} - 1}}\frac{1}{{n}_{1}!}\cdots \frac{1}{{n}_{k}!}{\left( {i}_{1}{h}_{1}\right) }^{{n}_{1}}\ldots {\left( {i}_{k}{h}_{k}\right) }^{{n}_{k}}
$$

$$
\times  \frac{{\partial }^{n}f\left( {{x}_{1},\ldots ,{x}_{k}}\right) }{\partial {x}_{1}^{{n}_{1}}\cdots \partial {x}_{k}^{{n}_{k}}} + O\left( {h}_{1}^{{p}_{1} + {d}_{1}}\right)  + \cdots  + O\left( {h}_{k}^{{p}_{k} + {d}_{k}}\right)
$$

For this to be true the following constraints should hold:

$$
\mathop{\sum }\limits_{{{i}_{1} = {i}_{{l}_{1}}}}^{{i}_{{u}_{1}}}\mathop{\sum }\limits_{{{i}_{2} = {i}_{{l}_{2}}}}^{{i}_{{u}_{2}}}\cdots \mathop{\sum }\limits_{{{i}_{k} = {i}_{{l}_{k}}}}^{{i}_{{u}_{k}}}{c}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}} = \left\{  \begin{array}{ll} 1 & {n}_{1} = {d}_{1} \land  {n}_{2} = {d}_{2} \land  \cdots  \land  {n}_{k} = {d}_{k} \\  0 & \text{ otherwise } \end{array}\right.
$$

#### C.1.1 Calculating Coefficients ${c}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}}$

Here are the findings and observations:

- The solution to these equations would be unique if and only if we limit the number of constraints in ${x}_{j}$ -direction to ${d}_{j} + {p}_{j}$ for $j = 1,\ldots , k$ . So we must have ${d}_{j} + {p}_{j} =$ ${i}_{{u}_{j}} - {i}_{{l}_{j}} + 1$ for all $j$ which restricts the number of terms we can use in our approximation

- In case of a forward difference approximation in all directions we set ${i}_{{l}_{j}} = 0,{i}_{{u}_{j}} =$ ${d}_{j} + {p}_{j} - 1$ for all $j$

- In case of a backward difference approximation in both directions we set ${i}_{{l}_{j}} =  - \left( {{d}_{j} + }\right.$ $\left. {{p}_{j} - 1}\right) ,{i}_{{u}_{j}} = 0$ for all $j$

- In case of a central difference approximation in both directions we set ${i}_{{l}_{j}} =  - \frac{1}{2}\left( {{d}_{j} + }\right.$ $\left. {{p}_{j} - 1}\right) ,{i}_{{u}_{j}} = \frac{1}{2}\left( {{d}_{j} + {p}_{j} - 1}\right)$ for all $j$

In Algorithm 42, we show how to set up the linear system ${Ac} = b$ to find vector $c$ by setting up matrix $A$ and vector $b$ . Having $A$ and $b$ , we can solve the following linear system for vector $c$ .

$$
{Ac} = b \tag{C.3}
$$


```

Algorithm 42 Algorith for finding ${c}_{{i}_{1},{i}_{2}\ldots ,{i}_{k}}$

---

Require: Set ${d}_{1},\ldots ,{d}_{k}$ and ${p}_{1},\ldots ,{p}_{k}$

Require: Allocate matrix $A$ of size $N \times  N$ where $N = \left( {{d}_{1} + {p}_{1}}\right)  \times  \cdots  \times  \left( {{d}_{k} + {p}_{k}}\right)$

Require: Allocate vector $b$ of size $N \times  1$

Require: Set ${i}_{{l}_{j}}$ and ${i}_{{u}_{j}}$ for $j = 1,\ldots , k$

	$i = 0$
	
	for ${n}_{1} = 0,\ldots ,{d}_{1} + {p}_{1} - 1$ do
	
			for ${n}_{2} = 0,\ldots ,{d}_{2} + {p}_{2} - 1$ do
	
				...
	
				for ${n}_{k} = 0,\ldots ,{d}_{k} + {p}_{k} - 1$ do
	
						$i \leftarrow  i + 1$
	
						$j \leftarrow  0$
	
						for ${i}_{1} = {i}_{{l}_{1}},\ldots ,{i}_{{u}_{1}}$ do
	
							for ${i}_{2} = {i}_{{l}_{2}},\ldots ,{i}_{{u}_{2}}$ do
	
									...
	
									for ${i}_{k} = {i}_{{l}_{k}},\ldots ,{i}_{{u}_{k}}$ do
	
										$j \leftarrow  j + 1$
	
										$A\left\lbrack  i\right\rbrack  \left\lbrack  j\right\rbrack   = {\left( {i}_{1}\right) }^{{n}_{1}} \times  {\left( {i}_{2}\right) }^{{n}_{2}} \times  \cdots  \times  {\left( {i}_{k}\right) }^{{n}_{k}}$
	
									end for
	
									. .
	
							end for
	
						end for
	
						if ${n}_{1} = {d}_{1} \land  {n}_{2} = {d}_{2} \land  \cdots  \land  {n}_{k} = {d}_{k}$ then
	
							$b\left\lbrack  i\right\rbrack   \leftarrow  1$
	
						else
	
							$b\left\lbrack  i\right\rbrack   \leftarrow  0$
	
						end if
	
				end for
	
				...
	
			end for
	
	end for

---
```

### C.2 Examples

We go through various different examples, starting with one-dimensional case, going to two-and three-dimensional cases.

#### C.2.1 One-dimensional Examples

Example 61 Forward difference approximation of third derivative of second order

Assume we want to compute the forward difference approximation of ${f}^{\left( 3\right) }\left( x\right)$ with $O\left( {h}^{2}\right)$ . Thus we have $d = 3$ and $p = 2, n = 0,1,\ldots , d + p - 1 = 4$ , and because we want a forward difference we have ${i}_{l} = 0$ and ${i}_{u} = 4$ . The constraint is then

$$
\mathop{\sum }\limits_{{i = 0}}^{4}{c}_{i}{i}^{n} = \left\{  \begin{array}{ll} 1 & n = 3 \\  0 & n \neq  3 \end{array}\right.
$$

In a matrix form this would be

$$
\left\lbrack  \begin{matrix} {0}^{0} & {1}^{0} & {2}^{0} & {3}^{0} & {4}^{0} \\  {0}^{1} & {1}^{1} & {2}^{1} & {3}^{1} & {4}^{1} \\  {0}^{2} & {1}^{2} & {2}^{2} & {3}^{2} & {4}^{2} \\  {0}^{3} & {1}^{3} & {2}^{3} & {3}^{3} & {4}^{3} \\  {0}^{4} & {1}^{4} & {2}^{4} & {3}^{4} & {4}^{4} \end{matrix}\right\rbrack  \left\lbrack  \begin{matrix} {c}_{0} \\  {c}_{1} \\  {c}_{2} \\  {c}_{3} \\  {c}_{4} \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix} 0 \\  0 \\  0 \\  1 \\  0 \end{matrix}\right\rbrack   \Rightarrow  \left\lbrack  \begin{matrix} {c}_{0} \\  {c}_{1} \\  {c}_{2} \\  {c}_{3} \\  {c}_{4} \end{matrix}\right\rbrack   = \left\lbrack  \begin{array}{l}  - 5/{12} \\  3/2 \\   - 2 \\  7/6 \\   - 1/4 \end{array}\right\rbrack
$$

and thus

$$
{f}^{\left( 3\right) }\left( x\right)  = \frac{3!}{{h}^{3}}\mathop{\sum }\limits_{{i = 0}}^{4}{c}_{i}f\left( {x + {ih}}\right)  + O\left( {h}^{p}\right)  \tag{C.4}
$$

$$
= \frac{-{5f}\left( x\right)  + {18f}\left( {x + h}\right)  - {24f}\left( {x + {2h}}\right)  + {14f}\left( {x + {3h}}\right)  - {3f}\left( {x + {4h}}\right) }{2{h}^{3}} + O\left( {h}^{2}\right)
$$

Example 62 Central difference approximation of second derivative of order 3

For this example we have $d = 2$ and $p = 3, n = 0,1,\ldots , d + p - 1 = 4$ , and for central difference ${i}_{l} =  - 2$ , and ${i}_{u} = 2$ .

$$
\mathop{\sum }\limits_{{i =  - 2}}^{2}{c}_{i}{i}^{n} = \left\{  \begin{array}{ll} 1 & n = 2 \\  0 & n \neq  2 \end{array}\right.
$$

In matrix form that is

$$
\left\lbrack  \begin{matrix} {\left( -2\right) }^{0} & {\left( -1\right) }^{0} & {0}^{0} & {1}^{0} & {2}^{0} \\  {\left( -2\right) }^{1} & {\left( -1\right) }^{1} & {1}^{1} & {1}^{1} & {2}^{1} \\  {\left( -2\right) }^{2} & {\left( -1\right) }^{2} & {0}^{2} & {1}^{2} & {2}^{2} \\  {\left( -2\right) }^{3} & {\left( -1\right) }^{3} & {0}^{3} & {1}^{3} & {2}^{3} \\  {\left( -2\right) }^{4} & {\left( -1\right) }^{4} & {0}^{4} & {1}^{4} & {2}^{4} \end{matrix}\right\rbrack  \left\lbrack  \begin{matrix} {c}_{-2} \\  {c}_{-1} \\  {c}_{0} \\  {c}_{1} \\  {c}_{2} \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix} 0 \\  0 \\  1 \\  0 \\  0 \end{matrix}\right\rbrack   \Rightarrow  \left\lbrack  \begin{matrix} {c}_{-2} \\  {c}_{-1} \\  {c}_{0} \\  {c}_{1} \\  {c}_{2} \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix}  - 1/{24} \\  2/3 \\   - 5/4 \\  2/3 \\   - 1/{24} \end{matrix}\right\rbrack
$$

Thus

$$
{f}^{\left( 2\right) }\left( x\right)  = \frac{2!}{{h}^{2}}\mathop{\sum }\limits_{{i =  - 2}}^{2}{c}_{i}f\left( {x + {ih}}\right)  + O\left( {h}^{p}\right)  \tag{C.5}
$$

$$
= \frac{-f\left( {x - {2h}}\right)  + {16f}\left( {x - h}\right)  - {30f}\left( x\right)  + {16f}\left( {x + h}\right)  - f\left( {x + {2h}}\right) }{{12}{h}^{2}} + O\left( {h}^{3}\right)
$$

Derivative Approximation by Finite Differences in Higher Dimensional Case

#### C.2.2 Two-dimensional Examples

Example 63 Central difference approximation of cross derivative $\frac{{\partial }^{2}f\left( {{x}_{1},{x}_{2}}\right) }{\partial {x}_{1}\partial {x}_{2}}$ of second order in both ${x}_{1}$ and ${x}_{2}$

Assume we want to compute the forward difference approximation of $\frac{{\partial }^{2}f\left( {{x}_{1},{x}_{2}}\right) }{\partial {x}_{1}\partial {x}_{2}}$ with $O\left( {h}_{1}^{2}\right)  +$ $O\left( {h}_{2}^{2}\right)$ . Thus we have ${d}_{1} = 1,{d}_{2} = 1,{p}_{1} = 2$ and ${p}_{2} = 2$ , and because we want a central difference we have ${i}_{{l}_{1}} =  - \frac{1}{2}\left( {{d}_{1} + {p}_{1} - 1}\right)  =  - 1,{i}_{{u}_{1}} = \frac{1}{2}\left( {{d}_{1} + {p}_{1} - 1}\right)  = 1,{i}_{{l}_{2}} =  - \frac{1}{2}\left( {{d}_{2} + {p}_{2} - 1}\right)  =$ $- 1,{i}_{{u}_{2}} = \frac{1}{2}\left( {{d}_{2} + {p}_{2} - 1}\right)  = 1,{n}_{1} = 0,\ldots ,{d}_{1} + {p}_{1} - 1 = 2$ , and ${n}_{2} = 0,\ldots ,{d}_{2} + {p}_{2} - 1 = 2$ . The constraint is then

$$
\mathop{\sum }\limits_{{{i}_{1} =  - 1}}^{1}\mathop{\sum }\limits_{{{i}_{2} =  - 1}}^{1}{c}_{{i}_{1},{i}_{2}}{i}_{1}^{{n}_{1}}{i}_{2}^{{n}_{2}} = \left\{  \begin{array}{ll} 1 & {n}_{1} = 1 \land  {n}_{2} = 1 \\  0 & \text{ otherwise } \end{array}\right.
$$

In a matrix form this would be![0195247f-2f23-7bdd-9335-9204d62fe613_581_182_739_1274_445_0.jpg](images/0195247f-2f23-7bdd-9335-9204d62fe613_581_182_739_1274_445_0.jpg)

$$
\times  \left\lbrack  \begin{matrix} {c}_{-1, - 1} \\  {c}_{-1,0} \\  {c}_{-1, + 1} \\  {c}_{0, - 1} \\  {c}_{0,0} \\  {c}_{0, + 1} \\  {c}_{+1, - 1} \\  {c}_{+1,0} \\  {c}_{+1,0} \\  {c}_{+1,0} \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix} 0 \\  0 \\  0 \\  0 \\  1 \\  0 \\  0 \\  0 \\  0 \\  0 \end{matrix}\right\rbrack
$$

Or equivalently

$$
\left\lbrack  \begin{matrix}  + 1 &  + 1 &  + 1 &  + 1 &  + 1 &  + 1 &  + 1 &  + 1 & \\   - 1 & 0 &  + 1 &  - 1 & 0 &  + 1 &  - 1 & 0 &  + 1 \\   + 1 & 0 &  + 1 &  + 1 & 0 &  + 1 &  + 1 & 0 &  + 1 \\   - 1 &  - 1 &  - 1 & 0 & 0 & 0 &  + 1 &  + 1 &  + 1 \\   - 1 &  - 1 &  - 1 & 0 & 0 & 0 &  - 1 & 0 &  + 1 \\   + 1 & 0 &  - 1 & 0 & 0 & 0 &  + 1 & 0 &  + 1 \\   + 1 &  + 1 &  + 1 & 0 & 0 & 0 &  + 1 & 0 &  + 1 \\   + 1 &  + 1 &  + 1 & 0 & 0 & 0 &  - 1 & 0 &  + 1 \\   + 1 & 0 &  + 1 & 0 & 0 & 0 &  - 1 & 0 &  + 1 \\   & & & & & & & &  \end{matrix}\right\rbrack  \left\lbrack  \begin{matrix} {c}_{-1,1} \\  {c}_{-1,1} \\  {c}_{-1,1} \\  {c}_{0,0} \\  {c}_{0,1} \\  {c}_{0,1} \\  {c}_{1,1} \\  {c}_{1,1} \\  {c}_{1,1} \\  {c}_{1,1} \\  \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix} 0 \\  0 \\  0 \\  0 \\  1 \\  0 \\  0 \\  0 \\  0 \\  {c}_{0,1} \\  {c}_{1,1} \\  0 \\  \end{matrix}\right\rbrack   \Rightarrow  \left\lbrack  \begin{matrix}  + \frac{1}{{c}_{-1,0}} \\  {c}_{-1,0} \\  {c}_{-1,1} \\  {c}_{0,0} \\  {c}_{0,1} \\  {c}_{0,0} \\  {c}_{1,1} \\  {c}_{1,0} \\  {c}_{1,1} \\  {c}_{1,0} \\  {c}_{1,1} \\  \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix}  + \frac{1}{{c}_{-1,0}} \\   - \frac{1}{{c}_{-1,0}} \\  0 \\  0 \\  0 \\  0 \\   - \frac{1}{{c}_{-1,0}} \\   + \frac{1}{{c}_{-1,0}} \\  0 \\   - \frac{1}{{c}_{-1,0}} \\  \end{matrix}\right\rbrack
$$

The alternative to this could be of the following form

$$
\left\lbrack  \begin{matrix} {\left( -1\right) }^{0} & {0}^{0} & {1}^{0} \\  {\left( -1\right) }^{1} & {0}^{1} & {1}^{1} \\  {\left( -1\right) }^{2} & {0}^{2} & {1}^{2} \end{matrix}\right\rbrack  \left\lbrack  \begin{matrix} {c}_{-1, - 1} & {c}_{-1,0} & {c}_{-1,1} \\  {c}_{0, - 1} & {c}_{0,0} & {c}_{0,1} \\  {c}_{+1, - 1} & {c}_{+1,0} & {c}_{+1,1} \end{matrix}\right\rbrack  \left\lbrack  \begin{matrix} {\left( -1\right) }^{0} & {\left( -1\right) }^{1} & {\left( -1\right) }^{2} \\  {0}^{0} & {0}^{1} & {0}^{2} \\  {1}^{0} & {1}^{1} & {1}^{2} \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix} 0 & 0 & 0 \\  0 & 1 & 0 \\  0 & 0 & 0 \end{matrix}\right\rbrack
$$

or equivalently

$$
\left\lbrack  \begin{matrix} 1 & 1 & 1 \\   - 1 & 0 & 1 \\  1 & 0 & 1 \end{matrix}\right\rbrack  \left\lbrack  \begin{matrix} {c}_{-1, - 1} & {c}_{-1,0} & {c}_{-1,1} \\  {c}_{0, - 1} & {c}_{0,0} & {c}_{0,1} \\  {c}_{1, - 1} & {c}_{1,0} & {c}_{1,1} \end{matrix}\right\rbrack  \left\lbrack  \begin{matrix} 1 &  - 1 & 1 \\  1 & 0 & 0 \\  1 & 1 & 1 \end{matrix}\right\rbrack   = \left\lbrack  \begin{array}{lll} 0 & 0 & 0 \\  0 & 1 & 0 \\  0 & 0 & 0 \end{array}\right\rbrack
$$

multiplying by inverse of

$$
\left\lbrack  \begin{matrix} 1 & 1 & 1 \\   - 1 & 0 & 1 \\  1 & 0 & 1 \end{matrix}\right\rbrack
$$

from the left, and the inverse of

$$
\left\lbrack  \begin{matrix} 1 &  - 1 & 1 \\  1 & 0 & 0 \\  1 & 1 & 1 \end{matrix}\right\rbrack
$$

from the right we obtain

$$
\left\lbrack  \begin{matrix} {c}_{-1, - 1} & {c}_{-1,0} & {c}_{-1,1} \\  {c}_{0, - 1} & {c}_{0,0} & {c}_{0,1} \\  {c}_{1, - 1} & {c}_{1,0} & {c}_{1,1} \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix} \frac{1}{4} & 0 &  - \frac{1}{4} \\  0 & 0 & 0 \\   - \frac{1}{4} & 0 & \frac{1}{4} \end{matrix}\right\rbrack
$$

which is the same result as one would expect. Having $c$ ’s we can write

$$
\frac{{\partial }^{2}f\left( {{x}_{1},{x}_{2}}\right) }{\partial {x}_{1}\partial {x}_{2}} = \frac{1!}{{h}_{1}^{1}}\frac{1!}{{h}_{2}^{1}}\mathop{\sum }\limits_{{{i}_{1} =  - 1}}^{1}\mathop{\sum }\limits_{{{i}_{2} =  - 1}}^{1}{c}_{{i}_{1},{i}_{2}}f\left( {{x}_{1} + {i}_{1}{h}_{1},{x}_{2} + {i}_{2}{h}_{2}}\right)  + O\left( {h}_{1}^{2}\right)  + O\left( {h}_{2}^{2}\right)
$$

$$
= \frac{\frac{1}{4}f\left( {{x}_{1} - {h}_{1},{x}_{2} - {h}_{2}}\right)  - \frac{1}{4}f\left( {{x}_{1} + {h}_{1},{x}_{2} - {h}_{2}}\right)  - \frac{1}{4}f\left( {{x}_{1} - {h}_{1},{x}_{2} + {h}_{2}}\right)  + \frac{1}{4}f\left( {{x}_{1} + {h}_{1},{x}_{2} + {h}_{2}}\right) }{{h}_{1}{h}_{2}}
$$

$$
+ O\left( {h}_{1}^{2}\right)  + O\left( {h}_{2}^{2}\right)
$$

$$
= \frac{f\left( {{x}_{1} - {h}_{1},{x}_{2} - {h}_{2}}\right)  - f\left( {{x}_{1} + {h}_{1},{x}_{2} - {h}_{2}}\right)  - f\left( {{x}_{1} - {h}_{1},{x}_{2} + {h}_{2}}\right)  + f\left( {{x}_{1} + {h}_{1},{x}_{2} + {h}_{2}}\right) }{4{h}_{1}{h}_{2}}
$$

$$
+ O\left( {h}_{1}^{2}\right)  + O\left( {h}_{2}^{2}\right)
$$

Example 64 Forward difference approximation of cross derivative $\frac{{\partial }^{2}f\left( {x, y}\right) }{\partial {x}_{1}\partial {x}_{2}}$ of second order in ${x}_{1}$ and second order in ${x}_{2}$

We wish to compute the forward difference approximation of $\frac{{\partial }^{2}f\left( {{x}_{1},{x}_{2}}\right) }{\partial {x}_{1}\partial {x}_{2}}$ with $O\left( {h}_{1}^{2}\right)  + O\left( {h}_{2}^{2}\right)$ . Thus we have ${d}_{1} = 1,{d}_{2} = 1,{p}_{1} = 2$ and ${p}_{2} = 2$ , and because we want a forward difference we have ${i}_{{l}_{1}} = 0,{i}_{{u}_{1}} = {d}_{1} + {p}_{1} - 1 = 2,{i}_{{l}_{2}} = 0,{i}_{{u}_{2}} = {d}_{2} + {p}_{2} - 1 = 2,{n}_{1} = 0,\ldots ,{d}_{1} + {p}_{1} - 1 = 2$ , and ${n}_{2} = 0,\ldots ,{d}_{2} + {p}_{2} - 1 = 2$ . The constraint is then

$$
\mathop{\sum }\limits_{{{i}_{1} = 0}}^{2}\mathop{\sum }\limits_{{{i}_{2} = 0}}^{2}{c}_{{i}_{1},{i}_{2}}{i}_{1}^{{n}_{1}}{i}_{2}^{{n}_{2}} = \left\{  \begin{array}{ll} 1 & {n}_{1} = 1 \land  {n}_{2} = 1 \\  0 & \text{ otherwise } \end{array}\right.
$$

In a matrix form this would be![0195247f-2f23-7bdd-9335-9204d62fe613_583_193_206_1254_342_0.jpg](images/0195247f-2f23-7bdd-9335-9204d62fe613_583_193_206_1254_342_0.jpg)

$$
= \left\lbrack  \begin{array}{l} 0 \\  0 \\  0 \\  0 \\  1 \\  0 \\  0 \\  0 \\  0 \end{array}\right\rbrack
$$

Or equivalently

$$
\left\lbrack  \begin{matrix} 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\  0 & 1 & 2 & 0 & 1 & 2 & 0 & 1 & 2 \\  0 & 1 & 4 & 0 & 1 & 4 & 0 & 1 & 4 \\  0 & 0 & 0 & 1 & 1 & 1 & 2 & 2 & 2 \\  0 & 0 & 0 & 0 & 1 & 2 & 0 & 2 & 4 \\  0 & 0 & 0 & 0 & 1 & 4 & 0 & 2 & 8 \\  0 & 0 & 0 & 1 & 1 & 1 & 4 & 4 & 4 \\  0 & 0 & 0 & 0 & 1 & 2 & 0 & 4 & 8 \\  0 & 0 & 0 & 0 & 1 & 2 & 0 & 4 & 8 \\  0 & 0 & 0 & 0 & 1 & 4 & 0 & 4 & {16} \end{matrix}\right\rbrack  \left\lbrack  \begin{matrix} {c}_{0,0} \\  {c}_{0,1} \\  {c}_{0,2} \\  {c}_{1,0} \\  {c}_{1,1} \\  {c}_{1,2} \\  {c}_{2,0} \\  {c}_{2,1} \\  {c}_{2,2} \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix} 0 \\  0 \\  0 \\  0 \\  1 \\  0 \\  0 \\  0 \\  0 \\  0 \\  {c}_{2,1} \\  {c}_{2,2} \end{matrix}\right\rbrack   \Rightarrow  \left\lbrack  \begin{matrix}  + \frac{9}{4} \\  {c}_{0,1} \\  {c}_{0,2} \\  {c}_{1,0} \\  {c}_{1,1} \\  {c}_{1,2} \\  {c}_{2,0} \\  {c}_{2,1} \\  {c}_{2,2} \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix}  + \frac{9}{4} \\   - \frac{3}{4} \\   + \frac{3}{4} \\   - 3 \\   + 4 \\  \frac{3}{4} \\   + \frac{1}{4} \\   + \frac{1}{4} \\  3 \\  3 \end{matrix}\right\rbrack
$$

As in the previous example, the alternative to this could be of the following form

$$
\left\lbrack  \begin{array}{lll} {0}^{0} & {1}^{0} & {2}^{0} \\  {0}^{1} & {1}^{1} & {2}^{1} \\  {0}^{2} & {1}^{2} & {2}^{2} \end{array}\right\rbrack  \left\lbrack  \begin{array}{lll} {c}_{0,0} & {c}_{0,1} & {c}_{0,2} \\  {c}_{1,0} & {c}_{1,1} & {c}_{1,2} \\  {c}_{2,0} & {c}_{2,1} & {c}_{2,2} \end{array}\right\rbrack  \left\lbrack  \begin{array}{lll} {0}^{0} & {0}^{1} & {0}^{2} \\  {1}^{0} & {1}^{1} & {1}^{2} \\  {2}^{0} & {2}^{1} & {2}^{2} \end{array}\right\rbrack   = \left\lbrack  \begin{array}{lll} 0 & 0 & 0 \\  0 & 1 & 0 \\  0 & 0 & 0 \end{array}\right\rbrack
$$

or

$$
\left\lbrack  \begin{array}{lll} 1 & 1 & 1 \\  0 & 1 & 2 \\  0 & 1 & 4 \end{array}\right\rbrack  \left\lbrack  \begin{array}{lll} {c}_{0,0} & {c}_{0,1} & {c}_{0,2} \\  {c}_{1,0} & {c}_{1,1} & {c}_{1,2} \\  {c}_{2,0} & {c}_{2,1} & {c}_{2,2} \end{array}\right\rbrack  \left\lbrack  \begin{array}{lll} 1 & 0 & 0 \\  1 & 1 & 1 \\  1 & 2 & 4 \end{array}\right\rbrack   = \left\lbrack  \begin{array}{lll} 0 & 0 & 0 \\  0 & 1 & 0 \\  0 & 0 & 0 \end{array}\right\rbrack
$$

multiplying by inverse of

$$
\left\lbrack  \begin{array}{lll} 1 & 1 & 1 \\  0 & 1 & 2 \\  0 & 1 & 4 \end{array}\right\rbrack
$$

from the left and multiplying by inverse of

$$
\left\lbrack  \begin{array}{lll} 1 & 0 & 0 \\  1 & 1 & 1 \\  1 & 2 & 4 \end{array}\right\rbrack
$$

from the right, we obtain

$$
\left\lbrack  \begin{array}{lll} {c}_{0,0} & {c}_{0,1} & {c}_{0,2} \\  {c}_{1,0} & {c}_{1,1} & {c}_{1,2} \\  {c}_{2,0} & {c}_{2,1} & {c}_{2,2} \end{array}\right\rbrack   = \left\lbrack  \begin{matrix} \frac{9}{4} &  - 3 & \frac{3}{4} \\   - 3 & 4 &  - 1 \\  \frac{3}{4} &  - 1 & \frac{1}{4} \end{matrix}\right\rbrack
$$

as expected we get the same result. Having $c$ ’s we can write

$$
\frac{{\partial }^{2}f\left( {{x}_{1},{x}_{2}}\right) }{\partial {x}_{1}\partial {x}_{2}}
$$

$$
= \frac{1!}{{h}_{1}^{1}}\frac{1!}{{h}_{2}^{1}}\mathop{\sum }\limits_{{{i}_{1} = 0}}^{2}\mathop{\sum }\limits_{{{i}_{2} = 0}}^{2}{c}_{{i}_{1},{i}_{2}}f\left( {{x}_{1} + {i}_{1}{h}_{1},{x}_{2} + {i}_{2}{h}_{2}}\right)  + O\left( {h}_{1}^{2}\right)  + O\left( {h}_{2}^{2}\right)
$$

$$
= \frac{\frac{9}{4}f\left( {{x}_{1},{x}_{2}}\right)  - {3f}\left( {{x}_{1} + {h}_{1},{x}_{2}}\right)  + \frac{3}{4}f\left( {{x}_{1} + 2{h}_{1},{x}_{2}}\right)  - {3f}\left( {{x}_{1},{x}_{2} + {h}_{2}}\right)  + {4f}\left( {{x}_{1} + {h}_{1},{x}_{2} + {h}_{2}}\right)  - f\left( {{x}_{1} + 2{h}_{1},{x}_{2} + {h}_{2}}\right) }{{h}_{1}{h}_{2}}
$$

$$
+ \frac{\frac{3}{4}f\left( {{x}_{1},{x}_{2} + 2{h}_{2}}\right)  - f\left( {{x}_{1} + {h}_{1},{x}_{2} + 2{h}_{2}}\right)  + \frac{1}{4}f\left( {{x}_{1} + 2{h}_{1},{x}_{2} + 2{h}_{2}}\right) }{{h}_{1}{h}_{2}} + O\left( {h}_{1}^{2}\right)  + O\left( {h}_{2}^{2}\right)
$$

$$
= \frac{{9f}\left( {{x}_{1},{x}_{2}}\right)  - {12f}\left( {{x}_{1} + {h}_{1},{x}_{2}}\right)  + {3f}\left( {{x}_{1} + 2{h}_{1},{x}_{2}}\right)  - {12f}\left( {{x}_{1},{x}_{2} + {h}_{2}}\right)  + {16f}\left( {{x}_{1} + {h}_{1},{x}_{2} + {h}_{2}}\right)  - {4f}\left( {{x}_{1} + 2{h}_{1},{x}_{2} + {h}_{2}}\right) }{4{h}_{1}{h}_{2}}
$$

$$
+ \frac{{3f}\left( {{x}_{1},{x}_{2} + 2{h}_{2}}\right)  - {4f}\left( {{x}_{1} + {h}_{1},{x}_{2} + 2{h}_{2}}\right)  + f\left( {{x}_{1} + 2{h}_{1},{x}_{2} + 2{h}_{2}}\right) }{4{h}_{1}{h}_{2}} + O\left( {h}_{1}^{2}\right)  + O\left( {h}_{2}^{2}\right)
$$

#### C.2.3 Higher-dimensional Examples

For illustrative purposes, we look at a 4-dimensional example.

Example 65 Difference approximation of $\frac{{\partial }^{4}f\left( {{x}_{1},{x}_{2},{x}_{3},{x}_{4}}\right) }{\partial {x}_{1}\partial {x}_{2}\partial {x}_{3}\partial {x}_{4}}$ , central difference of second order in ${x}_{1},{x}_{2},{x}_{3}$ , and ${x}_{4}$ .

We wish to compute the forward difference approximation of $\frac{{\partial }^{4}f\left( {{x}_{1},{x}_{2},{x}_{3},{x}_{4}}\right) }{\partial {x}_{1}\partial {x}_{2}\partial {x}_{3}\partial {x}_{4}}$ with $O\left( {h}_{1}^{2}\right)  +$ $O\left( {h}_{2}^{2}\right)  + O\left( {h}_{3}^{2}\right)  + O\left( {h}_{4}^{2}\right)$ . Thus we have ${d}_{1} = 1,{d}_{2} = 1,{d}_{3} = 1,{d}_{4} = 1$ , and ${p}_{1} = 2,{p}_{2} = 2$ , ${p}_{3} = 2,{p}_{4} = 2$ with

$$
{i}_{{l}_{1}} =  - \frac{1}{2}\left( {{d}_{1} + {p}_{1} - 1}\right)  =  - 1,{i}_{{u}_{1}} = \frac{1}{2}\left( {{d}_{1} + {p}_{1} - 1}\right)  = 1
$$

$$
{i}_{{l}_{2}} =  - \frac{1}{2}\left( {{d}_{2} + {p}_{2} - 1}\right)  =  - 1,{i}_{{u}_{2}} = \frac{1}{2}\left( {{d}_{2} + {p}_{2} - 1}\right)  = 1
$$

$$
{i}_{{l}_{3}} =  - \frac{1}{2}\left( {{d}_{3} + {p}_{3} - 1}\right)  =  - 1,{i}_{{u}_{3}} = \frac{1}{2}\left( {{d}_{3} + {p}_{3} - 1}\right)  = 1
$$

$$
{i}_{{l}_{4}} =  - \frac{1}{2}\left( {{d}_{4} + {p}_{4} - 1}\right)  =  - 1,{i}_{{u}_{4}} = \frac{1}{2}\left( {{d}_{4} + {p}_{4} - 1}\right)  = 1
$$

The constraint is then

$$
\mathop{\sum }\limits_{{{i}_{1} =  - 1}}^{1}\mathop{\sum }\limits_{{{i}_{1} =  - 1}}^{1}\mathop{\sum }\limits_{{{i}_{3} =  - 1}}^{1}\mathop{\sum }\limits_{{{i}_{4} =  - 1}}^{1}{c}_{{i}_{1},{i}_{2},{i}_{3},{i}_{4}}{i}_{1}^{{n}_{1}}{i}_{2}^{{n}_{2}}{i}_{3}^{{n}_{3}}{i}_{4}^{{n}_{4}} = \left\{  \begin{array}{ll} 1 & {n}_{1} = 1 \land  {n}_{2} = 1 \land  {n}_{3} = 1 \land  {n}_{4} = 1 \\  0 & \text{ otherwise } \end{array}\right.
$$

By utilizing Algorithm 42, we can set up $A$ and $b$ and solve for $c$ where

$$
\mathbf{c} = \left( \begin{matrix} {c}_{0} \\  {c}_{1} \\  \vdots \\  {c}_{N - 2} \\  {c}_{N - 1} \end{matrix}\right)
$$

as mentioned earlier $N = \left( {{d}_{1} + {p}_{1}}\right)  \times  \cdots  \times  \left( {{d}_{k} + {p}_{k}}\right)$ . To save space we just show non-zero elements of $c$ with the corresponding indices.

$$
\left\lbrack  \begin{matrix} {c}_{0} = \frac{1}{16}, & {c}_{2} =  - \frac{1}{16}, & {c}_{6} =  - \frac{1}{16}, & {c}_{8} = \frac{1}{16} \\  {c}_{18} =  - \frac{1}{16}, & {c}_{20} = \frac{1}{16}, & {c}_{24} = \frac{1}{16}, & {c}_{26} =  - \frac{1}{16} \\  {c}_{54} =  - \frac{1}{16}, & {c}_{56} =  - \frac{1}{16}, & {c}_{60} = \frac{1}{16}, & {c}_{62} =  - \frac{1}{16} \\  {c}_{72} = \frac{1}{16}, & {c}_{74} =  - \frac{1}{16}, & {c}_{78} =  - \frac{1}{16}, & {c}_{80} = \frac{1}{16} \end{matrix}\right\rbrack
$$

From the index of non-zero element, we should find the corresponding ${i}_{j}$ is ${x}_{j}$ -direction for $j = 1,\ldots ,4$ . Algorithm 43 demonstrates how to find the corresponding ${i}_{1},{i}_{2},\ldots ,{i}_{k}$ for a given index $I$ . For instance using Algorithm 43 we can see that in our example ${c}_{72}$ corresponds to ${i}_{1} = 1,{i}_{2} = 1,{i}_{3} =  - 1,{i}_{4} =  - 1$ .
```
Algorithm 43 Algorithm for finding the correpsonding index

---

Require: Set ${d}_{1},\ldots ,{d}_{k}$ and ${p}_{1},\ldots ,{p}_{k}$

Require: Set ${i}_{{l}_{j}}$ and ${i}_{{u}_{j}}$ for $j = 1,\ldots , k$

	$a \leftarrow  1$
	
	for $j = 2,\ldots , k$ do
	
			$a \leftarrow  a \times  \left( {{d}_{j} + {p}_{j} - 1}\right)$
	
	end for
	
	for $j = 2,\ldots , k$ do
	
			${i}_{j - 1} \leftarrow  \left\lfloor  \frac{I}{a}\right\rfloor$
	
			$I \leftarrow  I - {i}_{j - 1} \times  a$
	
			$a \leftarrow  \frac{a}{\left( {d}_{j} + {p}_{j} - 1\right) }$
	
	end for
	
	${i}_{k} \leftarrow  I$

---
```
## Appendix D Derivation of Characteristic Function

In this appendix, we show the derivation of characteristic function of exponential distribution and the characteristic function of Heston model. The approach for the derivation of the characteristic function of Heston model is pretty generic and can be utilized for other stochastic volatility models.

### D.1 Exponential Distribution — Characteristic Function of Exponential Distribution

Writing the charateristic function for exponential distribution

$$
\phi \left( u\right)  = \mathbb{E}\left( {e}^{iuX}\right)
$$

$$
= {\int }_{0}^{\infty }{e}^{iux}\lambda {e}^{-{\lambda x}}{dx}
$$

The integral may be evaluated by writing

$$
{e}^{iux} = \cos \left( {ux}\right)  + i\sin \left( {ux}\right)
$$

By doing this we get two integrals that be evaluated separately.

$$
\phi \left( u\right)  = \mathbb{E}\left( {e}^{iuX}\right)
$$

$$
= {\int }_{0}^{\infty }{e}^{iux}\lambda {e}^{-{\lambda x}}{dx}
$$

$$
= \lambda {\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} + {i\lambda }{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx} \tag{D.1}
$$

For the first integral

$$
{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx}
$$

We call

$$
{f}^{\prime }\left( x\right)  = \cos \left( {ux}\right)
$$

$$
g\left( x\right)  = {e}^{-{\lambda x}}
$$

by applying integration by parts, that is

$$
{\int }_{0}^{\infty }{f}^{\prime }\left( x\right) g\left( x\right) {dx} = {\left. f\left( x\right) g\left( x\right) \right| }_{0}^{\infty } - {\int }_{0}^{\infty }f\left( x\right) {g}^{\prime }\left( x\right) {dx}
$$

we get

$$
{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} = {\left. \frac{1}{u}\sin \left( ux\right) {e}^{-{\lambda x}}\right| }_{0}^{\infty } - {\int }_{0}^{\infty }\frac{1}{u}\sin \left( {ux}\right) \left( {-\lambda }\right) {e}^{-{\lambda x}}{dx}
$$

$$
= \frac{\lambda }{u}{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx} \tag{D.2}
$$

This time, we call

$$
{f}^{\prime }\left( x\right)  = \sin \left( {ux}\right)
$$

$$
g\left( x\right)  = {e}^{-{\lambda x}}
$$

and apply integration by parts more one more time to get

$$
\frac{\lambda }{u}{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx} = \frac{\lambda }{u}\left( {-{\left. \frac{1}{u}\cos \left( ux\right) {e}^{\lambda x}\right| }_{0}^{\infty } - {\int }_{0}^{\infty }\frac{1}{u}\cos \left( {ux}\right) \lambda {e}^{-{\lambda x}}{dx}}\right)
$$

$$
= \frac{\lambda }{u}\left( {\frac{1}{u} - \frac{\lambda }{u}{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx}}\right)
$$

$$
= \frac{\lambda }{{u}^{2}} - \frac{{\lambda }^{2}}{{u}^{2}}{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} \tag{D.3}
$$

Bu substituting (D.3) into (D.2) we get

$$
{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} = \frac{\lambda }{{u}^{2}} - \frac{{\lambda }^{2}}{{u}^{2}}{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} \tag{D.4}
$$

We recognize the expression in (D.4) is a linear equation as a function of the integral we are actually trying to evaluate, solving (D.4) for it and we get

$$
{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} = \frac{\lambda }{{\lambda }^{2} + {u}^{2}} \tag{D.5}
$$

From (D.2) we can imply

$$
{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx} = \frac{u}{\lambda }{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} \tag{D.6}
$$

and substituting (D.6) into (D.5) we get

$$
{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx} = \frac{u}{{\lambda }^{2} + {u}^{2}} \tag{D.7}
$$

Finally substituting both (D.7) and (D.5) into (D.1) we obtain

$$
\phi \left( u\right)  = \mathbb{E}\left( {e}^{iuX}\right)
$$

$$
= {\int }_{0}^{\infty }{e}^{iux}\lambda {e}^{-{\lambda x}}{dx}
$$

$$
= \lambda \left( {{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} + i{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx}}\right)
$$

$$
= \lambda \left( {\frac{\lambda }{{\lambda }^{2} + {u}^{2}} + i\frac{u}{{\lambda }^{2} + {u}^{2}}}\right)
$$

$$
= \frac{\lambda \left( {\lambda  + {iu}}\right) }{{\lambda }^{2} + {u}^{2}}
$$

$$
= \frac{\lambda \left( {\lambda  + {iu}}\right) }{\left( {\lambda  + {iu}}\right) \left( {\lambda  - {iu}}\right) }
$$

$$
= \frac{\lambda }{\lambda  - {iu}}
$$

which is the characteristic function of exponential distribution, in short

$$
\phi \left( u\right)  = \frac{\lambda }{\lambda  - {iu}}
$$

### D.2 Heston Model — Characteristic Function of the Log Asset Price

There are various different ways of deriving the characteristic function of Heston model, one of which is manifested in Problem 4 of Chapter 1. We provide an alternative derivation to its characteristic function in this appendix. This derivation is quite generic and can be used to derive the characteristic function of the log of asset prices under various different processes. Derivations similar to the one presented can be seen in [165] and [172].

The characteristic function for the log of the asset price under the Heston stochastic volatility model is given by

$$
\Phi \left( u\right)  = \mathbb{E}\left( {e}^{{iu}\ln {S}_{t}}\right)
$$

$$
= \frac{\exp \left\{  {{iu}\ln {S}_{0} + {iu}\left( {r - q}\right) t + \frac{{\kappa \theta t}\left( {\kappa  - {i\rho \sigma u}}\right) }{{\sigma }^{2}}}\right\}  }{{\left( \cosh \frac{\gamma t}{2} + \frac{\kappa  - {i\rho \sigma u}}{\gamma }\sinh \frac{\gamma t}{2}\right) }^{\frac{2\kappa \theta }{{\sigma }^{2}}}}\exp \left\{  \frac{-\left( {{u}^{2} + {iu}}\right) {v}_{0}}{\gamma \coth \frac{\gamma t}{2} + \kappa  - {i\rho \sigma u}}\right\}
$$

where $\gamma  = \sqrt{{\sigma }^{2}\left( {{u}^{2} + {iu}}\right)  + {\left( \kappa  - i\rho \sigma u\right) }^{2}}$ and ${S}_{0}$ and ${v}_{0}$ are the initial values for the price process and the volatility process, respectively.

To start, we define the joint characteristic function of $\left( {x, v}\right)$ at time $t,0 < t < T$ as

$$
\phi \left( {t,\xi ,\omega }\right)  = \mathbb{E}\left\lbrack  {{e}^{{i\xi }{x}_{T} + {i\omega }{v}_{T}} \mid  {x}_{t} = x,{v}_{t} = v}\right\rbrack   \tag{D.8}
$$

where $\left( {\xi ,\omega }\right)$ are the transform variables. It is conjectured that the characteristic function at time $t = 0$ has a solution of the form

$$
\phi \left( {0,\xi ,\omega }\right)  = {e}^{-a\left( T\right)  - b\left( T\right) x - c\left( T\right) v}
$$

Therefore by the Markov property it must be the case that

$$
\phi \left( {t,\xi ,\omega }\right)  = {e}^{-a\left( {T - t}\right)  - b\left( {T - t}\right) x - c\left( {T - t}\right) v}
$$

The first thing to notice is that evaluating this at $t = T$ gives the following boundary conditions:

$$
\phi \left( {T,\xi ,\omega }\right)  = {e}^{-a\left( 0\right)  - b\left( 0\right) x - c\left( 0\right) v}
$$

$$
= \mathbb{E}\left\lbrack  {{e}^{{i\xi }{x}_{T} + {i\omega }{v}_{T}} \mid  {x}_{T} = x,{v}_{T} = v}\right\rbrack
$$

$$
= {e}^{{i\xi x} + {i\omega v}}
$$

which implies

$$
a\left( 0\right)  = 0
$$

$$
b\left( 0\right)  =  - {i\xi }
$$

$$
c\left( 0\right)  =  - {i\omega }
$$

If we define $\mathcal{G}\left( t\right)$ to be

$$
\mathcal{G}\left( t\right)  = \phi \left( {t,\xi ,\omega }\right)  \tag{D.9}
$$

$\mathcal{G}\left( t\right)$ is a martingale because it is a conditional expectation of a terminal random variable. Therefore its derivative with respect to $t$ , the ${dt}$ term, must be identically zero.

As stated earlier, for the Heston stochastic volatility model, we assume that ${S}_{t}$ evolves according to the following SDE:

$$
d{S}_{t} = r{S}_{t}{dt} + \sqrt{{v}_{t}}{S}_{t}d{W}_{t}^{\left( 1\right) }
$$

$$
d{v}_{t} = \kappa \left( {\theta  - {v}_{t}}\right) {dt} + \sigma \sqrt{{v}_{t}}d{W}_{t}^{\left( 2\right) }
$$

We define ${x}_{t} = \ln {S}_{t} = F\left( {t,{S}_{t}}\right)$ and apply Itô’s lemma to derive $d{x}_{t}$ .

$$
d{x}_{t} = \frac{\partial F}{\partial t}{dt} + \frac{\partial F}{\partial {S}_{t}}d{S}_{t} + \frac{1}{2}\frac{{\partial }^{2}F}{\partial {S}_{t}^{2}}{\left( d{S}_{t}\right) }^{2}
$$

$$
= 0 + \frac{1}{{S}_{t}}\left( {r{S}_{t}{dt} + \sqrt{{v}_{t}}{S}_{t}d{W}_{t}^{\left( 1\right) }}\right)  - \frac{1}{2}\frac{1}{{S}_{t}^{2}}{\left( r{S}_{t}dt + \sqrt{{v}_{t}}{S}_{t}d{W}_{t}^{\left( 1\right) }\right) }^{2}
$$

$$
= {rdt} + \sqrt{{v}_{t}}d{W}_{t}^{\left( 1\right) } - \frac{1}{2}{v}_{t}{dt}
$$

$$
= \left( {r - \frac{1}{2}{v}_{t}}\right) {dt} + \sqrt{{v}_{t}}d{W}_{t}^{\left( 1\right) }
$$

where

$$
d{v}_{t} = \kappa \left( {\theta  - {v}_{t}}\right) {dt} + \sigma \sqrt{{v}_{t}}d{W}_{t}^{\left( 2\right) }
$$

Thus we have

$$
d{x}_{t} = \left( {r - \frac{1}{2}{v}_{t}}\right) {dt} + \sqrt{{v}_{t}}d{W}_{t}^{\left( 1\right) }
$$

$$
d{v}_{t} = \kappa \left( {\theta  - {v}_{t}}\right) {dt} + \sigma \sqrt{{v}_{t}}d{W}_{t}^{\left( 2\right) }
$$

The goal is to find

$$
{\mathbb{E}}_{t}^{\mathbb{Q}}\left( {e}^{{iu}\ln {S}_{T}}\right)  = {\mathbb{E}}_{t}^{\mathbb{Q}}\left( {e}^{{iu}{x}_{T}}\right)
$$

It is clear that $\phi \left( {t,\xi  = u,\omega  = 0}\right)  = \mathbb{E}\left\lbrack  {e}^{{iu}{x}_{T}}\right\rbrack$ . Because $\mathcal{G}\left( t\right)  = \phi \left( {t,\xi ,\omega }\right)$ is a martingale, we have

$$
d\mathcal{G}\left( t\right)  = \frac{\partial \mathcal{G}\left( t\right) }{\partial t}{dt} + \ldots
$$

$$
= {0dt} + \ldots
$$

because its derivatives with respect to time must be zero and this leads to the expression

$$
\frac{\partial \mathcal{G}\left( t\right) }{\partial t} = {\phi }_{t} + {\phi }_{x}\left( {r - \frac{1}{2}{v}_{t}}\right)  + {\phi }_{v}\left( {\kappa \left( {\theta  - {v}_{t}}\right) }\right)  \tag{D.10}
$$

$$
+ \frac{1}{2}\operatorname{Trace}\left( {{\phi }_{xx}{v}_{t}}\right)  + \frac{1}{2}{\phi }_{vv}{\sigma }^{2}{v}_{t} + \rho {\sigma }^{2}\left( t\right) {v}_{t}{\phi }_{xv} = 0
$$

As mentioned, it is conjectured that $\phi \left( {t,\xi ,\omega }\right)$ can be expressed as

$$
\phi \left( {t,\xi ,\varphi }\right)  = {e}^{-a\left( {T - t}\right)  - b\left( {T - t}\right) x - c\left( {T - t}\right) v}
$$

and therefore its derivatives would be

$$
{\phi }_{t} = \left( {{a}^{\prime }\left( {T - t}\right)  + {b}^{\prime }\left( {T - t}\right) x + {c}^{\prime }\left( {T - t}\right) v}\right) \phi
$$

$$
{\phi }_{x} =  - b\left( {T - t}\right) \phi
$$

$$
{\phi }_{v} =  - c\left( {T - t}\right) \phi
$$

$$
{\phi }_{xx} = {b}^{2}\left( {T - t}\right) \phi
$$

$$
{\phi }_{vv} = {c}^{2}\left( {T - t}\right) \phi
$$

$$
{\phi }_{vx} = b\left( {T - t}\right) c\left( {T - t}\right) \phi
$$

Substituting all derivatives into (D.10) we get

$$
\phi \left( {{a}^{\prime }\left( {T - t}\right)  + {b}^{\prime }\left( {T - t}\right) x + {c}^{\prime }\left( {T - t}\right) v - b\left( {T - t}\right) \left( {r - \frac{1}{2}v}\right) }\right.  \tag{D.11}
$$

$$
\left. {-c\left( {T - t}\right) \kappa \left( {\theta  - v}\right)  + \frac{1}{2}{b}^{2}\left( {T - t}\right) v + \frac{1}{2}{c}^{2}\left( {T - t}\right) {\sigma }^{2}v + {\rho \sigma vb}\left( {T - t}\right) c\left( {T - t}\right) }\right)  = 0
$$

Since this holds for all $\left( {x, v}\right)$ , we get three simpler equations, namely, the Riccati equations, by grouping $x, v$ , and the remaining terms

$$
\left\{  \begin{array}{l} {a}^{\prime }\left( {T - t}\right)  - c\left( {T - t}\right) {\kappa \theta } - {rb}\left( {T - t}\right)  = 0 \\  {b}^{\prime }\left( {T - t}\right)  = 0 \\  {c}^{\prime }\left( {T - t}\right)  + \frac{1}{2}b\left( {T - t}\right)  + c\left( {T - t}\right) \kappa  + \frac{1}{2}{b}^{2}\left( {T - t}\right)  + \frac{1}{2}{c}^{2}\left( {T - t}\right) {\sigma }^{2} + {\rho \sigma b}\left( {T - t}\right) c\left( {T - t}\right)  = 0 \end{array}\right.
$$

Define $\tau  = T - t$ and we get

$$
\left\{  \begin{array}{l} {a}^{\prime }\left( \tau \right)  - c\left( \tau \right) {\kappa \theta } - {rb}\left( \tau \right)  = 0 \\  {b}^{\prime }\left( \tau \right)  = 0 \\  {c}^{\prime }\left( \tau \right)  + \frac{1}{2}b\left( \tau \right)  + c\left( \tau \right) \kappa  + \frac{1}{2}{b}^{2}\left( \tau \right)  + \frac{1}{2}{c}^{2}\left( \tau \right) {\sigma }^{2} + {\rho \sigma b}\left( \tau \right) c\left( \tau \right)  = 0 \end{array}\right.
$$

The second Riccati equation, ${b}^{\prime }\left( \tau \right)  = 0$ , implies that $b\left( \tau \right)$ is constant and the boundary condition implies

$$
b\left( \tau \right)  =  - {i\xi }
$$

Substituting it in the third equation we have

$$
{c}^{\prime }\left( \tau \right)  = \frac{1}{2}{i\xi } - c\left( \tau \right) \kappa  - \frac{1}{2}{\left( -i\xi \right) }^{2} - \frac{1}{2}{c}^{2}\left( \tau \right) {\sigma }^{2} - {\rho \sigma }\left( {-{i\xi }}\right) c\left( \tau \right)
$$

$$
=  - \frac{1}{2}{\sigma }^{2}{c}^{2}\left( \tau \right)  + \left( {{i\xi \rho \sigma } - \kappa }\right) c\left( \tau \right)  + \left( {\frac{1}{2}{i\xi } + \frac{1}{2}{\xi }^{2}}\right)
$$

$$
\frac{{dc}\left( \tau \right) }{d\tau } =  - \frac{1}{2}{\sigma }^{2}\left\lbrack  {{c}^{2}\left( \tau \right)  + \frac{2}{{\sigma }^{2}}\left( {\kappa  - {i\xi \rho \sigma }}\right) c\left( \tau \right)  - \frac{{i\xi } + {\xi }^{2}}{{\sigma }^{2}}}\right\rbrack
$$

$$
\frac{{dc}\left( \tau \right) }{{c}^{2}\left( \tau \right)  + \frac{2}{{\sigma }^{2}}\left( {\kappa  - {i\xi \rho \sigma }}\right) c\left( \tau \right)  - \frac{{i\xi } + {\xi }^{2}}{{\sigma }^{2}}} =  - \frac{1}{2}{\sigma }^{2}{d\tau }
$$

We solve this equation using partial fractions. The roots of the equation in the denominator

$$
{c}^{2}\left( \tau \right)  + \frac{2}{{\sigma }^{2}}\left( {\kappa  - {i\xi \rho \sigma }}\right) c\left( \tau \right)  - \frac{{i\xi } + {\xi }^{2}}{{\sigma }^{2}}
$$

are

$$
{c}_{1} = \frac{\beta  - \gamma }{{\sigma }^{2}}
$$

$$
{c}_{2} = \frac{\beta  + \gamma }{{\sigma }^{2}}
$$

where

$$
\beta  = \kappa  - {i\xi \rho \sigma }
$$

$$
\gamma  = \sqrt{{\left( \kappa  - i\xi \rho \sigma \right) }^{2} + {\sigma }^{2}\left( {{\xi }^{2} + {i\xi }}\right) }
$$

We can find $A$ and $B$ such that

$$
\frac{1}{{c}^{2}\left( \tau \right)  + \frac{2}{{\sigma }^{2}}\left( {\kappa  - {i\xi \rho \sigma }}\right) c\left( \tau \right)  - \frac{{i\xi } + {\xi }^{2}}{{\sigma }^{2}}} = \frac{A}{c\left( \tau \right)  - {c}_{1}} + \frac{B}{c\left( \tau \right)  - {c}_{2}}
$$

We see that $A$ and $B$ should satisfy the following equation:

$$
A\left( {c\left( \tau \right)  - \frac{\beta  - \gamma }{{\sigma }^{2}}}\right)  + B\left( {c\left( \tau \right)  - \frac{\beta  + \gamma }{{\sigma }^{2}}}\right)  = 1
$$

Or equivalently

$$
A + B = 0
$$

$$
- A\left( {\beta  - \gamma }\right)  - B\left( {\beta  + \gamma }\right)  = {\sigma }^{2}
$$

and we get $A = \frac{{\sigma }^{2}}{2\sigma }$ and $B =  - \frac{{\sigma }^{2}}{2\sigma }$ . Now substituting and integrating we get

$$
\int \frac{\frac{{\sigma }^{2}}{2\gamma }}{c\left( \tau \right)  - \frac{\beta  + \gamma }{{\sigma }^{2}}}{dc}\left( \tau \right)  + \int \frac{-\frac{{\sigma }^{2}}{2\gamma }}{c\left( \tau \right)  - \frac{\beta  - \gamma }{{\sigma }^{2}}}{dc}\left( \tau \right)  =  - \frac{1}{2}{\sigma }^{2}\tau  + \text{ constant }
$$

$$
\frac{{\sigma }^{2}}{2\gamma }\ln \left( {c\left( \tau \right)  - \frac{-\beta  + \gamma }{{\sigma }^{2}}}\right)  - \frac{{\sigma }^{2}}{2\gamma }\ln \left( {c\left( \tau \right)  - \frac{-\beta  - \gamma }{{\sigma }^{2}}}\right)  =  - \frac{1}{2}{\sigma }^{2}\tau  + \text{ constant }
$$

or

$$
\ln \left( \frac{c\left( \tau \right)  - \frac{-\beta  + \gamma }{{\sigma }^{2}}}{c\left( \tau \right)  - \frac{-\beta  - \gamma }{{\sigma }^{2}}}\right)  =  - {\gamma \tau } + \text{ constant }
$$

$$
\frac{c\left( \tau \right)  - \frac{-\beta  + \gamma }{{\sigma }^{2}}}{c\left( \tau \right)  - \frac{-\beta  - \gamma }{{\sigma }^{2}}} = \alpha {e}^{-{\gamma \tau }} \tag{D.12}
$$

The boundary condition for $c\left( \tau \right)$ is

$$
c\left( {\tau  = 0}\right)  = c\left( 0\right)  =  - {i\varphi } =  - i\left( 0\right)  = 0
$$

Applying this we obtain

$$
\alpha  = \frac{0 - \frac{-\beta  + \gamma }{{\sigma }^{2}}}{0 - \frac{-\beta  - \gamma }{{\sigma }^{2}}} = \frac{\beta  - \gamma }{\beta  + \gamma }
$$

We substitute this back into (D.12) and solve for $c\left( \tau \right)$ .

$$
c\left( \tau \right)  = \frac{\gamma  - \beta }{{\sigma }^{2}}\frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}
$$

Having $c\left( \tau \right)$ , we can solve for $a\left( \tau \right)$ .

$$
{a}^{\prime }\left( \tau \right)  = c\left( \tau \right) {\kappa \theta } + {rb}\left( \tau \right)
$$

$$
= {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}} - {i\xi r}
$$

$$
a\left( \tau \right)  = {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\int \frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}{d\tau } - {i\xi r}\int {d\tau }
$$

$$
= {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\int \frac{1}{1 - \alpha {e}^{-{\gamma \tau }}}{d\tau }-\int \frac{{e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}{d\tau }}\right\rbrack   - {i\xi r}\int {d\tau }
$$

$$
= {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\tau  + \frac{1}{\gamma }\ln \left( {1 - \alpha {e}^{-{\gamma \tau }}}\right)  - \frac{1}{\alpha \gamma }\ln \left( {1 - \alpha {e}^{-{\gamma \tau }}}\right) }\right\rbrack   - {i\xi r\tau } + \text{ constant }
$$

$$
= {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\tau  + \ln {\left( 1 - \alpha {e}^{-{\gamma \tau }}\right) }^{\frac{\alpha  - 1}{\alpha \gamma }}}\right\rbrack   - {iu\xi r\tau } + \text{ constant }
$$

To find the constant, we know that $a\left( {\tau  = 0}\right)  = 0$ and that implies

$$
a\left( 0\right)  = {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {0 + \ln {\left( 1 - \alpha \right) }^{\frac{\alpha  - 1}{\alpha \gamma }}}\right\rbrack   + \text{ constant } = 0
$$

and we obtain

$$
\text{ constant } =  - {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\ln {\left( 1 - \alpha \right) }^{\frac{\alpha  - 1}{\alpha \gamma }}}\right\rbrack
$$

Substituting it into $a\left( \tau \right)$ we get

$$
a\left( \tau \right)  = {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\tau  + \ln {\left( \frac{1 - \alpha {e}^{-{\gamma \tau }}}{1 - \alpha }\right) }^{\frac{\alpha  - 1}{\alpha \gamma }}}\right\rbrack   - {iur\tau }
$$

Now that we have all loadings $a\left( \tau \right) , b\left( \tau \right)$ , and $c\left( \tau \right)$ explicitly we can calculate the characteristic function

$$
\mathbb{E}\left( {e}^{{iu}{x}_{T}}\right)  = \phi \left( {t = 0,\xi  = u,\omega  = 0}\right)
$$

$$
= {e}^{-a\left( \tau \right)  - b\left( \tau \right) {x}_{0} - c\left( \tau \right) {v}_{0}}
$$

where

$$
a\left( \tau \right)  = {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\tau  + \ln {\left( \frac{1 - \alpha {e}^{-{\gamma \tau }}}{1 - \alpha }\right) }^{\frac{\alpha  - 1}{\alpha \gamma }}}\right\rbrack   - {iur\tau }
$$

$$
b\left( \tau \right)  =  - {iu}
$$

$$
c\left( \tau \right)  = \frac{\gamma  - \beta }{{\sigma }^{2}}\frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}
$$

and $\beta  = \kappa  - {iu\rho \sigma },\gamma  = \sqrt{{\left( \kappa  - i\xi \rho \sigma \right) }^{2} + {\sigma }^{2}\left( {{\xi }^{2} + {i\xi }}\right) }$ , and $\alpha  = \frac{\beta  - \gamma }{\beta  + \gamma }$ . Thus the full characteristic function is as follows:

$$
{\mathbb{E}}_{t}\left( {e}^{{iu}{x}_{T}}\right)  = \exp \left\{  {-{\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\tau  - \ln {\left( \frac{1 - \alpha {e}^{-{\gamma \tau }}}{1 - \alpha }\right) }^{{\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\frac{\alpha  - 1}{\alpha \gamma }}}\right\}
$$

$$
\times  \;\exp \left\{  {{iur\tau } + {iu}{x}_{t} - \frac{\gamma  - \beta }{{\sigma }^{2}}\frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}{v}_{t}}\right\}
$$

$$
= \exp \left\{  {-{\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\tau  - \ln {\left( \frac{1 - \alpha {e}^{-{\gamma \tau }}}{1 - \alpha }\right) }^{\frac{2\kappa \theta }{{\sigma }^{2}}} + {iur\tau } + {iu}{x}_{t}}\right\}
$$

$$
\times  \;\exp \left\{  {-\frac{\gamma  - \beta }{{\sigma }^{2}}\frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}{v}_{t}}\right\}
$$

$$
= \exp \left\{  {{\kappa \theta \tau }\frac{\beta }{{\sigma }^{2}} + {iu}{x}_{t} + {iur\tau }}\right\}
$$

$$
\times  \exp \left\{  {-\ln {\left( \frac{1 - \alpha {e}^{-{\gamma \tau }}}{1 - \alpha }\right) }^{\frac{2\kappa \theta }{{\sigma }^{2}}} - {\kappa \theta \tau }\frac{\gamma }{{\sigma }^{2}}}\right\}
$$

$$
\times  \exp \left\{  {-\frac{\gamma  - \beta }{{\sigma }^{2}}\frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}{v}_{t}}\right\}   \tag{D.13}
$$

The last term in Equation (D.13) can be simplified as follows:

$$
\exp \left\{  {\frac{\beta  - \gamma }{{\sigma }^{2}}\frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}{v}_{t}}\right\}   = \exp \left\{  {\frac{{\beta }^{2} - {\gamma }^{2}}{\beta  + \gamma }\frac{1}{{\sigma }^{2}}\frac{{e}^{\gamma \tau }\left( {1 - {e}^{-{\gamma \tau }}}\right) }{{e}^{\gamma \tau }\left( {1 - \alpha {e}^{-{\gamma \tau }}}\right) }{v}_{t}}\right\}
$$

$$
= \exp \left\{  {-\frac{{u}^{2} + {iu}}{\beta  + \gamma }\frac{{e}^{\gamma \tau } - 1}{{e}^{\gamma \tau } - \alpha }{v}_{t}}\right\}
$$

$$
= \exp \left\{  {-\left( {{u}^{2} + {iu}}\right) {v}_{t}\frac{{e}^{\gamma \tau } - 1}{{e}^{\gamma \tau } - \frac{\beta  - \gamma }{\beta  + \gamma }}\frac{1}{\beta  + \gamma }}\right\}
$$

$$
= \exp \left\{  {-\left( {{u}^{2} + {iu}}\right) {v}_{t}\frac{{e}^{\gamma \tau } - 1}{\beta \left( {{e}^{\gamma \tau } - 1}\right)  + \gamma \left( {{e}^{\gamma \tau } + 1}\right) }}\right\}
$$

$$
= \exp \left\{  {-\left( {{u}^{2} + {iu}}\right) {v}_{t}\frac{1}{\frac{\beta \left( {{e}^{\gamma \tau } - 1}\right)  + \gamma \left( {{e}^{\gamma \tau } + 1}\right) }{{e}^{\gamma \tau } - 1}}}\right\}
$$

$$
= \exp \left\{  {-\left( {{u}^{2} + {iu}}\right) {v}_{t}\frac{1}{\gamma \frac{{e}^{\gamma \tau } + 1}{{e}^{\gamma \tau } - 1} + \beta }}\right\}
$$

$$
= \exp \left\{  {-\frac{\left( {{u}^{2} + {iu}}\right) {v}_{t}}{\gamma \coth \frac{\gamma \tau }{2} + \beta }}\right\}
$$

In addition, the second to last term in Equation (D.13) can also be simplified.

$$
\exp \left\{  {-\ln {\left( \frac{1 - \alpha {e}^{-{\gamma \tau }}}{1 - \alpha }\right) }^{\frac{2\kappa \theta }{{\sigma }^{2}}} - \frac{\kappa \theta }{{\sigma }^{2}}{\gamma \tau }}\right\}   = {\left( {e}^{\frac{\gamma \tau }{2}}\frac{1 - \alpha {e}^{-{\gamma \tau }}}{1 - \alpha }\right) }^{-\frac{2\kappa \theta }{{\sigma }^{2}}}
$$

$$
= {\left( {e}^{\frac{\gamma \tau }{2}}\frac{1 - \alpha {e}^{-{\gamma \tau }}}{\frac{2\gamma }{\gamma  + \beta }}\right) }^{-\frac{2\kappa \theta }{{\sigma }^{2}}}
$$

$$
= {\left( \frac{\left( {\gamma  + \beta }\right) {e}^{\frac{\gamma \tau }{2}}}{2\gamma }\left( 1 - \alpha {e}^{-{\gamma \tau }}\right) \right) }^{-\frac{2\kappa \theta }{{\sigma }^{2}}}
$$

$$
= {\left( \frac{\left( {\gamma  + \beta }\right) {e}^{\frac{\gamma \tau }{2}} + \left( {\gamma  - \beta }\right) {e}^{\frac{-{\gamma \tau }}{2}}}{2\gamma }\right) }^{-\frac{2\kappa \theta }{{\sigma }^{2}}}
$$

$$
= {\left( \frac{\gamma \left( {{e}^{\frac{\gamma \tau }{2}} + {e}^{\frac{\gamma \tau }{2}}}\right)  + \beta \left( {{e}^{\frac{\gamma \tau }{2}} - {e}^{\frac{\gamma \tau }{2}}}\right) }{2\gamma }\right) }^{-\frac{2\kappa \theta }{{\sigma }^{2}}}
$$

$$
= {\left( \cosh \frac{\gamma \tau }{2} + \frac{\beta }{\gamma }\sinh \frac{\gamma \tau }{2}\right) }^{-\frac{2\kappa \theta }{{\sigma }^{2}}}
$$

Putting them all together we get

$$
{\mathbb{E}}_{t}\left( {e}^{{iu}\ln {S}_{T}}\right)  = \frac{\exp \left\{  {{iu}\ln {S}_{t} + {iu}\left( {r - q}\right) \tau  + {\kappa \theta \tau }\frac{\beta }{{\sigma }^{2}}}\right\}   \times  \exp \left\{  \frac{-\left( {{u}^{2} + {iu}}\right) {v}_{t}}{\gamma \coth \frac{\gamma \tau }{2} + \beta }\right\}  }{{\left( \cosh \frac{\gamma \tau }{2} + \frac{\beta }{\gamma }\sinh \frac{\gamma \tau }{2}\right) }^{\frac{2\kappa \theta }{{\sigma }^{2}}}}
$$

## Appendix E Evaluation of the PIDE

This appendix will delve into the evaluation of the partial integro-differential equation (PIDE) in an unsupervised deep learning approach to solving PIDEs introduced in Chapter 8.

### E.1 Split of the Integral in the PIDE

As mentioned earlier, this part mostly follows the derivations in Chapter 5. We split the integral term in Equation (8.1) into two parts, the integrals on $\left\{  {-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\right\}$ and $\left\{  {y <  - {\epsilon }^{ - }}\right.$ or $\left. {y > {\epsilon }^{ + }}\right\}$ respectively.

In the region $\left\{  {-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\right\}$ ,

$$
w\left( {x + y,\tau }\right)  = w\left( {x,\tau }\right)  + y\frac{\partial w}{\partial x}\left( {x,\tau }\right)  + \frac{{y}^{2}}{2}\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right)  + O\left( {y}^{3}\right)
$$

and

$$
{e}^{y} = 1 + y + \frac{{y}^{2}}{2} + O\left( {y}^{3}\right) .
$$

Using those two approximations, we get

$$
{\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right)  - \frac{\partial w}{\partial x}\left( {x,\tau }\right) \left( {{e}^{y} - 1}\right) }\right) m\left( {dy}\right)
$$

$$
= {\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\left( {\frac{{y}^{2}}{2}\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right)  - \frac{{y}^{2}}{2}\frac{\partial w}{\partial x}\left( {x,\tau }\right)  + O\left( {y}^{3}\right) }\right) m\left( {dy}\right)
$$

$$
\approx  {\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\left( {\frac{{y}^{2}}{2}\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right)  - \frac{{y}^{2}}{2}\frac{\partial w}{\partial x}\left( {x,\tau }\right) }\right) m\left( {dy}\right) .
$$

Define ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = {\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}{y}^{2}m\left( {dy}\right)$ and we get

$$
{\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right)  - \frac{\partial w}{\partial x}\left( {x,\tau }\right) \left( {{e}^{y} - 1}\right) }\right) m\left( {dy}\right)
$$

$$
\approx  \frac{1}{2}{\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right) \left( {\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right)  - \frac{\partial w}{\partial x}\left( {x,\tau }\right) }\right) .
$$

In the region $\left\{  {y <  - {\epsilon }^{ - }}\right.$ or $\left. {y > {\epsilon }^{ + }}\right\}$ ,

$$
{\int }_{y <  - {\epsilon }^{ - }\text{or }y > {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right)  - \frac{\partial w}{\partial x}\left( {x,\tau }\right) \left( {{e}^{y} - 1}\right) }\right) m\left( {dy}\right)
$$

$$
= {\int }_{y <  - {\epsilon }^{ - }\text{or }y > {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right) }\right) m\left( {dy}\right)  + \frac{\partial w}{\partial x}\left( {x,\tau }\right) \omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right) ,
$$

where $\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = {\int }_{y <  - {\epsilon }^{ - }\text{or }y > {\epsilon }^{ + }}\left( {1 - {e}^{y}}\right) m\left( {dy}\right)$ . DOI: 10.1201/9780429094743-E Combining the two parts of integrals and putting them back to Equation (8.1), we get

$$
\left( {{\int }_{y <  - {\epsilon }^{ - }\text{or }y > {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right) }\right) m\left( {dy}\right)  + \frac{{s}^{2} + {\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right) }{2}\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right) }\right.  \tag{E.1}
$$

$$
\left. {-\frac{\partial w}{\partial \tau }\left( {x,\tau }\right)  + \left( {r - q - \frac{{s}^{2} + {\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right) }{2} + \omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right) }\right) \frac{\partial w}{\partial x}\left( {x,\tau }\right)  - {rw}\left( {x,\tau }\right) }\right)  = 0.
$$

TABLE E.1: ${\epsilon }^{ - },{\epsilon }^{ + },{\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ and $\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ for each model

<table><tr><td>Model</td><td>${\epsilon }^{ - }$</td><td>${\epsilon }^{ + }$</td><td>${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$</td><td>$\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$</td></tr><tr><td>VG</td><td>0.02/G</td><td>0.02/M</td><td>${\sigma }_{CGMY}^{2}\left( {C, G, M,0,{\epsilon }^{ - },{\epsilon }^{ + }}\right)$</td><td>${\omega }_{CGMY}\left( {C, G, M,0,{\epsilon }^{ - },{\epsilon }^{ + }}\right)$</td></tr><tr><td>CGMY</td><td>0.01/G</td><td>0.01/M</td><td>${\sigma }_{CGMY}^{2}\left( {C, G, M, Y,{\epsilon }^{ - },{\epsilon }^{ + }}\right)$</td><td>${\omega }_{CGMY}\left( {C, G, M, Y,{\epsilon }^{ - },{\epsilon }^{ + }}\right)$</td></tr><tr><td>NIG</td><td>0.05/α</td><td>0.05/α</td><td>-</td><td>-</td></tr><tr><td>Merton's</td><td>0</td><td>0</td><td>0</td><td>$- \lambda \left( {\exp \left( {\alpha  + {\delta }^{2}/2}\right)  - 1}\right)$</td></tr><tr><td>Kou's</td><td>0</td><td>0</td><td>0</td><td>$- \lambda \left( {\frac{p{\eta }_{1}}{{\eta }_{1} - 1} + \frac{\left( {1 - p}\right) {\eta }_{2}}{{\eta }_{2} + 1} - 1}\right)$</td></tr></table>

In Equation (E.1), the function $w\left( {x,\tau }\right)$ as well as its derivatives $\frac{\partial w}{\partial x}\left( {x,\tau }\right) ,\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right)$ and $\frac{\partial w}{\partial \tau }\left( {x,\tau }\right)$ can be calculated by the neural network itself or the back-propagation of the neural network. Then the terms remaining to be calculated are ${\int }_{y <  - {\epsilon }^{ - }\text{or }y > {\epsilon }^{ + }}(w\left( {x + y,\tau }\right)$ $- w\left( {x,\tau }\right) )m\left( {dy}\right) ,{\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ and $\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ .

### E.2 Pre-calculations

In Table E.1, we list the choice of ${\epsilon }^{ - },{\epsilon }^{ + }$ and the expressions of ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ , and $\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ for each model. ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ and $\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ are calculated before training.

where

$$
{\sigma }_{CGMY}^{2}\left( {C, G, M, Y,{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = C{G}^{Y - 2}\left( {\Gamma \left( {2 - Y}\right)  - \Gamma \left( {2 - Y, G{\epsilon }^{ - }}\right) }\right)
$$

$$
+ C{M}^{Y - 2}\left( {\Gamma \left( {2 - Y}\right)  - \Gamma \left( {2 - Y, M{\epsilon }^{ + }}\right) }\right) ,
$$

and

$$
{\omega }_{CGMY}\left( {C, G, M, Y,{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = C\left( {{M}^{Y}\Gamma \left( {-Y, M{\epsilon }^{ + }}\right)  - {\left( M - 1\right) }^{Y} * \Gamma \left( {-Y,\left( {M - 1}\right) {\epsilon }^{ + }}\right) }\right)
$$

$$
+ C\left( {{G}^{Y}\Gamma \left( {-Y, G{\epsilon }^{ - }}\right)  - {\left( G + 1\right) }^{Y}\Gamma \left( {-Y,\left( {G + 1}\right) {\epsilon }^{ - }}\right) }\right) .
$$

$M$ and $G$ follow the definitions in Equation (1.45) and (1.46) and $C = 1/\nu .\Gamma \left( \cdot \right)$ is the gamma function and $\Gamma \left( {\cdot , \cdot  }\right)$ is the incomplete gamma function following the definition

$$
\Gamma \left( {s, y}\right)  = {\int }_{y}^{\infty }{u}^{s - 1}{e}^{-u}{du}.
$$

${\epsilon }^{ + }$ and ${\epsilon }^{ - }$ could be dependent on the model parameters. For the NIG model, we do not have the closed-form expressions of ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ and $\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ and they are calculated using numerical integration in scipy. ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = 0$ in the Merton’s model and the Kou’s model since ${\epsilon }^{ + } = {\epsilon }^{ - } = 0$ .

TABLE E.2: Relationship between the scaled grid points ${y}_{j}$ and fixed grid points ${z}_{j}$

<table><tr><td>Model</td><td>${y}_{j}$ in the negative part</td><td>${y}_{j}$ in the positive part</td></tr><tr><td>VG</td><td>$- {z}_{j}/G$</td><td>${z}_{j}/M$</td></tr><tr><td>CGMY</td><td>$- {z}_{j}/G$</td><td>${z}_{j}/M$</td></tr><tr><td>NIG</td><td>$- {z}_{j}/\alpha$</td><td>${z}_{j}/\alpha$</td></tr><tr><td>Merton's</td><td>$\alpha  - \delta {z}_{j}$</td><td>$\alpha  + \delta {z}_{j}$</td></tr><tr><td>Kou's</td><td>$- {z}_{j}/{\eta }_{2}$</td><td>${z}_{j}/{\eta }_{1}$</td></tr></table>

### E.3 Numerical Integral

The integral ${\int }_{y <  - {\epsilon }^{ - }\text{or }y > {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right) }\right) m\left( {dy}\right)$ is calculated using the Simpson’s rule [296]. If there are ${2N} + 1$ grid points ${y}_{0},{y}_{1},\ldots ,{y}_{2N}$ , which satisfy $2{y}_{{2j} + 1} = {y}_{2j} +$ ${y}_{{2j} + 2},\forall 0 \leq  j \leq  N - 1$ and ${y}_{0} = {\epsilon }^{ + }$ , the numerical integral is

$$
{\int }_{y > {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right) }\right) m\left( {dy}\right)
$$

$$
= {\int }_{y > {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right) }\right) k\left( y\right) {dy}
$$

$$
\approx  \mathop{\sum }\limits_{{j = 0}}^{{N - 1}}\left( {w\left( {x + {y}_{2j},\tau }\right)  - w\left( {x,\tau }\right) }\right) k\left( {y}_{2j}\right) \frac{{y}_{{2j} + 2} - {y}_{2j}}{6} +
$$

$$
+ \mathop{\sum }\limits_{{j = 0}}^{{N - 1}}\left( {w\left( {x + {y}_{{2j} + 1},\tau }\right)  - w\left( {x,\tau }\right) }\right) k\left( {y}_{{2j} + 1}\right) \frac{2\left( {{y}_{{2j} + 2} - {y}_{2j}}\right) }{3}
$$

$$
+ \mathop{\sum }\limits_{{j = 0}}^{{N - 1}}\left( {w\left( {x + {y}_{{2j} + 2},\tau }\right)  - w\left( {x,\tau }\right) }\right) k\left( {y}_{{2j} + 2}\right) \frac{{y}_{{2j} + 2} - {y}_{2j}}{6}
$$

,

which is a linear combination of the values of $w\left( {\cdot ,\tau }\right)$ . The integral on $\left\{  {y <  - {\epsilon }^{ - }}\right\}$ is calculated in the same way.

Since the shape of $k\left( y\right)$ depends on the model parameters, it is not efficient if we use the same integral grid for different sample points. Take the Merton's model as an example, where

$$
k\left( y\right)  = \frac{\lambda }{\sqrt{2\pi }\delta }{e}^{-{\left( x - \alpha \right) }^{2}/\left( {2{\delta }^{2}}\right) }
$$

The density function has a center parameter $\alpha$ and a scale parameter $\delta$ . If we define the integral grid points to be ${y}_{j} = \alpha  + \delta {z}_{j},\forall 0 \leq  j \leq  {2N}$ , where ${z}_{j}$ ’s are fixed, we will assign enough grid points around the peak of $k\left( y\right)$ whatever the model parameters and the integral will be more accurate. For other models, the density $k\left( y\right)$ is centered around 0, but it decreases at different rates when the model parameters are different. So we always use a scaled integral grid. In Table E.2, we list the relationship between the scaled grid points ${y}_{j}$ and fixed gird points $0 \leq  {z}_{0} \leq  {z}_{1} \leq  \cdots  \leq  {z}_{2N}$ used for integral. The values of ${z}_{j}$ can be found at https://github.com/weilong-columbia/pide.
