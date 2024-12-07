>[!DEFINITION] Definition: Double Integral of a Real Scalar Field over a Rectangle
>
>Let $f: R \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) over some rectangle $R = [a;b] \times [c;d] \subset \mathbb{R}^2$.
>
>The **double integral of** $f$ **over** $R$ is the [limit](../../../Univariate%20Real%20Analysis/Real%20Functions/Limits%20of%20Functions/Limits%20of%20a%20Function.md) of all of its [double Riemann sums](Double%20Riemann%20Sum.md), if it exists and is the same for all of them.
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
>The **double integral of** $f$ **over** $D$ is the [double integral](Double%20Integral%20of%20a%20Real%20Scalar%20Field.md)
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
>>![](Resources/Geometric%20Meaning%20of%20the%20Double%20Integral.png)
>>
>

>[!THEOREM] Theorem: Linearity of the Double Integral
>
>Let $f,g: D\to\mathbb{R}$ be [real scalar fields](../Real%20Scalar%20Field.md) over a [general region](../../../../../Geometry/General%20Regions%20in%202D.md) $D \subset \mathbb{R}^2$.
>
>The [double integral](Double%20Integral%20of%20a%20Real%20Scalar%20Field.md) is [linear](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Linear%20Transformation.md) - for all $\lambda,\mu\in\mathbb{R}$:
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

>[!THEOREM] Theorem: Double Integral over General Regions
>
>Let $f: D\subseteq\mathbb{R}^2 \to\mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md).
>
>If $f$ is [continuous](../Continuity%20of%20Real%20Scalar%20Fields.md) and $D$ is a [general region](../../../../../Geometry/General%20Regions%20in%202D.md) $D = \{(x,y)\mid a\le x \le b, l(x) \le y \le u(x)\}$, then the [double integral](Double%20Integral%20of%20a%20Real%20Scalar%20Field.md) of $f$ over $D$ can be calculated through via iterated [parametric integrals](Parametric%20Integrals.md):
>
>$$
>\iint\limits_D f \mathop{\mathrm{d}D} = \int_a^b \int_{l(x)}^{u(x)} f(x, y) \mathop{\mathrm{d}y}\mathop{\mathrm{d}x}
>$$
>
>If $f$ is [continuous](../Continuity%20of%20Real%20Scalar%20Fields.md) and $D$ is a [general region](../../../../../Geometry/General%20Regions%20in%202D.md) $D = \{(x,y)\mid l(y)\le x \le u(y), a \le y \le b\}$, then the [double integral](Double%20Integral%20of%20a%20Real%20Scalar%20Field.md) of $f$ over $D$ can be calculated through via iterated [parametric integrals](Parametric%20Integrals.md):
>
>$$
>\iint\limits_D f \mathop{\mathrm{d}D} = \int_a^b \int_{l(y)}^{u(y)} f(x, y) \mathop{\mathrm{d}x}\mathop{\mathrm{d}y}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Region Decomposition
>
>Let $f: D \subset \mathbb{R}^2 \to\mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md).
>
>If $D$ can be represented as a [union](../../../../../Set%20Theory/Operations%20with%20Sets/Union.md) [disjoint](../../../../../Set%20Theory/Disjoint%20Sets.md) $D = D_1\cup\cdots\cup D_n$ of finitely many [disjoint](../../../../../Set%20Theory/Disjoint%20Sets.md) [general regions](../../../../../Geometry/General%20Regions%20in%202D.md), then the [double integral](Double%20Integral%20of%20a%20Real%20Scalar%20Field.md) of $f$ over $D$ is the sum of the [double integral](Double%20Integral%20of%20a%20Real%20Scalar%20Field.md) of $f$ over $D_1,\cdots, D_n$:
>
>$$
>\iint\limits_D f \mathop{\mathrm{d}A} = \iint\limits_{D_1} \mathop{\mathrm{d}D_1} + \cdots + \iint\limits_{D_n} f \mathop{\mathrm{d}D_n}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
