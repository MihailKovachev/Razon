---
tags:
    - kinematics
    - physics
---

# Circular Motion

>[!DEFINITION] Definition: Circular Motion
>
>Let $\mathcal{R}(O)$ be a [reference frame](../Classical%20Mechanics/Reference%20Frames.md), let $l$ be an [axis](TODO) and let $p$ be a [point particle](../Classical%20Mechanics/Point%20Particles.md).
>
>We say that $p$ undergoes **circular motion** around $l$ if its [velocity](./Velocity.md) $\boldsymbol{v}$ is the [cross product](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Cross%20Product.md) of its [angular velocity](./Angular%20Velocity.md) $\boldsymbol{\omega}$ w.r.t. $l$ and the [radial vector](TODO) $\boldsymbol{r}$ from $l$ to $p$:
>
>$$\boldsymbol{v} = \boldsymbol{\omega} \times \boldsymbol{r}$$
>
>![Circular Motion](./res/Circular%20Motion.svg)
>

>[!THEOREM] Theorem: Orthogonality of Velocity and Radial Vector
>
>Let $\mathcal{R}(O)$ be a [reference frame](../Classical%20Mechanics/Reference%20Frames.md), let $l$ be an [axis](TODO) and let $p$ be a [point particle](../Classical%20Mechanics/Point%20Particles.md).
>
>If $p$ is undergoing [circular motion](./Circular%20Motion.md) around $l$, then the [dot product](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Dot%20Product.md) of its [velocity](./Velocity.md) $\boldsymbol{v}$ and the [radial vector](TODO) $\boldsymbol{r}$ from $l$ to $p$ is always zero:
>
>$$\boldsymbol{v} \cdot \boldsymbol{r} = 0$$
>
>>[!PROOF]-
>>
>>By the definition of [circular motion](./Circular%20Motion.md), we have:
>>
>>$$\boldsymbol{v} = \boldsymbol{\omega} \cdot \boldsymbol{r}$$
>>
>>We take the [dot product](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Dot%20Product.md) of both sides with $\boldsymbol{r}$:
>>
>>$$\boldsymbol{v} \cdot \boldsymbol{r} = (\boldsymbol{\omega} \cdot \boldsymbol{r}) \cdot \boldsymbol{r}$$
>>
>>Applying a [standard property](TODO) to the right-hand side, we get:
>>
>>$$(\boldsymbol{\omega} \cdot \boldsymbol{r}) \cdot \boldsymbol{r} = \boldsymbol{\omega} \cdot (\boldsymbol{r} \times \boldsymbol{r}) = \boldsymbol{\omega} \cdot \boldsymbol{0} = 0$$
>>
>

>[!THEOREM] Theorem: Constancy of Radial Distance in Circular Motion
>
>Let $\mathcal{R}(O)$ be a [reference frame](../Classical%20Mechanics/Reference%20Frames.md), let $l$ be an [axis](TODO) and let $p$ be a [point particle](../Classical%20Mechanics/Point%20Particles.md).
>
>If $p$ is undergoing [circular motion](#Circular%20Motion) around $l$, then the distance $r$ between $l$ and $p$ is constant:
>
>$$||\boldsymbol{r}(t)|| = r(t) = \text{const}$$
>
>>[!PROOF]-
>>
>>Let $\boldsymbol{r}(t)$ be the [radial vector](TODO) from $l$ to $p$ and let $\boldsymbol{r}_p(t)$ be the [position](./Position.md) of $p$.
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Angular Velocity from Velocity and Radial Vector
>
>Let $\mathcal{R}(O)$ be a [reference frame](../Classical%20Mechanics/Reference%20Frames.md), let $l$ be an [axis](TODO) and let $p$ be a [point particle](../Classical%20Mechanics/Point%20Particles.md).
>
>If $p$ is undergoing [circular motion](./Circular%20Motion.md) around $l$, then its [angular velocity](./Angular%20Velocity.md) $\boldsymbol{\omega}$ is equal to the [cross product](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Cross%20Product.md) of the [radial vector](TODO) $\boldsymbol{r}$ from $l$ to $p$ and $p$'s [velocity](./Velocity.md) $\boldsymbol{v}$ divided by the square of the [distance](./Distance.md) $r$ between $l$ and $p$:
>
>$$\boldsymbol{\omega} = \frac{\boldsymbol{r} \times \boldsymbol{v}}{r^2} = \frac{\boldsymbol{r} \times \boldsymbol{v}}{||\boldsymbol{r}||^2}$$
>
>>[!PROOF]-
>>
>>By the definition of [circular motion](./Circular%20Motion.md), we have:
>>
>>$$\boldsymbol{v} = \boldsymbol{\omega} \times \boldsymbol{r}$$
>>
>>We take the [cross product](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Cross%20Product.md) (on the left) of both sides with $\boldsymbol{r}$:
>>
>>$$\boldsymbol{r} \times \boldsymbol{v} = \boldsymbol{r} \times (\boldsymbol{\omega} \times \boldsymbol{r})$$
>>
>>Now we apply the [triple cross product identity](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Cross%20Product.md) to the right-hand side:
>>
>>$$\boldsymbol{r} \times (\boldsymbol{\omega} \times \boldsymbol{r}) = \omega(\boldsymbol{r} \cdot \boldsymbol{r}) - \boldsymbol{r}(\boldsymbol{r} \cdot \boldsymbol{\omega})$$
>>
>>Since $\boldsymbol{r} \cdot \boldsymbol{\omega} = 0$, this simplifies to the following:
>>
>>$$\boldsymbol{r} \times (\boldsymbol{\omega} \times \boldsymbol{r}) = \omega(\boldsymbol{r} \cdot \boldsymbol{r}) = \boldsymbol{\omega}||\boldsymbol{r}||^2 = r^2 \boldsymbol{\omega}$$
>>
>>We thus have:
>>
>>$$\boldsymbol{r} \times \boldsymbol{v} = r^2 \boldsymbol{\omega}$$
>>
>>$$\boldsymbol{\omega} = \frac{\boldsymbol{r} \times \boldsymbol{v}}{r^2}$$
>>
>

>[!THEOREM] Theorem: Radial Vector from Velocity and Angular Velocity
>
>Let $\mathcal{R}(O)$ be a [reference frame](../Classical%20Mechanics/Reference%20Frames.md), let $l$ be an [axis](TODO) and let $p$ be a [point particle](../Classical%20Mechanics/Point%20Particles.md).
>
>If $p$ is undergoing [circular motion](./Circular%20Motion.md) around $l$, then the [radial vector](TODO) $\boldsymbol{r}$ from $l$ to $p$ is equal to the [cross product](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Cross%20Product.md) and $p$'s [velocity](./Velocity.md) $\boldsymbol{v}$ and $p$'s [angular velocity](./Angular%20Velocity.md) $\boldsymbol{\omega}$ divided by the square of $p$'s [angular speed](./Angular%20Velocity.md) $\omega$:
>
>$$\boldsymbol{r} = \frac{\boldsymbol{v} \times \boldsymbol{\omega}}{\omega^2} = \frac{\boldsymbol{v} \times \boldsymbol{\omega}}{||\boldsymbol{\omega}||^2}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Uniform Circular Motion

>[!DEFINITION] Definition: Uniform Circular Motion
>
>A [point particle](../Classical%20Mechanics/Point%20Particles.md) undergoes **uniform circular motion** if it is in [circular motion](./Circular%20Motion.md) and its [speed](./Velocity.md) does not change with time.
>

>[!THEOREM] Theorem: Angular Velocity during Uniform Circular Motion
>
>Let $\mathcal{R}(O)$ be a [reference frame](../Classical%20Mechanics/Reference%20Frames.md), let $l$ be an [axis](TODO) and let $p$ be a [point particle](../Classical%20Mechanics/Point%20Particles.md).
>
>If $p$ is undergoing [uniform circular motion](#Uniform%20Circular%20Motion)  around $l$, then its [angular velocity](./Angular%20Velocity.md) is constant.
>
>$$\boldsymbol{\omega}(t) = \boldsymbol{\omega} = \text{const}$$
>
>>[!PROOF]-
>>
>>Let $\boldsymbol{v}(t)$ be the [velocity](./Velocity.md) of $p$, let $\boldsymbol{\omega}(t)$ be the [angular velocity](./Angular%20Velocity.md) of $p$ w.r.t. $l$ and let $\boldsymbol{r}(t)$ be the radial vector from $l$ to $p$:
>>
>>$$\boldsymbol{v}(t) = \begin{bmatrix}v_1(t) \\ v_2(t) \\ v_3(t)\end{bmatrix} \qquad \boldsymbol{\omega}(t) = \begin{bmatrix}\omega_1(t) \\ \omega_2(t) \\ \omega_3(t)\end{bmatrix} \qquad \boldsymbol{r}(t) = \begin{bmatrix}r_1(t) \\ r_2(t) \\ r_3(t)\end{bmatrix}$$
>>
>>Since $p$ is undergoing [circular motion](./Circular%20Motion.md), we know the following for $\boldsymbol{\omega}(t)$:
>>
>>$$\boldsymbol{\omega}(t) = \frac{\boldsymbol{r}(t) \times \boldsymbol{v}(t)}{||\boldsymbol{r}(t)||^2}$$
>>
>>Since $p$ is undergoing [uniform circular motion](#Uniform%20Circular%20Motion), we know that $||\boldsymbol{r}(t)||^2$ is constant:
>>
>>$$\boldsymbol{\omega}(t) = \frac{\boldsymbol{r}(t) \times \boldsymbol{v}(t)}{r^2}$$
>>
>>We now [differentiate](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) $\boldsymbol{\omega}(t)$:
>>
>>$$\boldsymbol{\omega}'(t) = \frac{r^2 (\boldsymbol{r}(t) \times \boldsymbol{v}'(t)) - 2(\boldsymbol{r}(t) \cdot \boldsymbol{v}(t))(\boldsymbol{r}(t) \times \boldsymbol{v}(t))}{r^4}$$
>>
>>Since $p$ is undergoing [circular motion](./Circular%20Motion.md), we know that $\boldsymbol{r}(t) \cdot \boldsymbol{v}(t) = 0$. Therefore:
>>
>>$$\boldsymbol{\omega}'(t) = \frac{r^2(\boldsymbol{r}(t) \times \boldsymbol{v}'(t))}{r^4} = \frac{\boldsymbol{r}(t) \times \boldsymbol{v}'(t)}{r^2}$$
>>
>>Furthermore, because $p$ is undergoing [uniform circular motion](#Uniform%20Circular%20Motion), the [acceleration](./Acceleration.md) $\boldsymbol{v}'(t)$ is purely centripetal. This means it points directly opposite to the radial vector $\boldsymbol{r}(t)$. Since these vectors are antiparallel, their cross product is zero: >> >>$$\boldsymbol{r}(t) \times \boldsymbol{v}'(t) = \boldsymbol{0}$$ >> >>Substituting this back into our simplified equation yields: >> >>$$\boldsymbol{\omega}'(t) = \frac{\boldsymbol{0}}{r^2} = \boldsymbol{0}$$ >> >>Therefore, the [angular acceleration](./Angular%20Acceleration.md) $\boldsymbol{\alpha}(t) = \boldsymbol{\omega}'(t)$ is $\boldsymbol{0}$.
>>
>

>[!THEOREM] Theorem: Speed during Uniform Circular Motion
>
>If a [point particle](../Classical%20Mechanics/Point%20Particles.md) is undergoing [uniform circular motion](#Uniform%20Circular%20Motion) around an axis $l$, then its [speed](./Velocity.md) $v$ is equal to the product of its [angular speed](./Angular%20Velocity.md) $\omega$ w.r.t. $l$ and the distance $r$ between it and $l$:
>
>$$v = \omega r$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Acceleration during Uniform Circular Motion
>
>If a [point particle](../Classical%20Mechanics/Point%20Particles.md) $p$ is undergoing [uniform circular motion](./Circular%20Motion.md) around an axis $l$, then its [acceleration](./Acceleration.md) $\boldsymbol{a}$ is the [cross product](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Cross%20Product.md) of its [angular velocity](./Angular%20Velocity.md) $\boldsymbol{\omega}$ w.r.t. $l$ and its [velocity](./Velocity.md) $\boldsymbol{v}$:
>
>$$\boldsymbol{a} = \boldsymbol{\omega} \times \boldsymbol{v}$$
>
>Alternatively, $\boldsymbol{a}$ is equal to the [cross product](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Cross%20Product.md) of $\boldsymbol{\omega}$ with the [cross product](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Cross%20Product.md) of $\boldsymbol{\omega}$ and the radial vector from $l$ to $p$:
>
>$$\boldsymbol{a} = \boldsymbol{\omega} \times (\boldsymbol{\omega} \times \boldsymbol{r})$$
>
>The [magnitude](TODO) $a$ of $\boldsymbol{a}$ can be expressed via the [speed](./Velocity.md) $v$ of $p$ and the distance $r$ between $l$ and $p$:
>
>$$a = \frac{v^2}{r}$$
>
>Alternatively, it can be expressed via the [angular speed](./Angular%20Velocity.md) $\omega$ and $r$:
>
>$$a = \omega^2 r$$
>
>>[!PROOF]-
>>
>>TODO
>>
>