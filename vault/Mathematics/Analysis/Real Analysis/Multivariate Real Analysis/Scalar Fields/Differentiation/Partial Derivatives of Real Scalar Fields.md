>[!DEFINITION] Definition: Partial Derivative of a Real Scalar Field
>
>Let $f: D \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md).
>
>The **partial derivative** of $f$ in $\vec{x} \in D$ with respect to the variable $x_i$ is the [directional derivative](Directional%20Derivatives%20of%20Real%20Scalar%20Fields.md) of $f$ along the $i$-th [standard basis vector](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Standard%20Basis.md) $\vec{e}_i$, if it exists:
>
>$$
>\lim_{h\to 0}\frac{f(\vec{x}+h\cdot\vec{e}_i)-f(\vec{x})}{h} = \lim_{h\to 0}\frac{f(x_1,\cdots,x_i+h,\cdots + x_n) - f(x_1,\cdots,x_i,\cdots, x_n)}{h}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\frac{\partial f}{\partial x_i} (\vec{x}) \qquad  \frac{\partial}{\partial x_i} f(\vec{x})\qquad \partial_i f (\vec{x}) \qquad f_{x_i} (\vec{x}) \qquad f_{x_i}(\vec{x})
>>$$
>>
>

>[!DEFINITION] Definition: (Continuous) Partial Differentiability
>
>A [real scalar field](../Real%20Scalar%20Field.md) $f$ is called $k$**-times (continuously) partially differentiable** if all of its $k$-th order [partial derivatives](Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) exist (and are [continuous](../Continuity%20of%20Real%20Scalar%20Fields.md)). 
>