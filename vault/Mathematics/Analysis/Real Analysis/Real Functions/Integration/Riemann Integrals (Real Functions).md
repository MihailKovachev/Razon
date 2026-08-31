---
tags:
    - real-analysis
    - analysis
    - mathematics
---

# Riemann Integrals (Real Functions)

>[!DEFINITION] Definition: partition
>
>A **partition** of a [compact interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $[a,b]$ is a [set](../../../../Set%20Theory/Sets.md)
>
>$$P = \{x_0, x_1, \dotsc, x_n\}$$
>
>with $a = x_0 \lt x_1 \lt \cdots \lt x_n = b$.
>

>[!DEFINITION] Definition: Darboux Sums
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Functions.md) which is [bounded](../Boundedness%20of%20Real%20Functions.md) on some [compact interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $[a,b] \subseteq \mathcal{D}$ and let $P = \{x_0, x_1, \dotsc, x_n\}$ be a [partition](#Riemann%20Integral) of $[a,b]$.
>
>The **lower Darboux sum** of $f$ with respect to $P$ is defined using the [infima](../../../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md) of $f$, on each [interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $[x_{i-1}; x_i]$:
>
>$$L_{f, P} \overset{\text{def}}{=} \sum_{i=1}^n (x_i - x_{i-1}) \inf_{x \in [x_{i-1}; x_i]} f(x)$$
>
>The **upper Darboux sum** of $f$ with respect to $P$ is defined using the [suprema](../../../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md) of $f$, on each [interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $[x_{i-1}; x_i]$:
>
>$$U_{f, P} \overset{\text{def}}{=} \sum_{i=1}^n (x_i - x_{i-1}) \sup_{x \in [x_{i-1}; x_i]} f(x)$$
>

>[!DEFINITION] Definition: Darboux Integrals
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Functions.md) which is [bounded](../Boundedness%20of%20Real%20Functions.md) on a [compact interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $[a,b] \subseteq \mathcal{D}$.
>
>The **lower Darboux integral** of $f$ on $[a,b]$ is the [supremum](../../../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md) of all its [lower Darboux sums](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$:
>
>$$L_f \overset{\text{def}}{=} \sup \{L_{f, P} \mid P \text{ is a partition of } [a,b]\}$$
>
>The **upper Darboux integral** on $[a,b]$ of $f$ is the [infimum](../../../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md) of all its [upper Darboux sums](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$:
>
>$$U_f \overset{\text{def}}{=} \inf \{U_{f, P} \mid P \text{ is a partition of } [a,b]\}$$
>

>[!DEFINITION] Definition: Riemann Integral
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Functions.md) which is [bounded](../Boundedness%20of%20Real%20Functions.md) on a [compact interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $[a,b] \subseteq \mathcal{D}$.
>
>We say that $f$ is **Riemann-integrable** on $[a,b]$ if its [lower Darboux integral](#Riemann%20Integrals%20of%20Real%20Functions) and [upper Darboux integral](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$ are equal. This common value is the **Riemann integral** of $f$ on $[a,b]$.
>
>>[!NOTATION]
>>
>>The [Riemann integral](#Riemann%20Integrals%20of%20Real%20Functions) of $f$ on $[a,b]$ is denoted by
>>
>>$$\int_a^b f(x) \mathop{\mathrm{d}x},$$
>>
>>where $x$ is just a label.
>>
>>We additionally use the following notation to simplify the wording of some theorems:
>>
>>$$\int_b^a f(x) \mathop{\mathrm{d}x} = -\int_a^b f(x) \mathop{\mathrm{d}x}$$
>>
>>$$\int_c^c f(x) \mathop{\mathrm{d}x} = 0 \qquad \forall c \in [a,b]$$
>>
>

>[!DEFINITION] Definition: Local Riemann Integrability
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Functions.md).
>
>We say that $f$ is **locally Riemann-integrable** on an arbitrary [interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $I \subseteq \mathcal{D}$ if it is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on every [compact](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) [interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) contained in $I$.
>

>[!THEOREM] Theorem: Linearity of the Riemann Integral
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../../Real-Valued%20Functions.md).
>
>If $f$ and $g$ are [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on a [compact interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $[a,b] \subseteq \mathcal{D}_f \cap \mathcal{D}_g$, then so is $\lambda f + \mu g$ for all $\lambda,\mu \in \mathbb{R}$ with
>
>$$\int_a^b \lambda f(x) + \mu g(x) \mathop{\mathrm{d}x} = \lambda \int_a^b f(x) \mathop{\mathrm{d}x} + \mu \int_a^b g(x) \mathop{\mathrm{d}x}.$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Domain Additivity for Riemann Integrals
>
>Let $[a, b] \subset \mathbb{R}$ be a [compact interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) and let $c \in (a,b)$.
>
>A [real function](../Real%20Functions.md) $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ (where $\mathcal{D} \supset [a,b]$) is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$ if and only if it is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,c]$ and $[c, b]$. Moreover:
>
>$$\int_a^b f(x) \mathop{\mathrm{d}x} = \int_a^c f(x) \mathop{\mathrm{d}x} + \int_c^b f(x) \mathop{\mathrm{d}x}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Riemann Integral under Alterations
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../../Real-Valued%20Functions.md), let $[a,b] \subseteq \mathcal{D}_f \cap \mathcal{D}_g$ be a [compact interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) and $X = \{x \in [a, b] \mid f(x) \ne g(x)\}$.
>
>If $f$ is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$ and $X$ is [finite](../../../../Set%20Theory/Cardinality.md), then $g$ is also [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$ with
>
>$$\int_a^b f(x) \mathop{\mathrm{d}x} = \int_a^b g(x) \mathop{\mathrm{d}x}.$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Inequality $\implies$ Riemann Integral Inequality
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../../Real-Valued%20Functions.md) which are [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on a [compact interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $[a,b] \subseteq \mathcal{D}_f \cap \mathcal{D}_g$.
>
>If $f(x) \le g(x)$ for all $x \in [a,b]$, then
>
>$$\int_a^b f(x) \mathop{\mathrm{d}x} \le \int_a^b g(x) \mathop{\mathrm{d}x}.$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] The Mean Value Theorem for Riemann Integrals
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../../Real-Valued%20Functions.md#Real%20Functions) and let $[a,b] \subseteq \mathcal{D}_f \cap \mathcal{D}_g$ be a [compact interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line).
>
>If $f$ is [continuous](../Continuity%20(Real%20Functions).md) on $[a,b]$ and $g$ is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$ and does not change sign on $[a,b]$, then the [product](../../Real-Valued%20Functions.md#Real%20Functions) $fg$ is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$ and there exists some $\xi \in [a,b]$ such that
>
>$$\int_a^b f(x) g(x) \,\mathrm{d}x = f(\xi)\int_a^b g(x) \,\mathrm{d}x$$
>
>>[!TIP] Tip: $g(x) = 1$
>>
>>In the case of $g(x) = 1$ for all $x$, we get
>>
>>$$\int_a^b f = f(\xi)(b - a).$$
>>
>
>>[!PROOF]-
>>
>>Since $f$ is [continuous](../Continuity%20(Real%20Functions).md) on $[a,b]$, the [extreme value theorem](../Continuity%20(Real%20Functions).md) tells us that $f$ attains a minimum $m$ and a maximum $M$ on $[a,b]$:
>>
>>$$m \le f(x) \le M \qquad \forall x \in [a,b]$$
>>
>>Since $g$ does not change sign on $[a,b]$, there are two cases which we need to consider:
>>
>>    - (I) $g(x) \ge 0$ for all $x \in [a,b]$;
>>    - (II) $g(x) \le 0$ for all $x \in [a,b]$.
>>
>>**Case (I):**
>>
>>Multiplying the inequality for $f$ by $g$, we obtain the following:
>>
>>$$mg(x) \le f(x)g(x) \le Mg(x) \qquad \forall x \in [a,b]$$
>>
>>Since $f$ is [continuous](../Continuity%20(Real%20Functions).md) on $[a,b]$ and $g$ is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$, we know that $fg$ is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$. Combining this with the above inequality, we get:
>>
>>$$\int_a^b mg(x)\,\mathrm{d}x \le \int_a^b f(x)g(x) \,\mathrm{d}x \le \int_a^b Mg(x) \,\mathrm{d}x$$
>>
>>$$m\int_a^b g(x)\,\mathrm{d}x \le \int_a^b f(x)g(x) \,\mathrm{d}x \le M\int_a^b g(x) \,\mathrm{d}x$$
>>
>>If $\int_a^b g(x)\,\mathrm{d}x = 0$, we have $0 \le \int_a^b f(x)g(x)\,\mathrm{d}x \le 0$ and so $\int_a^b f(x)g(x) \,\mathrm{d}x = 0$. Therefore, $\int_a^b f(x)g(x)\,\mathrm{d}x = f(\xi) \cdot \int_a^b g(x)\,\mathrm{d}x$ for any $\xi \in [a,b]$, since $0 \cdot f(\xi) = 0$.
>>
>>If $\int_a^b g(x)\,\mathrm{d}x \gt 0$, we can divide the inequality by it:
>>
>>$$m \le \frac{\int_a^b f(x)g(x)\,\mathrm{d}x}{\int_a^b g(x)\,\mathrm{d}x} \le M$$
>>
>>Since $f$ is [continuous](../Continuity%20(Real%20Functions).md) on $[a,b]$, the [intermediate value theorem](../Continuity%20(Real%20Functions).md) tells us that $f$ attains every value between its minimum $m$ and maximum $M$, i.e. there exists some $\xi \in [a,b]$ such that
>>
>>$$f(\xi) = \frac{\int_a^b f(x)g(x)\,\mathrm{d}x}{\int_a^b g(x)\,\mathrm{d}x}$$
>>
>>Multiplying by $\int_a^b g(x)\,\mathrm{d}x$, we obtain:
>>
>>$$\int_a^b f(x) g(x) \,\mathrm{d}x = f(\xi)\int_a^b g(x) \,\mathrm{d}x$$
>>
>>**Case (II):**
>>
>>Multiplying the inequality for $f$ by $g$, we obtain the following:
>>
>>$$mg(x) \ge f(x)g(x) \ge Mg(x) \qquad \forall x \in [a,b]$$
>>
>>Since $f$ is [continuous](../Continuity%20(Real%20Functions).md) on $[a,b]$ and $g$ is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$, we know that $fg$ is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$. Combining this with the above inequality, we get:
>>
>>$$\int_a^b mg(x)\,\mathrm{d}x \ge \int_a^b f(x)g(x) \,\mathrm{d}x \ge \int_a^b Mg(x) \,\mathrm{d}x$$
>>
>>$$m\int_a^b g(x)\,\mathrm{d}x \ge \int_a^b f(x)g(x) \,\mathrm{d}x \ge M\int_a^b g(x) \,\mathrm{d}x$$
>>
>>If $\int_a^b g(x)\,\mathrm{d}x = 0$, we have $0 \ge \int_a^b f(x)g(x)\,\mathrm{d}x \ge 0$ and so $\int_a^b f(x)g(x) \,\mathrm{d}x = 0$. Therefore, $\int_a^b f(x)g(x) \,\mathrm{d}x = f(\xi) \cdot \int_a^b g(x)\,\mathrm{d}x$ for any $\xi \in [a,b]$, since $0 \cdot f(\xi) = 0$.
>>
>>If $\int_a^b g(x)\,\mathrm{d}x \lt 0$, we can divide the inequality by it:
>>
>>$$m \le \frac{\int_a^b f(x)g(x)\,\mathrm{d}x}{\int_a^b g(x)\,\mathrm{d}x} \le M$$
>>
>>Since $f$ is [continuous](../Continuity%20(Real%20Functions).md) on $[a,b]$, the [intermediate value theorem](../Continuity%20(Real%20Functions).md) tells us that $f$ attains every value between its minimum $m$ and maximum $M$, i.e. there exists some $\xi \in [a,b]$ such that
>>
>>$$f(\xi) = \frac{\int_a^b f(x)g(x)\,\mathrm{d}x}{\int_a^b g(x)\,\mathrm{d}x}$$
>>
>>Multiplying by $\int_a^b g(x)\,\mathrm{d}x$, we obtain:
>>
>>$$\int_a^b f(x) g(x) \,\mathrm{d}x = f(\xi)\int_a^b g(x) \,\mathrm{d}x$$
>>
>

>[!THEOREM] The Fundamental Theorem of Calculus (Part I)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Functions.md) .
>
>If $f$ is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on a [compact interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $[a,b] \subseteq \mathcal{D}$, then the [function](../../Real-Valued%20Functions.md) $F: [a,b] \to \mathbb{R}$ defined as
>
>$$F(x) \overset{\text{def}}{=} \int_a^x f(t) \mathop{\mathrm{d}t}$$
>
>is [continuous](../Continuity%20(Real%20Functions).md). Moreover, if $f$ is [continuous](../Continuity%20(Real%20Functions).md) at some $c \in (a,b)$, then $F$ is an [antiderivative](../Antidifferentiability%20(Real%20Functions).md) of $f$ at $c$, i.e. $F'(c) = f(c)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] The Fundamental Theorem of Calculus (Part II)
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $F: \mathcal{D}_F \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../../Real-Valued%20Functions.md#Real%20Functions).
>
>If $f$ is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on a [compact interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $[a,b] \subseteq \mathcal{D}_f \cap \mathcal{D}_F$, $F$ is [continuous](../Continuity%20(Real%20Functions).md) on $[a,b]$ and is an [antiderivative](../Antidifferentiability%20(Real%20Functions).md) of $f$ on $(a,b)$, then
>
>$$\int_a^b f(x) \mathop{\mathrm{d}x} = F(b) - F(a).$$
>
>>[!NOTATION]
>>
>>The expression $F(b) - F(a)$ is usually shortened to just $F(x)\big|_a^b$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Riemann Integration by Parts
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../../Real-Valued%20Functions.md) and let $[a,b] \subseteq \mathcal{D}_f \cap \mathcal{D}_g$ be a [compact interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line).
>
>If $f$ and $g$ are [continuous](../Continuity%20(Real%20Functions).md) on $[a,b]$, [differentiable](../Differentiability%20(Real%20Functions).md) on $(a,b)$ and if $f'$ and $g'$ can be extended to be [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$, then 
>
>$$\int_a^b f(x) g'(x) \mathop{\mathrm{d}x} = f(b)g(b) - f(a)g(a) - \int_a^b f'(x)g(x) \mathop{\mathrm{d}x}.$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: $\int_0^{\pi} x \sin x \mathop{\mathrm{d}x}$
>>
>>We want to find the following [Riemann-integral](#Riemann%20Integrals%20of%20Real%20Functions):
>>
>>$$\int_0^{\pi} x \sin x \mathop{\mathrm{d}x}$$
>>
>>We have
>>
>>$$\int_0^{\pi} x \sin x\mathop{\mathrm{d}x} = \int_0^{\pi} f(x) g'(x)$$
>>
>>with $f(x) = x$, $f'(x) = 1$, $g'(x) = \sin x$ and $g(x) = - \cos x$.
>>
>>Therefore:
>>
>>$$\begin{aligned}\int_{0}^{\pi}x\sin x\mathop{\mathrm{d}x} & =\int_0^\pi f(x)g'(x) \mathop{\mathrm{d}x} \\& = f(x)g(x)|_0^\pi - \int_0^\pi f'(x)g(x) \mathop{\mathrm{d}x} \\& =\left. -x\cos x \right|_0^\pi+\int_0^\pi\cos x \mathop{\mathrm{d}x} \\ & = \left.-x\cos x\right|_0^\pi+\sin x|_0^\pi \\ & =-\pi\cos\pi+\sin\pi-\sin0=\pi.\end{aligned}$$
>>
>

>[!THEOREM] Theorem: Riemann Integration by Substitution
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../../Real-Valued%20Functions.md#Real%20Functions) and let $[a,b] \subseteq \mathcal{D}_g$ be a [compact interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line).
>
>If $g$ is [continuous](../Continuity%20(Real%20Functions).md) on $[a,b]$ and is [differentiable](../Differentiability%20(Real%20Functions).md) on $(a,b)$ such that $g'$ can be extended to be [Riemann-integrable](./Riemann%20Integrals%20(Real%20Functions).md) on $[a,b]$ and if $f$ is [continuous](../Continuity%20(Real%20Functions).md) on $g([a,b])$, then the [function](../../Real-Valued%20Functions.md#Real%20Functions) $(f\circ g)g'$ is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$ with
>
>$$\int_a^b f(g(x))g'(x) \mathop{\mathrm{d}x} = \int_{g(a)}^{g(b)} f(u) \mathop{\mathrm{d}u}$$
>
>>[!EXAMPLE]- Example: $\int_а^b f(cx+r)\, \mathrm{d}x$
>>
>>We can use this theorem to find a formula for [Riemann integrals](#Riemann%20Integrals%20of%20Real%20Functions) of the following form:
>>
>>$$\int_a^b f(cx + r) \,\mathrm{d}x$$
>>
>>If we define $g: \mathbb{R} \to \mathbb{R}$ as $g(x) = cx + r$, then the above [Riemann integral](#Riemann%20Integrals%20of%20Real%20Functions) becomes:
>>
>>$$\int_a^b f(g(x)) \,\mathrm{d}x$$
>>
>>We see that $g$ is [polynomial](../Real%20Polynomial%20Functions.md) and thus fulfills all the requirements in the theorem. In particular, $g$ is [continuous](../Continuity%20(Real%20Functions).md) on $[a,b]$ and, since $f$ is [continuous](../Continuity%20(Real%20Functions).md) on $g([a,b])$, the [composition](../../../Functions/Functions.md) $f \circ g$ is [continuous](../Continuity%20(Real%20Functions).md) on $[a,b]$. This means that $f\circ g$ is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$ and we can write the following:
>>
>>$$\int_a^b f(g(x)) \,\mathrm{d}x = \frac{1}{c} \int_a^b f(g(x))\cdot c \,\mathrm{d}x$$
>>
>>We notice that $g'(x) = c$ and so we have:
>>
>>$$\int_a^b f(g(x)) \,\mathrm{d}x = \frac{1}{c} \int_a^b f(g(x))g'(x) \,\mathrm{d}x$$
>>
>>We can now apply the theorem:
>>
>>$$\int_a^b f(g(x)) \,\mathrm{d}x = \frac{1}{c} \int_{g(a)}^{g(b)} f(u) \,\mathrm{d}u$$
>>
>>$$\int_a^b f(cx + r) \,\mathrm{d}x = \frac{1}{c} \int_{ca+r}^{cb+r} f(u) \,\mathrm{d}u$$
>>
>
>>[!EXAMPLE]- Example: $\int_0^{\frac{\pi}{2}} \mathrm{e}^{\sin x} \cos {x} \,\mathrm{d}x$
>>
>>We want to determine the following [Riemann integral](#Riemann%20Integrals%20of%20Real%20Functions):
>>
>>$$\int_{0}^{\frac{\pi}{2}} \mathrm{e}^{\sin x} \cos {x} \,\mathrm{d}x$$
>>
>>We notice that 
>>
>>$$\int_{0}^{\frac{\pi}{2}} \mathrm{e}^{\sin x} \cos {x} \,\mathrm{d}x = \int_{0}^{\frac{\pi}{2}} f(g(x))g'(x) \,\mathrm{d}x$$
>>
>>with $g(x) = \sin x$, $g'(x) = \cos x$ and $f(u) = \mathrm{e}^u$. We can verify that $f$ and $g$ satisfy the requirements of the theorem. Therefore, we have:
>>
>>$$\begin{aligned}\int_{0}^{\frac{\pi}{2}} \mathrm{e}^{\sin x} \cos {x} \,\mathrm{d}x & = \int_{g(0)}^{g\left(\frac{\pi}{2}\right)} f(u)\, \mathrm{d}u \\ & = \int_{0}^{1} \mathrm{e}^u \, \mathrm{d}u \\ & = \mathrm{e}^u \vert_0^1 = \mathrm{e}^1 - \mathrm{e}^0 = \mathrm{e} -1 \end{aligned}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: King's Rule
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Functions.md).
>
>If $f(x)$ is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b] \subseteq \mathcal{D}$, then so is $f(a + b - x)$:
>
>$$\int_a^b f(x) \,\mathrm{d}x = \int_a^b f(a + b - x) \,\mathrm{d}x.$$
>
>If $\frac{f(x)}{f(x) + f(a + b - x)}$ is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b] \subseteq \mathcal{D}$, then
>
>$$\int_a^b \frac{f(x)}{f(x) + f(a + b - x)}\,\mathrm{d}x = \frac{b - a}{2}.$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Integrability of the Absolute Value
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Functions.md).
>
>If $f$ is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on a [compact interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $[a,b]$, then so is $|f|$ and
>
>$$\left|\int_a^b f(x) \mathop{\mathrm{d}x}\right| \le \int_a^b |f(x)| \mathop{\mathrm{d}x}.$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

### Improper Riemann Integrals

The notion of [Riemann integrals](#Riemann%20Integrals%20of%20Real%20Functions) can be extended to [open and semi-open intervals](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) using [limits](../Limits%20(Real%20Functions.md).

>[!DEFINITION] Definition: Improper Riemann Integrals
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Functions.md).
>
>We say that $f$ is **improperly Riemann-integrable** on:
>
>    - $[a, b) \subseteq \mathcal{D}$, where $-\infty \lt a \lt b \lt +\infty$, if $f$ is [locally Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a, b)$ and the following [limit](../Limits%20(Real%20Functions.md) exists and is finite:
>
>$$\int_a^b f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \lim_{\beta \to b^-} \int_a^\beta f(x) \mathop{\mathrm{d}x}$$
>
>    - $[a, +\infty) \subseteq \mathcal{D}$, where $-\infty \lt a \lt +\infty$, if $f$ is [locally Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a, +\infty)$ and the following [limit](../Limits%20(Real%20Functions.md) exists and is finite:
>
>$$\int_a^{+\infty} f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \lim_{\beta \to +\infty} \int_a^\beta f(x) \mathop{\mathrm{d}x}$$
>
>    - $(a, b] \subseteq \mathcal{D}$, where $-\infty \lt a \lt b \lt +\infty$, if $f$ is [locally Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $(a, b]$ and the following [limit](../Limits%20(Real%20Functions.md) exists and is finite:
>
>$$\int_a^b f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \lim_{\alpha \to a^+} \int_\alpha^b f(x) \mathop{\mathrm{d}x}$$
>
>    - $(-\infty, b] \subseteq \mathcal{D}$, where $-\infty \lt b \lt +\infty$, if $f$ is [locally Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $(-\infty, b]$ and the following [limit](../Limits%20(Real%20Functions.md) exists and is finite:
>
>$$\int_{-\infty}^b f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \lim_{\alpha \to -\infty} \int_\alpha^b f(x) \mathop{\mathrm{d}x}$$
>
>    - $(a, b) \subseteq \mathcal{D}$, where $-\infty \lt a \lt b \lt +\infty$, if $f$ is [improperly Riemann-integrable](#Improper%20Riemann%20Integrals) on $(a, c]$ and $[c, b)$ for any $c \in (a, b)$:
>
>$$\int_a^b f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \int_a^c f(x) \mathop{\mathrm{d}x} + \int_c^b f(x) \mathop{\mathrm{d}x}$$
>
>    - $(-\infty, b) \subseteq \mathcal{D}$, where $-\infty \lt b \lt +\infty$, if $f$ is [improperly Riemann-integrable](#Improper%20Riemann%20Integrals) on $(-\infty, c]$ and $[c, b)$ for any $c \in (-\infty, b)$:
>
>$$\int_{-\infty}^b f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \int_{-\infty}^c f(x) \mathop{\mathrm{d}x} + \int_c^b f(x) \mathop{\mathrm{d}x}$$
>
>    - $(a, +\infty) \subseteq \mathcal{D}$, where $-\infty \lt a \lt +\infty$, if $f$ is [improperly Riemann-integrable](#Improper%20Riemann%20Integrals) on $(a, c]$ and $[c, +\infty)$ for any $c \in (a, +\infty)$:
>
>$$\int_a^{+\infty} f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \int_a^c f(x) \mathop{\mathrm{d}x} + \int_c^{+\infty} f(x) \mathop{\mathrm{d}x}$$
>
>    - $(-\infty, +\infty) \subseteq \mathcal{D}$, if $f$ is [improperly Riemann-integrable](#Improper%20Riemann%20Integrals) on $(-\infty, c]$ and $[c, +\infty)$ for any $c \in (-\infty, +\infty)$:
>
>$$\int_{-\infty}^{+\infty} f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \int_{-\infty}^c f(x) \mathop{\mathrm{d}x} + \int_c^{+\infty} f(x) \mathop{\mathrm{d}x}$$
>
>>[!NOTATION]
>>
>>Given an arbitrary [interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $I$, the expression
>>
>>$$\int_I f(x)\,\mathrm{d}x$$
>>
>>denotes either the [Riemann integral](#Riemann%20Integrals%20of%20Real%20Functions) of $f$ on $I$ (whenever $I$ is a [compact](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line)  [interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line)) or $f$'s corresponding [improper Riemann integral](#Improper%20Riemann%20Integrals).
>>
>
>>[!EXAMPLE]- Example: $\int_0^1 \frac{1}{x^r} \,\mathrm{d}x$
>>
>>We want to determine
>>
>>$$\int_0^1 \frac{1}{x^r} \,\mathrm{d}x.$$
>>
>>For $r = 1$, we have:
>>
>>$$\begin{aligned}\int_0^1 \frac{1}{x} \,\mathrm{d}x & = \lim_{\alpha \to 0^{+}} \int_{\alpha}^1 \frac{1}{x} \,\mathrm{d}x \\ & = \lim_{\alpha \to 0^{+}} \left. \ln x \right\vert_\alpha^1 \\ & = \lim_{\alpha \to 0^{+}} (\ln 1 - \ln \alpha) = +\infty \end{aligned}$$
>>
>>However, $\frac{1}{x}$ is *not* [improperly Riemann-integrable](#Improper%20Riemann%20Integrals) on $(0, 1]$ because this value is not finite.
>>
>>For $r \ne 1$, we have:
>>
>>$$\begin{aligned}\int_0^1 \frac{1}{x^r} \,\mathrm{d}x & = \lim_{\alpha \to 0^{+}} \int_{\alpha}^1 \frac{1}{x^r} \,\mathrm{d}x \\ & = \lim_{\alpha \to 0^{+}} \left. \frac{1}{1-r}x^{1-r}\right\vert_\alpha^1 \\ & = \lim_{\alpha \to 0^{+}} \frac{1-\alpha^{1-r}}{1-r} = \begin{cases}\frac{1}{1-r}, & \text{if} & r \lt 1 \\ +\infty, & \text{if} & r \gt 1\end{cases} \end{aligned}$$
>>
>>In sum:
>>
>>$$\int_0^1 \frac{1}{x^{\alpha}} \,\mathrm{d}x = \begin{cases}\frac{1}{1-r}, & \text{if} & r \lt 1 \\ +\infty, & \text{if} & r \ge 1\end{cases}$$
>>
>
>>[!EXAMPLE]- Example: $\int_1^{\infty} \frac{1}{x^r} \,\mathrm{d}x$
>>
>>We want to determine
>>
>>$$\int_1^{\infty} \frac{1}{x^r} \,\mathrm{d}x.$$
>>
>>For $r = 1$, we have:
>>
>>$$\begin{aligned}\int_1^{\infty} \frac{1}{x} \,\mathrm{d}x & = \lim_{\beta \to +\infty} \int_1^{\beta} \frac{1}{x} \,\mathrm{d}x \\ & = \lim_{\beta \to +\infty} \left. \ln x \right\vert_1^{\beta} \\ & = \lim_{\beta \to +\infty} (\ln \beta - \ln 1) = +\infty \end{aligned}$$
>>
>>For $r \ne 1$, we have:
>>
>>$$\begin{aligned}\int_1^{\infty} \frac{1}{x^r} \,\mathrm{d}x & = \lim_{\beta \to +\infty} \int_1^{\infty} \frac{1}{x^r} \,\mathrm{d}x \\ & = \lim_{\beta \to +\infty} \left. \frac{1}{1-r}x^{1-r}\right\vert_1^{\beta} \\ & = \lim_{\beta \to +\infty} \frac{\beta^{1-r}-1}{1-r} = \begin{cases}\frac{1}{r-1}, & \text{if} & r \gt 1 \\ +\infty, & \text{if} & r \lt 1\end{cases} \end{aligned}$$
>>
>>In sum:
>>
>>$$\int_1^{\infty} \frac{1}{x^r} \,\mathrm{d}x = \begin{cases}+\infty, & \text{if} & r \le 1 \\ \frac{1}{r-1}, & \text{if} & r \gt 1\end{cases}$$
>>
>
>>[!EXAMPLE]- Example: $\int_0^{\infty} \mathrm{e}^{-3x}\,\mathrm{d}x$
>>
>>$$\begin{aligned}\int_0^{\infty} \mathrm{e}^{-3x}\,\mathrm{d}x & = \lim_{\beta \to \infty} \int_0^{\beta} \mathrm{e}^{-3x}\,\mathrm{d}x \\ & = \lim_{\beta \to \infty} \left(\left.-\frac{1}{3}\mathrm{e}^{-3x}\right\vert_0^{\beta}\right) \\ & = \lim_{\beta \to \infty} \left(-\frac{1}{3}(\mathrm{e}^{-3\beta}-1)\right) \\ & = \frac{1}{3}\end{aligned}$$
>>
>>Therefore, $\mathrm{e}^{-3x}$ is [improperly Riemann-integrable](#Improper%20Riemann%20Integrals) on $[0, +\infty)$.
>>
>

>[!THEOREM] Theorem: Constant Independence of Improper Integrals
>
>TODO
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Improper Integral $\rightarrow$ Proper Integral
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Functions.md).
>
>If $f$ is [improperly Riemann-integrable](#Improper%20Riemann%20Integrals) on $[a,b)$ and $\tilde{f}$ is an extension of $f$ which is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$, then
>
>$$\int_a^b f(x) \,\mathrm{d}x = \int_a^b \tilde{f}(x) \,\mathrm{d}x.$$
>
>If $f$ is [improperly Riemann-integrable](#Improper%20Riemann%20Integrals) on $(a,b]$ and $\tilde{f}$ is an extension of $f$ which is [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[a,b]$, then
>
>$$\int_a^b f(x) \,\mathrm{d}x = \int_a^b \tilde{f}(x) \,\mathrm{d}x.$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Comparison Test for Improper Integrals
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Functions.md) and let $I$ be any [interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line).
>
>If $f$ is [locally Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $I$ and there exists some [real function](../Real%20Functions.md) $g$ which is [improperly Riemann-integrable](#Improper%20Riemann%20Integrals) on $I$ with
>
>$$|f(x)| \le g(x)$$
>
>for all $x \in I$, then $f$ is also [improperly Riemann-integrable](#Improper%20Riemann%20Integrals) on $I$ with
>
>$$\left\vert\int_{I} f(x) \,\mathrm{d}x\right\vert \le \int_I g(x) \,\mathrm{d}x.$$
>
>>[!EXAMPLE]- Example: $\int_1^{\infty} \mathrm{e}^{-x}x^3 \,\mathrm{d}x$
>>
>>From the [limit](../Limits%20(Real%20Functions.md)
>>
>>$$\lim_{x \to \infty} \frac{x^5}{\mathrm{e}^{-x}} = \lim_{x \to \infty} \frac{x^5}{\mathrm{e}^x} = 0$$
>>
>>we know that $\mathrm{e}^{-x}x^5$ is [bounded](../Boundedness%20of%20Real%20Functions.md) on $[1; +\infty)$, i.e. there exists some $B \gt 0$ such that
>>
>>$$\mathrm{e}^{-x}x^5 \le B$$
>>
>>for all $x \ge 1$. From this inequality, we get
>>
>>$$\mathrm{e}^{-x}x^3 \le Bx^{-2}$$
>>
>>for all $x \ge 1$. Since the [integral](#Improper%20Riemann%20Integrals)
>>
>>$$\int_1^{\infty} x^{-2} \,\mathrm{d}x$$
>>
>>converges, we know that
>>
>>$$\int_1^{\infty} Cx^{-2} \,\mathrm{d}x$$
>>
>>also converges and so
>>
>>$$\int_1^{\infty} \mathrm{e}^{-x}x^3 \,\mathrm{d}x$$
>>
>>must converge as well.
>>
>
>>[!EXAMPLE]- Example: $\int_0^{\infty} \frac{\sin x}{x}\,\mathrm{d}x$
>>
>>We want to determine if the [integral](#Improper%20Riemann%20Integrals)
>>
>>$$\int_0^{\infty} \frac{\sin x}{x}\,\mathrm{d}x$$
>>
>>converges. We split it into two:
>>
>>$$\int_0^{\infty} \frac{\sin x}{x}\,\mathrm{d}x = \int_0^1 \frac{\sin x}{x}\,\mathrm{d}x + \int_1^{\infty}\frac{\sin x}{x}\,\mathrm{d}x$$
>>
>>The [function](../Real%20Functions.md) $f: \mathbb{R} \to \mathbb{R}$ defined as
>>
>>$$f(x) = \begin{cases} 1 & \text{if} x = 0 \\ \frac{\sin x}{x} & \text{if} x \ne 0\end{cases}$$
>>
>>is an [extension](../../../Functions/Functions.md) of $\frac{\sin x}{x}$. It is [continuous](../Continuity%20(Real%20Functions).md), since $\lim_{x \to 0}\frac{\sin x}{x} = 1$, and so it is also [Riemann-integrable](#Riemann%20Integrals%20of%20Real%20Functions) on $[0,1]$. We thus have:
>>
>>$$\int_0^1 \frac{\sin x}{x} \,\mathrm{d}x = \int_0^1 f(x) \,\mathrm{d}x \in \mathbb{R}$$
>>
>>For $\int_1^{\infty}\frac{\sin x}{x}\,\mathrm{d}x$, we have:
>>
>>$$\int_1^{\infty}\frac{\sin x}{x}\,\mathrm{d}x = \lim_{\beta \to +\infty} \int_1^{\beta} \frac{\sin x}{x} \,\mathrm{d}x$$
>>
>>We use [integration by parts](#Riemann%20Integrals%20of%20Real%20Functions):
>>
>>$$\begin{aligned}\int_1^{\infty}\frac{\sin x}{x}\,\mathrm{d}x & = \lim_{\beta \to +\infty} \int_1^{\beta} \frac{\sin x}{x} \,\mathrm{d}x \\ & = \lim_{\beta \to +\infty} \left(\left.-\frac{\cos x}{x} \right\vert_1^{\beta} - \int_{1}^{\beta} \frac{\cos x}{x^2} \,\mathrm{d}x\right)\end{aligned}$$
>>
>>For the first term:
>>
>>$$\begin{aligned}\lim_{\beta \to +\infty} \left.-\frac{\cos x}{x} \right\vert_1^{\beta} = \lim_{\beta \to +\infty} \left( -\frac{\cos \beta}{\beta} + \frac{\cos 1}{1}\right) = \cos 1\end{aligned}$$
>>
>>For the second, term $\lim_{\beta \to +\infty} -\int_{1}^{\beta} \frac{\cos x}{x^2} \,\mathrm{d}x$ is just the [improper integral](#Improper%20Riemann%20Integrals) $\int_1^{\infty} -\frac{\cos x}{x}\, \mathrm{d}x$. Since
>>
>>$$\left\vert \frac{\cos x}{x} \right\vert \le x^{-2}$$
>>
>>for all $x \in [1, \infty)$ and since $\int_1^{\infty} x^{-2}\, \mathrm{d}x$ converges, we know that
>>
>>$$\int_1^{\infty} -\frac{\cos x}{x}\, \mathrm{d}x$$
>>
>>must also converge.
>>
>>Therefore, the [limit](../Limits%20(Real%20Functions.md)
>>
>>$$\int_1^{\infty} \frac{\sin x}{x}\,\mathrm{d}x = \lim_{\beta \to +\infty} \int_1^{\beta} \frac{\sin x}{x} \,\mathrm{d}x = \lim_{\beta \to +\infty} \left.-\frac{\cos x}{x} \right\vert_1^{\beta} + \lim_{\beta \to +\infty} -\int_{1}^{\beta} \frac{\cos x}{x^2} \,\mathrm{d}x$$
>>
>>must also exist.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Integral Test
>
>Let $f: [a, \infty) \subseteq \mathbb{R} \to \mathbb{R}$ be a non-negative, [decreasing](../Monotonicity%20of%20Real%20Functions.md) [real function](../Real%20Functions.md).
>
>The [improper integral](#Improper%20Riemann%20Integrals)
>
>$$\int_a^{\infty} f(x) \,\mathrm{d}x$$
>
>[converges](../Limits%20(Real%20Functions.md) if and only if the [series](../../Real%20Series.md)
>
>$$\sum_{n=\lceil a \rceil}^{\infty} f(n)$$
>
>[converges](../../Real%20Series.md#Convergence).
>
>>[!PROOF]-
>>
>>TODO
>>
>