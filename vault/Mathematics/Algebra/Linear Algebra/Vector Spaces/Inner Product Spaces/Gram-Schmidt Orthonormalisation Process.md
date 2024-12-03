>[!ALGORITHM] Algorithm: Gram-Schmidt Orthonormalisation Process
>
>Every [basis](../Bases/Basis.md) $B = \{\mathbf{b}_1,\cdots,\mathbf{b}_n\}$ of a [finite-dimensional](../Bases/Dimension.md) [inner product space](Inner%20Product%20Space.md) $(V,F,+,\cdot)$ can be turned into an [orthonormal basis](Orthonormal%20Basis.md) $B' = \{\mathbf{b}_1',\cdots,\mathbf{b}_n'\}$ through the following process:
>
>1. The first vector $\mathbf{b}_1'$ in $B'$ is simply the [normalised](Canonical%20Norm.md) version of $\mathbf{b}_1$.
>
>$$
>\mathbf{b}_1' \leftarrow \frac{1}{||\mathbf{b}_1||}\mathbf{b}_1
>$$
>
>2. We construct the $k$-th element $\mathbf{b}_k'$ of $B'$ so that it is orthogonal to all the resulting basis vectors $\{\mathbf{b}_1', \cdots, \mathbf{b}_{k-1}'\}$ before it and so that its [canonical norm](Canonical%20Norm.md) is one.
>- Firstly, we ensure that $\mathbf{b}_k'$ is orthogonal to all $\{\mathbf{b}_1', \cdots, \mathbf{b}_{k-1}'\}$ by assigning it the following value.
>
>$$
>\mathbf{b}_k' \leftarrow \mathbf{b}_{k}-\sum_{i=1}^{k-1} \langle\mathbf{b}_{k},\mathbf{b}_i'\rangle \mathbf{b}_i'
>$$
>
>- We then [normalise](Canonical%20Norm.md) $\mathbf{b}_k'$ to ensure that its [norm](Canonical%20Norm.md) is one.
>
>$$
>\mathbf{b}_k' \leftarrow \frac{1}{||\mathbf{b}_k'||} \mathbf{b}_k'
>$$ 
>