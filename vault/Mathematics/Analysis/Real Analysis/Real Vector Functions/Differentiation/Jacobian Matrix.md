>[!DEFINITION] Definition: Jacobian Matrix
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [partially differentiable](Partial%20Derivatives%20of%20Real%20Vector%20Functions.md) [real vector function](../Real%20Vector%20Function.md) with [component functions](../Real%20Vector%20Function.md) $f_1,\cdots,f_n$.
>
>The **Jacobian matrix** of $f$ is the $n \times n$-[matrix](../../../../../Algebra/Linear%20Algebra/Matrices/Square%20Matrices/Square%20Matrix.md) whose rows are the [gradients](../Scalar%20Fields/Differentiation/Gradient.md) of $f_1,\cdots,f_n$:
>
>$$
>\begin{bmatrix} - & (\nabla f_1)^\mathsf{T} & - \\ - & \vdots & - \\ - & (\nabla f_n)^\mathsf{T} & - \end{bmatrix}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>Df \qquad J_f \qquad \mathbf{J}_f
>>$$
>>
>>The coefficients of the [Jacobian matrix](Jacobian%20Matrix.md) are real numbers and are different for different $\mathbf{x} \in \mathcal{D}$, since the [partial derivatives](Partial%20Derivatives%20of%20Real%20Vector%20Functions.md) of $f$ depend on $\mathbf{x}$. To make this clear, the [Jacobian matrix](Jacobian%20Matrix.md) at a particular $\mathbf{x}_0 \in \mathcal{D}$ is denoted as $Df(\mathbf{x}_0)$.
>>
>