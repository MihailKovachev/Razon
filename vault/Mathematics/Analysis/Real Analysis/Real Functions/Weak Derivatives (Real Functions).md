---
tags:
    - real-analysis
    - analysis
    - mathematics
---

# Weak Derivatives (Real Functions)

>[!DEFINITION] Definition: Weak Derivative (Real Functions)
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md), let $S \subseteq \mathcal{D}_f$ be [open](../../../Topology/Topological%20Spaces/Open%20Sets.md) in $\mathbb{R}$ and let $k \in \mathbb{N}_{\ge 1}$.
>
>A **$k$-th order weak derivative** of $f$ on $S$ is any [real function](./Real%20Functions.md) $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ with the following properties:
>
>- $S \subseteq \mathcal{D}_g$;
>- for each [$k$-times continuously differentiable](./Differentiability%20(Real%20Functions).md#Higher%20Order%20Differentiability) [real function](./Real%20Functions.md) $\phi: S \to \mathbb{R}$ with [compact support](../../Functional%20Analysis/Compact%20Support.md), the following [Lebesgue integrals](../Lebesgue%20Integral.md) are well-defined, finite and obey:
>
>$$\int_S f(t) \phi^{(k)}(t) \,\mathrm{d}t = (-1)^k \int_S g(t) \phi(t) \,\mathrm{d}t$$
>
>>[!NOTATION]
>>
>>If $g$ is a [weak derivative](./Weak%20Derivatives%20(Real%20Functions).md) of $f$, we can denote $g$ by $f^{(k)}$ or $D_w^k f$. However, strictly speaking [weak derivatives](./Weak%20Derivatives%20(Real%20Functions).md) are *not* unique, so these expressions can be ambiguous.
>>
>

>[!THEOREM] Theorem: Weak Derivative $\implies$ Local Lebesgue-Integrability
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md), let $S \subseteq \mathcal{D}_f$ be [open](../../../Topology/Topological%20Spaces/Open%20Sets.md) in $\mathbb{R}$ and let $k \in \mathbb{N}_{\ge 1}$.
>
>If $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ is a [weak derivative](./Weak%20Derivatives%20(Real%20Functions).md) of $f$ on $S$, then both $f$ and $g$ are [locally Lebesgue-integrable](../Real%20Vector%20Functions/Locally%20Lebesgue-Integrable%20Functions.md) on $S$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!DEFINITION] Definition: Weak Derivative (Real Functions)
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md), let $S \subseteq \mathcal{D}_f$ be [open](../../../Topology/Topological%20Spaces/Open%20Sets.md) in $\mathbb{R}$ such that $f$ is [locally integrable](../Real%20Vector%20Functions/Locally%20Lebesgue-Integrable%20Functions.md) on $S$ and let $k \in \mathbb{N}_{\ge 1}$.
>
>A $k$**-th order weak derivative** of $f$ on $S$ is any [real function](./Real%20Functions.md) $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ with the following properties:
>
>- $S \subseteq \mathcal{D}_g$;
>- $g$ is [locally integrable](../Real%20Vector%20Functions/Locally%20Lebesgue-Integrable%20Functions.md) on $S$;
>- for each [$k$-times continuously differentiable](./Differentiability%20(Real%20Functions).md) [function](./Real%20Functions.md) $\phi: S \to \mathbb{R}$ with [compact support](../../Functional%20Analysis/Compact%20Support.md), the [Lebesgue integral](../Lebesgue%20Integral.md) obeys the following:
>
>$$\int_S f(t) \phi^{(k)}(t) \,\mathrm{d}t = (-1)^k \int_S g(t) \phi(t) \,\mathrm{d}t$$
>
>>[!NOTATION]
>>
>>If $g$ is a [weak derivative](./Weak%20Derivatives%20(Real%20Functions).md) of $f$, we can denote $g$ by $f^{(k)}$ or $D_w^k f$. However, [weak derivatives](./Weak%20Derivatives%20(Real%20Functions).md) are *not* unique, so these expressions can be ambiguous.
>>
>
