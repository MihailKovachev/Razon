---
title: Asymptotes of Real Functions
tags:
  - asymptotes
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

# Asymptotes

>[!DEFINITION] Definition: Vertical Asymptote
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../../Functions%20of%20the%20Real%20Numbers.md).
>
>We say that $f$ has a **vertical asymptote** at $x = c \in \mathbb{R}$ if it has at least one [infinite one-sided limit](Limits%20of%20Real%20Functions.md) at $c$, i.e. at least one of the following holds:
>
>- $\displaystyle \lim_{x \to c^-} f(x) = -\infty$
>- $\displaystyle \lim_{x \to c^+} f(x) = -\infty$
>- $\displaystyle \lim_{x \to c^-} f(x) = \infty$ 
>- $\displaystyle \lim_{x \to c^+} f(x) = \infty$
>
>>[!INTUITION]-
>>
>>Intuitively, this definition means that the value of $f(x)$ gets closer and closer to $- \infty$ or $+ \infty$ as $x$ approaches $c$ either from the left or from the right.
>>
>

>[!DEFINITION] Definition: Horizontal Asymptote
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../../Functions%20of%20the%20Real%20Numbers.md).
>
>We say that $f$ has a **horizontal asymptote** $y = a \in \mathbb{R}$ if the [limit](Limits%20of%20Real%20Functions.md) of $f$ as $x$ approaches positive or negative infinity is $a$, i.e. if at least one of the following holds:
>
>- $\displaystyle \lim_{x \to -\infty} f(x) = a$
>- $\displaystyle \lim_{x \to \infty} f(x) = a$
>
>>[!INTUITION]-
>>
>>Intuitively, this definition means that the value of $f(x)$ gets closer and closer to $a$ as $x$ approaches either positive or negative infinity.
>>
>

>[!DEFINITION] Definition: Oblique Asymptote
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../../Functions%20of%20the%20Real%20Numbers.md).
>
>The line $y = ax + b$ is an **oblique** or **slanted asymptote** of $f$ if at least one of the following is true:
>- $\displaystyle \lim_{x \to -\infty} [f(x) - (ax + b)] = 0$
>- $\displaystyle \lim_{x \to \infty} [f(x) - (ax + b)] = 0$
>
>>[!INTUITION]-
>>
>>Intuitively, this definition means $f(x)$ gets closer and closer to the line $y = ax + b$ as $x$ approaches either positive or negative infinity.
>>
>

## Properties

>[!THEOREM] Theorem: Oblique Asymptotes
>
>Let $f$ be a [real function](../../Functions%20of%20the%20Real%20Numbers.md).
>
>The [straight line](../../../../Geometry/Euclidean%20Geometry/Curves/Straight%20Lines/Straight%20Line.md) $y = ax + b$ is an [asymptote](Asymptotes.md) of $f$ if and only if the [limits](Limits%20of%20Real%20Functions.md) $\lim_{x \to \pm \infty} \frac{f(x)}{x}$ and $\lim_{x \to \pm \infty} (f(x) - ax)$ exist and
>
>$$
>\begin{align*}
>a &= \lim_{x \to \pm \infty} \frac{f(x)}{x} \\
>
>\\
>
>b &= \lim_{x \to \pm \infty} (f(x) - ax)
>\end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>