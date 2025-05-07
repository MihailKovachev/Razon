---
title: Triangles
tags:
  - triangles
  - planimetry
  - euclidean-geometry
  - geometry
  - mathematics
  - polygons
---

# Triangles

>[!DEFINITION] Definition: Triangle
>
>A **triangle** is a [polygon](../Polygons.md) with three [vertices](../Polygons.md) and three [sides](../Polygons.md).
>
>![](res/Triangles.svg)
>

## Properties

>[!THEOREM]- Theorem: Sum of Interior Angles
>
>The sum of the [interior angles](../Polygons.md#Interior%20Angles) $\alpha, \beta, \gamma$ of a [triangle](Triangles.md) is always $180 \degree$.
>
>$$
>\alpha + \beta + \gamma = 180 \degree
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: The Triangle Inequality
>
>If a [triangle](Triangles.md) has side lengths $a, b,c$, then
>
>$$
>\begin{align*} a + b \gt c \\ b + c \gt a \\ a + c \gt b \end{align*}
>$$
>
>Conversely, if $a, b, c$ are positive [real numbers](../../../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) for which all of the above inequalities hold, then there exists a [triangle](Triangles.md) with side lengths $a, b, c$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Cyclicity of Triangles
>
>Every [triangle](Triangles.md) is a [cyclic](../Cyclic%20Polygons/Cyclic%20Polygon.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Circumcircle
>>
>>The **circumcircle** of a [triangle](Triangles.md) is the [circle](../../Plane%20Curves/Circles/Circle.md) on which all of its the vertices lie.
>>
>

>[!THEOREM]- Theorem: Law of Sines
>
>The ratios of each side in a [triangle](Triangles.md) to the [sine](../../../../../Analysis/Real%20Analysis/Real%20Functions/Real%20Trigonometric%20Functions/Real%20Sine%20Function.md) of its opposite angle are all equal to the [diameter](../../Plane%20Curves/Circles/Circle.md) of the [circumcircle](Triangles.md#Properties).
>
>$$
>\frac{a}{\sin \alpha} = \frac{b}{\sin \beta} = \frac{c}{\sin \gamma} = 2R
>$$
>
>![](res/Law%20of%20Sines.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Law of Cosines
>
>The side lengths $a,b,c$ of a [triangle](Triangles.md) and the [cosines](../../../../../Analysis/Real%20Analysis/Real%20Functions/Real%20Trigonometric%20Functions/Real%20Cosine%20Function.md) of the corresponding opposite angles $\alpha$, $\beta$, $\gamma$ are related as follows:
>
>$$
>\begin{align*}
>a^2 &= b^2 + c^2 - 2bc \cos \alpha \\
>b^2 &= a^2 + c^2 - 2ac \cos \beta \\
>c^2 &= a^2 + b^2 - 2ab \cos \gamma
>\end{align*}
>$$
>
>![Law of Cosines](res/Law%20of%20Cosines.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Menelaus's Theorem
>
>Let $\triangle ABC$ be a [triangle](Triangles.md) and let $A'$, $B'$ and $C'$ be points respectively on the [lines](../../../Curves/Straight%20Lines/Straight%20Line.md) defined by the sides $BC$, $AC$ and $AB$.
>
>The points $A'$, $B'$ and $C'$ lie on one [straight line](../../../Curves/Straight%20Lines/Straight%20Line.md) if and only if exactly one or three of them lie outside of the triangle's sides and
>
>$$
>\frac{AC'}{BC'} \cdot \frac{BA'}{CA'} \cdot \frac{CB'}{AB'} = 1
>$$
>
>- If exactly one of the points lies outside of the triangle's sides, then this line is outside the triangle.
>- If exactly three of these points lie outside the triangle's sides, then this line passes through the triangle.
>
>![](res/Menelaus's%20Theorem.svg) 
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Similarity

## Characterizations

>[!THEOREM]- Theorem: Angle-Angle-Angle (AAA)
>
>Two [triangles](Triangles.md) are [similar](../../../Geometric%20Shapes.md#Similarity) if and only if their three angles are respectively equal.
>
>$$
>\triangle ABC \sim \triangle A'B'C' \iff \begin{cases} \angle A = \angle A' \\ \angle B = \angle B' \\ \angle C = \angle C \end{cases}
>$$
>
>![](res/Similar%20Triangles%20-%20AAA.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!TIP]
>>
>>In practice, one only needs two angles and not three, since the third can always be determined using the [sum of angles theorem](Triangles.md#Properties).
>>
>

>[!THEOREM]- Theorem: Side-Side-Side (SSS)
>
>Two [triangles](Triangles.md) are [similar](../../../Geometric%20Shapes.md#Similarity) if and only if each side in one can be paired with another such that the ratios of these pairs are all equal.
>
>$$
>\triangle ABC \sim \triangle A'B'C' \iff \frac{AB}{A'B'} = \frac{BC}{B'C'} = \frac{AC}{A'C'}
>$$
>
>![](res/Similar%20Triangles%20-%20SSS.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Side-Angle-Side (SAS)
>
>Two [triangles](Triangles.md) are [similar](../../../Geometric%20Shapes.md#Similarity) if and only if two sides of one triangle can be paired with two sides of the other such that the ratios of the pairs are equal and the angles between these sides are equal.
>
>$$
>\triangle ABC \sim \triangle A'B'C' \iff \begin{cases} \frac{AB}{A'B'} = \frac{AC}{A'C'} \\ \angle A = \angle A' \end{cases}
>$$
>
>![](res/Similar%20Triangles%20-%20SAS.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Side-Side-Angle (SSA)
>
>Two [triangles](Triangles.md) are [similar](../../../Geometric%20Shapes.md#Similarity) if and only if two sides of one triangle can be paired with two sides of the other such that the ratios of the pairs are equal and the angles opposite to the longer of these sides are equal.
>
>$$
>\triangle ABC \sim \triangle A'B'C' \iff \begin{cases} \frac{AB}{A'B'} = \frac{BC}{B'C'} \\ AB \gt BC \\ A'B' \gt B'C' \\ \angle C = \angle C' \end{cases}
>$$
>
>![](res/Similar%20Triangles%20-%20SSA.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Congruence

>[!THEOREM]- Theorem: Side-Angle-Side (SAS)
>
>Two [triangles](Triangles.md) $T_1$ and $T_2$ are [congruent](../../../Geometric%20Shapes.md) if and only if two sides of $T_1$ and the [angle](../../../Curves/Straight%20Lines/Line%20Segments.md) between them are respectively equal to two sides of $T_2$ and the angle between them.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Angle-Side-Angle
>
>Two [triangles](Triangles.md) $T_1$ and $T_2$ are [congruent](../../../Geometric%20Shapes.md) if and only if two [interior angles](../Polygons.md) of $T_1$ and the side joining them are respectively equal to two [interior angles](../Polygons.md) of $T_2$ and the side joining them.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Side-Side-Side (SSS)
>
>Two [triangles](Triangles.md) $T_1$ and $T_2$ are [congruent](../../../Geometric%20Shapes.md) if and only if the three sides of $T_1$ are respectively equal to the three sides of $T_2$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Surface Area

>[!THEOREM]- Theorem: Heron's Formula (Area using Sides)
>
>The [area](../Polygons.md) $A$ of a [triangle](Triangles.md) with [sides](../Polygons.md) $a,b,c$ and [semiperimeter](../Polygons.md) $p$ is given by
>
>$$A = \sqrt{p(p-a)(p-b)(p-c)}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Area using Altitudes
>
>The [area](../Polygons.md) $S$ of a [triangle](Triangles.md) with [sides](../Polygons.md) $a,b,c$ and corresponding [altitudes](Cevians/Altitudes.md) $h_a,h_b,h_c$ is given by
>
>$$S = \frac{a \cdot h_a}{2} = \frac{b \cdot h_b}{2} = \frac{c \cdot h_c}{2}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Area using Medians
>
>The [area](../Polygons.md) $S$ of a [triangle](Triangles.md) with [medians](Cevians/Medians.md) $m_a, m_b, m_c$ is given by
>
>$$S = \frac{4}{3}\sqrt{\sigma(\sigma - m_a) (\sigma - m_b) (\sigma - m_c)},$$
>
>where  $\sigma = \frac{m_a + m_b + m_c}{2}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>