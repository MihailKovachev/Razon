---
title: Limits of Complex Functions
tags:
    - limits
    - complex-functions
    - complex-analysis
    - mathematics
---

# Limits

>[!DEFINITION] Definition: Limit of a Complex Function
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](../index.md) and let $c \in \mathbb{C}$ be an [accumulation point](../../../../Topology/Interior,%20Boundary,%20Exterior/Accumulation%20Point.md) of $\mathcal{D}$.
>
>We say that $L$ is the **limit** of $f$ as $z$ approaches $c$ iff for each $\varepsilon \gt 0$ there exists some $\delta \gt 0$ such that, for all $z \in \mathcal{D}$,
>
>$$
>0 \lt |z - c| \lt \delta \implies |f(z) - L| \lt \varepsilon.
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\lim_{z \to c} f(z) = L \qquad 
>>$$
>>
>>In text, one also writes "$f(z) \to L$ as $z \to c$". Sometimes, one might also encounter $f(z) \underset{z \to c}{\longrightarrow} L$ and $f(z) \overset{z \to c}{\longrightarrow} L$.
>>
>
>>[!THEOREM] Theorem: Uniqueness of the Limit
>>
>>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](../index.md) and let $c \in \mathbb{C}$ be an [accumulation point](../../../../Topology/Interior,%20Boundary,%20Exterior/Accumulation%20Point.md) of $\mathcal{D}$.
>>
>>If the [limit](Limits.md) of $f$ exists for $c$, then it is unique, i.e. if $\lim_{z \to c} f(z) = L \in \mathbb{C}$ and $\lim_{z \to c} f(z) = M \in \mathbb{C}$, then $L = M$.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

>[!THEOREM] Theorem: Limit Criteria
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](../index.md) and let $c \in \mathbb{C}$ be an [accumulation point](../../../../Topology/Interior,%20Boundary,%20Exterior/Accumulation%20Point.md) of $\mathcal{D}$.
>
>A number $L \in \mathbb{C}$ is the [limit](Limits.md) of $f$ for $z \to c$ if and only if
>
>$$
>\lim_{z \to c} |f(z) - L| = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>