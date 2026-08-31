---
tags:
    - real-analysis
    - analysis
    - mathematics
---

# Homogeneous Ordinary Differential Equations

>[!DEFINITION] Definition: Homogeneous Ordinary Differential Equations
>
>Let $n \in \mathbb{N}_{\ge 1}$ and let $F: \mathcal{D}_F \subseteq \mathbb{R}^{n+2} \to \mathbb{R}$ be a [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md).
>
>The [ordinary differential equation](./Real%20Ordinary%20Differential%20Equations.md)
>
>$$F(t, x, x', \dotsc, x^{(n)}) = 0$$
>
>is **homogeneous** if there exists some [real number](../../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) $r \in \mathbb{R}$ such that
>
>$$F(t, \lambda x_0, \lambda x_1, \dotsc, \lambda x_n) = \lambda^r F(t, x_0, x_1, \dotsc, x_n)$$
>
>for all $\begin{bmatrix}t & x_0 & x_1 & \cdots & x_n\end{bmatrix}^{\mathsf{T}} \in \mathcal{D}_F$ and all $\lambda \in \mathbb{R}_{\gt 0}$ for which $\begin{bmatrix}t & \lambda x_0 & \lambda x_1 & \cdots & \lambda x_n\end{bmatrix}^{\mathsf{T}} \in \mathcal{D}_F$.
>

>[!THEOREM] Theorem: Multiples of Solutions are Solutions
>
>Let $n \in \mathbb{N}_{\ge 1}$, let $F: \mathcal{D}_F \subseteq \mathbb{R} \times \mathbb{R} \times \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), let $S \subseteq \mathbb{R}$ and let $\mu \in \mathbb{R}_{\gt 0}$.
>
>If the [ordinary differential equation](./Real%20Ordinary%20Differential%20Equations.md)
>
>$$F\left(t, x, x', x'', \dotsc, x^{(n)}\right) = 0$$
>
>is [homogeneous](./Homogeneous%20Ordinary%20Differential%20Equations.md) and $\phi: S \to \mathbb{R}$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $S$, then $\mu \phi$ is also a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $S$ if and only if $\begin{bmatrix} t & \mu \phi(t) & \mu \phi'(t) & \cdots & \mu \phi^{(n)}(t)\end{bmatrix}^{\mathsf{T}} \in \mathcal{D}_F$ for all $t \in S$.
>
>>[!PROOF]-
>>
>>Suppose that
>>
>>$$F\left(t, x, x', x'', \dotsc, x^{(n)}\right) = 0$$
>>
>>is [homogeneous](./Homogeneous%20Ordinary%20Differential%20Equations.md) and $\phi: S \to \mathbb{R}$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $S$.
>>
>>We need to prove two things:
>>
>>- (1) If $\mu \phi$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $S$, then $\begin{bmatrix} t & \mu \phi(t) & \mu \phi'(t) & \cdots & \mu \phi^{(n)}(t)\end{bmatrix}^{\mathsf{T}} \in \mathcal{D}_F$ for all $t \in S$.
>>
>>- (2) If $\begin{bmatrix} t & \mu \phi(t) & \mu \phi'(t) & \cdots & \mu \phi^{(n)}(t)\end{bmatrix}^{\mathsf{T}} \in \mathcal{D}_F$ for all $t \in S$, then $\mu \phi$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $S$.
>>
>>**Proof of (1):**
>>
>>By the very definition of a [solution](./Real%20Ordinary%20Differential%20Equations.md), we have $\begin{bmatrix} t & (\mu \phi)(t) & (\mu \phi)'(t) & \cdots & (\mu \phi)^{(n)}(t)\end{bmatrix}^{\mathsf{T}} \in \mathcal{D}_F$ for all $t \in S$. Using the linear property of [derivatives](../../Real%20Functions/Differentiability%20(Real%20Functions).md), we can pull $\mu$ out and so we get $\begin{bmatrix} t & \mu \phi(t) & \mu \phi'(t) & \cdots & \mu \phi^{(n)}(t)\end{bmatrix}^{\mathsf{T}} \in \mathcal{D}_F$ for all $t \in S$.
>>
>>**Proof of (2):**
>>
>>We have $\begin{bmatrix} t & (\mu\phi)(t) & (\mu\phi)'(t) & \cdots & (\mu\phi)^{(n)}(t)\end{bmatrix}^{\mathsf{T}} \in \mathcal{D}_F$ for all $t \in S$ by hypothesis.
>>
>>Now, since $\phi: S \to \mathbb{R}$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $S$, it is $n$-times [differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) on $S$. Therefore, $\mu \phi$ is also $n$-times [differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) on $S$, with $(\mu \phi)^{(j)} = \mu \phi^{(j)}$ for each $j \in \{0, 1, \dotsc, n\}$.
>>
>>It remains to show that $F\left(t, \mu\phi(t), \mu\phi'(t), \dotsc, \mu\phi^{(n)}(t)\right) = 0$ for all $t \in S$. Fix $t \in S$. Since $\phi$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md), we have $\begin{bmatrix} t & \phi(t) & \phi'(t) & \cdots & \phi^{(n)}(t)\end{bmatrix}^{\mathsf{T}} \in \mathcal{D}_F$. By hypothesis, $\begin{bmatrix} t & \mu\phi(t) & \mu\phi'(t) & \cdots & \mu\phi^{(n)}(t)\end{bmatrix}^{\mathsf{T}} \in \mathcal{D}_F$. Since the [ODE](./Real%20Ordinary%20Differential%20Equations.md) is [homogeneous](./Homogeneous%20Ordinary%20Differential%20Equations.md) and $\mu \gt 0$, there is some $r \in \mathbb{R}$ such that
>>
>>$$F\left(t, \mu\phi(t), \mu\phi'(t), \dotsc, \mu\phi^{(n)}(t)\right) = \mu^r F\left(t, \phi(t), \phi'(t), \dotsc, \phi^{(n)}(t)\right) = \mu^r \cdot 0 = 0.$$
>>
>>Since $t \in S$ was arbitrary, $\mu \phi$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $S$. 
>>
>