$$
\left\{  \begin{array}{l} {a}^{\prime }\left( {T - t}\right)  - c\left( {T - t}\right) {\kappa \theta } - {rb}\left( {T - t}\right)  = 0 \\  {b}^{\prime }\left( {T - t}\right)  = 0 \\  {c}^{\prime }\left( {T - t}\right)  + \frac{1}{2}b\left( {T - t}\right)  + c\left( {T - t}\right) \kappa  + \frac{1}{2}{b}^{2}\left( {T - t}\right)  + \frac{1}{2}{c}^{2}\left( {T - t}\right) {\sigma }^{2} + {\rho \sigma b}\left( {T - t}\right) c\left( {T - t}\right)  = 0 \end{array}\right.
$$

Define $\tau  = T - t$ and we get

$$
\left\{  \begin{array}{l} {a}^{\prime }\left( \tau \right)  - c\left( \tau \right) {\kappa \theta } - {rb}\left( \tau \right)  = 0 \\  {b}^{\prime }\left( \tau \right)  = 0 \\  {c}^{\prime }\left( \tau \right)  + \frac{1}{2}b\left( \tau \right)  + c\left( \tau \right) \kappa  + \frac{1}{2}{b}^{2}\left( \tau \right)  + \frac{1}{2}{c}^{2}\left( \tau \right) {\sigma }^{2} + {\rho \sigma b}\left( \tau \right) c\left( \tau \right)  = 0 \end{array}\right.
$$

The second Riccati equation, ${b}^{\prime }\left( \tau \right)  = 0$ , implies that $b\left( \tau \right)$ is constant and the boundary condition implies

$$
b\left( \tau \right)  =  - {i\xi }
$$

Substituting it in the third equation we have

$$
{c}^{\prime }\left( \tau \right)  = \frac{1}{2}{i\xi } - c\left( \tau \right) \kappa  - \frac{1}{2}{\left( -i\xi \right) }^{2} - \frac{1}{2}{c}^{2}\left( \tau \right) {\sigma }^{2} - {\rho \sigma }\left( {-{i\xi }}\right) c\left( \tau \right)
$$

$$
=  - \frac{1}{2}{\sigma }^{2}{c}^{2}\left( \tau \right)  + \left( {{i\xi \rho \sigma } - \kappa }\right) c\left( \tau \right)  + \left( {\frac{1}{2}{i\xi } + \frac{1}{2}{\xi }^{2}}\right)
$$

$$
\frac{{dc}\left( \tau \right) }{d\tau } =  - \frac{1}{2}{\sigma }^{2}\left\lbrack  {{c}^{2}\left( \tau \right)  + \frac{2}{{\sigma }^{2}}\left( {\kappa  - {i\xi \rho \sigma }}\right) c\left( \tau \right)  - \frac{{i\xi } + {\xi }^{2}}{{\sigma }^{2}}}\right\rbrack
$$

$$
\frac{{dc}\left( \tau \right) }{{c}^{2}\left( \tau \right)  + \frac{2}{{\sigma }^{2}}\left( {\kappa  - {i\xi \rho \sigma }}\right) c\left( \tau \right)  - \frac{{i\xi } + {\xi }^{2}}{{\sigma }^{2}}} =  - \frac{1}{2}{\sigma }^{2}{d\tau }
$$

We solve this equation using partial fractions. The roots of the equation in the denominator

$$
{c}^{2}\left( \tau \right)  + \frac{2}{{\sigma }^{2}}\left( {\kappa  - {i\xi \rho \sigma }}\right) c\left( \tau \right)  - \frac{{i\xi } + {\xi }^{2}}{{\sigma }^{2}}
$$

are

$$
{c}_{1} = \frac{\beta  - \gamma }{{\sigma }^{2}}
$$

$$
{c}_{2} = \frac{\beta  + \gamma }{{\sigma }^{2}}
$$

where

$$
\beta  = \kappa  - {i\xi \rho \sigma }
$$

$$
\gamma  = \sqrt{{\left( \kappa  - i\xi \rho \sigma \right) }^{2} + {\sigma }^{2}\left( {{\xi }^{2} + {i\xi }}\right) }
$$

We can find $A$ and $B$ such that

$$
\frac{1}{{c}^{2}\left( \tau \right)  + \frac{2}{{\sigma }^{2}}\left( {\kappa  - {i\xi \rho \sigma }}\right) c\left( \tau \right)  - \frac{{i\xi } + {\xi }^{2}}{{\sigma }^{2}}} = \frac{A}{c\left( \tau \right)  - {c}_{1}} + \frac{B}{c\left( \tau \right)  - {c}_{2}}
$$

We see that $A$ and $B$ should satisfy the following equation:

$$
A\left( {c\left( \tau \right)  - \frac{\beta  - \gamma }{{\sigma }^{2}}}\right)  + B\left( {c\left( \tau \right)  - \frac{\beta  + \gamma }{{\sigma }^{2}}}\right)  = 1
$$

Or equivalently

$$
A + B = 0
$$

$$
- A\left( {\beta  - \gamma }\right)  - B\left( {\beta  + \gamma }\right)  = {\sigma }^{2}
$$

and we get $A = \frac{{\sigma }^{2}}{2\sigma }$ and $B =  - \frac{{\sigma }^{2}}{2\sigma }$ . Now substituting and integrating we get

$$
\int \frac{\frac{{\sigma }^{2}}{2\gamma }}{c\left( \tau \right)  - \frac{\beta  + \gamma }{{\sigma }^{2}}}{dc}\left( \tau \right)  + \int \frac{-\frac{{\sigma }^{2}}{2\gamma }}{c\left( \tau \right)  - \frac{\beta  - \gamma }{{\sigma }^{2}}}{dc}\left( \tau \right)  =  - \frac{1}{2}{\sigma }^{2}\tau  + \text{ constant }
$$

$$
\frac{{\sigma }^{2}}{2\gamma }\ln \left( {c\left( \tau \right)  - \frac{-\beta  + \gamma }{{\sigma }^{2}}}\right)  - \frac{{\sigma }^{2}}{2\gamma }\ln \left( {c\left( \tau \right)  - \frac{-\beta  - \gamma }{{\sigma }^{2}}}\right)  =  - \frac{1}{2}{\sigma }^{2}\tau  + \text{ constant }
$$

or