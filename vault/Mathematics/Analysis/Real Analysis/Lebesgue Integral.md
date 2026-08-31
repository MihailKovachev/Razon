---
tags:
    - real-analysis
    - analysis
    - mathematics
---

# Lebesgue Integral


Consider a [subset](../../Set%20Theory/Sets.md#Subsets) $S \subseteq \mathbb{R}$ and its [indicator function](../../Set%20Theory/Sets.md#Subsets) $\mathbf{1}_S: \mathbb{R} \to \mathbb{R}$. The graph of $\mathbf{1}_S$ would resemble the following, since $\mathbf{1}_S(x) = 1$ if $x \in S$ and $\mathbf{1}_S(x) = 0$ otherwise:

![](./res/Integration%20of%20Indicator%20Functions.svg)

The area under the graph of $\mathbf{1}_S$ is just the sum of the shaded areas, all of which have a height of $1$. The area of each of these is given by $1 \cdot \mu (S_i)$, where $\mu(S_i)$ is the size (length) of each blue piece. Therefore, the area under the graph of $\mathbf{1}_S$ is $\sum_{i} 1 \cdot \mu(S_i) = 1\cdot \sum_{i} \mu(S_i) = \sum_{i} \mu(S_i)$. However, the sum $\sum_{i} \mu(S_i)$ of the sizes of the blue pieces $S_i$ is just equal to the size $\mu(S)$ of $S$. Thus we define the integral of $\mathbf{1}_S$ in the following way.

>[!DEFINITION] Definition: Lebesgue Integral of Indicator Functions
>
>Let $(X, \Sigma, \mu)$ be a [measure space](../../Measure%20Theory/Measure%20Spaces.md), let $S \subseteq X$ be [measurable](../../Measure%20Theory/Measure%20Spaces.md) and let $\mathbf{1}_S: X \to \mathbb{R}$ be the [indicator function](../../Set%20Theory/Sets.md#Subsets) of $S$.
>
>The **(Lebesgue) integral** of $\mathbf{1}_S$ **with respect to** $\mu$ is the [measure](../../Measure%20Theory/Measure%20Spaces.md) of $S$:
>
>$$
>\int \mathbf{1}_S \mathop{\mathrm{d}\mu} \overset{\text{def}}{=} \mu(S)
>$$
>

We now extend this definition to functions which can be built from finitely many [indicator functions](../../Set%20Theory/Sets.md#Subsets).

>[!DEFINITION] Definition: Simple Function
>
>Let $(X, \Sigma, \mu)$ be a [measure space](../../Measure%20Theory/Measure%20Spaces.md) and let $\phi: \mathcal{D} \subseteq X \to \mathbb{R}_{\ge 0}$ be a [real-valued function](./Real%20Functions/Real%20Functions.md).
>
>We say that $\phi$ is a **simple function** if $\mathcal{D}$ can be represented as the [union](../../Set%20Theory/Collections.md#Operations) of a [finite](../../Set%20Theory/Cardinality.md) [collection](../../Set%20Theory/Collections.md) [disjoint](../../Set%20Theory/Sets.md#Operations) [measurable](../../Measure%20Theory/Measure%20Spaces.md) [sets](../../Set%20Theory/Sets.md#Subsets) $\mathcal{D} = \mathcal{D}_1 \cup \cdots \cup \mathcal{D}_n$ and there exist $n$ [real numbers](../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) $c_1, \dotsc, c_n \ge 0$ such that
>
>$$
>\phi(x) = \sum_{i = 1}^n c_i \mathbf{1}_{\mathcal{D}_i}(x) \qquad \forall x \in \mathcal{D},
>$$
>
>where $\mathbf{1}_{\mathcal{D}_i}$ is the [indicator function](../../Set%20Theory/Sets.md#Subsets) of $\mathcal{D}_i$.

Consider a [simple](./Lebesgue%20Integral.md) [real function](./Real%20Functions/Real%20Functions.md) $\phi: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$. 

![](./res/Integration%20of%20Simple%20Functions.svg)

The are under its graph is just the sum of the shaded areas. All shaded areas with a blue bottom have a height of $c_1$ and all shaded areas with a green bottom have a height of $c_2$. Applying the same reasoning as we did with [indicator functions](./Lebesgue%20Integral.md), the total shaded area with a blue bottom is $c_1 \cdot \mu (\mathcal{D}_1)$. Similarly, the total shaded area with a green bottom is $c_2 \cdot \mu(\mathcal{D}_2)$. The area under the graph of $\phi$ is then given by summing these two areas: $c_1 \cdot \mu (\mathcal{D}_1) + c_2 \cdot \mu(\mathcal{D}_2)$. More generally, when $\mathcal{D}$ must be decomposed into $n$ [subsets](../../Set%20Theory/Sets.md) $\mathcal{D} = \mathcal{D}_1 \cup \cdots \cup \mathcal{D}_n$, the total area is given by $\sum_{i=1}^n c_i \cdot \mu(\mathcal{D}_i)$.

>[!DEFINITION] Definition: Lebesgue Integral of Simple Functions
>
>Let $(X, \Sigma, \mu)$ be a [measure space](../../Measure%20Theory/Measure%20Spaces.md) and let $\phi: \mathcal{D} \subseteq X \to \mathbb{R}_{\ge 0}$ be a [real-valued function](./Real%20Functions/Real%20Functions.md) such that $\mathcal{D}$ can be represented as the [union](../../Set%20Theory/Collections.md#Operations) of a [finite](../../Set%20Theory/Cardinality.md) [collection](../../Set%20Theory/Collections.md) [disjoint](../../Set%20Theory/Sets.md#Operations) [measurable](../../Measure%20Theory/Measure%20Spaces.md) [sets](../../Set%20Theory/Sets.md#Subsets) $\mathcal{D} = \mathcal{D}_1 \cup \cdots \cup \mathcal{D}_n$ and there exist $n$ [real numbers](../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) $c_1, \dotsc, c_n \ge 0$ with
>
>$$
>\phi(x) = \sum_{i = 1}^n c_i \mathbf{1}_{\mathcal{D}_i}(x) \qquad \forall x \in \mathcal{D}.
>$$
>
>The **(Lebesgue) integral** of $\phi$ **with respect to** $\mu$ is defined using the [measures](../../Measure%20Theory/Measure%20Spaces.md) of $\mathcal{D}_i$ as
>
>$$
>\int \phi \mathop{\mathrm{d}\mu} \overset{\text{def}}{=} \sum_{i = 1}^n c_i \mu(\mathcal{D}_i),
>$$
>
>with the convention $0 \cdot \infty = 0$.
>

This definition can be extended to non-negative [real-valued functions](./Real-Valued%20Functions.md). Consider a [real function](./Real%20Functions/Real%20Functions.md) $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}_{\ge 0}$. We can approximate $f$ using a [simple function](./Lebesgue%20Integral.md). Choose $n \in \mathbb{N}$ values $c_1, \dotsc, c_n \in f(\mathcal{D})$ from the [range](../Functions/Functions.md) of $f$ and let $\mathcal{D}_i = \{x \in \mathcal{D} \mid f(x) \ge c_i\}$. Define $\phi: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}_{\ge 0}$ in the following way:

$$
\phi(x) \overset{\text{def}}{=} \begin{cases}c_1 \qquad \text{if } x \in \mathcal{D}_1 \\ \vdots \\ c_n \qquad \text{if } x \in \mathcal{D}_n\end{cases} 
$$

We see $\phi$ is a [simple function](./Lebesgue%20Integral.md)

$$
\phi(x) = \sum_{i = 1}^n c_i \mathbf{1}_{\mathcal{D}_i}(x),
$$

since $\mathbf{1}_{\mathcal{D}_j}(x)$ gives $1$ only when $x \in \mathcal{D}_j$ and gives $0$ otherwise. Therefore, $\phi(x) = c_j$ if and only if $x \in \mathcal{D}_j$. Of course, if we choose only a few values $c_1, \cdots, c_n$, then $\phi$ will be a pretty bad approximation of $f$. However, as we increase the number of values $n$, $\phi$ becomes a better and better approximation. This is illustrated in the following animation:

![](./res/Simple%20Function%20Approximation.gif)

Lines with the same color correspond to the same value $c_j$ and $\mathcal{D}_j$ is the part of the of $\mathbb{R}$ which lies directly below the lines corresponding to $c_j$. 

The more closely $\phi$ approximates $f$, the more the area under the graph of $\phi$ resembles the area under the graph of $f$:

![](./res/Simple%20Function%20Area%20Approximation.gif)

This notion of $\phi$ approximating $f$ can be defined and proven rigorously via [function sequences](TODO) and their [limits](TODO) but that is unnecessary. Notice that $0 \le \phi(x) \le f(x)$ for all $x \in \mathcal{D}$. Consider now the [set](../../Set%20Theory/Sets.md#Sets) $S$ of the [integrals](./Lebesgue%20Integral.md) of all [simple functions](./Lebesgue%20Integral.md) $s: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ such that $0 \le s(x) \le f(x)$ for all $x \in \mathcal{D}$. Since these [simple functions](./Lebesgue%20Integral.md) are always less than or equal to $f$, the areas under their graphs must be less than or equal to the area under the graph of $f$. The [supremum](../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md) of $S$, i.e. the largest of these areas, is thus as close as one could get to the area under the graph of $f$. Moreover, it can be proven that this is equal to the [integral](#Lebesgue%20Integrals) of $\phi$ as $\phi$ becomes a better approximation of $f$.

>[!DEFINITION] Definition: Integration of Non-Negative Functions
>
>Let $(X, \Sigma, \mu)$ be a [measure space](../../Measure%20Theory/Measure%20Spaces.md) and let $f: \mathcal{D} \to \mathbb{R}_{\ge 0}$ be a [measurable](../../Measure%20Theory/Measurable%20Functions.md) (in the sense of the [Lebesgue measure](./Lebesgue%20Integral.md)) [real-valued function](./Real%20Functions/Real%20Functions.md) on a [measurable](../../Measure%20Theory/Measure%20Spaces.md) [subset](../../Set%20Theory/Sets.md#Subsets) $\mathcal{D} \subseteq X$.
>
>The **integral** of $f$ is the [supremum](../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md) of the [set](../../Set%20Theory/Sets.md) of all [integrals](./Lebesgue%20Integral.md) of [simple functions](./Lebesgue%20Integral.md) $s$ such that $0 \le s \le f$:
>
>$$
>\int f \mathop{\mathrm{d}\mu} \overset{\text{def}}{=} \sup \left\{ \int s \mathop{\mathrm{d}s} \mid s \text{ is simple and } 0 \le s \le f\right\}
>$$
>

Extending the above definition to [real-valued functions](./Real-Valued%20Functions.md) which can also take on negative values is fairly easy. Consider a [real function](./Real%20Functions/Real%20Functions.md) $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$. Essentially, we split $f$ into a negative and a non-negative part. We take the area between the horizontal axis and the graph of $f$'s non-negative part of $f$ and subtract from it the area between the horizontal axis and the graph of $f$'s negative part. This gives us a notion of the *signed area* between the horizontal axis and the graph of $f$ and thus yields a good definition for the integral of $f$.

![](./res/Signed%20Area.png)

>[!DEFINITION] Definition: Integration of General Functions
>
>Let $(X, \Sigma, \mu)$ be a [measure space](../../Measure%20Theory/Measure%20Spaces.md),  let $f: \mathcal{D} \to \mathbb{R}$ be a [measurable](../../Measure%20Theory/Measure%20Spaces.md) (in the sense of the [Lebesgue measure](./Lebesgue%20Integral.md)) [real-valued function](./Real%20Functions/Real%20Functions.md) on a [measurable](../../Measure%20Theory/Measure%20Spaces.md) [subset](../../Set%20Theory/Sets.md#Subsets) $\mathcal{D} \subseteq X$ and let $f^{-} = \max (-f, 0)$ and $f^{+} = \max (f, 0)$.
>
>The **(Lebesgue) integral** of $f$ **with respect to** $\mu$ is defined using the [integrals](./Lebesgue%20Integral.md) of $f^{-}$ and $f^{+}$ as
>
>$$
>\int f \mathop{\mathrm{d}\mu} \overset{\text{def}}{=} \int f^{+} \mathop{\mathrm{d}\mu} - \int f^{-} \mathop{\mathrm{d}\mu},
>$$
>
>provided that at least one of $\int f^{+} \mathop{\mathrm{d}\mu}$ or $\int f^{-} \mathop{\mathrm{d}\mu}$ is finite (in order to avoid $\infty - \infty$).
>
>We say that $f$ is $\mu$-**integrable** if its [integral](#Lebesgue%20Integrals) is finite.
>
>>[!DEFINITION] Definition: Integrating on a Subset
>>
>>Let $S$ be a [measurable](../../Measure%20Theory/Measure%20Spaces.md) [subset](../../Set%20Theory/Sets.md#Subsets) $S \subseteq X$.
>>
>>The **(Lebesgue) integral** of $f$ **over** $S$ **with respect to** $\mu$ is the [integral](#Lebesgue%20Integrals)
>>
>>$$
>>\int_{S} f \mathop{\mathrm{d}\mu} \overset{\text{def}}{=} \int f \cdot \mathbf{1}_S \mathop{\mathrm{d}\mu},
>>$$
>>
>>where $\mathbf{1}_S$ is the [indicator function](../../Set%20Theory/Sets.md#Subsets) of $S$.
>>
>>We say that $f$ is $\mu$**-integrable on** $S$ if its [integral](#Lebesgue%20Integrals) on $S$ is finite.
>>
>
>
>>[!NOTE] Note: Lebesgue Integral with Respect to the Lebesgue Measure
>>
>>When $X$ is $\mathbb{R}^n$ (or $\mathbb{R}$) and $\mu$ is the [Lebesgue measure](#Lebesgue%20Measure) on $\mathbb{R}^n$ (or $\mathbb{R}$), then we just say "Lebesgue integral" and omit "with respect to". Similarly, we just say that $f$ is "Lebesgue-integrable".
>>
>

>[!THEOREM] Theorem: Integrability Criterion
>
>Let $(X, \Sigma, \mu)$ be a [measure space](../../Measure%20Theory/Measure%20Spaces.md),  let $f: \mathcal{D} \to \mathbb{R}$ be a [measurable](../../Measure%20Theory/Measure%20Spaces.md) (in the sense of the [Lebesgue measure](./Lebesgue%20Integral.md)) [real-valued function](./Real%20Functions/Real%20Functions.md) on a [measurable](../../Measure%20Theory/Measure%20Spaces.md) [subset](../../Set%20Theory/Sets.md#Subsets) $\mathcal{D} \subseteq X$ and let $S$ be a [measurable](../../Measure%20Theory/Measure%20Spaces.md) [subset](../../Set%20Theory/Sets.md#Subsets) $S \subseteq X$.
>
>The [function](./Real%20Functions/Real%20Functions.md) $f$ is $\mu$-[integrable](./Lebesgue%20Integral.md) on $S$ if and only if the [integral](#Lebesgue%20Integrals) of its [absolute value](TODO) is $\mu$-[integrable](./Lebesgue%20Integral.md) on $S$:
>
>$$
>\int_S f \mathop{\mathrm{d}\mu} \lt \infty \iff \int_S |f| \mathop{\mathrm{d}\mu} \lt \infty
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
