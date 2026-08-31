---
tags:
    - algebra
    - real-analysis
    - analysis
    - mathematics
---

# Equilibrium Point

>[!DEFINITION] Definition: Equilibrium Point
>
>Let $\dot{\boldsymbol{x}} = f(\boldsymbol{x})$ be an [autonomous](./Autonomous%20Systems.md) [system](../System%20of%20Real%20Ordinary%20Differential%20Equations.md) of $n$ equations.
>
>An **equilibrium point** is any $\boldsymbol{x}_{\text{eq}} \in \mathbb{R}^n$ such that $f(\boldsymbol{x}_{\text{eq}}) = \boldsymbol{0}$.
>
>>[!NOTATION]
>>
>>[Equilibrium points](./Equilibrium%20Point.md) are sometimes denoted using $\infty$ as a subscript: $\boldsymbol{x}_{\infty}$, $\boldsymbol{x}_{\infty,1}$, $\boldsymbol{x}_{\infty,2}$, etc.
>>
>
>>[!NOTE]
>>
>>[Equilibrium points](./Equilibrium%20Point.md) are also known as **stationary points** or **fixed points**.
>>
>

>[!THEOREM] Theorem: Behavior after Stationary Points
>
>Let $\dot{\boldsymbol{x}} = f(\boldsymbol{x})$ be an [autonomous](./Autonomous%20Systems.md) [system](../System%20of%20Real%20Ordinary%20Differential%20Equations.md) of $n$ equations, let $\boldsymbol{x}_{\text{eq}} \in \mathbb{R}^n$ be an [equilibrium point](./Equilibrium%20Point.md) and let $\boldsymbol{\phi}$ be a [solution](../System%20of%20Real%20Ordinary%20Differential%20Equations.md) on some [interval](../../../../../Set%20Theory/Orderings/Interval.md) $I \subseteq \mathbb{R}$.
>
>If $f$ is [locally Lipschitz continuous](TODO) at $\boldsymbol{x}_{\text{eq}}$ and there exists some $t_{\text{eq}} \in I$ with $\boldsymbol{\phi}(t_{\text{eq}}) = \boldsymbol{x}_{\text{eq}}$, then $\boldsymbol{\phi}(t) = \boldsymbol{x}_{\text{eq}}$ for all $t \in I$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Stability

>[!DEFINITION] Definition: Attractivity
>
>Let $\dot{\boldsymbol{x}} = f(\boldsymbol{x})$ be an [autonomous](./Autonomous%20Systems.md) [system](../System%20of%20Real%20Ordinary%20Differential%20Equations.md) of $n$ equations.
>
>An [equilibrium point](./Equilibrium%20Point.md) $\boldsymbol{x}_{\text{eq}} \in \mathbb{R}^n$ is **attractive** if it has some [neighborhood](../../../../../Topology/Topological%20Spaces/Neighborhoods.md) $N \subseteq \mathbb{R}^n$ such that if $\boldsymbol{\phi}(t)$ is a [solution](../System%20of%20Real%20Ordinary%20Differential%20Equations.md) on some [interval](../../../../../Set%20Theory/Orderings/Interval.md) $[t_0,\infty)$ with $\boldsymbol{\phi}(t_0) \in N$, then the [limit](../../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Limits%20of%20Parametric%20Curves.md) of $\boldsymbol{\phi}(t)$ at $\infty$ is $\boldsymbol{x}_{\text{eq}}$:
>
>$$\lim_{t \to \infty} \boldsymbol{\phi}(t) = \boldsymbol{x}_{\text{eq}}$$
>

>[!DEFINITION] Definition: Stability
>
>Let $\dot{\boldsymbol{x}} = f(\boldsymbol{x})$ be an [autonomous](./Autonomous%20Systems.md) [system](../System%20of%20Real%20Ordinary%20Differential%20Equations.md) of $n$ equations.
>
>An [equilibrium point](./Equilibrium%20Point.md) $\boldsymbol{x}_{\text{eq}} \in \mathbb{R}^n$ is **stable** if for every [neighborhood](../../../../../Topology/Topological%20Spaces/Neighborhoods.md) $U \subseteq \mathbb{R}^n$ of $\boldsymbol{x}_{\text{eq}}$, there exists a smaller [neighborhood](../../../../../Topology/Topological%20Spaces/Neighborhoods.md) $V \subseteq U$ of $\boldsymbol{x}_{\text{eq}}$ such that if $\boldsymbol{\phi}(t)$ is a [solution](../System%20of%20Real%20Ordinary%20Differential%20Equations.md) on some [interval](../../../../../Set%20Theory/Orderings/Interval.md) $[t_0,\infty)$ with $\boldsymbol{\phi}(t_0) \in V$, then $\boldsymbol{\phi}(t) \in U$ for all $t \ge t_0$:
>
>$$\boldsymbol{\phi}(t) \in U \quad \forall t \ge t_0$$
>
>>[!NOTE]
>>
>>This concept is commonly called **Lyapunov stability**. If $\boldsymbol{x}_{\text{eq}}$ is not [stable](./Equilibrium%20Point.md), then it is often called **unstable**.
>>
>

>[!DEFINITION] Definition: Asymptotic Stability
>
>Let $\dot{\boldsymbol{x}} = f(\boldsymbol{x})$ be an [autonomous](./Autonomous%20Systems.md) [system](../System%20of%20Real%20Ordinary%20Differential%20Equations.md) of $n$ equations.
>
>An [equilibrium point](./Equilibrium%20Point.md) is **asymptotically stable** if it is both [attractive](./Equilibrium%20Point.md) and [stable](./Equilibrium%20Point.md).
>

>[!THEOREM] Theorem: Lyapunov's Indirect Method
>
>Let $\dot{\boldsymbol{x}} = f(\boldsymbol{x})$ be an [autonomous](./Autonomous%20Systems.md) [system](../System%20of%20Real%20Ordinary%20Differential%20Equations.md) of $n$ equations and let $\boldsymbol{x}_{\text{eq}} \subseteq \mathbb{R}^n$ be an [equilibrium point](./Equilibrium%20Point.md). 
>
>Suppose that there exists some [neighborhood](../../../../../Topology/Topological%20Spaces/Neighborhoods.md) of $\boldsymbol{x}_{\text{eq}}$ on which $f$ is [continuously differentiable](../../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) and let $\lambda_1, \dotsc, \lambda_n \in \mathbb{C}$ be the [eigenvalues](../../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) of the [Jacobian matrix](../../../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md) $\boldsymbol{J}_f(\boldsymbol{x}_{\text{eq}})$ as a [complex matrix](../../../../../Algebra/Matrices/Complex%20Matrices/Complex%20Matrices.md):
>
>    - If the [real part](../../../../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md) of each $\lambda \in \{\lambda_1, \dotsc, \lambda_n\}$ is strictly negative, then $\boldsymbol{x}_{\text{eq}}$ is [asymptotically stable](./Equilibrium%20Point.md).
>    - If there is some $\lambda \in \{\lambda_1, \dotsc, \lambda_n\}$ whose [real part](../../../../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md) is strictly positive, then $\boldsymbol{x}_{\text{eq}}$ is [unstable](./Equilibrium%20Point.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Lyapunov's Indirect Method for Linear Systems
>
>Let $\dot{\boldsymbol{x}} = \boldsymbol{A}\boldsymbol{x} + \boldsymbol{b}$ be an [autonomous](./Autonomous%20Systems.md) [system](../System%20of%20Real%20Ordinary%20Differential%20Equations.md) of $n$ equations with some [real matrix](../../../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ and some [real vector](../../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $\boldsymbol{b} \in \mathbb{R}^n$ and let $\boldsymbol{x}_{\text{eq}} \subseteq \mathbb{R}^n$ be an [equilibrium point](./Equilibrium%20Point.md). Let $\lambda_1, \dotsc, \lambda_n \in \mathbb{C}$ be the [eigenvalues](../../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) of $\boldsymbol{A}$ as a [complex matrix](../../../../../Algebra/Matrices/Complex%20Matrices/Complex%20Matrices.md).
>
>The [equilibrium point](./Equilibrium%20Point.md) $\boldsymbol{x}_{\text{eq}}$ is [asymptotically stable](./Equilibrium%20Point.md) if and only if each $\lambda \in \{\lambda_1, \dotsc, \lambda_n\}$ has a strictly negative [real part](../../../../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md).
>
>If there exists some $\lambda \in \{\lambda_1, \dotsc, \lambda_n\}$ whose [real part](../../../../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md) is strictly positive, then $\boldsymbol{x}_{\text{eq}}$ is [unstable](./Equilibrium%20Point.md).
>
>>[!EXAMPLE]-
>>
>>Consider the following [autonomous system](./Autonomous%20Systems.md):
>>
>>$$\boldsymbol{y}' = \underset{\boldsymbol{A}}{\underbrace{\begin{bmatrix} -1 & 0 \\ 0 & -2 \end{bmatrix}}}\boldsymbol{y}$$
>>
>>We see that $\boldsymbol{v} = \boldsymbol{0}$ is a [stationary point](./Autonomous%20Systems.md).
>>
>>The [eigenvalues](../../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) of $\boldsymbol{A}$ are $-1$ and $-2$. Therefore, $\boldsymbol{v}$ is [asymptotically stable](./Autonomous%20Systems.md).
>>
>
>>[!EXAMPLE]-
>>
>>Consider the following [autonomous system](./Autonomous%20Systems.md):
>>
>>$$\boldsymbol{y}' = \underset{\boldsymbol{A}}{\underbrace{\begin{bmatrix} 1 & 0 \\ 0 & -2 \end{bmatrix}}}\boldsymbol{y}$$
>>
>>We see that $\boldsymbol{v} = \boldsymbol{0}$ is a [stationary point](./Autonomous%20Systems.md).
>>
>>The [eigenvalues](../../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) of $\boldsymbol{A}$ are $1$ and $-2$. Therefore, $\boldsymbol{v}$ is [unstable](./Autonomous%20Systems.md), since $\operatorname{Re}(1) = 1 \gt 0$.
>>
>
>>[!EXAMPLE]-
>>
>>Consider the following [autonomous system](./Autonomous%20Systems.md):
>>
>>$$\boldsymbol{y}' = \underset{\boldsymbol{A}}{\underbrace{\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}}}\boldsymbol{y}$$
>>
>>We see that $\boldsymbol{v} = \boldsymbol{0}$ is a [stationary point](./Autonomous%20Systems.md).
>>
>>The [eigenvalues](../../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) of $\boldsymbol{A}$ are $1$ and $0$. Therefore, $\boldsymbol{v}$ is [unstable](./Autonomous%20Systems.md), since $\operatorname{Re}(1) = 1 \gt 0$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>
