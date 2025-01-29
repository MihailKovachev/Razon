>[!DEFINITION] Definition: Partial Derivative of a Real Vector Function
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Function.md) with [component functions](../Real%20Vector%20Function.md) $f_1,\cdots,f_n$ and let $\phi$ be a [coordinate system](../../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Coordinate%20Systems/index.md) for $\mathbb{R}^m$.
>
>The **partial derivative** of $f$ at $\mathbf{a} \in \mathcal{D}$ with respect to the $i$-th coordinate $\phi^i$ is the [vector](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md) whose entries are the [partial derivatives](../../Scalar%20Fields/Differentiation/Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) of $f_1,\cdots,f_n$ with respect to $\phi^i$:
>
>$$
>\begin{bmatrix}\frac{\partial f_1}{\partial \phi^i}(\mathbf{a}) \\ \vdots \\ \frac{\partial f_n}{\partial \phi^i}(\mathbf{a}) \end{bmatrix}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\frac{\partial f}{\partial \phi^i} (\mathbf{a}) \qquad \left. \frac{\partial f}{\partial \phi^i} \right|_{\mathbf{a}}  \qquad \frac{\partial}{\partial \phi^i} f(\mathbf{a}) \qquad f_{\phi^i} (\mathbf{a})
>>$$
>>
>

>[!DEFINITION] Definition: (Continuous) Partial Differentiability
>
>A [real vector function](../Real%20Vector%20Function.md) $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is called $k$**-times (continuously) partially differentiable** if all of its $k$-th order [partial derivatives](Partial%20Derivatives%20of%20Real%20Vector%20Functions.md) exist (and are [continuous](../Continuity%20of%20Real%20Vector%20Functions.md)) on $\mathcal{D}$. 
>
>If $f$ is $k$-times continuously partially differentiable, then we also say that $f$ is **of class** $C^k$ if $f$.
>
>>[!NOTATION]-
>>
>>$$
>>f \in C^k
>>$$
>>
>
>>[!DEFINITION] Definition: Piecewise (Continuous) Partial Differentiability
>>
>>A [real vector function](../Real%20Vector%20Function.md) $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is $k$-times **piecewise (continuously) partially differentiable** iff $\mathcal{D}$ can be represented as a [disjoint](../../../../../Set%20Theory/Disjoint%20Sets.md) [union](../../../../../Set%20Theory/Operations%20with%20Sets/Union.md) $\mathcal{D} = \mathcal{D}_1 \cup \cdots \cup \mathcal{D}_k$ of finitely many [subsets](../../../../../Set%20Theory/Subset.md) $\mathcal{D}_1, \dotsc, \mathcal{D}_k$ of $\mathbb{R}^m$ such that the [restrictions](../../../../Functions/Restriction.md) $f_{\mathcal{D}_1}, \dotsc, f_{\mathcal{D}_k}$ are $k$-times [(continuously) partially differentiable](Partial%20Derivatives%20of%20Real%20Vector%20Functions.md).
>>
>
