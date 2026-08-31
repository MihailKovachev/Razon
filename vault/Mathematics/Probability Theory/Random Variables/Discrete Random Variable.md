---
tags:
    - probability-theory
    - mathematics
---

# Discrete Random Variable

>[!DEFINITION] Definition: Discrete Random Variable
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md).
>
>A [random variable](./Real%20Random%20Variable.md) $X: \Omega \to \mathbb{R}$ is **discrete** if there exists a [countable](../../Set%20Theory/Cardinality.md) [set](../../Set%20Theory/Sets.md) $S$ such that the [probability](../Probability%20Measure.md) of $X$ being equal to an element of $S$ is $1$:
>
>$$\Pr(X \in S) = 1$$
>

>[!THEOREM] Theorem: Countable Random Variables are Discrete
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md) and let $X: \Omega \to \mathbb{R}$ be a [random variable](./Real%20Random%20Variable.md).
>
>If the [image](../../Analysis/Functions/Functions.md) of $X$ is [countable](../../Set%20Theory/Cardinality.md), then $X$ is [discrete](./Discrete%20Random%20Variable.md).
>
>>[!PROOF]-
>>
>>Let $S$ be the [image](../../Analysis/Functions/Functions.md) of $X$:
>>
>>$$S = X(\Omega) = \{X(\omega):\omega \in \Omega\}$$
>>
>>By assumption, $S$ is [countable](../../Set%20Theory/Cardinality.md). By definition, for each $\omega \in \Omega$, we have $X(\omega) \in S$. Therefore, the [event](../Probability%20Space.md) that $X$ is in $S$ is exactly $\Omega$:
>>
>>$$\{\omega \in \Omega: X(\omega) \in S\} = \Omega$$
>>
>>$$\Pr(X \in S) = \Pr(\{\omega \in \Omega: X(\omega) \in S\}) = \Pr (\Omega)$$
>>
>>By definition, the [total mass](../../Measure%20Theory/Measure%20Theory.md) of the [probability measure](../Probability%20Measure.md) $\Pr$ is $1$:
>>
>>$$\Pr(\Omega) = 1 = \Pr(X \in S)$$
>>
>>Therefore, there exists a [countable](../../Set%20Theory/Cardinality.md) [set](../../Set%20Theory/Sets.md), namely $S$, such that $\Pr(X \in S) = 1$ and so $X$ is [discrete](./Discrete%20Random%20Variable.md).
>>
>