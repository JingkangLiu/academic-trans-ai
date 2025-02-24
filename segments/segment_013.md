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