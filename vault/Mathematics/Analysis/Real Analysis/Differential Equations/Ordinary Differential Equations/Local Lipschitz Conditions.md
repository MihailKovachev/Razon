---
tags:
    - real-analysis
    - analysis
    - mathematics
---

# Local Lipschitz Conditions

>[!DEFINITION] Definition: Local Lipschitz Condition
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $S \subseteq \mathcal{D}_f$.
>
>We say that $f$ **satisfies a local Lipschitz condition on** $S$ **with respect to the** $i_1, \dotsc, i_m$**-th variables** if each $\boldsymbol{p} \in S$ has some [neighborhood](../../../../Topology/Topological%20Spaces/Neighborhoods.md) $N$ of $\boldsymbol{p}$ and some $L \in \mathbb{R}_{\ge 0}$ such that for all $\boldsymbol{x}, \boldsymbol{y} \in N \cap S$ with $x_k = y_k$ for all indices $k \notin \{i_1, \dotsc, i_m\}$, we have:
>
>$$|f(\boldsymbol{x}) - f(\boldsymbol{y})| \le L \max_{j \in \{i_1, \dotsc, i_m\}}|x_j - y_j|$$
>
>>[!EXAMPLE]- Example: $f(t, y) = 2t + y^2$
>>
>>Consider the following [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md):
>>
>>$$f: \mathbb{R}^2 \to \mathbb{R} \qquad f(t, y) = 2t + y^2$$
>>
>>It satisfies a [local Lipschitz condition](./Lipschitz%20Conditions.md) on $\mathbb{R}^2$ because for each $(t, y) \in \mathbb{R}^2$, if we choose some $R \gt 0$, then for each $(t, y_1)$ and $(t, y_2)$ with $|y_1| \lt R$ and $|y_2| \lt R$, we get
>>
>>$$\begin{aligned}|f(t, y_1) - f(t, y_2)| & = |2t + y_1^2 - 2t - y_2^2| \\ & = |y_1^2 - y_2^2| \\ & = |y_1 - y_2|\cdot|y_1 + y_2| \\ & \le |y_1 - y_2|(|y_1| + |y_2|) \\ & \le 2R |y_1 - y_2| \le L |y_1 - y_2|\end{aligned}$$
>>
>>with $L = 2R$. 
>>
>
>>[!EXAMPLE]- Example: $f(t, y) = \sqrt{|y|}$
>>
>>Consider the following [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md):
>>
>>$$f: \mathbb{R}^2 \to \mathbb{R} \qquad f(t, y) = \sqrt{|y|}$$
>>
>>It cannot satisfy [local Lipschitz condition](./Lipschitz%20Conditions.md)  around any [neighborhood](../../../../Topology/Topological%20Spaces/Neighborhoods.md) of $(t, y)$ whenever $y = 0$. Specifically:
>>
>>$$|f(t, y_1) - f(t, y_2)| = |\sqrt{y_1} - \sqrt{y_2}| = \frac{|y_1 - y_2|}{\sqrt{y_1} + \sqrt{y_2}}$$
>>
>>For $y_1, y_2 \to 0$, this approaches $\infty$ and so no such $L$ can exist.
>>
>

>[!THEOREM] Theorem: Local Lipschitz Conditions in 2D
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}$ be a [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f(t,x)$ and let $S \subseteq \mathcal{D}$.
>
>Then $f$ satisfies a [local Lipschitz condition](./Local%20Lipschitz%20Conditions.md) on $S$ with respect to $x$ if and only if for each $\boldsymbol{p} \in S$ there is a [neighborhood](../../../../Topology/Topological%20Spaces/Neighborhoods.md) $N_\boldsymbol{p}$ and some $L_{\boldsymbol{p}} \in \mathbb{R}_{\ge 0}$ such that
>
>$$|f(t, x_1) - f(t, x_2)| \le L_{\boldsymbol{p}} |x_1 - x_2|$$
>
>for all $(t, x_1), (t,x_2) \in N_{\boldsymbol{p}} \cap \mathcal{D}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuous Partial Differentiability $\implies$ Local Lipschitz Condition
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $S \subseteq \mathcal{D}_f$ be [locally convex](TODO).
>
>If $f$ is [continuously partially differentiable](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $S$ w.r.t. the $i_1, \dotsc, i_m$-th variables, then $f$ satisfies a [local Lipschitz condition](./Local%20Lipschitz%20Conditions.md) on $S$ w.r.t. the $i_1, \dotsc, i_m$-th variables.
>
>>[!PROOF]-
>>
>>TODO
>>
>