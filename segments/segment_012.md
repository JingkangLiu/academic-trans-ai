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