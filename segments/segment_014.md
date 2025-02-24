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