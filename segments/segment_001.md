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