$$
{\mathbb{E}}_{t}\left( {e}^{{iu}\ln {S}_{T}}\right)  = \frac{\exp \left\{  {{iu}\ln {S}_{t} + {iu}\left( {r - q}\right) \tau  + {\kappa \theta \tau }\frac{\beta }{{\sigma }^{2}}}\right\}   \times  \exp \left\{  \frac{-\left( {{u}^{2} + {iu}}\right) {v}_{t}}{\gamma \coth \frac{\gamma \tau }{2} + \beta }\right\}  }{{\left( \cosh \frac{\gamma \tau }{2} + \frac{\beta }{\gamma }\sinh \frac{\gamma \tau }{2}\right) }^{\frac{2\kappa \theta }{{\sigma }^{2}}}}
$$

## Appendix E Evaluation of the PIDE

This appendix will delve into the evaluation of the partial integro-differential equation (PIDE) in an unsupervised deep learning approach to solving PIDEs introduced in Chapter 8.

### E.1 Split of the Integral in the PIDE

As mentioned earlier, this part mostly follows the derivations in Chapter 5. We split the integral term in Equation (8.1) into two parts, the integrals on $\left\{  {-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\right\}$ and $\left\{  {y <  - {\epsilon }^{ - }}\right.$ or $\left. {y > {\epsilon }^{ + }}\right\}$ respectively.

In the region $\left\{  {-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\right\}$ ,

$$
w\left( {x + y,\tau }\right)  = w\left( {x,\tau }\right)  + y\frac{\partial w}{\partial x}\left( {x,\tau }\right)  + \frac{{y}^{2}}{2}\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right)  + O\left( {y}^{3}\right)
$$

and

$$
{e}^{y} = 1 + y + \frac{{y}^{2}}{2} + O\left( {y}^{3}\right) .
$$

Using those two approximations, we get

$$
{\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right)  - \frac{\partial w}{\partial x}\left( {x,\tau }\right) \left( {{e}^{y} - 1}\right) }\right) m\left( {dy}\right)
$$

$$
= {\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\left( {\frac{{y}^{2}}{2}\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right)  - \frac{{y}^{2}}{2}\frac{\partial w}{\partial x}\left( {x,\tau }\right)  + O\left( {y}^{3}\right) }\right) m\left( {dy}\right)
$$

$$
\approx  {\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\left( {\frac{{y}^{2}}{2}\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right)  - \frac{{y}^{2}}{2}\frac{\partial w}{\partial x}\left( {x,\tau }\right) }\right) m\left( {dy}\right) .
$$

Define ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = {\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}{y}^{2}m\left( {dy}\right)$ and we get

$$
{\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right)  - \frac{\partial w}{\partial x}\left( {x,\tau }\right) \left( {{e}^{y} - 1}\right) }\right) m\left( {dy}\right)
$$

$$
\approx  \frac{1}{2}{\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right) \left( {\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right)  - \frac{\partial w}{\partial x}\left( {x,\tau }\right) }\right) .
$$

In the region $\left\{  {y <  - {\epsilon }^{ - }}\right.$ or $\left. {y > {\epsilon }^{ + }}\right\}$ ,

$$
{\int }_{y <  - {\epsilon }^{ - }\text{or }y > {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right)  - \frac{\partial w}{\partial x}\left( {x,\tau }\right) \left( {{e}^{y} - 1}\right) }\right) m\left( {dy}\right)
$$

$$
= {\int }_{y <  - {\epsilon }^{ - }\text{or }y > {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right) }\right) m\left( {dy}\right)  + \frac{\partial w}{\partial x}\left( {x,\tau }\right) \omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right) ,
$$

where $\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = {\int }_{y <  - {\epsilon }^{ - }\text{or }y > {\epsilon }^{ + }}\left( {1 - {e}^{y}}\right) m\left( {dy}\right)$ . DOI: 10.1201/9780429094743-E Combining the two parts of integrals and putting them back to Equation (8.1), we get

$$
\left( {{\int }_{y <  - {\epsilon }^{ - }\text{or }y > {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right) }\right) m\left( {dy}\right)  + \frac{{s}^{2} + {\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right) }{2}\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right) }\right.  \tag{E.1}
$$