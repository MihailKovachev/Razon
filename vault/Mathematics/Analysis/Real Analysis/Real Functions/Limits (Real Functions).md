---
tags:
  - real-mathematical-analysis
  - mathematical-analysis
  - mathematics
---

# Limits (Real Functions)

## Real One-Sided Limits

>[!DEFINITION] Definition: Left-Sided Limit
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md), let $c \in \mathbb{R}$ be an [accumulation point](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $\mathcal{D} \cap (-\infty; c)$ and let $L \in \mathbb{R}$.
>
>We say that $L$ is the **left-sided limit of** $f$ **at** $c$ if for every $\varepsilon \gt 0$ there is some $\delta \gt 0$ such that 
>
>$$|x-c| \lt \delta \implies |f(x)-L| \lt \varepsilon$$
>
>for all $x \in \mathcal{D}$ with $x \lt c$.
>
>>[!NOTATION]
>>
>>$$\lim_{x\to c^-} f(x) = L \qquad \lim_{\begin{matrix} x \to c \\ x \lt c\end{matrix}} f(x) = L$$
>>
>
>>[!THEOREM] Theorem: Left-Sided Limit via Sequences
>>
>>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md), let $c \in \mathbb{R}$ be an [accumulation point](../Euclidean%20Space/Euclidean%20Space.md) of $\mathcal{D} \cap (-\infty; c)$ and let $L \in \mathbb{R}$.
>>
>>The following statements are equivalent:
>>
>>- The [left-sided limit](#Real%20One-Sided%20Limits) of $f$ at $c$ is $L$:
>>
>>$$\lim_{x \to c^{-}} f(x) = L$$
>>
>>- For each [infinite](../../Functional%20Analysis/Sequences/Sequences.md) [sequence](../Real%20Sequences.md) $(x_n)_{n \in \mathcal{D}'}$ with $x_n \lt c$ for all $n \in \mathcal{D}'$ which [converges](../Real%20Sequences.md) to $c$, the [sequence](../../Functional%20Analysis/Sequences/Sequences.md) $(f(x_n))_{n \in \mathcal{D}'}$ [converges](../Real%20Sequences.md) to $L$:
>>
>>$$\lim_{n \to \infty} x_n = c \implies \lim_{n \to \infty} f(x_n) = L$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

>[!DEFINITION] Definition: Right-Sided Limit
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md), let $c \in \mathbb{R}$ be an [accumulation point](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $\mathcal{D} \cap (c; +\infty)$ and let $L \in \mathbb{R}$.
>
>We say that $L$ is the **right-sided limit of** $f$ **at** $c$ if for every $\varepsilon \gt 0$ there is some $\delta \gt 0$ such that 
>
>$$|x-c| \lt \delta \implies |f(x)-L| \lt \varepsilon$$
>
>for all $x \in \mathcal{D}$ with $x \gt c$.
>
>>[!NOTATION]
>>
>>$$\lim_{x\to c^+} f(x) = L \qquad \lim_{\begin{matrix} x \to c \\ x \gt c\end{matrix}} f(x) = L$$
>>
>
>>[!THEOREM] Theorem: Right-Sided Limit via Sequences
>>
>>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md), let $c \in \mathbb{R}$ be an [accumulation point](../Euclidean%20Space/Euclidean%20Space.md) of $\mathcal{D} \cap (c; +\infty)$ and let $L \in \mathbb{R}$.
>>
>>The following statements are equivalent:
>>- The [right-sided limit](#Real%20One-Sided%20Limits) of $f$ at $c$ is $L$:
>>
>>$$\lim_{x \to c^{+}} f(x) = L$$
>>
>>- For each [infinite](../../Functional%20Analysis/Sequences/Sequences.md) [sequence](../Real%20Sequences.md) $(x_n)_{n \in \mathcal{D}'}$ with $x_n \gt c$ for all $n \in \mathcal{D}'$ which [converges](../Real%20Sequences.md) to $c$, the [sequence](../../Functional%20Analysis/Sequences/Sequences.md) $(f(x_n))_{n \in \mathcal{D}'}$ [converges](../Real%20Sequences.md) to $L$:
>>
>>$$\lim_{n \to \infty} x_n = c \implies \lim_{n \to \infty} f(x_n) = L$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

## Real Limits

>[!DEFINITION] Definition: Limit of a Function (Cauchy)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $p \in \mathbb{R}$ be an [accumulation point](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $\mathcal{D}$.
>
>We say that $L \in \mathbb{R}$ is the **limit** of $f$ at $p$ if for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that for all $x \in \mathcal{D}$, we have the following:
>
>$$0 \lt |x-p| \lt \delta \implies |f(x)-L| \lt \varepsilon$$
>
>>[!NOTATION]
>>
>>$$\lim_{x\to p} f(x) = L$$
>>
>

>[!DEFINITION] Definition: Limit at Positive Infinity
>
>Let $\mathcal{D}$ be [unbounded above](../../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md#Boundedness) and let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>We say that $L$ is the **limit of** $f$ **at positive infinity** if for each $\varepsilon \gt 0$ there is some $A \in \mathbb{R}$ such that
>
>$$|f(x) - L| \lt \varepsilon$$
>
>for all $x \in \mathcal{D}$ with $x \ge A$.
>
>>[!NOTATION]
>>
>>$$\lim_{x\to \infty} f(x) = L$$
>>
>
>>[!EXAMPLE]- Example: $\lim_{x \to +\infty} \frac{1}{x}$
>>
>>The [limit](#Real%20Limits) of $\frac{1}{x}$ at $+\infty$ is $0$:
>>
>>$$\lim_{x \to +\infty} \frac{1}{x} = 0$$
>>
>

>[!DEFINITION] Definition: Limit at Negative Infinity
>
>Let $\mathcal{D}$ be [unbounded below](../../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md#Boundedness) and let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>We say that $L$ is the **limit of** $f$ **at negative infinity** if for each $\varepsilon \gt 0$ there is some $A \in \mathbb{R}$ such that
>
>$$|f(x) - L| \lt \varepsilon$$
>
>for all $x \in \mathcal{D}$ with $x \le A$.
>
>>[!NOTATION]
>>
>>$$\lim_{x\to -\infty} f(x) = L$$
>>
>

>[!DEFINITION] Definition: Limit Existence
>
>If $\lim_{x \to c} f(x) = L \in \mathbb{R}$ for $c \in \mathbb{R} \cup \{-\infty, +\infty\}$, then we say that the **limit of** $f$ **at** $c$ **exists**.
>

>[!THEOREM] Theorem: Real Limit and One-Sided Real Limits
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $c \in \mathbb{R}$ be an [accumulation point](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of both $\mathcal{D} \cap (-\infty;c)$ and $\mathcal{D} \cap (c; +\infty)$.
>
>The [two-sided limit](#Real%20Limits) of $f$ at $c$ exists if and only if both [one-sided limits](#Real%20One-Sided%20Limits) of $f$ at $c$ exist and are equal.
>
>$$\lim_{x \to c} f(x) = L \in \mathbb{R} \iff \lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = L$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: The Floor Function
>>
>>The **floor function** is the [function](./Real%20Functions.md) $\lfloor \cdot\rfloor: \mathbb{R} \to \mathbb{R}$ which for each $x$ gives the largest [integer](TODO) which is less than or equal to $x$. For example,
>>
>>$$\lfloor 0.5 \rfloor = 0 \qquad \lfloor 1.2 \rfloor = 1 \qquad \lfloor -3.3 \rfloor = -4 \qquad \lfloor 5 \rfloor = 5$$
>>
>>For each [integer](TODO) $m \in \mathbb{Z}$ we have
>>
>>$$\lim_{x \to m^{-}} \lfloor x \rfloor = m - 1 \qquad \lim_{x \to m^{+}} \lfloor x \rfloor = m.$$
>>
>>This means that $\lim_{x \to m} \lfloor x \rfloor$ does not exist when $m$ is an [integer](TODO).
>>
>

>[!THEOREM] Theorem: Limits through Transformations
>
>Let $f$ and $g$ be [real functions](./Real%20Functions.md) and let $c \in \mathbb{R}$.
>
>If there exists some [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $c$ on which $f$ and $g$ are equal and the [limit](#Real%20Limits) of $g$ at $c$ is $L \in \mathbb{R}$, then
>
>$$\lim_{x \to c} f(x) = \lim_{x \to c} g(x) = L.$$
>
>>[!NOTE]
>>
>>This theorem is extremely powerful because it allows us to find the limit of $f$ by finding another function $g$ (usually through algebraic manipulations) whose limit is easier to compute, so long as the two functions are equal around $c$. We don't care about what happens at $x = c$ or if $f$ and $g$ are even defined at $c$.
>>
>
>>[!PROOF]-
>>
>>Let $\varepsilon \gt 0$ be any positive real number.
>>
>>Since there is some [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $c$ on which $f$ and $g$ are equal, we know that there exists some $\delta_1 \gt 0$ such that
>>
>>$$0 \lt |x - c| \lt \delta_1 \implies f(x) = g(x).$$
>>
>>Since $\lim_{x \to c} g(x) = L$, we know that for our choice of $\varepsilon$ there exists some $\delta_2 \gt 0$ such that
>>
>>$$0 \lt |x - c| \lt \delta_2 \implies |g(x) - L| \lt \varepsilon.$$
>>
>>Set $\delta = \min\{\delta_1, \delta_2\}$.
>>
>>Since $\delta \le \delta_1$, we have
>>
>>$$0 \lt |x - c| \lt \delta \implies 0 \lt |x - c| \lt \delta$$
>>
>>and, since $0 \lt |x - c| \lt \delta_1 \implies f(x) = g(x)$, we have proved that 
>>
>>$$0 \lt |x - c| \lt \delta \implies f(x) = g(x).$$
>>
>>Similarly, since $\delta \le \delta_2$, we have
>>
>>$$0 \lt |x - c| \lt \delta \implies 0 \lt |x - c| \lt \delta$$
>>
>>and, since $0 \lt |x - c| \lt \delta_2 \implies |g(x) - L| \lt \varepsilon$, we have proved that
>>
>>$$0 \lt |x - c| \lt \delta \implies |g(x) - L| \lt \varepsilon.$$
>>
>>Now we combine these facts. Consider $|f(x) - L|$. For all $x$ with $0 \lt |x - c| \lt \delta$, we showed that $f(x) = g(x)$. Therefore,
>>
>>$$0 \lt |x - c| \lt \delta \implies |f(x) - L| = |g(x) - L|$$
>>
>>Moreover, we showed that $|g(x) - L| \lt \varepsilon$ for all $x$ with $0 \lt |x - c| \lt \delta$. Therefore,
>>
>>$$0 \lt |x - c| \lt \delta \implies |f(x) - L| \lt \varepsilon.$$
>>
>
>>[!EXAMPLE]-
>>
>>Consider the [function](./Real%20Functions.md) $f: \mathbb{R} \setminus \{1\} \to \mathbb{R}$ defined in the following way:
>>
>>$$f(x) = \frac{x^3 - 1}{x-1}$$
>>
>>Consider also the [function](./Real%20Functions.md) $g: \mathbb{R} \to \mathbb{R}$ defined in the following way:
>>
>>$$g(x) = x^2 + x + 1$$
>>
>>We want to determine the [limits](./Limits%20(Real%20Functions.md) of $f$ and $g$ at $c = 1$. We see, for example, that $f$ and $g$ are equal on the [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line)  $(0; 1)\cup(1;2)$ of $c$, since
>>
>>$$f(x) = \frac{x^3 - 1}{x - 1} = \frac{(x-1)(x^2+x+1)}{x-1} = x^2+x+1$$
>>
>>for all $x \ne 1$. We thus know that the  [limits](./Limits%20(Real%20Functions.md) of $f$ and $g$ at $c$, if they exist, must be equal:
>>
>>$$\lim_{x \to c} f(x) = \lim_{x \to c} g(x)$$
>>
>>Now, $g$ is a [real polynomial function](./Real%20Polynomial%20Functions.md) and so we know that
>>
>>$$\lim_{x \to c} g(x) = g(c) = 1^2 + 1 + 1 = 3.$$
>>
>>This automatically means that
>>
>>$$\lim_{x \to c} f(x) = 3.$$
>>
>
>>[!EXAMPLE]-
>>
>>Consider the [function](./Real%20Functions.md) $f: \mathbb{R} \setminus \{0\} \to \mathbb{R}$ defined in the following way:
>>
>>$$f(x) = \frac{\sqrt{x + 1} - 1}{x}$$
>>
>>We want to determine its [limit](./Limits%20(Real%20Functions.md) at $0$.
>>
>>For $x \ne 0$, we have
>>
>>$$\begin{aligned} f(x) & = \frac{\sqrt{x + 1} - 1}{x} \\ &= \frac{(\sqrt{x + 1} - 1)(\sqrt{x + 1} + 1)}{x(\sqrt{x + 1} + 1)} \\ &= \frac{1 + x - 1}{x(\sqrt{x + 1} + 1)} \\ &= \frac{x}{x(\sqrt{x + 1} + 1)} \\ &= \frac{1}{\sqrt{x+1}+1} \qquad \forall x \in \mathbb{R} \setminus \{0\}\end{aligned}$$
>>
>>Since $\mathbb{R} \setminus \{0\}$ is a [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $0$, we know that
>>
>>$$\lim_{x \to 0} \frac{\sqrt{x + 1} - 1}{x} = \lim_{x \to 0} \frac{1}{\sqrt{x+1}+1}$$
>>
>>The [function](./Real%20Functions.md) $\frac{1}{\sqrt{x+1}+1}$ is [continuous](../../Continuity/Continuity.md) at $0$, i.e.
>>
>>$$\lim_{x \to 0} \frac{1}{\sqrt{x+1}+1} = \frac{1}{\sqrt{1 + 1} + 1} = \frac{1}{2}.$$
>>
>>Therefore,
>>
>>$$\lim_{x \to 0} f(x) = \frac{1}{2}.$$
>>
>

>[!THEOREM] Theorem: Arithmetic with Real Limits
>
>Let $f$ and $g$ be [real functions](./Real%20Functions.md) and let $c \in \mathbb{R} \cup \{-\infty, +\infty\}$.
>
>If the [limits](./Limits%20(Real%20Functions.md) of $f$ and $g$ exist at $c$, then
>
>$$\begin{aligned} &\lim_{x\to c} \left(\alpha f(x) + \beta g(x)\right) = \alpha \lim_{x \to c} f(x) + \beta \lim_{x \to c} g(x) \qquad \forall \alpha, \beta \in \mathbb{R} \\ \\ &\lim_{x \to c} \left(f(x) g(x)\right) = \left(\lim_{x\to c} f(x)\right) \cdot \left(\lim_{x\to c} g(x)\right) \\ \\ &\lim_{x \to c} \frac{f(x)}{g(x)} = \frac{\displaystyle \lim_{x \to c} f(x)}{\displaystyle \lim_{x \to c} g(x)}, \qquad \text{if} \lim_{x \to c} g(x) \ne 0 \\ \\ & \lim_{x \to c} f(x)^{g(x)} = \lim_{x \to c} f(x)^{\displaystyle \lim_{x \to c} g(x)}, \qquad \text{if} \lim_{x \to c} f(x) \gt 0\end{aligned}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!WARNING]
>>
>>These do *not* apply to [infinite limits](#Infinite%20Limits).
>>
>

>[!THEOREM] Theorem: The Squeeze Theorem for Functions
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$, $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ and $h: \mathcal{D}_h \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](./Real%20Functions.md) and let $c \in \mathbb{R}$.
>
>If there exists some [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $c$ on which $f(x) \le h(x) \le g(x)$ and the [limits](#Real%20Limits) of $f$ and $g$ exist at $c$ and are equal to the same $L \in \mathbb{R}$, then
>
>$$\lim_{x\to c} f(x) = \lim_{x \to c} h(x) = \lim_{x \to c} g(x) = L.$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: $\lim_{x \to 0} \frac{\sin x}{x} = 1$
>>
>>We want to find the [limit](./Limits%20(Real%20Functions.md) at $0$ of the [function](./Real%20Functions.md) $f: \mathbb{R} \setminus \{0\}\to \mathbb{R}$ defined in the following way:
>>
>>$$f(x) = \frac{\sin x}{x}$$
>>
>>We examine the [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $\mathcal{N} = \left(-\frac{\pi}{2}; 0\right)\cup\left(0; +\frac{\pi}{2}\right)$.
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: $\lim_{x \to 0} \frac{\mathrm{e}^x - 1}{x} = 1$
>>
>>We want to find the [limit](./Limits%20(Real%20Functions.md) at $0$ of the [function](./Real%20Functions.md) $f: \mathbb{R} \setminus \{0\}\to \mathbb{R}$ defined in the following way:
>>
>>$$f(x) = \frac{\mathrm{e}^x - 1}{x}$$
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: $\lim_{x \to 0} x \sin \frac{1}{x}$
>>
>>We want to find the [limit](./Limits%20(Real%20Functions.md) at $0$of the [function](./Real%20Functions.md) $f: \mathbb{R} \setminus \{0\}\to \mathbb{R}$ defined in the following way:
>>
>>$$f(x) = x \sin \frac{1}{x}$$
>>
>>Since the [image](../../Functions/Functions.md) of [sin](./Real%20Trigonometric%20Functions/Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function) is $[-1; +1]$, we have
>>
>>$$-|x| \le x \sin \frac{1}{x} \le +|x| \qquad \forall x \in \mathbb{R} \setminus \{0\}.$$
>>
>>We know that $\mathbb{R} \setminus \{0\}$ is a [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $0$ and, since $\lim_{x \to 0} -|x| = \lim_{x \to 0} +|x| = 0$, we have
>>
>>$$\lim_{x \to 0} x\sin\frac{1}{x} = 0.$$
>>
>

>[!THEOREM] Theorem: Limits Inequality
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](./Real%20Functions.md).
>
>If the [limits](#Real%20Limits) of $f$ and $g$ exist at $c \in \mathbb{R}$ and there exists some [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $c$ on which $g(x) \le f(x)$ and, then
>
>$$\lim_{x \to c} g(x) \le \lim_{x \to c} f(x).$$
>
>If the [limits](#Real%20Limits) of $f$ and $g$ exist at $- \infty$ and there exists some $A \in \mathbb{R}$ such that $g(x) \le f(x)$ for all $x \lt A$, then
>
>$$\lim_{x \to -\infty} g(x) \le \lim_{x \to -\infty} f(x).$$
>
>If the [limits](#Real%20Limits) of $f$ and $g$ exist at $+ \infty$ and there exists some $B \in \mathbb{R}$ such that $g(x) \le f(x)$ for all $x \gt B$, then
>
>$$\lim_{x \to +\infty} g(x) \le \lim_{x \to +\infty} f(x).$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Infinite One-Sided Limits

>[!DEFINITION] Definition: Negative Infinity as a Left-Sided Limit
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $c \in \mathbb{R}$ be an [accumulation point](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $\mathcal{D} \cap (-\infty; c)$.
>
>We say that $-\infty$ is the **left-sided limit of** $f$ **at** $c$ if for each $A \in \mathbb{R}$ there is a $\delta \gt 0$ such that for all $x \in \mathcal{D}$ with $x \lt c$ we have:
>
>$$0 \lt |x - c| \lt \delta \implies f(x) \lt A$$
>
>>[!NOTATION]
>>
>>$$\lim_{x\to c^-} f(x) = -\infty$$
>>
>

>[!DEFINITION] Definition: Positive Infinity as a Left-Sided Limit
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $c \in \mathbb{R}$ be an [accumulation point](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $\mathcal{D} \cap (-\infty; c)$.
>
>We say that $+\infty$ is the **left-sided limit of** $f$ **at** $c$ if for each $A \in \mathbb{R}$ there is a $\delta \gt 0$ such that for all $x \in \mathcal{D}$ with $x \lt c$ we have:
>
>$$0 \lt |x-c| \lt \delta \implies f(x) \gt A$$
>
>>[!NOTATION]
>>
>>$$\lim_{x\to c^-} f(x) = \infty$$
>>
>

>[!DEFINITION] Definition: Negative Infinity as a Right-Sided Limit
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $c \in \mathbb{R}$ be an [accumulation point](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $\mathcal{D} \cap (c;+\infty)$.
>
>We say that $-\infty$ is the **right-sided limit of** $f$ **at** $c$ if for each $A \in \mathbb{R}$ there is a $\delta \gt 0$ such that for all $x \in \mathcal{D}$ with $x \gt c$ we have:
>
>$$0 \lt |x - c| \lt \delta \implies f(x) \lt A$$
>
>>[!NOTATION]
>>
>>$$\lim_{x\to c^+} f(x) = -\infty$$
>>
>

>[!DEFINITION] Definition: Positive Infinity as a Right-Sided Limit
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $c \in \mathbb{R}$ be an [accumulation point](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $\mathcal{D} \cap (c;+\infty)$.
>
>We say that $+\infty$ is the **right-sided limit of** $f$ **at** $c$ if for each $A \in \mathbb{R}$ there is a $\delta \gt 0$ such that for all $x \in \mathcal{D}$ with $x \gt c$ we have:
>
>$$0 \lt |x-c| \lt \delta \implies f(x) \gt A$$
>
>>[!NOTATION]
>>
>>$$\lim_{x\to c^+} f(x) = \infty$$
>>
>

## Infinite Limits

>[!DEFINITION] Definition: Negative Infinity as Two-Sided Limit
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $c \in \mathbb{R}$ be an [accumulation point](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $\mathcal{D}$.
>
>We say that $f$ **approaches** $-\infty$ **as** $x$ **approaches** $c \in \mathbb{R}$ or that $-\infty$ **is the limit of** $f$ **at** $c$ if for each $A \in \mathbb{R}$ there is some $\delta \gt 0$ such that 
>
>$$0 \lt |x-c| \lt \delta \implies f(x) \lt A$$
>
>for all $x \in \mathcal{D}$.
>
>>[!NOTATION]
>>
>>$$\lim_{x\to c} f(x) = -\infty$$
>>
>

>[!DEFINITION] Definition: Negative Infinity as Limit at Negative Infinity
>
>Let $\mathcal{D}$ be [unbounded below](../../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md#Boundedness) and let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>We say that $f$ **approaches** $-\infty$ **as** $x$ **approaches** $-\infty$ or that $-\infty$ **is the limit of** $f$ **at** $-\infty$ if for each $A \in \mathbb{R}$ there is some $B \in \mathbb{R}$ such that $f(x) \lt A$ for all $x \in \mathcal{D}$ with $x \lt B$.
>
>>[!NOTATION]
>>
>>$$\lim_{x \to -\infty} f(x) = -\infty$$
>>
>

>[!DEFINITION] Definition: Negative Infinity as Limit at Positive Infinity
>
>Let $\mathcal{D}$ be [unbounded above](../../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md#Boundedness) and let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>We say that $f$ **approaches** $-\infty$ **as** $x$ **approaches** $+\infty$ or that $-\infty$ **is the limit of** $f$ **at** $+\infty$ if for each $A \in \mathbb{R}$ there is some $B \in \mathbb{R}$ such that $f(x) \lt A$ for all $x \in \mathcal{D}$ with $x \gt B$.
>
>>[!NOTATION]
>>
>>$$\lim_{x \to +\infty} f(x) = -\infty$$
>>
>

>[!DEFINITION] Definition: Positive Infinity as Two-Sided Limit
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $c \in \mathbb{R}$ be an [accumulation point](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $\mathcal{D}$.
>
>We say that $f$ **approaches** $+\infty$ **as** $x$ **approaches** $c \in \mathbb{R}$ or that $+\infty$ **is the limit of** $f$ **at** $c$ if for each $A \in \mathbb{R}$ there is some $\delta \gt 0$ such that 
>
>$$0 \lt |x-c| \lt \delta \implies f(x) \gt A$$
>
>for all $x \in \mathcal{D}$.
>
>>[!NOTATION]
>>
>>$$\lim_{x\to c} f(x) = +\infty$$
>>
>

>[!DEFINITION] Definition: Positive Infinity as Limit at Negative Infinity
>
>Let $\mathcal{D}$ be [unbounded below](../../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md#Boundedness) and let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>We say that $f$ **approaches** $+\infty$ **as** $x$ **approaches** $-\infty$ or that $+\infty$ **is the limit of** $f$ **at** $-\infty$ if for each $A \in \mathbb{R}$ there is some $B \in \mathbb{R}$ such that $f(x) \gt A$ for all $x \in \mathcal{D}$ with $x \lt B$.
>
>>[!NOTATION]
>>
>>$$\lim_{x \to -\infty} f(x) = +\infty$$
>>
>

>[!DEFINITION] Definition: Positive Infinity as Limit at Positive Infinity
>
>Let $\mathcal{D}$ be [unbounded above](../../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md#Boundedness) and let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>We say that $f$ **approaches** $+\infty$ **as** $x$ **approaches** $+\infty$ or that $+\infty$ **is the limit of** $f$ **at** $+\infty$ if for each $A \in \mathbb{R}$ there is some $B \in \mathbb{R}$ such that $f(x) \gt A$ for all $x \in \mathcal{D}$ with $x \gt B$.
>
>>[!NOTATION]
>>
>>$$\lim_{x \to +\infty} f(x) = +\infty$$
>>
>

>[!THEOREM] Theorem: Arithmetic with Infinite Limits
>
>Let $f$ and $g$ be [real functions](./Real%20Functions.md) and let $c \in \mathbb{R} \cup \{-\infty, +\infty\}$.
>
>The following rules apply for the [limits](./Limits%20(Real%20Functions.md) of $f$ and $g$ at $c$, either [real](#Real%20Limits) or [infinite](#Infinite%20Limits):
>
>||$\displaystyle \lim_{x\to c} f(x) = L \lt 0$|$\displaystyle \lim_{x\to c} f(x) = L \gt 0$|
>|:--:|:--:|:--:|
>|$\displaystyle \lim_{x\to c} g(x) = -\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = -\infty$ <br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = +\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = -\infty$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = -\infty$|
>|$\displaystyle \lim_{x\to c} g(x) = + \infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = +\infty$ <br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = -\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = +\infty$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = +\infty$|
> 
>||$\displaystyle \lim_{x\to c} f(x) = -\infty$|$\displaystyle \lim_{x\to c} f(x) = +\infty$|
>|:--:|:--:|:--:|
>|$\displaystyle \lim_{x\to c} g(x) = -\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = -\infty$ <br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = +\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = \, ?$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = -\infty$|
>|$\displaystyle \lim_{x\to c} g(x) = + \infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = \, ?$ <br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = -\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = +\infty$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = +\infty$|
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

>[!THEOREM] Theorem: Converting between Limits at Infinity and Limits at Zero
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $L \in \mathbb{R} \cup \{-\infty, +\infty \}$.
>
>The following rules allow us to convert between [limits at infinity](./Limits%20(Real%20Functions.md) and [one-sided limits](./Limits%20(Real%20Functions.md)  at zero:
>
>$$\lim_{x \to +\infty} f(x) = L \iff \lim_{y \to 0^+} f\left(\frac{1}{y}\right) = L$$
>
>$$\lim_{x \to -\infty} f(x) = L \iff \lim_{y \to 0^-} f\left(\frac{1}{y}\right) = L$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Converting between Infinite Limits and Zero Limits
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $c \in \mathbb{R}$.
>
>The following rules allow us to convert between [infinite limits](#Infinite%20Limits) and [real limits](#Real%20Limits):
>
>- If $\lim_{x \to c} f(x) = + \infty$ or $\lim_{x \to c} f(x) = - \infty$, then $\lim_{x \to c} \frac{1}{f(x)} = 0$, i.e.
>
>$$\lim_{x \to c} f(x) = \pm \infty \implies \lim_{x \to c} \frac{1}{f(x)} = 0.$$
>
>- If $\lim_{x \to c} f(x) = 0$ and there exists some [neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $\mathcal{N}$ of $c$ on which $f(x) \gt 0$, then $\lim_{x \to c} \frac{1}{f(x)} = + \infty$, i.e.
>
>$$\lim_{x \to c} f(x) = 0 \text{ and } f(x) \gt 0 \text{ for all } x \in \mathcal{N} \implies \lim_{x \to c} \frac{1}{f(x)} = + \infty.$$
>
>- If $\lim_{x \to c} f(x) = 0$ and [neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $\mathcal{N}$ of $c$ on which $f(x) \lt 0$, then $\lim_{x \to c} \frac{1}{f(x)} = - \infty$, i.e.
>
>$$\lim_{x \to c} f(x) = 0 \text{ and } f(x) \lt 0 \text{ for all } x \in \mathcal{N} \implies \lim_{x \to c} \frac{1}{f(x)} = - \infty.$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Limits of Compositions
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](./Real%20Functions.md) and let $c \in \mathbb{R}$.
>
>If the [limit](#Real%20Limits) of $g$ exists at $c$ and $f$ is [continuous](./Continuity%20(Real%20Functions).md) at $\lim_{x \to c} g(x)$, then the [limit](#Real%20Limits) of their [composition](../../Functions/Functions.md) exists and
>
>$$\lim_{x \to c} f(g(x)) = f\left(\lim_{x \to c} g(x) \right).$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: L'Hôpital's Rule (Left-Sided Limits)
>
>Let $c \in \mathbb{R}$ and let $f$ and $g$ be [real functions](./Real%20Functions.md) that are [differentiable](./Differentiability%20(Real%20Functions).md) on an open interval $(a, c)$ (where $a < c$) with $g'(x) \neq 0$ for all $x \in (a, c)$.
>
>If the [limit](#Real%20Limits) of $\lim_{x \to c^-} \frac{f'(x)}{g'(x)}$ is
>
>$$\lim_{x \to c^-} \frac{f'(x)}{g'(x)} = L \in \mathbb{R} \cup \{-\infty, +\infty\}$$
>
>and one of the following conditions holds:
>
>    - zero limit condition: $\lim_{x \to c^-} f(x) = 0$ and $\lim_{x \to c^-} g(x) = 0$;
>    - infinite limit condition: $\lim_{x \to c^-} |g(x)| = +\infty$;
>
>then the [limit](./Limits%20(Real%20Functions.md) $\lim_{x \to c^-} \frac{f(x)}{g(x)}$ is equal to the [limit](./Limits%20(Real%20Functions.md) $\lim_{x \to c^-} \frac{f'(x)}{g'(x)}$:
>
>$$\lim_{x \to c^-} \frac{f(x)}{g(x)} = \lim_{x \to c^-} \frac{f'(x)}{g'(x)} = L$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: L'Hôpital's Rule (Right-Sided Limits)
>
>Let $c \in \mathbb{R}$ and let $f$ and $g$ be [real functions](./Real%20Functions.md) that are [differentiable](./Differentiability%20(Real%20Functions).md) on an open interval $(c, b)$ (where $b > c$) with $g'(x) \neq 0$ for all $x \in (c, b)$.
>
>If the [limit](#Real%20Limits) of $\lim_{x \to c^+} \frac{f'(x)}{g'(x)}$ is
>
>$$\lim_{x \to c^+} \frac{f'(x)}{g'(x)} = L \in \mathbb{R} \cup \{-\infty, +\infty\}$$
>
>and one of the following conditions holds:
>
>    - zero limit condition: $\lim_{x \to c^+} f(x) = 0$ and $\lim_{x \to c^+} g(x) = 0$;
>    - infinite limit condition: $\lim_{x \to c^+} |g(x)| = +\infty$;
>
>then the [limit](./Limits%20(Real%20Functions.md) $\lim_{x \to c^+} \frac{f(x)}{g(x)}$ is equal to the [limit](./Limits%20(Real%20Functions.md) $\lim_{x \to c^+} \frac{f'(x)}{g'(x)}$:
>
>$$\lim_{x \to c^+} \frac{f(x)}{g(x)} = \lim_{x \to c^+} \frac{f'(x)}{g'(x)} = L$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: $\lim_{x \to 0^+} x \ln x$
>>
>>We want to determine the following [limit](./Limits%20(Real%20Functions.md):
>>
>>$$\lim_{x \to 0^+} x \ln x$$
>>
>>We first transform the expression:
>>
>>$$\lim_{x \to 0^+} x \ln x = \lim_{x \to 0^+} \frac{\ln x}{\frac{1}{x}} = \lim_{x \to 0^+} \frac{f(x)}{g(x)}$$
>>
>>We see that $\lim_{x \to 0^+} |g(x)| = \infty$, so this is a candidate for [L'Hôpital's rule](./Limits%20(Real%20Functions.md). By [differentiating](./Differentiability%20(Real%20Functions).md), we obtain the following:
>>
>>$$f'(x) = \frac{1}{x} \qquad g'(x) = -\frac{1}{x^2}$$
>>
>>We see that $g'(x) \ne 0$ for all $x \in \mathbb{R} \setminus \{0\}$. Furthermore:
>>
>>$$\lim_{x \to 0^+} \frac{f'(x)}{g'(x)} = \lim_{x \to 0^+} \frac{\frac{1}{x}}{-\frac{1}{x^2}} = \lim_{x \to 0^+} (-x) = 0 \in \mathbb{R} \cup \{-\infty, +\infty\}$$
>>
>>Therefore, we can use [L'Hôpital's rule](./Limits%20(Real%20Functions.md):
>>
>>$$\lim_{x \to 0^+} \frac{f(x)}{g(x)} = \lim_{x \to 0^+} \frac{f'(x)}{g'(x)} = 0$$
>>
>

>[!THEOREM] Theorem: L'Hôpital's Rule (Two-Sided Limits and Limits at $\pm \infty$)
>
>Let $c \in \mathbb{R} \cup \{-\infty, +\infty\}$ and let $f$ and $g$ be [real functions](./Real%20Functions.md) that are [differentiable](./Differentiability%20(Real%20Functions).md) on a [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $\mathcal{N}(c)$ with $g'(x) \neq 0$ for all $x \in \mathcal{N}(c)$.
>
>If the [limit](#Real%20Limits) of $\lim_{x \to c} \frac{f'(x)}{g'(x)}$ is
>
>$$\lim_{x \to c} \frac{f'(x)}{g'(x)} = L \in \mathbb{R} \cup \{-\infty, +\infty\}$$
>
>and one of the following conditions holds:
>
>    - zero limit condition: $\lim_{x \to c} f(x) = 0$ and $\lim_{x \to c} g(x) = 0$;
>    - infinite limit condition: $\lim_{x \to c} |g(x)| = +\infty$;
>
>then the [limit](./Limits%20(Real%20Functions.md) $\lim_{x \to c} \frac{f(x)}{g(x)}$ is equal to the [limit](./Limits%20(Real%20Functions.md) $\lim_{x \to c} \frac{f'(x)}{g'(x)}$:
>
>$$\lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)} = L$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: $\lim_{x \to 0} \frac{\mathrm{e}^x - 1}{x}$
>>
>>We want to determine the following [limit](./Limits%20(Real%20Functions.md):
>>
>>$$\lim_{x \to 0} \frac{\mathrm{e}^x - 1}{x}$$
>>
>>We see that $\lim_{x \to 0} (\mathrm{e}^{x} - 1) = \lim_{x \to 0} x = 0$, so we might be able to use [L'Hôpital's rule](./Limits%20(Real%20Functions.md) provided that the appropriate conditions are met. We see first that $(x)' = 1$ and so $(x') \ne 0$ for all $x \in \mathbb{R}$. We see that $\lim_{x \to 0} \frac{(\mathrm{e}^x - 1)'}{(x)'} \in \mathbb{R} \cup \{-\infty, +\infty\}$:
>>
>>$$\lim_{x \to 0} \frac{(\mathrm{e}^x - 1)'}{(x)'} = \lim_{x \to 0} \frac{\mathrm{e}^x}{1} = 1$$
>>
>>Therefore:
>>
>>$$\lim_{x \to 0} \frac{\mathrm{e}^x - 1}{x} = \lim_{x \to 0} \frac{(\mathrm{e}^x - 1)'}{(x)'} = 1$$
>>
>
>>[!EXAMPLE]- Example: $\lim_{x \to 0} \left(\frac{1}{\sin x} - \frac{1}{x}\right)$
>>
>>We want to determine the following [limit](./Limits%20(Real%20Functions.md):
>>
>>$$\lim_{x \to 0} \left(\frac{1}{\sin x} - \frac{1}{x}\right)$$
>>
>>We first transform the expression a bit:
>>
>>$$\frac{1}{\sin x} - \frac{1}{x} = \frac{x - \sin x}{x \sin x}$$
>>
>>Let $f(x) = x - \sin x$ and $g(x) = x \sin x$. We immediately see that $\lim_{x \to 0} f(x) = \lim_{x \to 0} g(x) = 0$, so we might be able to use [L'Hôpital's rule](./Limits%20(Real%20Functions.md). By [differentiating](./Differentiability%20(Real%20Functions).md), we obtain the following:
>>
>>$$f'(x) = 1 - \cos x \qquad g'(x) = \sin x + x \cos x$$
>>
>>We can see that $g'(x) \ne 0$ for all $x \in (-\frac{\pi}{2}; 0)\cup (0; +\frac{\pi}{2})$. 
>>
>>However, we also see that $\lim_{x \to 0} f'(x) = \lim_{x \to 0} g'(x) = 0$, so we cannot use [L'Hôpital's rule](./Limits%20(Real%20Functions.md) directly. Nevertheless, we might be able to use apply use it *for* $f'$ and $g'$ as well. By [differentiating](./Differentiability%20(Real%20Functions).md) again, we obtain the following:
>>
>>$$f''(x) = \sin x \qquad g''(x) = 2 \cos x - x \sin x$$
>>
>>We see that $g''(x) \ne 0$ for all $x \in (-\frac{\pi}{4};0)\cup (0; +\frac{\pi}{4})$. Moreover, we have:
>>
>>$$\lim_{x \to 0} \frac{f''(x)}{g''(x)} = \lim_{x \to 0}\frac{\sin x}{2 \cos x - x \sin x} = \frac{0}{2} = 0$$
>>
>>We can therefore use [L'Hôpital's rule](./Limits%20(Real%20Functions.md):
>>
>>$$\lim_{x \to 0} \frac{f'(x)}{g'(x)} = \lim_{x \to 0} \frac{f''(x)}{g''(x)} = 0$$
>>
>>$$\lim_{x \to 0} \frac{f(x)}{g(x)} = \lim_{x \to 0} \frac{f'(x)}{g'(x)} = 0$$
>>
>

>[!THEOREM] Theorem: Zero Limit via Boundedness
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](./Real%20Functions.md) and let $c \in \mathbb{R} \cup \{-\infty, +\infty\}$.
>
>If there exists a [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $c$ (an [interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of the form $(-\infty, M)$ or $(M, +\infty)$ for $c = \pm \infty$) on which $f$ is [bounded](./Boundedness%20of%20Real%20Functions.md) and the [limit](#Real%20Limits) of $g$ at $c$ is zero, then
>
>$$\lim_{x \to c} (g(x) f(x)) = 0.$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Important Trigonometric Limits
>
>Following are some [limits](./Limits%20(Real%20Functions.md) involving the [real trigonometric functions](./Real%20Trigonometric%20Functions/Real%20Trigonometric%20Functions.md):
>
>
>$$\lim_{x \to 0} \frac{\sin x}{x} = \lim_{x \to 0} \frac{x}{\sin x} = 1$$
>
>$$\lim_{x \to 0} \frac{1 - \cos x}{x} = 0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Important Exponential Limits
>
>Following are some [limits](./Limits%20(Real%20Functions.md) involving the [real exponential function](./Real%20Exponentiation.md#The%20Real%20Exponential%20Function):
>
>$$\lim_{x \to -\infty} \left(1 + \frac{1}{x}\right)^x = \lim_{x \to +\infty} \left(1 + \frac{1}{x}\right)^x = \mathrm{e}$$
>
>$$\lim_{x \to 0} (1 + x)^{\frac{1}{x}} = \mathrm{e}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Asymptotes

>[!DEFINITION] Definition: Vertical Asymptote
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>We say that $f$ has a **vertical asymptote** at $x = c \in \mathbb{R}$ if it has at least one [infinite one-sided limit](#Infinite%20One-Sided%20Limits), i.e. at least one of the following holds:
>
>- $\displaystyle \lim_{x \to c^-} f(x) = -\infty$
>- $\displaystyle \lim_{x \to c^+} f(x) = -\infty$
>- $\displaystyle \lim_{x \to c^-} f(x) = \infty$ 
>- $\displaystyle \lim_{x \to c^+} f(x) = \infty$
>
>>[!INTUITION]
>>
>>Intuitively, this definition means that the value of $f(x)$ gets closer and closer to $- \infty$ or $+ \infty$ as $x$ approaches $c$ either from the left or from the right.
>>
>

>[!DEFINITION] Definition: Horizontal Asymptote
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>We say that $f$ has a **horizontal asymptote** $y = a \in \mathbb{R}$ if the [limit](#Real%20Limits) of $f$ as $x$ approaches positive or negative infinity is $a$, i.e. if at least one of the following holds:
>
>- $\displaystyle \lim_{x \to -\infty} f(x) = a$
>- $\displaystyle \lim_{x \to \infty} f(x) = a$
>
>>[!INTUITION]
>>
>>Intuitively, this definition means that the value of $f(x)$ gets closer and closer to $a$ as $x$ approaches either positive or negative infinity.
>>
>

>[!DEFINITION] Definition: Oblique Asymptote
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>The line $y = ax + b$ is an **oblique** or **slanted asymptote** of $f$ if at least one of the following is true:
>
>- $\displaystyle \lim_{x \to -\infty} [f(x) - (ax + b)] = 0$
>- $\displaystyle \lim_{x \to \infty} [f(x) - (ax + b)] = 0$
>
>>[!INTUITION]
>>
>>Intuitively, this definition means $f(x)$ gets closer and closer to the line $y = ax + b$ as $x$ approaches either positive or negative infinity.
>>
>

>[!THEOREM] Theorem: Oblique Asymptotes
>
>Let $f$ be a [real function](./Real%20Functions.md).
>
>The line $y = ax + b$ is an [asymptote](#Asymptotes) of $f$ if and only if the [limits](#Real%20Limits)  $\lim_{x \to \pm \infty} \frac{f(x)}{x}$ and $\lim_{x \to \pm \infty} (f(x) - ax)$ exist and
>
>$$\begin{aligned} a &= \lim_{x \to \pm \infty} \frac{f(x)}{x} \\ \\ b &= \lim_{x \to \pm \infty} (f(x) - ax)\end{aligned}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>