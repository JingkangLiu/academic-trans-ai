$$
\ln \left( \frac{c\left( \tau \right)  - \frac{-\beta  + \gamma }{{\sigma }^{2}}}{c\left( \tau \right)  - \frac{-\beta  - \gamma }{{\sigma }^{2}}}\right)  =  - {\gamma \tau } + \text{ constant }
$$

$$
\frac{c\left( \tau \right)  - \frac{-\beta  + \gamma }{{\sigma }^{2}}}{c\left( \tau \right)  - \frac{-\beta  - \gamma }{{\sigma }^{2}}} = \alpha {e}^{-{\gamma \tau }} \tag{D.12}
$$

The boundary condition for $c\left( \tau \right)$ is

$$
c\left( {\tau  = 0}\right)  = c\left( 0\right)  =  - {i\varphi } =  - i\left( 0\right)  = 0
$$

Applying this we obtain

$$
\alpha  = \frac{0 - \frac{-\beta  + \gamma }{{\sigma }^{2}}}{0 - \frac{-\beta  - \gamma }{{\sigma }^{2}}} = \frac{\beta  - \gamma }{\beta  + \gamma }
$$

We substitute this back into (D.12) and solve for $c\left( \tau \right)$ .

$$
c\left( \tau \right)  = \frac{\gamma  - \beta }{{\sigma }^{2}}\frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}
$$

Having $c\left( \tau \right)$ , we can solve for $a\left( \tau \right)$ .

$$
{a}^{\prime }\left( \tau \right)  = c\left( \tau \right) {\kappa \theta } + {rb}\left( \tau \right)
$$

$$
= {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}} - {i\xi r}
$$

$$
a\left( \tau \right)  = {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\int \frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}{d\tau } - {i\xi r}\int {d\tau }
$$

$$
= {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\int \frac{1}{1 - \alpha {e}^{-{\gamma \tau }}}{d\tau }-\int \frac{{e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}{d\tau }}\right\rbrack   - {i\xi r}\int {d\tau }
$$

$$
= {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\tau  + \frac{1}{\gamma }\ln \left( {1 - \alpha {e}^{-{\gamma \tau }}}\right)  - \frac{1}{\alpha \gamma }\ln \left( {1 - \alpha {e}^{-{\gamma \tau }}}\right) }\right\rbrack   - {i\xi r\tau } + \text{ constant }
$$

$$
= {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\tau  + \ln {\left( 1 - \alpha {e}^{-{\gamma \tau }}\right) }^{\frac{\alpha  - 1}{\alpha \gamma }}}\right\rbrack   - {iu\xi r\tau } + \text{ constant }
$$

To find the constant, we know that $a\left( {\tau  = 0}\right)  = 0$ and that implies

$$
a\left( 0\right)  = {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {0 + \ln {\left( 1 - \alpha \right) }^{\frac{\alpha  - 1}{\alpha \gamma }}}\right\rbrack   + \text{ constant } = 0
$$

and we obtain

$$
\text{ constant } =  - {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\ln {\left( 1 - \alpha \right) }^{\frac{\alpha  - 1}{\alpha \gamma }}}\right\rbrack
$$

Substituting it into $a\left( \tau \right)$ we get

$$
a\left( \tau \right)  = {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\tau  + \ln {\left( \frac{1 - \alpha {e}^{-{\gamma \tau }}}{1 - \alpha }\right) }^{\frac{\alpha  - 1}{\alpha \gamma }}}\right\rbrack   - {iur\tau }
$$

Now that we have all loadings $a\left( \tau \right) , b\left( \tau \right)$ , and $c\left( \tau \right)$ explicitly we can calculate the characteristic function

$$
\mathbb{E}\left( {e}^{{iu}{x}_{T}}\right)  = \phi \left( {t = 0,\xi  = u,\omega  = 0}\right)
$$

$$
= {e}^{-a\left( \tau \right)  - b\left( \tau \right) {x}_{0} - c\left( \tau \right) {v}_{0}}
$$

where

$$
a\left( \tau \right)  = {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\tau  + \ln {\left( \frac{1 - \alpha {e}^{-{\gamma \tau }}}{1 - \alpha }\right) }^{\frac{\alpha  - 1}{\alpha \gamma }}}\right\rbrack   - {iur\tau }
$$

$$
b\left( \tau \right)  =  - {iu}
$$

$$
c\left( \tau \right)  = \frac{\gamma  - \beta }{{\sigma }^{2}}\frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}
$$

and $\beta  = \kappa  - {iu\rho \sigma },\gamma  = \sqrt{{\left( \kappa  - i\xi \rho \sigma \right) }^{2} + {\sigma }^{2}\left( {{\xi }^{2} + {i\xi }}\right) }$ , and $\alpha  = \frac{\beta  - \gamma }{\beta  + \gamma }$ . Thus the full characteristic function is as follows: