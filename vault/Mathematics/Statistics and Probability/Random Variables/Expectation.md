---
title: Expectation
tags:
    - probability-theory
    - mathematics
---


# Expectation

>[!DEFINITION] Definition: Expectation (Discrete Case)
>
>The **expectation** of a [discrete random variable](Random%20Variables.md#Discrete%20Random%20Variables) $X$ with [support](Random%20Variables.md#Discrete%20Random%20Variables) $S = \{s_1, s_2, \dotsc\}$ and [probability mass function](Random%20Variables.md) $p$ is the value of the [series](../../Analysis/Real%20Analysis/Real%20Series/Convergence.md)
>
>$$
>\sum_{i=1}^{\infty} s_i \cdot p(s_i),
>$$
>
>if it exists.
>
>>[!TIP] Note: Finite Support
>>
>>If the [support](Random%20Variables.md#Discrete%20Random%20Variables) $S$ is finite, then the [expectation](Expectation.md) of $X$ reduces to the sum
>>
>>$$
>>\sum_{i = 1}^{|S|} s_i \cdot p(s_i)
>>$$
>>
>

>[!DEFINITION] Definition: Expectation (Continuous Case)
>
>The **expectation** of a [continuous random variable](Random%20Variables.md#Continuous%20Random%20Variables) $X$ with [probability function](Random%20Variables.md) $f$ is the [integral](../../Analysis/Real%20Analysis/Real%20Functions/Integration/Definite%20Integrals.md#Improper%20Integrals) of $x f(x)$ from $-\infty$ to $+\infty$:
>
>$$
>\int_{-\infty}^{+\infty} x f(x) \mathop{\mathrm{d}x}
>$$
>

>[!NOTATION]
>
>The [expectation](Expectation.md) of a [random variable](Random%20Variables.md) $X$ is usually denoted in one of the following ways:
>
>$$
>EX \qquad \mathrm{E}[X] \qquad \mathrm{E}(X) \qquad \mathbb{E}(X) \qquad \langle X \rangle \qquad \bar{X} \qquad \mu_X
>$$
>

>[!NOTE]
>
>The [expectation](Expectation.md) of a [random variable](Random%20Variables.md) may also be called its **expected value** or **mean**.
>

## Properties

>[!THEOREM]- Theorem: Range of the Expected Value
>
>The [expectation](Expectation.md) of a [random variable](Random%20Variables.md) $X$ always lies between its minimum and maximum value:
>
>$$
>\mathbb{E}[X] \in [\min X; \max X]
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Linearity of Expectation
>
>[Expectation](Expectation.md) is a [linear](../../Algebra/Linear%20Algebra/Linear%20Transformations/Linear%20Transformation.md) operation - for all [random variables](Random%20Variables.md) $X$ and $Y$ and all $\lambda, \mu \in \mathbb{R}$, we have
>
>$$
>\mathbb{E}[\lambda X + \mu Y] = \lambda \, \mathbb{E}[X] + \mu \, \mathbb{E}[Y]
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Law of the Unconscious Statistician (LOTUS)
>
>Let $X$ be a [random variable](Random%20Variables.md) and let $g: \mathbb{R} \to \mathbb{R}$ be a [real function](../../Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md).
>
>If $X$ is [discrete](Random%20Variables.md#Discrete%20Random%20Variables) with [support](Random%20Variables.md#Discrete%20Random%20Variables) $S = \{x_1, x_2, \dotsc \}$ and [probability mass function](Random%20Variables.md#Discrete%20Random%20Variables) $p$, the [expectation](Expectation.md) of $g(X)$ is given by the [value](../../Analysis/Real%20Analysis/Real%20Series/Convergence.md) of the following [series](../../Analysis/Real%20Analysis/Real%20Series/Real%20Series.md):
>
>$$
>\mathbb{E}[g(X)] = \sum_{i} g(x_i) \cdot p(x_i)
>$$
>
>If $X$ is [continuous](Random%20Variables.md#Continuous%20Random%20Variables) with [probability density function](Random%20Variables.md#Continuous%20Random%20Variables) $p$, then the [expectation](Expectation.md) of $g(X)$ is given by the following [integral](../../Analysis/Real%20Analysis/Real%20Functions/Integration/Definite%20Integrals.md#Improper%20Integrals):
>
>$$
>\mathbb{E}[g(X)] = \int_{-\infty}^{+\infty} g(x) p(x) \mathop{\mathrm{d}x}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Independent Random Variables

>[!DEFINITION] Definition: Independent Random Variables
>
>Two [random variables](Random%20Variables.md) $X$ and $Y$ are **independent** if and only if the [events](../Experiments.md) $x \lt X$ and $y \lt Y$ are [independent](../Probability%20Spaces.md#Conditional%20Probability) for all $x, y \in \mathbb{R}$.
>

## Properties

>[!THEOREM]- Theorem: Expectation of the Product of Independent Random Variables
>
>The [expectation](Expectation.md) of the product of two [independent](Expectation.md#Independent%20Random%20Variables) [random variables](Random%20Variables.md) $X$ and $Y$ is equal to the product of their [expectations](Expectation.md):
>
>$$
>\mathbb{E}[X \cdot Y] = \mathbb{E}[X] \cdot \mathbb{E}[Y]
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>