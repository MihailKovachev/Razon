>[!DEFINITION] Definition: Partial Derivative of a Real Scalar Field
>
>Let $f: \mathcal{D} \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) on an [open subset](../../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Open%20Sets%20in%20Euclidean%20Space.md) $\mathcal{D} \subseteq \mathbb{R}^n$.
>
>The **partial derivative** of $f$ at $\mathbf{x}_0 \in \mathcal{D}$ with respect to the variable $x_i$ is the [directional derivative](Directional%20Derivatives%20of%20Real%20Scalar%20Fields.md) of $f$ along the $i$-th [standard basis vector](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20vectors/Standard%20Basis.md) $\mathbf{e}_i$ (if it exists):
>
>$$
>\lim_{h\to 0} \frac{f(\mathbf{x}_0 + h \cdot \mathbf{e}_i) - f(\mathbf{x}_0)}{h} = \lim_{h\to 0} \frac{f(x_1, \dotsc, x_i+h, \dotsc, x_n) - f(x_1, \dotsc, x_i, \dotsc, x_n)}{h}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\frac{\partial f}{\partial x_i} (\mathbf{x}_0) \qquad  \frac{\partial}{\partial x_i} f(\mathbf{x}_0)\qquad \partial_i f (\mathbf{x}_0) \qquad f_{x_i} (\mathbf{x}_0) \qquad D_{x_i}f(\mathbf{x}_0)
>>$$
>>
>
>>[!NOTE]
>>
>>When there is no specific $\mathbf{x}_0 \in \mathcal{D}$ mentioned, the term "partial derivative" is usually used for the [function](../Real%20Scalar%20Field.md) $\frac{\partial f}{\partial x_i} : \mathcal{D} \to \mathbb{R}$ which to each $\mathbf{x} \in \mathcal{D}$ assigns the [partial derivative](Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) of $f$ at the point $\mathbf{x}$ with respect to the variable $x_i$.
>>
>
>>[!NOTE] Note: Orders of Partial Derivatives
>>
>>An $n$-th order partial derivative of $f$ is a partial derivative of $f$'s $(n-1)$-th partial derivative function.
>>
>

>[!DEFINITION] Definition: (Continuous) Partial Differentiability
>
>A [real scalar field](../Real%20Scalar%20Field.md) $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ is called $k$**-times (continuously) partially differentiable** if all of its $k$-th order [partial derivatives](Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) exist (and are [continuous](../Continuity%20of%20Real%20Scalar%20Fields.md)) on $\mathcal{D}$. 
>