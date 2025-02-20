---
title: Coulomb's Law
tags:
    - electrostatics
    - electromagnetism
    - physics
---

# Coulomb's Law

Coulomb's law governs how [electric charges](../Electric%20Charge.md) interact with each other when they are both at rest.

>[!LAW] Empirical Law: Coulomb's Law
>
>Every pair of [point charges](../Electric%20Charge.md) $q_1$ and $q_2$ which are both at rest interact with a pair of [forces](../../Mechanics/Force.md), $\mathbf{F}_{\text{on } q_1}$ and $\mathbf{F}_{\text{on } q_2}$, which we call **electrostatic forces**. We refer to which depend on the [charges](Electric%20Charge.md) $q_1$ and $q_2$,  the distance $r$ between them and the [permittivity](Permittivity.md) $\varepsilon$ of their environment.
>
>- Magnitude - the electrostatic forces $\mathbf{F}_{\text{on } q_1}$ and $\mathbf{F}_{\text{on } q_2}$ have the same magnitude which depends on $q_1$ and $q_2$, the square of the distance $r$ between them and is proportional to a constant $\varepsilon$ which is a characteristic of the environment of the two charges called the [permittivity](Permittivity.md):
>
>$$
>||\mathbf{F}_{\text{on } q_1}|| = ||\mathbf{F}_{\text{on } q_2}|| = \frac{1}{4 \pi \varepsilon}\frac{|q_1 q_2|}{r^2}
>$$
>
>- Direction - the electrostatic [forces](../../Mechanics/Force.md) always act along the line joining $q_1$ and $q_2$. It is repulsive if both [charges](../Electric%20Charge.md) have the same algebraic sign, and it is attractive if they have different signs.
>
>Equations for the electrostatic forces as vectors can be written using the [normalized](../../../Mathematics/Algebra/Linear%20Algebra/Vector%20Spaces/Normed%20Vector%20Spaces/Unit%20Vector.md) difference between their positions, where $\displaystyle \hat{\mathbf{r}}_{q_1 \to q_2} = \frac{1}{||\mathbf{r}_{q_2} - \mathbf{r}_{q_1}||}\mathbf{r}_{q_2} - \mathbf{r}_{q_1}$ and $\displaystyle \hat{\mathbf{r}}_{q_2 \to q_1} = \frac{1}{||\mathbf{r}_{q_1} - \mathbf{r}_{q_2}||}\mathbf{r}_{q_1} - \mathbf{r}_{q_2}$:
>
>$$
>\mathbf{F}_{\text{on } q_2} = \frac{1}{4\pi\varepsilon}\frac{q_1 q_2}{r^2}\hat{\mathbf{r}}_{q_1 \to q_2}
>$$
>
>$$
>\mathbf{F}_{\text{on } q_1} = \frac{1}{4\pi\varepsilon}\frac{q_1 q_2}{r^2}\hat{\mathbf{r}}_{q_2 \to q_1}
>$$
>
>![](res/Coulomb's%20Law.svg)
>