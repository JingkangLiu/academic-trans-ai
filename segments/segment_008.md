and thus

$$
{f}^{\left( 3\right) }\left( x\right)  = \frac{3!}{{h}^{3}}\mathop{\sum }\limits_{{i = 0}}^{4}{c}_{i}f\left( {x + {ih}}\right)  + O\left( {h}^{p}\right)  \tag{C.4}
$$

$$
= \frac{-{5f}\left( x\right)  + {18f}\left( {x + h}\right)  - {24f}\left( {x + {2h}}\right)  + {14f}\left( {x + {3h}}\right)  - {3f}\left( {x + {4h}}\right) }{2{h}^{3}} + O\left( {h}^{2}\right)
$$

Example 62 Central difference approximation of second derivative of order 3

For this example we have $d = 2$ and $p = 3, n = 0,1,\ldots , d + p - 1 = 4$ , and for central difference ${i}_{l} =  - 2$ , and ${i}_{u} = 2$ .

$$
\mathop{\sum }\limits_{{i =  - 2}}^{2}{c}_{i}{i}^{n} = \left\{  \begin{array}{ll} 1 & n = 2 \\  0 & n \neq  2 \end{array}\right.
$$

In matrix form that is

$$
\left\lbrack  \begin{matrix} {\left( -2\right) }^{0} & {\left( -1\right) }^{0} & {0}^{0} & {1}^{0} & {2}^{0} \\  {\left( -2\right) }^{1} & {\left( -1\right) }^{1} & {1}^{1} & {1}^{1} & {2}^{1} \\  {\left( -2\right) }^{2} & {\left( -1\right) }^{2} & {0}^{2} & {1}^{2} & {2}^{2} \\  {\left( -2\right) }^{3} & {\left( -1\right) }^{3} & {0}^{3} & {1}^{3} & {2}^{3} \\  {\left( -2\right) }^{4} & {\left( -1\right) }^{4} & {0}^{4} & {1}^{4} & {2}^{4} \end{matrix}\right\rbrack  \left\lbrack  \begin{matrix} {c}_{-2} \\  {c}_{-1} \\  {c}_{0} \\  {c}_{1} \\  {c}_{2} \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix} 0 \\  0 \\  1 \\  0 \\  0 \end{matrix}\right\rbrack   \Rightarrow  \left\lbrack  \begin{matrix} {c}_{-2} \\  {c}_{-1} \\  {c}_{0} \\  {c}_{1} \\  {c}_{2} \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix}  - 1/{24} \\  2/3 \\   - 5/4 \\  2/3 \\   - 1/{24} \end{matrix}\right\rbrack
$$

Thus

$$
{f}^{\left( 2\right) }\left( x\right)  = \frac{2!}{{h}^{2}}\mathop{\sum }\limits_{{i =  - 2}}^{2}{c}_{i}f\left( {x + {ih}}\right)  + O\left( {h}^{p}\right)  \tag{C.5}
$$

$$
= \frac{-f\left( {x - {2h}}\right)  + {16f}\left( {x - h}\right)  - {30f}\left( x\right)  + {16f}\left( {x + h}\right)  - f\left( {x + {2h}}\right) }{{12}{h}^{2}} + O\left( {h}^{3}\right)
$$

Derivative Approximation by Finite Differences in Higher Dimensional Case

#### C.2.2 Two-dimensional Examples

Example 63 Central difference approximation of cross derivative $\frac{{\partial }^{2}f\left( {{x}_{1},{x}_{2}}\right) }{\partial {x}_{1}\partial {x}_{2}}$ of second order in both ${x}_{1}$ and ${x}_{2}$

Assume we want to compute the forward difference approximation of $\frac{{\partial }^{2}f\left( {{x}_{1},{x}_{2}}\right) }{\partial {x}_{1}\partial {x}_{2}}$ with $O\left( {h}_{1}^{2}\right)  +$ $O\left( {h}_{2}^{2}\right)$ . Thus we have ${d}_{1} = 1,{d}_{2} = 1,{p}_{1} = 2$ and ${p}_{2} = 2$ , and because we want a central difference we have ${i}_{{l}_{1}} =  - \frac{1}{2}\left( {{d}_{1} + {p}_{1} - 1}\right)  =  - 1,{i}_{{u}_{1}} = \frac{1}{2}\left( {{d}_{1} + {p}_{1} - 1}\right)  = 1,{i}_{{l}_{2}} =  - \frac{1}{2}\left( {{d}_{2} + {p}_{2} - 1}\right)  =$ $- 1,{i}_{{u}_{2}} = \frac{1}{2}\left( {{d}_{2} + {p}_{2} - 1}\right)  = 1,{n}_{1} = 0,\ldots ,{d}_{1} + {p}_{1} - 1 = 2$ , and ${n}_{2} = 0,\ldots ,{d}_{2} + {p}_{2} - 1 = 2$ . The constraint is then

$$
\mathop{\sum }\limits_{{{i}_{1} =  - 1}}^{1}\mathop{\sum }\limits_{{{i}_{2} =  - 1}}^{1}{c}_{{i}_{1},{i}_{2}}{i}_{1}^{{n}_{1}}{i}_{2}^{{n}_{2}} = \left\{  \begin{array}{ll} 1 & {n}_{1} = 1 \land  {n}_{2} = 1 \\  0 & \text{ otherwise } \end{array}\right.
$$

In a matrix form this would be![0195247f-2f23-7bdd-9335-9204d62fe613_581_182_739_1274_445_0.jpg](images/0195247f-2f23-7bdd-9335-9204d62fe613_581_182_739_1274_445_0.jpg)

$$
\times  \left\lbrack  \begin{matrix} {c}_{-1, - 1} \\  {c}_{-1,0} \\  {c}_{-1, + 1} \\  {c}_{0, - 1} \\  {c}_{0,0} \\  {c}_{0, + 1} \\  {c}_{+1, - 1} \\  {c}_{+1,0} \\  {c}_{+1,0} \\  {c}_{+1,0} \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix} 0 \\  0 \\  0 \\  0 \\  1 \\  0 \\  0 \\  0 \\  0 \\  0 \end{matrix}\right\rbrack
$$

Or equivalently