---
tags:
  - real-analysis
  - vector-analysis
  - analysis
  - mathematics
---

# Polar Coordinate Representations (Real Vector Fields)

>[!DEFINITION] Definition: Polar Coordinate Representation
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}^2$ be a [real vector field](./Real%20Vector%20Fields.md) and let $\mathcal{T}: [0, \infty) \times (0, 2\uppi) \subset \mathbb{R}^2 \to \mathcal{D}$ be the [coordinate transformation](../Euclidean%20Space/Coordinate%20Transformations.md) from [polar coordinates](../Euclidean%20Space/Polar%20Coordinates.md):
>
>$$\mathcal{T}(\rho, \varphi) = \begin{bmatrix} \rho \cos \varphi \\ \rho \sin \varphi \end{bmatrix}$$
>
>The **polar coordinate representation** of $f$ is the [real vector field](./Real%20Vector%20Fields.md) $\tilde{f}: [0, \infty) \times (0, 2\uppi) \subset \mathbb{R}^2 \to \mathbb{R}^2$ defined as the following [product](../../../Algebra/Matrices/Matrix%20Product.md):
>
>$$\tilde{f}(\rho, \varphi) = \begin{bmatrix} \cos \varphi & \sin \varphi \\ -\sin \varphi & \cos \varphi \end{bmatrix}(f \circ \mathcal{T})(\rho, \varphi)$$
>