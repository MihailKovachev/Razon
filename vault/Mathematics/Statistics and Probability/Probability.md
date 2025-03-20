---
title: Probability
tags:
    - probability-theory
    - mathematics
---

# Probability

At its core, the probability of an [event](Experiments.md) is just a [real number](../Algebra/Fields/The%20Real%20Numbers/index.md) between $0$ and $1$, inclusively, which measures the likelihood of that event occurring.

>[!DEFINITION] Definition: Probability Space
>
>A **probability space** $(\Omega, P)$ is a [sample space](Experiments.md) $\Omega$ equipped with a [real-valued](../Analysis/Real%20Analysis/Real-Valued%20Function.md) **probability function** $P: \mathcal{P}(\Omega) \to [0;1]$ defined on the [power set](../Set%20Theory/Power%20Set.md) of $\Omega$ with the following properties:
>- $P(\varnothing) = 0$ and $P(\Omega) = 1$;
>- For every [countable](../Set%20Theory/Cardinality/Countable%20Sets.md) [collection](../Set%20Theory/Collections/Collections.md) $\mathcal{E} = \{E_1, E_2, \dotsc \}$ of [mutually exclusive](Experiments.md) [events](Experiments.md), we have
>
>$$
>P\left(\bigcup \mathcal{E} \right) = \sum_{E \in \mathcal{E}} P(E)
>$$
>
>>[!NOTATION]
>>
>>Some people may denote the probability space as $(\Omega, \mathcal{P}(\Omega), P)$.
>>
>
>>[!DEFINITION] Definition: (Absolute) Probability
>>
>>Given an [event](Experiments.md) $E \in \mathcal{P}(\Omega)$, we call $P(E)$ the **(absolute) probability** of $E$.
>>
>

## Conditional Probability

>[!DEFINITION] Definition: Conditional Probability
>
>Let $A$ and $B$ be two [events](Experiments.md) in a [probability space](Probability.md).
>
>The **probability of** $A$ **given** $B$ is defined as
>
>$$
>P(A\mid B) \overset{\text{def}}{=} \frac{P(A \cap B)}{P(B)}
>$$
>
>>[!NOTE] Note: Prior and Posterior Probabilities
>>
>>In the context of conditional probabilities, the number $P(A)$ is often called the **prior probability** and $P(A\mid B)$ the **posterior probability** of $A$.
>>
>

Conditional probability is a measure of the likelihood that $A$ will occur if we know that $B$ has occurred. 

>[!DEFINITION] Definition: Independent Events
>
>Let $A$ and $B$ be two [events](Experiments.md) in a [probability space](Probability.md).
>
>We say that $A$ is **independent** of $B$ if the [conditional probability](Probability.md) of $A$ given $B$ is the same as the [absolute probability](Probability.md) of $A$.
>
>$$
>P(A \mid B) = P(A)
>$$
>
>>[!THEOREM] Theorem: Mutual Independence
>>
>>If $A$ is [independent](Probability.md) of $B$, then $B$ is also [independent](Probability.md) of $A$.
>>
>>>[!PROOF]-
>>>
>>>This follows directly from [Bayes' rule](Probability.md#Properties)
>>>
>>
>

### Properties

>[!THEOREM]- Theorem: Bayes' Rule
>
>If $A$ and $B$ are two [events](Experiments.md) in a [probability space](Probability.md), then their [conditional probabilities](Probability.md#Conditional%20Probability) are related as follows:
>
>$$
>P(A \mid B) = \frac{P(A)}{P(B)} P(B \mid A)
>$$
>
>>[!NOTE]
>>
>>Bayes' rules essentially allows us to switch the events around.
>>
>
>>[!PROOF]-
>>
>>By definition,
>>
>>$$
>>P(A \mid B) = \frac{P(A \cap B)}{P(B)}
>>$$
>>
>>and so
>> 
>>$$
>>P(A \cap B) = P(A \mid B) P(B).
>>$$
>>
>>Similarly,
>>
>>$$
>>P(B \mid A) = \frac{P(B \cap A)}{P(A)} = \frac{P(A \cap B)}{P(A)}
>>$$
>>
>>and so
>>
>>$$
>>P(A \cap B) = P(B \mid A) P(A).
>>$$
>>
>>By combining the two equations, we obtain the result from the theorem. 
>>
>>$$
>>P(A \mid B) P(B) = P(B \mid A) P(A)
>>$$
>>
>>$$
>>P(A \mid B) = \frac{P(B \mid A) P(A)}{P(B)}
>>$$
>>
>

>[!THEOREM]- Theorem: Law of Total Probability
>
>Let $(\Omega, P)$ be a [probability space](Probability.md), let $\{B_1, \dotsc, B_n\}$ be a [collection](../Set%20Theory/Collections/Collections.md) of [events](Experiments.md) and let $A$ be some other [event](Experiments.md).
>
>If $\{B_1, \dotsc, B_n\}$ are [mutually exclusive](Experiments.md) and their [union](../Set%20Theory/Collections/Operations%20with%20Collections.md) is $\Omega$, then the [probability](Probability.md) of $A$ is the sum of its [conditional probability](Probability.md) given each $B_i$ multiplied by the [probability](Probability.md) of $B_i$:
>
>$$
>P(A) = \sum_{i = 1}^n P(A \mid B_i) P(B_i)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>