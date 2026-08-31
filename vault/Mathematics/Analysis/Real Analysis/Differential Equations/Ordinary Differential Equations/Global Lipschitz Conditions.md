---
tags:
    - real-analysis
    - analysis
    - mathematics
---

# Global Lipschitz Conditions

>[!DEFINITION] Definition: Global Lipschitz Condition
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $S \subseteq \mathcal{D}_f$.
>
>We say that $f$ **satisfies a global Lipschitz condition on** $S$ **with respect to the** $i_1, \dotsc, i_m$**-th variables** if there exists some $L \in \mathbb{R}_{\ge 0}$ such that for all $\boldsymbol{x}, \boldsymbol{y} \in S$ with $x_k = y_k$ for all indices $k \notin \{i_1, \dotsc, i_m\}$, we have:
>
>$$|f(\boldsymbol{x}) - f(\boldsymbol{y})| \le L \max_{j \in \{i_1, \dotsc, i_m\}}|x_j - y_j|$$
>
>>[!EXAMPLE]- Example: $f(t, y) = t + 2y$
>>
>>Consider the following [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md):
>>
>>$$f: \mathbb{R}^2 \to \mathbb{R} \qquad f(t, y) = t + 2y$$
>>
>>It satisfies a [global Lipschitz condition](./Lipschitz%20Conditions.md)on $\mathbb{R}^2$ with $L = 2$:
>>
>>$$|f(t, y_1) - f(t, y_2)| = |t + 2y_1 - t - 2y_2| = 2|y_1 - y_2|$$
>>
>