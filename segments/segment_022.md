$$
{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} = \frac{\lambda }{{u}^{2}} - \frac{{\lambda }^{2}}{{u}^{2}}{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} \tag{D.4}
$$

We recognize the expression in (D.4) is a linear equation as a function of the integral we are actually trying to evaluate, solving (D.4) for it and we get

We recognize the expression in (D.4) is a linear equation as a function of the integral we are actually trying to evaluate, solving (D.4) for it and we get

$$
{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} = \frac{\lambda }{{\lambda }^{2} + {u}^{2}} \tag{D.5}
$$

$$
{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} = \frac{\lambda }{{\lambda }^{2} + {u}^{2}} \tag{D.5}
$$

From (D.2) we can imply

From (D.2) we can imply

$$
{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx} = \frac{u}{\lambda }{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} \tag{D.6}
$$

$$
{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx} = \frac{u}{\lambda }{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} \tag{D.6}
$$

and substituting (D.6) into (D.5) we get

and substituting (D.6) into (D.5) we get

$$
{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx} = \frac{u}{{\lambda }^{2} + {u}^{2}} \tag{D.7}
$$

$$
{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx} = \frac{u}{{\lambda }^{2} + {u}^{2}} \tag{D.7}
$$

Finally substituting both (D.7) and (D.5) into (D.1) we obtain

Finally substituting both (D.7) and (D.5) into (D.1) we obtain

$$
\phi \left( u\right)  = \mathbb{E}\left( {e}^{iuX}\right)
$$

$$
\phi \left( u\right)  = \mathbb{E}\left( {e}^{iuX}\right)
$$

$$
= {\int }_{0}^{\infty }{e}^{iux}\lambda {e}^{-{\lambda x}}{dx}
$$

$$
= {\int }_{0}^{\infty }{e}^{iux}\lambda {e}^{-{\lambda x}}{dx}
$$

$$
= \lambda \left( {{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} + i{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx}}\right)
$$

$$
= \lambda \left( {{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} + i{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx}}\right)
$$

$$
= \lambda \left( {\frac{\lambda }{{\lambda }^{2} + {u}^{2}} + i\frac{u}{{\lambda }^{2} + {u}^{2}}}\right)
$$

$$
= \lambda \left( {\frac{\lambda }{{\lambda }^{2} + {u}^{2}} + i\frac{u}{{\lambda }^{2} + {u}^{2}}}\right)
$$

$$
= \frac{\lambda \left( {\lambda  + {iu}}\right) }{{\lambda }^{2} + {u}^{2}}
$$

$$
= \frac{\lambda \left( {\lambda  + {iu}}\right) }{{\lambda }^{2} + {u}^{2}}
$$

$$
= \frac{\lambda \left( {\lambda  + {iu}}\right) }{\left( {\lambda  + {iu}}\right) \left( {\lambda  - {iu}}\right) }
$$

$$
= \frac{\lambda \left( {\lambda  + {iu}}\right) }{\left( {\lambda  + {iu}}\right) \left( {\lambda  - {iu}}\right) }
$$

$$
= \frac{\lambda }{\lambda  - {iu}}
$$

$$
= \frac{\lambda }{\lambda  - {iu}}
$$

which is the characteristic function of exponential distribution, in short

which is the characteristic function of exponential distribution, in short

$$
\phi \left( u\right)  = \frac{\lambda }{\lambda  - {iu}}
$$

$$
\phi \left( u\right)  = \frac{\lambda }{\lambda  - {iu}}
$$

### D.2 Heston Model — Characteristic Function of the Log Asset Price

### D.2 Heston Model — Characteristic Function of the Log Asset Price

There are various different ways of deriving the characteristic function of Heston model, one of which is manifested in Problem 4 of Chapter 1. We provide an alternative derivation to its characteristic function in this appendix. This derivation is quite generic and can be used to derive the characteristic function of the log of asset prices under various different processes. Derivations similar to the one presented can be seen in [165] and [172].

There are various different ways of deriving the characteristic function of Heston model, one of which is manifested in Problem 4 of Chapter 1. We provide an alternative derivation to its characteristic function in this appendix. This derivation is quite generic and can be used to derive the characteristic function of the log of asset prices under various different processes. Derivations similar to the one presented can be seen in [165] and [172].