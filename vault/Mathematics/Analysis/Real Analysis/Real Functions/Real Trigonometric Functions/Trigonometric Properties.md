---
title: Trigonometric Properties
tags:
  - real-analysis
  - mathematical-analysis
  - mathematics
---

# Fundamental Trigonometric Properties

>[!THEOREM] Theorem: Trigonometric Functions of Standard Angles
>
>Here are some common values for [sine](./Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function), [cosine](./Real%20Trigonometric%20Functions.md#The%20Real%20Cosine%20Function), [tangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function) and [cotangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Cotangent%20Function):
>
>||$0$|$\frac{\pi}{6}$|$\frac{\pi}{4}$|$\frac{\pi}{3}$|$\frac{\pi}{2}$|$\frac{2\pi}{3}$|$\frac{5\pi}{6}$|$\pi$|
>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>|$\sin \theta$|$0$|$\frac{1}{2}$|$\frac{\sqrt{2}}{2}$|$\frac{\sqrt{3}}{2}$|$1$|$\frac{\sqrt{3}}{2}$|$\frac{1}{2}$|$0$|
>|$\cos \theta$|$1$|$\frac{\sqrt{3}}{2}$|$\frac{\sqrt{2}}{2}$|$\frac{1}{2}$|$0$|$-\frac{1}{2}$|$-\frac{\sqrt{3}}{2}$|$-1$|
>|$\tan \theta$|$0$|$\frac{\sqrt{3}}{3}$|$1$|$\sqrt{3}$||$-\sqrt{3}$|$-\frac{\sqrt{3}}{3}$|$0$|
>|$\cot \theta$||$\sqrt{3}$|$1$|$\frac{\sqrt{3}}{3}$|$0$|$-\frac{\sqrt{3}}{3}$|$-\sqrt{3}$||
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Fundamental Trigonometric Identities
>
>[Sine](./Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function), [cosine](./Real%20Trigonometric%20Functions.md#The%20Real%20Cosine%20Function), [tangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function) and [cotangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Cotangent%20Function) obey the following identities:
>
>$$
>\sin^2 \theta + \cos^2 \theta = 1
>$$
>
>$$
>\tan \theta \cot \theta = 1
>$$
>
>>[!PROOF]-
>>
>>**Proof of (1):**
>>
>>We define $f(\theta) = \sin^2 \theta + \cos^2 \theta$ and then [differentiate](../Differentiability%20(Real%20Functions).md) $f$:
>>
>>$$
>>\begin{aligned}
>>f'(\theta) &= (\sin^2 \theta + \cos^2 \theta)' \\
>>&= (\sin^2 \theta)' + (\cos^2 \theta)' \\
>>&= 2\sin \theta \cos \theta - 2 \cos \theta \sin \theta = 0
>>\end{aligned}
>>$$
>>
>>Since the [derivative](../Differentiability%20(Real%20Functions).md) of $f$ is always zero, we know that $f$ is a constant function, i.e. $f(\theta) = C$ for all $\theta$. To find $C$, we just need to evaluate $f$ at any convenient point, for example $\theta = 0$.
>>
>>$$
>>f(0) = \sin^2(0) + \cos^2(0) = 0 + 1 = 1
>>$$
>>
>>**Proof of (2):**
>>
>>This follows directly from the definitions of [tangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function) and [cotangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Cotangent%20Function).
>>
>

>[!THEOREM] Theorem: Universal Trigonometric Substitution
>
>The [sine](./Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function), [cosine](./Real%20Trigonometric%20Functions.md#The%20Real%20Cosine%20Function), [tangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function) and [cotangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Cotangent%20Function) of $\theta$ can all be expressed in terms of $\tan \frac{\theta}{2}$:
>
>$$
>\sin \theta = \frac{2\tan \frac{\theta}{2}}{1+\tan^2 \frac{\theta}{2}}
>$$
>
>$$
>\cos \theta = \frac{1 - \tan^2 \frac{\theta}{2}}{1 + \tan^2 \frac{\theta}{2}}
>$$
>
>$$
>\tan \theta = \frac{2\tan \frac{\theta}{2}}{1-\tan^2\frac{\theta}{2}}
>$$
>
>$$
>\cot \theta = \frac{1-\tan^2\frac{\theta}{2}}{2\tan \frac{\theta}{2}}
>$$
>
>>[!PROOF]-
>>
>>**Proof of (1):**
>>
>>
>>
>>TODO
>>
>

# Angle Sums

>[!THEOREM] Theorem: Trigonometric Identities for Angle Sums
>
>[Sine](./Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function), [cosine](./Real%20Trigonometric%20Functions.md#The%20Real%20Cosine%20Function), [tangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function) and [cotangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Cotangent%20Function) have the following properties:
>
>$$
>\begin{aligned}
>\sin(\theta \pm \varphi) &= \sin\theta\cos\varphi \pm \cos\theta \sin \varphi \\ \\ \cos (\theta \pm \varphi) &= \cos \theta \cos \varphi \mp \sin \theta \sin \varphi \\ \\ \tan (\theta \pm \varphi) &= \frac{\tan \theta \pm \tan \varphi}{1 \mp \tan \theta \tan \varphi} \\ \\ \cot(\theta \pm \varphi) &= \frac{\cot \theta \cot \varphi \mp 1}{\cot \varphi \pm \cot \theta}
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>**Proof of (1):**
>>
>>From the definition of [sine](./Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function):
>>
>>$$
>>\sin(\theta + \varphi) = \sum_{n = 0}^\infty (-1)^n \frac{(\theta+\varphi)^{2n+1}}{(2n+1)!}
>>$$
>>
>>Using the [binomial theorem](../../../../Algebra/Fields/The%20Real%20Numbers/Real%20Polynomials.md), we can rewrite $(\theta+\varphi)^{2n+1}$ as
>>
>>$$
>>(\theta+\varphi)^{2n+1} = \sum_{k = 0}^{2n+1} \binom{2n+1}{k} \theta^k \varphi^{2n+1 - k}
>>$$
>>
>>Therefore,
>>
>>$$
>>\sin(\theta + \varphi) = \sum_{n = 0}^\infty \left[\frac{(-1)^n}{(2n+1)!} \sum_{k = 0}^{2n+1} \binom{2n+1}{k} \theta^k \varphi^{2n+1 - k}\right]
>>$$
>>
>>We notice that when $k$ is odd, $(2n+1 - k)$ is even and, when $k$ is even, $(2n + 1 - k)$ is odd. We thus split the inner sum (the one over $k$) into two sums, where the first contains only the odd powers of $\theta$ and the second contains only the even powers of $\theta$.
>>
>>$$
>>\sum_{k = 0}^{2n+1} \binom{2n+1}{k} \theta^k \varphi^{2n+1 - k} = \sum_{j = 0}^n \binom{2n+1}{2j+1} \theta^{2j + 1} \varphi^{2n - 2j} + \sum_{j = 0}^n \binom{2n+1}{2j} \theta^{2j} \varphi^{2n + 1 - 2j}
>>$$
>>
>>We can substitute this into the formula for $\sin(\theta + \varphi)$:
>>
>>$$
>>\sin(\theta + \varphi) = \sum_{n = 0}^\infty \frac{(-1)^n}{(2n+1)!}\left[ \sum_{j = 0}^n \binom{2n+1}{2j+1} \theta^{2j + 1} \varphi^{2n - 2j} + \sum_{j = 0}^n \binom{2n+1}{2j} \theta^{2j} \varphi^{2n + 1 - 2j}\right] \\
>>$$
>>
>>Since the [power series](../../Real%20Power%20Series.md) for [sine](./Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function) is [absolutely convergent](../../Real%20Power%20Series.md#Convergence) everywhere, we can distribute the outer sum:
>>
>>$$
>>\sin(\theta + \varphi) = \sum_{n = 0}^\infty \frac{(-1)^n}{(2n+1)!} \left[\sum_{j = 0}^n \binom{2n+1}{2j+1} \theta^{2j + 1} \varphi^{2n - 2j} \right] + \sum_{n = 0}^\infty \frac{(-1)^n}{(2n+1)!} \left[\sum_{j = 0}^n \binom{2n+1}{2j} \theta^{2j} \varphi^{2n + 1 - 2j}\right]
>>$$
>>
>>We examine each part separately.
>>
>>$$
>>\sum_{n = 0}^\infty \frac{(-1)^n}{(2n+1)!} \left[\sum_{j = 0}^n \binom{2n+1}{2j+1} \theta^{2j + 1} \varphi^{2n - 2j} \right] = \sum_{n = 0}^\infty \sum_{j = 0}^n \frac{(-1)^n}{(2n+1)!} \binom{2n+1}{2j+1} \theta^{2j + 1} \varphi^{2n - 2j}
>>$$
>>
>>Expand the [binomial coefficient](../../../../Algebra/Fields/The%20Real%20Numbers/Real%20Polynomials.md):
>>
>>$$
>>\sum_{n = 0}^\infty \sum_{j = 0}^n \frac{(-1)^n}{(2n+1)!} \binom{2n+1}{2j+1} \theta^{2j + 1} \varphi^{2n - 2j} = \sum_{n = 0}^\infty \sum_{j = 0}^n \frac{(-1)^n}{(2n+1)!} \frac{(2n+1)!}{(2j+1)!(2n - 2j)!} \theta^{2j + 1} \varphi^{2n - 2j}
>>$$
>>
>>Cancel the $(2n+1)!$ factors:
>>
>>$$
>>\sum_{n = 0}^\infty \sum_{j = 0}^n \frac{(-1)^n}{(2n+1)!} \frac{(2n+1)!}{(2j+1)!(2n - 2j)!} \theta^{2j + 1} \varphi^{2n - 2j} = \sum_{n = 0}^\infty \sum_{j = 0}^n \frac{(-1)^n}{(2j+1)!(2n - 2j)!} \theta^{2j + 1} \varphi^{2n - 2j}
>>$$
>>
>>Let $m = n - j$. We can thus rewrite $(-1)^n$ as $(-1)^{j+m} = (-1)^j (-1)^m$ and obtain
>>
>>$$
>>\begin{aligned}
>>\sum_{n = 0}^\infty \sum_{j = 0}^n \frac{(-1)^n}{(2j+1)!(2n - 2j)!} \theta^{2j + 1} \varphi^{2n - 2j} &= \sum_{j = 0}^{\infty}\sum_{m = 0}^{\infty} (-1)^j (-1)^m \frac{\theta^{2j+1}}{(2j+1)!}\frac{\varphi^{2m}}{(2m)!} \\
>>&= \left(\sum_{j=0}^{\infty} \frac{(-1)^j}{(2j+1)!}\theta^{2j + 1}\right) \left(\sum_{m = 0}^{\infty} \frac{(-1)^m}{(2m)!}\varphi^{2m}\right)
>>\end{aligned}
>>$$
>>
>>The first parentheses contain the definition of $\sin \theta$ and the second parentheses contain the definition of $\cos \varphi$. Therefore,
>>
>>$$
>>\sin(\theta + \varphi) = \sin \theta \cos \varphi + \sum_{n = 0}^\infty \frac{(-1)^n}{(2n+1)!} \left[\sum_{j = 0}^n \binom{2n+1}{2j} \theta^{2j} \varphi^{2n + 1 - 2j}\right].
>>$$
>>
>>The proof that the second sum is equal to $\cos \theta \sin \varphi$ is analogous.
>>
>>To prove that $\sin(\theta - \varphi) = \sin \theta \cos \varphi - \cos \theta \sin \varphi$, we use the [parity](../Parity.md) of [sine](./Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function) and [cosine](./Real%20Trigonometric%20Functions.md#The%20Real%20Cosine%20Function):
>>
>>$$
>>\sin(\theta - \varphi) = \sin(\theta + (-\varphi)) = \sin \theta \cos (-\varphi) + \cos \theta \sin (-\varphi) = \sin \theta \cos \varphi - \cos \theta \sin \varphi
>>$$
>>
>>**Proof of (2):**
>>
>>We use the fact that $\cos(\theta \pm \varphi) = \sin\left(\frac{\pi}{2} - (\theta \pm \varphi)\right)$:
>>
>>$$
>>\cos(\theta + \varphi) = \sin\left(\frac{\pi}{2} - (\theta + \varphi)\right) = \sin\left(\left(\frac{\pi}{2} - \theta\right) - \varphi\right)
>>$$
>>
>>Apply the formula for $\sin (x - y)$:
>>
>>$$
>>\sin\left(\left(\frac{\pi}{2} - \theta\right) - \varphi\right) = \sin\left(\frac{\pi}{2} - \theta\right)\cos{\varphi} - \cos\left(\frac{\pi}{2} - \theta\right)
>>$$
>>
>>Again, we use the fact that $\sin\left(\frac{\pi}{2} - x\right) = \cos(x)$ and $\sin\left(\frac{\pi}{2} - x\right) = \cos(x)$:
>>
>>$$
>>\sin\left(\frac{\pi}{2} - \theta\right)\cos{\varphi} - \cos\left(\frac{\pi}{2} - \theta\right) = \cos \theta \cos \varphi - \sin \theta \sin \varphi
>>$$
>>
>>To prove that $\cos(\theta - \varphi) = \cos \theta \cos \varphi + \sin \theta \sin \varphi$, we use the [parity](../Parity.md) of [sine](./Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function) and [cosine](./Real%20Trigonometric%20Functions.md#The%20Real%20Cosine%20Function):
>>
>>$$
>>\cos(\theta - \varphi) = \cos(\theta + (-\varphi)) = \cos \theta \cos (-\varphi) - \sin \theta \sin (-\varphi) = \cos \theta \cos \varphi + \sin \theta \sin \varphi
>>$$
>>
>>**Proof of (3):**
>>
>>We use the definition of [tangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function):
>>
>>$$
>>\tan(\theta \pm \varphi) = \frac{\sin (\theta \pm \varphi)}{\cos(\theta \pm \varphi)}
>>$$
>>
>>Use the formulas for $\sin (x \pm y)$ and $\cos (x \pm y)$:
>>
>>$$
>>\frac{\sin (\theta \pm \varphi)}{\cos(\theta \pm \varphi)} = \frac{\sin \theta \cos \varphi + \cos \theta \sin \varphi}{\cos \theta \cos \varphi \mp \sin \theta \sin \varphi}
>>$$
>>
>>We divide the numerator and denominator by $\cos \theta \cos \varphi$:
>>
>>$$
>>\frac{\sin \theta \cos \varphi \pm \cos \theta \sin \varphi}{\cos \theta \cos \varphi \mp \sin \theta \sin \varphi} = \frac{\frac{\sin\theta \cos\varphi}{\cos\theta \cos\varphi} \pm \frac{\cos\theta \sin\varphi}{\cos\theta \cos\varphi}}{\frac{\cos\theta \cos\varphi}{\cos\theta \cos\varphi} \mp \frac{\sin\theta \sin\varphi}{\cos\theta \cos\varphi}}
>>$$
>>
>>Cancel like terms:
>>
>>$$
>>\frac{\frac{\sin\theta \cos\varphi}{\cos\theta \cos\varphi} \pm \frac{\cos\theta \sin\varphi}{\cos\theta \cos\varphi}}{\frac{\cos\theta \cos\varphi}{\cos\theta \cos\varphi} \mp \frac{\sin\theta \sin\varphi}{\cos\theta \cos\varphi}} = 
>>\frac{\frac{\sin\theta}{\cos\theta} \pm \frac{\sin\varphi}{\cos\varphi}}{1 \mp \left(\frac{\sin\theta}{\cos\theta}\right)\left(\frac{\sin\varphi}{\cos\varphi}\right)}
>>$$
>>
>>Use the definition of [tangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function) again:
>>
>>$$
>>\frac{\frac{\sin\theta}{\cos\theta} \pm \frac{\sin\varphi}{\cos\varphi}}{1 \mp \left(\frac{\sin\theta}{\cos\theta}\right)\left(\frac{\sin\varphi}{\cos\varphi}\right)} = \frac{\tan \theta \pm \tan \varphi}{1 \mp \tan \theta \tan \varphi}
>>$$
>>
>>**Proof of (4):**
>>
>>We use the definition of [cotangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Cotangent%20Function):
>>
>>$$
>>\cot (\theta \pm \varphi) = \frac{\cos(\theta \pm \varphi)}{\sin(\theta \pm \varphi)}
>>$$
>>
>>Apply the formulas for $\cos(\theta \pm \varphi)$ and $\sin(\theta \pm \varphi)$:
>>
>>$$
>>\frac{\cos (\theta \pm \varphi)}{\sin(\theta \pm \varphi)} = \frac{\cos \theta \cos \varphi \mp \sin \theta \sin \varphi}{\sin \theta \cos \varphi \pm \cos \theta \sin \varphi}
>>$$
>>
>>We divide the numerator and denominator by $\sin \theta \sin \varphi$:
>>
>>$$
>>\frac{\cos \theta \cos \varphi \mp \sin \theta \sin \varphi}{\sin \theta \cos \varphi \pm \cos \theta \sin \varphi} = \frac{\frac{\cos \theta \cos \varphi}{\sin \theta \sin \varphi} \mp \frac{\sin \theta \sin \varphi}{\sin \theta \sin \varphi}}{\frac{\sin \theta \cos \varphi}{\sin \theta \sin \varphi} \pm \frac{\cos \theta \sin \varphi}{\sin \theta \sin \varphi}}
>>$$
>>
>>Cancel like terms:
>>
>>$$
>>\frac{\frac{\cos \theta \cos \varphi}{\sin \theta \sin \varphi} \mp \frac{\sin \theta \sin \varphi}{\sin \theta \sin \varphi}}{\frac{\sin \theta \cos \varphi}{\sin \theta \sin \varphi} \pm \frac{\cos \theta \sin \varphi}{\sin \theta \sin \varphi}} = \frac{\frac{\cos \theta}{\sin \theta} \frac{\cos \varphi}{\sin \varphi} \mp 1}{\frac{\cos \varphi}{\sin \varphi} \pm \frac{\cos \theta}{\sin \theta}}
>>$$
>>
>>Use the definition of [cotangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Cotangent%20Function) again:
>>
>>$$
>>\frac{\frac{\cos \theta}{\sin \theta} \frac{\cos \varphi}{\sin \varphi} \mp 1}{\frac{\cos \varphi}{\sin \varphi} \pm \frac{\cos \theta}{\sin \theta}} = \frac{\cot \theta \cot \varphi \mp 1}{\cot \varphi \pm \cot \theta}
>>$$
>>
>

# Angle Products

>[!THEOREM] Theorem: Chebyshev's Formulas
>
>The [sine](./Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function), [cosine](./Real%20Trigonometric%20Functions.md#The%20Real%20Cosine%20Function) and [tangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function) obey Chebyshev's formulas for every $r \in \mathbb{R}$:
>
>$$
>\begin{aligned}\sin(r\varphi) &= 2\cos \varphi \sin ((r-1)\varphi) - \sin ((r-2)\varphi) \\ \\ \cos (r \varphi) &= 2\cos \varphi \cos ((r-1)\varphi) - \cos((r-2)\varphi) \\ \\ \tan(r\varphi) &= \frac{\tan((r-1)\varphi) + \tan \varphi}{1 - \tan \varphi\tan ((r-1)\varphi)} \end{aligned}
>$$
>
>>[!PROOF]-
>>
>>TODO
>
>

>[!THEOREM] Theorem: Double-Angle Formulas
>
>The [sine](./Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function), [cosine](./Real%20Trigonometric%20Functions.md#The%20Real%20Cosine%20Function), [tangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function) and [cotangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Cotangent%20Function) of $2\theta$ can be expressed as
>
>
>$$
>\begin{aligned} \sin(2\theta) &= 2\sin \theta \cos \theta \\ \\ \cos(2\theta) &= 2\cos^2\theta + 1 = \cos^2 \theta - \sin^2 \theta = 1-2\sin^2 \theta \\ \\ \tan (2\theta) &= \frac{2\tan \theta}{1-\tan^2 \theta} \end{aligned}
>$$
>
>>[!PROOF]-
>>
>>**Proof of (1):**
>>
>>We use the summation formula:
>>
>>$$
>>\sin(2\theta) = \sin(\theta + \theta) = \sin\theta\cos\theta + \cos\theta\sin\theta = 2 \sin \theta \cos \theta
>>$$
>>
>>**Proof of (2):**
>>
>>TODO
>>
>>**Proof of (3):**
>>
>>We use the summation formula:
>>
>>$$
>>\tan(2 \theta) = \tan(\theta + \theta) = \frac{\tan \theta + \tan \theta}{1 - \tan \theta \tan \theta} = \frac{2 \tan \theta}{1 - \tan^2 \theta}
>>$$
>>
>

>[!THEOREM] Theorem: Half-Angle Formulae
>
>The [sine](./Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function), [cosine](./Real%20Trigonometric%20Functions.md#The%20Real%20Cosine%20Function), [tangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function) and [cotangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Cotangent%20Function) obey the following properties:
>
>$$
>\begin{aligned}\sin \frac{\theta}{2} &= \operatorname{sgn}\left(\sin \frac{\theta}{2}\right) \sqrt{\frac{1-\cos\theta}{2}} \\ \\ \cos \frac{\theta}{2} &= \operatorname{sgn}\left(\cos \frac{\theta}{2}\right) \sqrt{\frac{1+\cos\theta}{2}} \\ \\ \tan\frac{\theta}{2} &= \frac{\sin \theta}{1+\cos \theta} = \frac{1 - \cos \theta}{\sin \theta} = \operatorname{sgn}(\sin \theta) \sqrt{\frac{1-\cos \theta}{1+\cos \theta}} \\ \\ \cot \frac{\theta}{2} &= \frac{1+\cos \theta}{\sin \theta} = \frac{\sin \theta}{1 - \cos \theta} = \pm \sqrt{\frac{1+\cos \theta}{1-\cos \theta}} \end{aligned}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Argument Offsets

>[!THEOREM] Theorem: Trigonometric Identities for Argument Offsets
>
>The [sine](./Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function), [cosine](./Real%20Trigonometric%20Functions.md#The%20Real%20Cosine%20Function), [tangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function) and [cotangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Cotangent%20Function) have the following properties:
>
>||$\frac{\pi}{2}+\theta$|$\frac{\pi}{2}-\theta$|$\pi+\theta$|$\pi-\theta$|$\frac{3\pi}{2} + \theta$|$\frac{3\pi}{2} - \theta$|
>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>|$\sin$|$\cos \theta$|$\cos \theta$|$-\sin \theta$|$\sin \theta$|$-\cos \theta$|$-\cos \theta$|
>|$\cos$|$-\sin \theta$|$\sin \theta$|$-\cos \theta$|$-\cos \theta$|$\sin \theta$|$-\sin \theta$|
>|$\tan$|$-\cot \theta$|$\cot \theta$|$\tan \theta$|$-\tan \theta$|$-\cot \theta$|$\cot \theta$|
>|$\cot$|$-\tan \theta$|$\tan \theta$|$\cot \theta$|$-\cot \theta$|$-\tan \theta$|$\tan \theta$|
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Function Sums

>[!THEOREM] Theorem: Trigonometric Identities for Function Sums
>
>[sine](./Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function), [cosine](./Real%20Trigonometric%20Functions.md#The%20Real%20Cosine%20Function), [tangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function) and [cotangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Cotangent%20Function) have the following properties:
>
>$$
>\begin{aligned}
>\sin \theta \pm \sin \varphi &= 2\sin \frac{\theta \pm \varphi}{2} \cos \frac{\theta \mp \varphi}{2} \\ \\
>\cos \theta + \cos \varphi &= 2 \cos \frac{\theta + \varphi}{2} \cos \frac{\theta - \varphi}{2} \\ \\
>\cos \theta - \cos \varphi &= -2 \sin \frac{\theta + \varphi}{2} \sin \frac{\theta - \varphi}{2} \\ \\
>\tan \theta \pm \tan \varphi &= \frac{\sin(\theta \pm \varphi)}{\cos \theta \cos \varphi} \\ \\
>\cot \theta \pm \cot \varphi &= \frac{\sin(\varphi \pm \theta)}{\sin \theta \sin \varphi}
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>**Proof of (1):**
>>
>>**Proof of (2):**
>>
>>**Proof of (3):**
>>
>>**Proof of (4):**
>>
>>We use the definition of [tangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function) and the formula for $\sin (x \pm y)$:
>>
>>$$
>>\begin{aligned}
>>\tan \theta \pm \tan \varphi &= \frac{\sin \theta}{\cos \theta} \pm \frac{\sin \varphi}{\cos \varphi} \\
>>&= \frac{\sin \theta \cos \varphi \pm \sin \varphi \cos \theta}{\cos \theta \cos \varphi} \\
>>&= \frac{\sin (\theta \pm \varphi)}{\cos \theta \cos \varphi}
>>\end{aligned}
>>$$
>>
>>**Proof of (5):**
>>
>>TODO
>>
>

# Function Products

>[!THEOREM] Theorem: Trigonometric Identities for Function Products
>
>[sine](./Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function), [cosine](./Real%20Trigonometric%20Functions.md#The%20Real%20Cosine%20Function), [tangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function) and [cotangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Cotangent%20Function) have the following properties:
>
>$$
>\begin{aligned}
>\cos \theta \cos \varphi &= \frac{1}{2}(\cos(\theta - \varphi) + \cos(\theta + \varphi)) \\ \\
>\sin \theta \sin \varphi &= \frac{1}{2}(\cos(\theta - \varphi) - \cos(\theta + \varphi)) \\ \\
>\sin \theta \cos \varphi &= \frac{1}{2}(\sin(\theta + \varphi) + \sin(\theta - \varphi)) \\ \\
>\tan \theta \tan \varphi &= \frac{\cos(\theta - \varphi) - \cos (\theta + \varphi)}{\cos(\theta - \varphi) + \cos (\theta + \varphi)} \\ \\
>\tan \theta \cot \varphi &= \frac{\sin(\theta + \varphi) + \sin(\theta - \varphi)}{\sin(\theta + \varphi) - \sin(\theta - \varphi)}\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>**Proof of (1):**
>>
>>We use the formula for $\cos(x \pm y)$:
>>
>>$$
>>\begin{aligned}
>>\frac{1}{2}(\cos(\theta - \varphi) + \cos(\theta + \varphi)) &= \frac{1}{2}(\cos \theta \cos \varphi + \sin \theta \sin \varphi + \cos \theta \cos \varphi - \sin \theta \sin \varphi) \\ &= \frac{1}{2} \cdot 2 \cos \theta \cos \varphi \\ &= \cos \theta \cos \varphi
>>\end{aligned}
>>$$
>>
>>**Proof of (2):**
>>
>>We use the formula for $\cos(x \pm y)$:
>>
>>$$
>>\begin{aligned}
>>\frac{1}{2}(\cos(\theta - \varphi) - \cos(\theta + \varphi)) &= \frac{1}{2}(\cos \theta \cos \varphi + \sin \theta \sin \varphi - ( \cos \theta \cos \varphi - \sin \theta \sin \varphi)) \\ &= \frac{1}{2}(\cos \theta \cos \varphi + \sin \theta \sin \varphi - \cos \theta \cos \varphi + \sin \theta \sin \varphi) \\ &= \frac{1}{2} \cdot 2 \sin \theta \sin \varphi \\ &= \sin \theta \sin \varphi
>>\end{aligned}
>>$$
>>
>>**Proof of (3):**
>>
>>We use the formula for $\sin(x \pm y)$:
>>
>>$$
>>\frac{1}{2}(\sin(\theta + \varphi) + \sin(\theta - \varphi)) = \frac{1}{2}(\sin \theta \cos \varphi + \cos \theta \sin \varphi + \sin \theta \cos \varphi - \cos \theta \sin \varphi) = \frac{1}{2}\cdot 2 \sin \theta \cos \varphi = \sin \theta \cos \varphi
>>$$
>>
>>**Proof of (4):**
>>
>>We use the definition of [tangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function) and the formulas for $\sin \theta \sin \varphi$ and $\cos \theta \cos \varphi$:
>>
>>$$
>>\begin{aligned}
>>\tan \theta \tan \varphi &= \frac{\sin \theta}{\cos \theta}\frac{\sin \varphi}{\cos \varphi} \\
>>&= \frac{\sin \theta \sin \varphi}{\cos \theta \cos \varphi} \\
>>&= \frac{\frac{1}{2}(\cos(\theta - \varphi) - \cos(\theta + \varphi))}{\frac{1}{2}(\cos(\theta - \varphi) + \cos(\theta + \varphi))} \\
>>&= \frac{\cos(\theta - \varphi) - \cos (\theta + \varphi)}{\cos(\theta - \varphi) + \cos (\theta + \varphi)}
>>\end{aligned}
>>$$
>>
>>**Proof of (5):**
>>
>>We use the definition of [tangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function) and [cotangent](./Real%20Trigonometric%20Functions.md#The%20Real%20Tangent%20Function) and the formula for $\sin \theta \sin \varphi$ and $\cos \theta \cos \varphi$:
>>
>>$$
>>\begin{aligned}
>>\tan \theta \cot \varphi &= \frac{\sin \theta}{\cos \theta}\frac{\cos \varphi}{\sin \varphi} \\
>>&= \frac{\sin \theta \cos \varphi}{\cos \theta \sin \varphi} \\
>>&= \frac{\frac{1}{2}(\sin(\theta + \varphi) + \sin(\theta - \varphi))}{\frac{1}{2}(\sin(\varphi + \theta) + \sin(\varphi - \theta))} \\
>>&= \frac{\sin(\theta + \varphi) + \sin(\theta - \varphi)}{\sin(\varphi + \theta) + \sin(\varphi - \theta)} \\
>>&= \frac{\sin(\theta + \varphi) + \sin(\theta - \varphi)}{\sin(\theta + \varphi) - \sin(\theta - \varphi)}
>>\end{aligned}
>>$$
>>
>

# Compositions

>[!THEOREM] Theorem: Functions of Arcfunctions
>
>The [compositions](../../../Functions/Functions.md) of [inverse real trigonometric functions](./Inverse%20Real%20Trigonometric%20Functions.md) inside [real trigonometric functions](./Real%20Trigonometric%20Functions.md) have the following properties:
>
>$$
>\begin{aligned}
>
>&\sin(\arctan x) = \frac{x}{\sqrt{1+x^2}} \\
>
>&\cos(\arctan (x)) = \frac{1}{\sqrt{1 + x^2}} \\
>
>&\cos(\arcsin(x)) = \sqrt{1 - x^2} \\
>
>&\cos\left(\arctan \left( \frac{1}{x} \right) \right) = \frac{|x|}{\sqrt{1 + x^2}} 
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>**Proof of (1):**
>>
>>We substitute $y = \arctan x$ and so $x = \tan y$. Therefore, we have
>>
>>$$
>>\sin(\arctan x) = \frac{x}{\sqrt{1+x^2}} \iff \sin y = \frac{\tan y}{\sqrt{1 + \tan^2 y}}
>>$$
>>
>>Now, we use the definition of $\tan y$:
>>
>>$$
>>\begin{aligned}
>>\frac{\tan y}{\sqrt{1 + \tan^2 y}} &= \frac{\frac{\sin y}{\cos y}}{\sqrt{1 + \frac{\sin^2 y}{\cos^2 y}}} \\ &= \frac{\sin y}{\cos y} \times \frac{1}{\sqrt{1 + \frac{\sin^2 y}{\cos^2 y}}} \\ &= \frac{\sin y}{\cos y} \times \frac{1}{\sqrt{ \frac{\cos^2 y + \sin^2 y}{\cos^2 y}}} \\ &= \frac{\sin y}{\cos y} \times \frac{1}{\sqrt{ \frac{1}{\cos^2 y}}} \\ &= \frac{\sin y}{\cos y} \times \sqrt{\cos^2 y}
>>\end{aligned}
>>$$
>>
>>Since $y = \arctan x$ and the [image](../../../Functions/Functions.md) of $\arctan$ is $\left(-\frac{\pi}{2}; \frac{\pi}{2}\right)$, we know that $y \in \left(-\frac{\pi}{2}; \frac{\pi}{2}\right)$. For $y = \left(-\frac{\pi}{2}; \frac{\pi}{2}\right)$, we know that $\cos y \gt 0$, so we can cancel the square root and the second power.
>>
>>$$
>>\frac{\sin y}{\cos y} \times \sqrt{\cos^2 y} = \frac{\sin y}{\cos y} \times \cos y = \sin y
>>$$
>>
>>**Proof of (3):**
>>
>>From $\sin^2 y + \cos^2 y = 1$, we get
>>
>>$$
>>\sin^2 (\arcsin x) + \cos^2(\arcsin x) = 1
>>$$
>>
>>for some $x = \sin (y)$. We thus get
>>
>>$$
>>\begin{aligned}
>>&x^2 + \cos^2(\arcsin x) = 1 \\
>>&\cos^2(\arcsin x) = 1 - x^2
>>\end{aligned}
>>$$
>>
>>The right-hand side is always non-negative for the [domain](../../../Functions/Functions.md) of $\arcsin$, i.e. $x \in [-1; +1]$, so we can take the square root:
>>
>>$$
>>\cos (\arcsin x) = \sqrt{1-x^2}
>>$$
>>
>>TODO
>>
>