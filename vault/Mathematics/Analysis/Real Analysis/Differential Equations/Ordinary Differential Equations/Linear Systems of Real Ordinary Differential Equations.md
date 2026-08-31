---
tags:
    - real-analysis
    - vector-analysis
    - mathematics
---

# Linear Systems of Real Ordinary Differential Equations

>[!DEFINITION] Definition: Linear System of Real Ordinary Differential Equations
>
>Let $k, m, n \in \mathbb{N}_{\ge 1}$, let $\boldsymbol{F}: \mathcal{D}_{\boldsymbol{F}} \subseteq \mathbb{R}^{1+k+k\cdot n} \to \mathbb{R}^m$ with $\mathcal{D}_{\boldsymbol{F}} \ne \varnothing$ be a [function](../../Real%20Vector%20Functions/Real%20Vector%20Functions.md) which is [dependent](TODO) on at least one of its last $k$ arguments, and let $\mathcal{D}_t \subseteq \mathbb{R}$ be the [projection](TODO) of $\mathcal{D}_{\boldsymbol{F}}$ on its first variable.
>
>The [system of ordinary differential equations](./System%20of%20Real%20Ordinary%20Differential%20Equations.md)
>
>$$ \boldsymbol{F}\left(t, \boldsymbol{x}, \boldsymbol{x}', \dotsc, \boldsymbol{x}^{(n)}\right) = \boldsymbol{0} $$
>
>is **linear** if there exist [real matrix-valued functions](TODO) $\boldsymbol{A}_0, \boldsymbol{A}_1, \dotsc, \boldsymbol{A}_n: \mathcal{D}_t \to \mathbb{R}^{m \times k}$ and a [function](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\boldsymbol{b}: \mathcal{D}_t \to \mathbb{R}^m$ such that 
>
>$$\boldsymbol{F}\left(t, \boldsymbol{x}_0, \boldsymbol{x}_1, \dotsc, \boldsymbol{x}_n\right) = \boldsymbol{A}_0(t)\boldsymbol{x}_0 + \boldsymbol{A}_1(t)\boldsymbol{x}_1 + \cdots + \boldsymbol{A}_n(t)\boldsymbol{x}_n - \boldsymbol{b}(t) $$
>
>for all $\left(t, \boldsymbol{x}_0, \boldsymbol{x}_1, \dotsc, \boldsymbol{x}_n\right) \in \mathcal{D}_{\boldsymbol{F}}$.
>
>>[!DEFINITION] Definition: Corresponding Homogeneous System
>>
>>The **corresponding homogenenous equation** of $F$ is the [system of real ordinary differential equations](./System%20of%20Real%20Ordinary%20Differential%20Equations.md)
>>
>>$$\boldsymbol{F}_{\text{h}}\left(t, \boldsymbol{x}_0, \boldsymbol{x}_1, \dotsc, \boldsymbol{x}_n\right) = 0,$$
>>
>>where $\boldsymbol{F}_{\text{h}}: \mathcal{D}_F \subseteq \mathbb{R}^{n+2} \to \mathbb{R}$ is the [function](../../Real%20Vector%20Functions/Real%20Vector%20Functions.md) defined as follows:
>>
>>$$\boldsymbol{F}_{\text{h}}\left(t, \boldsymbol{x}_0, \boldsymbol{x}_1, \dotsc, \boldsymbol{x}_n\right) \overset{\text{def}}{=} \boldsymbol{A}_0(t)\boldsymbol{x}_0 + \boldsymbol{A}_1(t)\boldsymbol{x}_1 + \cdots + \boldsymbol{A}_n(t)\boldsymbol{x}_n$$
>>
>>
>