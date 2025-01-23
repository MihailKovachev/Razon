>[!DEFINITION] Definition: Divergence
>
>Let $\boldsymbol{v}: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../Real%20Vector%20Field.md) with [component functions](../../Real%20Vector%20Functions/Real%20Vector%20Function.md) $v_1, \cdots, v_n$, where $v_i$ is [partially differentiable](../../Scalar%20Fields/Differentiation/Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) with respect to the $i$-th variable.
>
>The **divergence** of $\boldsymbol{v}$ at $\mathbf{x} \in \mathcal{D}$ is
>
>$$
>\sum_{i=1}^n \partial_i v_i (\mathbf{x})
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\nabla \cdot \boldsymbol{v}(\mathbf{x}) \qquad \mathop{\operatorname{div}}\boldsymbol {v}(\mathbf{x})
>>$$
>>
>
>>[!TIP]- Tip: Divergence as a Dot Product
>>
>>The divergence can be thought of as the [dot product](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Dot%20Product.md) of the [del operator](../Del%20Operator.md) with $\boldsymbol{v}(\mathbf{x})$.
>>
>>$$
>>\nabla \cdot \boldsymbol{v} = \begin{bmatrix}\frac{\partial}{\partial x_1} \\ \vdots \\ \frac{\partial}{\partial x_n}\end{bmatrix}\begin{bmatrix}v_1 & \cdots & v_n \end{bmatrix} = \frac{\partial v_1}{\partial x_1} + \cdots + \frac{\partial v_n}{\partial x_n}
>>$$
>>
>
>>[!INTUITION]- Intuition: Geometric Meaning of Divergence
>>
>>The divergence at a given point is a measure of how much the surrounding vector field flows into or out of it.
>>
>
>>[!NOTE] Note: Divergence as a Function
>>
>>When there is no specific $\mathbf{x} \in \mathcal{D}$ mentioned, the term "divergence" is used to refer to the [scalar field](../../Scalar%20Fields/Real%20Scalar%20Field.md) $\mathop{\operatorname{div}}\boldsymbol {v}: \mathcal{D} \to \mathbb{R}$ which maps each $\mathbf{x}$ to its divergence $\nabla \cdot \boldsymbol{v}(\mathbf{x})$.
>>
>

>[!THEOREM] Theorem: Divergence in Cartesian Coordinates
>
>Let $\boldsymbol{v}: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../Real%20Vector%20Field.md) with [component functions](../../Real%20Vector%20Functions/Real%20Vector%20Function.md) $v_1, \cdots, v_n$.
>
>If for every $i \in \{1, \dotsc, n\}$, the component function $v_i$ is [partially differentiable](../../Scalar%20Fields/Differentiation/Partial%20Differentiability%20of%20Real%20Scalar%20Fields.md) at $\mathbf{a} \in \mathcal{D}$ with respect to the $i$-th [Cartesian coordinate](../../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Coordinate%20Systems/Cartesian%20Coordinate%20System.md) $x^i$, then the [divergence](Divergence.md) of $\boldsymbol{v}$ at $\mathbf{a}$ is given by
>
>$$
>\nabla \cdot \boldsymbol{v}(\mathbf{a}) = \sum_{i = 1}^n \frac{\partial v_i}{\partial x^i}(\mathbf{a}) = \frac{\partial v_1}{\partial x^1}(\mathbf{a}) + \cdots + \frac{\partial v_n}{\partial x^n}(\mathbf{a})
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Linearity of the Divergence
>
>The [divergence](Divergence.md) is [linear transformation](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Linear%20Transformation.md) - for all $\lambda, \gamma \in \mathbb{R}$ and all [vector fields](../Real%20Vector%20Field.md) $\boldsymbol{u}, \boldsymbol{v}: D \subseteq \mathbb{R}^n \to \mathbb{R}^n$ whose $i$-th [component functions](../../Real%20Vector%20Functions/Real%20Vector%20Function.md) are [partially differentiable](../../Scalar%20Fields/Differentiation/Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) with respect to the $i$-th variable:
>
>$$
>\mathop{\operatorname{div}} (\lambda \,\mathbf{u} + \mu\,\mathbf{v}) = \lambda \mathop{\operatorname{div}}(\mathbf{u})+\mu \mathop{\operatorname{div}}\mathbf{v}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Product Rule for Divergence
>
>Let $\varphi: D \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [scalar field](../../Scalar%20Fields/Real%20Scalar%20Field.md) and $\mathbf{F}: D \to \mathbb{R}^n$ be a [vector field](../Real%20Vector%20Field.md). 
>
>If $\varphi$ is [partially differentiable](../../Scalar%20Fields/Differentiation/Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) and $\mathbf{F}$'s $i$-th [component function](../../Real%20Vector%20Functions/Real%20Vector%20Function.md) is partially differentiable with respect to the $i$-th variable, then the [divergence](Divergence.md) of their product can be expressed via $\varphi$'s [gradient](../../Scalar%20Fields/Differentiation/Gradient.md) and $\mathbf{F}$'s divergence:
>
>$$
>\nabla\cdot(\varphi\mathbf{F}) = (\nabla\varphi)\cdot \mathbf{F} + \varphi\, (\nabla \cdot \mathbf{F})
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>