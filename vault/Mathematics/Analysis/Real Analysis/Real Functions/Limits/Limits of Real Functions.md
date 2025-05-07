---
title: Limits of Real Functions
tags:
  - limits
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

# Real One-Sided Limits

>[!DEFINITION] Definition: Left-Sided Limit
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../../Functions%20of%20the%20Real%20Numbers.md).
>
>A number $L \in \mathbb{R}$ is called the **left-sided limit of** $f$ **as** $x$ **approaches** $c \in D$ if for every $\varepsilon \gt 0$ there is a $\delta \gt 0$ such that for all $x \in D$ with $x \lt c$
>
>$$
>|x-c| \lt \delta \implies |f(x)-L| \lt \varepsilon
>$$
>
>>[!NOTATION]
>>
>>$$
>>\begin{align*}
>>&\lim_{x\to c^-} f(x) = L \\ 
>>&\lim_{\begin{matrix} x \to c^+ \\ x \lt c\end{matrix}} f(x) = L
>>\end{align*}
>>$$
>>
>

>[!DEFINITION] Definition: Right-Sided Limit
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../../Functions%20of%20the%20Real%20Numbers.md).
>
>A number $L \in \mathbb{R}$ is called the **right-sided limit** of $f$ as $x$ approaches $c \in D$ if for every $\varepsilon \gt 0$ there is a $\delta \gt 0$ such that for all $x \in D$ with $x \gt c$
>
>$$|x-c| \lt \delta \implies |f(x)-L| \lt \varepsilon$$
>
>>[!NOTATION]
>>
>>$$
>>\begin{align*}
>>&\lim_{x\to c^+} f(x) = L \\ 
>>&\lim_{\begin{matrix} x \to c^+ \\ x \gt c\end{matrix}} f(x) = L
>>\end{align*}
>>$$
>>
>

# Real Limits

>[!DEFINITION] Definition: Limit of a Function (Cauchy)
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../../Functions%20of%20the%20Real%20Numbers.md).
>
>A real number $L \in \mathbb{R}$ is called the **limit of** $f$ **as** $x$ **approaches** $c \in \mathbb{R}$ if for every $\varepsilon \gt 0$ there is a $\delta \gt 0$ such that for all $x \in D$ with $x \ne c$
>
>$$
>|x-c| \lt \delta \implies |f(x)-L| \lt \varepsilon
>$$
>
>>[!NOTATION]
>>
>>$$
>>\lim_{x\to c} f(x) = L
>>$$
>
>>[!DEFINITION] Definition: Limit at Positive Infinity
>>
>>A real number $L \in \mathbb{R}$ is called the **limit of** $f$ **as** $x$ **approaches positive infinity** if for every $\varepsilon \gt 0$ there is a $A \in \mathbb{R}$ such that
>>
>>$$
>>|f(x) - L| \lt \varepsilon \qquad \forall x \ge A
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\lim_{x\to \infty} f(x) = L
>>>$$
>>>
>>
>
>>[!DEFINITION] Definition: Limit at Negative Infinity
>>
>>A real number $L \in \mathbb{R}$ is called the **limit of** $f$ **as** $x$ **approaches negative infinity** if for every $\varepsilon \gt 0$ there is a $A \in \mathbb{R}$ such that
>>
>>$$
>>|f(x) - L| \lt \varepsilon \qquad \forall x \le A
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\lim_{x\to -\infty} f(x) = L
>>>$$
>>>
>>
>
>If $f$ has a limit $L \in \mathbb{R}$, then the limit is said to exist.
>

## Characterizations

>[!THEOREM]- Theorem: Real Limit and One-Sided Real Limits
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../../Functions%20of%20the%20Real%20Numbers.md).
>
>The [two-sided limit](Limits%20of%20Real%20Functions.md#Real%20Limits) of $f$ as $x$ approaches $c \in \mathbb{R}$ exists if and only if both [one-sided limits](Limits%20of%20Real%20Functions.md#Real%20One-Sided%20Limits) of $f$ at $c$ exist and are equal.
>
>$$
>\lim_{x \to c} f(x) = L \in \mathbb{R} \iff \lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = L
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Infinite Limits

>[!DEFINITION] Definition: Infinite Limits
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../../Functions%20of%20the%20Real%20Numbers.md).
>
>>[!DEFINITION] Definition: Approaching Positive Infinity
>>
>>We say that $f$ **approaches positive infinity as** $x$ **approaches** $c \in \mathbb{R}$ if for every $A \in \mathbb{R}$ there is a $\delta \gt 0$ such that for all $x \in D$
>>
>>$$
>>|x-c| \lt \delta \implies f(x) \gt A
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\lim_{x\to c} f(x) = \infty
>>>$$
>>
>>>[!DEFINITION] Definition: Approaching Positive Infinity for $x\to \pm \infty$
>>>
>>>We say that $f$ **approaches positive infinity**
>>>- **as** $x$ **approaches** $-\infty$ if for every $A \in \mathbb{R}$ there is a $B \in \mathbb{R}$ such that $f(x) \gt A$ for all $x \lt B$;
>>>- **as** $x$ **approaches** $\infty$ if for every $A \in \mathbb{R}$ there is a $B \in \mathbb{R}$ such that $f(x) \gt A$ for all $x \gt B$.
>>>
>>>>[!NOTATION]
>>>>
>>>>$$
>>>>\lim_{x\to -\infty} f(x) = \infty
>>>>$$
>>>>
>>>>$$
>>>>\lim_{x \to \infty} f(x) = \infty
>>>>$$
>>>>
>>>
>>
>
>>[!DEFINITION] Definition: Approaching Negative Infinity
>>
>>We say that $f$ **approaches negative infinity as** $x$ **approaches** $c \in \mathbb{R}$ if for every $A \in \mathbb{R}$ there is a $\delta \gt 0$ such that for all $x \in D$
>>
>>$$
>>|x-c| \lt \delta \implies f(x) \lt A
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\lim_{x\to c} f(x) = -\infty
>>>$$
>>
>>>[!DEFINITION] Definition: Approaching Negative Infinity for $x\to \pm \infty$
>>>
>>>We say that $f$ **approaches negative infinity**
>>>- **as** $x$ **approaches** $-\infty$ if for every $A \in \mathbb{R}$ there is a $B \in \mathbb{R}$ such that $f(x) \lt A$ for all $x \lt B$;
>>>- **as** $x$ **approaches** $\infty$ if for every $A \in \mathbb{R}$ there is a $B \in \mathbb{R}$ such that $f(x) \lt A$ for all $x \gt B$.
>>>
>>>>[!NOTATION]
>>>>
>>>>$$
>>>>\lim_{x\to -\infty} f(x) = -\infty
>>>>$$
>>>>
>>>>$$
>>>>\lim_{x \to \infty} f(x) = -\infty
>>>>$$
>>>>
>>>
>>
>

## Infinite One-Sided Limits

>[!DEFINITION] Definition: Infinite One-Sided Limits
>
>Let $f$ be a [real function](../../Functions%20of%20the%20Real%20Numbers.md).
>
>>[!DEFINITION] Definition: Positive Infinity as a Left-Sided Limit
>>
>>We say that $f$ **approaches positive infinity as** $x$ **approaches** $c\in D$ **from the left** if for every $A \in \mathbb{R}$ there is a $\delta \gt 0$ such that for all $x \in D$ with $x \lt c$
>>
>>$$
>>|x-c| \lt \delta \implies f(x) \gt A
>>$$
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>\lim_{x\to c^-} f(x) = \infty
>>>$$
>>
>
>>[!DEFINITION] Definition: Negative Infinity as a Left-Sided Limit
>>
>>We say that $f$ **approaches negative infinity as** $x$ **approaches** $c\in D$ **from the left** if for every $A \in \mathbb{R}$ there is a $\delta \gt 0$ such that for all $x \in D$ with $x \lt c$
>>
>>$$
>>|x-c| \lt \delta \implies f(x) \lt A
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\lim_{x\to c^-} f(x) = -\infty
>>>$$
>>>
>>
>
>>[!DEFINITION] Definition: Positive Infinity as a Right-Sided Limit
>>
>>We say that $f$ **approaches positive infinity as** $x$ **approaches** $c\in D$ **from the right** if for every $A \in \mathbb{R}$ there is a $\delta \gt 0$ such that for all $x \in D$ with $x \gt c$
>>
>>$$
>>|x-c| \lt \delta \implies f(x) \gt A
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\lim_{x\to c^-} f(x) = \infty
>>>$$
>>>
>>
>
>>[!DEFINITION] Definition: Negative Infinity as a Right-Sided Limit
>>
>>We say that $f$ **approaches negative infinity as** $x$ **approaches** $c\in D$ **from the right** if for every $A \in \mathbb{R}$ there is a $\delta \gt 0$ such that for all $x \in D$ with $x \gt c$
>>
>>$$
>>|x-c| \lt \delta \implies f(x) \lt A
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\lim_{x\to c^-} f(x) = -\infty
>>>$$
>>>
>>
>

# Properties

>[!THEOREM]- Theorem: Limits through Transformations
>
>Let $f$ and $g$ be [real functions](../../Functions%20of%20the%20Real%20Numbers.md#Real%20Functions) and let $c \in \mathbb{R}$.
>
>If there exists some [deleted neighborhood](../../The%20Topology%20of%20Euclidean%20Space.md) of $c$ on which $f$ and $g$ are equal and the [limit](Limits%20of%20Real%20Functions.md#Real%20Limits) of $g$ for $x \to c$ is $L \in \mathbb{R}$, then
>
>$$
>\lim_{x \to c} f(x) = \lim_{x \to c} g(x) = L.
>$$
>
>>[!NOTE]
>>
>>This theorem is extremely powerful because it allows us to find the limit of $f$ by finding another function $g$ (usually through algebraic manipulations) whose limit is easier to compute, so long as the two functions are equal around $c$. We don't care about what happens at $x = c$ or if $f$ and $g$ are even defined at $c$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Arithmetic with Real Limits
>
>Let $f$ and $g$ be [real functions](../../Functions%20of%20the%20Real%20Numbers.md).
>
>If both [limits](Limits%20of%20Real%20Functions.md) $\displaystyle \lim_{x \to c} f(x)$ and $\displaystyle \lim_{x \to c} g(x)$ exist for $c \in \mathbb{R} \cup \{-\infty, +\infty\}$, then
>
>$$
>\begin{align*}
>&\lim_{x\to c} \alpha f(x) + \beta g(x) = \alpha \lim_{x \to c} f(x) + \beta \lim_{x \to c} g(x) \qquad \forall \alpha, \beta \in \mathbb{R} \\
>
>\\
>
>&\lim_{x \to c} \left(f(x) g(x)\right) = \left(\lim_{x\to c} f(x)\right) \cdot \left(\lim_{x\to c} g(x)\right) \\
>
>\\
>
>&\lim_{x \to c} \frac{f(x)}{g(x)} = \frac{\displaystyle \lim_{x \to c} f(x)}{\displaystyle \lim_{x \to c} g(x)}, \qquad \lim_{x \to c} g(x) \ne 0
>
>\\
>
>&\lim_{x \to c} f(x)^{g(x)} = \lim_{x \to c} f(x)^{\displaystyle \lim_{x \to c} g(x)}
>
>\end{align*}
>
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!WARNING]
>>
>>These do *not* apply to [infinite limits](Limits%20of%20Real%20Functions.md).
>>
>

>[!THEOREM]- Theorem: Arithmetic with Infinite Limits
>
>Let $f$ and $g$ [real functions](../../Functions%20of%20the%20Real%20Numbers.md#Real%20Functions).
>
>The following rules apply for the [limits](Limits%20of%20Real%20Functions.md) of $f$ and $g$ for $c \in \mathbb{R} \cup \{-\infty, +\infty\}$, no matter if they are [real](Limits%20of%20Real%20Functions.md) or [infinite](Limits%20of%20Real%20Functions.md):
>
>||$\displaystyle \lim_{x\to c} f(x) = L \lt 0$|$\displaystyle \lim_{x\to c} f(x) = L \gt 0$|
>|:--:|:--:|:--:|
>|$\displaystyle \lim_{x\to c} g(x) = -\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = -\infty$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = +\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = -\infty$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = -\infty$|
>|$\displaystyle \lim_{x\to c} g(x) = + \infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = +\infty$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = -\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = +\infty$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = +\infty$|
> 
>||$\displaystyle \lim_{x\to c} f(x) = -\infty$|$\displaystyle \lim_{x\to c} f(x) = +\infty$|
>|:--:|:--:|:--:|
>|$\displaystyle \lim_{x\to c} g(x) = -\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = -\infty$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = +\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = \, ?$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = -\infty$|
>|$\displaystyle \lim_{x\to c} g(x) = + \infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = \, ?$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = -\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = +\infty$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = +\infty$|
>
>>[!NOTE]
>>
>>A question mark ("?") indicates that we cannot compute the limit directly, but we can try to transform the expression via algebraic manipulations in such a way, so as to make the limit computable.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Converting between Limits at Infinity and Limits at Zero
>
>Let $L \in \mathbb{R} \cup \{-\infty, +\infty \}$.
>
>The following rules allow us to convert between [limits at infinity](Limits%20of%20Real%20Functions.md) and [one-sided limits](Limits%20of%20Real%20Functions.md) at zero:
>
>$$
>\lim_{x \to +\infty} f(x) = L \iff \lim_{y \to 0^+} f\left(\frac{1}{y}\right) = L
>$$
>
>$$
>\lim_{x \to -\infty} f(x) = L \iff \lim_{y \to 0^-} f\left(\frac{1}{y}\right) = L
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Converting between Infinite Limits and Zero Limits
>
>Let $c \in \mathbb{R}$.
>
>The following rules allow us to convert between [infinite limits](Limits%20of%20Real%20Functions.md#Infinite%20Limits) and [zero limits](Limits%20of%20Real%20Functions.md):
>- If $\lim_{x \to c} f(x) = + \infty$ or $\lim_{x \to c} f(x) = - \infty$, then $\lim_{x \to c} \frac{1}{f(x)} = 0$, i.e.
>
>$$
>\lim_{x \to c} f(x) = \pm \infty \implies \lim_{x \to c} \frac{1}{f(x)} = 0.
>$$
>
>- If $\lim_{x \to c} f(x) = 0$ and there exists some [neighborhood](../../The%20Topology%20of%20Euclidean%20Space.md) $\mathcal{N}$ of $c$ on which $f(x) \gt 0$, then $\lim_{x \to c} \frac{1}{f(x)} = + \infty$, i.e.
>
>$$
>\lim_{x \to c} f(x) = 0 \text{ and } f(x) \gt 0 \text{ for all } x \in \mathcal{N} \implies \lim_{x \to c} \frac{1}{f(x)} = + \infty.
>$$
>
>- If $\lim_{x \to c} f(x) = 0$ and [neighborhood](../../The%20Topology%20of%20Euclidean%20Space.md) $\mathcal{N}$ of $c$ on which $f(x) \lt 0$, then $\lim_{x \to c} \frac{1}{f(x)} = - \infty$, i.e.
>
>$$
>\lim_{x \to c} f(x) = 0 \text{ and } f(x) \lt 0 \text{ for all } x \in \mathcal{N} \implies \lim_{x \to c} \frac{1}{f(x)} = - \infty.
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Limits of Compositions
>
>Let the $L \in \mathbb{R}$ be the [limit](Limits%20of%20Real%20Functions.md) of $g$ for some $c \in \mathbb{R}$, i.e. $\lim_{x \to c} g(x) = L$.
>
>If $f$ is [continuous](../Continuity.md) at $L$, then
>
>$$
>\lim_{x \to c} f(g(x)) = f\left(\lim_{x \to c} g(x) \right) = f(L).
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: The Squeeze Theorem for Functions
>
>Let $f,g,h: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../../Functions%20of%20the%20Real%20Numbers.md).
>
>If the [limit](Limits%20of%20Real%20Functions.md) of $f$ and $g$ as $x$ approaches $c \in \mathbb{R} \cup \{-\infty, +\infty\}$ is $L \in \mathbb{R}$ and $f(x) \le h(x) \le g(x)$ for all $x\in \mathcal{D}$, then $h$ also approaches $L$ for $x \to c$.
>
>$$
>\lim_{c\to x} f(x) = \lim_{c \to x} h(x) = \lim_{x \to c} g(x) = L.
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Limits Inequality
>
>Let $f$ and $g$ be [real functions](../../Functions%20of%20the%20Real%20Numbers.md#Real%20Functions) and let $c \in \mathbb{R}$.
>
>If there exists some [neighborhood](../../The%20Topology%20of%20Euclidean%20Space.md) of $c$ on which $g(x) \le f(x)$ and the [limits](Limits%20of%20Real%20Functions.md#Real%20Limits) of $f$ and $g$ for $x \to c$ exist, then
>
>$$
>\lim_{x \to c} g(x) \le \lim_{x \to c} f(x)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: L'Hôpital's rule
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem
>
>Let $g$ be a [real function](../../Functions%20of%20the%20Real%20Numbers.md#Real%20Function) whose [limit](Limits%20of%20Real%20Functions.md#Real%20Limits) for some $c \in \mathbb{R}$ is zero, i.e. $\lim_{x \to c} g(x) = 0$, and let $f$ be some other [real function](../../Functions%20of%20the%20Real%20Numbers.md#Real%20Function).
>
>If there exists some [neighborhood](../../The%20Topology%20of%20Euclidean%20Space.md) of $c$ on which $f$ is [bounded](../Bounds%20of%20Real%20Functions.md), then
>
>$$
>\lim_{x \to c} [g(x) f(x)] = 0.
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Important Limits

>[!THEOREM]- Theorem: Important Trigonometric Limits
>
>Following are some [limits](Limits%20of%20Real%20Functions.md) involving the [real trigonometric functions](../Real%20Trigonometric%20Functions/Real%20Trigonometric%20Functions.md):
>
>
>$$
>\lim_{x \to 0} \frac{\sin x}{x} = \lim_{x \to 0} \frac{x}{\sin x} = 1
>$$
>
>$$
>\lim_{x \to 0} \frac{1 - \cos x}{x} = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Important Exponential Limits
>
>Following are some [limits](Limits%20of%20Real%20Functions.md) involving the [real exponential function](../The%20Real%20Exponential%20Function.md):
>
>$$
>\lim_{x \to -\infty} \left(1 + \frac{1}{x}\right)^x = \lim_{x \to +\infty} \left(1 + \frac{1}{x}\right)^x = \mathrm{e}
>$$
>
>$$
>\lim_{x \to 0} (1 + x)^{\frac{1}{x}} = \mathrm{e}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
