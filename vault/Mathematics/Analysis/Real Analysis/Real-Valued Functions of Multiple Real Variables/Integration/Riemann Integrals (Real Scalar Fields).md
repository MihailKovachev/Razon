---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Riemann Integrals (Real Scalar Fields)

The concept of the [Riemann integral](../../Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md) as the surface area bounded by the graph of a [real function](../../Real%20Functions/Real%20Functions.md) can be extended to multiple dimensions via [real scalar fields](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md). For a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^n \to \mathbb{R}$, the "multidimensional Riemann integral" gives us the $(n+1)$-dimensional "volume" bounded by the graph of $f$.

>[!DEFINITION] Definition: Darboux Sums
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) which is [bounded](../../Boundedness%20(Functions).md) on a [compact](../../Euclidean%20Space/Euclidean%20Space.md) rectangular region $[a_1,b_1] \times \cdots \times [a_n, b_n] \subset \mathbb{R}^n$ and let 
>
>$$\begin{aligned}Z_1 & = \{x_{1,1}, \dotsc, x_{1,m_1}\} \\ Z_2 & = \{x_{2,1}, \dotsc, x_{2,m_2}\} \\ & \vdots \\ Z_n & = \{x_{n,1}, \dotsc, x_{n,m_n}\}\end{aligned}$$
>
>be [partitions](../../Euclidean%20Space/Euclidean%20Space.md) of the [intervals](../../Euclidean%20Space/Euclidean%20Space.md) $[a_1,b_1],\dotsc, [a_n, b_n]$, respectively:
>
>$$\begin{aligned}a_1 = x_{1,1} < x_{1,2} & < \cdots < x_{1,m_1} = b_1 \\ a_2 = x_{2,1} < x_{2,2} & < \cdots < x_{2,m_2} = b_2 \\ & \vdots & & \\ a_n = x_{n,1} < x_{n,2} & < \cdots < x_{n,m_n} = b_n \end{aligned}$$
>
>The **lower Darboux sum** of $f$ with respect to $Z_1, \dotsc, Z_n$ is defined using the [infima](../../../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md) of $f$ as follows:
>
>$$L_{Z_1, \dotsc, Z_n}(f) = \sum_{j_1=1}^{m_1-1} \cdots \sum_{j_n=1}^{m_n-1} \inf_{\substack{x_1 \in [x_{1, j_1}, x_{1, j_1+1}] \\ \vdots \\ x_n \in [x_{n, j_n}, x_{n, j_n+1}]}} f(x_1, \dotsc, x_n) \prod_{i=1}^n (x_{i, j_i+1} - x_{i, j_i})$$
>
>The **upper Darboux sum** of $f$ with respect to $Z_1, \dotsc, Z_n$ is defined using the [suprema](../../../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md) of $f$:
>
>$$U_{Z_1, \dotsc, Z_n}(f) = \sum_{j_1=1}^{m_1-1} \cdots \sum_{j_n=1}^{m_n-1} \sup_{\substack{x_1 \in [x_{1, j_1}, x_{1, j_1+1}] \\ \vdots \\ x_n \in [x_{n, j_n}, x_{n, j_n+1}]}} f(x_1, \dotsc, x_n) \prod_{i=1}^n (x_{i, j_i+1} - x_{i, j_i})$$
>

>[!DEFINITION] Definition: Darboux Integrals
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) which is [bounded](../../Boundedness%20(Functions).md) on a [compact rectangular region](../../Euclidean%20Space/Euclidean%20Space.md) $R = [a_1,b_1] \times \cdots \times [a_n, b_n] \subset \mathbb{R}^n$.
>
>The **lower Darboux integral** of $f$ on $R$ is the [supremum](../../../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md) of $f$'s [lower Darboux sums](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) on $R$:
>
>$$L_R(f) = \sup \{L_{Z_1, \dotsc, Z_n} (f) \mid (Z_1, \dotsc, Z_n) \text{ is a partition of } R\}$$
>
>The **upper Darboux integral** of $f$ on $R$ is the [infimum](../../../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md) of $f$'s [upper Darboux sums](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) on $R$:
>
>$$U_R(f) = \inf \{U_{Z_1, \dotsc, Z_n} (f) \mid (Z_1, \dotsc, Z_n) \text{ is a partition of } R\}$$
>

>[!DEFINITION] Definition: Riemann-Integrability (Rectangular Regions)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md).
>
>If $f$ is [bounded](../../Boundedness%20(Functions).md) on a [compact rectangular region](../../Euclidean%20Space/Euclidean%20Space.md) $R = [a_1,b_1] \times \cdots \times [a_n, b_n] \subset \mathbb{R}^n$, then we say that $f$ is **Riemann-integrable** on $R$ if its [lower Darboux integral](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) and [upper Darboux integral](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) are equal:
>
>$$L_R(f) = U_R(f)$$
>
>In this case, this common value is known as $f$'s **Riemann integral** on $R$.
>

>[!DEFINITION] Definition: Riemann-Integrability (Jordan-Measurable Sets)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md).
>
>If $f$ is [bounded](../../Boundedness%20(Functions).md) on a [Jordan-measurable](../../../../Measure%20Theory/Peano-Jordan%20Measure.md) $S \subseteq \mathcal{D}$, then $f$ is **Riemann-integrable** on $S$ if the product $f \cdot \mathbf{1}_S$ is [Riemann-integrable](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) on any [compact rectangular region](../../Euclidean%20Space/Euclidean%20Space.md) containing $S$, where $\mathbf{1}_S$ is the indicator function of $S$:
>
>$$\mathbf{1}_S(\boldsymbol{x}) = \begin{cases}0 & \text{if} & \boldsymbol{x} \notin S \\ 1 & \text{if} & \boldsymbol{x} \in S\end{cases}$$
>
>In this case, the [Riemann integral](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) of $f \cdot \mathbf{1}_S$ is simply called the **Riemann integral** of $f$.
>
>>[!NOTATION]
>>
>>The [Riemann integral](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) of $f$ on $S$ is most commonly denoted as follows:
>>
>>$$\int \cdots \int_{S} f(\boldsymbol{x}) \,\mathrm{d}^n \boldsymbol{x}$$
>>
>>$$\int_{S} f(\boldsymbol{x}) \,\mathrm{d}^n \boldsymbol{x}$$
>>
>>If labels $x_1, \dotsc, x_n$ are introduced for the components, we write:
>>
>>$$\int \cdots \int_{S} f(x_1, \dotsc, x_n) \,\mathrm{d}(x_1, \dotsc, x_n)$$
>>
>>For $n = 2$, we commonly write $\mathrm{d}^2 \boldsymbol{x}$ as $\mathrm{d}S$ or $\mathrm{d}A$. For $n = 3$, we commonly write $\mathrm{d}^3 \boldsymbol{x}$ as $\mathrm{d}V$.
>>
>>Sometimes, a single $\int$ sign is used.
>>
>

For $n = 2$ and $n = 3$, [multidimensional Riemann integrals](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) are also called **double integrals** and **triple integrals**, respectively. 

>[!THEOREM] Theorem: Linearity of Riemann Integrals
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R}^n \to \mathbb{R}$ be [real scalar fields](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $S \subseteq \mathcal{D}_f \cap \mathcal{D}_g$ be [Jordan-measurable](../../../../Measure%20Theory/Peano-Jordan%20Measure.md).
>
>If $f$ and $g$ are [Riemann-integrable](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) on $S$, then so is $\alpha f + \beta g$ for all $\alpha, \beta \in \mathbb{R}$:
>
>$$\int \cdots \int_{S} (\alpha f + \beta g) (\boldsymbol{x}) \,\mathrm{d}^n \boldsymbol{x} = \alpha \int \cdots \int_{S} f (\boldsymbol{x}) \,\mathrm{d}^n \boldsymbol{x} + \beta \int \cdots \int_{S} g (\boldsymbol{x}) \,\mathrm{d}^n \boldsymbol{x}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Riemann integrals via Iterated Integrals
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $R = [a_1, b_1] \times \cdots \times [a_n, b_n] \subset \mathcal{D}$ be a [compact rectangular region](../../Euclidean%20Space/Euclidean%20Space.md).
>
>If $f$ is [continuous](../Continuity%20(Real%20Scalar%20Fields).md) on $R$, then it is [Riemann-integrable](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) on $R$ and its [Riemann-integral](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) is given by any of its [iterated integrals](./Parametric%20Integrals.md):
>
>$$\int \cdots \int_R f(x_1, \dotsc, x_n) \,\mathrm{d}(x_1, \dotsc, x_n) = \int_{a_{\sigma(1)}}^{b_{\sigma(1)}} \cdots \int_{a_{\sigma(n)}}^{b_{\sigma(n)}} f(x_1, \dotsc, x_n) \,\mathrm{d}x_{\sigma(n)} \cdots \mathrm{d}x_{\sigma(1)},$$
>
>where $\sigma$ is any [permutation](../../../../Combinatorics/Permutations.md) of $\{1, \dotsc, n\}$.
>
>>[!EXAMPLE]- Example: $\iint_{R} x + 3x^2 y^2 \,\mathrm{d}(x,y)$ with $R = [0,1] \times [0,1]$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$ defined as
>>
>>$$f(x, y) = x + 3x^2 y^2$$
>>
>>and the [compact rectangular region](../../Euclidean%20Space/Euclidean%20Space.md) $R = [0,1] \times [0,1] \subset \mathbb{R}^2$.
>>
>>We see that $f$ is [continuous](../Continuity%20(Real%20Scalar%20Fields).md) on $R$. Therefore, we have the following for its [double integral](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) over $R$:
>>
>>$$\begin{aligned} \iint_R f(x,y) \, \mathrm{d}(x,y) & = \iint_{R} x + 3x^2 y^2 \,\mathrm{d}(x,y) \\ & = \int_0^1 \int_0^1 x + 3x^2 y^2 \,\mathrm{d}y \,\mathrm{d}x \\ & = \int_0^1 \left.(xy + x^2y^3)\right\vert_{y=0}^{y=1} \,\mathrm{d}x \\ & = \int_0^1 x + x^2 \,\mathrm{d}x \\ & = \left.\left( \frac{1}{2}x^2 + \frac{1}{3}x^3 \right)\right\vert_{x = 0}^{x = 1} \\ & = \frac{5}{6}\end{aligned}$$
>>
>>We could also use the other [iterated integral](./Parametric%20Integrals.md):
>>
>>$$\begin{aligned} \iint_R f(x,y) \, \mathrm{d}(x,y) & = \iint_{R} x + 3x^2 y^2 \,\mathrm{d}(x,y) \\ & = \int_0^1 \int_0^1 x + 3x^2 y^2 \,\mathrm{d}x \,\mathrm{d}y \\ & = \int_0^1 \left.\left(\frac{1}{2}x^2 + x^3y^2\right)\right\vert_{x=0}^{x=1} \,\mathrm{d}y \\ & = \int_0^1 \frac{1}{2} + y^2 \,\mathrm{d}y \\ & = \left.\left( \frac{1}{2}y + \frac{1}{3}y^3 \right)\right\vert_{y=0}^{y=1} \\ & = \frac{5}{6}\end{aligned}$$
>>
>
>>[!EXAMPLE]- Example: $\iiint_{R} xyz \,\mathrm{d}(x,y,z)$ with $R = [0,1]^3$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^3 \to \mathbb{R}$ defined as
>>
>>$$f(x, y, z) = xyz$$
>>
>>and the [compact rectangular region](../../Euclidean%20Space/Euclidean%20Space.md) $R = [0,1]^3 = [0,1] \times [0,1] \times [0,1] \subset \mathbb{R}^3$.
>>
>>We see that $f$ is [continuous](../Continuity%20(Real%20Scalar%20Fields).md) on $R$. Therefore, we have the following for its [triple integral](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) over $R$:
>>
>>$$\begin{aligned} \iiint_R f(x,y,z) \, \mathrm{d}(x,y,z) & = \iiint_{R} xyz \,\mathrm{d}(x,y,z) \\ & = \int_0^1 \int_0^1 \int_0^1 xyz \,\mathrm{d}z \,\mathrm{d}y \,\mathrm{d}x \\ & = \int_0^1 \int_0^1 \left.\left( \frac{1}{2}xyz^2 \right)\right\vert_{z=0}^{z=1} \,\mathrm{d}y \,\mathrm{d}x \\ & = \int_0^1 \int_0^1 \frac{1}{2}xy \,\mathrm{d}y \,\mathrm{d}x \\ & = \int_0^1 \left.\left( \frac{1}{4}xy^2 \right)\right\vert_{y=0}^{y=1} \,\mathrm{d}x \\ & = \int_0^1 \frac{1}{4}x \,\mathrm{d}x \\ & = \left.\left( \frac{1}{8}x^2 \right)\right\vert_{x=0}^{x=1} \\ & = \frac{1}{8}\end{aligned}$$
>>
>>We could also use any of the other five possible [iterated integrals](./Parametric%20Integrals.md). 
>>
>>$$\begin{aligned} \iiint_R f(x,y,z) \, \mathrm{d}(x,y,z) & = \int_0^1 \int_0^1 \int_0^1 xyz \,\mathrm{d}z \,\mathrm{d}x \,\mathrm{d}y \\ & = \int_0^1 \int_0^1 \left.\left( \frac{1}{2}xyz^2 \right)\right\vert_{z=0}^{z=1} \,\mathrm{d}x \,\mathrm{d}y \\ & = \int_0^1 \int_0^1 \frac{1}{2}xy \,\mathrm{d}x \,\mathrm{d}y \\ & = \int_0^1 \left.\left( \frac{1}{4}x^2y \right)\right\vert_{x=0}^{x=1} \,\mathrm{d}y \\ & = \int_0^1 \frac{1}{4}y \,\mathrm{d}y \\ & = \left.\left( \frac{1}{8}y^2 \right)\right\vert_{y=0}^{y=1} \\ & = \frac{1}{8}\end{aligned}$$
>>
>>$$\begin{aligned} \iiint_R f(x,y,z) \, \mathrm{d}(x,y,z) & = \int_0^1 \int_0^1 \int_0^1 xyz \,\mathrm{d}y \,\mathrm{d}z \,\mathrm{d}x \\ & = \int_0^1 \int_0^1 \left.\left( \frac{1}{2}xy^2z \right)\right\vert_{y=0}^{y=1} \,\mathrm{d}z \,\mathrm{d}x \\ & = \int_0^1 \int_0^1 \frac{1}{2}xz \,\mathrm{d}z \,\mathrm{d}x \\ & = \int_0^1 \left.\left( \frac{1}{4}xz^2 \right)\right\vert_{z=0}^{z=1} \,\mathrm{d}x \\ & = \int_0^1 \frac{1}{4}x \,\mathrm{d}x \\ & = \left.\left( \frac{1}{8}x^2 \right)\right\vert_{x=0}^{x=1} \\ & = \frac{1}{8}\end{aligned}$$
>>
>>$$\begin{aligned} \iiint_R f(x,y,z) \, \mathrm{d}(x,y,z) & = \int_0^1 \int_0^1 \int_0^1 xyz \,\mathrm{d}y \,\mathrm{d}x \,\mathrm{d}z \\ & = \int_0^1 \int_0^1 \left.\left( \frac{1}{2}xy^2z \right)\right\vert_{y=0}^{y=1} \,\mathrm{d}x \,\mathrm{d}z \\ & = \int_0^1 \int_0^1 \frac{1}{2}xz \,\mathrm{d}x \,\mathrm{d}z \\ & = \int_0^1 \left.\left( \frac{1}{4}x^2z \right)\right\vert_{x=0}^{x=1} \,\mathrm{d}z \\ & = \int_0^1 \frac{1}{4}z \,\mathrm{d}z \\ & = \left.\left( \frac{1}{8}z^2 \right)\right\vert_{z=0}^{z=1} \\ & = \frac{1}{8}\end{aligned}$$
>>
>>$$\begin{aligned} \iiint_R f(x,y,z) \, \mathrm{d}(x,y,z) & = \int_0^1 \int_0^1 \int_0^1 xyz \,\mathrm{d}x \,\mathrm{d}z \,\mathrm{d}y \\ & = \int_0^1 \int_0^1 \left.\left( \frac{1}{2}x^2yz \right)\right\vert_{x=0}^{x=1} \,\mathrm{d}z \,\mathrm{d}y \\ & = \int_0^1 \int_0^1 \frac{1}{2}yz \,\mathrm{d}z \,\mathrm{d}y \\ & = \int_0^1 \left.\left( \frac{1}{4}yz^2 \right)\right\vert_{z=0}^{z=1} \,\mathrm{d}y \\ & = \int_0^1 \frac{1}{4}y \,\mathrm{d}y \\ & = \left.\left( \frac{1}{8}y^2 \right)\right\vert_{y=0}^{y=1} \\ & = \frac{1}{8}\end{aligned}$$
>>
>>$$\begin{aligned} \iiint_R f(x,y,z) \, \mathrm{d}(x,y,z) & = \int_0^1 \int_0^1 \int_0^1 xyz \,\mathrm{d}x \,\mathrm{d}y \,\mathrm{d}z \\ & = \int_0^1 \int_0^1 \left.\left( \frac{1}{2}x^2yz \right)\right\vert_{x=0}^{x=1} \,\mathrm{d}y \,\mathrm{d}z \\ & = \int_0^1 \int_0^1 \frac{1}{2}yz \,\mathrm{d}y \,\mathrm{d}z \\ & = \int_0^1 \left.\left( \frac{1}{4}y^2z \right)\right\vert_{y=0}^{y=1} \,\mathrm{d}z \\ & = \int_0^1 \frac{1}{4}z \,\mathrm{d}z \\ & = \left.\left( \frac{1}{8}z^2 \right)\right\vert_{z=0}^{z=1} \\ & = \frac{1}{8}\end{aligned}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Riemann-Integrals over Null Sets
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $N \subseteq \mathcal{D}$ be a [null set](../../../../Measure%20Theory/Null%20Sets.md) of the [Peano-Jordan measure](../../../../Measure%20Theory/Peano-Jordan%20Measure.md).
>
>If $f$ is [bounded](../../Boundedness%20(Functions).md) on $N$, then it is also [Riemann-integrable](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) on $N$ and its [Riemann integral](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) is zero:
>
>$$\int \cdots \int_N f(\boldsymbol{x}) \, \mathrm{d}^n \boldsymbol{x} = 0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Domain Additivity of Riemann Integrals
>
>Let $S_1, \dotsc, S_p \subseteq \mathbb{R}^n$ be [Jordan-measurable](../../../../Measure%20Theory/Peano-Jordan%20Measure.md) such that for all $i \ne j$, the [intersection](../../../../Set%20Theory/Intersections.md) $S_i \cap S_j$ is a [null set](../../../../Measure%20Theory/Null%20Sets.md) of the [Peano-Jordan measure](../../../../Measure%20Theory/Peano-Jordan%20Measure.md).
>
>A [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ is [Riemann-integrable](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) on the [union](../../../../Set%20Theory/Unions.md) $S = S_1 \cup \cdots \cup S_p \subseteq \mathcal{D}$ if and only if it is [Riemann-integrable](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) on each of $S_1, \dotsc, S_p$. In this case:
>
>$$\int_{S} f(\boldsymbol{x}) \, \mathrm{d}^n \boldsymbol{x} = \sum_{i = 1}^p\int_{S_i} f(\boldsymbol{x}) \, \mathrm{d}^n \boldsymbol{x}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Riemann Integrals under Alterations
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R}^n \to \mathbb{R}$ be [real scalar fields](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), let $S \subseteq \mathcal{D}_f \cap \mathcal{D}_g$ be [Jordan-measurable](../../../../Measure%20Theory/Peano-Jordan%20Measure.md) and let $N = \{\boldsymbol{x} \in S \mid f(\boldsymbol{x}) \ne g(\boldsymbol{x})\}$.
>
>If $f$ is [Riemann-integrable](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) on $S$, $g$ is [bounded](../../Boundedness%20(Functions).md) on $S$ and $N$ is a [null set](../../../../Measure%20Theory/Null%20Sets.md) of the [Peano-Jordan measure](../../../../Measure%20Theory/Peano-Jordan%20Measure.md), then $g$ is also [Riemann-integrable](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) on $S$ and its [Riemann integral](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) is the same:
>
>$$\int_{S} f(\boldsymbol{x}) \, \mathrm{d}^n\boldsymbol{x} = \int_{S} g(\boldsymbol{x}) \, \mathrm{d}^n\boldsymbol{x}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Integration by Substitution
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\Omega \subseteq \mathbb{R}^n$ be [Jordan-measurable](../../../../Measure%20Theory/Peano-Jordan%20Measure.md). Let $\Phi: \mathcal{D}_{\Phi} \subseteq \mathbb{R}^n \to \mathcal{D}_f$ be a [real vector field](../../Real%20Vector%20Fields/Real%20Vector%20Fields.md) with the following properties:
>
>    - $\Phi$ is [injective](../../../Functions/Injections,%20Surjections%20and%20Bijections.md) on $\Omega$, except possibly on a [null set](../../../../Measure%20Theory/Null%20Sets.md) of the [Peano-Jordan measure](../../../../Measure%20Theory/Peano-Jordan%20Measure.md).
>    - $\Phi$ is (extendable to be) [continuously totally differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) on an [open set](../../Euclidean%20Space/Euclidean%20Space.md) containing $\Omega$.
>    - $\Phi$ can be extended to be [continuously totally differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) on an [open set](../../Euclidean%20Space/Euclidean%20Space.md) containing $\Omega$.
>    - The [Jacobian matrix](../../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md) $J_{\Phi}$ is [invertible](../../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md) on the [interior](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\Omega$.
>
>Then $(f \circ \Phi)|\det J_{\Phi}|$ is [Riemann-integrable](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) on $\Omega$ if and only if $f$ is [Riemann-integrable](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) on $\Phi(\Omega)$. In this case:
>
>$$\int_{\Omega} f(\Phi(\boldsymbol{x})) |\det J_{\Phi}(\boldsymbol{x})| \,\mathrm{d}^n \boldsymbol{x} = \int_{\Phi(\Omega)} f(\boldsymbol{u}) \, \mathrm{d}^n \boldsymbol{u}$$
>
>>[!EXAMPLE]-
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$ defined as follows:
>>
>>$$f(x,y) = x$$
>>
>>Let $B = \{\begin{bmatrix}x & y\end{bmatrix}^{\mathsf{T}} \in \mathbb{R}^2 \mid x^2 + y^2 \le 1, x \ge 0, y \ge 0\}$. 
>>
>>We want to evaluate the [Riemann integral](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) of $f$ over $B$:
>>
>>$$\iint_B f(x,y) \, \mathrm{d}(x,y)$$
>>
>>We notice that $B$ is a quarter-circle. Specifically, it is the [image](../../../Functions/Functions.md) of $\Omega = [0,1] \times \left[0, \frac{\uppi}{2}\right]$ under the [coordinate transformation](../../Euclidean%20Space/Coordinate%20Transformations.md) $\Phi: [0, +\infty] \times [0, 2\uppi] \to \mathbb{R}^2$ from [polar coordinates](../../Euclidean%20Space/Polar%20Coordinates.md):
>>
>>$$\Phi(\rho, \varphi) = \begin{bmatrix} \rho \cos \varphi \\ \rho \sin \varphi\end{bmatrix}$$
>>
>>$$B = \Phi(\Omega)$$
>>
>>We see that the conditions in the theorem are met. Therefore:
>>
>>$$\iint_B f(x,y) \, \mathrm{d}(x,y) = \iint_{\Omega} f(\Phi(\rho, \varphi)) |\det J_{\Phi}(\rho, \varphi)| \, \mathrm{d}(\rho,\varphi)$$
>>
>>For the [Jacobian matrix](../../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md) of $J_{\Phi}$, we have:
>>
>>$$J_{\Phi}(\rho, \varphi) = \begin{bmatrix} \cos \varphi & -\rho \sin \varphi \\ \sin \varphi & \rho \cos \varphi \end{bmatrix}$$
>>
>>Therefore:
>>
>>$$|\det J_{\Phi}(\rho, \varphi)| = |\rho| = \rho$$
>>
>>We have:
>>
>>$$\begin{aligned}\iint_B f(x,y) \, \mathrm{d}(x,y) & = \iint_{\Omega} f(\Phi(\rho, \varphi)) |\det J_{\Phi}(\rho, \varphi)| \, \mathrm{d}(\rho,\varphi) \\ & = \iint_{\Omega} \rho \cos (\varphi) \rho \, \mathrm{d}(\rho,\varphi) \\ & = \iint_{\Omega} \rho^2 \cos \varphi \, \mathrm{d}(\rho,\varphi) \end{aligned}$$
>>
>>Since $\rho^2 \cos \varphi$ is [continuous](../Continuity%20(Real%20Scalar%20Fields).md), we have:
>>
>>$$\begin{aligned}\iint_{\Omega} \rho^2 \cos \varphi \, \mathrm{d}(\rho,\varphi) & = \int_0^{\frac{\uppi}{2}} \int_0^1 \rho^2 \cos \varphi \, \mathrm{d}\rho \, \mathrm{d}\varphi \\ & = \left( \int_0^{\frac{\uppi}{2}} \cos \varphi \, \mathrm{d}\varphi \right) \left( \int_0^1 \rho^2 \, \mathrm{d}\rho \right) \\ & = 1 \cdot \frac{1}{3} \\ & = \frac{1}{3}\end{aligned}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Riemann Integrals over Elementary Regions
>
>>[!DEFINITION] Definition: Elementary Regions
>>
>>An **elementary region** of $\mathbb{R}^1$ is a [compact interval](../../Euclidean%20Space/Euclidean%20Space.md).
>>
>>An **elementary region** of $\mathbb{R}^n$ ($n \gt 1$) is a [subset](../../../../Set%20Theory/Subsets.md) $E \subset \mathbb{R}^n$ for which there exists a [permutation](../../../../Combinatorics/Permutations.md) $\sigma$ of $\{1, \dotsc, n\}$ such that $E$ can be specified as
>>
>>$$E = \left\{\begin{bmatrix}x_1 \\ \vdots \\ x_n \end{bmatrix} \in \mathbb{R}^n : \begin{bmatrix}x_{\sigma(1)} \\ \vdots \\ x_{\sigma(n-1)} \end{bmatrix}\in E' \text{ and } l\left( \begin{bmatrix}x_{\sigma(1)} \\ \vdots \\ x_{\sigma(n - 1)}\end{bmatrix}\right) \le x_{\sigma(n)} \le u\left( \begin{bmatrix}x_{\sigma(1)} \\ \vdots \\ x_{\sigma(n - 1)}\end{bmatrix}\right)\right\}$$
>>
>>for some [elementary region](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) $E'$ of $\mathbb{R}^{n-1}$ and some [continuous](../Continuity%20(Real%20Scalar%20Fields).md) [real scalar fields](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $l, u: E' \to \mathbb{R}$.
>>
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $E \subseteq \mathcal{D}$ be an [elementary region](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) as defined above.
>
>If $f$ is [continuous](../Continuity%20(Real%20Scalar%20Fields).md) on $E$, then its [Riemann integral](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) over $E$ exists and is given by the following [Riemann integral](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) of a [parametric integral](./Parametric%20Integrals.md):
>
>$$\int_E f(x_1, \dotsc, x_n) \, \mathrm{d}(x_1, \dotsc, x_n) = \int_{E'} \left( \int\limits_{\displaystyle l(x_{\sigma(1)}, \dotsc, x_{\sigma(n-1)})}^{\displaystyle u(x_{\sigma(1)}, \dotsc, x_{\sigma(n-1)})} f(x_1, \dotsc, x_n) \, \mathrm{d}x_{\sigma(n)}\right)\, \mathrm{d}(x_{\sigma(1)}, \dotsc, x_{\sigma(n-1)})$$
>
>>[!EXAMPLE]- Example: $\iint_{E} xy^2 \, \mathrm{d}(x,y)$ with $E = \{(x,y) \in \mathbb{R}^2 \mid 0 \le x \le 1 + y^2, -1 \le y \le 1\}$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$ defined as follows:
>>
>>$$f(x, y) = xy^2$$
>>
>>We want to evaluate the [Riemann integral](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md)
>>
>>$$\iint_{E} f(x,y) \, \mathrm{d}(x,y) = \iint_{E} xy^2 \, \mathrm{d}(x,y),$$
>>
>>where $E$ is defined as follows:
>>
>>$$E = \{(x,y) \in \mathbb{R}^2 \mid 0 \le x \le 1 + y^2, -1 \le y \le 1\}$$
>>
>>We see that $E$ is an [elementary region](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) of $\mathbb{R}^2$ because
>>
>>$$E = \{(x, y) \in \mathbb{R}^2 \mid y \in E' \text{ and } l(y) \le x \le u(y)\}$$
>>
>>with $E' = [-1, 1]$ (a [compact interval](../../Euclidean%20Space/Euclidean%20Space.md) and thus an [elementary region](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) of $\mathbb{R}$) and with the [continuous](../../Real%20Functions/Continuity%20(Real%20Functions).md) $l,u: E' \to \mathbb{R}$ defined as $l(y) = 0$ and $u(y) = 1 + y^2$.
>>
>>Since $f$ is [continuous](../Continuity%20(Real%20Scalar%20Fields).md) on $E$, we can apply the theorem:
>>
>>$$\begin{aligned} \iint_{E} f(x,y) \, \mathrm{d}(x,y) & = \iint_{E} xy^2 \, \mathrm{d}(x,y) \\ & = \int_{E'}\left( \int_{l(y)}^{u(y)} f(x,y) \, \mathrm{d}x \right) \, \mathrm{d}y \\ & = \int_{-1}^{1} \left( \int_{0}^{1+y^2} xy^2 \, \mathrm{d}x \right) \, \mathrm{d}y \\ & = \int_{-1}^{1} \left( \left.\frac{1}{2}x^2 y^2\right\vert_{x=0}^{x=1+y^2} \right) \, \mathrm{d}y \\ & = \int_{-1}^{1} \frac{1}{2}(1+y^2)^2 y^2 \, \mathrm{d}y \\ & = \frac{1}{2} \int_{-1}^{1} (1 + 2y^2 + y^4) y^2 \, \mathrm{d}y \\ & = \frac{1}{2} \int_{-1}^{1} (y^2 + 2y^4 + y^6) \, \mathrm{d}y \\ & = \frac{1}{2} \left[ \frac{y^3}{3} + \frac{2y^5}{5} + \frac{y^7}{7} \right]_{-1}^{1} \\ & = \frac{1}{2} \left( \left( \frac{1}{3} + \frac{2}{5} + \frac{1}{7} \right) - \left( -\frac{1}{3} - \frac{2}{5} - \frac{1}{7} \right) \right) \\ & = \frac{1}{3} + \frac{2}{5} + \frac{1}{7} \\ & = \frac{35}{105} + \frac{42}{105} + \frac{15}{105} \\ & = \frac{92}{105} \end{aligned}$$
>>
>
>>[!EXAMPLE]- Example: $\iint_S x^2 y \,\mathrm{d}(x,y)$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$ defined as follows:
>>
>>$$f(x, y) = xy^2$$
>>
>>We want to evaluate the [Riemann integral](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md)
>>
>>$$\iint_{S} f(x,y) \, \mathrm{d}(x,y) = \iint_{S} x^2y \, \mathrm{d}(x,y),$$
>>
>>where $S$ is defined as the [subset](../../../../Set%20Theory/Subsets.md) bounded by the graphs of the [functions](../../Real%20Functions/Real%20Functions.md) $y = 2$, $y = x$ and $y = \frac{1}{2}$:
>>
>>![Non-Elementary Region](./res/Non-Elementary%20Region.svg)
>>
>>While $S$ is not itself an [elementary region](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md), it can be expressed as the [union](../../../../Set%20Theory/Unions.md) of two [elementary regions](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) $E_1$ and $E_2$:
>>
>>$$E_1 = \left\{(x,y) \in \mathbb{R}^2 \mid \frac{1}{2} \le x \le 1, \frac{1}{x} \le y \le 2 \right\}$$
>>
>>$$E_2 = \left\{(x, y) \in \mathbb{R}^2 \mid 1 \le x \le 2, x \le y \le 2\right\}$$
>>
>>![Elementary Region Division](./res/Elementary%20Region%20Division.svg)
>>
>>Since $S$ is [Jordan-measurable](../../../../Measure%20Theory/Peano-Jordan%20Measure.md) and since $f$ is [continuous](../Continuity%20(Real%20Scalar%20Fields).md) on $S$, the [Riemann integral](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md) of $f$ over $S$ exists. Moreover, since 
>>
>>$$E_1 \cap E_2 = \{(x, y) \in \mathbb{R}^2 \mid x = 1, 1 \le y \le 2\}$$
>>
>>is a [null set](../../../../Measure%20Theory/Null%20Sets.md) of the [Peano-Jordan measure](../../../../Measure%20Theory/Peano-Jordan%20Measure.md), we can split the [Riemann integral](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md):
>>
>>$$\iint_S f(x, y) \,\mathrm{d}(x, y) = \iint_{E_1} f(x, y) \,\mathrm{d}(x, y) + \iint_{E_2} f(x, y) \,\mathrm{d}(x, y)$$
>>
>>We now use the fact that $E_1$ is an [elementary region](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md)
>>
>>$$E_1 = \left\{(x,y) \in \mathbb{R}^2 \mid \frac{1}{2} \le x \le 1, \frac{1}{x} \le y \le 2 \right\}$$
>>
>>with $E_1' = \left[\frac{1}{2}, 1\right]$, $l_1(x) = \frac{1}{x}$ and $u_1(x) = 2$ and the fact that $E_2$ is an [elementary region](./Riemann%20Integrals%20(Real%20Scalar%20Fields).md)
>>
>>$$E_2 = \left\{(x, y) \in \mathbb{R}^2 \mid 1 \le x \le 2, x \le y \le 2\right\}$$
>>
>>with $E_2' = \left[1, 2\right]$, $l_2(x) = x$ and $u_2(x) = 2$. Therefore:
>>
>>$$\begin{aligned}\iint_{E_1} f(x,y) \,\mathrm{d}(x, y) + \iint_{E_2} f(x,y) \,\mathrm{d}(x, y) & = \int_{E_1'} \left( \int_{l_1(x)}^{u_1(x)} f(x, y) \, \mathrm{d}y \right) \,\mathrm{d}x + \int_{E_2'} \left( \int_{l_2(x)}^{u_2(x)} f(x, y) \, \mathrm{d}y \right) \,\mathrm{d}x \\ & = \int_{\frac{1}{2}}^{1} \left( \int_{\frac{1}{x}}^{2} x^2 y \, \mathrm{d}y \right) \,\mathrm{d}x + \int_{1}^{2} \left( \int_{x}^{2} x^2 y \, \mathrm{d}y \right) \,\mathrm{d}x \\ & = \int_{\frac{1}{2}}^{1} \left(\left.\frac{1}{2}x^2 y^2 \right\vert_{y = \frac{1}{x}}^{2} \right)\,\mathrm{d}x + \int_{1}^{2} \left(\left.\frac{1}{2}x^2 y^2 \right\vert_{y = x}^{2} \right) \,\mathrm{d}x \\ & = \int_{\frac{1}{2}}^{1} \left( 2x^2 - \frac{1}{2} \right) \,\mathrm{d}x + \int_{1}^{2} \left( 2x^2 - \frac{1}{2}x^4 \right) \,\mathrm{d}x \\ & = \left( \frac{2}{3}x^3 - \frac{1}{2}x \right)\Bigg|_{\frac{1}{2}}^{1} + \left( \frac{2}{3}x^3 - \frac{1}{10}x^5 \right)\Bigg|_{1}^{2} \\ & = \left[ \left(\frac{2}{3} - \frac{1}{2}\right) - \left(\frac{1}{12} - \frac{1}{4}\right) \right] + \left[ \left(\frac{16}{3} - \frac{32}{10}\right) - \left(\frac{2}{3} - \frac{1}{10}\right) \right] \\ & = \left[ \frac{1}{6} - \left(-\frac{1}{6}\right) \right] + \left[ \frac{32}{15} - \frac{17}{30} \right] \\ & = \frac{1}{3} + \frac{47}{30} \\ & = \frac{10}{30} + \frac{47}{30} \\ & = \frac{57}{30} \\ & = \frac{19}{10} \end{aligned}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>
