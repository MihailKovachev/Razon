---
title: Infinite Limits of Complex Functions
tags:
    - limits
    - complex-functions
    - complex-analysis
    - analysis
    - mathematics
---

# Infinite Limits

>[!NOTATION] Notation: Infinite Limits
>
>Let $f: \mathcal{N} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](index.md) defined on some [deleted neighborhood](../../Topology%20of%20the%20Complex%20Plane.md#Neighborhoods) of $c \in \mathbb{C}$.
>
>We write
>
>$$
>\lim_{z \to c} f(z) = \infty
>$$
>
>if, for each $M \gt 0$, there exists some $\delta \gt 0$ such that
>
>$$
>0 \lt |z - c| \lt \delta \implies |f(z)| \gt M \qquad \forall z \in \mathcal{N}.
>$$
>

## Characterizations

>[!THEOREM]- Theorem: Infinite Limit via Modulus
>
>Let $f: \mathcal{N} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](index.md) defined on some [deleted neighborhood](../../Topology%20of%20the%20Complex%20Plane.md#Neighborhoods) of $c \in \mathbb{C}$.
>
>The [limit](Infinite%20Limits.md) of $f$ for $z \to c$ is $\infty$ if and only if the [limit](Infinite%20Limits.md) of $|f|$ for $z \to c$ is $\infty$.
>
>$$
>\lim_{z \to c} f(z) = \infty \iff \lim_{z \to c} |f(z)| = \infty
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Infinite Limits at Infinity

>[!NOTATION] Notation: Limits at Infinity
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](index.md) such that $\mathcal{D}$ is the [complement](../../../../Set%20Theory/Complement.md) of some [open ball](../../Topology%20of%20the%20Complex%20Plane.md) around $0$.
>
>We write
>
>$$
>\lim_{z \to \infty} f(z) = \infty
>$$
>
>if for each $M \gt 0$ there exists some $R \gt 0$ such that
>
>$$
>|z| \gt R \implies |f(z)| \gt M \qquad \forall z \in \mathcal{D}.
>$$ 
>

>[!WARNING]
>
>Even though we use limit notation for infinite limits and infinite limits at infinity, we never say that these limits *exist*, since they are not complex numbers.
>

## Characterizations

>[!THEOREM]- Theorem: Infinite Limit via Absolute Value
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](index.md) such that $\mathcal{D}$ is the [complement](../../../../Set%20Theory/Complement.md) of some [open ball](../../Topology%20of%20the%20Complex%20Plane.md) around $0$.
>
>The [limit](Infinite%20Limits.md) of $f$ for $z \to \infty$ is $\infty$ if and only if the  [limit](Infinite%20Limits.md) of $|f|$ for $|z| \to \infty$ is $\infty$.
>
>$$
>\lim_{z \to \infty} f(z) = \infty \iff \lim_{|z| \to \infty } |f(z)| = \infty
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Converting Limits

>[!THEOREM]- Theorem: Infinite Limit $\leftrightarrow$ Infinite Limit at Infinity
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](index.md) such that $\mathcal{D}$ is the [complement](../../../../Set%20Theory/Complement.md) of some [open ball](../../Topology%20of%20the%20Complex%20Plane.md) around $0$.
>
>The [limit](Infinite%20Limits.md#Infinite%20Limits%20At%20Infinity) of $f$ for $z \to \infty$ is $\infty$ if and only if the [limit](Infinite%20Limits.md#Infinite%20Limits) of $f\left( \frac{1}{z} \right)$ for $z \to 0$ is $\infty$.
>
>$$
>\lim_{z \to \infty} f(z) = \infty \iff \lim_{z \to 0} f\left( \frac{1}{z} \right) = \infty
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Bibliography

1. N. H. Asmar, L. Grafakos, "Analytic Functions," in *Complex Analysis with Applications*, Columbia, USA: Springer, 2018