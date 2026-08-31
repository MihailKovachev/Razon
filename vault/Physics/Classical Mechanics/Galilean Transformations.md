---
tags:
    - classical-mechanics
    - physics
---

# Galilean Transformations

It is quite common for some physical problems to be easier to solve in one [reference frame](./Reference%20Frames.md) than in another or for us to want to find [kinematical quantities](./Kinematics.md) in different [reference frames](./Reference%20Frames.md). To achieve this, we need a way to convert between [kinematical quantities](./Kinematics.md) in one [reference frame](./Reference%20Frames.md) to the [kinematical quantities](./Kinematics.md) in another [reference frame](./Kinematics.md).

In [classical mechanics](./Classical%20Mechanics.md), this conversion is done using **Galilean transformations**.

>[!AXIOM] Axiom: Galilean Transformations
>
>Let $\mathcal{R}_{\alpha}$ and $\mathcal{R}_{\beta}$ be [reference frames](./Reference%20Frames.md) with [origins](./Reference%20Frames.md) $\mathcal{O}_{\alpha}$ and $\mathcal{O}_{\beta}$ and [temporal origins](./Reference%20Frames.md) $T_{\alpha}$ and $T_{\beta}$, respectively. We assume the following:
>
>- If a [moment in time](./Classical%20Mechanics.md) is ${}_{\mathcal{R}_{\alpha}}t$ in $\mathcal{R}_{\alpha}$, then in $\mathcal{R}_{\beta}$ it is
>$$
>{}_{\mathcal{R}_{\beta}}t = {}_{\mathcal{R}_{\alpha}}t + T_{\alpha} - T_{\beta}
>$$
>
>- If a [point particle](./Point%20Particles.md) $p$ has [position](./Kinematics.md#Position) ${}_{\mathcal{R}_{\alpha}} \boldsymbol{r}_p$ at time ${}_{\mathcal{R}_{\alpha}}t$ with respect to $\mathcal{R}_{\alpha}$ and if the [position](./Kinematics.md#Position) of $\mathcal{O}_{\beta}$ at time ${}_{\mathcal{R}_{\alpha}}t$ with respect to $\mathcal{R}_{\alpha}$ is ${}_{\mathcal{R}_{\alpha}} \boldsymbol{r}_{\mathcal{O}_{\beta}}$, then the [position](./Kinematics.md#Position) of $p$ at time ${}_{\mathcal{R}_{\beta}}t$ with respect to $\mathcal{R}_{\beta}$ is
>
>$$
>{}_\mathcal{\mathcal{R}_{\beta}} \boldsymbol{r}_p = {}_\mathcal{\mathcal{R}_{\alpha}} \boldsymbol{r}_p - {}_{\mathcal{R}_{\alpha}} \boldsymbol{r}_{\mathcal{O}_{\beta}}
>$$
>
>![](./res/Galilean%20Position%20Relativity.svg)
>
>- If the [velocity](./Kinematics.md#Velocity) of $\mathcal{O}_{\beta}$ at time ${}_{\mathcal{R}_{\alpha}}t$ with respect to $\mathcal{R}_{\alpha}$ is ${}_{\mathcal{R}_{\alpha}}\boldsymbol{v}_{\mathcal{O}_{\beta}}$ and the [velocity](./Kinematics.md#Velocity) of $\mathcal{O}_{\alpha}$ at time ${}_{\mathcal{R}_{\beta}}t$ with respect to $\mathcal{R}_{\beta}$ is ${}_{\mathcal{R}_{\beta}}\boldsymbol{v}_{\mathcal{O}_{\alpha}}$, then
>
>$$
>{}_{\mathcal{R}_{\beta}}\boldsymbol{v}_{\mathcal{O}_{\alpha}} = -{}_{\mathcal{R}_{\alpha}}\boldsymbol{v}_{\mathcal{O}_{\beta}}
>$$
>
>The above equations are called **Galilean transformations**.
>

From the above equations we can derive two other equations regarding [velocity](./Kinematics.md#Velocity) and [acceleration](./Kinematics.md#Acceleration).

>[!THEOREM] Theorem: Velocity and Acceleration Addition
>
>Let $\mathcal{R}_{\alpha}$ and $\mathcal{R}_{\beta}$ be [reference frames](./Reference%20Frames.md) with [origins](./Reference%20Frames.md) $\mathcal{O}_{\alpha}$ and $\mathcal{O}_{\beta}$ and let $p$ be a [point particle](./Point%20Particles.md). Suppose we have a moment in time which is ${}_{\mathcal{R}_{\alpha}}t$ in $\mathcal{R}_{\alpha}$ and ${}_{\mathcal{R}_{\beta}}t$ in $\mathcal{R}_{\beta}$.
>
>If the [velocity](./Kinematics.md#Velocity) of $p$ with respect to $\mathcal{R}_{\alpha}$ at ${}_{\mathcal{R}_{\alpha}}t$ is ${}_{\mathcal{R}_{\alpha}}\boldsymbol{v}_{p}$ and the the [velocity](./Kinematics.md#Velocity) of $\mathcal{O}_{\beta}$ with respect to $\mathcal{R}_{\alpha}$ at ${}_{\mathcal{R}_{\alpha}}t$ is ${}_{\mathcal{R}_{\alpha}}\boldsymbol{v}_{\mathcal{O}_{\beta}}$, then the [velocity](./Kinematics.md#Velocity) of $p$ with respect to $\mathcal{R}_{\beta}$ at ${}_{\mathcal{R}_{\beta}}t$ is
>
>$$
>{}_{\mathcal{R}_{\beta}}\boldsymbol{v}_{p} = {}_{\mathcal{R}_{\alpha}}\boldsymbol{v}_{p} - {}_{\mathcal{R}_{\alpha}}\boldsymbol{v}_{\mathcal{O}_{\beta}}
>$$
>
>If the [acceleration](./Kinematics.md#Acceleration) of $p$ with respect to $\mathcal{R}_{\alpha}$ at ${}_{\mathcal{R}_{\alpha}}t$ is ${}_{\mathcal{R}_{\alpha}}\boldsymbol{a}_{p}$ and the the [acceleration](./Kinematics.md#Acceleration) of $\mathcal{O}_{\beta}$ with respect to $\mathcal{R}_{\alpha}$ at ${}_{\mathcal{R}_{\alpha}}t$ is ${}_{\mathcal{R}_{\alpha}}\boldsymbol{a}_{\mathcal{O}_{\beta}}$, then the [acceleration](./Kinematics.md#Acceleration) of $p$ with respect to $\mathcal{R}_{\beta}$ at ${}_{\mathcal{R}_{\beta}}t$ is
>
>$$
>{}_{\mathcal{R}_{\beta}}\boldsymbol{a}_{p} = {}_{\mathcal{R}_{\alpha}}\boldsymbol{a}_{p} - {}_{\mathcal{R}_{\alpha}}\boldsymbol{a}_{\mathcal{O}_{\beta}}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>


[Galilean transformations](./Galilean%20Transformations.md) are true as long as we are not dealing with very high [speeds](./Kinematics.md#Velocity), way below $300\,000\,000 \frac{\mathrm{m}}{\mathrm{s}}$. Reality, however, is more complicated as you approach these [speeds](./Kinematics.md#Velocity) because, for some reason, $300\,000\,000 \frac{\mathrm{m}}{\mathrm{s}}$ is a universal speed limit. In these situations, [Galilean transformations](./Galilean%20Transformations.md) break down and we need other transformations in order to match empirical observation.
