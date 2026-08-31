---
tags:
    - probability-theory
    - mathematics
---

# Cumulative Distribution Function

>[!DEFINITION] Definition: Cumulative Distribution Function
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md) and let $X: \Omega \to \mathbb{R}$ be a [random variable](./Real%20Random%20Variable.md).
>
>The **cumulative distribution function** (**CDF**) of $X$ is the [real function](../../Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) $F: \mathbb{R} \to \mathbb{R}$ which is defined for each $x \in \mathbb{R}$ as the [probability](../Probability%20Space.md) that $X$ is less than or equal to $x$::
>
>$$F(x) \overset{\text{def}}{=} \Pr(X \le x)$$
>

>[!THEOREM] Theorem: Monotonicity of Cumulative Distribution Functions
>
>The [cumulative distribution function](./Cumulative%20Distribution%20Function.md) of each [random variable](./Real%20Random%20Variable.md) is [non-decreasing](../../Analysis/Real%20Analysis/Real%20Functions/Monotonicity%20of%20Real%20Functions.md).
>
>>[!PROOF]-
>>
>>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md) and let $X: \Omega \to \mathbb{R}$ be a [random variable](./Real%20Random%20Variable.md) with [cumulative distribution function](./Cumulative%20Distribution%20Function.md) $F: \mathbb{R} \to \mathbb{R}$. Let $x_1, x_2 \in \mathbb{R}$.
>>
>>If $x_1 \le x_2$, then $\{\omega \in \Omega: X(\omega) \le x_1\} \subseteq \{\omega \in \Omega: X(\omega) \le x_2\}$. We see that these two [sets](../../Set%20Theory/Sets.md) are the [preimages](TODO) under $X$ of the [intervals](../../Set%20Theory/Orderings/Interval.md) $(-\infty, x_1]$ and $(-\infty, x_2]$, respectively:
>>
>>$$\{\omega \in \Omega: X(\omega) \le x_1\} = X^{-1}((-\infty,x_1])$$
>>
>>$$\{\omega \in \Omega: X(\omega) \le x_2\} = X^{-1}((-\infty,x_2])$$
>>
>>We see that $(-\infty,x_1]$ and $(-\infty,x_2]$ are [Borel sets](../../Measure%20Theory/Borel%20σ-Algebra.md) of the [real number line](../../Analysis/Real%20Analysis/Real%20Number%20Line.md) and thus [measurable](../../Measure%20Theory/Measurable%20Space.md) with respect to its [Borel σ-algebra](../../Measure%20Theory/Borel%20σ-Algebra.md). By definition, $X$ is [measurable](../../Measure%20Theory/Measurable%20Functions.md) with respect to $(\Omega, \mathcal{F})$ and the [Borel σ-algebra](../../Measure%20Theory/Borel%20σ-Algebra.md) on $\mathbb{R}$ and so $X^{-1}((-\infty,x_1])$ and $X^{-1}((-\infty,x_2])$ must be [measurable](../../Measure%20Theory/Measurable%20Space.md) in $(\Omega, \mathcal{F})$. Moreover, since $\Pr$ is a [measure](../../Measure%20Theory/Measures.md), its monotonicity yields the following:
>>
>>$$\Pr (\{\omega \in \Omega: X(\omega) \le x_1\}) \le \Pr (\{\omega \in \Omega: X(\omega) \le x_2\})$$
>>
>>This is just the following:
>>
>>$$\Pr(X \le x_1) \le \Pr (X \le x_2)$$
>>
>>The left-hand side is the definition of $F(x_1)$ and the right-hand side is the definition of $F(x_2)$. Therefore:
>>
>>$$F(x_1) \le F(x_2)$$
>>
>

>[!THEOREM] Theorem: Limits of Cumulative Distribution Functions
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md).
>
>If $F: \mathbb{R} \to \mathbb{R}$ is the [cumulative distribution function](./Cumulative%20Distribution%20Function.md) of a [random variable](./Real%20Random%20Variable.md), then its [limit](../../Analysis/Real%20Analysis/Real%20Functions/Limits%20(Real%20Functions).md) at $-\infty$ is $0$ and its [limit](../../Analysis/Real%20Analysis/Real%20Functions/Limits%20(Real%20Functions).md) at $+\infty$ is $1$:
>
>$$\lim_{x \to -\infty} F(x) = 0 \qquad \lim_{x \to \infty} F(x) = 1$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Right-Continuity
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md).
>
>If $F: \mathbb{R} \to \mathbb{R}$ is the [cumulative distribution function](./Cumulative%20Distribution%20Function.md) of a [random variable](./Real%20Random%20Variable.md), then it is equal to its own [right-sided limit](../../Analysis/Real%20Analysis/Real%20Functions/Limits%20(Real%20Functions).md) at each $p \in \mathbb{R}$:
>
>$$\lim_{x \to p^{+}} F(x) = F(p)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Left-Sided Limits
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md).
>
>If $F: \mathbb{R} \to \mathbb{R}$ is the [cumulative distribution function](./Cumulative%20Distribution%20Function.md) of a [random variable](./Real%20Random%20Variable.md) $X$, then its [left-sided limit](../../Analysis/Real%20Analysis/Real%20Functions/Limits%20(Real%20Functions).md) exists at each $p \in \mathbb{R}$ and is equal to $\Pr(X \lt p)$:
>
>$$\lim_{x \to p^{-}} F(x) = \Pr (X \lt p)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Probability of Equality
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md), let $X: \Omega \to \mathbb{R}$ be a [random variable](./Real%20Random%20Variable.md) with [cumulative distribution function](./Cumulative%20Distribution%20Function.md) $F: \mathbb{R} \to \mathbb{R}$ and let $v \in \mathbb{R}$.
>
>The [probability](../Probability%20Measure.md) that $X$ is equal to $v$ is the difference between $F(v)$ and $F$'s [left-sided limit](../../Analysis/Real%20Analysis/Real%20Functions/Limits%20(Real%20Functions).md) at $v$:
>
>$$\Pr(X = v) = F(v) - \lim_{x \to v^-} F(x)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Distribution Equality and CDF Equality
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md) and let $X: \Omega \to \mathbb{R}$ and $Y: \Omega \to \mathbb{R}$ be a [random variables](./Real%20Random%20Variable.md).
>
>Then $X$ and $Y$ have the same [probability distribution](./Probability%20Distribution.md) if and only if they have the same [cumulative distribution function](./Cumulative%20Distribution%20Function.md):
>
>$$\Pr_X = \Pr_Y \iff \operatorname{CDF}_X = \operatorname{CDF}_Y$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Countably Many Discontinuities
>
>Let $f: \mathbb{R} \to \mathbb{R}$ be a [real function](../../Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md).
>
>If there exists a [probability space](../Probability%20Space.md) and a [real random variable](../../Statistics%20and%20Probability/Random%20Variables/Random%20Variables.md) whose [cumulative distribution function](./Cumulative%20Distribution%20Function.md) is $f$, then the [set](../../Set%20Theory/Sets.md) of all points where $f$ is [discontinuous](../../Analysis/Real%20Analysis/Real%20Functions/Continuity%20(Real%20Functions).md) is [countable](../../Set%20Theory/Cardinality.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>