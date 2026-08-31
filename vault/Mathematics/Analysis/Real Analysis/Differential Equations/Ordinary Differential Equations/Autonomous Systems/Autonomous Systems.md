---
tags:
    - real-analysis
    - analysis
    - mathematics
---

# Autonomous Systems

>[!DEFINITION] Definition: Autonomous System of ODEs
>
>A [system of ODEs](../System%20of%20Real%20Ordinary%20Differential%20Equations.md) $\boldsymbol{F}$ is **autonomous** if $\boldsymbol{F}$ does not depend explicitly on its first argument (the independent variable $x$). 
>

## First-Order

The above theorem tells us that if a [solution](../System%20of%20Real%20Ordinary%20Differential%20Equations.md) is equal to some $\boldsymbol{y}^{\ast}$ for which $f(\boldsymbol{y}^{\ast}) = \boldsymbol{0}$, then that [solution](../System%20of%20Real%20Ordinary%20Differential%20Equations.md) must be equal to $\boldsymbol{y}^{\ast}$ on the entire [interval](../../../Euclidean%20Space/Euclidean%20Space.md) on which it is defined, i.e. the [solution](../System%20of%20Real%20Ordinary%20Differential%20Equations.md) does not change, it is *stationary*:

>[!DEFINITION] Definition: Stationary Point
>
>We say that $\boldsymbol{y}^{\ast} \in \mathbb{R}^n$ is a **stationary point** / **equilibrium point** / **fixed point** of an [autonomous system](./Autonomous%20Systems.md) $\boldsymbol{y}' = f(\boldsymbol{y})$ with $n$ equations if $f(\boldsymbol{y}^{\ast}) = \boldsymbol{0}$.
>

>[!DEFINITION] Definition: Stationary Point
>
>We say that $\boldsymbol{v} \in \mathbb{R}^n$ is a **stationary point** / **equilibrium point** / **fixed point** of the [autonomous system](./Autonomous%20Systems.md)
>
>$$\boldsymbol{y}' = f(\boldsymbol{y})$$
>
>>[!DEFINITION] Definition: Attractivity
>>
>>We say that $\boldsymbol{v}$ is **attractive** if there exists some $\delta \gt 0$ such that each [solution](../Real%20Ordinary%20Differential%20Equations.md) $\boldsymbol{y}$ with $||\boldsymbol{y}(0) - \boldsymbol{v}|| \lt \delta$ [approaches](../../../Real%20Functions/Limits%20(Real%20Functions).md) $\boldsymbol{v}$ at $+\infty$:
>>
>>$$\lim_{t \to \infty} \boldsymbol{y}(t) = \boldsymbol{v}$$
>>
>
>>[!DEFINITION] Definition: Stability
>>
>>We say that $\boldsymbol{v}$ is **stable** if, for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that for each [solution](../Real%20Ordinary%20Differential%20Equations.md) $\boldsymbol{y}$ with $||\boldsymbol{y}(0) - \boldsymbol{v}|| \lt \delta$, we have $||\boldsymbol{y}(t) - \boldsymbol{v}|| \lt \varepsilon$ for all $t \ge 0$.
>>
>>If $\boldsymbol{v}$ is not [stable](./Autonomous%20Systems.md), then we call it **unstable**.
>>
>
>>[!DEFINITION] Definition: Asymptotic Stability
>>
>>We say that $\boldsymbol{v}$ is **asymptotically stable** if it is both [attractive](./Autonomous%20Systems.md) and [stable](./Autonomous%20Systems.md)
>>
>

>[!THEOREM] Theorem: Attractivity $\implies$ Stability with One Equation
>
>Consider the [autonomous system](./Autonomous%20Systems.md) with just a single [ordinary differential equation](../Real%20Ordinary%20Differential%20Equations.md)
>
>$$y' = f(y)$$
>
>and let $v \in \mathbb{R}$ be a [stationary point](./Autonomous%20Systems.md).
>
>If $v$ is [attractive](./Autonomous%20Systems.md), then it is also [stable](./Autonomous%20Systems.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

[Stationary points](./Autonomous%20Systems.md) are called

>[!THEOREM] Theorem: Attractivity $\implies$ Stability with One Equation
>
>Consider the [autonomous system](./Autonomous%20Systems.md) with just a single [ordinary differential equation](../Real%20Ordinary%20Differential%20Equations.md)
>
>$$y' = f(y)$$
>
>and let $v \in \mathbb{R}$ be a [stationary point](./Autonomous%20Systems.md).
>
>If $v$ is [attractive](./Autonomous%20Systems.md), then it is also [stable](./Autonomous%20Systems.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]
>
>Consider the [autonomous system](./Autonomous%20Systems.md)
>
>$$\boldsymbol{y}' = f(\boldsymbol{y})$$
>
>with a [continuously differentiable](../../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) [real vector field](../../../Real%20Vector%20Fields/Real%20Vector%20Fields.md) $f: \mathbb{R}^n \to \mathbb{R}^n$ and a [stationary point](./Autonomous%20Systems.md) $\boldsymbol{v} \in \mathbb{R}^n$. Let $\lambda_1, \dotsc, \lambda_n \in \mathbb{C}$ be the [eigenvalues](../../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) of the [Jacobian matrix](../../../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md) $\boldsymbol{J}_f(\boldsymbol{v})$ as a [complex matrix](../../../../../Algebra/Matrices/Complex%20Matrices/Complex%20Matrices.md).
>
>If $\operatorname{Re}(\lambda_i) \lt 0$ for all $i \in \{1, \dotsc, n\}$, then $\boldsymbol{v}$ is [asymptotically stable](./Autonomous%20Systems.md).
>
>If there exists some $j \in \{1, \dotsc, n\}$ with $\operatorname{Re}(\lambda_j) \gt 0$, then $\boldsymbol{v}$ is [unstable](./Autonomous%20Systems.md).
>
>>[!EXAMPLE]-
>>
>>Consider the following [autonomous system](./Autonomous%20Systems.md):
>>
>>$$\boldsymbol{y}' = \begin{bmatrix} y_1 + y_2 + 2 \\ y_2 - y_1^2 + 4 \end{bmatrix}$$
>>
>>To find the [stationary points](./Autonomous%20Systems.md), we solve
>>
>>$$\begin{bmatrix} y_1 + y_2 + 2 \\ y_2 - y_1^2 + 4 \end{bmatrix} = \begin{bmatrix}0 \\ 0\end{bmatrix}$$
>>
>>and obtain:
>>
>>$$\boldsymbol{v} = \begin{bmatrix} -2 \\ 0 \end{bmatrix} \qquad \boldsymbol{w} = \begin{bmatrix} 1 \\ -3 \end{bmatrix}$$
>>
>>We get the following [Jacobian matrices](../../../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md):
>>
>>$$\boldsymbol{J}_f (\boldsymbol{v}) = \begin{bmatrix} 1 & 1 \\ 4 & 1 \end{bmatrix} \qquad \boldsymbol{J}_f (\boldsymbol{w}) = \begin{bmatrix} 1 & 1 \\ -2 & 1 \end{bmatrix}$$
>>
>>We see that $\boldsymbol{J}_f (\boldsymbol{v})$ has the [eigenvalues](../../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) $-1$ and $3$ and since $\operatorname{Re}(3) = 3 \gt 0$, we know that $\boldsymbol{v}$ must be [unstable](./Autonomous%20Systems.md).
>>
>>We see that $\boldsymbol{J}_f (\boldsymbol{w})$ has the [eigenvalues](../../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) $1 \pm \mathrm{i}\sqrt{2}$, and since $\operatorname{Re}(1 + \mathrm{i}\sqrt{2}) = 1 \gt 0$, we know that $\boldsymbol{w}$ must also be [unstable](./Autonomous%20Systems.md).
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

