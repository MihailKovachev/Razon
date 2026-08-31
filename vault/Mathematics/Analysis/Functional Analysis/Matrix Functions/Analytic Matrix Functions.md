---
tags:
    - functional-mathematical-analysis
    - mathematical-analysis
    - linear-algebra
    - mathematics
---

# Analytic Matrix Functions

>[!DEFINITION] Definition: Analytic Matrix Function
>
>Let $F$ be a [complete](TODO) [valued field](TODO) and let $f: \mathcal{D}_f \subseteq F^{n \times n} \to F^{n \times n}$ be a [matrix function](./Matrix%20Functions.md).
>
>We say that $f$ is **analytic** on $S \subseteq \mathcal{D}_f$ if there exists a [matrix power series](./Matrix%20Power%20Series.md) $\sum_{k \in \mathcal{I}} a_k(\boldsymbol{X} - c\boldsymbol{I}_n)^k$ which is [convergent](./Matrix%20Power%20Series.md#Convergence) on $S$ and is equal to $f$:
>
>$$f(\boldsymbol{X}) = \sum_{k \in \mathcal{I}} a_k(\boldsymbol{X} - c\boldsymbol{I}_n)^k \qquad \forall \boldsymbol{X} \in S$$
>