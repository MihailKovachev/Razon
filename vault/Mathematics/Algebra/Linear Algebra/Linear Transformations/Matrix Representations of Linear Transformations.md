>[!THEOREM] Theorem: Matrix Representation of a Linear Transformation
>
>Every [linear transformation](Linear%20Transformation.md) $T: V \to W$ from the [vector space](../Vector%20Spaces/Vector%20Space.md) $(V,F,+,\cdot)$ in the [vector space](../Vector%20Spaces/Vector%20Space.md) $(W,F,+,\cdot)$ can be represented as a [matrix](../Matrices/Matrix.md) $M_T\in F^{\dim(W)\times \dim(V)}$.
> 
>Let $B_V$ and $B_W$ be [ordered bases](../Vector%20Spaces/Bases/Ordered%20Basis.md) of $V$ and $W$, respectively. For every $\mathbf{v}\in V$, we have
> 
>$$
>{}_{B_W} T(\mathbf{v}) = M_T\cdot {}_{B_V}\mathbf{v},
>$$
> 
>where ${}_{B_V}\mathbf{v}$ is the [coordinate vector](../Vector%20Spaces/Bases/Coordinate%20Vector.md) of $\mathbf{v}$ with respect to $B_V$ and ${}_{B_W} T(\mathbf{v})$ is the [coordinate vector](../Vector%20Spaces/Bases/Coordinate%20Vector.md) with respect to $B_W$ of the vector $T(\mathbf{v}) \in W$ which is the result of applying $T$ to $\mathbf{v}$.
>
>>[!WARNING] Warning: Dependence on the Choice of Bases
>>
>>The [matrix](../Matrices/Matrix.md) $M_T$ depends on the choice of $B_V$ and $B_W$ - different [bases](../Vector%20Spaces/Bases/Ordered%20Basis.md) will make the coefficients of $M_T$ different. To make this clear, we usually denote $M_T$ as ${}_{B_{W}}[M_T]_{B_{V}}$.
>>
>

>[!ALGORITHM] Algorithm: Finding the Matrix Representation
>
>Let $(V,F,+,\cdot)$ and $(W,F,+,\cdot)$ be two [vector spaces](../Vector%20Spaces/Vector%20Space.md) and let $T: V \to W$ be a [linear transformation](Linear%20Transformation.md) from $V$ to $W$.
>
>We want to find the [matrix representation](Matrix%20Representations%20of%20Linear%20Transformations.md) ${}_{B_W}[M_T]$ with respect to the [bases](../Vector%20Spaces/Bases/Ordered%20Basis.md) of our choice - $B_V = (\mathbf{b}_1^V,\cdots,\mathbf{b}_m^V)$ for $V$ and $B_W = (\mathbf{b}_1^W,\cdots,\mathbf{b}_n^W)$ for $W$. 
> 
>1. Determine the effect of $T$ on the elements of $B_V$, i.e. 
>
>$$\mathbf{w}_1 = T(\mathbf{b}_1^V) \qquad \cdots \qquad \mathbf{w}_m = T(\mathbf{b}_m^V)$$
>
>2. Determine the [coordinate vector](../Vector%20Spaces/Bases/Coordinate%20Vector.md) ${}_{B_W}\mathbf{w}_1,\cdots,{}_{B_W}\mathbf{w}_m$ of $\mathbf{w}_1,\cdots,\mathbf{w}_n$ with respect to $B_W$.
>	- There is no general process for this - it is different for each [vector space](../Vector%20Spaces/Vector%20Space.md).
>
>3. Construct ${}_{B_W}[M_T]$ by using the [coordinate vectors](../Vector%20Spaces/Bases/Coordinate%20Vector.md) ${}_{B_W}\mathbf{w}_1,\cdots, {}_{B_W}\mathbf{w}_m$ as its columns:
>
>$$
>{}_{B_W}[M_T]_{B_V} = \begin{bmatrix}\vert & \vert & \vert \\ {}_{B_W}\mathbf{w}_1 & \cdots & {}_{B_W}\mathbf{w}_m \\ \vert & \vert & \vert \end{bmatrix} = \begin{bmatrix}\vert & \vert & \vert \\ {}_{B_W}T(\mathbf{b}_1^V) & \cdots & {}_{B_W}T(\mathbf{b}_m^V) \\ \vert & \vert & \vert \end{bmatrix}
>$$
> 
>>[!EXAMPLE]-
>>
>>TODO
>>
>