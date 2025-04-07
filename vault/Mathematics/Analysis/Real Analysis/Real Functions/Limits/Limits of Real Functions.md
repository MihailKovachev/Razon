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
>>[!NOTATION]-
>>
>>$$
>>\lim_{x\to c^-} f(x) = L
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
>>[!NOTATION]-
>>
>>$$
>>\lim_{x\to c^+} f(x) = L
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
>>[!NOTATION]-
>>
>>$$
>>\lim_{x\to c} f(x) = L
>>$$
>
>>[!THEOREM] Theorem: Existence of the Limit
>>
>>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../../Functions%20of%20the%20Real%20Numbers.md).
>>
>>The [limit](Limit%20of%20a%20Real%20Function.md) of $f$ as $x$ approaches $c \in D$ exists if and only if both [one-sided limits](Limits%20of%20Real%20Functions.md) of $f$ at $c$ exist and are equal.
>>
>>$$\lim_{x \to c} f(x) = L \in \mathbb{R} \iff \lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = L$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>
>>[!DEFINITION] Definition: Limit at Positive Infinity
>>
>>A real number $L \in \mathbb{R}$ is called the **limit of** $f$ **as** $x$ **approaches positive infinity** if for every $\varepsilon \gt 0$ there is a $A \in \mathbb{R}$ such that
>>
>>$$
>>|f(x) - L| \lt \varepsilon \qquad \forall x \ge A
>>$$
>>
>>>[!NOTATION]-
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
>>>[!NOTATION]-
>>>
>>>$$
>>>\lim_{x\to -\infty} f(x) = L
>>>$$
>>>
>>
>
>If $f$ has a limit $L \in \mathbb{R}$, then the limit is said to exist.
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
>>>[!NOTATION]-
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
>>>>[!NOTATION]-
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
>>>[!NOTATION]-
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
>>>>[!NOTATION]-
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
>>>[!NOTATION]-
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
>>>[!NOTATION]-
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
>>>[!NOTATION]-
>>>
>>>$$
>>>\lim_{x\to c^-} f(x) = -\infty
>>>$$
>>>
>>
>
