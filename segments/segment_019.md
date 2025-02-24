$$
\left. {-\frac{\partial w}{\partial \tau }\left( {x,\tau }\right)  + \left( {r - q - \frac{{s}^{2} + {\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right) }{2} + \omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right) }\right) \frac{\partial w}{\partial x}\left( {x,\tau }\right)  - {rw}\left( {x,\tau }\right) }\right)  = 0.
$$

TABLE E.1: ${\epsilon }^{ - },{\epsilon }^{ + },{\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ and $\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ for each model

<table><tr><td>Model</td><td>${\epsilon }^{ - }$</td><td>${\epsilon }^{ + }$</td><td>${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$</td><td>$\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$</td></tr><tr><td>VG</td><td>0.02/G</td><td>0.02/M</td><td>${\sigma }_{CGMY}^{2}\left( {C, G, M,0,{\epsilon }^{ - },{\epsilon }^{ + }}\right)$</td><td>${\omega }_{CGMY}\left( {C, G, M,0,{\epsilon }^{ - },{\epsilon }^{ + }}\right)$</td></tr><tr><td>CGMY</td><td>0.01/G</td><td>0.01/M</td><td>${\sigma }_{CGMY}^{2}\left( {C, G, M, Y,{\epsilon }^{ - },{\epsilon }^{ + }}\right)$</td><td>${\omega }_{CGMY}\left( {C, G, M, Y,{\epsilon }^{ - },{\epsilon }^{ + }}\right)$</td></tr><tr><td>NIG</td><td>0.05/α</td><td>0.05/α</td><td>-</td><td>-</td></tr><tr><td>Merton's</td><td>0</td><td>0</td><td>0</td><td>$- \lambda \left( {\exp \left( {\alpha  + {\delta }^{2}/2}\right)  - 1}\right)$</td></tr><tr><td>Kou's</td><td>0</td><td>0</td><td>0</td><td>$- \lambda \left( {\frac{p{\eta }_{1}}{{\eta }_{1} - 1} + \frac{\left( {1 - p}\right) {\eta }_{2}}{{\eta }_{2} + 1} - 1}\right)$</td></tr></table>

In Equation (E.1), the function $w\left( {x,\tau }\right)$ as well as its derivatives $\frac{\partial w}{\partial x}\left( {x,\tau }\right) ,\frac{{\partial }^{2}w}{\partial {x}^{2}}\left( {x,\tau }\right)$ and $\frac{\partial w}{\partial \tau }\left( {x,\tau }\right)$ can be calculated by the neural network itself or the back-propagation of the neural network. Then the terms remaining to be calculated are ${\int }_{y <  - {\epsilon }^{ - }\text{or }y > {\epsilon }^{ + }}(w\left( {x + y,\tau }\right)$ $- w\left( {x,\tau }\right) )m\left( {dy}\right) ,{\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ and $\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ .

### E.2 Pre-calculations

In Table E.1, we list the choice of ${\epsilon }^{ - },{\epsilon }^{ + }$ and the expressions of ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ , and $\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ for each model. ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ and $\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ are calculated before training.

where

$$
{\sigma }_{CGMY}^{2}\left( {C, G, M, Y,{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = C{G}^{Y - 2}\left( {\Gamma \left( {2 - Y}\right)  - \Gamma \left( {2 - Y, G{\epsilon }^{ - }}\right) }\right)
$$

$$
+ C{M}^{Y - 2}\left( {\Gamma \left( {2 - Y}\right)  - \Gamma \left( {2 - Y, M{\epsilon }^{ + }}\right) }\right) ,
$$

and

$$
{\omega }_{CGMY}\left( {C, G, M, Y,{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = C\left( {{M}^{Y}\Gamma \left( {-Y, M{\epsilon }^{ + }}\right)  - {\left( M - 1\right) }^{Y} * \Gamma \left( {-Y,\left( {M - 1}\right) {\epsilon }^{ + }}\right) }\right)
$$

$$
+ C\left( {{G}^{Y}\Gamma \left( {-Y, G{\epsilon }^{ - }}\right)  - {\left( G + 1\right) }^{Y}\Gamma \left( {-Y,\left( {G + 1}\right) {\epsilon }^{ - }}\right) }\right) .
$$

$M$ and $G$ follow the definitions in Equation (1.45) and (1.46) and $C = 1/\nu .\Gamma \left( \cdot \right)$ is the gamma function and $\Gamma \left( {\cdot , \cdot  }\right)$ is the incomplete gamma function following the definition

$$
\Gamma \left( {s, y}\right)  = {\int }_{y}^{\infty }{u}^{s - 1}{e}^{-u}{du}.
$$

${\epsilon }^{ + }$ and ${\epsilon }^{ - }$ could be dependent on the model parameters. For the NIG model, we do not have the closed-form expressions of ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ and $\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ and they are calculated using numerical integration in scipy. ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = 0$ in the Merton’s model and the Kou’s model since ${\epsilon }^{ + } = {\epsilon }^{ - } = 0$ .