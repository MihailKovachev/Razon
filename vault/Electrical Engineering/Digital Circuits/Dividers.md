---
tags:
    - digital-circuits
    - electrical-engineering
---

# Dividers

## Integer Dividers

>[!DEFINITION] Definition: Integer Dividers
>
>An **integer divider** is a [divider](./Dividers.md) which can compute the [division with remainder] of two [integers](TODO).
>

$$\text{Dividend} / \text{Divisor} = \text{Quotient} (\text{Remainder})$$

### Array Divider

An **array divider** is a [combinational circuit](./Combinational%20Circuits.md) which can be used  to compute the [division](TODO) of two [integers](TODO) in [unsigned binary representation](../../Computer%20Science/Data%20Representation/Integers.md). It essentially implements the following algorithm:

>[!ALGORITHM] Algorithm: Restoring Division of Unsigned Binary Integers
>
>We want to compute the quotient $Q = (Q[n-1],\dotsc, Q[0])$ and remainder $R$ of dividing an unsigned binary dividend $A = (A[n-1],\dotsc, A[0])$ by a divisor $B = (B[n-1],\dotsc, B[0])$.
>
>1. Initialize a partial remainder $\rho$ to $0$.
>2. For each $i \in n-1,\dotsc,0$:
>
>    - Shift $\rho$ one bit to the left ($\rho \leftarrow 2 \rho$) and fill the gap with $A[i]$.
>    - Subtract $B$ from $\rho$ and call the result $D$.
>    
>        - If $\rho - B \ge 0$ (no borrow): Set quotient bit $q_i = 1$ and update partial remainder $P \leftarrow D$.
>        - If $\rho - B < 0$ (borrow occurs): Set quotient bit $q_i = 0$ and restore partial remainder $P$ (keep previous value).
>
>$$A = Q \cdot B + R$$
>
>![Combinational Division Algorithm](./res/Dividers/Combinational%20Division%20Algorithm.svg)
>

>[!ALGORITHM] Algorithm: Sequential Divider
>
>We want to perform the division
>
>$$x / y = q \text{ with remainder } r,$$
>
>where $x$ and $y$ have $n$ bits.
>
>1. Initialization
>
>    - Initialize a $2n$-bit remainder register $R$ whose $n$ least significant bits are the bits of $x$ and whose $n$ most significant bits are all $0$.
>
>    $$R[2n-1],\dotsc, R[n] \leftarrow 0,\dotsc,0$$
>
>    $$R[n-1],\dotsc,R[0] \leftarrow x[n-1],\dotsc,x[0]$$
>
>    - Initialize an $n$-bit divisor register $D$ with $y$.
>
>    $$D[n-1],\dotsc,D[0] \leftarrow y[n-1],\dotsc,y[0]$$
>
>2. Iterate the following steps $n$ times:
>
>    - Shift $R$ one place to the left, filling the gap with zero.
>    - If the result of the subtraction $R[2n-1]\cdots R[n] - D$ is non-negative, then set $R[0]$ to $1$ and store the result of the subtraction into $R[2n-1]\cdots R[n]$. Otherwise, do nothing.
>    - Proceed to the next iteration.
>
>3. At the end, the quotient $q$ is $R[n-1]\cdots R[0]$ and the remainder $r$ is $R[2n-1]\cdots R[n]$.
>
>>[!WARNING]
>>
>>This works only with [unsigned fixed-point numbers](TODO).
>>
>