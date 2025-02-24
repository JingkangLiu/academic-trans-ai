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