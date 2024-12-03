>[!DEFINITION] Definition: Linear Dependence
>
>Let $\mathbf{v}_1, \cdots, \mathbf{v}_n$ be [vectors](Vector.md) in some [vector space](Vector%20Space.md) $(V,F,+,\cdot$).
>
>We say that $\mathbf{v}_1, \cdots, \mathbf{v}_n$ are **linearly dependent** iff they are not [linearly independent](Linear%20Independence.md), i.e. there exist $c_1, \cdots, c_n$ with at least one $c_i \ne 0$ such that
>
>$$
>c_1\mathbf{v}_1 + \cdots + c_n\mathbf{v}_n = \mathbf{0}
>$$
>

>[!THEOREM] Theorem: Linear Dependence $\implies$ Linear Combination
>
>If $\{ \mathbf{v}_1, \cdots, \mathbf{v}_n\} \, (n \ge 2)$ are [linearly dependent](Linear%20Dependence.md) [vectors](Vector.md), then there is at least one $\mathbf{v}_i \in \{ \mathbf{v}_1, \cdots, \mathbf{v}_n\}$  which can be expressed as a [linear combination](Linear%20Combination.md) of the rest of the [vectors](Vector.md):
>
>$$
>\mathbf{v}_i = \sum_{\begin{align*}j &= 1 \\ j &\ne i\end{align*}}^n c_j \mathbf{v}_j
>$$
>
>>[!PROOF]-
>>
>>According to the definition of linear dependence, there are coefficients $h_1, \cdots, h_n \in F$ with at least one $h_i \ne 0$ such that
>>
>>$$
>>h_1 \mathbf{v}_1 + \cdots + h_i \mathbf{v}_i + \cdots + h_n \mathbf{v}_n = \mathbf{0}
>>$$
>>
>>Let's move everything except $h_i \mathbf{v}_i$ to the other side of the equation:
>>
>>$$
>>h_i \mathbf{v}_i = -h_1\mathbf{v}_1+\cdots -h_{i-1}\mathbf{v}_{i-1}-h_{i+1}\mathbf{v}_{i+1}+\cdots+-h_n\mathbf{v}_n
>>$$
>>
>>Since $h_i \ne 0$, we can divide both sides by it:
>>
>>
>>
>>$$
>>\mathbf{v}_i = c_1\mathbf{v}_1+\cdots + c_{i-1}\mathbf{v}_{i-1}+c_{i+1}\mathbf{v}_{i+1}+\cdots+c_n\mathbf{v}_n
>>$$
>>
>>We have thus obtained $\mathbf{v}_i$ as a linear combination of the other vectors, where $c_j = -\frac{h_j}{h_i}$
>>
>