---
title: Variance and Standard Deviation
tags:
    - probability-theory
    - mathematics
---


# Variance

>[!DEFINITION] Definition: Variance
>
>The **variance** of a [random variable](Random%20Variables.md) $X$ is the [expectation](Expectation.md) of square of the deviation from $X$'s [expectation](Expectation.md):
>
>$$
>\mathbb{E}[(X - \mathbb{E}[X])^2]
>$$
>
>>[!NOTATION]
>>
>>$$
>>\mathop{\operatorname{Var}} (X) \qquad \sigma^2 \qquad s^2 \qquad V(X) \qquad \mathbb{V}(X)
>>$$
>>
>

>[!TIP] Tip: Discrete Variance
>
>The [variance](Variance%20and%20Standard%20Deviation.md) of a [discrete random variable](Random%20Variables.md#Discrete%20Random%20Variable) $X$ with [support](Random%20Variables.md#Discrete%20Random%20Variable) $S = \{x_1, x_2, \dotsc\}$ and [probability mass function](Random%20Variables.md#Discrete%20Random%20Variable) $p$ is given by the [value](../../Analysis/Real%20Analysis/Real%20Series/Convergence.md) of the following [series](../../Analysis/Real%20Analysis/Real%20Series/Real%20Series.md):
>
>$$
>\sigma^2 = \sum_{i = 1}^{\infty} p(x_i) \cdot (x_i - \mathbb{E}[X])^2
>$$
>
>If $S$ is finite, then this reduces to a simple sum:
>
>$$
>\sigma^2 = \sum_{i = 1}^{|S|} p(x_i) \cdot (x_i - \mathbb{E}[X])^2
>$$
>

## Properties

>[!THEOREM]- Theorem: Computation Formula for Variance
>
>The [variance](Variance%20and%20Standard%20Deviation.md) of every [random variable](Random%20Variables.md) $X$ is the difference between the [expectation](Expectation.md) of its square and the square of its [expectation](Expectation.md):
>
>$$
>\sigma^2 = \mathbb{E}[X^2] - \mathbb{E}[X]^2
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Variance of a Constant
>
>The [variance](Variance%20and%20Standard%20Deviation.md) of a constant [random variable](Random%20Variables.md) is zero.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Variance of Constant Multiple
>
>The [variance](Variance%20and%20Standard%20Deviation.md) of a constant multiple $\lambda \in \mathbb{R}$ of a [random variable](Random%20Variables.md) $X$ is equal to the square of $\lambda$ multiplied by the [variance](Variance%20and%20Standard%20Deviation.md) of $X$:
>
>$$
>\mathop{\operatorname{Var}}(\lambda \cdot X) = \lambda^2 \cdot \mathop{\mathrm{Var}}(X)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Variance of Sum and Difference
>
>If $X$ and $Y$ are two [random variables](Random%20Variables.md), then the [variance](Variance%20and%20Standard%20Deviation.md) of their and the [variance](Variance%20and%20Standard%20Deviation.md) of their difference are both equal to the sum of their [variances](Variance%20and%20Standard%20Deviation.md):
>
>$$
>\begin{align*}
>\mathop{\operatorname{Var}}(X + Y) = \mathop{\operatorname{Var}}(X) + \mathop{\operatorname{Var}}(Y) \\
>\mathop{\operatorname{Var}}(X - Y) = \mathop{\operatorname{Var}}(X) + \mathop{\operatorname{Var}}(Y)
>\end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Standard Deviation

>[!DEFINITION] Definition: Standard Deviation of a Random Variable
>
>The **standard deviation** of a [random variable](Random%20Variables.md) $X$ is the square-root of its [variance](Variance%20and%20Standard%20Deviation.md#Variance).
>
>$$
>\sqrt{\mathop{\operatorname{Var}}(X)}
>$$
>
>>[!NOTATION]
>>
>>$$
>>\sigma \qquad \sigma_X \qquad s
>>$$
>>
>