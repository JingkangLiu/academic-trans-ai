

TABLE E.2: Relationship between the scaled grid points ${y}_{j}$ and fixed grid points ${z}_{j}$

<table><tr><td>Model</td><td>${y}_{j}$ in the negative part</td><td>${y}_{j}$ in the positive part</td></tr><tr><td>VG</td><td>$- {z}_{j}/G$</td><td>${z}_{j}/M$</td></tr><tr><td>CGMY</td><td>$- {z}_{j}/G$</td><td>${z}_{j}/M$</td></tr><tr><td>NIG</td><td>$- {z}_{j}/\alpha$</td><td>${z}_{j}/\alpha$</td></tr><tr><td>Merton's</td><td>$\alpha  - \delta {z}_{j}$</td><td>$\alpha  + \delta {z}_{j}$</td></tr><tr><td>Kou's</td><td>$- {z}_{j}/{\eta }_{2}$</td><td>${z}_{j}/{\eta }_{1}$</td></tr></table>

### E.3 Numerical Integral

The integral ${\int }_{y <  - {\epsilon }^{ - }\text{or }y > {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right) }\right) m\left( {dy}\right)$ is calculated using the Simpson’s rule [296]. If there are ${2N} + 1$ grid points ${y}_{0},{y}_{1},\ldots ,{y}_{2N}$ , which satisfy $2{y}_{{2j} + 1} = {y}_{2j} +$ ${y}_{{2j} + 2},\forall 0 \leq  j \leq  N - 1$ and ${y}_{0} = {\epsilon }^{ + }$ , the numerical integral is

$$
{\int }_{y > {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right) }\right) m\left( {dy}\right)
$$

$$
= {\int }_{y > {\epsilon }^{ + }}\left( {w\left( {x + y,\tau }\right)  - w\left( {x,\tau }\right) }\right) k\left( y\right) {dy}
$$

$$
\approx  \mathop{\sum }\limits_{{j = 0}}^{{N - 1}}\left( {w\left( {x + {y}_{2j},\tau }\right)  - w\left( {x,\tau }\right) }\right) k\left( {y}_{2j}\right) \frac{{y}_{{2j} + 2} - {y}_{2j}}{6} +
$$

$$
+ \mathop{\sum }\limits_{{j = 0}}^{{N - 1}}\left( {w\left( {x + {y}_{{2j} + 1},\tau }\right)  - w\left( {x,\tau }\right) }\right) k\left( {y}_{{2j} + 1}\right) \frac{2\left( {{y}_{{2j} + 2} - {y}_{2j}}\right) }{3}
$$

$$
+ \mathop{\sum }\limits_{{j = 0}}^{{N - 1}}\left( {w\left( {x + {y}_{{2j} + 2},\tau }\right)  - w\left( {x,\tau }\right) }\right) k\left( {y}_{{2j} + 2}\right) \frac{{y}_{{2j} + 2} - {y}_{2j}}{6}
$$

,

which is a linear combination of the values of $w\left( {\cdot ,\tau }\right)$ . The integral on $\left\{  {y <  - {\epsilon }^{ - }}\right\}$ is calculated in the same way.

Since the shape of $k\left( y\right)$ depends on the model parameters, it is not efficient if we use the same integral grid for different sample points. Take the Merton's model as an example, where

$$
k\left( y\right)  = \frac{\lambda }{\sqrt{2\pi }\delta }{e}^{-{\left( x - \alpha \right) }^{2}/\left( {2{\delta }^{2}}\right) }
$$

The density function has a center parameter $\alpha$ and a scale parameter $\delta$ . If we define the integral grid points to be ${y}_{j} = \alpha  + \delta {z}_{j},\forall 0 \leq  j \leq  {2N}$ , where ${z}_{j}$ ’s are fixed, we will assign enough grid points around the peak of $k\left( y\right)$ whatever the model parameters and the integral will be more accurate. For other models, the density $k\left( y\right)$ is centered around 0, but it decreases at different rates when the model parameters are different. So we always use a scaled integral grid. In Table E.2, we list the relationship between the scaled grid points ${y}_{j}$ and fixed gird points $0 \leq  {z}_{0} \leq  {z}_{1} \leq  \cdots  \leq  {z}_{2N}$ used for integral. The values of ${z}_{j}$ can be found at https://github.com/weilong-columbia/pide.
