---
title: Double Integrals
tags:
    - vector-analysis
    - real-analysis
    - analysis
    - mathematics
---

# Double Riemann Sums

>[!DEFINITION] Definition: Double Riemann Sum
>
>Let $f: R \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) over some rectangle $R = [a;b] \times [c;d] \subset \mathbb{R}^2$.
>
>1. Subdivide the interval $[a;b]$ into $m$ intervals $[x_{i-1}; x_i]$ of length $\Delta x = \frac{b - a}{m}$.
>
>2. Subdivide the interval $[c;d]$ into $n$ intervals $[y_{i-1}; y_i]$ of length $\Delta x = \frac{d - c}{n}$.
>
>3. These subdivision result in smaller rectangles $R_{ij} = \{(x,y)\mid x_{i-1} \le x \le x_i, y_{j-1} \le y \le y_j\},$ each with area $\Delta A = \Delta x \Delta y$.
>
>- For every choice of $(x_{ij}^\ast, y_{ij}^\ast) \in R_{ij}$ we get a **double Riemann sum** of $f$ **over** $R$.
>
>$$
>\sum_{i=1}^m\sum_{j=1}^n f(x_{ij}^\ast, y_{ij}^\ast)\Delta A
>$$
>

# Double Integrals

>[!DEFINITION] Definition: Double Integral of a Real Scalar Field over a Rectangle
>
>Let $f: R \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) over some rectangle $R = [a;b] \times [c;d] \subset \mathbb{R}^2$.
>
>The **double integral of** $f$ **over** $R$ is the [limit](../../../Real%20Functions/Limits/Limits%20of%20Real%20Functions.md) of all of its [double Riemann sums](Double%20Integrals.md), if it exists and is the same for all of them.
>
>$$
>\lim_{m,n\to\infty} \sum_{i=1}^m\sum_{j=1}^n f(x_{ij}^\ast, y_{ij}^\ast) \Delta A
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\iint\limits_R f\mathop{\mathrm{d}R} \qquad \iint\limits_R f\mathop{\mathrm{d}A} \qquad \iint\limits_R f(x,y)\mathop{\mathrm{d}A}
>>$$
>>
>

>[!DEFINITION] Definition: Double Integral of a Real Scalar Field over an Arbitrary Region
>
>Let $f: D \subset \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md).
>
>The **double integral of** $f$ **over** $D$ is the [double integral](Double%20Integrals.md#Double%20Integrals)
>
>$$
>\iint\limits_R \mathcal{F}\mathop{\mathrm{d}R},
>$$
>
>where $R \subset \mathbb{R}^2$ is any rectangle which completely contains $D$ and 
>
>$$
>\mathcal{F}(x,y) = \begin{cases}f(x,y), \qquad \text {if } (x,y)\in D \\ 0, \qquad\qquad \text{ if } (x,y) \in R\setminus D\end{cases}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\iint\limits_D f \mathop{\mathrm{d}D} \qquad \iint\limits_D f \mathop{\mathrm{d}A} \qquad \iint\limits_D f(x,y) \mathop{\mathrm{d}A}
>>$$
>>
>
>>[!INTUITION]- Intuition: Geometric Meaning of the Double Intgeral
>>
>>The [double integral](Double%20Integral%20of%20a%20Real%20Scalar%20Field.md) of $f$ over $D$ is the signed volume between the graph of $f$ and $D$.
>>
>>![](res/Geometric%20Meaning%20of%20the%20Double%20Integral.png)
>>
>

## Properties

>[!THEOREM]- Theorem: Linearity of the Double Integral
>
>Let $f,g: D\to\mathbb{R}$ be [real scalar fields](../Real%20Scalar%20Field.md) over a [general region](../../../../../Geometry/General%20Regions%20in%202D.md) $D \subset \mathbb{R}^2$.
>
>The [double integral](Double%20Integrals.md#Double%20Integrals) is [linear](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Linear%20Transformation.md) - for all $\lambda,\mu\in\mathbb{R}$:
>
>$$
>\iint\limits_D \lambda\,f(x,y) + \mu\, g(x,y)\mathop{\mathrm{d}A} = \lambda \iint \limits_D f(x,y) \mathop{\mathrm{d}A} \,\, + \,\, \mu \iint\limits_D g(x,y)\mathop{\mathrm{d}A}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Double Integrals via Iterated Integrals
>
>Let $f: \mathcal{D} \subseteq\mathbb{R}^2 \to\mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md).
>
>If $f$ is [continuous](../Continuity%20of%20Real%20Scalar%20Fields.md) and $\mathcal{D}$ can be expressed as $D = \left\{\begin{bmatrix} x \\ y\end{bmatrix}\mid a\le x \le b, l(x) \le y \le u(x)\right\}$, where $l$ and $u$ are [continuous](../../../Real%20Functions/Continuity.md) [real functions](../../../Functions%20of%20the%20Real%20Numbers.md), then the [double integral](Double%20Integrals.md#Double%20Integrals) of $f$ over $\mathcal{D}$ can be calculated via iterated [parametric integrals](Parametric%20Integrals.md):
>
>$$
>\iint\limits_{\mathcal{D}} f \mathop{\mathrm{d}\mathcal{D}} = \int_a^b \int_{l(x)}^{u(x)} f(x, y) \mathop{\mathrm{d}y}\mathop{\mathrm{d}x}
>$$
>
>If $f$ is [continuous](../Continuity%20of%20Real%20Scalar%20Fields.md) and $\mathcal{D}$ can be expressed as $\mathcal{D} = \left\{\begin{bmatrix} x \\ y \end{bmatrix} \mid l(y)\le x \le u(y), a \le y \le b\right\}$, where $l$ and $u$ are [continuous](../../../Real%20Functions/Continuity.md) [real functions](../../../Functions%20of%20the%20Real%20Numbers.md), then the [double integral](Double%20Integrals.md#Double%20Integrals) of $f$ over $\mathcal{D}$ can be calculated via iterated [parametric integrals](Parametric%20Integrals.md):
>
>$$
>\iint\limits_{\mathcal{D}} f \mathop{\mathrm{d}\mathcal{D}} = \int_a^b \int_{l(y)}^{u(y)} f(x, y) \mathop{\mathrm{d}x}\mathop{\mathrm{d}y}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Region Decomposition
>
>Let $f: \mathcal{D} \subset \mathbb{R}^2 \to\mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md).
>
>If $D$ can be represented as a [union](../../../../../Set%20Theory/Set%20Operations.md) [disjoint](../../../../../Set%20Theory/Disjoint%20Sets.md) $\mathcal{D} = \mathcal{D}_1 \cup \cdots \cup \mathcal{D}_n$ of finitely many [disjoint](../../../../../Set%20Theory/Disjoint%20Sets.md) [sets](../../../../../Set%20Theory/Sets.md), then the [double integral](Double%20Integrals.md#Double%20Integrals) of $f$ over $\mathcal{D}$ is the sum of the [double integral](Double%20Integrals.md#Double%20Integrals) of $f$ over $\mathcal{D}_1,\dotsc, \mathcal{D}_n$:
>
>$$
>\iint\limits_{\mathcal{D}} f \mathop{\mathrm{d}\mathcal{D}} = \iint\limits_{\mathcal{D}_1} \mathop{\mathrm{d}\mathcal{D}_1} + \cdots + \iint\limits_{\mathcal{D}_n} f \mathop{\mathrm{d}\mathcal{D}_n}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
