>[!DEFINITION] Definition: Jacobian Matrix
>
>Let $f: D \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [partially differentiable](Partial%20Derivatives%20of%20Real%20Vector%20Functions.md) [real vector function](../Real%20Vector%20Function.md) with [component functions](../Real%20Vector%20Function.md) $f_1,\cdots,f_n$.
>
>The **Jacobian matrix** of $f$ is the $n \times n$-[matrix](../../../../../Algebra/Linear%20Algebra/Matrices/Square%20Matrices/Square%20Matrix.md) $Df$ whose rows are the [gradients](../../Scalar%20Fields/Differentiation/Gradient.md) of $f_1,\cdots,f_n$:
>
>$$
>\mathop{D} f \overset{\text{def}}{=} \begin{bmatrix}\textemdash & \nabla^\mathsf{T} f_1 & \textemdash \\ \textemdash & \vdots & \textemdash \\ \textemdash & \nabla^\mathsf{T} f_n & \textemdash \end{bmatrix}
>$$
>
>>[!NOTATION]-
>>
>>The [Jacobian matrix](Jacobian%20Matrix.md) $Df$ is different for different $\vec{x} \in D$, since the [partial derivatives](Partial%20Derivatives%20of%20Real%20Vector%20Functions.md) of $f$ depend on $\vec{x}$. The [Jacobian matrix](Jacobian%20Matrix.md) at a particular $\vec{x} \in D$ is thus denoted as $Df(\vec{x})$.
>>
>