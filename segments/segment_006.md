$$
+ O\left( {h}_{1}^{{p}_{1}}\right)  + O\left( {h}_{2}^{{p}_{2}}\right)  + \cdots  + O\left( {h}_{k}^{{p}_{k}}\right)
$$

where ${\widehat{c}}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}}$ are the unknown coefficients that we are looking for, ${i}_{{l}_{j}}$ and ${i}_{{u}_{j}}$ are the number of backward and forward terms in ${x}_{j}$ -direction in our approximation . If we multiply by $\frac{{h}_{1}^{{d}_{1}}}{{d}_{1}!}\frac{{h}_{2}^{{d}_{2}}}{{d}_{2}!}\ldots \frac{{h}_{k}^{{d}_{k}}}{{d}_{k}!}$ and define ${c}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}} = {\widehat{c}}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}}\frac{{h}_{1}^{{d}_{1}}}{{d}_{1}!}\frac{{h}_{2}^{{d}_{2}}}{{d}_{2}!}\ldots \frac{{h}_{k}^{{d}_{k}}}{{d}_{k}!}$ , we get

$$
\frac{{h}_{1}^{{d}_{1}}}{{d}_{1}!}\frac{{h}_{2}^{{d}_{2}}}{{d}_{2}!}\ldots \frac{{h}_{k}^{{d}_{k}}}{{d}_{k}!}\frac{{\partial }^{d}f\left( {{x}_{1},{x}_{2},\ldots ,{x}_{k}}\right) }{\partial {x}_{1}^{{d}_{1}}\partial {x}_{2}^{{d}_{2}}\ldots \partial {x}_{k}^{{d}_{k}}} + O\left( {h}_{1}^{{p}_{1} + {d}_{1}}\right)  + O\left( {h}_{2}^{{p}_{2} + {d}_{2}}\right)  + \cdots  + O\left( {h}_{k}^{{p}_{k} + {d}_{k}}\right)
$$

$$
= \mathop{\sum }\limits_{{{i}_{1} = {i}_{{l}_{1}}}}^{{i}_{{u}_{1}}}\mathop{\sum }\limits_{{{i}_{2} = {i}_{{l}_{2}}}}^{{i}_{{u}_{2}}}\cdots \mathop{\sum }\limits_{{{i}_{k} = {i}_{{l}_{k}}}}^{{i}_{{u}_{k}}}{c}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}}f\left( {{x}_{1} + {i}_{1}{h}_{1},{x}_{2} + {i}_{2}{h}_{2},\ldots ,{x}_{k} + {i}_{k}{h}_{k}}\right)  \tag{C.2}
$$

Substituting (C.1) into (C.2) we obtain

$$
\frac{{h}_{1}^{{d}_{1}}}{{d}_{1}!}\frac{{h}_{2}^{{d}_{2}}}{{d}_{2}!}\ldots \frac{{h}_{k}^{{d}_{k}}}{{d}_{k}!}\frac{{\partial }^{d}f\left( {{x}_{1},{x}_{2},\ldots ,{x}_{k}}\right) }{\partial {x}_{1}^{{d}_{1}}\partial {x}_{2}^{{d}_{2}}\ldots \partial {x}_{k}^{{d}_{k}}} + O\left( {h}_{1}^{{p}_{1} + {d}_{1}}\right)  + O\left( {h}_{2}^{{p}_{2} + {d}_{2}}\right)  + \cdots  + O\left( {h}_{k}^{{p}_{k} + {d}_{k}}\right)
$$

$$
= \mathop{\sum }\limits_{{{i}_{1} = {i}_{{l}_{1}}}}^{{i}_{{u}_{1}}}\cdots \mathop{\sum }\limits_{{{i}_{k} = {i}_{{l}_{k}}}}^{{i}_{{u}_{k}}}{c}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}}\mathop{\sum }\limits_{{{n}_{1} = 0}}^{\infty }\cdots \mathop{\sum }\limits_{{{n}_{k} = 0}}^{\infty }\frac{1}{{n}_{1}!}\ldots \frac{1}{{n}_{k}!}{\left( {i}_{1}{h}_{1}\right) }^{{n}_{1}}\ldots {\left( {i}_{k}{h}_{k}\right) }^{{n}_{k}}\frac{{\partial }^{n}f\left( {{x}_{1},\ldots ,{x}_{k}}\right) }{\partial {x}_{1}^{{n}_{1}}\cdots \partial {x}_{k}^{{n}_{k}}}
$$

$$
= \mathop{\sum }\limits_{{{i}_{1} = {i}_{{l}_{1}}}}^{{i}_{{u}_{1}}}\cdots \mathop{\sum }\limits_{{{i}_{k} = {i}_{{l}_{k}}}}^{{i}_{{u}_{k}}}{c}_{{i}_{1},{i}_{2},\ldots ,{i}_{k}}\mathop{\sum }\limits_{{{n}_{1} = 0}}^{{{p}_{1} + {d}_{1} - 1}}\cdots \mathop{\sum }\limits_{{{n}_{k} = 0}}^{{{p}_{k} + {d}_{k} - 1}}\frac{1}{{n}_{1}!}\ldots \frac{1}{{n}_{k}!}{\left( {i}_{1}{h}_{1}\right) }^{{n}_{1}}\ldots {\left( {i}_{k}{h}_{k}\right) }^{{n}_{k}}
$$

$$
\times  \frac{{\partial }^{n}f\left( {{x}_{1},\ldots ,{x}_{k}}\right) }{\partial {x}_{1}^{{n}_{1}}\cdots \partial {x}_{k}^{{n}_{k}}} + O\left( {h}_{1}^{{p}_{1} + {d}_{1}}\right)  + \cdots  + O\left( {h}_{k}^{{p}_{k} + {d}_{k}}\right)
$$

multiplying by $\frac{{d}_{1}!}{{h}_{1}^{{d}_{1}}}\frac{{d}_{2}!}{{h}_{2}^{{d}_{2}}}\ldots \frac{{d}_{k}!}{{h}_{k}^{{d}_{k}}}$ we can see that

$$
\frac{{\partial }^{d}f\left( {{x}_{1},{x}_{2},\ldots ,{x}_{k}}\right) }{\partial {x}_{1}^{{d}_{1}}\partial {x}_{2}^{{d}_{2}}\ldots \partial {x}_{k}^{{d}_{k}}}
$$

$$
= \frac{{d}_{1}!}{{h}_{1}^{{d}_{1}}}\cdots \frac{{d}_{k}!}{{h}_{k}^{{d}_{k}}}\mathop{\sum }\limits_{{{i}_{1} = {i}_{{l}_{1}}}}^{{i}_{{u}_{1}}}\cdots \mathop{\sum }\limits_{{{i}_{k} = {i}_{{l}_{k}}}}^{{i}_{{u}_{k}}}{c}_{{i}_{1},\ldots ,{i}_{k}}\mathop{\sum }\limits_{{{n}_{1} = 0}}^{{{p}_{1} + {d}_{1} - 1}}\cdots \mathop{\sum }\limits_{{{n}_{k} = 0}}^{{{p}_{k} + {d}_{k} - 1}}\frac{1}{{n}_{1}!}\cdots \frac{1}{{n}_{k}!}{\left( {i}_{1}{h}_{1}\right) }^{{n}_{1}}\ldots {\left( {i}_{k}{h}_{k}\right) }^{{n}_{k}}
$$

$$
\times  \frac{{\partial }^{n}f\left( {{x}_{1},\ldots ,{x}_{k}}\right) }{\partial {x}_{1}^{{n}_{1}}\cdots \partial {x}_{k}^{{n}_{k}}} + O\left( {h}_{1}^{{p}_{1} + {d}_{1}}\right)  + \cdots  + O\left( {h}_{k}^{{p}_{k} + {d}_{k}}\right)
$$

For this to be true the following constraints should hold: