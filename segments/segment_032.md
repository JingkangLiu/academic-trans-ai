## Appendix E Evaluation of the PIDE

## Appendix E Evaluation of the PIDE

This appendix will delve into the evaluation of the partial integro-differential equation (PIDE) in an unsupervised deep learning approach to solving PIDEs introduced in Chapter 8.

This appendix will delve into the evaluation of the partial integro-differential equation (PIDE) in an unsupervised deep learning approach to solving PIDEs introduced in Chapter 8.

### E.1 Split of the Integral in the PIDE

### E.1 Split of the Integral in the PIDE

As mentioned earlier, this part mostly follows the derivations in Chapter 5. We split the integral term in Equation (8.1) into two parts, the integrals on $\left\{  {-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\right\}$ and $\left\{  {y <  - {\epsilon }^{ - }}\right.$ or $\left. {y > {\epsilon }^{ + }}\right\}$ respectively.

As mentioned earlier, this part mostly follows the derivations in Chapter 5. We split the integral term in Equation (8.1) into two parts, the integrals on $\left\{  {-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\right\}$ and $\left\{  {y <  - {\epsilon }^{ - }}\right.$ or $\left. {y > {\epsilon }^{ + }}\right\}$ respectively.

In the region $\left\{  {-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\right\}$ ,

In the region $\left\{  {-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\right\}$ ,

$$
w\left( {x + y,\tau }\right)  = w\left( {x,\tau }\right)  + y\frac{\partial w}{\partial x}\left( {x,\tau }\right)  + \frac{{y}^{2}}{2}\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right)  + O\left( {y}^{3}\right)
$$

$$
w\left( {x + y,\tau }\right)  = w\left( {x,\tau }\right)  + y\frac{\partial w}{\partial x}\left( {x,\tau }\right)  + \frac{{y}^{2}}{2}\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right)  + O\left( {y}^{3}\right)
$$

and

and

$$
{e}^{y} = 1 + y + \frac{{y}^{2}}{2} + O\left( {y}^{3}\right) .
$$

$$
{e}^{y} = 1 + y + \frac{{y}^{2}}{2} + O\left( {y}^{3}\right) .
$$

Using those two approximations, we get

Using those two approximations, we get

$$
{\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right)  - \frac{\partial w}{\partial x}\left( {x,\tau }\right) \left( {{e}^{y} - 1}\right) }\right) m\left( {dy}\right)
$$

$$
{\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right)  - \frac{\partial w}{\partial x}\left( {x,\tau }\right) \left( {{e}^{y} - 1}\right) }\right) m\left( {dy}\right)
$$

$$
= {\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\left( {\frac{{y}^{2}}{2}\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right)  - \frac{{y}^{2}}{2}\frac{\partial w}{\partial x}\left( {x,\tau }\right)  + O\left( {y}^{3}\right) }\right) m\left( {dy}\right)
$$

$$
= {\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\left( {\frac{{y}^{2}}{2}\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right)  - \frac{{y}^{2}}{2}\frac{\partial w}{\partial x}\left( {x,\tau }\right)  + O\left( {y}^{3}\right) }\right) m\left( {dy}\right)
$$

$$
\approx  {\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\left( {\frac{{y}^{2}}{2}\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right)  - \frac{{y}^{2}}{2}\frac{\partial w}{\partial x}\left( {x,\tau }\right) }\right) m\left( {dy}\right) .
$$

$$
\approx  {\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\left( {\frac{{y}^{2}}{2}\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right)  - \frac{{y}^{2}}{2}\frac{\partial w}{\partial x}\left( {x,\tau }\right) }\right) m\left( {dy}\right) .
$$

Define ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = {\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}{y}^{2}m\left( {dy}\right)$ and we get

Define ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = {\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}{y}^{2}m\left( {dy}\right)$ and we get

$$
{\int }_{-{\epsilon }^{ - } \leq  y \leq  {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right)  - \frac{\partial w}{\partial x}\left( {x,\tau }\right) \left( {{e}^{y} - 1}\right) }\right) m\left( {dy}\right)
$$