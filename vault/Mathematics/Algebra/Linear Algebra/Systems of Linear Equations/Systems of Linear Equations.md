---
tags:
  - linear-algebra
  - algebra
  - mathematics
---

# Systems of Linear Equations

>[!DEFINITION] Definition: System of Linear Equations
>
>A **system of** $m$ **linear equations** with $n$ unknowns $x_1, \cdots, x_n$ over some [field](../../Fields/Fields.md) $F$ is a [set](../../../Set%20Theory/Sets.md) of $m$ [equations](../../Equations/Equation.md) which can be expressed in the following way:
>
>$$
>\left|\begin{aligned}a_{11}x_1 + \cdots + a_{1n}x_n &= b_1 \\ a_{21}x_1+\cdots+a_{2n}x_n &= b_2 \\\vdots \hphantom{+++++++}\vdots \\ a_{m1}x_1 + \cdots + a_{mn}x_n &= b_m\end{aligned}\right. \qquad \text{ where } a_{ij}, b_{i} \in F
>$$
>
>>[!DEFINITION] Definition: Coefficient Matrix
>>
>>The **coefficient matrix** of the [system of linear equations](./Systems%20of%20Linear%20Equations.md) is the $m\times n$-[matrix](../../Matrices/Matrices.md) $A \in F^{m \times n}$ whose entries are the coefficients before the unknowns:
>>
>>$$
>>A = \begin{bmatrix}a_{11} & \cdots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \cdots & a_{mn}\end{bmatrix}
>>$$
>>
>
>>[!DEFINITION] Definition: Augmented Matrix
>>
>>The **augmented matrix** of the [system of linear equations](./Systems%20of%20Linear%20Equations.md) is its [coefficient](./Systems%20of%20Linear%20Equations.md) with an additional column containing the values $b_1, \cdots, b_m$ on the right-hand side of the equations:
>>
>>$$
>>\begin{bmatrix}a_{11} & \cdots & a_{1n} & b_1 \\ \vdots & \ddots & \vdots & \vdots \\ a_{m1} & \cdots & a_{mn} & b_m\end{bmatrix}
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>(A\mid \boldsymbol{b}) \qquad \left[\begin{array}{ccc|c} a_{11} & \cdots & a_{1n} & b_1\\ \vdots & \ddots & \vdots & \vdots \\ a_{m1} & \cdots & a_{mn} &b_m\end{array}\right]
>>>$$
>>>
>>
>
>
>>[!TIP] Tip: Matrix Form of a System of Linear Equations
>>
>>The [system of linear equations](./Systems%20of%20Linear%20Equations.md) is equivalent to a [matrix](../../Matrices/Matrices.md) equation
>>
>>$$
>>A \boldsymbol{x} = \boldsymbol{b},
>>$$
>>
>>where $A$ is its [coefficient matrix](./Systems%20of%20Linear%20Equations.md), $\boldsymbol{x} = \begin{bmatrix}x_1 & \cdots & x_n\end{bmatrix}^\mathsf{T}$ and $\boldsymbol{b} = \begin{bmatrix}b_1 & \cdots & b_m\end{bmatrix}^\mathsf{T}$.
>>
>

>[!DEFINITION] Definition: Homogeneity
>
>A [system of linear equations](./Systems%20of%20Linear%20Equations.md) $A \boldsymbol{x} = \boldsymbol{b}$ is **homogeneous** if $\boldsymbol{b} = \boldsymbol{0}$.
>

## Solvability

>[!DEFINITION] Definition: Solution of a System of Linear Equations
>
>A **solution** of a [system of linear equation](./Systems%20of%20Linear%20Equations.md) with $n$ unknowns is any $n$-[tuple](../../../Set%20Theory/Tuples.md) $(l_1, \cdots, l_n)$ such that substituting $l_k$ for the $k$-th unknown variable results in all equations of the system being satisfied.
>
>>[!DEFINITION] Definition: Solution Set
>>
>>The **solution set** of a [system of linear equation](./Systems%20of%20Linear%20Equations.md) is the [set](../../../Set%20Theory/Sets.md) of all its [solutions](./Systems%20of%20Linear%20Equations.md).
>>
>
>>[!DEFINITION] Definition: Solvability
>>
>>A [system of linear equation](./Systems%20of%20Linear%20Equations.md) is **solvable** if it has at least one [solution](./Systems%20of%20Linear%20Equations.md).
>>
>

>[!THEOREM] Theorem: Solvability of a System of Linear Equations
>
>A [system of linear equation](./Systems%20of%20Linear%20Equations.md) is [solvable](#Solvability) if and only if its [coefficient matrix](./Systems%20of%20Linear%20Equations.md) $A$ and its [augmented matrix](./Systems%20of%20Linear%20Equations.md) $(A\mid \boldsymbol{b})$ have the same [rank](../../Matrices/Matrices.md#Matrix%20Spaces).
>
>$$
>\operatorname{rank}(A) = \operatorname{rank}(A\mid\boldsymbol{b})
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!ALGORITHM] Algorithm: Gauss-Jordan Elimination
>
>The **Gauss-Jordan elimination** algorithm allows us to determine the solutions of a [system of linear equations](./Systems%20of%20Linear%20Equations.md).
>
>1. Notate the [augmented matrix](./Systems%20of%20Linear%20Equations.md) $(A|\boldsymbol{b})$.
>
>2. Bring $(A|\boldsymbol{b})$ into [reduced row echelon form](./Row%20Echelon%20Forms.md) via [elementary row operations](../../Matrices/Elementary%20Matrix%20Operations.md).
>	- Make the pivot of the $k$-th row equal to $1$ by multiplying the row with an appropriate constant. Then add an appropriate multiple of the $k$-th row to every row below it in order to obtain only $0$s below its pivot.
>	
>3. Examine the solution space of the system:
>	- If a row of the form $\begin{bmatrix}0 & \cdots & 0 \mid \ast\end{bmatrix}$, where $\ast \ne 0$, appears at any step of the process, then the [system of linear equations](./Systems%20of%20Linear%20Equations.md) has no solutions.
>	- If the resultant [coefficient matrix](./Systems%20of%20Linear%20Equations.md) $A$ has only $1$s on the diagonal and $0$s everywhere else, then system has a unique solution and the last entry in the $k$-th row of the resultant [augmented matrix](./Systems%20of%20Linear%20Equations.md) $(A\mid \boldsymbol{b})$ is the value for the $k$-th unknown $x_k$.
>	- If the resultant [augmented matrix](./Systems%20of%20Linear%20Equations.md) $(A\mid \boldsymbol{b})$ has one or more all-zero rows, then the system has infinitely many solutions.
>
>>[!EXAMPLE]-
>>
>>TODO
>>
>