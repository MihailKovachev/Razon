---
title: Area of a Triangle
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
>A **triangle** is a [polygon](../index.md) with three [vertices](../index.md) and three [sides](../index.md).
>
>![](res/Triangles.svg)
>

## Properties

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
>The ratios of each side in a [triangle](Triangles.md) to the [sine](../../../../../Analysis/Real%20Analysis/Real%20Functions/Real%20Trigonometric%20Functions/Real%20Sine%20Function/Real%20Sine%20Function.md) of its opposite angle are all equal to the [diameter](../../Plane%20Curves/Circles/Circle.md) of the [circumcircle](Triangles.md#Properties).
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
>The side lengths $a,b,c$ of a [triangle](Triangles.md) and the [cosines](../../../../../Analysis/Real%20Analysis/Real%20Functions/Real%20Trigonometric%20Functions/Real%20Cosine%20Function/Real%20Cosine%20Function.md) of the corresponding opposite angles $\alpha$, $\beta$, $\gamma$ are related as follows:
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

# Surface Area

>[!THEOREM]- Theorem: Heron's Formula (Area using Sides)
>
>The [area](../Area%20of%20a%20Polygon.md) $A$ of a [triangle](Triangles.md) with [sides](../index.md) $a,b,c$ and [semiperimeter](../Perimeter.md) $p$ is given by
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
>The [area](../Area%20of%20a%20Polygon.md) $S$ of a [triangle](Triangles.md) with [sides](../index.md) $a,b,c$ and corresponding [altitudes](Cevians/Altitudes.md) $h_a,h_b,h_c$ is given by
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
>The [area](../Area%20of%20a%20Polygon.md) $S$ of a [triangle](Triangles.md) with [medians](Cevians/Medians.md) $m_a, m_b, m_c$ is given by
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