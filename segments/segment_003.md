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