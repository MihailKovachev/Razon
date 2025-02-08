---
title: Improper Integrals
tags:
  - integration
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

# Improper Integrals

>[!NOTATION] Notation: Improper Integrals
>
>An **improper integral** is a [definite integral](./index.md) for a [real function](../../../Real-Valued%20Function.md) $f: D \subseteq \mathbb{R} \to \mathbb{R}$ on an open or a semi-open interval $D$:
>- If $D = [a;b)$ where $a, b \in \mathbb{R}$, the improper integral is defined through the [left-sided limit](../../Limits/index.md)
>
>$$\int_a^b f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \lim_{\beta \to b^-} \int_a^\beta f(x) \mathop{\mathrm{d}x}$$
>
>- If $D = (a;b]$ where $a, b \in \mathbb{R}$, the improper integral is defined through the [right-sided limit](../../Limits/index.md)
>
>$$\int_a^b f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \lim_{\alpha \to a^+} \int_\alpha^b f(x) \mathop{\mathrm{d}x}$$
>
>- If $D = [a;\infty)$ where $a \in \mathbb{R}$, the improper integral is defined through the [limit](../../Limits/index.md)
>
>$$\int_a^\infty f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \lim_{\beta \to \infty} \int_a^\beta f(x) \mathop{\mathrm{d}x}$$
>
>- If $D = (-\infty;b]$ where $b \in \mathbb{R}$, the improper integral is defined through the [limit](../../Limits/index.md)
>
>$$\int_{-\infty}^b f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \lim_{\alpha \to -\infty} \int_\alpha^b f(x) \mathop{\mathrm{d}x}$$
>
>- If $D = (-\infty;\infty)$, then for any choice of $c \in \mathbb{R}$ the improper integral is defined as
>
>$$\int_{-\infty}^\infty f(x)\mathop{\mathrm{d}x} \overset{\text{def}}{=} \int_{-\infty}^c f(x)\mathop{\mathrm{d}x} +\int_c^\infty f(x)\mathop{\mathrm{d}x}$$
>
>If the respective limit exists, then the improper integral is said to **converge** or simply **exist**. Otherwise, it **diverges** or does **not exist**.
>

## Convergence Criteria

>[!THEOREM]
>
>Let $f,g: [a;\infty) \to \mathbb{R}$ be [Riemann-integrable](./index.md) on every closed interval $[a;b]$ where $a \le b$.
>
>If $|f(x)| \le g(x)$ for all $x \in [a;\infty)$ and the [improper integral](Improper%20Integrals.md) $\int_a^\infty g(x) \mathop{\mathrm{d}x}$ converges, then $\int_a^\infty f(x) \mathop{\mathrm{d}x}$ also converges.
>
>>[!PROOF]-
>>
>>TODO


>[!THEOREM]
>
>Let $f,g: (-\infty;b] \to \mathbb{R}$ be [Riemann-integrable](./index.md) on every closed interval $[a;b]$ where $a \le b$.
>
>If $|f(x)| \le g(x)$ $x \in [a;\infty)$ the [improper integral](Improper%20Integrals.md) $\int_{-\infty}^b g(x) \mathop{\mathrm{d}x}$ converges, then $\int_{-\infty}^b f(x) \mathop{\mathrm{d}x}$ also converges.
>
>>[!PROOF]-
>>
>>TODO
>

