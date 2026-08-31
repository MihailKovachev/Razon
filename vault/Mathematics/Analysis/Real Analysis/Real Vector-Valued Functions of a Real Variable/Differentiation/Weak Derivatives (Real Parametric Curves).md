---
tags:
    - real-analysis
    - vector-analysis
    - analysis
    - mathematics
---

# Weak Derivatives (Real Parametric Curves)

>[!DEFINITION] Definition: Weak Derivative (Real Parametric Curves)
>
>Let $n \in \mathbb{N}_{\ge 1}$, let $\boldsymbol{f}: \mathcal{D}_{\boldsymbol{f}} \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [real parametric curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md), let $S \subseteq \mathcal{D}_{\boldsymbol{f}}$ be [open](../../../../Topology/Topological%20Spaces/Open%20Sets.md) in $\mathbb{R}$ and let $k \in \mathbb{N}_{\ge 1}$.
>
>A **$k$-th order weak derivative** of $\boldsymbol{f}$ on $S$ is any [function](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\boldsymbol{g}: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}^n$ with the following properties:
>
>- $S \subseteq \mathcal{D}_{\boldsymbol{g}}$;
>- for each [$k$-times continuously differentiable](./Differentiability%20(Real%20Parametric%20Curves).md#Higher%20Order%20Differentiability) [function](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\boldsymbol{\phi}: S \to \mathbb{R}^n$ with [compact support](../../../Functional%20Analysis/Compact%20Support.md), the following [Lebesgue integrals](../../Real%20Functions/Integration/Lebesgue%20Integral%20(Real%20Function).md) are well-defined, finite and obey:
>
>$$\int_S \boldsymbol{f}(t) \cdot \boldsymbol{\phi}^{(k)}(t) \,\mathrm{d}t = (-1)^k \int_S \boldsymbol{g}(t) \cdot \boldsymbol{\phi}(t) \,\mathrm{d}t$$
>
>>[!NOTATION]
>>
>>If $\boldsymbol{g}$ is a [weak derivative](./Weak%20Derivatives%20(Real%20Parametric%20Curves).md) of $\boldsymbol{f}$, we can denote $\boldsymbol{g}$ by $\boldsymbol{f}^{(k)}$ or $D_w^k \boldsymbol{f}$. However, strictly speaking [weak derivatives](./Weak%20Derivatives%20(Real%20Parametric%20Curves).md) are *not* unique, so these expressions can be ambiguous.
>>
>

>[!THEOREM] Theorem: Weak Derivative $\implies$ Local Lebesgue-Integrability
>
>Let $n \in \mathbb{N}_{\ge 1}$, let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [real parametric curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md), let $S \subseteq \mathcal{D}_f$ be [open](../../../../Topology/Topological%20Spaces/Open%20Sets.md) in $\mathbb{R}$ and let $k \in \mathbb{N}_{\ge 1}$.
>
>If $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}^n$ is a [weak derivative](./Weak%20Derivatives%20(Real%20Parametric%20Curves).md) of $f$ on $S$, then both $f$ and $g$ are [locally Lebesgue-integrable](../../Real%20Vector%20Functions/Locally%20Lebesgue-Integrable%20Functions.md) on $S$.
>
>>[!PROOF]-
>>
>>TODO
>>
>