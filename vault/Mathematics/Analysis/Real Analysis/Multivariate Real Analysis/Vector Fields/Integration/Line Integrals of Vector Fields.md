>[!THEOREM] Theorem: Line Integrals of Vector Fields
>
>Let $\boldsymbol{v}: D\subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../Real%20Vector%20Field.md) and let $\gamma: [a;b] \to \mathbb{R}^n$ and $\varphi: [c;d] \to \mathbb{R}^n$ be [reparameterisations](../../Parametric%20Curves/Equivalence%20of%20Parametric%20Curves.md) of a [curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curve.md) $\mathcal{C} \subset D$.
>
>If $\gamma$ and $\varphi$ have the [same orientation](../../../../../Geometry/Euclidean%20Geometry/Curves/Curve.md), then the following [definite integrals](../../../Univariate%20Real%20Analysis/Integration/Definite%20Integrals/Definite%20Integral.md) (where "$\cdot$" denotes the [dot product](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Dot%20Product.md)) are equal :
>
>$$
>\int_a^b \boldsymbol{v}(\gamma(t)) \cdot \gamma'(t) \mathop{\mathrm{d}t} = \int_c^d \boldsymbol{v}(\varphi(t)) \cdot \varphi'(t) \mathop{\mathrm{d}t}
>$$
>
>If $\gamma$ and $\varphi$ have [opposite orientations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curve.md), then the integrals are opposite:
>
>$$
>\int_a^b \boldsymbol{v}(\gamma(t)) \cdot \gamma'(t) \mathop{\mathrm{d}t} = - \int_c^d \boldsymbol{v}(\varphi(t)) \cdot \varphi'(t) \mathop{\mathrm{d}t}
>$$
>
>>[!PROOF]-
>>
>>We will just show this for the case when $\gamma$ and $\varphi$ are *not* piecewise, since the proof is easily generalisable - if $\gamma$ and $\varphi$ *are* piecewise, then one can just apply the following proof to each of their partitions and obtain the same end result after summing the results from each partition.
>>
>>Since $\gamma$ and $\varphi$ parameterise the same curve $\mathcal{C}$, we can [reparameterise](../../../../../Geometry/Euclidean%20Geometry/Curves/Curve.md) one in the other. More specifically, there exists a [bijective](../../../../Functions/Types%20of%20Functions/Bijection.md), [continuously differentiable function](../../../Univariate%20Real%20Analysis/Differentiation/Differentiability%20of%20Real%20Functions.md) $u: [a;b] \to [c;d]$ such that
>>
>>$$
>>\varphi(u(t)) = \gamma (t)
>>$$
>>
>>The [chain rule](../../Parametric%20Curves/Differentiation/Differentiation%20Rules%20for%20Curve%20Parameterisations.md#^chainrule) gives us
>>
>>$$
>>\int_a^b \boldsymbol{v}(\gamma(t))\cdot \gamma' (t)\mathop{\mathrm{d}t} = \int_a^b \boldsymbol{v}(\varphi(u(t))) \cdot \varphi' (u(t)) \,u'(t) \mathop{\mathrm{d}t}
>>$$
>>
>>If $\gamma$ and $\varphi$ have the [same orientation](../../../../../Geometry/Euclidean%20Geometry/Curves/Curve.md), then $u(a) = c$ and $u(b) = d$. Using the substitution $\mathrm{d}u = u'(t) \mathop{\mathrm{d}t}$ we obtain
>>
>>$$
>>\int_a^b \boldsymbol{v}(\varphi(u(t))) \cdot \varphi' (u(t)) \,u'(t) \mathop{\mathrm{d}t} = \int_c^d \boldsymbol{v}(\varphi(u)) \cdot \varphi' (u) \mathop{\mathrm{d}u}
>>$$
>>
>>$$
>>\int_a^b \boldsymbol{v}(\gamma(t))\cdot \gamma' (t)\mathop{\mathrm{d}t} = \int_c^d \boldsymbol{v}(\varphi(u)) \cdot \varphi' (u) \mathop{\mathrm{d}u}
>>$$
>>
>>If $\gamma$ and $\varphi$ have the [same orientation](../../../../../Geometry/Euclidean%20Geometry/Curves/Curve.md), then $u(a) = d$ and $u(b) = c$. Using the substitution $\mathrm{d}u = u'(t) \mathop{\mathrm{d}t}$ we obtain
>>
>>$$
>>\int_a^b \boldsymbol{v}(\varphi(u(t))) \cdot \varphi' (u(t)) \,u'(t) \mathop{\mathrm{d}t} = \int_d^c \boldsymbol{v}(\varphi(u)) \cdot \varphi' (u) \mathop{\mathrm{d}u}
>>$$
>>
>>$$
>>\int_a^b \boldsymbol{v}(\gamma(t))\cdot \gamma' (t)\mathop{\mathrm{d}t} = - \int_c^d \boldsymbol{v}(\varphi(u)) \cdot \varphi' (u) \mathop{\mathrm{d}u}
>>$$
>>
>
>>[!DEFINITION] Definition: Line Integral of a Vector Field
>>
>>Let $\boldsymbol{v}: D \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a a [real vector field](../Real%20Vector%20Field.md) and let $\mathcal{C} \subseteq D$ be a [curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curve.md) with a [parameterisation](../../Parametric%20Curves/Parametric%20Curve.md) $\gamma: [a;b] \to \mathbb{R}^n$.
>>
>>$$
>>\int \boldsymbol{v}(t) \cdot \gamma'(t) \mathop{\mathrm{d}t}
>>$$
>>
>>>[!NOTATION]-
>>>
>>>Even though the vector line integral does depend on the parameterisation, the only thing that may change is its sign. This is why we still denote it as
>>>
>>>$$\int_\mathcal{C} \boldsymbol{v} \cdot \mathop{\mathrm{d}\boldsymbol{s}}$$
>>>
>>>If $\mathcal{C}$ is [closed](../../../../../Geometry/Euclidean%20Geometry/Curves/Closed%20Curve.md), we write
>>>
>>>$$\oint_\mathcal{C} \boldsymbol{v} \cdot \mathop{\mathrm{d}\boldsymbol{s}}$$
>>>
>>>One should be careful, though, since these notations may refer to either one of the possible values for the line integral. Unless specifically stated otherwise, one should assume that multiple occurrences of the line integral refer to parameterisations with the same orientation.
>>>
>>>When we want to specify the parameterisation $\gamma$ used, we usually write $\int_\gamma$ instead of $\int_\mathcal{C}$.
>>>
>>
>

>[!THEOREM] Theorem: Linearity of the Vector Line Integral
>
>The [vector line integral](Line%20Integrals%20of%20Vector%20Fields.md) is [linear](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Linear%20Transformation.md) - for all [vector fields](../Real%20Vector%20Field.md) $\boldsymbol{v}, \boldsymbol{w}: D \subseteq \mathbb{R}^n \to \mathbb{R}^n$, all $\lambda, \mu \in \mathbb{R}$ and every [curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curve.md) $\mathcal{C} \subseteq D$:
>
>$$
>\int_\mathcal{C} (\lambda\, \boldsymbol{v} +\mu \, \boldsymbol{w})\cdot\mathop{\mathrm{d}\boldsymbol{s}} = \lambda\int_\mathcal{C} \boldsymbol{v}\cdot\mathop{\mathrm{d}\boldsymbol{s}} + \mu \int_\mathcal{C} \boldsymbol{w}\cdot \mathop{\mathrm{d}\boldsymbol{s}}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Partitioning of the Vector Line Integral
>
>Let $\boldsymbol{v}: D \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../Real%20Vector%20Field.md) and $\mathcal{C} \subset D$ be a [curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curve.md).
>
>If $\mathcal{C}$ can be represented as a [union](../../../../../Set%20Theory/Operations%20with%20Sets/Union.md) $\mathcal{C} = \mathcal{C}_1 \cup \cdots \cup \mathcal{C}_k$ of finitely many [disjoint](../../../../../Set%20Theory/Disjoint%20Sets.md) curves $\mathcal{C}_1, \cdots,\mathcal{C}_k$, then the [line integral](Line%20Integrals%20of%20Vector%20Fields.md) of $\boldsymbol{v}$ over $\mathcal{C}$ is just the sum of line integrals of $\boldsymbol{v}$ over $\mathcal{C}_1, \cdots,\mathcal{C}_k$:
>
>$$
>\int_\mathcal{C} \boldsymbol{v} \cdot \mathop{\mathrm{d}\boldsymbol{s}} = \int_{\mathcal{C}_1} \boldsymbol{v} \cdot \mathop{\mathrm{d}\boldsymbol{s}} + \cdots + \int_{\mathcal{C}_k} \boldsymbol{v} \cdot \mathop{\mathrm{d}\boldsymbol{s}}
>$$
>
>
>>[!NOTE]
>>
>>To obtain the correct result, one should be careful with the choice of parameterisation for each integral.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>