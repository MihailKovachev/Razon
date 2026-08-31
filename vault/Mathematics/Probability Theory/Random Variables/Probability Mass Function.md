---
tags:
    - probability-theory
    - mathematics
---

# Probability Mass Function

>[!DEFINITION] Definition: Probability Mass Function
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md), let $(V, \Sigma_V)$ be a [measurable space](../../Measure%20Theory/Measurable%20Space.md) and let $X: \Omega \to V$ be a [random element](./Random%20Element.md).
>
>The **probability mass function** of $X$ is the [real function](../../Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) $\text{PMF}_X: \mathbb{R} \to [0,1]$ which for each $v \in V$ gives the [probability](../Probability%20Space.md) that $X$ is equal to $v$:
>
>$$\text{PMF}_X(v) \overset{\text{def}}{=} \Pr(X = v)$$
>

>[!THEOREM] Theorem: PMF as Radon-Nikodym Derivative
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md) and let $X: \Omega \to \mathbb{R}$ be a [real random variable](./Real%20Random%20Variable.md).
>
>If $X$ is [discrete](./Discrete%20Random%20Variable.md), then its [probability mass function](./Probability%20Mass%20Function.md) is the unique [Radon-Nikodym derivative](../../Measure%20Theory/Radon-Nikodym%20Derivative.md) of its [probability distribution](./Probability%20Distribution.md) with respect to the [counting measure](../../Measure%20Theory/Counting%20Measure.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: PMF of Absolutely Continuous Random Variable
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md) and let $X: \Omega \to \mathbb{R}$ be a [real random variable](./Real%20Random%20Variable.md).
>
>If $X$ is [absolutely continuous](./Absolutely%20Continuous%20Random%20Variable.md), then its [probability mass function](./Probability%20Mass%20Function.md) is always zero:
>
>$$\Pr(X = x) = 0 \qquad \forall x \in \mathbb{R}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>