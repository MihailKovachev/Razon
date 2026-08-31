---
tags:
    - real-analysis
    - vector-analysis
    - analysis
    - mathematics
---

# System of Real Ordinary Differential Equations

>[!DEFINITION] Definition: System of Real Ordinary Differential Equations
>
>Let $k, m, n \in \mathbb{N}_{\ge 1}$.
>
>An **$n$-th order system of $m$ ordinary differential equations** is a [function](../../Real%20Vector%20Functions/Real%20Vector%20Functions.md)
>
>$$\boldsymbol{F}: \mathcal{D}_{\boldsymbol{F}} \subseteq \mathbb{R}^{1+k+k\cdot n} \to \mathbb{R}^m$$
>
>which is [dependent](TODO) on at least one of its last $k$ arguments.
>
>>[!NOTATION]
>>
>>Most commonly, a [system of ODEs](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) is written directly using vector notation as follows:
>>
>>$$\boldsymbol{F}(x, \boldsymbol{y}, \boldsymbol{y}', \boldsymbol{y}'', \dotsc, \boldsymbol{y}^{(n)}) = \boldsymbol{0}$$
>>
>>where $\boldsymbol{y} = (y_1, y_2, \dotsc, y_m)^T$ is a vector of unknown functions.
>>
>

>[!DEFINITION] Definition: Explicit System of Real Ordinary Differential Equations
>
>Let $m, n \in \mathbb{N}_{\ge 1}$.
>
>An **explicit $n$-th order system of $m$ real ordinary differential equations** is an [$n$-th order system of $m$ real ordinary differential equations](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) $\boldsymbol{F}: \mathcal{D}_{\boldsymbol{F}} \subseteq \mathbb{R}^{1+m+m\cdot n} \to \mathbb{R}^m$ such that there exists a [function](../../Real%20Vector%20Functions/Real%20Vector%20Functions.md) $\boldsymbol{f}: \mathcal{D}_\boldsymbol{f} \subseteq \mathbb{R}^{1+m+m\cdot(n-1)} \to \mathbb{R}^m$ with
>
>$$\boldsymbol{F}(x, \boldsymbol{y}_0, \boldsymbol{y}_1, \dotsc, \boldsymbol{y}_n) = \boldsymbol{y}_n - \boldsymbol{f}(x, \boldsymbol{y}_0, \boldsymbol{y}_1, \dotsc, \boldsymbol{y}_{n-1})$$
>
>for all $(x, \boldsymbol{y}_0, \boldsymbol{y}_1, \dotsc, \boldsymbol{y}_n) \in \mathcal{D}_\boldsymbol{F}$.
>

## Solutions

>[!DEFINITION] Definition: Solution (System of Real Ordinary Differential Equations)
>
>Let $k, m, n \in \mathbb{N}_{\ge 1}$ and let $\boldsymbol{F}: \mathcal{D}_{\boldsymbol{F}} \subseteq \mathbb{R}^{1+k+k\cdot n} \to \mathbb{R}^m$ be a [system of real ordinary differential equations](./System%20of%20Real%20Ordinary%20Differential%20Equations.md). Let $S \subseteq \mathbb{R}$.
>
>A **solution** of $\boldsymbol{F}(\cdot) = \boldsymbol{0}$ is any [function](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\boldsymbol{\phi}: \mathcal{D}_{\boldsymbol{\phi}} \subseteq \mathbb{R} \to \mathbb{R}^k$ which is [$n$-times differentiable](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md#Higher%20Order%20Differentiability) on $S$ with
>
>$$\boldsymbol{F}\left(t, \boldsymbol{\phi}(t), \boldsymbol{\phi}'(t), \boldsymbol{\phi}''(t), \dotsc, \boldsymbol{\phi}^{(n)}(t)\right) = \boldsymbol{0}$$
>
>for all $t \in S$.
>

>[!DEFINITION] Definition: Weak Solution
>
>Let $k, m, n \in \mathbb{N}_{\ge 1}$, let $\boldsymbol{F}: \mathcal{D}_{\boldsymbol{F}} \subseteq \mathbb{R}^{1+k+k\cdot n} \to \mathbb{R}^m$ be a [system of real ordinary differential equations](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) and let $S \subseteq \mathbb{R}$.
>
>A **weak solution** of $\boldsymbol{F}(\cdot) = \boldsymbol{0}$ is any [function](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\boldsymbol{\phi}: \mathcal{D}_{\boldsymbol{\phi}} \subseteq \mathbb{R} \to \mathbb{R}^k$ which has [weak derivatives](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Weak%20Derivatives%20(Real%20Parametric%20Curves).md) $\boldsymbol{\phi}', \boldsymbol{\phi}'', \dotsc, \boldsymbol{\phi}^{(n)}$ on $S$ and for which there exists a [null set](../../../../Measure%20Theory/Null%20Sets.md) $N \subseteq S$ of the [Lebesgue measure](../../../../Measure%20Theory/Lebesgue%20Measure.md) such that
>
>$$\boldsymbol{F}\left(x, \boldsymbol{\phi}(x), \boldsymbol{\phi}'(x), \boldsymbol{\phi}''(x), \dotsc, \boldsymbol{\phi}^{(n)}(x)\right) = \boldsymbol{0}$$
>
>for all $x \in S \setminus N$. TODO
>

>[!THEOREM] Theorem: Homogeneous Linear System
>
>Consider the [initial value problem](./System%20of%20Real%20Ordinary%20Differential%20Equations.md)
>
>$$\boldsymbol{y}'(t) = \boldsymbol{A} \boldsymbol{y}(t) \qquad \boldsymbol{y}(t_0) = \boldsymbol{y}_0$$
>
>with the [real](../../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) [square matrix](../../../../Algebra/Matrices/Square%20Matrices/Square%20Matrices.md) $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ and the [initial condition](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) $t_0 \in \mathbb{R}$, $\boldsymbol{y}_0 \in \mathbb{R}^n$. It has the following a unique [solution](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) on $\mathbb{R}$ given by a [matrix exponential](../../../Functional%20Analysis/Matrix%20Functions/Matrix%20Exponential.md):
>
>$$\boldsymbol{y}(t) = \mathrm{e}^{(t - t_0)\boldsymbol{A}}\boldsymbol{y}_0$$
>
>>[!EXAMPLE]-
>>
>>Consider the following [initial value problem](./System%20of%20Real%20Ordinary%20Differential%20Equations.md):
>>
>>$$\boldsymbol{y}'(t) = \begin{bmatrix}1 & 2 \\ 2 & 1\end{bmatrix} \boldsymbol{y}(t) \qquad \boldsymbol{y}(0) = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$$
>>
>>We have:
>>
>>$$\boldsymbol{A} = \begin{bmatrix}1 & 2 \\ 2 & 1\end{bmatrix} \qquad t_0 = 0 \qquad \boldsymbol{y}_0 = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$$
>>
>>Its unique [solution](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) on $\mathbb{R}$ is the following:
>>
>>$$\boldsymbol{y}(t) = \mathrm{e}^{(t - t_0)\boldsymbol{A}}\boldsymbol{y}_0 = \mathrm{e}^{t\boldsymbol{A}}\begin{bmatrix} 2 \\ 3 \end{bmatrix}$$
>>
>>We know that $\boldsymbol{A}$ is [diagonalizable](../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md). Specifically:
>>
>>$$\boldsymbol{A} = \begin{bmatrix}1 & 1 \\ 1 & -1\end{bmatrix} \begin{bmatrix}3 & 0 \\ 0 & - 1\end{bmatrix}\begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & - \frac{1}{2}\end{bmatrix}$$
>>
>>Therefore, $t\boldsymbol{A}$ is also [diagonalizable](../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md):
>>
>>$$t\boldsymbol{A} = \begin{bmatrix}1 & 1 \\ 1 & -1\end{bmatrix} \begin{bmatrix}3t & 0 \\ 0 & - 1t\end{bmatrix}\begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & - \frac{1}{2}\end{bmatrix}$$
>>
>>The [matrix exponential](../../../Functional%20Analysis/Matrix%20Functions/Matrix%20Exponential.md) $\mathrm{e}^{t\boldsymbol{A}}$ can thus be calculated using the [real exponential](../../Real%20Functions/Real%20Exponentiation.md) as follows:
>>
>>$$\mathrm{e}^{t\boldsymbol{A}} = \begin{bmatrix}1 & 1 \\ 1 & -1\end{bmatrix} \begin{bmatrix}\mathrm{e}^{3t} & 0 \\ 0 & \mathrm{e}^{-1t}\end{bmatrix}\begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & - \frac{1}{2}\end{bmatrix} = \frac{1}{2}\begin{bmatrix} \mathrm{e}^{3t} + \mathrm{e}^{-t} & \mathrm{e}^{3t} - \mathrm{e}^{-t} \\ \mathrm{e}^{3t} - \mathrm{e}^{-t} & \mathrm{e}^{3t} + \mathrm{e}^{-t}\end{bmatrix}$$
>>
>>We thus have:
>>
>>$$\boldsymbol{y}(t) = \frac{1}{2}\begin{bmatrix} \mathrm{e}^{3t} + \mathrm{e}^{-t} & \mathrm{e}^{3t} - \mathrm{e}^{-t} \\ \mathrm{e}^{3t} - \mathrm{e}^{-t} & \mathrm{e}^{3t} + \mathrm{e}^{-t}\end{bmatrix}\begin{bmatrix} 2 \\ 3 \end{bmatrix} = \frac{1}{2}\begin{bmatrix} 5\mathrm{e}^{3t} - \mathrm{e}^{-t} \\ 5 \mathrm{e}^{3t} + \mathrm{e}^{-t}\end{bmatrix}$$
>>
>
>>[!EXAMPLE]-
>>
>>Consider the following [initial value problem](./System%20of%20Real%20Ordinary%20Differential%20Equations.md):
>>
>>$$\boldsymbol{y}'(t) = \begin{bmatrix}1 & 2 \\ 0 & 1\end{bmatrix} \boldsymbol{y}(t) \qquad \boldsymbol{y}(0) = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$$
>>
>>We have:
>>
>>$$\boldsymbol{A} = \begin{bmatrix}1 & 2 \\ 0 & 1\end{bmatrix} \qquad t_0 = 0 \qquad \boldsymbol{y}_0 = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$$
>>
>>Its unique [solution](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) on $\mathbb{R}$ is the following:
>>
>>$$\boldsymbol{y}(t) = \mathrm{e}^{(t - t_0)\boldsymbol{A}}\boldsymbol{y}_0 = \mathrm{e}^{t\boldsymbol{A}}\begin{bmatrix} 2 \\ 3 \end{bmatrix}$$
>>
>>We can express $t\boldsymbol{A}$ as follows:
>>
>>$$t\boldsymbol{A} = t\boldsymbol{I}_2 + t\boldsymbol{B} \qquad \boldsymbol{B} = \begin{bmatrix}0 & 2 \\ 0 & 0\end{bmatrix}$$
>>
>>For the [matrix exponential](../../../Functional%20Analysis/Matrix%20Functions/Matrix%20Exponential.md), we get:
>>
>>$$\mathrm{e}^{t\boldsymbol{A}} = \mathrm{e}^{t\boldsymbol{I}_2 + t\boldsymbol{B}} = \mathrm{e}^{t\boldsymbol{I}_2} \mathrm{e}^{t \boldsymbol{B}} = \mathrm{e}^{t} \boldsymbol{I}_2 \mathrm{e}^{t \boldsymbol{B}} = \mathrm{e}^{t}\mathrm{e}^{t \boldsymbol{B}}$$
>> 
>>Since $(t\boldsymbol{B})^2 = (t\boldsymbol{B})^3 = \cdots = \boldsymbol{0}$, we get:
>>
>>$$\mathrm{e}^{t \boldsymbol{B}} = \boldsymbol{I} + t\boldsymbol{B}$$
>>
>>Therefore:
>>
>>$$\mathrm{e}^{t\boldsymbol{A}} = \mathrm{e}^{t}(\boldsymbol{I} + t\boldsymbol{B}) = \mathrm{e}^{t} \begin{bmatrix}1 & 2t \\ 0 & 1\end{bmatrix}$$
>>
>>Finally:
>>
>>$$\boldsymbol{y}(t) = \mathrm{e}^{t} \begin{bmatrix}1 & 2t \\ 0 & 1\end{bmatrix}\begin{bmatrix} 2 \\ 3 \end{bmatrix} = \mathrm{e}^{t} \begin{bmatrix} 2 + 6t \\ 3 \end{bmatrix}$$
>>
>
>>[!EXAMPLE]-
>>
>>Consider the following [initial value problem](./System%20of%20Real%20Ordinary%20Differential%20Equations.md):
>>
>>$$\boldsymbol{y}'(t) = \begin{bmatrix}a & -b \\ b & a\end{bmatrix} \boldsymbol{y}(t), b \ne 0 \qquad \boldsymbol{y}(0) = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$$
>>
>>Its unique [solution](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) on $\mathbb{R}$ is the following:
>>
>>$$\boldsymbol{y}(t) = \mathrm{e}^{(t - t_0)\boldsymbol{A}}\boldsymbol{y}_0 = \mathrm{e}^{t\boldsymbol{A}}\begin{bmatrix} 2 \\ 3 \end{bmatrix}$$
>>
>>We can express $\boldsymbol{A}$ as follows:
>>
>>$$\boldsymbol{A} = a\boldsymbol{I}_2 + \boldsymbol{B} \qquad \boldsymbol{B} = \begin{bmatrix}0 & -b \\ b & 0\end{bmatrix}$$
>>
>>For the [matrix exponential](../../../Functional%20Analysis/Matrix%20Functions/Matrix%20Exponential.md) $\mathrm{e}^{t\boldsymbol{A}}$, we get:
>>
>>$$\mathrm{e}^{t\boldsymbol{A}} = \mathrm{e}^{ta\boldsymbol{I}_2 + t\boldsymbol{B}} = \mathrm{e}^{at\boldsymbol{I}_2} \mathrm{e}^{t \boldsymbol{B}} = \mathrm{e}^{at} \boldsymbol{I}_2 \mathrm{e}^{t \boldsymbol{B}} = \mathrm{e}^{at}\mathrm{e}^{t \boldsymbol{B}}$$
>>
>>We have:
>>
>>$$\boldsymbol{B}^2 = \begin{bmatrix}0 & -b \\ b & 0\end{bmatrix}\begin{bmatrix}0 & -b \\ b & 0\end{bmatrix} = -b^2 \boldsymbol{I}_2$$
>>
>>Therefore:
>>
>>$$\boldsymbol{B}^{2k} = (\boldsymbol{B}^2)^k = (-1)^k b^{2k} \boldsymbol{I}_2 \qquad \boldsymbol{B}^{2k + 1} = (-1)^k b^{2k} \boldsymbol{B} = (-1)^k \begin{bmatrix} 0 & -b^{2k + 1} \\ b^{2k+1} & 0 \end{bmatrix}$$
>>
>>Accordingly:
>>
>>$$(t\boldsymbol{B})^{2k} = (-1)^k t^2k b^{2k} \boldsymbol{I}_2 \qquad \boldsymbol{B}^{2k + 1} = (-1)^k \begin{bmatrix} 0 & -(tb)^{2k + 1} \\ (tb)^{2k+1} & 0 \end{bmatrix}$$
>>
>>The [matrix exponential](../../../Functional%20Analysis/Matrix%20Functions/Matrix%20Exponential.md) $\mathrm{e}^{t\boldsymbol{B}}$ can thus be expressed in terms of the [real sine function](../../Real%20Functions/Real%20Trigonometric%20Functions/Real%20Trigonometric%20Functions.md) and the [real cosine function](../../Real%20Functions/Real%20Trigonometric%20Functions/Real%20Trigonometric%20Functions.md):
>>
>>$$\begin{aligned} \mathrm{e}^{t\boldsymbol{B}} & = \sum_{k = 0}^{\infty} \frac{1}{k!} \boldsymbol{B}^k \\ & = \sum_{k = 0}^{\infty} \frac{1}{(2k)!}(-1)^k (tb)^{2k} \boldsymbol{I}_2 + \sum_{k = 0}^{\infty} \frac{1}{(2k+1)!}(-1)^k \begin{bmatrix} 0 & -(tb)^{2k + 1} \\ (tb)^{2k+1} & 0 \end{bmatrix} \\ & = \sum_{k = 0}^{\infty} \frac{1}{(2k)!}(-1)^k (tb)^{2k} \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} + \sum_{k = 0}^{\infty} \frac{1}{(2k+1)!}(-1)^k \begin{bmatrix} 0 & -(tb)^{2k + 1} \\ (tb)^{2k+1} & 0 \end{bmatrix} \\ & = \begin{bmatrix} \sum_{k = 0}^{\infty} \frac{(-1)^k}{(2k)!} (tb)^{2k} & 0 \\ 0 & \sum_{k = 0}^{\infty} \frac{(-1)^k}{(2k)!} (tb)^{2k} \end{bmatrix} + \begin{bmatrix} 0 & -\sum_{k = 0}^{\infty} \frac{(-1)^k}{(2k+1)!} (tb)^{2k + 1} \\ \sum_{k = 0}^{\infty} \frac{(-1)^k}{(2k+1)!} (tb)^{2k+1} & 0 \end{bmatrix} \\ & = \begin{bmatrix}\cos(tb) & 0 \\ 0 & \cos(tb)\end{bmatrix} + \begin{bmatrix}0 & - \sin (tb) \\ \sin (tb) & 0\end{bmatrix} \\ & = \begin{bmatrix} \cos(bt) & - \sin (bt) \\ \sin (bt) & \cos (bt) \end{bmatrix}\end{aligned}$$
>>
>>Finally:
>>
>>$$\begin{aligned}\boldsymbol{y}(t) & = \mathrm{e}^{t\boldsymbol{A}}\begin{bmatrix} 2 \\ 3\end{bmatrix} \\ & = \mathrm{e}^{at}\mathrm{e}^{t \boldsymbol{B}} \begin{bmatrix}2 \\ 3\end{bmatrix} \\ & = \mathrm{e}^{at} \begin{bmatrix} \cos(bt) & - \sin (bt) \\ \sin (bt) & \cos (bt) \end{bmatrix} \begin{bmatrix}2 \\ 3\end{bmatrix} \\ & = \mathrm{e}^{at} \begin{bmatrix} 2\cos(bt) - 3\sin(bt) \\ 2\sin(bt) + 3\cos(bt) \end{bmatrix} \end{aligned}$$
>>
>
>>[!EXAMPLE]- Example: Diagonalizability
>>
>>Consider the [initial value problem](./System%20of%20Real%20Ordinary%20Differential%20Equations.md)
>>
>>$$\boldsymbol{y}'(t) = \boldsymbol{A} \boldsymbol{y}(t) \qquad \boldsymbol{y}(t_0) = \boldsymbol{y}_0$$
>>
>>with the [real](../../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) [square matrix](../../../../Algebra/Matrices/Square%20Matrices/Square%20Matrices.md) $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ and the [initial condition](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) $t_0 \in \mathbb{R}$, $\boldsymbol{y}_0 \in \mathbb{R}^n$.
>>
>>Its unique [solution](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) on $\mathbb{R}$ is the following:
>>
>>$$\boldsymbol{y}(t) = \mathrm{e}^{(t - t_0)\boldsymbol{A}}\boldsymbol{y}_0$$
>>
>>If $\boldsymbol{A}$ is [diagonalizable](../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md), then it can be expressed as
>>
>>$$\boldsymbol{A} = \boldsymbol{P} \boldsymbol{D} \boldsymbol{P}^{-1} = \begin{bmatrix} \vert & \vert & \vert \\ \boldsymbol{v}_1 & \cdots & \boldsymbol{v}_n \\ \vert & \vert & \vert \end{bmatrix} \begin{bmatrix} \lambda_1 & 0 & \cdots & 0 \\ 0 & \lambda_2 & \ddots & \vdots \\ \vdots & \ddots & \ddots & \vdots \\ 0 & \cdots & 0 & \lambda_n \end{bmatrix} \begin{bmatrix} \vert & \vert & \vert \\ \boldsymbol{v}_1 & \cdots & \boldsymbol{v}_n \\ \vert & \vert & \vert \end{bmatrix}^{-1},$$
>>
>>where $\lambda_1, \dotsc, \lambda_n$ are the (not necessarily unique) [eigenvalues](../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) of $\boldsymbol{A}$ and $\boldsymbol{v}_1, \dotsc, \boldsymbol{v}_n$ are [eigenvectors](../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) from the corresponding [eigenspaces](../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md). The [matrix exponential](../../../Functional%20Analysis/Matrix%20Functions/Matrix%20Exponential.md) can thus be rewritten as follows:
>>
>>$$\mathrm{e}^{(t-t_0)\boldsymbol{A}} = \boldsymbol{P} \mathrm{e}^{(t-t_0)\boldsymbol{D}} \boldsymbol{P}^{-1}$$
>>
>>
>>Since $\boldsymbol{v}_1, \dotsc, \boldsymbol{v}_n$ form a [basis](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) for $\mathbb{R}^n$, we can express $\boldsymbol{y}_0$ as a [linear combination](../../../../Algebra/Vector%20Spaces/Linear%20Combinations.md):
>>
>>$$\boldsymbol{y}_0 = c_1 \boldsymbol{v}_1 + \cdots + c_n \boldsymbol{v}_n$$
>>
>>If we let $\boldsymbol{c} = \begin{bmatrix}c_1 & \cdots & c_n\end{bmatrix}^{\mathsf{T}}$, we get:
>>
>>$$\boldsymbol{y}_0 = \begin{bmatrix} \vert & \vert & \vert \\ \boldsymbol{v}_1 & \cdots & \boldsymbol{v}_n \\ \vert & \vert & \vert \end{bmatrix} \begin{bmatrix}c_1 \\ \vdots \\ c_n\end{bmatrix} = \boldsymbol{P}\boldsymbol{c}$$
>>
>>Therefore:
>>
>>$$\begin{aligned}\boldsymbol{y}(t) & = \mathrm{e}^{(t - t_0)\boldsymbol{A}}\boldsymbol{y}_0 \\ & = \boldsymbol{P} \mathrm{e}^{(t-t_0)\boldsymbol{D}} \boldsymbol{P}^{-1} \boldsymbol{P}\boldsymbol{c} \\ & = \boldsymbol{P} \mathrm{e}^{(t-t_0)\boldsymbol{D}}\boldsymbol{c} \\ & = \begin{bmatrix} \vert & \vert & \vert \\ \boldsymbol{v}_1 & \cdots & \boldsymbol{v}_n \\ \vert & \vert & \vert \end{bmatrix} \begin{bmatrix} \mathrm{e}^{\lambda_1(t-t_0)} & 0 & \cdots & 0 \\ 0 & \mathrm{e}^{\lambda_2(t-t_0)} & \ddots & \vdots \\ \vdots & \ddots & \ddots & \vdots \\ 0 & \cdots & 0 & \mathrm{e}^{\lambda_n(t-t_0)} \end{bmatrix} \begin{bmatrix}c_1 \\ \vdots \\ c_n\end{bmatrix} \\ & = \begin{bmatrix} \vert & \vert & \vert \\ \boldsymbol{v}_1 & \cdots & \boldsymbol{v}_n \\ \vert & \vert & \vert \end{bmatrix} \begin{bmatrix} \mathrm{e}^{\lambda_1 (t-t_0)}c_1 \\ \vdots \\ \mathrm{e}^{\lambda_n (t-t_0)}c_n\end{bmatrix} \\ & = \mathrm{e}^{\lambda_1 (t-t_0)}c_1 \boldsymbol{v}_1 + \cdots + \mathrm{e}^{\lambda_n (t-t_0)}c_n \boldsymbol{v}_n\end{aligned}$$
>>
>
>>[!EXAMPLE]- Example: Diagonalizability over the Complex Numbers
>>
>>Consider the following [system](./System%20of%20Real%20Ordinary%20Differential%20Equations.md)
>>
>>$$\boldsymbol{y}'(t) = \boldsymbol{A} \boldsymbol{y}(t)$$
>>
>>with the [real](../../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) [square matrix](../../../../Algebra/Matrices/Square%20Matrices/Square%20Matrices.md) $\boldsymbol{A} \in \mathbb{R}^{n \times n}$.
>>
>>If $\boldsymbol{A}$ is *not* [diagonalizable](../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) as a [real matrix](../../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md), but *is* [diagonalizable](../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) as a [complex matrix](../../../../Algebra/Matrices/Complex%20Matrices/Complex%20Matrices.md), then we can generate a [basis](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) for its [solution space](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) as follows:
>>
>>Each [real](../../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) 
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Inhomogeneous Linear System
>
>Consider the [initial value problem](./System%20of%20Real%20Ordinary%20Differential%20Equations.md)
>
>$$\boldsymbol{y}'(t) = \boldsymbol{A} \boldsymbol{y}(t) + f(t) \qquad \boldsymbol{y}(t_0) = \boldsymbol{y}_0$$
>
>with the [real](../../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) [square matrix](../../../../Algebra/Matrices/Square%20Matrices/Square%20Matrices.md) $\boldsymbol{A} \in \mathbb{R}^{n \times n}$, the [initial condition](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) $t_0 \in \mathbb{R}$, $\boldsymbol{y}_0 \in \mathbb{R}^n$ and the [function](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}^n$. 
>
>If $\mathrm{e}^{(t_0 - \tau)\boldsymbol{A}}f(\tau)$ is [antidifferentiable](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Antidifferentiability%20(Real%20Parametric%20Curves).md) on an [interval](../../Euclidean%20Space/Euclidean%20Space.md) $[t_0, T]$, then there exists a unique [solution](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) on $[t_0, T]$:
>
>$$\boldsymbol{y}(t) = \mathrm{e}^{(t-t_0)\boldsymbol{A}} \left( \boldsymbol{y}_0 + \int_{t_0}^t \mathrm{e}^{(t_0 - \tau)\boldsymbol{A}}f(\tau) \,\mathrm{d}\tau \right)$$
>
>
>>[!EXAMPLE]-
>>
>>Consider the following [initial value problem](./System%20of%20Real%20Ordinary%20Differential%20Equations.md):
>>
>>$$\boldsymbol{y}'(t) = \begin{bmatrix}1 & 2 \\ 2 & 1\end{bmatrix} \boldsymbol{y}(t) + \begin{bmatrix}1 \\ 1\end{bmatrix} \qquad \boldsymbol{y}(0) = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$$
>>
>>We have:
>>
>>$$\boldsymbol{A} = \begin{bmatrix}1 & 2 \\ 2 & 1\end{bmatrix} \qquad f(t) = \begin{bmatrix}1 \\ 1\end{bmatrix} \qquad t_0 = 0 \qquad \boldsymbol{y}_0 = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$$
>>
>>For $\mathrm{e}^{(t_0 - \tau)\boldsymbol{A}}f(\tau)$, we have:
>>
>>$$\begin{aligned}\mathrm{e}^{(t_0 - \tau)\boldsymbol{A}}f(\tau) & = \mathrm{e}^{-\tau \boldsymbol{A}}\begin{bmatrix}1 \\ 1\end{bmatrix} \\ & = \frac{1}{2}\begin{bmatrix}\mathrm{e}^{-3 \tau} + \mathrm{e}^{\tau} & \mathrm{e}^{-3 \tau} - \mathrm{e}^{\tau} \\ \mathrm{e}^{-3\tau} - \mathrm{e}^{\tau} & \mathrm{e}^{-3\tau} + \mathrm{e}^{\tau} \end{bmatrix} \begin{bmatrix}1 \\ 1\end{bmatrix} \\ & = \mathrm{e}^{-3\tau}\begin{bmatrix}1 \\ 1\end{bmatrix}\end{aligned}$$
>>
>>For each $T \gt 0$, we see that $\mathrm{e}^{(t_0 - \tau)\boldsymbol{A}}f(\tau)$ is [antidifferentiable](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Antidifferentiability%20(Real%20Parametric%20Curves).md) on $[0, T]$ and we have:
>>
>>$$\begin{aligned}\int_0^t \mathrm{e}^{(t_0 - \tau)\boldsymbol{A}}f(\tau) \, \mathrm{d}\tau & = \int_0^t \mathrm{e}^{-3\tau} \begin{bmatrix}1 \\ 1\end{bmatrix} \,\mathrm{d}\tau \\ & = \begin{bmatrix}1 \\ 1\end{bmatrix} \int_0^t \mathrm{e}^{-3\tau} \,\mathrm{d}\tau \\ & = -\frac{1}{3}(\mathrm{e}^{-3t} - 1)\begin{bmatrix}1 \\ 1\end{bmatrix} \end{aligned}$$
>>
>>Finally:
>>
>>$$\begin{aligned} \boldsymbol{y}(t) & = \mathrm{e}^{(t-t_0)\boldsymbol{A}} \left( \boldsymbol{y}_0 + \int_{t_0}^t \mathrm{e}^{(t_0 - \tau)\boldsymbol{A}}f(\tau) \,\mathrm{d}\tau \right) \\ & = \frac{1}{2}\begin{bmatrix} \mathrm{e}^{3t} + \mathrm{e}^{-t} & \mathrm{e}^{3t} - \mathrm{e}^{-t} \\ \mathrm{e}^{3t} - \mathrm{e}^{-t} & \mathrm{e}^{3t} + \mathrm{e}^{-t}\end{bmatrix} \left( \begin{bmatrix}2 \\ 3\end{bmatrix} -\frac{1}{3}(\mathrm{e}^{-3t} - 1)\begin{bmatrix}1 \\ 1\end{bmatrix} \right) \\ & = \frac{1}{2}\begin{bmatrix} \mathrm{e}^{3t} + \mathrm{e}^{-t} & \mathrm{e}^{3t} - \mathrm{e}^{-t} \\ \mathrm{e}^{3t} - \mathrm{e}^{-t} & \mathrm{e}^{3t} + \mathrm{e}^{-t}\end{bmatrix} \begin{bmatrix} 2 - \frac{1}{3}\mathrm{e}^{-3t} + \frac{1}{3} \\ 3 - \frac{1}{3}\mathrm{e}^{-3t} + \frac{1}{3} \end{bmatrix} \\ & = \frac{1}{2}\begin{bmatrix} \mathrm{e}^{3t} + \mathrm{e}^{-t} & \mathrm{e}^{3t} - \mathrm{e}^{-t} \\ \mathrm{e}^{3t} - \mathrm{e}^{-t} & \mathrm{e}^{3t} + \mathrm{e}^{-t}\end{bmatrix} \begin{bmatrix} \frac{7}{3} - \frac{1}{3}\mathrm{e}^{-3t} \\ \frac{10}{3} - \frac{1}{3}\mathrm{e}^{-3t} \end{bmatrix} \\ & = \frac{1}{2} \begin{bmatrix} (\mathrm{e}^{3t} + \mathrm{e}^{-t})(\frac{7}{3} - \frac{1}{3}\mathrm{e}^{-3t}) + (\mathrm{e}^{3t} - \mathrm{e}^{-t})(\frac{10}{3} - \frac{1}{3}\mathrm{e}^{-3t}) \\ (\mathrm{e}^{3t} - \mathrm{e}^{-t})(\frac{7}{3} - \frac{1}{3}\mathrm{e}^{-3t}) + (\mathrm{e}^{3t} + \mathrm{e}^{-t})(\frac{10}{3} - \frac{1}{3}\mathrm{e}^{-3t}) \end{bmatrix} \\ & = \frac{1}{2} \begin{bmatrix} \left(\frac{7}{3}\mathrm{e}^{3t} - \frac{1}{3} + \frac{7}{3}\mathrm{e}^{-t} - \frac{1}{3}\mathrm{e}^{-4t}\right) + \left(\frac{10}{3}\mathrm{e}^{3t} - \frac{1}{3} - \frac{10}{3}\mathrm{e}^{-t} + \frac{1}{3}\mathrm{e}^{-4t}\right) \\ \left(\frac{7}{3}\mathrm{e}^{3t} - \frac{1}{3} - \frac{7}{3}\mathrm{e}^{-t} + \frac{1}{3}\mathrm{e}^{-4t}\right) + \left(\frac{10}{3}\mathrm{e}^{3t} - \frac{1}{3} + \frac{10}{3}\mathrm{e}^{-t} - \frac{1}{3}\mathrm{e}^{-4t}\right) \end{bmatrix} \\ & = \frac{1}{2} \begin{bmatrix} \frac{17}{3}\mathrm{e}^{3t} - \mathrm{e}^{-t} - \frac{2}{3} \\ \frac{17}{3}\mathrm{e}^{3t} + \mathrm{e}^{-t} - \frac{2}{3} \end{bmatrix} \\ & = \begin{bmatrix} \frac{17}{6}\mathrm{e}^{3t} - \frac{1}{2}\mathrm{e}^{-t} - \frac{1}{3} \\ \frac{17}{6}\mathrm{e}^{3t} + \frac{1}{2}\mathrm{e}^{-t} - \frac{1}{3} \end{bmatrix} \\ & = \frac{17}{6}\mathrm{e}^{3t}\begin{bmatrix}1 \\ 1\end{bmatrix} + \frac{1}{2} \mathrm{e}^{-t}\begin{bmatrix}-1 \\ 1\end{bmatrix} - \frac{1}{3} \begin{bmatrix}1 \\ 1\end{bmatrix} \end{aligned}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

