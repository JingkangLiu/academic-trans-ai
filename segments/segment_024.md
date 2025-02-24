$\mathcal{G}\left( t\right)$ is a martingale because it is a conditional expectation of a terminal random variable. Therefore its derivative with respect to $t$ , the ${dt}$ term, must be identically zero.

$$
d{S}_{t} = r{S}_{t}{dt} + \sqrt{{v}_{t}}{S}_{t}d{W}_{t}^{\left( 1\right) }
$$

$$
d{S}_{t} = r{S}_{t}{dt} + \sqrt{{v}_{t}}{S}_{t}d{W}_{t}^{\left( 1\right) }
$$

$$
d{v}_{t} = \kappa \left( {\theta  - {v}_{t}}\right) {dt} + \sigma \sqrt{{v}_{t}}d{W}_{t}^{\left( 2\right) }
$$

$$
d{v}_{t} = \kappa \left( {\theta  - {v}_{t}}\right) {dt} + \sigma \sqrt{{v}_{t}}d{W}_{t}^{\left( 2\right) }
$$

We define ${x}_{t} = \ln {S}_{t} = F\left( {t,{S}_{t}}\right)$ and apply Itô’s lemma to derive $d{x}_{t}$ .

We define ${x}_{t} = \ln {S}_{t} = F\left( {t,{S}_{t}}\right)$ and apply Itô’s lemma to derive $d{x}_{t}$ .

$$
d{x}_{t} = \frac{\partial F}{\partial t}{dt} + \frac{\partial F}{\partial {S}_{t}}d{S}_{t} + \frac{1}{2}\frac{{\partial }^{2}F}{\partial {S}_{t}^{2}}{\left( d{S}_{t}\right) }^{2}
$$

$$
d{x}_{t} = \frac{\partial F}{\partial t}{dt} + \frac{\partial F}{\partial {S}_{t}}d{S}_{t} + \frac{1}{2}\frac{{\partial }^{2}F}{\partial {S}_{t}^{2}}{\left( d{S}_{t}\right) }^{2}
$$

$$
= 0 + \frac{1}{{S}_{t}}\left( {r{S}_{t}{dt} + \sqrt{{v}_{t}}{S}_{t}d{W}_{t}^{\left( 1\right) }}\right)  - \frac{1}{2}\frac{1}{{S}_{t}^{2}}{\left( r{S}_{t}dt + \sqrt{{v}_{t}}{S}_{t}d{W}_{t}^{\left( 1\right) }\right) }^{2}
$$

$$
= 0 + \frac{1}{{S}_{t}}\left( {r{S}_{t}{dt} + \sqrt{{v}_{t}}{S}_{t}d{W}_{t}^{\left( 1\right) }}\right)  - \frac{1}{2}\frac{1}{{S}_{t}^{2}}{\left( r{S}_{t}dt + \sqrt{{v}_{t}}{S}_{t}d{W}_{t}^{\left( 1\right) }\right) }^{2}
$$

$$
= {rdt} + \sqrt{{v}_{t}}d{W}_{t}^{\left( 1\right) } - \frac{1}{2}{v}_{t}{dt}
$$

$$
= {rdt} + \sqrt{{v}_{t}}d{W}_{t}^{\left( 1\right) } - \frac{1}{2}{v}_{t}{dt}
$$

$$
= \left( {r - \frac{1}{2}{v}_{t}}\right) {dt} + \sqrt{{v}_{t}}d{W}_{t}^{\left( 1\right) }
$$

$$
= \left( {r - \frac{1}{2}{v}_{t}}\right) {dt} + \sqrt{{v}_{t}}d{W}_{t}^{\left( 1\right) }
$$

where

where

$$
d{v}_{t} = \kappa \left( {\theta  - {v}_{t}}\right) {dt} + \sigma \sqrt{{v}_{t}}d{W}_{t}^{\left( 2\right) }
$$

$$
d{v}_{t} = \kappa \left( {\theta  - {v}_{t}}\right) {dt} + \sigma \sqrt{{v}_{t}}d{W}_{t}^{\left( 2\right) }
$$

Thus we have

Thus we have

$$
d{x}_{t} = \left( {r - \frac{1}{2}{v}_{t}}\right) {dt} + \sqrt{{v}_{t}}d{W}_{t}^{\left( 1\right) }
$$

$$
d{x}_{t} = \left( {r - \frac{1}{2}{v}_{t}}\right) {dt} + \sqrt{{v}_{t}}d{W}_{t}^{\left( 1\right) }
$$

$$
d{v}_{t} = \kappa \left( {\theta  - {v}_{t}}\right) {dt} + \sigma \sqrt{{v}_{t}}d{W}_{t}^{\left( 2\right) }
$$

$$
d{v}_{t} = \kappa \left( {\theta  - {v}_{t}}\right) {dt} + \sigma \sqrt{{v}_{t}}d{W}_{t}^{\left( 2\right) }
$$

The goal is to find

The goal is to find

$$
{\mathbb{E}}_{t}^{\mathbb{Q}}\left( {e}^{{iu}\ln {S}_{T}}\right)  = {\mathbb{E}}_{t}^{\mathbb{Q}}\left( {e}^{{iu}{x}_{T}}\right)
$$

$$
{\mathbb{E}}_{t}^{\mathbb{Q}}\left( {e}^{{iu}\ln {S}_{T}}\right)  = {\mathbb{E}}_{t}^{\mathbb{Q}}\left( {e}^{{iu}{x}_{T}}\right)
$$

It is clear that $\phi \left( {t,\xi  = u,\omega  = 0}\right)  = \mathbb{E}\left\lbrack  {e}^{{iu}{x}_{T}}\right\rbrack$ . Because $\mathcal{G}\left( t\right)  = \phi \left( {t,\xi ,\omega }\right)$ is a martingale, we have

It is clear that $\phi \left( {t,\xi  = u,\omega  = 0}\right)  = \mathbb{E}\left\lbrack  {e}^{{iu}{x}_{T}}\right\rbrack$ . Because $\mathcal{G}\left( t\right)  = \phi \left( {t,\xi ,\omega }\right)$ is a martingale, we have

$$
d\mathcal{G}\left( t\right)  = \frac{\partial \mathcal{G}\left( t\right) }{\partial t}{dt} + \ldots
$$

$$
d\mathcal{G}\left( t\right)  = \frac{\partial \mathcal{G}\left( t\right) }{\partial t}{dt} + \ldots
$$

$$
= {0dt} + \ldots
$$

$$
= {0dt} + \ldots
$$

because its derivatives with respect to time must be zero and this leads to the expression

because its derivatives with respect to time must be zero and this leads to the expression

$$
\frac{\partial \mathcal{G}\left( t\right) }{\partial t} = {\phi }_{t} + {\phi }_{x}\left( {r - \frac{1}{2}{v}_{t}}\right)  + {\phi }_{v}\left( {\kappa \left( {\theta  - {v}_{t}}\right) }\right)  \tag{D.10}
$$