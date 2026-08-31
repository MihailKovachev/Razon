---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Antidifferentiability (Real Parametric Curves)

>[!DEFINITION] Definition: Antidifferentiability (Real Parametric Curves)
>
>A [real parametric curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $f: \mathcal{D}_{f} \subseteq \mathbb{R} \to \mathbb{R}^n$ is **antidifferentiable** on a [subset](../../../../Set%20Theory/Subsets.md) $S \subseteq \mathcal{D}_{f}$ if there exists a [real parametric curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $F: \mathcal{D}_{F} \subseteq \mathbb{R} \to \mathbb{R}^n$ whose [derivative](./Differentiability%20(Real%20Parametric%20Curves).md) on $S$ is $f$:
>
>$$F'(t) = f(t) \qquad \forall t \in S$$
>
>Any such $F$ is known as an **antiderivative** of $f$ on $S$.
>

>[!THEOREM] Theorem: Component-Wise Antidifferentiability
>
>Let $f: \mathcal{D}_{f} \subseteq \mathbb{R} \to \mathbb{R}^n$ and $F: \mathcal{D}_{F} \subseteq \mathbb{R} \to \mathbb{R}^n$ be [real parametric curves](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) with [component functions](../../Real%20Vector-Valued%20Functions.md) $f_1, \dotsc, f_n$ and $F_1, \dotsc, F_n$, respectively, and let $S \subseteq \mathcal{D}_f$.
>
>Then $F$ is an [antiderivative](./Antidifferentiability%20(Real%20Parametric%20Curves).md) of $f$ on $S$ if and only if $F_1, \dotsc, F_n$ are [antiderivatives](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) of $f_1, \dotsc, f_n$ on $S$, respectively:
>
>$$F'(t) = f(t) \qquad \forall t \in S \iff F_i'(t) = f_i(t) \qquad \forall t \in S, \forall i \in \{1, 2, \dotsc, n\}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antiderivatives on Intervals
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [real parametric curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md), let $I \subseteq \mathcal{D}_f$ be an [interval](../../Euclidean%20Space/Euclidean%20Space.md) and let $F: \mathcal{D}_F \subseteq \mathbb{R} \to \mathbb{R}^n$ be an [antiderivative](./Antidifferentiability%20(Real%20Parametric%20Curves).md) of $f$ on $I$.
>
>A [real parametric curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $G: \mathcal{D}_G \subseteq \mathbb{R} \to \mathbb{R}^n$ is also an [antiderivative](./Antidifferentiability%20(Real%20Parametric%20Curves).md) of $f$ on $I$ if and only if there exists some [vector](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $\boldsymbol{C} \in \mathbb{R}^n$ such that
>
>$$F(t) = G(t) + \boldsymbol{C}$$
>
>for all $t \in I$.
>
>>[!PROOF]-
>>
>>TODO
>>
>