>[!THEOREM] Theorem: Transforming the Zero Vector
>
>Every [linear transformation](Linear%20Transformation.md) $T: V \to W$ always transforms the [zero vector](../Vector%20Spaces/Vector%20Space.md) $V$ to the zero vector of [zero vector](../Vector%20Spaces/Vector%20Space.md):
>
>$$
>T(\mathbf{0}_V) = \mathbf{0}_W
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Linearity of Composition
>
>The composition $g\circ f: V\to W$ of two [linear transformations](Linear%20Transformation.md) $f: V \to U$ and $g: U \to W$ is also a [linear transformation](Linear%20Transformation.md).
>
>>[!PROOF]-
>>
>>$$
>>\begin{align*}g\circ f(\lambda \mathbf{u} +\mu\mathbf{v}) &= g(f(\lambda \mathbf{u} +\mu\mathbf{v}))\\ &= g(\lambda f(\mathbf{u}) + \mu f(\mathbf{v})) \\ &= g(\lambda f(\mathbf{u})) + g(\mu f(\mathbf{v})) \\ &= \lambda g(f(\mathbf{u})) +\mu g(f(\mathbf{v}))\\ &= \lambda g\circ f(\mathbf{u})+\mu g\circ f (\mathbf{v})\end{align*}
>>$$
>>
>

>[!THEOREM] Theorem: Linearity of the Inverse Transformation
>
>If $T$ is a [bijective](../../../Analysis/Functions/Types%20of%20Functions/Bijection.md) [linear transformation](Linear%20Transformation.md), then its [inverse](../../../Analysis/Functions/Types%20of%20Functions/Injection.md) $T^{-1}$ is also a [bijective](../../../Analysis/Functions/Types%20of%20Functions/Bijection.md) [linear transformation](Linear%20Transformation.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>