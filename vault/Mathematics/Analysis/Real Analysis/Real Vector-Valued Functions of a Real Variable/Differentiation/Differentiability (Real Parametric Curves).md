---
tags:
    - real-analysis
    - vector-analysis
    - analysis
    - mathematics
---

# Differentiability (Real Parametric Curves)

>[!DEFINITION] Definition: Differentiability (Real Parametric Curves)
>
>Let $\gamma: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [real parametric curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) and let $p \in \mathcal{D}$ be an [accumulation point](../../../../Topology/Accumulation%20Points.md) of $\mathcal{D}$.
>
>We say that $\gamma$ is **differentiable** at $p$ if the [limit](../Limits%20of%20Parametric%20Curves.md)
>
>$$\lim_{t \to p} \frac{\gamma(t) - \gamma(p)}{t - p}$$
>
>exists. In this case, the value of this [limit](../Limits%20of%20Parametric%20Curves.md) is known as $\gamma$'s **derivative** at $p$.
>
>For $S \subseteq \mathcal{D}$, we say that $\gamma$ is **differentiable on** $S$ if it is [differentiable](#Differentiability%20(Real%20Parametric%20Curves)) at each $x \in S$.
>
>>[!NOTATION]
>>
>>We denote $\gamma$'s [derivative](#Differentiability%20(Real%20Parametric%20Curves)) at $p$ as $\gamma'(p)$ or $\dot{\gamma}(p)$. If a specific label such as $x$, $t$, etc. is used for $\gamma$'s input, then we also denote it in one of the following ways:
>>
>>$$\left.\frac{\mathrm{d}\gamma}{\mathrm{d}x}\right\vert_{x=p} \qquad \left.\frac{\mathrm{d}\gamma}{\mathrm{d}t}\right\vert_{t=p} \qquad \frac{\mathrm{d}\gamma}{\mathrm{d}x}(p)$$
>>
>

>[!THEOREM] Theorem: Differentiability at Interior Points
>
>A [parametric curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}^n$ is [differentiable](#Differentiability%20(Real%20Parametric%20Curves)) at an [interior point](../../../../Topology/Interior,%20Boundary,%20Exterior.md) $t_0$ of $\mathcal{D}$ if and only if it is [totally differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) there. In this case, the [derivative](../../Real%20Functions/Differentiability%20(Real%20Functions).md) of $\gamma$ is $\gamma$'s [Jacobian matrix](../../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md):
>
>$$\gamma'(t_0) = J_{\gamma}(t_0)$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>
>>- (I) If $\displaystyle \lim_{t \to t_0} \frac{\gamma(t) - \gamma(t_0)}{t - t_0}$ exists, then there is a [linear transformation](../../../Functional%20Analysis/Linearity/Linearity%20(Functions).md) $T: I \to \mathbb{R}^n$ such that 
>>
>>$$\lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - T(t - t_0)||}{|t- t_0|} = 0$$
>>
>>- (II) If there is a [linear transformation](../../../Functional%20Analysis/Linearity/Linearity%20(Functions).md) $T: I \to \mathbb{R}^n$ such that $\displaystyle \lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - T(t - t_0)||}{||t- t_0||} = 0$, then $\displaystyle \lim_{t \to t_0} \frac{\gamma(t) - \gamma(t_0)}{t - t_0}$ exists.
>>
>>**Proof of (I):**
>>
>>Let $\mathbf{L} = \lim_{t \to t_0} \frac{\gamma(t) - \gamma(t_0)}{t - t_0}$. Define $T: I \to \mathbb{R}^n$ as
>>
>>$$T(x) = x\mathbf{L}$$
>>
>>We can easily check that $T$ is a [linear transformation](../../../Functional%20Analysis/Linearity/Linearity%20(Functions).md):
>>
>>$$T(\alpha x + \beta y) = (\alpha x + \beta y)\mathbf{L} = \alpha x \mathbf{L} + \beta y \mathbf{L} = \alpha T(x) + \beta T(y)$$
>>
>>Then
>>
>>$$\begin{aligned}\lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - T(t - t_0)||}{||t- t_0||} &= \lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - (t - t_0)\mathbf{L}||}{|t- t_0|} \\ & = \lim_{t \to t_0} \frac{ |t-t_0| \cdot \left|\left|\frac{\gamma(t) - \gamma(t_0)}{t-t_0} - \mathbf{L}\right|\right|}{|t- t_0|} \\ & = \lim_{t \to t_0} \left|\left|\frac{\gamma(t) - \gamma(t_0)}{t-t_0} - \mathbf{L}\right|\right| \\ & = \left|\left| \lim_{t \to t_0} \left( \frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \mathbf{L}\right) \right|\right| \\ & = \left|\left|\lim_{t \to t_0} \left( \frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \frac{\gamma(t) - \gamma(t_0)}{t-t_0}\right)\right|\right| \\ & = ||\mathbf{0}|| = 0 \end{aligned}$$
>>
>>
>>**Proof of (II):**
>>
>>Let $\mathbf{T}$ be the [matrix representation](../../../Functional%20Analysis/Linearity/Linearity%20(Functions).md#Matrix%20Representations) of $T$ with respect to the [standard bases](../../../../Algebra/Matrices/Row%20and%20Column%20Vectors.md) of $\mathbb{R}$ and $\mathbb{R}^n$. Then,
>>
>>$$\lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - \mathbf{T}\begin{bmatrix}t-t_0\end{bmatrix}||}{|t- t_0|} = \lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - (t-t_0)\mathbf{T}||}{|t- t_0|} = 0$$
>>
>>Factor out $t-t_0$ from the numerator and move it outside the magnitude.
>>
>>$$\begin{aligned}\lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - (t-t_0)\mathbf{T}||}{|t- t_0|} &= \lim_{t - t_0} \frac{|t-t_0|\cdot \left|\left| \frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \mathbf{T} \right|\right|}{|t-t_0|} \\ & = \lim_{t \to t_0} \left|\left| \frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \mathbf{T} \right|\right| \\ & = \left|\left| \lim_{t \to t_0} \left( \frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \mathbf{T} \right) \right|\right| = 0\end{aligned}$$
>>
>>Therefore,
>>
>>$$\begin{aligned}& \lim_{t \to t_0} \left(\frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \mathbf{T}\right) = \mathbf{0} \\ & \lim_{t \to t_0} \left(\frac{\gamma(t) - \gamma(t_0)}{t - t_0}\right) - \mathbf{T} = \mathbf{0} \\ & \lim_{t \to t_0} \frac{\gamma(t) - \gamma(t_0)}{t - t_0} = \mathbf{T}\end{aligned}$$
>>
>

>[!THEOREM] Theorem: Differentiability $\implies$ Continuity
>
>Let $\gamma: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [parametric curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) and let $t \in \mathcal{D}$ be a [limit point](../../../../Topology/Accumulation%20Points.md) of $\mathcal{D}$.
>
>If $\gamma$ is [differentiable](#Differentiability%20(Real%20Parametric%20Curves)) at $t$, then it is also [continuous](../Continuity%20(Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable).md) there.
>
>>[!PROOF]-
>>
>>For $\gamma$ to be [continuous](../Continuity%20(Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable).md) at $t$, we need to prove the following [limit](../Limits%20of%20Parametric%20Curves.md):
>>
>>$$\lim_{x \to t} \gamma(x) = \gamma(t)$$
>>
>>We have:
>>
>>$$\lim_{x \to t} \gamma(x) = \gamma(t) \iff \left(\lim_{x \to t} \gamma(x)\right) - \gamma(t) = \boldsymbol{0} \iff \lim_{x \to t} \left(\gamma(x) - \gamma (t)\right) = \boldsymbol{0}$$
>>
>>We now examine the last [limit](../Limits%20of%20Parametric%20Curves.md):
>>
>>$$\lim_{x \to t} \left(\gamma(x) - \gamma (t)\right) = \lim_{x \to t} \left(\frac{\gamma(x) - \gamma (t)}{x - t} (x-t)\right)$$
>>
>>Since $\gamma$ is [differentiable](#Differentiability%20(Real%20Parametric%20Curves)) at $t$, we have:
>>
>>$$\begin{aligned}\lim_{x \to t} \left(\frac{\gamma(x) - \gamma (t)}{x - t} (x-t)\right) = &  \left(\lim_{x \to t} \frac{\gamma(x) - \gamma (t)}{x - t}\right) \left(\lim_{x \to t} (x-t) \right) \\ & = \gamma'(t) \cdot 0 \\ & = \boldsymbol{0}\end{aligned}$$
>>
>



>[!DEFINITION] Definition: Regularity
>
>A [vector-valued function](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}^n$ is **regular** if it is [differentiable](#Differentiation) on $\mathcal{D}$ and its [derivative](#Differentiation) is never zero.
>

>[!THEOREM] Theorem: Linearity of Differentiation
>
>If $\mathbf{u}$ and $\mathbf{v}$ are [differentiable](#Differentiability%20(Real%20Parametric%20Curves)) at some $t$, then for all $\mu,\lambda \in \mathbb{R}$:
>
>$$
>(\lambda\,\mathbf{u}(t) + \mu\,\mathbf{v}(t))' = \lambda\,\mathbf{u}'(t) + \mu\,\mathbf{v}'(t)
>$$
>
>
>>[!PROOF]-
>>
>>TODO
>>

>[!THEOREM] Theorem: Chain Rule
>
>Let $\gamma: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../../Real-Valued%20Functions.md) and let $\mathbf{r}: \mathcal{D}_{\mathbf{r}} \subseteq \mathbb{R} \to \mathbb{R}^n$ be [vector-valued](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md).
>
>If $\gamma$ is [differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) at some $t \in \mathcal{D}_f$ and $\mathbf{r}$ is [differentiable](#Differentiability%20(Real%20Parametric%20Curves)) at $\gamma(t)$, then their [composition](../../../Functions/Functions.md) is also [differentiable](#Differentiability%20(Real%20Parametric%20Curves)) at $t$ with
>
>$$
>(\mathbf{r} \circ f)(t)' = f'(t)\,\mathbf{r}'(f(t))
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Product Rule
>
>Let $\gamma: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../../Real-Valued%20Functions.md) and let $\mathbf{r}: \mathcal{D}_{\mathbf{r}} \subseteq \mathbb{R} \to \mathbb{R}^n$ be [vector-valued](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md).
>
>If $\gamma$ is [differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) at some $t \in \mathcal{D}_f$ and $\mathbf{r}$ is [differentiable](#Differentiability%20(Real%20Parametric%20Curves)) at $\gamma(t)$, then 
>
>$$
>(f(t)\mathbf{r}(t))' = f'(t)\mathbf{r}(t) + f(t)\mathbf{r}'(t)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Dot Product Rule
>
>Let $\mathbf{u}:\mathcal{D}_{\mathbf{u}} \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\mathbf{v}:\mathcal{D}_{\mathbf{v}} \subseteq \mathbb{R} \to \mathbb{R}^n$ be [vector-valued](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md).
>
>If $\mathbf{u}$ and $\mathbf{v}$ are both [differentiable](#Differentiability%20(Real%20Parametric%20Curves)) at some $t \in \mathcal{D}_{\mathbf{u}} \cap \mathcal{D}_{\mathbf{v}}$, then their [dot product](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) is also [differentiable](#Differentiability%20(Real%20Parametric%20Curves)) at $t$ with
>
>$$
>(\mathbf{u}(t)\cdot\mathbf{v}(t))' = \mathbf{u}'(t)\cdot \mathbf{v}(t) + \mathbf{u}(t)\cdot\mathbf{v}'(t)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Cross Product Rule
>
>Let $\mathbf{u}:\mathcal{D}_{\mathbf{u}} \subseteq \mathbb{R} \to \mathbb{R}^3$ and $\mathbf{v}:\mathcal{D}_{\mathbf{v}} \subseteq \mathbb{R} \to \mathbb{R}^3$ be [vector-valued](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md).
>
>If $\mathbf{u}$ and $\mathbf{v}$ are both [differentiable](#Differentiability%20(Real%20Parametric%20Curves)) at some $t \in \mathcal{D}_{\mathbf{u}} \cap \mathcal{D}_{\mathbf{v}}$, then their [cross product](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) is also [differentiable](#Differentiability%20(Real%20Parametric%20Curves)) at $t$ with
>
>$$
>(\mathbf{u}(t)\times \mathbf{v}(t))' = \mathbf{u}'(t)\times\mathbf{v}(t) + \mathbf{u}(t)\times\mathbf{v}'(t)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Higher Order Differentiability

>[!DEFINITION] Definition: Higher Order Differentiability (Real Parametric Curves)
>
>Let $\gamma: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [real parametric curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) and let $k \in \mathbb{N}_{\ge 0}$.
>
>For $k = 0$: We say that $\gamma$ is **0-times differentiable at** each $p \in \mathcal{D}$ and **0-times differentiable on** each $S \subseteq \mathcal{D}$. The **zeroth-order derivative function** of $\gamma$ is $\gamma$.
>
>For $k \ge 1$:
>
>We say that $\gamma$ is **$k$-times differentiable at** $p \in \mathcal{D}$ if $p$ is an [accumulation point](../../../../Topology/Accumulation%20Points.md) of the [domain](../../../Functions/Functions.md) $\mathcal{D}^{(k-1)}$ of $\gamma$'s $(k-1)$-th [derivative function](#Higher%20Order%20Differentiability) $\gamma^{(k-1)}: \mathcal{D}^{(k-1)} \to \mathbb{R}^n$ and $\gamma^{(k-1)}$ is [differentiable](#Differentiability) at $p$. In this case, the [derivative](#Differentiability) of $\gamma^{(k-1)}$ at $p$ is known as $\gamma$'s **$k$-th order derivative at** $p$. For $S \subseteq \mathcal{D}$, we say that $\gamma$ is **$k$-times differentiable on** $S$ if $\gamma$ is [$k$-times differentiable](#Higher%20Order%20Differentiability) at each $x \in S$.
>
>The **$k$-th order derivative function** of $\gamma$ is the [real parametric curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma^{(k)}: \mathcal{D}^{(k)} \to \mathbb{R}^n$ whose [domain](../../../Functions/Functions.md) $\mathcal{D}^{(k)}$ is the [set](../../../../Set%20Theory/Sets.md) of all $x \in \mathcal{D}$ at which $\gamma$ is [$k$-times differentiable](#Higher%20Order%20Differentiability) and which maps each $x \in \mathcal{D}^{(k)}$ to $\gamma$'s [$k$-th order derivative](#Higher%20Order%20Differentiability) at $x$.
>
>>[!NOTATION]
>>
>>The [derivative functions](#Higher%20Order%20Differentiability) are denoted as follows:
>>
>>$$\gamma' \qquad \gamma'' \qquad \gamma''' \qquad \gamma^{\text{IV}} \qquad \gamma^{\text{V}} \qquad \cdots \qquad \gamma^{(k)}$$
>>
>>$$\dot{\gamma} \qquad \ddot{\gamma} \qquad \dddot{\gamma} \qquad \cdots$$
>>
>>$$\frac{\mathrm{d}\gamma}{\mathrm{d}x} \qquad \frac{\mathrm{d}^2 \gamma}{\mathrm{d}x^2} \qquad \frac{\mathrm{d}^3 \gamma}{\mathrm{d}x^3} \qquad \frac{\mathrm{d}^4 \gamma}{\mathrm{d}x^4} \qquad  \frac{\mathrm{d}^5 \gamma}{\mathrm{d}x^5} \qquad \cdots \qquad \frac{\mathrm{d}^k \gamma}{\mathrm{d}x^k}$$
>>
>
>>[!DEFINITION] Definition: Infinite Differentiability
>>
>>We say that $\gamma$ is **infinitely differentiable at** $p \in \mathcal{D}$ if $\gamma$ is [$k$-times differentiable](#Higher%20Order%20Differentiability) at $p$ for all $k \in \mathbb{N}_{\ge 0}$.
>>
>>>[!NOTATION]
>>>
>>>When $\gamma$ is [infinitely differentiable](#Higher%20Order%20Differentiability) on $S$, we say that "$\gamma$ is $C^{\infty}$ on $S$" or we write $\gamma \in C^{\infty}(S)$.
>>>
>>>
>>
>

>[!DEFINITION] Definition: Continuous Higher Order Differentiability
>
>Let $\gamma: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}^n$ and let $n \in \mathbb{N}_{\ge 0}$.
>
>We say that $\gamma$ is **continuously $k$-times differentiable at** $p \in \mathcal{D}$ if $\gamma$ is [$k$-times differentiable](#Higher%20Order%20Differentiability) at $p$ and its [$k$-th order derivative function](#Higher%20Order%20Differentiability) is [continuous](../Continuity%20(Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable).md) at $p$.
>
>We say that $\gamma$ is **continuously $k$-times differentiable on** $S \subseteq \mathcal{D}$ if $\gamma$ is [$k$-times differentiable](#Higher%20Order%20Differentiability) on $S$ and its [$k$-th order derivative function](#Higher%20Order%20Differentiability) is [continuous](../Continuity%20(Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable).md) on $S$.
>
>>[!NOTATION]
>>
>>When $\gamma$ is [$k$-times continuously differentiable](#Higher%20Order%20Differentiability) on $S$, we say that "$\gamma$ is $C^k$ on $S$" or we write $\gamma \in C^k(S)$.
>>
>

## Orientation

>[!THEOREM] Theorem: Colinearity of Tangent Vectors
>
>Let $\gamma: \mathcal{D}_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\varphi: \mathcal{D}_{\varphi} \subseteq \mathbb{R} \to \mathbb{R}^n$ be [differentiable](#Differentiability%20(Real%20Parametric%20Curves)) [vector-valued functions](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) with the same [image](../../../Functions/Functions.md) $\mathcal{C} \subseteq \mathbb{R}^n$.
>
>If $\gamma$  and $\varphi$ are [equivalent](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md#Equivalence) up to a [regular](../../Real%20Functions/Differentiability%20(Real%20Functions).md) [reparametrization](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md#Equivalence), then for each $t \in \mathcal{D}_{\gamma}$ and each $s \in \mathcal{D}_{\varphi}$ with $\gamma(t) = \varphi(s)$ there exists some $\lambda \in \mathbb{R}$ such that
>
>$$
>\gamma'(t) = \lambda \, \varphi'(s)
>$$
>
>>[!PROOF]-
>>
>>Let's call this [reparametrization](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md#Equivalence) $h$, i.e $t = h(s)$ and so
>>
>>$$
>>\varphi(s) = \gamma(h(s))
>>$$
>>
>>[Differentiate](#Differentiability%20(Real%20Parametric%20Curves)) both sides and apply the [chain rule](#Differentiability%20(Real%20Parametric%20Curves)):
>>
>>$$
>>\varphi'(s) = h'(s) \gamma'(h(s))
>>$$
>>
>>Since $h$ is [regular](../../Real%20Functions/Differentiability%20(Real%20Functions).md), we know that $h'(s) \ne 0$ and so
>>
>>$$
>>\gamma'(h(s)) = \frac{1}{h'(s)} \varphi'(s)
>>$$
>>
>>Let $\lambda = \frac{1}{h'(s)}$ and substitute back $t = h(s)$ and the proof is complete:
>>
>>$$
>>\gamma'(t) = \lambda \, \varphi'(s)
>>$$
>>
>
>>[!IMPORTANT] Important: Unit Tangent Vectors
>>
>>It immediately follows that the [unit tangent vectors](#Frenet-Serret%20Basis) of $\gamma$ and $\varphi$ are either always equal or always opposite.
>>
>
>>[!DEFINITION] Definition: Orientation of Parametrizations
>>
>>We say that $\gamma$ and $\varphi$ have:
>>- the **same orientation** if their [unit tangent vectors](#Frenet-Serret%20Basis) are always equal. In this case, we also say that $\gamma$ and $\varphi$ are **equivalent up to an orientation-perserving reparametrization**.
>>- **opposite orientations** if their [unit tangent vectors](#Frenet-Serret%20Basis) are always opposite. In this case, we also say that $\gamma$ and $\varphi$ are  **equivalent up to an orientation-reversing reparametrization**.
>>
>>![](../res/Unit%20Tangent%20Vectors%20of%20Equivalent%20Parametrizations.svg)
>>
>