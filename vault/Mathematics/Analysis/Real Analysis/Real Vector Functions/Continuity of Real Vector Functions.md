>[!DEFINITION] Continuity of a Real Vector Function
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](Real%20Vector%20Function.md).
>
>We say that $f$ is **continuous at** $\mathbf{a} \in \mathcal{D}$ iff its [limit](Limits%20of%20Real%20Vector%20Functions.md) for $\mathbf{x} \to \mathbf{a}$ is $f(\mathbf{a})$
>
>$$
>\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = f(\mathbf{a})
>$$
>
>or $\mathbf{a}$ is an [isolated point](../../../Topology/Interior,%20Boundary,%20Exterior/Isolated%20Points.md) of $D$.
>
>We say that $f$ is **continuous on** $\mathcal{D}$ if it is continuous at every $\mathbf{a} \in \mathcal{D}$.
>
>>[!DEFINITION] Definition: Piecewise Continuity
>>
>>Let $f: D \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](Real%20Vector%20Function.md).
>>
>>We say that $f$ is **piecewise continuous** if $D$ can be expressed as the [union](../../../Set%20Theory/Collections/Operations%20with%20Collections.md) of a finite [collection](../../../Set%20Theory/Collections/Collections.md) of [disjoint sets](../../../../Set%20Theory/Disjoint%20Sets.md) $D = D_1 \cup \cdots \cup D_p$ such that the [restrictions](../../Functions/Restriction.md) $f\big|_{D_1},\ldots, f\big|_{D_p}$ are [continuous](Continuity%20of%20Real%20Vector%20Functions.md).
>>
>

## Characterizations

>[!THEOREM] Theorem: Continuity via Component Functions
>
>A [real vector function](Real%20Vector%20Function.md) $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is [continuous](Continuity%20of%20Real%20Vector%20Functions.md) at $\mathbf{x}_0 \in \mathcal{D}$ if and only if its [component functions](Real%20Vector%20Function.md) $f_1, \dotsc, f_n$ are [continuous](Continuity%20of%20Real%20Vector%20Functions.md) at $\mathbf{x}_0$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity via Limits of Scalar Fields
>
>A [real vector function](Real%20Vector%20Function.md) $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is [continuous](Continuity%20of%20Real%20Vector%20Functions.md) at $\mathbf{a} \in \mathcal{D}$ if and only if $\mathbf{a} \in \mathcal{D}$ is an [isolated point](../../../Topology/Interior,%20Boundary,%20Exterior/Isolated%20Points.md) of $\mathcal{D}$ or the following [limit](Scalar%20Fields/Limits%20of%20Real%20Scalar%20Fields.md) is zero.
>
>$$
>\lim_{\mathbf{x} \to \mathbf{a}} ||f(\mathbf{x}) - f(\mathbf{a})|| = 0
>$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>
>>- (I) If $f$ is [continuous](Continuity%20of%20Real%20Vector%20Functions.md) at $\mathbf{a} \in \mathcal{D}$, then $\lim_{\mathbf{x} \to \mathbf{a}} ||f(\mathbf{x}) - f(\mathbf{a})|| = 0$.
>>- (II) If $\lim_{\mathbf{x} \to \mathbf{a}} ||f(\mathbf{x}) - f(\mathbf{a})|| = 0$, then $f$ is [continuous](Continuity%20of%20Real%20Vector%20Functions.md) at $\mathbf{a}$.
>>
>>**Proof of (I):**
>>
>>To prove that
>>
>>$$
>>\lim_{\mathbf{x} \to \mathbf{a}} ||f(\mathbf{x}) - f(\mathbf{a})|| = 0,
>>$$
>>
>>we need to show that for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that if $\mathbf{x} \in \mathcal{D}$ and $0 \lt ||\mathbf{x} - \mathbf{a}|| \lt \delta$, then $| \, ||f(\mathbf{x}) - f(\mathbf{a})|| - 0 \,|\lt \varepsilon$, i.e. $||f(\mathbf{x}) - f(\mathbf{a})||\lt \varepsilon$.
>>
>>Now, since $f$ is [continuous](Continuity%20of%20Real%20Vector%20Functions.md), we have
>>
>>$$
>>\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = f(\mathbf{a})
>>$$
>>
>>In other words, for each [open ball](../The%20Topology%20of%20Euclidean%20Space.md) $B_{\varepsilon}(f(\mathbf{a}))$ around $\mathbf{a}$, there exists some [open ball](../The%20Topology%20of%20Euclidean%20Space.md) $B_{\delta}(\mathbf{a})$ around $\mathbf{a}$ such that for all $\mathbf{x} \in \mathcal{D}$ different from $\mathbf{a}$, if $\mathbf{x} \in B_{\delta}(\mathbf{a})$, then $f(\mathbf{x}) \in B_{\varepsilon}(f(\mathbf{a}))$. By recalling the [definition of an open ball](../../../Topology/Metric%20Spaces/index.md), we can restate the previous sentence as the following - for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that for all $\mathbf{x} \in \mathcal{D}$, if $0 \lt || \mathbf{x} - \mathbf{a} || \lt \delta$, then $|| f(\mathbf{x}) - f(\mathbf{a}) || \lt \varepsilon$, which is precisely what we set out to prove.
>>
>>**Proof of (II):**
>>
>>To prove that $f$ is [continuous](Continuity%20of%20Real%20Vector%20Functions.md) at $\mathbf{a}$, we need to prove that
>>
>>$$
>>\lim_{ \mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = f(\mathbf{a})
>>$$
>>
>>Restating this using the [definition of a limit](Limits%20of%20Real%20Vector%20Functions.md), we need to prove that for each [open ball](../The%20Topology%20of%20Euclidean%20Space.md) $B_{\varepsilon}(f(\mathbf{a}))$ around $f(\mathbf{a})$, there exists some [open ball](../The%20Topology%20of%20Euclidean%20Space.md) $B_{\delta}(\mathbf{a})$ around $\mathbf{a}$ such that for all $\mathbf{x} \in \mathcal{D}$ different from $\mathbf{x}$, if $\mathbf{x} \in B_{\delta}(\mathbf{a})$, then $f(\mathbf{x}) \in B_{\varepsilon}(f(\mathbf{a}))$. Further paraphrasing this using the [definition of an open ball](../../../Topology/Metric%20Spaces/index.md), we need to prove that for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that for all $\mathbf{x} \in \mathcal{D}$, if $0 \lt || \mathbf{x} - \mathbf{a} || \lt \delta$, then $|| f(\mathbf{x}) - f(\mathbf{a}) || \lt \varepsilon$.
>>
>>We are given that
>>
>>$$
>>\lim_{\mathbf{x} \to \mathbf{a}} ||f(\mathbf{x}) - f(\mathbf{a})|| = 0
>>$$
>>
>>Using the [definition of the limit for scalar fields](Scalar%20Fields/Limits%20of%20Real%20Scalar%20Fields.md), we know that for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that for all $\mathbf{x} \in \mathcal{D}$, if $|| \mathbf{x} - \mathbf{a} ||$, then $|\, ||f(\mathbf{x}) - f(\mathbf{a})|| - 0 \,| \lt \varepsilon$. Since $|\, || f(\mathbf{x}) - f(\mathbf{a})|| - 0 \, | = || f(\mathbf{x}) - f(\mathbf{a}) ||$, this just means that for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that for all $\mathbf{x} \in \mathcal{D}$, if $|| \mathbf{x} - \mathbf{a} ||$, then $|| f(\mathbf{x}) - f(\mathbf{a}) || \lt \varepsilon$, which is what we wanted to prove.
>>

## Properties

>[!THEOREM] Theorem: Properties of Continuous Real Vector Functions
>
>If $f,g: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ are [continuous](Continuity%20of%20Real%20Vector%20Functions.md) at $\mathbf{x}_0 \in \mathcal{D}$, then so are $f+g$ and $\lambda f$ for all $\lambda \in \mathbb{R}$.
>
> >[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity of Composition
>
>If $g: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ and $f: g(\mathcal{D}) \to \mathbb{R}^p$ are [continuous](Continuity%20of%20Real%20Vector%20Functions.md), then so is their [composition](../../Functions/Composition.md) $f \circ g$.
>
>>[!PROOF]-
>>
>>TODO
>>
>