---
title: Velocity
tags:
    - classical-mechanics
    - kinematics
    - physics
---

# Displacement

>[!DEFINITION] Definition: Displacement
>
>Let $\mathcal{R}$ be a [reference frame](../../Mechanics/Reference%20Frame.md) with [origin](../../Mechanics/Reference%20Frame.md) $O$.
>
>The **displacement** of a [particle](../../Physical%20Systems/Point%20Masses/Point%20Mass.md) in the interval $\Delta t$ between the [times](../../Space%20and%20Time.md) $t_1$ and $t_2 \gt t_1$ is the difference in its [position](Position.md) at $t_2$ and its [position](Position.md) at $t_1$:
>
>$$
>\mathbf{r}(t_2) - \mathbf{r}(t_1)
>$$
>
>>[!NOTATION]
>>
>>$$
>>\Delta \mathbf{r} \qquad \Delta \boldsymbol{r} \qquad \Delta \vec{r}
>>$$
>
>![](res/Displacement.svg)
>

# Average Velocity

>[!DEFINITION] Definition: Average Velocity
>
>Let $\mathcal{R}$ be a [reference frame](../../Mechanics/Reference%20Frame.md) with [origin](../../Mechanics/Reference%20Frame.md) $O$.
>
>The **average velocity** of a [particle](../../Physical%20Systems/Point%20Masses/Point%20Mass.md) during the time interval $\Delta t$ is its [displacement](Velocity.md#Displacement) during $\Delta t$ divided by the length of the interval:
>
>$$
>\frac{\Delta \mathbf{r}}{\Delta t}
>$$
>
>>[!NOTATION]
>>
>>$$
>>\mathbf{v}_{\text{avg}} \qquad \boldsymbol{v}_{\text{avg}} \qquad \vec{v}_{\text{avg}}
>>$$
>>
>

# Instantaneous Velocity

>[!DEFINITION] Definition: Instantaneous Velocity
>
>The **instantaneous velocity** of a [point mass](../../Physical%20Systems/Point%20Masses/Point%20Mass.md) at a moment $t_0$ is its average velocity within an infinitely small time interval after $t_0$:
>
>$$\boldsymbol{v}(t_0)\overset{\text{def}}{=} \lim_{\Delta t\to 0} \boldsymbol{v}_{\text{avg}} = \lim_{\Delta t\to 0} \frac{\boldsymbol{r}(t_0+\Delta t)-\boldsymbol{r}(t_0)}{\Delta t} = \frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t}(t_0) = \dot{\boldsymbol{r}}(t_0)$$
>
>>[!NOTE]
>>
>>The instantaneous velocity is just the temporal derivative of the [position](Position.md).
>>
>
>>[!NOTE]
>>
>>When one says "velocity", they usually mean the instantaneous velocity.
>>
>

# Speed

>[!DEFINITION] Definition: (Average) Speed
>
>The **(average) speed** of a [particle](../../Physical%20Systems/Point%20Masses/Point%20Mass.md) is the magnitude of its [(average) velocity](Velocity.md).
>

# Bibliography
