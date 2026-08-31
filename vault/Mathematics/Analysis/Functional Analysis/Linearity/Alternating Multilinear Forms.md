---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Alternating Multilinear Forms

>[!DEFINITION] Definition: Alternating Multilinear Forms
>
>A [multilinear form](./Multilinear%20Forms.md) $f: V^n \to F$ is **alternating** if for all $\mathbf{v}_1, \dotsc, \mathbf{v}_n \in V$ we have
>
>$$
>\mathbf{v}_i = \mathbf{v}_j \text{ with } i \ne j \implies f(\mathbf{v}_1, \dotsc, \mathbf{v}_n) = 0.
>$$
>
>>[!INTUITION]
>>
>>A [multilinear form](./Multilinear%20Forms.md) is [alternating](./Alternating%20Multilinear%20Forms.md) if it is zero whenever any two of its arguments are equal.
>>
>

>[!THEOREM] Theorem: Argument Swap $\implies$ Sign Change
>
>Let $f: V^n \to F$ be a [multilinear form](./Multilinear%20Forms.md).
>
>If $f$ is [alternating](./Alternating%20Multilinear%20Forms.md), then
>
>$$
>f(\mathbf{v}_1, \dotsc, \mathbf{v}_i, \dotsc, \mathbf{v}_j, \dotsc, \mathbf{v}_n) = -f(\mathbf{v}_1, \dotsc, \mathbf{v}_j, \dotsc, \mathbf{v}_i, \dotsc, \mathbf{v}_n)
>$$
>
>for all $i, j \in \{1, \dotsc, n\}$ with $i \ne j$.
>
>>[!INTUITION]
>>
>>Swapping any two arguments of an [alternating multilinear form](./Alternating%20Multilinear%20Forms.md) switches the sign of the result.
>>
>
>>[!PROOF]-
>>
>>Since $f$ is [alternating](./Alternating%20Multilinear%20Forms.md), we have
>>
>>$$
>>f(\dotsc, \mathbf{u} + \mathbf{w}, \dotsc, \mathbf{u} + \mathbf{w}, \dotsc) = 0
>>$$
>>
>>for all $\mathbf{u}, \mathbf{w} \in V$. Furthermore, since $f$ is a [multilinear form](./Multilinear%20Forms.md), we have the following:
>>
>>$$
>>\begin{aligned} f(\dotsc, \mathbf{u} + \mathbf{w}, \dotsc, \mathbf{u} + \mathbf{w}, \dotsc) & = f(\dotsc, \mathbf{u}, \dotsc, \mathbf{u} + \mathbf{w}, \dotsc)  + f(\dotsc, \mathbf{w}, \dotsc, \mathbf{u} + \mathbf{w}, \dotsc) \\ & = f(\dotsc, \mathbf{u}, \dotsc, \mathbf{u}, \dotsc) + f(\dotsc, \mathbf{u}, \dotsc, \mathbf{w}, \dotsc) + f(\dotsc, \mathbf{w}, \dotsc, \mathbf{u}, \dotsc) + f(\dotsc, \mathbf{w}, \dotsc, \mathbf{w}, \dotsc) \\ & = 0 + f(\dotsc, \mathbf{u}, \dotsc, \mathbf{w}, \dotsc) + f(\dotsc, \mathbf{w}, \dotsc, \mathbf{u}, \dotsc) + 0\end{aligned}
>>$$
>>
>>Combining the two results, we obtain 
>>
>>$$
>>f(\dotsc, \mathbf{u}, \dotsc, \mathbf{w}, \dotsc) + f(\dotsc, \mathbf{w}, \dotsc, \mathbf{u}, \dotsc) = 0
>>$$
>>
>>and so
>>
>>$$
>>f(\dotsc, \mathbf{u}, \dotsc, \mathbf{w}, \dotsc) = - f(\dotsc, \mathbf{w}, \dotsc, \mathbf{u}, \dotsc)
>>$$
>>
>>for all $\mathbf{u}, \mathbf{v} \in V$.
>>
>

>[!THEOREM] Theorem: Linear Dependence $\implies$ Zero
>
>Let $f: V^n \to F$ be an [alternating](./Alternating%20Multilinear%20Forms.md) [multilinear form](./Multilinear%20Forms.md).
>
>If $\mathbf{v}_1, \dotsc, \mathbf{v}_n \in V$ are [linearly dependent](../../../Algebra/Vector%20Spaces/Linear%20Combinations.md#Linear%20Dependence), then $f(\mathbf{v}_1, \dotsc, \mathbf{v}_n) = 0$.
>
>>[!PROOF]-
>>
>>Since $\mathbf{v}_1, \dotsc, \mathbf{v}_n$ are [linearly dependent](../../../Algebra/Vector%20Spaces/Linear%20Combinations.md#Linear%20Dependence), we know that at least one of $\mathbf{v}_1, \dotsc, \mathbf{v}_n$ can be represented as a [linear combination](../../../Algebra/Vector%20Spaces/Linear%20Combinations.md) of the others. Assume, without loss of generality, that this is $\mathbf{v}_n$:
>>
>>$$
>>\mathbf{v}_n = \sum_{i = 1}^{n-1} \lambda_i \mathbf{v}_i
>>$$
>>
>>Since $f$ is [multilinear](./Multilinear%20Transformations.md), we have the following:
>>
>>$$
>>f\left(\mathbf{v}_1, \dotsc, \mathbf{v}_{n-1}, \sum_{i = 1}^{n-1} \lambda_i \mathbf{v}_i\right) = \sum_{i=1}^{n-1} \lambda_i f\left(\mathbf{v}_1, \dotsc, \mathbf{v}_{n-1}, \mathbf{v}_i\right)
>>$$
>>
>>For each term, $\mathbf{v}_i$ appears twice in $f$ - once at position $i$ and once at position $n$. Since $f$ is [alternating](./Alternating%20Multilinear%20Forms.md), this makes every term equal to zero.
>>
>

>[!THEOREM] Theorem: Basis $\implies$ Unique Alternating Multilinear Form
>
>Let $f, g: V^n \to F$ be [alternating multilinear forms](./Alternating%20Multilinear%20Forms.md).
>
>If $V$ is $n$-[dimensional](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) and $\mathbf{b}_1, \dotsc, \mathbf{b}_n \in V$ are a [basis](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) for $V$ and $f(\mathbf{b}_1, \dotsc, \mathbf{b}_n) = g(\mathbf{b}_1, \dotsc, \mathbf{b}_n)$, then $f = g$.
>
>>[!PROOF]-
>>
>>TODO
>>
>