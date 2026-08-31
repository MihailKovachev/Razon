---
tags:
    - real-analysis
    - analysis
    - mathematics
---

# Linear Ordinary Differential Equations

>[!DEFINITION] Definition: Linear Ordinary Differential Equations
>
>Let $n \in \mathbb{N}_{\ge 1}$, let $F: \mathcal{D}_F \subseteq \mathbb{R}^{n+2} \to \mathbb{R}$ with $\mathcal{D}_F \ne \varnothing$ be a [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) which is [dependent](TODO) on its last argument and let $\mathcal{D}_t \subseteq \mathbb{R}$ be the [projection](TODO) of $\mathcal{D}_F$ on its first variable.
>
>The [ordinary differential equation](./Real%20Ordinary%20Differential%20Equations.md)
>
>$$F\left(t, x, x', x'', \dotsc, x^{(n)}\right) = 0$$
>
>is **linear** if there exist [real functions](../../Real%20Functions/Real%20Functions.md) $\alpha_0, \alpha_1, \dotsc, \alpha_n, \beta: \mathcal{D}_t \to \mathbb{R}$ such that 
>
>$$F\left(t, x, x', x'', \dotsc, x^{(n)}\right) = \alpha_0(t) x + \alpha_1(t)x' + \cdots + \alpha_n(t) x^{(n)} - \beta(t)$$
>
>for all $\begin{bmatrix} t & x & x' & \cdots & x^{(n)}\end{bmatrix}^{\mathsf{T}} \in \mathcal{D}_F$.
>
>>[!DEFINITION] Definition: Corresponding Homogenenous Equation
>>
>>The **corresponding homogenenous equation** of $F$ is the [ordinary differential equation](./Real%20Ordinary%20Differential%20Equations.md)
>>
>>$$F_h\left(t, x, x', x'', \dotsc, x^{(n)}\right) = 0,$$
>>
>>where $F_h: \mathcal{D}_F \subseteq \mathbb{R}^{n+2} \to \mathbb{R}$ is the [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) defined as follows:
>>
>>$$F_{\text{h}}\left(t, x, x', x'', \dotsc, x^{(n)}\right) \overset{\text{def}}{=} \alpha_0(t) x + \alpha_1(t)x' + \cdots + \alpha_n(t) x^{(n)}$$
>>
>

>[!THEOREM] Theorem: Existence and Uniqueness
>
>Let $I \subseteq \mathbb{R}$ be some [open interval](../../Euclidean%20Space/Euclidean%20Space.md) and let
> 
>$$a_0(x) y + a_1(x)y' + \cdots + a_{n-1}(x) y^{(n-1)} + y^{(n)} = b(x)$$
>
>be a [linear ODE](./Linear%20Ordinary%20Differential%20Equations.md) with [initial conditions](./Initial%20Value%20Problems.md) $(x_0, y_0), \dotsc, (x_n, y_n)$, where $x_0, \dotsc, x_n \in I$.
>
>If $a_0, a_1, \dotsc, a_{n-1}$ and $b$ are [continuous](../../Real%20Functions/Continuity%20(Real%20Functions).md) on $I$, then there exists one and only one [function](../../Real%20Functions/Real%20Functions.md) $\phi: I \to \mathbb{R}$ which satisfies the [initial conditions](./Initial%20Value%20Problems.md) and the [linear ODE](./Linear%20Ordinary%20Differential%20Equations.md) for every $x \in I$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Homogeneity and Linear ODEs
>
>Let $n \in \mathbb{N}_{\ge 1}$, let $F: \mathcal{D}_F \subseteq \mathbb{R}^{n+2} \to \mathbb{R}$ be a [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) with $\mathcal{D}_F \ne \varnothing$, let $\mathcal{D}_t \subseteq \mathbb{R}$ be the [projection](TODO) of $\mathcal{D}_F$ on its first variable and suppose that the [ordinary differential equation](./Real%20Ordinary%20Differential%20Equations.md)
>
>$$F\left(t, x, x', x'', \dotsc, x^{(n)}\right) = 0$$
>
>is [linear](./Linear%20Ordinary%20Differential%20Equations.md) with
>
>$$F\left(t, x, x', x'', \dotsc, x^{(n)}\right) = \alpha_0(t) x + \alpha_1(t)x' + \cdots + \alpha_n(t) x^{(n)} - \beta(t).$$
>
>If $\beta (t) = 0$ for all $t \in \mathcal{D}_t$, then $F\left(t, x, x', x'', \dotsc, x^{(n)}\right) = 0$ is also [homogeneous](./Homogeneous%20Ordinary%20Differential%20Equations.md).
>
>If $F\left(t, x, x', x'', \dotsc, x^{(n)}\right) = 0$ is [homogeneous](./Homogeneous%20Ordinary%20Differential%20Equations.md) and such that the [set](../../../../Set%20Theory/Sets.md) $\{\boldsymbol{x} \in \mathbb{R}^{n+1}\mid (t, \boldsymbol{x})^{\mathsf{T}} \in \mathcal{D}_F\}$ is a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $\mathbb{R}^{n+1}$ for each $t \in \mathcal{D}_t$, then $\beta(t) = 0$ for all $t \in \mathcal{D}_t$ if and only if $x = 0$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $\mathcal{D}_t$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Homogeneous Solutions Form Linear Subspaces
>
>Let $n \in \mathbb{N}_{\ge 1}$, let $F: \mathcal{D}_F \subseteq \mathbb{R}^{n+2} \to \mathbb{R}$ with $\mathcal{D}_F \ne \varnothing$ be a [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) which is [dependent](TODO) on its last argument and let $S \subseteq \mathbb{R}$.
>
>Suppose that the [ordinary differential equation](./Real%20Ordinary%20Differential%20Equations.md) $F\left(t, x, x', x'', \dotsc, x^{(n)}\right) = 0$ satisfies all of the following:
>
>- It is [linear](./Linear%20Ordinary%20Differential%20Equations.md);
>- It is [homogeneous](./Homogeneous%20Ordinary%20Differential%20Equations.md);
>- It is such that the [set](../../../../Set%20Theory/Sets.md) $\{\boldsymbol{x} \in \mathbb{R}^{n+1}\mid (t, \boldsymbol{x})^{\mathsf{T}} \in \mathcal{D}_F\}$ is a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $\mathbb{R}^{n+1}$ for each $t \in S$;
>- It has [solutions](./Real%20Ordinary%20Differential%20Equations.md) on $S$ whose [domain](../../../Functions/Functions.md) is $S$.
>
>Then these [solutions](./Real%20Ordinary%20Differential%20Equations.md) form a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of the [canonical function space](../../../Functions/Canonical%20Function%20Space.md) $\mathbb{R}^S$.
>
>>[!PROOF]-
>>
>>Let $\text{Sol}(S)$ be the [set](../../../../Set%20Theory/Sets.md) of all [solutions](./Real%20Ordinary%20Differential%20Equations.md) on $S$ whose [domain](../../../Functions/Functions.md) is $S$:
>>
>>$$\text{Sol}(S) \overset{\text{def}}{=} \{\phi \in \mathbb{R}^S \mid \phi \text{ is a solution on } S\}$$
>>
>>By hypothesis, for each $t \in S$, the [set](../../../../Set%20Theory/Sets.md) $V_t \overset{\text{def}}{=} \{\boldsymbol{x} \in \mathbb{R}^{n+1}\mid (t, \boldsymbol{x})^{\mathsf{T}} \in \mathcal{D}_F\}$ is guaranteed to be a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $\mathbb{R}^{n+1}$. 
>>
>>Since $F\left(t, x, x', x'', \dotsc, x^{(n)}\right) = 0$ is [linear](./Linear%20Ordinary%20Differential%20Equations.md), we have:
>>
>>$$F\left(t, x, x', x'', \dotsc, x^{(n)}\right) = \alpha_0(t) x + \alpha_1(t)x' + \cdots + \alpha_n(t) x^{(n)} - \beta(t)$$
>>
>>For each $t \in \mathcal{D}_t$, define $L_t$ as follows:
>>
>>$$L_t(x_0, x_1, \dotsc, x_n) \overset{\text{def}}{=} \sum_{k = 0}^n \alpha_k(t) x_k$$
>>
>>We thus have the following on $\mathcal{D}_F$:
>>
>>$$F(t, x_0, x_1, \dotsc, x_n) = L_t(x_0, x_1, \dotsc, x_n) - \beta (t)$$
>>
>>If $S = \varnothing$, then $\mathbb{R}^S$ contains only the [empty function](../../../Functions/Empty%20Function.md), i.e. $\mathbb{R}^S = \{\varnothing\}$. Interestingly, it is irrelevant if the [empty function](../../../Functions/Empty%20Function.md) is considered a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $S$:
>>- If the [empty function](../../../Functions/Empty%20Function.md) *is* considered a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $S$, then $\text{Sol}(S) = \{\varnothing\} = \mathbb{R}^S$, which is a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $\mathbb{R}^S$, since every [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) is a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of itself.
>>- If the [empty function](../../../Functions/Empty%20Function.md) is *not* considered a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $S$, then the hypothesis "has [solution](./Real%20Ordinary%20Differential%20Equations.md) on $S$" is false and so the [implication](TODO) is vacuously true.
>>
>>If $S \ne \varnothing$, there exists some [solution](./Real%20Ordinary%20Differential%20Equations.md) $x: S \to \mathbb{R} \in \text{Sol}(S)$ on $S$ which is *not* the [empty function](../../../Functions/Empty%20Function.md). Fix some $t \in S$ and define $\boldsymbol{x} \in \mathbb{R}^{n+1}$ as follows:
>>
>>$$\boldsymbol{x} \overset{\text{def}}{=} \begin{bmatrix} x(t) \\ x'(t) \\ \vdots \\ x^{(n)}(t)\end{bmatrix} \in \mathbb{R}^{n+1}$$
>>
>>Since $x$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md), we have $(t, \boldsymbol{x})^{\mathsf{T}} \in \mathcal{D}_F$ and $F(t, \boldsymbol{x}) = 0$. By hypothesis, $V_t$ is a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) and, since $\boldsymbol{x} \in V_t$, we get $2 \boldsymbol{x} \in V_t$ and thus $(t, 2\boldsymbol{x}) \in \mathcal{D}_F$. By [homogeneity](./Homogeneous%20Ordinary%20Differential%20Equations.md), there exists some $r \in \mathbb{R}$ with $F(t, 2\boldsymbol{x}) = 2^r \cdot F(t, \boldsymbol{x})$. Therefore:
>>
>>$$F(t, 2\boldsymbol{x}) = 2^r \cdot F(t, \boldsymbol{x}) = 2^r \cdot 0 = 0$$
>>
>>Now, we use the fact that the [ODE](./Real%20Ordinary%20Differential%20Equations.md) is [linear](./Linear%20Ordinary%20Differential%20Equations.md) and that $L_t$ is also [linear](../../../Functional%20Analysis/Linearity/Linearity%20(Functions).md):
>>
>>$$F(t, \boldsymbol{x}) = L_t(\boldsymbol{x}) - \beta(t) = 0$$
>>
>>$$F(t, 2\boldsymbol{x}) = L_t(2\boldsymbol{x}) - \beta(t) = 2L_t(\boldsymbol{x}) - \beta(t) = 0$$
>>
>>Subtracting twice the first result from the second yields the following:
>>
>>$$2L_t(\boldsymbol{x}) - \beta(t) - 2(L_t(\boldsymbol{x}) - \beta(t)) = 0$$
>>
>>$$2L_t(\boldsymbol{x}) - \beta(t) - 2L_t(\boldsymbol{x}) + 2\beta(t) = 0$$
>>
>>$$\beta(t) = 0$$
>>
>>Since $t \in S$ was arbitrarily chosen, we get $\beta(t) = 0$ for all $t \in S$. Therefore, for each $t \in S$ and all $(t, x_0, x_1, \dotsc, x_n)^{\mathsf{T}} \in \mathcal{D}_F$, we get:
>>
>>$$F(t, x_0, x_1, \dotsc, x_n) = L_t(x_0, x_1, \dotsc, x_n) - \beta(t) = L_t(x_0, x_1, \dotsc, x_n)$$
>>
>>Now let $x,y \in \text{Sol}(S)$, let $a, b \in \mathbb{R}$ and define $z: S \to \mathbb{R}$ as follows:
>>
>>$$z = ax + by$$
>>
>>Using the properties of [differentiation](../../Real%20Functions/Differentiability%20(Real%20Functions).md), we get
>>
>>$$z^{(k)}(t) = a x^{(k)}(t) + b y^{(k)}(t)$$
>>
>>for all $k \in \{1, \dotsc, n\}$ and all $t \in S$. Therefore:
>>
>>$$\begin{bmatrix}z(t) \\ z'(t) \\ \vdots \\ z^{(n)}(t)\end{bmatrix} = a\begin{bmatrix}x(t) \\ x'(t) \\ \vdots \\ x^{(n)}(t)\end{bmatrix} + b\begin{bmatrix}y(t) \\ y'(t) \\ \vdots \\ y^{(n)}(t)\end{bmatrix}$$
>>
>>Since $x$ and $y$ are [solutions](./Real%20Ordinary%20Differential%20Equations.md), we know that $(x(t), x'(t), \dotsc, x^{(n)}(t))^{\mathsf{T}} \in V_t$ and $(y(t), y'(t), \dotsc, y^{(n)}(t))^{\mathsf{T}} \in V_t$ for each $t \in S$. Since $V_t$ is a [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md), the [linear combination](../../../../Algebra/Vector%20Spaces/Linear%20Combinations.md) $a(x(t), x'(t), \dotsc, x^{(n)}(t))^{\mathsf{T}} + b(y(t), y'(t), \dotsc, y^{(n)}(t))^{\mathsf{T}})$ must also be in $V_t$. Therefore, $(z(t), z'(t), \dotsc, z^{(n)}(t))^{\mathsf{T}} \in V_t$ for each $t \in S$ and so $(t, z(t), z'(t), \dotsc, z^{(n)}(t))^{\mathsf{T}} \in \mathcal{D}_F$ for each $t \in S$. We also get the following:
>>
>>$$\begin{aligned}F\left(t,z(t),z'(t),\dotsc,z^{(n)}(t)\right) & = L_t\left(z(t),z'(t),\dotsc,z^{(n)}(t)\right) \\ & = L_t\left( a\left(x(t),x'(t),\dotsc,x^{(n)}(t)\right) + b\left(y(t),y'(t),\dotsc,y^{(n)}(t)\right) \right) \\ & = a \cdot L_t\left(x(t),x'(t),\dotsc,x^{(n)}(t)\right) + b \cdot L_t\left(y(t),y'(t),\dotsc,y^{(n)}(t)\right) \\ & = a \cdot F\left(t,x(t),x'(t),\dotsc,x^{(n)}(t)\right) + b\cdot F\left(t,y(t),y'(t),\dotsc,y^{(n)}(t)\right) \\ & = a \cdot 0 + b \cdot 0 \\ & = 0\end{aligned}$$
>>
>>Therefore, $z: S \to \mathbb{R}$ is also a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $S$. Finally, since $\text{Sol}(S) \ne \varnothing$, we have shown that $\text{Sol}(S) \ne \varnothing$ is a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $\mathbb{R}^S$.
>>
>

>[!THEOREM] Theorem: General Solutions Form Affine Subspaces
>
>Let $n \in \mathbb{N}_{\ge 1}$, let $F: \mathcal{D}_F \subseteq \mathbb{R}^{n+2} \to \mathbb{R}$ with $\mathcal{D}_F \ne \varnothing$ be a [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) which is [dependent](TODO) on its last argument and let $S \subseteq \mathbb{R}$.
>
>Suppose that the [ordinary differential equation](./Real%20Ordinary%20Differential%20Equations.md) $F\left(t, x, x', x'', \dotsc, x^{(n)}\right) = 0$ satisfies all of the following:
>
>- It is [linear](./Linear%20Ordinary%20Differential%20Equations.md);
>- It is such that the [set](../../../../Set%20Theory/Sets.md) $\{\boldsymbol{x} \in \mathbb{R}^{n+1}\mid (t, \boldsymbol{x})^{\mathsf{T}} \in \mathcal{D}_F\}$ is a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $\mathbb{R}^{n+1}$ for each $t \in S$;
>- It has [solutions](./Real%20Ordinary%20Differential%20Equations.md) on $S$ whose [domain](../../../Functions/Functions.md) is $S$.
>
>Then these [solutions](./Real%20Ordinary%20Differential%20Equations.md) form an [affine subspace](../../../../Algebra/Vector%20Spaces/Affine%20Subspaces.md) of the [canonical function space](../../../Functions/Canonical%20Function%20Space.md) $\mathbb{R}^S$. Furthermore, in this case, $\phi: S \to \mathbb{R}$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $S$ if and only if there exists some [solution](./Real%20Ordinary%20Differential%20Equations.md) $\phi_{\text{p}}: S \to \mathbb{R}$ and some [solution](./Real%20Ordinary%20Differential%20Equations.md) $\phi_{\text{h}}: S \to \mathbb{R}$ on $S$ of the [corresponding homogeneous equation](./Linear%20Ordinary%20Differential%20Equations.md) $F_{\text{h}} \left(t, x, x', x'', \dotsc, x^{(n)}\right) = 0$ such that $\phi = \phi_{\text{p}} + \phi_{\text{h}}$.
>
>>[!PROOF]-
>>
>>Let $\text{Sol}(S)$ be the [set](../../../../Set%20Theory/Sets.md) of all [solutions](./Real%20Ordinary%20Differential%20Equations.md) of $F=0$ on $S$ whose [domain](../../../Functions/Functions.md) is $S$:
>>
>>$$\text{Sol}(S) \overset{\text{def}}{=} \{\phi \in \mathbb{R}^S \mid \phi \text{ is a solution of } F=0 \text{ on } S\}$$
>>
>>Let $\text{Sol}_h(S)$ be the [set](../../../../Set%20Theory/Sets.md) of all [solutions](./Real%20Ordinary%20Differential%20Equations.md) of the [corresponding homogeneous equation](./Linear%20Ordinary%20Differential%20Equations.md) $F_h = 0$ on $S$ whose [domain](../../../Functions/Functions.md) is $S$:
>>
>>$$\text{Sol}_h(S) \overset{\text{def}}{=} \{\phi \in \mathbb{R}^S \mid \phi \text{ is a solution of } F_h=0 \text{ on } S\}$$
>>
>>By hypothesis, for each $t \in S$, the [set](../../../../Set%20Theory/Sets.md) $V_t \overset{\text{def}}{=} \{\boldsymbol{x} \in \mathbb{R}^{n+1}\mid (t, \boldsymbol{x})^{\mathsf{T}} \in \mathcal{D}_F\}$ is guaranteed to be a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $\mathbb{R}^{n+1}$.
>>
>>Since $F\left(t, x, x', x'', \dotsc, x^{(n)}\right) = 0$ is [linear](./Linear%20Ordinary%20Differential%20Equations.md), we have:
>>
>>$$F\left(t, x, x', x'', \dotsc, x^{(n)}\right) = \alpha_0(t) x + \alpha_1(t)x' + \cdots + \alpha_n(t) x^{(n)} - \beta(t)$$
>>
>>For each $t \in \mathcal{D}_t$, define $L_t$ as follows:
>>
>>$$L_t(x_0, x_1, \dotsc, x_n) \overset{\text{def}}{=} \sum_{k = 0}^n \alpha_k(t) x_k$$
>>
>>We thus have the following on $\mathcal{D}_F$:
>>
>>$$F(t, x_0, x_1, \dotsc, x_n) = L_t(x_0, x_1, \dotsc, x_n) - \beta(t)$$
>>
>>By definition of the [corresponding homogeneous equation](./Linear%20Ordinary%20Differential%20Equations.md), we also have:
>>
>>$$F_h(t, x_0, x_1, \dotsc, x_n) = L_t(x_0, x_1, \dotsc, x_n)$$
>>
>>If $S = \varnothing$, then $\mathbb{R}^S$ contains only the [empty function](../../../Functions/Empty%20Function.md), i.e. $\mathbb{R}^S = \{\varnothing\}$. Interestingly, it is irrelevant if the [empty function](../../../Functions/Empty%20Function.md) is considered a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $S$:
>>- If the [empty function](../../../Functions/Empty%20Function.md) *is* considered a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $S$, then $\text{Sol}(S) = \{\varnothing\} = \mathbb{R}^S$ and $\text{Sol}_h(S) = \{\varnothing\} = \mathbb{R}^S$. Since every [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) is an [affine subspace](../../../../Algebra/Vector%20Spaces/Affine%20Subspaces.md) of itself, $\text{Sol}(S)$ is an [affine subspace](../../../../Algebra/Vector%20Spaces/Affine%20Subspaces.md) of $\mathbb{R}^S$. Furthermore, setting $\phi_{\text{p}} = \varnothing$ and $\phi_{\text{h}} = \varnothing$ trivially satisfies the condition $\phi = \phi_{\text{p}} + \phi_{\text{h}} = \varnothing$.
>>- If the [empty function](../../../Functions/Empty%20Function.md) is *not* considered a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $S$, then the hypothesis "has [solutions](./Real%20Ordinary%20Differential%20Equations.md) on $S$" is false and so the [implication](TODO) is vacuously true.
>>
>>If $S \ne \varnothing$, there exists some [solution](./Real%20Ordinary%20Differential%20Equations.md) $\phi_{\text{p}}: S \to \mathbb{R} \in \text{Sol}(S)$ on $S$ which is *not* the [empty function](../../../Functions/Empty%20Function.md).
>>
>>First, we show that $\phi \in \text{Sol}(S)$ if and only if there exists some $\phi_{\text{h}} \in \text{Sol}_h(S)$ such that $\phi = \phi_{\text{p}} + \phi_{\text{h}}$.
>>
>>Forward direction ($\implies$): Let $\phi \in \text{Sol}(S)$ and define $\phi_{\text{h}}: S \to \mathbb{R}$ as follows:
>>
>>$$\phi_{\text{h}} \overset{\text{def}}{=} \phi - \phi_{\text{p}}$$
>>
>>Using the properties of [differentiation](../../Real%20Functions/Differentiability%20(Real%20Functions).md), we get $\phi_{\text{h}}^{(k)}(t) = \phi^{(k)}(t) - \phi_{\text{p}}^{(k)}(t)$ for all $k \in \{1, \dotsc, n\}$ and all $t \in S$. Therefore:
>>
>>$$\begin{bmatrix}\phi_{\text{h}}(t) \\ \phi_{\text{h}}'(t) \\ \vdots \\ \phi_{\text{h}}^{(n)}(t)\end{bmatrix} = \begin{bmatrix}\phi(t) \\ \phi'(t) \\ \vdots \\ \phi^{(n)}(t)\end{bmatrix} - \begin{bmatrix}\phi_{\text{p}}(t) \\ \phi_{\text{p}}'(t) \\ \vdots \\ \phi_{\text{p}}^{(n)}(t)\end{bmatrix}$$
>>
>>Since $\phi$ and $\phi_{\text{p}}$ are [solutions](./Real%20Ordinary%20Differential%20Equations.md) of $F=0$, we know that $(\phi(t), \phi'(t), \dotsc, \phi^{(n)}(t))^{\mathsf{T}}$ and $\phi_{\text{p}}(t), \phi_{\text{p}}'(t), \dotsc, \phi_{\text{p}}^{(n)}(t))^{\mathsf{T}}$ are in $V_t$ for each $t \in S$. Because $V_t$ is a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md), their difference must also be in $V_t$, i.e. $(t, \phi_{\text{h}}(t), \phi_{\text{h}}'(t), \dotsc, \phi_{\text{h}}^{(n)}(t))^{\mathsf{T}} \in \mathcal{D}_F$ for all $t \in S$. Since $L_t$ is [linear](../../../Functional%20Analysis/Linearity/Linearity%20(Functions).md), we obtain:
>>
>>$$\begin{aligned}F_h\left(t,\phi_{\text{h}}(t),\phi_{\text{h}}'(t),\dotsc,\phi_{\text{h}}^{(n)}(t)\right) & = L_t\left(\phi_{\text{h}}(t),\phi_{\text{h}}'(t),\dotsc,\phi_{\text{h}}^{(n)}(t)\right) \\ & = L_t\left( \left(\phi(t),\phi'(t),\dotsc,\phi^{(n)}(t)\right) - \left(\phi_{\text{p}}(t),\phi_{\text{p}}'(t),\dotsc,\phi_{\text{p}}^{(n)}(t)\right) \right) \\ & = L_t\left(\phi(t),\phi'(t),\dotsc,\phi^{(n)}(t)\right) - L_t\left(\phi_{\text{p}}(t),\phi_{\text{p}}'(t),\dotsc,\phi_{\text{p}}^{(n)}(t)\right) \\ & = \left(F\left(t,\phi(t),\dotsc,\phi^{(n)}(t)\right) + \beta(t)\right) - \left(F\left(t,\phi_{\text{p}}(t),\dotsc,\phi_{\text{p}}^{(n)}(t)\right) + \beta(t)\right) \\ & = (0 + \beta(t)) - (0 + \beta(t)) \\ & = 0\end{aligned}$$
>>
>>Therefore, $\phi_{\text{h}}$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) of the [corresponding homogeneous equation](./Linear%20Ordinary%20Differential%20Equations.md) on $S$ (i.e., $\phi_{\text{h}} \in \text{Sol}_h(S)$) and $\phi = \phi_{\text{p}} + \phi_{\text{h}}$.
>>
>>Backwards direction ($\impliedby$): Let $\phi_{\text{h}} \in \text{Sol}_h(S)$ and define $\phi \overset{\text{def}}{=} \phi_{\text{p}} + \phi_{\text{h}}$.
>>
>>By the same reasoning regarding [differentiation](../../Real%20Functions/Differentiability%20(Real%20Functions).md) and $V_t$ being a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md), we have $(t, \phi(t), \phi'(t), \dotsc, \phi^{(n)}(t))^{\mathsf{T}} \in \mathcal{D}_F$ for all $t \in S$. We then have:
>>
>>$$\begin{aligned}F\left(t,\phi(t),\phi'(t),\dotsc,\phi^{(n)}(t)\right) & = L_t\left(\phi(t),\phi'(t),\dotsc,\phi^{(n)}(t)\right) - \beta(t) \\ & = L_t\left( \left(\phi_{\text{p}}(t),\phi_{\text{p}}'(t),\dotsc,\phi_{\text{p}}^{(n)}(t)\right) + \left(\phi_{\text{h}}(t),\phi_{\text{h}}'(t),\dotsc,\phi_{\text{h}}^{(n)}(t)\right) \right) - \beta(t) \\ & = L_t\left(\phi_{\text{p}}(t),\phi_{\text{p}}'(t),\dotsc,\phi_{\text{p}}^{(n)}(t)\right) + L_t\left(\phi_{\text{h}}(t),\phi_{\text{h}}'(t),\dotsc,\phi_{\text{h}}^{(n)}(t)\right) - \beta(t) \\ & = \left(F\left(t,\phi_{\text{p}}(t),\dotsc,\phi_{\text{p}}^{(n)}(t)\right) + \beta(t)\right) + F_h\left(t,\phi_{\text{h}}(t),\dotsc,\phi_{\text{h}}^{(n)}(t)\right) - \beta(t) \\ & = (0 + \beta(t)) + 0 - \beta(t) \\ & = 0\end{aligned}$$
>>
>>Thus, $\phi \in \text{Sol}(S)$.
>>
>>We have established that $\text{Sol}(S) = \{\phi_{\text{p}} + \phi_{\text{h}} \mid \phi_{\text{h}} \in \text{Sol}_h(S)\} = \phi_{\text{p}} + \text{Sol}_h(S)$. To conclude that $\text{Sol}(S)$ is an [affine subspace](../../../../Algebra/Vector%20Spaces/Affine%20Subspaces.md) of $\mathbb{R}^S$, we must finally show that $\text{Sol}_h(S)$ is a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $\mathbb{R}^S$.
>>
>>Notice that the [corresponding homogeneous equation](./Linear%20Ordinary%20Differential%20Equations.md) $F_{\text{h}} \left(t, x, x', x'', \dotsc, x^{(n)}\right) = 0$ is [linear](./Linear%20Ordinary%20Differential%20Equations.md) of the form
>>
>>$$F_{\text{h}}\left(t, x, x', x'', \dotsc, x^{(n)}\right) = \alpha_0(t) x + \alpha_1(t)x' + \cdots + \alpha_n(t) x^{(n)} - \beta(t)$$
>>
>>with $\beta = 0$ and so it is also [homogeneous](./Homogeneous%20Ordinary%20Differential%20Equations.md).
>>
>>By hypothesis, we have that $V_t = \{\boldsymbol{x} \in \mathbb{R}^{n+1}\mid (t, \boldsymbol{x})^{\mathsf{T}} \in \mathcal{D}_F\}$ is a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $\mathbb{R}^{n+1}$ for each $t \in S$ and so $(t, 0, 0, \dotsc, 0)^{\mathsf{T}} \in \mathcal{D}_F$ for all $t \in S$. Therefore, for each $t \in S$, we have:
>>
>>$$F_{\text{h}}\left(t, 0, 0, 0, \dotsc, 0\right) = \alpha_0(t) \cdot 0 + \alpha_1(t) \cdot 0 + \cdots + \alpha_n(t) \cdot 0 = 0$$
>>
>>This means that $0: S \to \mathbb{R}$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) of $F_{\text{h}}\left(t, x, x', x'', \dotsc, x^{(n)}\right) = 0$ on $S$ with [domain](../../../Functions/Functions.md) $S$. Now, $F_{\text{h}}\left(t, x, x', x'', \dotsc, x^{(n)}\right) = 0$ satisfies the following conditions:
>>
>>- It is [linear](./Linear%20Ordinary%20Differential%20Equations.md);
>>- It is [homogeneous](./Homogeneous%20Ordinary%20Differential%20Equations.md);
>>- It is such that the [set](../../../../Set%20Theory/Sets.md) $\{\boldsymbol{x} \in \mathbb{R}^{n+1}\mid (t, \boldsymbol{x})^{\mathsf{T}} \in \mathcal{D}_F\}$ is a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $\mathbb{R}^{n+1}$ for each $t \in S$;
>>- It has [solutions](./Real%20Ordinary%20Differential%20Equations.md) on $S$ whose [domain](../../../Functions/Functions.md) is $S$ (namely, $0$).
>>
>>Another theorem allows to therefore conclude that $\text{Sol}_{\text{h}}(S)$ is a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $\mathbb{R}^S$. Since $\text{Sol}(S) = \phi_{\text{p}} + \text{Sol}_h(S)$ corresponds to the translation of the [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) $\text{Sol}_h(S)$ by the element $\phi_{\text{p}} \in \mathbb{R}^S$, the [solutions](./Real%20Ordinary%20Differential%20Equations.md) $\text{Sol}(S)$ form an [affine subspace](../../../../Algebra/Vector%20Spaces/Affine%20Subspaces.md) of the [canonical function space](../../../Functions/Canonical%20Function%20Space.md) $\mathbb{R}^S$.
>>
>

## Linear ODEs with Constant Coefficients

>[!DEFINITION] Definition: Linear ODE with Constant Coefficients
>
>A **linear ODE with constant coefficients** is a [linear ODE](./Linear%20Ordinary%20Differential%20Equations.md) which can be written in the form
>
>$$a_n y^{(n)} + a_{n-1} y^{(n-1)} + \cdots + a_1 y' + a_0 y = b,$$
>
>where $b, a_0, \dotsc, a_n \in \mathbb{R}$ are [real numbers](../../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md).
>

>[!DEFINITION] Definition: Characteristic Polynomial
>
>The **characteristic polynomial** of a [homogeneous linear ODE with constant coefficients](./Linear%20Ordinary%20Differential%20Equations.md)
>
>$$a_n y^{(n)} + a_{n-1} y^{(n-1)} + \cdots + a_1 y' + a_0 y = 0,$$
>
>is the following [complex polynomial](../../../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Polynomials.md):
>
>$$P(\lambda) = a_n \lambda^n + a_{n-1} \lambda^{n-1} + \cdots + a_1 \lambda + a_0$$
>

>[!THEOREM] Theorem: Solutions from Characteristic Polynomials
>
>Consider the following [homogeneous linear ODE with constant coefficients](./Linear%20Ordinary%20Differential%20Equations.md):
>
>$$y^{(n)} + a_{n-1} y^{(n-1)} + \cdots + a_1 y' + a_0 y = 0$$
>
>The [roots](../../../../Algebra/Polynomials/Univariate%20Polynomials.md) of its [characteristic polynomial](./Linear%20Ordinary%20Differential%20Equations.md) can be used to generate a [basis](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) for the [solution space](./Linear%20Ordinary%20Differential%20Equations.md):
>
>    - Each [real](../../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) [root](../../../../Algebra/Polynomials/Univariate%20Polynomials.md) $\lambda$ with [multiplicity](TODO) $k$ yields the following [basis elements](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md):
>    
>    $$\mathrm{e}^{\lambda t}, t \mathrm{e}^{\lambda t}, \dotsc, t^{k-1}\mathrm{e}^{\lambda t}$$
>
>    - Each pair of [complex conjugated](../../../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md) [roots](../../../../Algebra/Polynomials/Univariate%20Polynomials.md) $\lambda = a \pm b \mathrm{i}$ with individual [multiplicity](TODO) $k$ yields the following [basis elements](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md):
>
>    $$\mathrm{e}^{at}\cos(bt), \mathrm{e}^{at}\sin(bt),t\mathrm{e}^{at} \cos(bt), t\mathrm{e}^{at}\sin(bt), \dotsc, t^{k-1} \mathrm{e}^{at} \cos(bt), t^{k-1} \mathrm{e}^{at} \sin(bt)$$
>
>>[!EXAMPLE]-
>>
>>Consider the following [homogeneous linear ODE with constant coefficients](./Linear%20Ordinary%20Differential%20Equations.md):
>>
>>$$y''' - 6y'' + 11 y' - 6y = 0$$
>>
>>It has the [characteristic polynomial](./Linear%20Ordinary%20Differential%20Equations.md)
>>
>>$$P(\lambda) = \lambda^3 -6\lambda^2 + 11\lambda - 6$$
>>
>>whose [roots](../../../../Algebra/Polynomials/Univariate%20Polynomials.md) are the following:
>>
>>$$\lambda_1 = 1 \qquad \lambda_2 = 2 \qquad \lambda_3 = 3$$
>>
>>We get the following [basis](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md):
>>
>>$$\{ \mathrm{e}^{t}, \mathrm{e}^{2t}, \mathrm{e}^{3t}\}$$
>>
>>The general [solution](./Real%20Ordinary%20Differential%20Equations.md) is thus the following:
>>
>>$$y(t) = c_1 \mathrm{e}^t + c_2 \mathrm{e}^{2t} + c_3 \mathrm{e}^{3t} \qquad c_1, c_2, c_3 \in \mathbb{R}$$
>>
>
>>[!EXAMPLE]-
>>
>>Consider the following [homogeneous linear ODE with constant coefficients](./Linear%20Ordinary%20Differential%20Equations.md):
>>
>>$$y^{(4)} - 4y''' + 5y'' - 4y' + 4y = 0$$
>>
>>It has the [characteristic polynomial](./Linear%20Ordinary%20Differential%20Equations.md)
>>
>>$$P(\lambda) = \lambda^4 - 4\lambda^3 + 5\lambda^2 - 4\lambda + 4$$
>>
>>whose [roots](../../../../Algebra/Polynomials/Univariate%20Polynomials.md) are the following:
>>
>>$$\lambda_1 = 2 \qquad \lambda_2 = 2 \qquad \lambda_3 = \mathrm{i} \qquad \lambda_4 = -\mathrm{i}$$
>>
>>We get the following [basis](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md):
>>
>>$$\{ \mathrm{e}^{2t}, t\mathrm{e}^{2t}, \cos(t), \sin(t) \}$$
>>
>>The general [solution](./Real%20Ordinary%20Differential%20Equations.md) is thus the following:
>>
>>$$y(t) = c_1 \mathrm{e}^{2t} + c_2 t\mathrm{e}^{2t} + c_3 \cos(t) + c_4 \sin(t) \qquad c_1, c_2, c_3, c_4 \in \mathbb{R}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Reduction to Linear System
>
>Consider the following [homogeneous linear ODE with constant coefficients](./Linear%20Ordinary%20Differential%20Equations.md):
>
>$$y^{(n)} + a_{n-1} y^{(n-1)} + \cdots + a_1 y' + a_0 y = 0$$
>
>A [function](../../Real%20Functions/Real%20Functions.md) $\phi$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) on some [interval](../../Euclidean%20Space/Euclidean%20Space.md) $I \subseteq \mathbb{R}$ if and only if $\boldsymbol{\psi}$ is a [solution](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) on $I$ of the [linear system](./Linear%20Systems%20of%20ODEs.md)
>
>$$\boldsymbol{y}' = \boldsymbol{A}\boldsymbol{y},$$
>
>where:
>
>$$\boldsymbol{\psi} = \begin{bmatrix} \phi \\ \phi' \\ \vdots \\ \phi^{(n-1)}\end{bmatrix} \qquad \boldsymbol{A} = \begin{bmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & 1 \\ -a_0 & -a_1 & -a_2 & \cdots & -a_{n-1} \end{bmatrix}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>