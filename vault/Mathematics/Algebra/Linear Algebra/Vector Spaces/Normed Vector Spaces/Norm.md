>[!DEFINITION] Definition: Norm
>
>A **norm** on a [complex](Complex%20Vector%20Space.md) or a [real](Real%20Vector%20Space.md) [vector space](Vector%20Space.md) $(V,F,+,\cdot)$ is any [function](../../../../Analysis/Functions/Functions.md) $N: V \to \mathbb{R}$ with the following properties:
>
>- $N(\mathbf{v})\ge 0$ and $N(\mathbf{v})=0\iff \mathbf{v}=\mathbf{0}$ for all $\mathbf{v}\in V$
>- $N(\lambda\mathbf{v}) = |\lambda|\cdot N(\mathbf{v})$ for all $\lambda\in F,\mathbf{v}\in V$
>- $N(\mathbf{u}+\mathbf{v})\le N(\mathbf{u})+N(\mathbf{v})$ for all $\mathbf{u},\mathbf{v}\in V$ (triangle inequality)