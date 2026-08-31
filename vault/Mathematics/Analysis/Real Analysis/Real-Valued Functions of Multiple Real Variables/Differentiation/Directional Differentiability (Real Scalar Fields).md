---
tags:
    - real-analysis
    - vector-analysis
    - analysis
    - mathematics
---

# Directional Differentiability (Real Scalar Fields)

>[!DEFINITION] Definition: Directional Differentiability of Real Scalar Fields
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), let $\boldsymbol{d} \in \mathbb{R}^n$ and let $\boldsymbol{p} \in \mathcal{D}$ be such that $0$ is an [accumulation point](../../../../Topology/Accumulation%20Points.md) of $\{h \in \mathbb{R}\mid \boldsymbol{p}+h\boldsymbol{d} \in \mathcal{D}\}$.
>
>We say that $f$ is **directionally differentiable at $\boldsymbol{p}$ along $\boldsymbol{d}$** if the [limit](../Limits%20(Real%20Scalar%20Fields).md)
>
>$$\lim_{t\to 0}\frac{f(\boldsymbol{p} + t \cdot \boldsymbol{d} ) - f(\boldsymbol{p})}{t}$$
>
>exists. The value of this [limit](../Limits%20(Real%20Scalar%20Fields).md) is known as $f$'s **directional derivative at $\boldsymbol{p}$ along $\boldsymbol{d}$**.
>
>>[!NOTATION]
>>
>>$$\frac{\partial f}{\partial \boldsymbol{d}}(\boldsymbol{p}) \qquad \partial_{\boldsymbol{d}}f(\boldsymbol{p}) \qquad f_{\boldsymbol{d}}(\boldsymbol{p}) \qquad D_{\boldsymbol{d}} f(\boldsymbol{p})$$
>>
>

>[!THEOREM] Theorem: Total Differentiability $\implies$ Directional Differentiability
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{p} \in \operatorname{int}\mathcal{D}$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}$.
>
>If $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$, then it is [directionally differentiable](./Directional%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ along each $\boldsymbol{r} \in \mathbb{R}^n$ and its [directional derivative](./Directional%20Differentiability%20(Real%20Scalar%20Fields).md) of $f$ along $\boldsymbol{r}$ is given by the [dot product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Dot%20Product.md) of $f$'s [gradient](./Gradient%20(Real%20Scalar%20Fields).md) and $\boldsymbol{r}$:
>
>$$\partial_{\boldsymbol{r}}f(\boldsymbol{p}) = \nabla f(\boldsymbol{p}) \cdot \boldsymbol{r}$$
>
>>[!EXAMPLE]- Example: $f(\boldsymbol{x}) = \boldsymbol{a}^{\mathsf{T}} \boldsymbol{x}$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^n \to \mathbb{R}$ defined as
>>
>>$$f(\boldsymbol{x}) = \boldsymbol{a}^{\mathsf{T}}\boldsymbol{x}$$
>>
>>for some fixed [real vector](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $\boldsymbol{a} = \begin{bmatrix} a^1 & \cdots & a^n \end{bmatrix}^{\mathsf{T}}\in \mathbb{R}^n$.
>>
>>It is [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^n$ and its [gradient](./Gradient%20(Real%20Scalar%20Fields).md) is the following:
>>
>>$$\nabla f(\boldsymbol{x}) = \boldsymbol{a}$$
>>
>>Its [directional derivatives](./Directional%20Differentiability%20(Real%20Scalar%20Fields).md) are thus the following:
>>
>>$$\partial_{\boldsymbol{r}} f(\boldsymbol{x}) = \nabla f(\boldsymbol{x}) \cdot \boldsymbol{r} = \boldsymbol{a} \cdot \boldsymbol{r}$$
>>
>
>>[!EXAMPLE]- Example: $f(\boldsymbol{x}) = \boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x}$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^n \to \mathbb{R}$ defined as
>>
>>$$f(\boldsymbol{x}) = \boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x}$$
>>
>>for some [real matrix](../../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) $\boldsymbol{A} \in \mathbb{R}^{n \times n}$.
>>
>>It is [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^n$ and its [gradient](./Gradient%20(Real%20Scalar%20Fields).md) is the following:
>>
>>$$\nabla f(\boldsymbol{x}) = (\boldsymbol{A} + \boldsymbol{A}^{\mathsf{T}})\boldsymbol{x}$$
>>
>>Therefore, its [directional derivatives](./Directional%20Differentiability%20(Real%20Scalar%20Fields).md) are as follows:
>>
>>$$\partial_{\boldsymbol{r}} f(\boldsymbol{x}) = \nabla f(\boldsymbol{x}) \cdot \boldsymbol{r} = \nabla f(\boldsymbol{x})^{\mathsf{T}} \cdot \boldsymbol{r} = \boldsymbol{x}^{\mathsf{T}}(\boldsymbol{A}^{\mathsf{T}} + \boldsymbol{A})\boldsymbol{r}$$
>>
>
>>[!EXAMPLE]- Example: Converse is False
>>
>>TODO
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$ defined as follows:
>>
>>$$f\left(x, y\right) = \begin{cases} \frac{x y^2}{x^2 + y^2} & \text{if } x \ne 0 \text{ and } y \ne 0 \\ 0 & \text{otherwise} \end{cases}$$
>>
>>For its [directional derivatives](./Directional%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{0}$, we have:
>>
>>$$\begin{aligned}\partial_{\boldsymbol{r}}f(\boldsymbol{0}) & = \lim_{h \to 0} \frac{f(\boldsymbol{0} + h\boldsymbol{r}) - f(\boldsymbol{0})}{h} \\ & = \lim_{h \to 0} \frac{\frac{(hr_1)(hr_2)^2}{h^2 r_1^2 + h^2 r_2^2} - 0}{h} \\ & = \lim_{h \to 0} \frac{\frac{h^3 r_1 r_2^2}{h^2(r_1^2 + r_2^2)}}{h} \\ & = \lim_{h \to 0} \frac{\frac{h r_1 r_2^2}{r_1^2 + r_2^2}}{h} \\ & = \lim_{h \to 0}\frac{hr_1 r_2^2}{h(r_1^2 + r_2^2)} \\ & = \lim_{h \to 0} \frac{r_1 r_2^2}{r_1^2 + r_2^2} \\ & = \frac{r_1 r_2^2}{r_1^2 + r_2^2} \\ & = f(\boldsymbol{r})\end{aligned}$$
>>
>>Therefore, all of $f$'s [directional derivatives](./Directional%20Differentiability%20(Real%20Scalar%20Fields).md) $\boldsymbol{0}$ exist. More specifically, its [partial derivatives](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) are the following:
>>
>>$$\frac{\partial f}{\partial x}(\boldsymbol{0}) = \partial_{\boldsymbol{e}_1} f(\boldsymbol{0}) = f(\boldsymbol{e}_1) = \frac{1 \cdot 0^2}{1^2 + 0^2} = 0$$
>>
>>$$\frac{\partial f}{\partial y}(\boldsymbol{0}) = \partial_{\boldsymbol{e}_2} f(\boldsymbol{0}) = f(\boldsymbol{e}_2) = \frac{0 \cdot 1^2}{0^2 + 1^2} = 0$$
>>
>>Therefore, $f$'s [gradient](./Gradient%20(Real%20Scalar%20Fields).md) is the following:
>>
>>$$\nabla f(\boldsymbol{0}) = \begin{bmatrix}\partial_{x}f(\boldsymbol{0}) \\ \partial_y f(\boldsymbol{0})\end{bmatrix} = \begin{bmatrix}0 \\ 0\end{bmatrix} = \boldsymbol{0}$$
>>
>>The [directional derivatives](./Directional%20Differentiability%20(Real%20Scalar%20Fields).md) of $f$ would then have to be given by
>>
>>$$\partial_{\boldsymbol{r}}f(\boldsymbol{0}) = \nabla f(\boldsymbol{0}) \cdot \boldsymbol{r} = \boldsymbol{0} \cdot \boldsymbol{r} = 0$$
>>
>>but we just proved that $f$'s [directional derivatives](./Directional%20Differentiability%20(Real%20Scalar%20Fields).md) are given by the following:
>>
>>$$\partial_{\boldsymbol{r}}f(\boldsymbol{0}) = f(\boldsymbol{r})$$
>>
>>In general, this is not equal to $0$ and so we have reached a contradiction. Therefore, $f$ is not [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{0}$ even though all of its [directional derivatives](./Directional%20Differentiability%20(Real%20Scalar%20Fields).md) there exist.
>>
>>To confirm this, we assume that $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{0}$. Therefore, there its [gradient](./Gradient%20(Real%20Scalar%20Fields).md) $\nabla f(\boldsymbol{0})$ exists and, since we just showed that $\nabla f(\boldsymbol{0}) = \boldsymbol{0}$, we know that $f(\boldsymbol{0} + \boldsymbol{h}) - f(\boldsymbol{0}) - \nabla f(\boldsymbol{0})^{\mathsf{T}}\boldsymbol{h}$ is [little o](../../Asymptotic%20Analysis/Bachmann-Landau%20Notation.md) of $||\boldsymbol{h}||$ for $\boldsymbol{h} \to \boldsymbol{0}$:
>>
>>$$f(\boldsymbol{0} + \boldsymbol{h}) - f(\boldsymbol{0}) - \nabla f(\boldsymbol{0})^{\mathsf{T}}\boldsymbol{h} = o(||\boldsymbol{h}||) \qquad \text{for} \qquad \boldsymbol{h} \to \boldsymbol{0}$$
>>
>>$$f(\boldsymbol{h}) - 0 - \boldsymbol{0}^{\mathsf{T}}\boldsymbol{h} = o(||\boldsymbol{h}||) \qquad \text{for} \qquad \boldsymbol{h} \to \boldsymbol{0}$$
>>
>>$$f(\boldsymbol{h}) = o(||\boldsymbol{h}||) \qquad \text{for} \qquad \boldsymbol{h} \to \boldsymbol{0}$$
>>
>>This implies the following [limit](../Limits%20(Real%20Scalar%20Fields).md):
>>
>>$$\lim_{\boldsymbol{h} \to \boldsymbol{0}} \frac{f(\boldsymbol{h})}{||\boldsymbol{h}||} = 0$$
>>
>>Let's examine the following [real vector sequence](../../Real%20Vector%20Sequences.md) $(\boldsymbol{h}_k)_{k \in \mathbb{N}}$:
>>
>>$$\boldsymbol{h}_k = \begin{bmatrix}\frac{1}{k} \\ \frac{1}{k}\end{bmatrix}$$
>>
>>Its [limit](../../Real%20Vector%20Sequences.md) for $k \to \infty$ is obviously $\boldsymbol{0}$. Furthermore, we have the following [limit](../../Real%20Functions/Limits%20(Real%20Functions.md):
>>
>>$$\begin{aligned}\lim_{k \to \infty} \frac{f(\boldsymbol{h}_k)}{||\boldsymbol{h}_k||} & = \lim_{k \to \infty} \frac{\frac{\frac{1}{k} \cdot \frac{1}{k^2}}{\frac{1}{k^2} + \frac{1}{k^2}}}{\sqrt{\frac{1}{k^2} + \frac{1}{k^2}}} \\ & = \lim_{k \to \infty} \frac{\frac{1/k^3}{2/k^2}}{\sqrt{2/k^2}} \\ & = \lim_{k \to \infty} \frac{\frac{1}{2k}}{\frac{\sqrt{2}}{k}} \\ & = \lim_{k \to \infty} \frac{1}{2\sqrt{2}} \\ & = \frac{\sqrt{2}}{4}\end{aligned}$$
>>
>>Since $\frac{\sqrt{2}}{4} \ne 0$, we know that $\lim_{\boldsymbol{h} \to \boldsymbol{0}} \frac{f(\boldsymbol{h})}{||\boldsymbol{h}||} \ne 0$ and so we reached a contradiction. Therefore, $f$ cannot be [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{0}$.
>>
>
>>[!PROOF]-
>>
>>Since $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$, we have that $f(\boldsymbol{p} + \boldsymbol{h}) - f(\boldsymbol{p}) - \nabla f(\boldsymbol{p})^{\mathsf{T}}\boldsymbol{h}$ is [little o](../../Asymptotic%20Analysis/Bachmann-Landau%20Notation.md#Little%20o%20Notation) of $||\boldsymbol{h}||$ for $\boldsymbol{h} \to \boldsymbol{0}$:
>>
>>$$f(\boldsymbol{p} + \boldsymbol{h}) - f(\boldsymbol{p}) - \nabla f(\boldsymbol{p})^{\mathsf{T}}\boldsymbol{h} = o(||\boldsymbol{h}||) \qquad \text{for} \qquad \boldsymbol{h} \to \boldsymbol{0}$$
>>
>>This implies that
>>
>>$$f(\boldsymbol{p} + h\boldsymbol{r}) - f(\boldsymbol{p}) - \nabla f(\boldsymbol{p})^{\mathsf{T}}(h\boldsymbol{r}) = o(h||\boldsymbol{r}||) \qquad \text{for} \qquad h \to 0$$
>>
>>and so
>>
>>$$f(\boldsymbol{p} + h\boldsymbol{r}) - f(\boldsymbol{p}) - h\nabla f(\boldsymbol{p})^{\mathsf{T}}\boldsymbol{r} = ||\boldsymbol{r}|| o(h) \qquad \text{for} \qquad h \to 0$$
>>
>>and
>>
>>$$f(\boldsymbol{p} + h\boldsymbol{r}) - f(\boldsymbol{p}) - h\nabla f(\boldsymbol{p})^{\mathsf{T}}\boldsymbol{r} = o(h) \qquad \text{for} \qquad h \to 0.$$
>>
>>This implies the following:
>>
>>$$\lim_{h \to 0} \frac{f(\boldsymbol{p} + h\boldsymbol{r}) - f(\boldsymbol{p}) - h\nabla f(\boldsymbol{p})^{\mathsf{T}}\boldsymbol{r}}{h} = 0$$
>>
>>We have:
>>
>>$$\begin{aligned}\partial_{\boldsymbol{r}} f(\boldsymbol{p}) & =  \lim_{h \to 0} \frac{f(\boldsymbol{p} + h\boldsymbol{r}) - f(\boldsymbol{p})}{h} \\ & = \lim_{h \to 0} \left(\frac{f(\boldsymbol{p} + h\boldsymbol{r}) - f(\boldsymbol{p}) - h\nabla f(\boldsymbol{p})^{\mathsf{T}}\boldsymbol{r}}{h} + \frac{h\nabla f(\boldsymbol{p})^{\mathsf{T}}\boldsymbol{r}}{h}\right) \\ & = \lim_{h \to 0} \frac{f(\boldsymbol{p} + h\boldsymbol{r}) - f(\boldsymbol{p}) - h\nabla f(\boldsymbol{p})^{\mathsf{T}}\boldsymbol{r}}{h} + \lim_{h \to 0} \frac{h\nabla f(\boldsymbol{p})^{\mathsf{T}}\boldsymbol{r}}{h} \\ & = 0 + \nabla f(\boldsymbol{p})^{\mathsf{T}} \boldsymbol{r} \\ & = \nabla f(\boldsymbol{p})^{\mathsf{T}} \boldsymbol{r} \\ & = \nabla f(\boldsymbol{p}) \cdot \boldsymbol{r}\end{aligned}$$
>>
>