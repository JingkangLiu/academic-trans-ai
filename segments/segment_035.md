In Table E.1, we list the choice of ${\epsilon }^{ - },{\epsilon }^{ + }$ and the expressions of ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ , and $\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ for each model. ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ and $\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ are calculated before training.

where

where

$$
{\sigma }_{CGMY}^{2}\left( {C, G, M, Y,{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = C{G}^{Y - 2}\left( {\Gamma \left( {2 - Y}\right)  - \Gamma \left( {2 - Y, G{\epsilon }^{ - }}\right) }\right)
$$

$$
{\sigma }_{CGMY}^{2}\left( {C, G, M, Y,{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = C{G}^{Y - 2}\left( {\Gamma \left( {2 - Y}\right)  - \Gamma \left( {2 - Y, G{\epsilon }^{ - }}\right) }\right)
$$

$$
+ C{M}^{Y - 2}\left( {\Gamma \left( {2 - Y}\right)  - \Gamma \left( {2 - Y, M{\epsilon }^{ + }}\right) }\right) ,
$$

$$
+ C{M}^{Y - 2}\left( {\Gamma \left( {2 - Y}\right)  - \Gamma \left( {2 - Y, M{\epsilon }^{ + }}\right) }\right) ,
$$

and

and

$$
{\omega }_{CGMY}\left( {C, G, M, Y,{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = C\left( {{M}^{Y}\Gamma \left( {-Y, M{\epsilon }^{ + }}\right)  - {\left( M - 1\right) }^{Y} * \Gamma \left( {-Y,\left( {M - 1}\right) {\epsilon }^{ + }}\right) }\right)
$$

$$
{\omega }_{CGMY}\left( {C, G, M, Y,{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = C\left( {{M}^{Y}\Gamma \left( {-Y, M{\epsilon }^{ + }}\right)  - {\left( M - 1\right) }^{Y} * \Gamma \left( {-Y,\left( {M - 1}\right) {\epsilon }^{ + }}\right) }\right)
$$

$$
+ C\left( {{G}^{Y}\Gamma \left( {-Y, G{\epsilon }^{ - }}\right)  - {\left( G + 1\right) }^{Y}\Gamma \left( {-Y,\left( {G + 1}\right) {\epsilon }^{ - }}\right) }\right) .
$$

$$
+ C\left( {{G}^{Y}\Gamma \left( {-Y, G{\epsilon }^{ - }}\right)  - {\left( G + 1\right) }^{Y}\Gamma \left( {-Y,\left( {G + 1}\right) {\epsilon }^{ - }}\right) }\right) .
$$

$M$ and $G$ follow the definitions in Equation (1.45) and (1.46) and $C = 1/\nu .\Gamma \left( \cdot \right)$ is the gamma function and $\Gamma \left( {\cdot , \cdot  }\right)$ is the incomplete gamma function following the definition

$M$ and $G$ follow the definitions in Equation (1.45) and (1.46) and $C = 1/\nu .\Gamma \left( \cdot \right)$ is the gamma function and $\Gamma \left( {\cdot , \cdot  }\right)$ is the incomplete gamma function following the definition

$$
\Gamma \left( {s, y}\right)  = {\int }_{y}^{\infty }{u}^{s - 1}{e}^{-u}{du}.
$$

$$
\Gamma \left( {s, y}\right)  = {\int }_{y}^{\infty }{u}^{s - 1}{e}^{-u}{du}.
$$

${\epsilon }^{ + }$ and ${\epsilon }^{ - }$ could be dependent on the model parameters. For the NIG model, we do not have the closed-form expressions of ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ and $\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ and they are calculated using numerical integration in scipy. ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = 0$ in the Merton’s model and the Kou’s model since ${\epsilon }^{ + } = {\epsilon }^{ - } = 0$ .

${\epsilon }^{ + }$ and ${\epsilon }^{ - }$ could be dependent on the model parameters. For the NIG model, we do not have the closed-form expressions of ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ and $\omega \left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)$ and they are calculated using numerical integration in scipy. ${\sigma }^{2}\left( {{\epsilon }^{ - },{\epsilon }^{ + }}\right)  = 0$ in the Merton’s model and the Kou’s model since ${\epsilon }^{ + } = {\epsilon }^{ - } = 0$ .

<table><tr><td>Model</td><td>${y}_{j}$ in the negative part</td><td>${y}_{j}$ in the positive part</td></tr><tr><td>VG</td><td>$- {z}_{j}/G$</td><td>${z}_{j}/M$</td></tr><tr><td>CGMY</td><td>$- {z}_{j}/G$</td><td>${z}_{j}/M$</td></tr><tr><td>NIG</td><td>$- {z}_{j}/\alpha$</td><td>${z}_{j}/\alpha$</td></tr><tr><td>Merton's</td><td>$\alpha  - \delta {z}_{j}$</td><td>$\alpha  + \delta {z}_{j}$</td></tr><tr><td>Kou's</td><td>$- {z}_{j}/{\eta }_{2}$</td><td>${z}_{j}/{\eta }_{1}$</td></tr></table>