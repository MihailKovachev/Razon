---
title: Binomial Distribution
tags:
    - probability-theory
    - mathematics
---

# Binomial Distribution

>[!DEFINITION] Definition: Binomial Distribution
>
>We say that a [discrete random variable](Random%20Variables.md#Discrete%20Random%20Variable) $X$ has a **binomial distribution** if there exist some $n \in \mathbb{N}$ and some [real number](../../Algebra/Fields/The%20Real%20Numbers/index.md) $p \in [0;1]$ such that
>
>$$
>P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
>$$
>
>for all $k \in \{0,1,2,\dotsc, n\}$.
>
>>[!NOTE]
>>
>>We often call $n$ and $p$ the parameters of the binomial distribution and say that $X$ is distributed according to the binomial distribution with parameters $n$ and $p$.
>>
>
>>[!NOTATION]
>>
>>$$
>>X \sim \mathop{\operatorname{Bin}}(n, p)
>>$$
>>
>

By far the most common random variable which has a binomial distributions is the following. Consider some [experiment](../Experiments.md) $E_1$ with a [random variable](Random%20Variables.md) $Y$ which is distributed according to a [Bernoulli distribution](Bernoulli%20Distribution.md) with parameter $p$. Now consider the [experiment](../Experiments.md) $E_2$ which consists of repeating $n$ times the $E_1$. The [random variable](Random%20Variables.md) $X$ which denotes the total number of times in which $Y$ was "success" follows the [binomial distribution](Binomial%20Distribution.md) with parameters $n$ and $p$.

## Properties

>[!THEOREM]- Theorem: Cumulative Distribution Function of Binomial Distributions
>
>The [cumulative distribution function](Random%20Variables.md#Cumulative%20Distribution%20Function) of a [discrete random variable](Random%20Variables.md) $X$ which follows the [binomial distribution](Binomial%20Distribution.md) $\operatorname{Bin}(n,p)$ is given by
>
>$$
>F(x) = \sum_{k = 0}^{\lfloor x \rfloor} \binom{n}{k} p^k (1-p)^{n-k}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Probability Mass Function of Binomial Distributions
>
>The [probability mass function](Random%20Variables.md#Probability%20Mass%20Functions) $p$ of a [discrete random variable](Random%20Variables.md#Discrete%20Random%20Variables) $X$ which follows the [binomial distribution](Binomial%20Distribution.md) $\mathop{\operatorname{Bin}}(n, p)$ is
>
>$$
>p(x) = \begin{cases}\binom{n}{k} p^x (1-p)^{n-x} \qquad \text{if } x \in \{0,1,2,\dotsc,n\} \\ 0 \qquad \text{otherwise}\end{cases}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Mode of Binomial Distributions
>
>The [mode(s)](Random%20Variables.md#Probability%20Mass%20Functions) of a [discrete random variable](Random%20Variables.md) which follows the [binomial distribution](Binomial%20Distribution.md) $\operatorname{Bin}(n, p)$ is (are):
>-  $\lfloor (n+1)p \rfloor$ if $(n+1)p$ is $0$ or a noninteger;
>- $(n+1)p$ and $(n+1)p - 1$ if $(n+1)p \in \{1, 2, \dotsc, n\}$;
>- $n$ if $(n+1)p = n+1$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Expectation of Binomial Distributions
>
>The [expectation](Expectation.md) of every [random variable](Random%20Variables.md) $X$ which follows the [binomial distribution](Binomial%20Distribution.md) $\mathop{\operatorname{Bin}}(n,p)$ is given by the product of $n$ and $p$:
>
>$$
>\mathbb{E}(X) = np
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Variance of Binomial Distributions
>
>The [variance](Variance%20and%20Standard%20Deviation.md) of every [random variable](Random%20Variables.md) $X$ which follows the [binomial distribution](Binomial%20Distribution.md) $\mathop{\operatorname{Bin}}(n,p)$ is equal to $np(1-p)$:
>
>$$
>\operatorname{Var}(X) = np(1-p)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>