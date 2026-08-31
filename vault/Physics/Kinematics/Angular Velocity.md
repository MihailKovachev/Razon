---
tags:
    - classical-mechanics
    - physics
---

# Angular Velocity

>[!DEFINITION] Definition: Angular Velocity
>
>Let $\mathcal{R}(O)$ be a [reference frame](../Classical%20Mechanics/Reference%20Frames.md), let $l$ be an axis and let $p$ be a [point particle](../Classical%20Mechanics/Point%20Particles.md) with [velocity](./Velocity.md) $\boldsymbol{v}$.
>
>The **angular velocity** of $p$ w.r.t. $l$ is defined as
>
>$$\frac{(\boldsymbol{r} \times \boldsymbol{v}) \cdot \boldsymbol{\hat{l}}}{||\boldsymbol{r}||^2}\boldsymbol{\hat{l}},$$
>
>where $\boldsymbol{r}$ is the [radial vector](./Distance.md) from $l$ to $p$ and $\boldsymbol{\hat{l}}$ is any [unit vector](TODO) along $l$.
>
>![Angular Velocity](./res/Angular%20Velocity.svg)
>
>>[!NOTATION]
>>
>>$$\boldsymbol{\omega} \qquad \boldsymbol{\omega}_l \qquad \vec{\omega} \qquad \vec{\omega}_l$$
>>
>

>[!THEOREM] Theorem: Orthogonality of Angular Velocity and Radial Vector
>
>The [dot product](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Dot%20Product.md) [angular velocity](./Angular%20Velocity.md) $\omega$ of a [point particle](../Classical%20Mechanics/Point%20Particles.md) $p$ w.r.t. an axis $l$ and the [radial vector](TODO) $\boldsymbol{r}$ from $l$ to $p$ is always zero:
>
>$$\boldsymbol{\omega} \cdot \boldsymbol{r} = 0$$
>
>>[!PROOF]-
>>
>>$$\begin{aligned}\boldsymbol{\omega} \cdot \boldsymbol{r} & = \left(\frac{(\boldsymbol{r} \times \boldsymbol{v}) \cdot \boldsymbol{\hat{l}}}{||\boldsymbol{r}||^2}\boldsymbol{\hat{l}}\right) \cdot \boldsymbol{r} \\ & = \frac{(\boldsymbol{r} \times \boldsymbol{v}) \cdot \boldsymbol{\hat{l}}}{||\boldsymbol{r}||^2} (\boldsymbol{\hat{l}} \cdot \boldsymbol{r}) \\ & = \frac{(\boldsymbol{r} \times \boldsymbol{v}) \cdot \boldsymbol{\hat{l}}}{||\boldsymbol{r}||^2} \cdot 0 \\ & = 0\end{aligned}$$
>>
>