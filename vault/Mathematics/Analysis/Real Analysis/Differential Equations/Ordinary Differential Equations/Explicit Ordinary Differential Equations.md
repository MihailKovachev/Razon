---
tags:
    - algebra
    - real-analysis
    - analysis
    - mathematics
---

# Explicit Ordinary Differential Equations

>[!DEFINITION] Definition: Explicit Ordinary Differential Equation
>
>An $n$[-th order ordinary differential equation](./Real%20Ordinary%20Differential%20Equations.md) $F: \mathcal{D}_F \subseteq \mathbb{R}^{n+2} \to \mathbb{R}$ is **explicit** if there exists a [function](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathcal{D}_f \subseteq \mathbb{R}^{n+1} \to \mathbb{R}$ such that
>
>$$F(x, y, y', y'', \dotsc, y^{(n)}) = y^{(n)} - f(x, y, y', \dotsc, y^{(n-1)})$$
>
>for all $(x, y, y', y'', \dotsc, y^{(n)}) \in \mathcal{D}_F$.
>

>[!THEOREM] Theorem: Explicit ODE to System of ODEs
>
>Let $F: \mathcal{D}_F \subseteq \mathbb{R}^{n+2} \to \mathbb{R}$ be an [explicit ordinary differential equation](./Explicit%20Ordinary%20Differential%20Equations.md) of [order](./Real%20Ordinary%20Differential%20Equations.md) $n$:
>
>$$F(x, y, y', y'', \dotsc, y^{(n)}) = y^{(n)} - f(x, y, y', \dotsc, y^{(n-1)})$$
>
>Let $\boldsymbol{F}: \mathcal{D}_{\boldsymbol{F}} \subseteq \mathbb{R} \times \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}^n$ be the [system](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) defined as follows:
>
>$$\boldsymbol{F}(x, \boldsymbol{u}, \boldsymbol{u}') = \boldsymbol{u}' - \begin{bmatrix}u_2 \\ \vdots \\ u_{n} \\ f(x, u_1, \dotsc, u_n)\end{bmatrix}$$
>
>
>
>>[!PROOF]-
>>
>>TODO
>>
>