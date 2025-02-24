$$
\phi \left( u\right)  = \mathbb{E}\left( {e}^{iuX}\right)
$$

$$
\phi \left( u\right)  = \mathbb{E}\left( {e}^{iuX}\right)
$$

$$
= {\int }_{0}^{\infty }{e}^{iux}\lambda {e}^{-{\lambda x}}{dx}
$$

$$
= {\int }_{0}^{\infty }{e}^{iux}\lambda {e}^{-{\lambda x}}{dx}
$$

$$
= \lambda {\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} + {i\lambda }{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx} \tag{D.1}
$$

$$
= \lambda {\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} + {i\lambda }{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx} \tag{D.1}
$$

For the first integral

For the first integral

$$
{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx}
$$

$$
{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx}
$$

We call

We call

$$
{f}^{\prime }\left( x\right)  = \cos \left( {ux}\right)
$$

$$
{f}^{\prime }\left( x\right)  = \cos \left( {ux}\right)
$$

$$
g\left( x\right)  = {e}^{-{\lambda x}}
$$

$$
g\left( x\right)  = {e}^{-{\lambda x}}
$$

by applying integration by parts, that is

by applying integration by parts, that is

$$
{\int }_{0}^{\infty }{f}^{\prime }\left( x\right) g\left( x\right) {dx} = {\left. f\left( x\right) g\left( x\right) \right| }_{0}^{\infty } - {\int }_{0}^{\infty }f\left( x\right) {g}^{\prime }\left( x\right) {dx}
$$

$$
{\int }_{0}^{\infty }{f}^{\prime }\left( x\right) g\left( x\right) {dx} = {\left. f\left( x\right) g\left( x\right) \right| }_{0}^{\infty } - {\int }_{0}^{\infty }f\left( x\right) {g}^{\prime }\left( x\right) {dx}
$$

we get

we get

$$
{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} = {\left. \frac{1}{u}\sin \left( ux\right) {e}^{-{\lambda x}}\right| }_{0}^{\infty } - {\int }_{0}^{\infty }\frac{1}{u}\sin \left( {ux}\right) \left( {-\lambda }\right) {e}^{-{\lambda x}}{dx}
$$

$$
{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} = {\left. \frac{1}{u}\sin \left( ux\right) {e}^{-{\lambda x}}\right| }_{0}^{\infty } - {\int }_{0}^{\infty }\frac{1}{u}\sin \left( {ux}\right) \left( {-\lambda }\right) {e}^{-{\lambda x}}{dx}
$$

$$
= \frac{\lambda }{u}{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx} \tag{D.2}
$$

$$
= \frac{\lambda }{u}{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx} \tag{D.2}
$$

This time, we call

This time, we call

$$
{f}^{\prime }\left( x\right)  = \sin \left( {ux}\right)
$$

$$
{f}^{\prime }\left( x\right)  = \sin \left( {ux}\right)
$$

$$
g\left( x\right)  = {e}^{-{\lambda x}}
$$

$$
g\left( x\right)  = {e}^{-{\lambda x}}
$$

and apply integration by parts more one more time to get

and apply integration by parts more one more time to get

$$
\frac{\lambda }{u}{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx} = \frac{\lambda }{u}\left( {-{\left. \frac{1}{u}\cos \left( ux\right) {e}^{\lambda x}\right| }_{0}^{\infty } - {\int }_{0}^{\infty }\frac{1}{u}\cos \left( {ux}\right) \lambda {e}^{-{\lambda x}}{dx}}\right)
$$

$$
\frac{\lambda }{u}{\int }_{0}^{\infty }\sin \left( {ux}\right) {e}^{-{\lambda x}}{dx} = \frac{\lambda }{u}\left( {-{\left. \frac{1}{u}\cos \left( ux\right) {e}^{\lambda x}\right| }_{0}^{\infty } - {\int }_{0}^{\infty }\frac{1}{u}\cos \left( {ux}\right) \lambda {e}^{-{\lambda x}}{dx}}\right)
$$

$$
= \frac{\lambda }{u}\left( {\frac{1}{u} - \frac{\lambda }{u}{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx}}\right)
$$

$$
= \frac{\lambda }{u}\left( {\frac{1}{u} - \frac{\lambda }{u}{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx}}\right)
$$

$$
= \frac{\lambda }{{u}^{2}} - \frac{{\lambda }^{2}}{{u}^{2}}{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} \tag{D.3}
$$

$$
= \frac{\lambda }{{u}^{2}} - \frac{{\lambda }^{2}}{{u}^{2}}{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} \tag{D.3}
$$

Bu substituting (D.3) into (D.2) we get

Bu substituting (D.3) into (D.2) we get

$$
{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} = \frac{\lambda }{{u}^{2}} - \frac{{\lambda }^{2}}{{u}^{2}}{\int }_{0}^{\infty }\cos \left( {ux}\right) {e}^{-{\lambda x}}{dx} \tag{D.4}
$$