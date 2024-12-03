>[!DEFINITION] Definition: Local Minimum
>Let $f: D\subseteq\mathbb{R}^n\to\mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md).
>
>We say that $f(\vec{x}_0)$ is a **local minimum** of $f$ if there is an [open ball](../../../../../Topology/Metric%20Spaces/Open%20Ball.md) $B_\varepsilon (\vec{x}_0)$ around $\vec{x}_0\in D$ where $f(\vec{x}_0)$ is the smallest funtional value.
>
>$$f(\vec{x}_0) \le f(\vec{x}) \qquad \forall \vec{x}\in B_\varepsilon (\vec{x}_0)$$
>
>We say that $\vec{x}_0$ is a **place of a local minimum** for $f$.
>

>[!DEFINITION] Definition: Global Maximum
>Let $f: D\subseteq\mathbb{R}^n\to\mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md).
>
>We say that $f(\vec{x}_0)$ is a **local maximum** of $f$ if there is an [open ball](../../../../../Topology/Metric%20Spaces/Open%20Ball.md) $B_\varepsilon (\vec{x}_0)$ around $\vec{x}_0\in D$ where $f(\vec{x}_0)$ is the greatest funtional value.
>
>$$f(\vec{x}_0) \ge f(\vec{x}) \qquad \forall \vec{x}\in B_\varepsilon (\vec{x}_0)$$
>
>We say that $\vec{x}_0$ is a **place of a local maximum** for $f$.
>

>[!DEFINITION] Definition: Local Extremum
>
>The [local minima](Local%20Extrema.md) and [local maxima](Local%20Extrema.md) of a [real scalar field](../Real%20Scalar%20Field.md) are collectively known as its **local extrema**.
>

>[!THEOREM] Theorem: Locations of Local Extrema
>
>All [local extrema](Local%20Extrema.md) of a [real scalar field](../Real%20Scalar%20Field.md) occur at [critical points](../Differentiation/Critical%20Point.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Hessian Matrix Criteria for Local Extrema
>Let $f: D\subseteq\mathbb{R}^n\to\mathbb{R}$ be a [twice continuously partially differentiable](../Differentiation/Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) [real scalar field](../Real%20Scalar%20Field.md) on an [](../../../../../Topology/Metric%20Spaces/Metric%20Topology.md#^opensets) $D$ of $\mathbb{R}^n$.
>
>A [critical point](../Differentiation/Critical%20Point.md) $\vec{x}_0 \in D$ is:
>- a place of a [local maximum](Local%20Extrema.md) if the [Hessian matrix](../Differentiation/Hessian%20Matrix.md) $H_f(\vec{x}_0)$ is [negative-definite](../../../../../Algebra/Linear%20Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices/Definiteness%20of%20Real%20Symmetric%20Matrices.md);
>- a place of a [local minimum](Local%20Extrema.md) if the [Hessian matrix](../Differentiation/Hessian%20Matrix.md) $H_f(\vec{x}_0)$ is [positive-definite](../../../../../Algebra/Linear%20Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices/Definiteness%20of%20Real%20Symmetric%20Matrices.md);
>- a place of a [saddle point](Saddle%20Point.md) if the [Hessian matrix](../Differentiation/Hessian%20Matrix.md) $H_f(\vec{x}_0)$ is [indefinite](../../../../../Algebra/Linear%20Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices/Definiteness%20of%20Real%20Symmetric%20Matrices.md);
>
>
>If the [Hessian matrix](../Differentiation/Hessian%20Matrix.md) $H_f(\vec{x}_0)$ is [semi-definite](../../../../../Algebra/Linear%20Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices/Definiteness%20of%20Real%20Symmetric%20Matrices.md), then it cannot be used to make any predictions.
>
>>[!PROOF]-
>>
>>TODO
>>
>
