---
tags:
    - real-analysis
    - vector-analysis
    - mathematical-analysis
    - mathematics
---

# Continuity (Real Vector Functions)

>[!THEOREM] Theorem: Continuity of Real Vector Functions
>
>A [real vector function](./Real%20Vector%20Functions.md) $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is [continuous](../../Continuity/Continuity.md) at $\boldsymbol{p} \in \mathcal{D}$ if and only if $\boldsymbol{p}$ is an [isolated point](../../../Topology/Isolated%20Points.md) of $\mathcal{D}$ or $f$ is equal to its own [limit](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Limits%20(Real%20Scalar%20Fields).md) there:
>
>$$\lim_{\boldsymbol{x} \to \boldsymbol{p}} f(\boldsymbol{x}) = f(\boldsymbol{p})$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity via Component Functions
>
>A [real vector function](./Real%20Vector%20Functions.md) $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is [continuous](../../Continuity/Continuity.md) at $\boldsymbol{p} \in \mathcal{D}$ if and only if its [component functions](./Real%20Vector%20Functions.md) $f_1, \dotsc, f_n$ are [continuous](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Continuity%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity via Limits of Scalar Fields
>
>A [real vector function](./Real%20Vector%20Functions.md) $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is [continuous](../../Continuity/Continuity.md) at $\boldsymbol{p} \in \mathcal{D}$ if and only if $\boldsymbol{p}$ is an [isolated point](../../../Topology/Isolated%20Points.md) of $\mathcal{D}$ or the [limit](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Limits%20(Real%20Scalar%20Fields).md) of $||f(\boldsymbol{x}) - f(\boldsymbol{p})||$ there is zero:
>
>$$\lim_{\boldsymbol{x} \to \boldsymbol{p}} ||f(\boldsymbol{x}) - f(\boldsymbol{p})|| = 0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity of Linear Combination
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^m \to \mathbb{R}^n$ and $g: \mathcal{D}_g \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be [real vector functions](./Real%20Vector%20Functions.md).
>
>If $f$ and $g$ are [continuous](./Continuity%20(Real%20Vector%20Functions).md) at $\boldsymbol{p} \in \mathcal{D}_f \cap \mathcal{D}_g$, then so is $\lambda f + \mu g$ for all $\lambda, \mu \in \mathbb{R}$.
>
> >[!PROOF]-
>>
>>TODO
>>
>