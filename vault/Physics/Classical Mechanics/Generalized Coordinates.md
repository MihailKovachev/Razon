---
tags:
    - classical-mechanics
    - physics
---

# Generalized Coordinates

>[!DEFINITION] Definition: Configuration
>
>Let $\mathcal{R}$ be a [reference frame](./Reference%20Frames.md).
>
>The **configuration** of a [physical system](../Physical%20Systems.md) with $n$ [point particles](../Physical%20Systems.md) $p_1, \dotsc, p_n$ is its [parametrization](../Physical%20Systems.md) by the [positions](./Kinematics.md#Position) $\boldsymbol{r}_{p_1}, \dotsc, \boldsymbol{r}_{p_n}$ of $p_1, \dotsc, p_n$:
>
>$$
>(\boldsymbol{r}_{p_1}, \dotsc, \boldsymbol{r}_{p_n})
>$$
>
>>[!DEFINITION] Definition: Configuration Space
>>
>>The [phase space](../Physical%20Systems.md#Parametrization) of this [parametrization](../Physical%20Systems.md#Parametrization) is known as **configuration space**.
>>
>

In general, the [configuration](./Generalized%20Coordinates.md) of a [physical system](../Physical%20Systems.md) with $n$ [point particles](../Physical%20Systems.md) has $3n$ [degrees of freedom](../Physical%20Systems.md#Parametrization) because each [position](./Kinematics.md#Position) has three components. 

>[!DEFINITION] Definition: Generalized Coordinates
>
>Suppose we have a [physical system](../Physical%20Systems.md) $S$ with $n$ [point particles](../Physical%20Systems.md) $p_1, \dotsc, p_n$.
>
>If $(q_1, \dotsc, q_s)$ is a [parametrization](../Physical%20Systems.md#Parametrization) of $S$ with $s = 3n$ [degrees of freedom](../Physical%20Systems.md#Parametrization) which is [equivalent](../Physical%20Systems.md#Parametrization) to the [configuration parametrization](./Generalized%20Coordinates.md) of $S$, then we say that $q_1, \dotsc, q_s$ are **generalized coordinates** for $S$.
>
>>[!DEFINITION] Definition: Generalized Velocities
>>
>>The [derivatives](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Differentiability%20(Real%20Functions).md) $\dot{q}_1, \dotsc, \dot{q}_s$ of the [generalized coordinates](./Generalized%20Coordinates.md) $q_1, \dotsc, q_s$ with respect to [time](./Classical%20Mechanics.md) are called **generalized velocities**.
>>
>>>[!DEFINITION] Definition: Generalized Accelerations
>>>
>>>The [derivatives](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Differentiability%20(Real%20Functions).md) $\ddot{q}_1, \dotsc, \ddot{q}_s$ of the [generalized velocities](./Generalized%20Coordinates.md) $\dot{q}_1, \dotsc, \dot{q}_s$ with respect to [time](./Classical%20Mechanics.md) are called **generalized accelerations**.
>>>
>>
>
>>[!NOTATION]
>>
>>We often use the following shorthand notations:
>>- $q$ for $q_1, \dotsc, q_s$
>>- $\dot{q}$ for $\dot{q}_1, \dotsc, \dot{q}_s$
>>- $\ddot{q}$ for $\ddot{q}_1, \dotsc, \ddot{q}_s$
>>
>

Simply put, [generalized coordinates](./Generalized%20Coordinates.md) are a set of values which allow us to uniquely determine the [configuration](./Generalized%20Coordinates.md) of a [physical system](../Physical%20Systems.md) of [point particles](../Physical%20Systems.md). 

>[!DEFINITION] Definition: Path
>
>Let $q_1, \dotsc, q_s$ be [generalized coordinates](./Generalized%20Coordinates.md) for a [physical system](../Physical%20Systems.md) $\mathcal{S}$ of [point particles](../Physical%20Systems.md) and let $t_1$ and $t_2 \gt t_1$ be two [moments in time](./Classical%20Mechanics.md).
>
>А **path** in [configuration space](./Generalized%20Coordinates.md) is a [function](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) $\boldsymbol{q}: [t_1; t_2] \to \mathbb{R}^s$ which is [continuous](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Continuity%20(Real%20Vector%20Functions).md) on $[t_1; t_2]$ and [continuously differentiable](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) on $(t_1; t_2)$.
>

Each [physical system](../Physical%20Systems.md) follows only one [path](./Generalized%20Coordinates.md) $\boldsymbol{q}$ between any two given [moments](./Classical%20Mechanics.md) $t_1$ and $t_2$. At any moment $t \in [t_1; t_2]$, the [configuration](./Generalized%20Coordinates.md) of the [physical system](../Physical%20Systems.md) is completely described by $\boldsymbol{q}(t) = \begin{bmatrix}q_1 & \cdots & q_s\end{bmatrix}^{\mathsf{T}}$.