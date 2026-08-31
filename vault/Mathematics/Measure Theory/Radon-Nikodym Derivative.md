---
tags:
    - measure-theory
    - mathematics
---

# Radon-Nikodym Derivative

>[!DEFINITION] Definition: Radon-Nikodym Derivative
>
>Let $(X,\Sigma)$ be a [measurable space](./Measurable%20Space.md) and let $\mu$ and $\nu$ be [measures](./Measures.md) on $(X,\Sigma)$.
>
>A **Radon-Nikodym derivative** of $\mu$ with respect to $\nu$ is any [function](TODO) $f: X \to [0,\infty]$ which is [measurable](./Measurable%20Functions.md) w.r.t. $\Sigma$ and the [Borel σ-Algebra](./Borel%20σ-Algebra.md) of the [extended real number line](../Analysis/Real%20Analysis/Extended%20Real%20Number%20Line.md) such that $\mu(S)$ is the [Lebesgue integral](../Analysis/Real%20Analysis/Lebesgue%20Integral.md) of $f$ w.r.t. $\nu$ for each $S \in \Sigma$:
>
>$$\mu(S) = \int_S f \,\mathrm{d}\nu$$
>
>>[!NOTATION]
>>
>>We denote $f$ as follows:
>>
>>$$\frac{\mathrm{d}\mu}{\mathrm{d}\nu}$$
>>
>
>>[!WARNING]
>>
>>There may be more than one [Radon-Nikodym derivative](./Radon-Nikodym%20Derivative.md)!
>>
>

>[!THEOREM] Theorem: Almost Equality of Radon-Nikodym under σ-Finiteness
>
>Let $(X,\Sigma)$ be a [measurable space](./Measurable%20Space.md) and let $\mu$ and $\nu$ be [measures](./Measures.md) on $(X,\Sigma)$.
>
>If $f$ and $g$ are [Radon-Nikodym derivatives](./Radon-Nikodym%20Derivative.md) of $\mu$ w.r.t. $\nu$ and $\nu$ is [σ-finite](./σ-Finite%20Measure.md), then
>
>$$\{x \in X: f(x) \ne g(x)\}$$
>
>is a [null set](./Null%20Sets.md) of $\nu$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Radon-Nikodym Theorem
>
>Let $(X,\Sigma)$ be a [measurable space](./Measurable%20Space.md) and let $\mu$ and $\nu$ be [measures](./Measures.md) on $(X,\Sigma)$.
>
>If $\mu$ and $\nu$ are both [σ-finite](./σ-Finite%20Measure.md) and $\mu$ is [absolutely continuous](./Absolute%20Continuity%20(Measures).md) w.r.t. $\nu$, then $\mu$ has a [Radon-Nikodym derivative](./Radon-Nikodym%20Derivative.md) with respect to $\nu$.
>
>>[!PROOF]-
>>
>>TODO
>>
>