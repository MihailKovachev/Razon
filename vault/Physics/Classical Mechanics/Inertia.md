---
tags:
    - classical-mechanics
    - physics
---

# Inertia

For whatever reason, the Universe is very lazy and always wants to be in the simplest possible state, which makes it really averse to changes. One of the way in which this manifests itself is in the resistance of objects to changes in their motion. Basically,  every physical object wants to keep moving on the path it is already moving on, a phenomenon we call **inertia**.

>[!DEFINITION] Definition: Inertia
>
>The **inertia** of a physical object is its ability to resist changes in its motion.
>

Naturally, if we want to describe physical reality correctly, we need a way of measuring and quantifying [inertia](./Inertia.md):

>[!DEFINITION] Definition: Mass
>
>The **mass** of a physical object is a measure of its [inertia](./Inertia.md).
>
>>[!NOTATION]
>>
>>$$
>>m
>>$$
>>
>
>>[!UNIT]
>>
>>The SI measurement unit for [mass](./Inertia.md) is the **kilogram** ($\mathrm{kg}$).
>>
>

>[!DEFINITION] Definition: Average Density
>
>The **average density** of an object is the ratio of its total [mass](#Mass) to the total volume it occupies.
>
>$$
>\frac{m}{V}
>$$
>
>>[!NOTATION]
>>
>>$$
>>\rho \qquad \rho_{\text{avg}}
>>$$
>>
>

We are used to associating the word "mass" with the amount of "stuff" which is contained in a physical object, but this notion is wrong because there are physical things, such as light, which have no mass. If mass was equivalent to stuff, then light would not exist because it has zero mass and would thus be nothing.

## Point Masses

We naturally have to extend the model of the [point particle](../../index.md#Point%20Particles) to include [mass](./Inertia.md).

>[!DEFINITION] Definition: Point Mass
>
>A **point mass** is a model of a physical object with [mass](./Inertia.md) as a [point particle](../../index.md#Point%20Particles).
>

>[!DEFINITION] Definition: System of Point Masses
>
>A **system of point masses** is any [set](../../Mathematics/Set%20Theory/Sets.md) of objects which we model as [point masses](#Mass).
>

>[!DEFINITION] Definition: Center of Mass
>
>The **center of mass** of a [finite](../../Mathematics/Set%20Theory/Cardinality.md) [system of point masses](#Masses) $m_1, \cdots, m_n$ with [positions](./Kinematics.md#Positions) $\boldsymbol{r}_1, \cdots, \boldsymbol{r}_n$ is an imaginary [point particle](./Point%20Particles.md) with [position](./Kinematics.md#Positions)
>
>$$
>\boldsymbol{r}_{\text{cm}} \overset{\text{def}}{=} \frac{1}{M} \sum_{i=1}^n m_i \boldsymbol{r}_i,
>$$
>
>where $M = m_1 + \cdots + m_n$.
>

## Continuous Mass Distributions

Sometimes, there are situations in which the spatial extent of physical objects cannot be neglected and modelling them as [point masses](#Mass) yields very inaccurate predictions. In such situations, we can model objects using (mass) density functions.

>[!DEFINITION] Definition: Continuous Mass Distributions
>
>A **continuous mass distribution** is a model of a physical object $\mathcal{O}$ as a [real scalar field](../../Mathematics/Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $\rho: \mathbb{R}^3 \to \mathbb{R}$ such that [integrating](../../Mathematics/Analysis/Real%20Analysis/Real%20Scalar%20Fields/Integration/Integration%20of%20Real%20Scalar%20Fields.md#Lebesgue%20Integrals) $\rho$ over a region of [space](./Classical%20Mechanics.md) $V$ occupied by $\mathcal{O}$ yields the [mass](#Mass) of $\mathcal{O}$ which is contained in $V$:
>
>$$
>m = \int_{V} \rho \mathop{\mathrm{d}V}
>$$
>

>[!DEFINITION] Definition: Center of Mass
>
>The **center of mass** of a [continuous mass distribution](#Mass) $\rho$ is an imaginary [point particle](./Point%20Particles.md) with [position](./Kinematics.md#Positions)
>
>$$
>\boldsymbol{r}_{\text{cm}} \overset{\text{def}}{=} \int_V \rho(\boldsymbol{r})\boldsymbol{r} \mathop{\mathrm{d}V},
>$$
>
>where we [integrate](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Integration%20of%20Real%20Vector%20Functions.md) $\rho(\boldsymbol{r})\boldsymbol{r}$ over the region of [space](./Classical%20Mechanics.md) occupied by the [continuous mass distribution](#Mass).
>