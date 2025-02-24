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