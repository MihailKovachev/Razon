---
title: Random Variables
tags:
    - probability-theory
    - mathematics
---

# Random Variables

>[!DEFINITION] Definition: Random Variable
>
>Suppose we have an [experiment](../Experiments.md) with [sample space](../Experiments.md) $\Omega$.
>
>A **random variable** is a [real-valued function](../../Analysis/Real%20Analysis/Real-Valued%20Functions.md) $X: \Omega \to \mathbb{R}$.
>
>>[!DEFINITION] Definition: Discrete and Continuous Random Variables
>>
>>If the [image](../../Analysis/Functions/Functions.md) of $X$ is [countable](../../Set%20Theory/Cardinality.md), then we call $X$ a **discrete random variable**. Otherwise, we call it a **continuous random variable**.
>>
>
>>[!NOTATION]
>>
>>It is typical to denote random variables via capital letters.
>>
>

A random variable is just a way to assign a value to each outcome in the [sample space](../Experiments.md) of an [experiment](../Experiments.md).

>[!EXAMPLE]-
>
>Consider the experiment of tossing a coin twice. The sample space is $S = \{\mathrm{TT}, \mathrm{HT}, \mathrm{TH}, \mathrm{HH}\}$. One [random variable](./Random%20Variables.md) we could define is the number of heads $X$ which appear in the outcome. We would then have
>
>$$
>\begin{aligned}
>X(\mathrm{TT}) = 0 \\
>X(\mathrm{TH}) = 1 \\
>X(\mathrm{HT}) = 1 \\
>X(\mathrm{HH}) = 2
>\end{aligned}
>$$
>

## Cumulative Distribution Functions

>[!DEFINITION] Definition: Cumulative Distribution Function (CDF)
>
>The **cumulative distribution function** of a [continuous random variable](#Continuous%20Random%20Variables) $X: \Omega \to \mathbb{R}$ is the [function](../../Analysis/Real%20Analysis/Real-Valued%20Functions.md) $F_X: \mathbb{R} \to [0;1]$ which to each $x \in \mathbb{R}$ assigns the [probability](../Probability%20Spaces.md) that $X$ is less than $x$ when the [experiment](../Experiments.md) is carried out.
>
>$$
>F_X(x) \overset{\text{def}}{=} P(X \lt x)
>$$
>

>[!THEOREM] Theorem: Probability in an Interval
>
>The [probability](../Probability%20Spaces.md) that the value of a [continuous random variable](#Continuous%20Random%20Variables) $X$ falls in the interval $[[Random Variables#Cumulative Distribution Functions|a; b)$ is the difference in its [cumulative distribution function]] evaluated at $a$ and $b$:
>
>$$
>P(a \le X \lt b) = F(b) - F(a)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Monotony of the CDF
>
>The [cumulative distribution function](#Cumulative%20Distribution%20Functions) of each [continuous random variable](#Continuous%20Random%20Variables) is [increasing](../../Analysis/Real%20Analysis/Real%20Functions/Monotonicity%20of%20Real%20Functions.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Limits of the CDF
>
>The [limits](../../Analysis/Real%20Analysis/Real%20Functions/Limits%20(Real%20Functions.md) of the [cumulative distribution function](#Cumulative%20Distribution%20Functions) $F_X$ of each [continuous random variable](#Continuous%20Random%20Variables) $X$ for $x \to -\infty$ and $x \to +\infty$ are $0$ and $1$, respectively.
>
>$$
>\begin{aligned}
>\lim_{x \to -\infty} F_X(x) = 0 \\
>\lim_{x \to +\infty} F_X(x) = 1
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Discrete Random Variables

>[!DEFINITION] Definition: Discrete Random Variables
>
>A [random variable](./Random%20Variables.md) is **discrete** if and only if its [image](../../Analysis/Functions/Functions.md) is [countable](../../Set%20Theory/Cardinality.md).
>

Essentially, a [discrete random variable](#Discrete%20Random%20Variables) can take on either finitely many values or it can take on infinitely many values which can be arranged in a [real sequence](../../Analysis/Real%20Analysis/Real%20Sequences.md).

>[!EXAMPLE]-
>
>Consider the experiment of tossing a coin twice. The sample space is $S = \{\mathrm{TT}, \mathrm{HT}, \mathrm{TH}, \mathrm{HH}\}$. One [random variable](./Random%20Variables.md) we could define is the number of heads $X$ which appear in the outcome. We would then have
>
>$$
>\begin{aligned}
>X(\mathrm{TT}) = 0 \\
>X(\mathrm{TH}) = 1 \\
>X(\mathrm{HT}) = 1 \\
>X(\mathrm{HH}) = 2
>\end{aligned}
>$$
>
>This is a [discrete random variable](#Discrete%20Random%20Variables), since it can take on only three possible values, namely $0$, $1$ and $2$.
>

## Probability Mass Functions

>[!DEFINITION] Definition: Probability Mass Function
>
>The **probability mass function** of a [discrete random variable](#Discrete%20Random%20Variables) $X: \Omega \to \mathbb{R}$ is the [function](../../Analysis/Real%20Analysis/Real-Valued%20Functions.md) $p_X: \mathbb{R} \to [0;1]$ which to each possible value $x \in X(\Omega)$ of $X$ assigns the [probability](../Probability%20Spaces.md) that $X$ is equal to $x$ when the [experiment](../Experiments.md) is carried out.
>
>$$
>p_X(x) \overset{\text{def}}{=} P(X = x)
>$$
>

>[!DEFINITION] Definition: Support of a Discrete Random Variable
>
>The **support** of a [discrete random variable](#Discrete%20Random%20Variables) $X: \Omega \to \mathbb{R}$ is [set](../../Set%20Theory/Sets.md) of all values $x_1, x_2, \dotsc \in \mathbb{R}$ which $X$ can take on with a nonzero probability.
>
>$$
>\{ x \in \mathbb{R} \mid P(X = x) \gt 0\}
>$$
>

>[!DEFINITION] Definition: Mode
>
>A **mode** of a [discrete random variable](#Discrete%20Random%20Variable) $X$ is the [real number](../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) $m \in \mathbb{R}$ for which the [probability mass function](#Probability%20Mass%20Functions) of $X$ is maximum.
>

# Continuous Random Variable

>[!DEFINITION] Definition: Continuous Random Variable
>
>A [random variable](./Random%20Variables.md) is **continuous** if and only if it is not [discrete](#Discrete%20Random%20Variables) and its [cumulative distribution function](#Cumulative%20Density%20Functions) is [differentiable](../../Analysis/Real%20Analysis/Real%20Functions/Differentiability%20(Real%20Functions).md) except for possibly finitely many points where it is [continuous](../../Analysis/Real%20Analysis/Real%20Functions/Continuity%20(Real%20Functions).md) but not [differentiable](../../Analysis/Real%20Analysis/Real%20Functions/Differentiability%20(Real%20Functions).md).
>

## Probability Density Function

>[!DEFINITION] Definition: Probability Density Function
>
>The **probability density function** of a [continuous random variable](#Continuous%20Random%20Variables) is the [derivative](../../Analysis/Real%20Analysis/Real%20Functions/Differentiability%20(Real%20Functions).md) of its [cumulative distribution function](#Cumulative%20Density%20Functions).
>

### Properties

>[!THEOREM] Theorem: Non-negativity of Probability Density
>
>The [probability density function](./Random%20Variables.md) $f$ of a [continuous random variable](#Continuous%20Random%20Variables) is always non-negative.
>
>$$
>f(x) \ge 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
> 

>[!THEOREM] Theorem: Probability in Interval
>
>The [probability](../Probability%20Spaces.md) that a [continuous random variable](#Continuous%20Random%20Variables) $X$ falls within the interval $[a;b]$ is given by the [definite integral](../../Analysis/Real%20Analysis/Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md) of its [probability density function](./Random%20Variables.md) $f$ over $[a;b]$:
>
>$$
>P(a \le X \le b) = \int_{[a;b]} f
>$$
>
>>[!PROOF]-
>>
>>
>>TODO
>

>[!THEOREM] Theorem: Normalization of Probability Density
>
>The [integral](../../Analysis/Real%20Analysis/Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md#Improper%20Integrals) of the [probability density function](./Random%20Variables.md) $f$ of a [continuous random variable](#Continuous%20Random%20Variables) from $-\infty$ to $+\infty$ is $1$:
>
>$$
>\int_{-\infty}^{+\infty} f = 1
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Bibliography