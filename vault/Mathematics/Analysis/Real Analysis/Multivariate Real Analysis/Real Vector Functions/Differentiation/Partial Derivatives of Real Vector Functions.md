>[!DEFINITION] Definition: Partial Derivative of a Real Vector Function
>
>Let $f: D \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Function.md) with [component functions](../Real%20Vector%20Function.md) $f_1,\cdots,f_n$.
>
>The **partial derivative** of $f$ with respect to the variable $x_i$ is the [vector](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md) whose entries are the [partial derivatives](../../Scalar%20Fields/Differentiation/Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) of $f_1,\cdots,f_n$ with respect to $x_i$
>
>$$
>\frac{\partial f}{\partial x_i}(\vec{x}) \overset{\text{def}}{=} \begin{bmatrix}\frac{\partial f_1}{\partial x_i}(\vec{x}) \\ \vdots \\ \frac{\partial f_n}{\partial x_i}(\vec{x})  \end{bmatrix}
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
>A [real vector function](../Real%20Vector%20Function.md) $f$ is called $k$**-times (continuously) partially differentiable** if all of its $k$-th order [partial derivatives](Partial%20Derivatives%20of%20Real%20Vector%20Functions.md) exist (and are [continuous](../Continuity%20of%20Real%20Vector%20Functions.md)). 
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
>>A [real vector function](../Real%20Vector%20Function.md) $f: D\subseteq \mathbb{R}^m \to \mathbb{R}^n$ is **piecewise (continuously) partially differentiable** if $D$ can be represented as a [disjoint](../../../../../Set%20Theory/Disjoint%20Sets.md) [union](../../../../../Set%20Theory/Operations%20with%20Sets/Union.md) $D = D_1 \cup \cdots \cup D_k$ of finitely many [subsets](../../../../../Set%20Theory/Subset.md) $D_1,\cdots, D_k$ of $\mathbb{R}^n$ and there exist (continuously) partially differentiable real vector functions $\mathcal{F}_1,\cdots,\mathcal{F}_k$ such that
>>
>>$$
>>f(\vec{x}) = \begin{cases}\mathcal{F}_1(\vec{x}) \qquad \text{ if } \vec{x} \in D_1 \\ \vdots \\ \mathcal{F}_k (\vec{x}) \qquad \text{ if } \vec{x} \in D_k\end{cases}
>>$$
>>
>>>[!INTUITION]-
>>>
>>>Intuitively, this means that $D$ can be partitioned into finitely many parts such that $f$ is (continuously) partially differentiable on each part and is not (continuously) partially differentiable only at a finite number of points in $D$.
>>>
>>
>
>>[!DEFINITION] Definition: Smoothness of a Real Vector Function
>>
>>If $f$ is $k$-times continuously partially differentiable for *every* $k \in \mathbb{N}$, then $f$ is called **smooth** or **of class** $C^\infty$.
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>f \in C^\infty
>>>$$
>>>
>>
>>>[!DEFINITION] Definition: Piecewise Smoothness
>>>
>>>A [real vector function](../Real%20Vector%20Function.md) $f: D\subseteq \mathbb{R}^m \to \mathbb{R}^n$ is **piecewise smooth** if $D$ can be represented as a [disjoint](../../../../../Set%20Theory/Disjoint%20Sets.md) [union](../../../../../Set%20Theory/Operations%20with%20Sets/Union.md) $D = D_1 \cup \cdots \cup D_k$ of finitely many [subsets](../../../../../Set%20Theory/Subset.md) $D_1,\cdots, D_k$ of $\mathbb{R}^n$ and there exist $C^\infty$ functions $\mathcal{F}_1,\cdots,\mathcal{F}_k$ such that
>>>
>>>$$
>>>f(\vec{x}) = \begin{cases}\mathcal{F}_1(\vec{x}) \qquad \text{ if } \vec{x} \in D_1 \\ \vdots \\ \mathcal{F}_k (\vec{x}) \qquad \text{ if } \vec{x} \in D_k\end{cases}
>>>$$
>>>
>>>>[!INTUITION]-
>>>>
>>>>Intuitively, this means that $D$ can be partitioned into finitely many parts such that $f$ is smooth on each part and is not smooth only at a finite number of points in $D$.
>>>>
>>>
>>
>>^smoothness
>>
>