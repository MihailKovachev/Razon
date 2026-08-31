---
tags:
    - algebra
    - mathematics
---

# Truth Tables

**Truth tables** are a way to define [logical connectives](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}$  by listing all possible inputs and outputs in a table. We first assign $n$ labels $x_1, \dotsc, x_n$ to the each element of the input [tuple](../../Set%20Theory/Tuples.md) from $\{0, 1\}^n$. The first row of the table contains these labels and the label $f(x_1, \dotsc, x_n)$. Each subsequent row contains a combination of possible values for the inputs $x_1, \dotsc, x_n$ and the value of the function when evaluated at those inputs.

>[!EXAMPLE] Example: Negation
>
>Consider the [negation function](./Boolean%20Functions.md) $f: \{0,1\} \to \{0,1\}$ defined as
>
>$$
>f(x) = \begin{cases} 0 \qquad \text{if } x = 1 \\ 1 \qquad \text{if } x = 0\end{cases}
>$$
>
>Its [truth table](./Boolean%20Functions.md#Truth%20Tables) is the following:
>
>|$x$|$f(x)$|
>|:--:|:--:|
>|$0$|$1$|
>|$1$|$0$|
>

>[!EXAMPLE] Example: Conjunction
>
>The [conjunction function](./Boolean%20Functions.md) $f: \{0,1\}^2 \to \{0,1\}$ is defined as
>
>$$
>f(x, y) = \begin{cases} 1 \qquad \text{if and only if } x = y = 1 \\ 0 \qquad \text{otherwise}\end{cases}
>$$
>
>Its [truth table](./Boolean%20Functions.md#Truth%20Tables) is the following:
>
>|$x$|$y$|$f(x, y)$|
>|:--:|:--:|:--:|
>|$0$|$0$|$0$|
>|$0$|$1$|$0$|
>|$1$|$0$|$0$|
>|$1$|$1$|$1$|
>