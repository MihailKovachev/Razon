# Introduction

In physics, it is often necessary to be able to get a sense of how much a [vector field](../Real%20Vector%20Field.md) tends to point towards or away from a particular point. This is precisely what divergence tells us. 

# Divergence 

Imagine a [vector field](../Real%20Vector%20Field.md) $\mathbf{F}$ and some point $\mathbf{p}$ in $\mathbb{R}^3$. To quantify the extent to which $\mathbf{F}$ points towards or away from $\mathbf{p}$, we can construct a sphere $S_r$ of radius $r$ which is centred at $\mathbf{p}$ and then see how much of the field enters and exits through $S_r$. This can be done by using the [integral](../Integration/Vector%20Surface%20Integral.md) of $\mathbf{F}$ over $S_r$, which is equal to $\displaystyle \iint_{S_r} \mathbf{F} \cdot \mathbf{n} \mathop{\mathrm{d}S_r}$, where $\mathbf{n}$ is the [unit surface normal](../../Parametric%20Surfaces/Surface%20Normal%20Vector.md). 

![](res/Divergence.drawio.svg)

Recall that the [dot product](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Dot%20Product.md) quantifies the extent to which two vectors are oriented in a similar direction. Essentially, at each point of the sphere $S_r$, the dot product $\mathbf{F} \cdot \mathbf{n}$ tells us how aligned $\mathbf{F}$ is with $\mathbf{n}$ there. A positive value means that $\mathbf{F}$ points in a direction which is generally aligned with $\mathbf{n}$, i.e. away from the sphere. Conversely, a negative value means that $\mathbf{F}$ points towards the sphere. The integral is just the sum of these values. If it is positive, then there are more points on the sphere where $\mathbf{F}$ tends to point outwards. If it is negative, then there are more points on the sphere where $\mathbf{F}$ tends to point inwards.

Moreover, as we make the radius $r$ smaller and smaller, the sphere closes in on $\mathbf{p}$. In the limit of $r \to 0$, the part of the field which enters the sphere is essentially the part of the field which points towards $\mathbf{p}$. Similarly, the part of the field which exits the sphere is the part of the field which points away from $\mathbf{p}$.

>[!THEOREM] Theorem: Existence of Divergence
>
>Let $\mathbf{F}: \mathcal{D} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Field.md) which is [differentiable](../../Real%20Vector%20Functions/Differentiation/Differentiability%20of%20Real%20Vector%20Functions.md) at $\mathbf{p}$ and let $S_r$ be a [parametric surface](../../Parametric%20Surfaces/Parametric%20Surface.md) whose [image](../../../../Functions/Image%20of%20a%20Function.md) is a sphere of radius $r$ centered at $\mathbf{p}$ such that its [normal vector](../../Parametric%20Surfaces/Surface%20Normal%20Vector.md) is always oriented outwards.
>
>If there exists some [neighbourhood](../../../../../Topology/Topological%20Spaces/Neighbourhoods.md) of $\mathbf{p}$ where $\mathbf{F}$ is [continuously differentiable](../../Real%20Vector%20Functions/Differentiation/Differentiability%20of%20Real%20Vector%20Functions.md), then the [limit](../../../Univariate%20Real%20Analysis/Real%20Functions/Limits%20of%20Functions/One-Sided%20Limits.md)
>
>$$
>\lim_{r \to 0^+} \frac{1}{V_r} \iint_{S_r} \mathbf{F} \cdot \mathrm{d}\mathbf{S}_r,
>$$
>
>where $\displaystyle \iint_{S_r} \mathbf{F} \cdot \mathrm{d}\mathbf{S}_r$ is the [surface integral](../Integration/Vector%20Surface%20Integral.md) of $\mathbf{F}$ over $S_r$ and $V_r$ is the volume of $S_r$, exists.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Divergence
>>
>>The **divergence** of $\mathbf{F}$ at $\mathbf{p}$ is defined as precisely
>>
>>$$
>>\lim_{r \to 0^+} \frac{1}{V_r} \iint_{S_r} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{S}_r},
>>$$
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>\nabla \cdot \mathbf{F}(\mathbf{p}) \qquad \operatorname{div}\mathbf{F}(\mathbf{p})
>>>$$
>>>
>>
>>
>>>[!NOTE] Note: Divergence as a Function
>>>
>>>When there is no specific $\mathbf{p} \in \mathcal{D}$ mentioned, the term "divergence" is used to refer to the [scalar field](../../Scalar%20Fields/Real%20Scalar%20Field.md) $\mathop{\operatorname{div}}\mathbf{F}: \mathcal{D} \to \mathbb{R}$ which maps each $\mathbf{x}$ to its divergence $\nabla \cdot \boldsymbol{v}(\mathbf{x})$.
>>>
>>
>

>[!THEOREM] Theorem: Divergence in Cartesian Coordinates
>
>Let $\boldsymbol{v}: \mathcal{D} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Field.md) with [component functions](../../Real%20Vector%20Functions/Real%20Vector%20Function.md) $v_1, v_2, v_3$ and let $\mathbf{p} \in \mathbb{R}^3$.
>
>If $\boldsymbol{v}$ is [continuously differentiable](../../Real%20Vector%20Functions/Differentiation/Differentiability%20of%20Real%20Vector%20Functions.md) at $\mathbf{p}$, then its [divergence](Divergence.md) there can be calculated using the [partial derivatives](../../Scalar%20Fields/Differentiation/Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) of $v_1, v_2, v_3$ with respect to [Cartesian coordinates](../../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Coordinate%20Systems/Cartesian%20Coordinate%20System.md):
>
>$$
>\nabla \cdot \boldsymbol{v} (\mathbf{p}) = \frac{\partial v_1}{\partial x}(\mathbf{p}) + \frac{\partial v_2}{\partial y}(\mathbf{p}) + \frac{\partial v_3}{\partial z}(\mathbf{p})
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Properties of Divergence 

>[!THEOREM] Theorem: Linearity of the Divergence
>
>
>
>The [divergence](Divergence.md) is [linear](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Linear%20Transformation.md) - for all $\lambda, \mu \in \mathbb{R}$ and all [vector fields](../Real%20Vector%20Field.md) $\boldsymbol{u}, \boldsymbol{v}$ which are [differentiable](../../Real%20Vector%20Functions/Differentiation/Differentiability%20of%20Real%20Vector%20Functions.md) at $\mathbf{p} \in \mathbb{R}^3$ we have
>
>$$
>\operatorname{div} (\lambda \boldsymbol{u} + \mu \boldsymbol{v})(\mathbf{p}) = \lambda \operatorname{div} \boldsymbol{u}(\mathbf{p}) + \mu \operatorname{div} \boldsymbol{v}(\mathbf{p})
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
