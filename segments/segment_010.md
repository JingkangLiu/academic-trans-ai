We wish to compute the forward difference approximation of $\frac{{\partial }^{2}f\left( {{x}_{1},{x}_{2}}\right) }{\partial {x}_{1}\partial {x}_{2}}$ with $O\left( {h}_{1}^{2}\right)  + O\left( {h}_{2}^{2}\right)$ . Thus we have ${d}_{1} = 1,{d}_{2} = 1,{p}_{1} = 2$ and ${p}_{2} = 2$ , and because we want a forward difference we have ${i}_{{l}_{1}} = 0,{i}_{{u}_{1}} = {d}_{1} + {p}_{1} - 1 = 2,{i}_{{l}_{2}} = 0,{i}_{{u}_{2}} = {d}_{2} + {p}_{2} - 1 = 2,{n}_{1} = 0,\ldots ,{d}_{1} + {p}_{1} - 1 = 2$ , and ${n}_{2} = 0,\ldots ,{d}_{2} + {p}_{2} - 1 = 2$ . The constraint is then

$$
\mathop{\sum }\limits_{{{i}_{1} = 0}}^{2}\mathop{\sum }\limits_{{{i}_{2} = 0}}^{2}{c}_{{i}_{1},{i}_{2}}{i}_{1}^{{n}_{1}}{i}_{2}^{{n}_{2}} = \left\{  \begin{array}{ll} 1 & {n}_{1} = 1 \land  {n}_{2} = 1 \\  0 & \text{ otherwise } \end{array}\right.
$$

In a matrix form this would be![0195247f-2f23-7bdd-9335-9204d62fe613_583_193_206_1254_342_0.jpg](images/0195247f-2f23-7bdd-9335-9204d62fe613_583_193_206_1254_342_0.jpg)

$$
= \left\lbrack  \begin{array}{l} 0 \\  0 \\  0 \\  0 \\  1 \\  0 \\  0 \\  0 \\  0 \end{array}\right\rbrack
$$

Or equivalently

$$
\left\lbrack  \begin{matrix} 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\  0 & 1 & 2 & 0 & 1 & 2 & 0 & 1 & 2 \\  0 & 1 & 4 & 0 & 1 & 4 & 0 & 1 & 4 \\  0 & 0 & 0 & 1 & 1 & 1 & 2 & 2 & 2 \\  0 & 0 & 0 & 0 & 1 & 2 & 0 & 2 & 4 \\  0 & 0 & 0 & 0 & 1 & 4 & 0 & 2 & 8 \\  0 & 0 & 0 & 1 & 1 & 1 & 4 & 4 & 4 \\  0 & 0 & 0 & 0 & 1 & 2 & 0 & 4 & 8 \\  0 & 0 & 0 & 0 & 1 & 2 & 0 & 4 & 8 \\  0 & 0 & 0 & 0 & 1 & 4 & 0 & 4 & {16} \end{matrix}\right\rbrack  \left\lbrack  \begin{matrix} {c}_{0,0} \\  {c}_{0,1} \\  {c}_{0,2} \\  {c}_{1,0} \\  {c}_{1,1} \\  {c}_{1,2} \\  {c}_{2,0} \\  {c}_{2,1} \\  {c}_{2,2} \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix} 0 \\  0 \\  0 \\  0 \\  1 \\  0 \\  0 \\  0 \\  0 \\  0 \\  {c}_{2,1} \\  {c}_{2,2} \end{matrix}\right\rbrack   \Rightarrow  \left\lbrack  \begin{matrix}  + \frac{9}{4} \\  {c}_{0,1} \\  {c}_{0,2} \\  {c}_{1,0} \\  {c}_{1,1} \\  {c}_{1,2} \\  {c}_{2,0} \\  {c}_{2,1} \\  {c}_{2,2} \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix}  + \frac{9}{4} \\   - \frac{3}{4} \\   + \frac{3}{4} \\   - 3 \\   + 4 \\  \frac{3}{4} \\   + \frac{1}{4} \\   + \frac{1}{4} \\  3 \\  3 \end{matrix}\right\rbrack
$$

As in the previous example, the alternative to this could be of the following form

$$
\left\lbrack  \begin{array}{lll} {0}^{0} & {1}^{0} & {2}^{0} \\  {0}^{1} & {1}^{1} & {2}^{1} \\  {0}^{2} & {1}^{2} & {2}^{2} \end{array}\right\rbrack  \left\lbrack  \begin{array}{lll} {c}_{0,0} & {c}_{0,1} & {c}_{0,2} \\  {c}_{1,0} & {c}_{1,1} & {c}_{1,2} \\  {c}_{2,0} & {c}_{2,1} & {c}_{2,2} \end{array}\right\rbrack  \left\lbrack  \begin{array}{lll} {0}^{0} & {0}^{1} & {0}^{2} \\  {1}^{0} & {1}^{1} & {1}^{2} \\  {2}^{0} & {2}^{1} & {2}^{2} \end{array}\right\rbrack   = \left\lbrack  \begin{array}{lll} 0 & 0 & 0 \\  0 & 1 & 0 \\  0 & 0 & 0 \end{array}\right\rbrack
$$

or

$$
\left\lbrack  \begin{array}{lll} 1 & 1 & 1 \\  0 & 1 & 2 \\  0 & 1 & 4 \end{array}\right\rbrack  \left\lbrack  \begin{array}{lll} {c}_{0,0} & {c}_{0,1} & {c}_{0,2} \\  {c}_{1,0} & {c}_{1,1} & {c}_{1,2} \\  {c}_{2,0} & {c}_{2,1} & {c}_{2,2} \end{array}\right\rbrack  \left\lbrack  \begin{array}{lll} 1 & 0 & 0 \\  1 & 1 & 1 \\  1 & 2 & 4 \end{array}\right\rbrack   = \left\lbrack  \begin{array}{lll} 0 & 0 & 0 \\  0 & 1 & 0 \\  0 & 0 & 0 \end{array}\right\rbrack
$$

multiplying by inverse of

$$
\left\lbrack  \begin{array}{lll} 1 & 1 & 1 \\  0 & 1 & 2 \\  0 & 1 & 4 \end{array}\right\rbrack
$$

from the left and multiplying by inverse of

$$
\left\lbrack  \begin{array}{lll} 1 & 0 & 0 \\  1 & 1 & 1 \\  1 & 2 & 4 \end{array}\right\rbrack
$$

from the right, we obtain

$$
\left\lbrack  \begin{array}{lll} {c}_{0,0} & {c}_{0,1} & {c}_{0,2} \\  {c}_{1,0} & {c}_{1,1} & {c}_{1,2} \\  {c}_{2,0} & {c}_{2,1} & {c}_{2,2} \end{array}\right\rbrack   = \left\lbrack  \begin{matrix} \frac{9}{4} &  - 3 & \frac{3}{4} \\   - 3 & 4 &  - 1 \\  \frac{3}{4} &  - 1 & \frac{1}{4} \end{matrix}\right\rbrack
$$