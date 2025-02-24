as expected we get the same result. Having $c$ ’s we can write

$$
\frac{{\partial }^{2}f\left( {{x}_{1},{x}_{2}}\right) }{\partial {x}_{1}\partial {x}_{2}}
$$

$$
= \frac{1!}{{h}_{1}^{1}}\frac{1!}{{h}_{2}^{1}}\mathop{\sum }\limits_{{{i}_{1} = 0}}^{2}\mathop{\sum }\limits_{{{i}_{2} = 0}}^{2}{c}_{{i}_{1},{i}_{2}}f\left( {{x}_{1} + {i}_{1}{h}_{1},{x}_{2} + {i}_{2}{h}_{2}}\right)  + O\left( {h}_{1}^{2}\right)  + O\left( {h}_{2}^{2}\right)
$$

$$
= \frac{\frac{9}{4}f\left( {{x}_{1},{x}_{2}}\right)  - {3f}\left( {{x}_{1} + {h}_{1},{x}_{2}}\right)  + \frac{3}{4}f\left( {{x}_{1} + 2{h}_{1},{x}_{2}}\right)  - {3f}\left( {{x}_{1},{x}_{2} + {h}_{2}}\right)  + {4f}\left( {{x}_{1} + {h}_{1},{x}_{2} + {h}_{2}}\right)  - f\left( {{x}_{1} + 2{h}_{1},{x}_{2} + {h}_{2}}\right) }{{h}_{1}{h}_{2}}
$$

$$
+ \frac{\frac{3}{4}f\left( {{x}_{1},{x}_{2} + 2{h}_{2}}\right)  - f\left( {{x}_{1} + {h}_{1},{x}_{2} + 2{h}_{2}}\right)  + \frac{1}{4}f\left( {{x}_{1} + 2{h}_{1},{x}_{2} + 2{h}_{2}}\right) }{{h}_{1}{h}_{2}} + O\left( {h}_{1}^{2}\right)  + O\left( {h}_{2}^{2}\right)
$$

$$
= \frac{{9f}\left( {{x}_{1},{x}_{2}}\right)  - {12f}\left( {{x}_{1} + {h}_{1},{x}_{2}}\right)  + {3f}\left( {{x}_{1} + 2{h}_{1},{x}_{2}}\right)  - {12f}\left( {{x}_{1},{x}_{2} + {h}_{2}}\right)  + {16f}\left( {{x}_{1} + {h}_{1},{x}_{2} + {h}_{2}}\right)  - {4f}\left( {{x}_{1} + 2{h}_{1},{x}_{2} + {h}_{2}}\right) }{4{h}_{1}{h}_{2}}
$$

$$
+ \frac{{3f}\left( {{x}_{1},{x}_{2} + 2{h}_{2}}\right)  - {4f}\left( {{x}_{1} + {h}_{1},{x}_{2} + 2{h}_{2}}\right)  + f\left( {{x}_{1} + 2{h}_{1},{x}_{2} + 2{h}_{2}}\right) }{4{h}_{1}{h}_{2}} + O\left( {h}_{1}^{2}\right)  + O\left( {h}_{2}^{2}\right)
$$

#### C.2.3 Higher-dimensional Examples

For illustrative purposes, we look at a 4-dimensional example.



Example 65 Difference approximation of $\frac{{\partial }^{4}f\left( {{x}_{1},{x}_{2},{x}_{3},{x}_{4}}\right) }{\partial {x}_{1}\partial {x}_{2}\partial {x}_{3}\partial {x}_{4}}$ , central difference of second order in ${x}_{1},{x}_{2},{x}_{3}$ , and ${x}_{4}$ .

We wish to compute the forward difference approximation of $\frac{{\partial }^{4}f\left( {{x}_{1},{x}_{2},{x}_{3},{x}_{4}}\right) }{\partial {x}_{1}\partial {x}_{2}\partial {x}_{3}\partial {x}_{4}}$ with $O\left( {h}_{1}^{2}\right)  +$ $O\left( {h}_{2}^{2}\right)  + O\left( {h}_{3}^{2}\right)  + O\left( {h}_{4}^{2}\right)$ . Thus we have ${d}_{1} = 1,{d}_{2} = 1,{d}_{3} = 1,{d}_{4} = 1$ , and ${p}_{1} = 2,{p}_{2} = 2$ , ${p}_{3} = 2,{p}_{4} = 2$ with

$$
{i}_{{l}_{1}} =  - \frac{1}{2}\left( {{d}_{1} + {p}_{1} - 1}\right)  =  - 1,{i}_{{u}_{1}} = \frac{1}{2}\left( {{d}_{1} + {p}_{1} - 1}\right)  = 1
$$

$$
{i}_{{l}_{2}} =  - \frac{1}{2}\left( {{d}_{2} + {p}_{2} - 1}\right)  =  - 1,{i}_{{u}_{2}} = \frac{1}{2}\left( {{d}_{2} + {p}_{2} - 1}\right)  = 1
$$

$$
{i}_{{l}_{3}} =  - \frac{1}{2}\left( {{d}_{3} + {p}_{3} - 1}\right)  =  - 1,{i}_{{u}_{3}} = \frac{1}{2}\left( {{d}_{3} + {p}_{3} - 1}\right)  = 1
$$

$$
{i}_{{l}_{4}} =  - \frac{1}{2}\left( {{d}_{4} + {p}_{4} - 1}\right)  =  - 1,{i}_{{u}_{4}} = \frac{1}{2}\left( {{d}_{4} + {p}_{4} - 1}\right)  = 1
$$

The constraint is then

$$
\mathop{\sum }\limits_{{{i}_{1} =  - 1}}^{1}\mathop{\sum }\limits_{{{i}_{1} =  - 1}}^{1}\mathop{\sum }\limits_{{{i}_{3} =  - 1}}^{1}\mathop{\sum }\limits_{{{i}_{4} =  - 1}}^{1}{c}_{{i}_{1},{i}_{2},{i}_{3},{i}_{4}}{i}_{1}^{{n}_{1}}{i}_{2}^{{n}_{2}}{i}_{3}^{{n}_{3}}{i}_{4}^{{n}_{4}} = \left\{  \begin{array}{ll} 1 & {n}_{1} = 1 \land  {n}_{2} = 1 \land  {n}_{3} = 1 \land  {n}_{4} = 1 \\  0 & \text{ otherwise } \end{array}\right.
$$

By utilizing Algorithm 42, we can set up $A$ and $b$ and solve for $c$ where

$$
\mathbf{c} = \left( \begin{matrix} {c}_{0} \\  {c}_{1} \\  \vdots \\  {c}_{N - 2} \\  {c}_{N - 1} \end{matrix}\right)
$$

as mentioned earlier $N = \left( {{d}_{1} + {p}_{1}}\right)  \times  \cdots  \times  \left( {{d}_{k} + {p}_{k}}\right)$ . To save space we just show non-zero elements of $c$ with the corresponding indices.

$$
\left\lbrack  \begin{matrix} {c}_{0} = \frac{1}{16}, & {c}_{2} =  - \frac{1}{16}, & {c}_{6} =  - \frac{1}{16}, & {c}_{8} = \frac{1}{16} \\  {c}_{18} =  - \frac{1}{16}, & {c}_{20} = \frac{1}{16}, & {c}_{24} = \frac{1}{16}, & {c}_{26} =  - \frac{1}{16} \\  {c}_{54} =  - \frac{1}{16}, & {c}_{56} =  - \frac{1}{16}, & {c}_{60} = \frac{1}{16}, & {c}_{62} =  - \frac{1}{16} \\  {c}_{72} = \frac{1}{16}, & {c}_{74} =  - \frac{1}{16}, & {c}_{78} =  - \frac{1}{16}, & {c}_{80} = \frac{1}{16} \end{matrix}\right\rbrack
$$