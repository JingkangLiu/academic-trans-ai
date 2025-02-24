$$
\Phi \left( u\right)  = \mathbb{E}\left( {e}^{{iu}\ln {S}_{t}}\right)
$$

$$
\Phi \left( u\right)  = \mathbb{E}\left( {e}^{{iu}\ln {S}_{t}}\right)
$$

$$
= \frac{\exp \left\{  {{iu}\ln {S}_{0} + {iu}\left( {r - q}\right) t + \frac{{\kappa \theta t}\left( {\kappa  - {i\rho \sigma u}}\right) }{{\sigma }^{2}}}\right\}  }{{\left( \cosh \frac{\gamma t}{2} + \frac{\kappa  - {i\rho \sigma u}}{\gamma }\sinh \frac{\gamma t}{2}\right) }^{\frac{2\kappa \theta }{{\sigma }^{2}}}}\exp \left\{  \frac{-\left( {{u}^{2} + {iu}}\right) {v}_{0}}{\gamma \coth \frac{\gamma t}{2} + \kappa  - {i\rho \sigma u}}\right\}
$$

$$
= \frac{\exp \left\{  {{iu}\ln {S}_{0} + {iu}\left( {r - q}\right) t + \frac{{\kappa \theta t}\left( {\kappa  - {i\rho \sigma u}}\right) }{{\sigma }^{2}}}\right\}  }{{\left( \cosh \frac{\gamma t}{2} + \frac{\kappa  - {i\rho \sigma u}}{\gamma }\sinh \frac{\gamma t}{2}\right) }^{\frac{2\kappa \theta }{{\sigma }^{2}}}}\exp \left\{  \frac{-\left( {{u}^{2} + {iu}}\right) {v}_{0}}{\gamma \coth \frac{\gamma t}{2} + \kappa  - {i\rho \sigma u}}\right\}
$$

where $\gamma  = \sqrt{{\sigma }^{2}\left( {{u}^{2} + {iu}}\right)  + {\left( \kappa  - i\rho \sigma u\right) }^{2}}$ and ${S}_{0}$ and ${v}_{0}$ are the initial values for the price process and the volatility process, respectively.

where $\gamma  = \sqrt{{\sigma }^{2}\left( {{u}^{2} + {iu}}\right)  + {\left( \kappa  - i\rho \sigma u\right) }^{2}}$ and ${S}_{0}$ and ${v}_{0}$ are the initial values for the price process and the volatility process, respectively.

$$
\phi \left( {t,\xi ,\omega }\right)  = \mathbb{E}\left\lbrack  {{e}^{{i\xi }{x}_{T} + {i\omega }{v}_{T}} \mid  {x}_{t} = x,{v}_{t} = v}\right\rbrack   \tag{D.8}
$$

$$
\phi \left( {t,\xi ,\omega }\right)  = \mathbb{E}\left\lbrack  {{e}^{{i\xi }{x}_{T} + {i\omega }{v}_{T}} \mid  {x}_{t} = x,{v}_{t} = v}\right\rbrack   \tag{D.8}
$$

where $\left( {\xi ,\omega }\right)$ are the transform variables. It is conjectured that the characteristic function at time $t = 0$ has a solution of the form

where $\left( {\xi ,\omega }\right)$ are the transform variables. It is conjectured that the characteristic function at time $t = 0$ has a solution of the form

$$
\phi \left( {0,\xi ,\omega }\right)  = {e}^{-a\left( T\right)  - b\left( T\right) x - c\left( T\right) v}
$$

$$
\phi \left( {0,\xi ,\omega }\right)  = {e}^{-a\left( T\right)  - b\left( T\right) x - c\left( T\right) v}
$$

Therefore by the Markov property it must be the case that

Therefore by the Markov property it must be the case that

$$
\phi \left( {t,\xi ,\omega }\right)  = {e}^{-a\left( {T - t}\right)  - b\left( {T - t}\right) x - c\left( {T - t}\right) v}
$$

$$
\phi \left( {t,\xi ,\omega }\right)  = {e}^{-a\left( {T - t}\right)  - b\left( {T - t}\right) x - c\left( {T - t}\right) v}
$$

The first thing to notice is that evaluating this at $t = T$ gives the following boundary conditions:

The first thing to notice is that evaluating this at $t = T$ gives the following boundary conditions:

$$
\phi \left( {T,\xi ,\omega }\right)  = {e}^{-a\left( 0\right)  - b\left( 0\right) x - c\left( 0\right) v}
$$

$$
\phi \left( {T,\xi ,\omega }\right)  = {e}^{-a\left( 0\right)  - b\left( 0\right) x - c\left( 0\right) v}
$$

$$
= \mathbb{E}\left\lbrack  {{e}^{{i\xi }{x}_{T} + {i\omega }{v}_{T}} \mid  {x}_{T} = x,{v}_{T} = v}\right\rbrack
$$

$$
= \mathbb{E}\left\lbrack  {{e}^{{i\xi }{x}_{T} + {i\omega }{v}_{T}} \mid  {x}_{T} = x,{v}_{T} = v}\right\rbrack
$$

$$
= {e}^{{i\xi x} + {i\omega v}}
$$

$$
= {e}^{{i\xi x} + {i\omega v}}
$$

which implies

which implies

$$
a\left( 0\right)  = 0
$$

$$
a\left( 0\right)  = 0
$$

$$
b\left( 0\right)  =  - {i\xi }
$$

$$
b\left( 0\right)  =  - {i\xi }
$$

$$
c\left( 0\right)  =  - {i\omega }
$$

$$
c\left( 0\right)  =  - {i\omega }
$$

If we define $\mathcal{G}\left( t\right)$ to be

If we define $\mathcal{G}\left( t\right)$ to be

$$
\mathcal{G}\left( t\right)  = \phi \left( {t,\xi ,\omega }\right)  \tag{D.9}
$$

$$
\mathcal{G}\left( t\right)  = \phi \left( {t,\xi ,\omega }\right)  \tag{D.9}
$$

$\mathcal{G}\left( t\right)$ is a martingale because it is a conditional expectation of a terminal random variable. Therefore its derivative with respect to $t$ , the ${dt}$ term, must be identically zero.