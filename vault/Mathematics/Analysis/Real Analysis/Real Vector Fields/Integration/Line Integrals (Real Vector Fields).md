---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Line Integrals (Real Vector Fields)

TODO: Make this more rigorous

>[!DEFINITION] Definition: Line Integral of a Real Vector Field
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../Real%20Vector%20Fields.md) and let $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [real parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) which is [differentiable](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) on the [interior](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of the [interval](../../Euclidean%20Space/Euclidean%20Space.md) $I$.
>
>The **line integral** of $f$ **along** $\gamma$ is the [(potentially improper) Riemann integral](../../Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md)
>
>$$\int_I f(\gamma(t)) \cdot \gamma'(t) \, \mathrm{d}t,$$
>
>of the [dot product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Dot%20Product.md) between $f \circ \gamma$ and $\gamma'$, provided that it exists.
>
>>[!NOTATION]
>>
>>We denote the [line integral](./Line%20Integrals%20(Real%20Vector%20Fields).md) of $f$ along $\gamma$ as follows:
>>
>>$$\int_{\gamma} f \cdot \mathrm{d}\boldsymbol{r}$$
>>
>>If $\gamma$ is [closed](TODO), we write:
>>
>>$$\oint_{\gamma} f \cdot \mathrm{d}\boldsymbol{r}$$
>>
>
>>[!EXAMPLE]-
>>
>>Consider the [real vector field](../Real%20Vector%20Fields.md) $f: \mathbb{R}^3 \to \mathbb{R}^3$ defined as
>>
>>$$f(x,y,z) = \begin{bmatrix}xy \\ x - z \\ xz\end{bmatrix}$$
>>
>>and the [parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma: [0,2] \to \mathbb{R}^3$ defined as follows:
>>
>>$$\gamma(t) = \begin{bmatrix}t \\ t^3 \\ 3\end{bmatrix}$$
>>
>>We have:
>>
>>$$f(\gamma(t)) = \begin{bmatrix}t^4 \\ t - 3 \\ 3t\end{bmatrix} \qquad \gamma'(t) = \begin{bmatrix}1 \\ 3t^2 \\ 0 \end{bmatrix}$$
>>
>>Both $f\circ \gamma$ and $\gamma'$ are [continuous](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Continuity%20(Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable).md). Therefore, $(f \circ \gamma) \cdot \gamma'$ is also [continuous](../../Real%20Functions/Continuity%20(Real%20Functions).md) and we have
>>
>>$$\begin{aligned}\int_{\gamma} f \cdot \mathrm{d}\boldsymbol{r} & = \int_0^2 f(\gamma(t)) \cdot \gamma'(t)\,\mathrm{d}t \\ & = \int_0^2 (t^4 \cdot 1 + (t-3)\cdot 3t^2 + 3t\cdot 0) \,\mathrm{d}t \\ & = \int_0^2 (t^4 + 3t^3 - 9t^2) \,\mathrm{d}t \\ & = \left.\left( \frac{t^5}{5} + \frac{3t^4}{4} - 3t^3 \right)\right\vert_0^2 \\ & = \left( \frac{32}{5} + 12 - 24 \right) - 0 \\ & = \frac{32}{5} - 12 \\ & = -\frac{28}{5}\end{aligned}$$
>>
>>for the [line integral](./Line%20Integrals%20(Real%20Vector%20Fields).md) of $f$ along $\gamma$.
>>
>
>>[!EXAMPLE]-
>>
>>Consider the [real vector field](../Real%20Vector%20Fields.md) $f: \mathbb{R}^2 \to \mathbb{R}^2$ defined as
>>
>>$$f(x,y) = \begin{bmatrix}-y \\ x\end{bmatrix}$$
>>
>>and the [parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma: [0,2\uppi] \to \mathbb{R}^2$ defined as follows:
>>
>>$$\gamma(t) = \begin{bmatrix}\cos t \\ \sin t\end{bmatrix}$$
>>
>>Since $\gamma(0) = \gamma(2\uppi)$, we know that $\gamma$ is [closed](TODO).
>>
>>We have:
>>
>>$$f(\gamma(t)) = \begin{bmatrix}-\sin t \\ \cos t\end{bmatrix} \qquad \gamma'(t) = \begin{bmatrix}-\sin t \\ \cos t\end{bmatrix}$$
>>
>>Both $f\circ \gamma$ and $\gamma'$ are [continuous](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Continuity%20(Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable).md). Therefore, $(f \circ \gamma) \cdot \gamma'$ is also [continuous](../../Real%20Functions/Continuity%20(Real%20Functions).md) and we have
>>
>>$$\begin{aligned}\oint_{\gamma} f \cdot \mathrm{d}\boldsymbol{r} & = \int_0^{2\uppi} f(\gamma(t)) \cdot \gamma'(t)\,\mathrm{d}t \\ & = \int_0^{2\uppi} ((-\sin t)(-\sin t) + (\cos t)(\cos t)) \,\mathrm{d}t \\ & = \int_0^{2\uppi} (\sin^2 t + \cos^2 t) \,\mathrm{d}t \\ & = \int_0^{2\uppi} 1 \,\mathrm{d}t \\ & = \left. t \right\vert_0^{2\uppi} \\ & = 2\uppi - 0 \\ & = 2\uppi\end{aligned}$$
>>
>>for the [line integral](./Line%20Integrals%20(Real%20Vector%20Fields).md) of $f$ along $\gamma$.
>>
>
>>[!EXAMPLE]-
>>
>>Consider the [real vector field](../Real%20Vector%20Fields.md) $f: \mathbb{R}^2 \to \mathbb{R}^2$ defined as
>>
>>$$f(x,y) = \begin{bmatrix}3x \\ 0\end{bmatrix}$$
>>
>>and the [parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma: [0,2\uppi] \to \mathbb{R}^2$ defined as follows:
>>
>>$$\gamma(t) = \begin{bmatrix}\cos t \\ \sin t\end{bmatrix}$$
>>
>>Since $\gamma(0) = \gamma(2\uppi)$, we know that $\gamma$ is [closed](TODO).
>>
>>We have:
>>
>>$$f(\gamma(t)) = \begin{bmatrix}3\cos t \\ 0\end{bmatrix} \qquad \gamma'(t) = \begin{bmatrix}-\sin t \\ \cos t\end{bmatrix}$$
>>
>>Both $f\circ \gamma$ and $\gamma'$ are [continuous](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Continuity%20(Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable).md). Therefore, $(f \circ \gamma) \cdot \gamma'$ is also [continuous](../../Real%20Functions/Continuity%20(Real%20Functions).md) and we have
>>
>>$$\begin{aligned}\int_{\gamma} f \cdot \mathrm{d}\boldsymbol{r} & = \int_0^{2\uppi} f(\gamma(t)) \cdot \gamma'(t)\,\mathrm{d}t \\ & = \int_0^{2\uppi} ((3\cos t)(-\sin t) + (0)(\cos t)) \,\mathrm{d}t \\ & = \int_0^{2\uppi} -3\sin t \cos t \,\mathrm{d}t \\ & = \left. -\frac{3}{2}\sin^2 t \right\vert_0^{2\uppi} \\ & = 0 - 0 \\ & = 0\end{aligned}$$
>>
>>for the [line integral](./Line%20Integrals%20(Real%20Vector%20Fields).md) of $f$ along $\gamma$.
>>
>


>[!THEOREM] Theorem: Linearity of Line Integrals
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}^n$ and $g: \mathcal{D}_g \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be [real vector fields](../Real%20Vector%20Fields.md) and let $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [real parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) which is [differentiable](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) on the [interior](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of the [interval](../../Euclidean%20Space/Euclidean%20Space.md) $I$ with $\gamma(I) \subseteq \mathcal{D}_f \cap \mathcal{D}_g$.
>
>If the [line integrals](./Line%20Integrals%20(Real%20Vector%20Fields).md) of $f$ and $g$ along $\gamma$ exist, then so does the [line integral](./Line%20Integrals%20(Real%20Vector%20Fields).md) of $\alpha f + \beta g$ for all $\alpha, \beta \in \mathbb{R}$:
>
>$$\int_{\gamma} (\alpha f + \beta g) \cdot \mathrm{d}\mathbf{r} = \alpha \int_{\gamma} f \cdot \mathrm{d}\mathbf{r} + \beta \int_{\gamma} g \cdot \mathrm{d}\mathbf{r}$$
>
>>[!PROOF]-
>>
>>$$\begin{aligned}\int_{\gamma} (\alpha f + \beta g) \cdot \mathrm{d}\mathbf{r} & = \int_I((\alpha f + \beta g) \circ \gamma)(t) \cdot \gamma'(t)\,\mathrm{d}t \\ & = \int_I(\alpha f (\gamma(t)) + \beta g(\gamma(t))) \cdot \gamma'(t)\,\mathrm{d}t \\ & = \int_I \left( \alpha (f (\gamma(t)) \cdot \gamma'(t)) + \beta (g(\gamma(t)) \cdot \gamma'(t)) \right) \,\mathrm{d}t \\ & = \int_I\alpha (f (\gamma(t)) \cdot \gamma'(t)) \,\mathrm{d}t + \int_I\beta (g(\gamma(t)) \cdot \gamma'(t)) \,\mathrm{d}t \end{aligned}$$
>>
>>Since the [line integrals](./Line%20Integrals%20(Real%20Vector%20Fields).md) of $f$ and $g$ along $\gamma$ exist, we know that
>>
>>$$\int_I f (\gamma(t)) \cdot \gamma'(t) \,\mathrm{d}t= \int_{\gamma} f \cdot \mathrm{d}\mathbf{r}$$
>>
>>and
>>
>>$$\int_I g (\gamma(t)) \cdot \gamma'(t) \,\mathrm{d}t = \int_{\gamma} g \cdot \mathrm{d}\mathbf{r}$$
>>
>>exist. Therefore:
>>
>>$$\begin{aligned}\int_{\gamma} (\alpha f + \beta g) \cdot \mathrm{d}\mathbf{r} & = \alpha \int_If (\gamma(t)) \cdot \gamma'(t) \,\mathrm{d}t + \beta \int_I g (\gamma(t)) \cdot \gamma'(t) \,\mathrm{d}t \\ & = \alpha \int_{\gamma} f \cdot \mathrm{d}\mathbf{r} + \beta \int_{\gamma} g \cdot \mathrm{d}\mathbf{r}\end{aligned}$$
>>
>

>[!THEOREM] Theorem: Vector Line Integral $=$ Scalar Line Integral
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../Real%20Vector%20Fields.md) and let $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [real parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) which is [differentiable](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) on the [interior](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of the [interval](../../Euclidean%20Space/Euclidean%20Space.md) $I$.
>
>The [line integral](./Line%20Integrals%20(Real%20Vector%20Fields).md) of $f$ over $\gamma$ (provided it exists) is equal to the [line integral](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Integration/Line%20Integrals%20(Real%20Scalar%20Fields).md) of the [dot product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Dot%20Product.md) between $f$ and $\gamma$'s [unit tangent vector](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Frenet-Serret%20Bases.md) over $\gamma$ (provided it exists):
>
>$$\int_{\gamma} f \cdot \,\mathrm{d}\boldsymbol{r} = \int_{\gamma} f \cdot \boldsymbol{T} \, \mathrm{d}s$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Green's Theorem
>
>TODO: Make more rigorous
>
>Let $\mathcal{D} \subset \mathbb{R}^2$ be [Lebesgue-measurable](../../../../Measure%20Theory/Lebesgue%20Measure.md) and such that its [boundary](../../../../Topology/Interior,%20Boundary,%20Exterior.md) can be [parameterized](TODO) by a [piecewise regular](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md), [simple](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) [closed](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) [parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma: [a,b] \subseteq \mathbb{R} \to \mathbb{R}^2$ with [positive orientation](TODO). Let $f: \mathcal{D} \to \mathbb{R}^2$ be a [real vector field](../Real%20Vector%20Fields.md) with [component functions](../../Real%20Vector-Valued%20Functions.md) $f_1$ and $f_2$.
>
>If $f$ is [continuously differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) on $\mathcal{D}$, then its [line integral](./Line%20Integrals%20(Real%20Vector%20Fields).md) over $\gamma$ is given by the following [integral](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Integration/Lebesgue%20Integrals%20(Real%20Scalar%20Fields).md) of the [partial derivatives](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) of $f_1$ and $f_2$:
>
>$$\int_{\gamma} f \cdot \,\mathrm{d}\boldsymbol{\gamma} = \iint_{\mathcal{D}} \partial_1 f_2 - \partial_2 f_1 \, \mathrm{d}\mathcal{D}$$
>
>>[!EXAMPLE]- Example
>>
>>Consider the square $\mathcal{D} = [0,1]^2 \subset \mathbb{R}^2$. The [boundary](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$ can be [parameterized](TODO) by the following [parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md):
>>
>>$$\gamma:[0,4] \to \mathbb{R}^2 \qquad \gamma(t) = \begin{cases} \begin{bmatrix} t & 0 \end{bmatrix}^{\mathsf{T}}, & t \in [0,1] \\ \begin{bmatrix} 1 & t-1 \end{bmatrix}^{\mathsf{T}}, & t \in [1,2] \\ \begin{bmatrix} 3 - t & 1 \end{bmatrix}^{\mathsf{T}}, & t \in [2,3] \\ \begin{bmatrix} 0 & 4 - t \end{bmatrix}^{\mathsf{T}}, & t \in [3,4]\end{cases}$$
>>
>>We see that $\gamma$ is [piecewise regular](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md), [simple](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md), [closed](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) and with [positive orientation](TODO).
>>
>>Let $f: \mathcal{D} \to \mathbb{R}^2$ be a [real vector field](../Real%20Vector%20Fields.md) defined as
>>
>>$$f(x, y) = \begin{bmatrix}f_1(x, y) \\ 0\end{bmatrix}$$
>>
>>for some [continuously differentiable](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md) [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f_1$.
>>
>>The conditions for the theorem are satisfied and for the [line Integral](./Line%20Integrals%20(Real%20Vector%20Fields).md) of $f$ over $\gamma$, we have:
>>
>>$$\begin{aligned} \int_{\gamma} f \cdot \,\mathrm{d}\boldsymbol{\gamma} & = \iint_{\mathcal{D}} \partial_1 f_2 - \partial_2 f_1 \, \mathrm{d}\mathcal{D} \\ & = \iint_{[0,1]^2} - \partial_2 f_1(x,y) \, \mathrm{d}\mathcal{D} \end{aligned}$$
>>
>>Since $\partial_2 f_1(x,y)$ is [continuous](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Continuity%20(Real%20Scalar%20Fields).md), we get the following [iterated integral](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Integration/Parametric%20Integrals.md):
>>
>>$$\begin{aligned}\iint_{[0,1]^2} - \partial_2 f_1(x,y) \, \mathrm{d}\mathcal{D} & = \int_0^1 \left( \int_0^1 - \partial_2 f_1(x,y) \, \mathrm{d}y \right) \, \mathrm{d}x \\ & = \int_0^1 -(f_1(x, 1)- f_1(x,0) )\,\mathrm{d}x \\ & = \int_0^1 f_1(x, 0) -f_1(x,1)\,\mathrm{d}x \end{aligned}$$
>>
>>We can also verify this via the definition of the [line integral](./Line%20Integrals%20(Real%20Vector%20Fields).md):
>>
>>$$\begin{aligned} \int_{\gamma} f \cdot \mathrm{d}\boldsymbol{\gamma} &= \int_{0}^{4} f(\gamma(t)) \cdot \gamma'(t) \,\mathrm{d}t \\ &= \int_{0}^{1} f(t, 0) \cdot \begin{bmatrix} 1 \\ 0 \end{bmatrix} \,\mathrm{d}t + \int_{1}^{2} f(1, t-1) \cdot \begin{bmatrix} 0 \\ 1 \end{bmatrix} \,\mathrm{d}t + \int_{2}^{3} f(3-t, 1) \cdot \begin{bmatrix} -1 \\ 0 \end{bmatrix} \,\mathrm{d}t + \int_{3}^{4} f(0, 4-t) \cdot \begin{bmatrix} 0 \\ -1 \end{bmatrix} \,\mathrm{d}t \\ &= \int_{0}^{1} f_1(t, 0) \,\mathrm{d}t - \int_{2}^{3} f_1(3-t, 1) \,\mathrm{d}t \\ &= \int_{0}^{1} f_1(t, 0) \,\mathrm{d}t - \int_{0}^{1} f_1(s, 1) \,\mathrm{d}s \\ & = \int_0^1 f_1(x, 0) -f_1(x,1)\,\mathrm{d}x \end{aligned}$$
>>
>
>>[!EXAMPLE]- Example: Area via Line Integral
>>
>>The theorem can also be used to find the [area](../../../../Measure%20Theory/Lebesgue%20Measure.md) of a [bounded](TODO) [Lebesgue-measurable](../../../../Measure%20Theory/Lebesgue%20Measure.md) [subset](../../../../Set%20Theory/Subsets.md) $\mathcal{D} \subseteq \mathbb{R}^2$.
>>
>>Specifically, if $f: \mathcal{D} \to \mathbb{R}^2$ is a [continuously differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) [real vector field](../Real%20Vector%20Fields.md) such that the [partial derivatives](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) of its [component functions](../../Real%20Vector-Valued%20Functions.md) $f_1$, $f_2$ obey $\partial_1 f_2 - \partial_2 f_1 = 1$, then the [area](../../../../Measure%20Theory/Lebesgue%20Measure.md) of $\mathcal{D}$ is given by the [line integral](./Line%20Integrals%20(Real%20Vector%20Fields).md) of $f$ over any [parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) which [parameterizes](TODO) the [boundary](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$. 
>>
>>For example, we can pick $f: \mathcal{D} \to \mathbb{R}^2$ defined as follows:
>>
>>$$f(x,y) = \frac{1}{2}\begin{bmatrix}-y \\ x\end{bmatrix}$$
>>
>>We have:
>>
>>$$\partial_x f_2(x,y) - \partial_y f_1(x,y) = \frac{1}{2} - \left(-\frac{1}{2}\right) = 1$$
>>
>>Now consider the following [ellipse](TODO):
>>
>>$$\mathcal{D} = \left\{\begin{bmatrix} x \\ y \end{bmatrix} \in \mathbb{R}^2 : \frac{x^2}{a^2} + \frac{y^2}{b^2} \le 1\right\}$$
>>
>>Its [boundary](../../../../Topology/Interior,%20Boundary,%20Exterior.md) can be [parameterized](TODO) by the following [parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md):
>>
>>$$\gamma: [0, 2\uppi] \to \mathbb{R}^2 \qquad \gamma(t) = \begin{bmatrix}a \cos t \\ b \sin t\end{bmatrix}$$
>>
>>We see that the conditions for the theorem are fulfilled. Therefore:
>>
>>$$\begin{aligned}A(\mathcal{D}) & = \iint_{\mathcal{D}} 1 \, \mathrm{d}\mathcal{D} \\ & = \iint_{\mathcal{D}} \partial_x f_2(x,y) - \partial_y f_1(x,y) \, \mathrm{d}\mathcal{D} \\ & = \int_{\gamma}f \cdot \,\mathrm{d}\boldsymbol{\gamma} \\ & = \int_{0}^{2\uppi} f(\gamma(t)) \cdot \gamma'(t)\,\mathrm{d}t \\ & = \int_{0}^{2\uppi} \frac{1}{2} \begin{bmatrix}-b \sin t \\ a \cos t\end{bmatrix} \cdot \begin{bmatrix} - a \sin t \\ b \cos t \end{bmatrix} \, \mathrm{d}t \\ & = \frac{1}{2}\int_0^{2\uppi} ab (\sin^2 t + \cos^2 t) \, \mathrm{d}t \\ & = \frac{1}{2}abt\vert_{0}^{2\uppi} \\ & = \frac{1}{2}\cdot 2 \uppi ab \\ & = \uppi ab\end{aligned}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>


