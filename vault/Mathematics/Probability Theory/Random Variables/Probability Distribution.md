---
tags:
    - probability-theory
    - mathematics
---

# Probability Distribution

>[!DEFINITION] Definition: Probability Distribution
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md), let $(V, \Sigma_V)$ be a [measurable space](../../Measure%20Theory/Measurable%20Space.md) and let $X: \Omega \to V$ be [random element](./Random%20Element.md).
>
>The **probability distribution** of $X$ is the [pushforward](../../Measure%20Theory/Pushforward.md) of $\Pr$ onto $V$ by $X$.
>
>>[!NOTATION]
>>
>>The [probability distribution](./Probability%20Distribution.md) of a [random variable](./Real%20Random%20Variable.md) is commonly denoted in one of the following ways:
>>
>>$$\Pr_X \qquad P_X$$
>>
>>If two [random variables](./Real%20Random%20Variable.md) $X$ and $Y$ have the same [probability distribution](./Probability%20Distribution.md), then we use one of the following notations:
>>
>>$$X \overset{\text{d}}{=} Y \qquad Y \overset{\text{d}}{=} X \qquad X =_{\text{d}} Y \qquad Y=_{\text{d}} X$$
>>
>

>[!THEOREM] Theorem: Distribution Equality and CDF Equality
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md) and let $X: \Omega \to \mathbb{R}$ and $Y: \Omega \to \mathbb{R}$ be a [real random variables](./Real%20Random%20Variable.md).
>
>Then $X$ and $Y$ have the same [probability distribution](./Probability%20Distribution.md) if and only if they have the same [cumulative distribution function](./Cumulative%20Distribution%20Function.md):
>
>$$X \overset{\text{d}}{=} Y \iff \operatorname{CDF}_X = \operatorname{CDF}_Y$$
>
>>[!PROOF]-
>>
>>TODO
>>
>