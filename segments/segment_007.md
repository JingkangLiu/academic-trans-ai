$$
\mathop{\sum }\limits_{{{i}_{1} = {i}_{{l}_{1}}}}^{{i}_{{u}_{1}}}\mathop{\sum }\limits_{{{i}_{2} = {i}_{{l}_{2}}}}^{{i}_{{u}_{2}}}\cdots \mathop{\sum }\limits_{{{i}_{k} = {i}_{{l}_{k}}}}^{{i}_{{u}_{k}}}{c}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}} = \left\{  \begin{array}{ll} 1 & {n}_{1} = {d}_{1} \land  {n}_{2} = {d}_{2} \land  \cdots  \land  {n}_{k} = {d}_{k} \\  0 & \text{ otherwise } \end{array}\right.
$$

#### C.1.1 Calculating Coefficients ${c}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}}$

Here are the findings and observations:

- The solution to these equations would be unique if and only if we limit the number of constraints in ${x}_{j}$ -direction to ${d}_{j} + {p}_{j}$ for $j = 1,\ldots , k$ . So we must have ${d}_{j} + {p}_{j} =$ ${i}_{{u}_{j}} - {i}_{{l}_{j}} + 1$ for all $j$ which restricts the number of terms we can use in our approximation

- In case of a forward difference approximation in all directions we set ${i}_{{l}_{j}} = 0,{i}_{{u}_{j}} =$ ${d}_{j} + {p}_{j} - 1$ for all $j$

- In case of a backward difference approximation in both directions we set ${i}_{{l}_{j}} =  - \left( {{d}_{j} + }\right.$ $\left. {{p}_{j} - 1}\right) ,{i}_{{u}_{j}} = 0$ for all $j$

- In case of a central difference approximation in both directions we set ${i}_{{l}_{j}} =  - \frac{1}{2}\left( {{d}_{j} + }\right.$ $\left. {{p}_{j} - 1}\right) ,{i}_{{u}_{j}} = \frac{1}{2}\left( {{d}_{j} + {p}_{j} - 1}\right)$ for all $j$

In Algorithm 42, we show how to set up the linear system ${Ac} = b$ to find vector $c$ by setting up matrix $A$ and vector $b$ . Having $A$ and $b$ , we can solve the following linear system for vector $c$ .

$$
{Ac} = b \tag{C.3}
$$

```

Algorithm 42 Algorith for finding ${c}_{{i}_{1},{i}_{2}\ldots ,{i}_{k}}$

---

Require: Set ${d}_{1},\ldots ,{d}_{k}$ and ${p}_{1},\ldots ,{p}_{k}$

Require: Allocate matrix $A$ of size $N \times  N$ where $N = \left( {{d}_{1} + {p}_{1}}\right)  \times  \cdots  \times  \left( {{d}_{k} + {p}_{k}}\right)$

Require: Allocate vector $b$ of size $N \times  1$

Require: Set ${i}_{{l}_{j}}$ and ${i}_{{u}_{j}}$ for $j = 1,\ldots , k$

	$i = 0$

	for ${n}_{1} = 0,\ldots ,{d}_{1} + {p}_{1} - 1$ do

			for ${n}_{2} = 0,\ldots ,{d}_{2} + {p}_{2} - 1$ do

				...

				for ${n}_{k} = 0,\ldots ,{d}_{k} + {p}_{k} - 1$ do

						$i \leftarrow  i + 1$

						$j \leftarrow  0$

						for ${i}_{1} = {i}_{{l}_{1}},\ldots ,{i}_{{u}_{1}}$ do

							for ${i}_{2} = {i}_{{l}_{2}},\ldots ,{i}_{{u}_{2}}$ do

									...

									for ${i}_{k} = {i}_{{l}_{k}},\ldots ,{i}_{{u}_{k}}$ do

										$j \leftarrow  j + 1$

										$A\left\lbrack  i\right\rbrack  \left\lbrack  j\right\rbrack   = {\left( {i}_{1}\right) }^{{n}_{1}} \times  {\left( {i}_{2}\right) }^{{n}_{2}} \times  \cdots  \times  {\left( {i}_{k}\right) }^{{n}_{k}}$

									end for

									. .

							end for

						end for

						if ${n}_{1} = {d}_{1} \land  {n}_{2} = {d}_{2} \land  \cdots  \land  {n}_{k} = {d}_{k}$ then

							$b\left\lbrack  i\right\rbrack   \leftarrow  1$

						else

							$b\left\lbrack  i\right\rbrack   \leftarrow  0$

						end if

				end for

				...

			end for

	end for

---
```

### C.2 Examples

We go through various different examples, starting with one-dimensional case, going to two-and three-dimensional cases.

#### C.2.1 One-dimensional Examples

Example 61 Forward difference approximation of third derivative of second order

Assume we want to compute the forward difference approximation of ${f}^{\left( 3\right) }\left( x\right)$ with $O\left( {h}^{2}\right)$ . Thus we have $d = 3$ and $p = 2, n = 0,1,\ldots , d + p - 1 = 4$ , and because we want a forward difference we have ${i}_{l} = 0$ and ${i}_{u} = 4$ . The constraint is then

$$
\mathop{\sum }\limits_{{i = 0}}^{4}{c}_{i}{i}^{n} = \left\{  \begin{array}{ll} 1 & n = 3 \\  0 & n \neq  3 \end{array}\right.
$$

In a matrix form this would be

$$
\left\lbrack  \begin{matrix} {0}^{0} & {1}^{0} & {2}^{0} & {3}^{0} & {4}^{0} \\  {0}^{1} & {1}^{1} & {2}^{1} & {3}^{1} & {4}^{1} \\  {0}^{2} & {1}^{2} & {2}^{2} & {3}^{2} & {4}^{2} \\  {0}^{3} & {1}^{3} & {2}^{3} & {3}^{3} & {4}^{3} \\  {0}^{4} & {1}^{4} & {2}^{4} & {3}^{4} & {4}^{4} \end{matrix}\right\rbrack  \left\lbrack  \begin{matrix} {c}_{0} \\  {c}_{1} \\  {c}_{2} \\  {c}_{3} \\  {c}_{4} \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix} 0 \\  0 \\  0 \\  1 \\  0 \end{matrix}\right\rbrack   \Rightarrow  \left\lbrack  \begin{matrix} {c}_{0} \\  {c}_{1} \\  {c}_{2} \\  {c}_{3} \\  {c}_{4} \end{matrix}\right\rbrack   = \left\lbrack  \begin{array}{l}  - 5/{12} \\  3/2 \\   - 2 \\  7/6 \\   - 1/4 \end{array}\right\rbrack
$$