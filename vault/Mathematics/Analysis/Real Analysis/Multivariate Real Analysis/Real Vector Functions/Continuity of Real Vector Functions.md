>[!DEFINITION] Continuity of a Real Vector Function
>
>Let $f: D \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](Real%20Vector%20Function.md).
>
>We say that $f$ is **continuous at** $\vec{a}$ if its [limit](Limits%20of%20Real%20Vector%20Functions.md) as its argument approaches $\vec{a}$ is $f(\vec{a})$.
>
>$$\lim_{\vec{x} \to \vec{a}} f(\vec{x}) = f(\vec{a})$$
>
>We say that $f$ is **continuous on** $D$ if it is continuous at every $\vec{a} \in D$.
>

>[!DEFINITION] Definition: Piecewise Continuity
>
>Let $f: D \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](Real%20Vector%20Function.md).
>
>We say that $f$ is **piecewise continuous** if $D$ can be expressed as the [union](../../../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of a finite [collection](../../../../Set%20Theory/Collections/Collection.md) of [disjoint sets](../../../../Set%20Theory/Disjoint%20Sets.md) $D = D_1 \cup \cdots \cup D_p$ such that the [restrictions](../../../Functions/Restriction.md) $f\big|_{D_1},\ldots, f\big|_{D_p}$ are [continuous](Continuity%20of%20Real%20Vector%20Functions.md).
>
>^piecewisecontinuity
>