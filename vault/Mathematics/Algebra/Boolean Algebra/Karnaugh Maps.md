---
tags:
    - algebra
    - mathematics
---

# Karnaugh Maps

**Karnaugh maps** are an alternative way to define and express [logical connectives](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}$. 

We first assign $n$ labels $x_0, \dotsc, x_{n-1}$ to each element of the input [tuple](../../Set%20Theory/Tuples.md) from $\{0, 1\}^n$. We then choose an index $k \in [1;n-1]$ and split the input [tuple](../../Set%20Theory/Tuples.md) $(x_0, \dotsc, x_{n-1})$ into two [tuples](../../Set%20Theory/Tuples.md) $(x_0, \dotsc, x_{k-1})$ and $(x_{k}, \dotsc, x_{n-1})$. Finally, we construct a table with $2^k$ columns and $2^{n-k}$ rows in the following way:
- We label the columns with all possible binary sequences representing numbers in the range $[0; 2^k]$. This should be done in a way so as to ensure that each combination differs by its adjacent ones only by a single input.
- We label the rows with all possible binary sequences representing numbers in the range $[0; 2^{n-k}]$. This should be done in a way so as to ensure that each combination differs by its adjacent ones only by a single input.
- The cell at the $i$-th column and the $j$-th row is filled with the value of $f$ evaluated at the concatenation of the label of the $i$-th column and the label of the $j$-th row.

A table constructed in this manner fully describes $f$ and is known as a **Karnaugh map** of $f$.

>[!EXAMPLE] Example
>
>Consider the [function](./Boolean%20Functions.md) $f:\{0,1\}^3 \to \{0,1\}$ defined in the following way:
>
>$$
>f(x, y, z) = yz + x\overline{z}
>$$
>
>If we pick $k = 2$, we split the input into $(x,y)$ and $(z)$. We construct the corresponding empty [Karnaugh map](./Karnaugh%20Maps.md):
>
>![Empty Karnaugh Map Example](./res/Empty%20Karnaugh%20Map%20Example.svg)
>
>We now evaluate $f$ at each cell, where $i$ is the column and $j$ is the row:
>
>- At $i = 1$ and $j = 1$, we have $xy = 00$ and $z = 0$. Therefore, the value of this cell is $f(000) = 0$.
>- At $i = 1$ and $j = 2$, we have $xy = 00$ and $z = 1$. Therefore, the value of this cell is $f(001) = 0$.
>- At $i = 2$ and $j = 1$, we have $xy = 01$ and $z = 0$. Therefore, the value of this cell is $f(010) = 0$.
>- At $i = 2$ and $j = 2$, we have $xy = 01$ and $z = 1$. Therefore, the value of this cell is $f(011) = 1$.
>- At $i = 3$ and $j = 1$, we have $xy = 11$ and $z = 0$. Therefore, the value of this cell is $f(110) = 1$.
>- At $i = 3$ and $j = 2$, we have $xy = 11$ and $z = 1$. Therefore, the value of this cell is $f(111) = 1$.
>- At $i = 4$ and $j = 1$, we have $xy = 10$ and $z = 0$. Therefore, the value of this cell is $f(100) = 1$.
>- At $i = 4$ and $j = j$, we have $xy = 10$ and $z = 1$. Therefore, the value of this cell is $f(101) = 0$.
>
>![Filled Karnaugh Map Example](./res/Filled%20Karnaugh%20Map%20Example.svg)
>