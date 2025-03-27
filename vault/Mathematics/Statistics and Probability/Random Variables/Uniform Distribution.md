---
title: Uniform Distribution
tags:
    - probability-theory
    - mathematics
---

# Discrete Uniform Distribution

>[!DEFINITION] Definition: Discrete Uniform Distribution
>
>We say that a [discrete random variable](Random%20Variables.md#Discrete%20Random%20Variables) $X$ has a **uniform distribution** if its [support](Random%20Variables.md) $S = \{x_1,\dotsc, x_n\}$ is finite and its [probability mass function](Random%20Variables.md) $p$ is given by
>
>$$
>p(x) = \begin{cases}\frac{1}{n} \qquad x \in S \\ 0 \qquad \text{otherwise} \end{cases}
>$$
>
>>[!NOTATION]
>>
>>$$
>>X \sim U(n) \qquad X \in U(n)
>>$$
>>
>

# Continuous Uniform Distribution

>[!DEFINITION] Definition: Continuous Uniform Distribution
>
>We say that a [continuous random variable](Random%20Variables.md#Continuous%20Random%20Variable) has a **uniform distribution** on the interval $[a;b]$ (or $(a;b)$) if its [cumulative distribution function](Random%20Variables.md#Cumulative%20Distribution%20Functions) is given by
>
>$$
>F(x) = \begin{cases}0\qquad\text{ if } x \lt a \\ \frac{x-a}{b-a} \hphantom{..} \text{ if } a \le x \le b \\ 1 \qquad \text{ if } x \gt b\end{cases}
>$$
>
>>[!NOTATION]
>>
>>$$
>>X \sim U(a,b) \qquad X \in U(a,b)
>>$$
>>
>

## Properties

>[!THEOREM]- Theorem: Probability Density of Uniform Distributions
>
>The [probability density function](Random%20Variables.md) of a [continuous random variable](Random%20Variables.md#Continuous%20Random%20Variable) which has the [uniform distribution](Uniform%20Distribution.md#Continuous%20Uniform%20Distribution) $U(a,b)$ is given by
>
>$$
>f(x) = \begin{cases}\frac{1}{b-a} \hphantom{..}\text{ if } a \lt x \lt b \\ 0 \qquad \text{ otherwise }\end{cases}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>