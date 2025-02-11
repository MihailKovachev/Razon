>[!DEFINITION] Definition: Limit of a Real Vector Function
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](Real%20Vector%20Function.md) and let $\mathbf{a} \in \mathbb{R}^m$ be an [accumulation point](../../../Topology/Interior,%20Boundary,%20Exterior/Accumulation%20Point.md) of $\mathcal{D}$.
>
>We say that $\mathbf{L} \in \mathbb{R}^n$ is a **limit** of $f$ for $\mathbf{x} \to \mathbf{a}$ iff for each [open ball](../The%20Topology%20of%20Euclidean%20Space.md) $B_{\varepsilon}(\mathbf{L})$ around $\mathbf{L}$ there exists an [open ball](../The%20Topology%20of%20Euclidean%20Space.md) $B_{\delta}(\mathbf{a})$ around $\mathbf{a}$ such that for all $\mathbf{x} \in \mathcal{D}$ different from $\mathbf{a}$,
>
>$$
>\mathbf{x} \in B_{\delta}(\mathbf{a}) \implies f(\mathbf{x}) \in B_{\varepsilon}(\mathbf{L})
>$$
>
>>[!TIP]- Tip: Restatement without Open Balls
>>
>>For the purposes of many proofs, it useful to define the limit without reference to open balls. This is done simply by taking the above definition and replacing every occurrence of "open ball" with the [definition of an open ball](../../../Topology/Metric%20Spaces/index.md).
>>
>>We say that $\mathbf{L} \in \mathbb{R}^n$ is a **limit** of $f$ for $\mathbf{x} \to \mathbf{a}$ iff for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that for all $\mathbf{x} \in \mathcal{D}$, if $0 \lt ||\mathbf{x} - \mathbf{a}|| \lt \delta$, then $||f(\mathbf{x}) - \mathbf{L}|| \lt \varepsilon$.
>>
>
>>[!NOTATION]-
>>
>>$$
>>\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = \mathbf{L} \qquad f(\mathbf{x}) \overset{\mathbf{x} \to \mathbf{a}}{\to} \mathbf{L}
>>$$
>>
>
>>[!INTUITION]-
>>
>>Suppose we have some fixed point $\mathbf{a} \in \mathbb{R}^m$ and a point $\mathbf{x} \in \mathcal{D}$ which we can move around freely. The limit $\lim_{\mathbf{x}\to\mathbf{a}}f(\mathbf{x})$ tells us what point in $\mathbb{R}^n$ (if any) $f(\mathbf{x})$ approaches as $\mathbf{x}$ gets closer and closer to $\mathbf{a}$. If the limit is $\mathbf{L}$, then no matter how small a sphere $B_{\varepsilon}(\mathbf{L})$ we choose around $\mathbf{L}$, there will always be some sphere $B_{\delta}(\mathbf{a})$ (probably a very small one, too, but nevertheless still containing more than a single point) around $\mathbf{a}$ such that if $\mathbf{x}$ is inside $B_{\delta}(\mathbf{a})$, then $f(\mathbf{x})$ will be inside $B_{\varepsilon}(\mathbf{L})$.
>>
>
>>[!THEOREM] Theorem: Uniqueness of the Limit
>>
>>If $f$ has a [limit](Limits%20of%20Real%20Vector%20Functions.md) for $\mathbf{x} \to \mathbf{a}$, then this [limit](Limits%20of%20Real%20Vector%20Functions.md) is unique.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

>[!THEOREM] Theorem: Limit via Component Functions
>
>Let $f: D \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](Real%20Vector%20Function.md) with [component functions](Real%20Vector%20Function.md) $f_1,\cdots, f_n$ and let $\mathbf{a} \in \mathbb{R}^m$.
>
>Then $f$ has a [limit](Limits%20of%20Real%20Vector%20Functions.md) for $\mathbf{x} \to \mathbf{a}$ if and only if $f_1,\cdots, f_n$ have [limits](Scalar%20Fields/Limits%20of%20Real%20Scalar%20Fields.md) for $\mathbf{x} \to \mathbf{a}$. Moreover,
>
>$$
>\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = 
>
>\begin{bmatrix}
>
>\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} f_1(\mathbf{x}) \\
>
>\vdots \\
>
>\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} f_n(\mathbf{x})
>
>\end{bmatrix}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>