The boundary condition for $c\left( \tau \right)$ is

The boundary condition for $c\left( \tau \right)$ is

$$
c\left( {\tau  = 0}\right)  = c\left( 0\right)  =  - {i\varphi } =  - i\left( 0\right)  = 0
$$

$$
c\left( {\tau  = 0}\right)  = c\left( 0\right)  =  - {i\varphi } =  - i\left( 0\right)  = 0
$$

Applying this we obtain

Applying this we obtain

$$
\alpha  = \frac{0 - \frac{-\beta  + \gamma }{{\sigma }^{2}}}{0 - \frac{-\beta  - \gamma }{{\sigma }^{2}}} = \frac{\beta  - \gamma }{\beta  + \gamma }
$$

$$
\alpha  = \frac{0 - \frac{-\beta  + \gamma }{{\sigma }^{2}}}{0 - \frac{-\beta  - \gamma }{{\sigma }^{2}}} = \frac{\beta  - \gamma }{\beta  + \gamma }
$$

We substitute this back into (D.12) and solve for $c\left( \tau \right)$ .

We substitute this back into (D.12) and solve for $c\left( \tau \right)$ .

$$
c\left( \tau \right)  = \frac{\gamma  - \beta }{{\sigma }^{2}}\frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}
$$

$$
c\left( \tau \right)  = \frac{\gamma  - \beta }{{\sigma }^{2}}\frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}
$$

Having $c\left( \tau \right)$ , we can solve for $a\left( \tau \right)$ .

Having $c\left( \tau \right)$ , we can solve for $a\left( \tau \right)$ .

$$
{a}^{\prime }\left( \tau \right)  = c\left( \tau \right) {\kappa \theta } + {rb}\left( \tau \right)
$$

$$
{a}^{\prime }\left( \tau \right)  = c\left( \tau \right) {\kappa \theta } + {rb}\left( \tau \right)
$$

$$
= {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}} - {i\xi r}
$$

$$
= {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}} - {i\xi r}
$$

$$
a\left( \tau \right)  = {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\int \frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}{d\tau } - {i\xi r}\int {d\tau }
$$

$$
a\left( \tau \right)  = {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\int \frac{1 - {e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}{d\tau } - {i\xi r}\int {d\tau }
$$

$$
= {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\int \frac{1}{1 - \alpha {e}^{-{\gamma \tau }}}{d\tau }-\int \frac{{e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}{d\tau }}\right\rbrack   - {i\xi r}\int {d\tau }
$$

$$
= {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\int \frac{1}{1 - \alpha {e}^{-{\gamma \tau }}}{d\tau }-\int \frac{{e}^{-{\gamma \tau }}}{1 - \alpha {e}^{-{\gamma \tau }}}{d\tau }}\right\rbrack   - {i\xi r}\int {d\tau }
$$

$$
= {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\tau  + \frac{1}{\gamma }\ln \left( {1 - \alpha {e}^{-{\gamma \tau }}}\right)  - \frac{1}{\alpha \gamma }\ln \left( {1 - \alpha {e}^{-{\gamma \tau }}}\right) }\right\rbrack   - {i\xi r\tau } + \text{ constant }
$$

$$
= {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\tau  + \frac{1}{\gamma }\ln \left( {1 - \alpha {e}^{-{\gamma \tau }}}\right)  - \frac{1}{\alpha \gamma }\ln \left( {1 - \alpha {e}^{-{\gamma \tau }}}\right) }\right\rbrack   - {i\xi r\tau } + \text{ constant }
$$

$$
= {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\tau  + \ln {\left( 1 - \alpha {e}^{-{\gamma \tau }}\right) }^{\frac{\alpha  - 1}{\alpha \gamma }}}\right\rbrack   - {iu\xi r\tau } + \text{ constant }
$$

$$
= {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {\tau  + \ln {\left( 1 - \alpha {e}^{-{\gamma \tau }}\right) }^{\frac{\alpha  - 1}{\alpha \gamma }}}\right\rbrack   - {iu\xi r\tau } + \text{ constant }
$$

To find the constant, we know that $a\left( {\tau  = 0}\right)  = 0$ and that implies

To find the constant, we know that $a\left( {\tau  = 0}\right)  = 0$ and that implies

$$
a\left( 0\right)  = {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {0 + \ln {\left( 1 - \alpha \right) }^{\frac{\alpha  - 1}{\alpha \gamma }}}\right\rbrack   + \text{ constant } = 0
$$

$$
a\left( 0\right)  = {\kappa \theta }\frac{\gamma  - \beta }{{\sigma }^{2}}\left\lbrack  {0 + \ln {\left( 1 - \alpha \right) }^{\frac{\alpha  - 1}{\alpha \gamma }}}\right\rbrack   + \text{ constant } = 0
$$