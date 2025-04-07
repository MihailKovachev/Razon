---
title: Injections, Surjections and Bijections
tags:
  - functions
  - analysis
  - mathematics
---

# Injections

>[!DEFINITION] Definition: Injection
>
>A [function](Functions.md) $f: X \to Y$ is called **injective** if for each $y \in Y$ there is only one $x\in X$ such that $y = f(x)$.
>

>[!DEFINITION] Definition: Inverse Function
>
>The **inverse function** of an [injection](Injections,%20Surjections%20and%20Bijections.md) $f: X \to Y$ is the [function](Functions.md) $f^{-1}: f(X) \to X$ which to each $y \in Y$ assigns the $x \in X$ for which $y = f(x)$, i.e.
>
>$$
>f^{-1}(f(x)) = x
>$$
>

>[!DEFINITION] Definition: Involution
>
>An **involution** is a [function](Functions.md) $f: X \to Y$ which is its own [inverse function](Injections,%20Surjections%20and%20Bijections.md).
>
>$$
>f(f(x)) = x \qquad \forall x \in X
>$$
>

# Surjections

>[!DEFINITION] Definition: Surjection
>
>A [function](Functions.md) $f: X \to Y$ is called **surjective** if its [image](Functions.md) and [codomain](Functions.md) are equal, i.e. for each $y \in Y$ there is at least one $x \in X$ such that $y = f(x)$.
>

# Bijections

>[!DEFINITION] Definition: Bijection
>
>A [function](Functions.md) $f: X \to Y$ is called **bijective** if it is both [injective](Injections,%20Surjections%20and%20Bijections.md) and [surjective](Injections,%20Surjections%20and%20Bijections.md).
>


![Injection, Surjection, Bijection](res/Injection,%20Surjection,%20Bijection.svg)