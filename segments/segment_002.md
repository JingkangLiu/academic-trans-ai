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