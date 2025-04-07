>[!THEOREM] Theorem: Linearity of Differentiation
>
>Let $f,g: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be [real vector functions](../../Functions%20of%20the%20Real%20Numbers.md).
>
>If $f$ and $g$ are both [differentiable](Differentiability%20of%20Real%20Vector%20Functions.md) at $\mathbf{a} \in \mathcal{D}$, then for all $\lambda, \mu \in \mathbb{R}$, the [function] $\lambda f + \mu g$ is also [differentiable](Differentiability%20of%20Real%20Vector%20Functions.md) there with
>
>$$
>\mathop{\mathrm{d}(\lambda f + \mu g)_{\mathbf{a}}} = \lambda \mathop{\mathrm{d}f_{\mathbf{a}}} + \mu \mathop{\mathrm{d}g_{\mathbf{a}}}
>$$
>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Chain Rule
>
>Let $g: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](../../Functions%20of%20the%20Real%20Numbers.md) on an [open set](../../The%20Topology%20of%20Euclidean%20Space.md) $\mathcal{D}$ such that the [image](../../../Functions/Functions.md) $g(\mathcal{D})$ is also [open](../../The%20Topology%20of%20Euclidean%20Space.md) and let $f: g(\mathcal{D}) \subseteq \mathbb{R}^n \to \mathbb{R}^p$.
>
>If $g$ is [differentiable](Differentiability%20of%20Real%20Vector%20Functions.md) at $\mathbf{a} \in \mathcal{D}$ and $f$ is [differentiable](Differentiability%20of%20Real%20Vector%20Functions.md) at $g(\mathbf{a})$, then the [composition](../../../Functions/Composition.md) $f \circ g: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^p$ is also [differentiable](Differentiability%20of%20Real%20Vector%20Functions.md) at $\mathbf{a}$ with
>
>$$
>\mathop{\mathrm{d}(f\circ g)_{\mathbf{a}}} = \mathop{\mathrm{d}f_{\mathbf{g(a)}}} \circ \mathop{\mathrm{d}g_{\mathbf{a}}}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>