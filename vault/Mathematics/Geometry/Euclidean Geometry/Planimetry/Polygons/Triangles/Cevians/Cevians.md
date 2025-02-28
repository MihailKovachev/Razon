---
title: Cevians
tags:
  - triangles
  - polygons
  - planimetry
  - euclidean-geometry
  - geometry
  - mathematics
---

# Cevians

>[!DEFINITION] Definition: Cevian
>
>A **cevian** in a [triangle](../Triangles.md) is a [line segment](../../../../Curves/Straight%20Lines/Line%20Segments.md) whose endpoints are a [vertex](../../Polygons.md) of the triangle and a [point](../../../../Euclidean%20Space/Points%20vs%20Vectors/index.md) on the [side](../../Polygons.md) opposite to the vertex.
>
>![](res/Cevian.svg)
>

## Properties

>[!THEOREM]- Stewart's Theorem
>
>Let $T$ be a [triangle](../Triangles.md) with [sides](../../Polygons.md) $a,b,c$.
>
>If a [cevian](Cevians.md) $d$ divides $a$ into two [segments](../../../../Curves/Straight%20Lines/Line%20Segments.md) $m$ and $n$ such that $n$ shares a [vertex](../../Polygons.md) with $b$ and $m$ shares a vertex with $c$, then 
>
>$$
>b^2 m + c^2 n = a(d^2 + mn)
>$$
>
>![](res/Stewart's%20Theorem.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Ceva's Theorem
>
>Let $\triangle ABC$ be a [triangle](../Triangles.md).
>
>Three [cevians](Cevians.md) $AA'$, $BB'$ and $CC'$ in $\triangle ABC$ are [concurrent](../../../../Curves/Straight%20Lines/Concurrent%20Lines.md) if and only if
>
>$$
>\frac{AC'}{BC'} \cdot \frac{BA'}{CA'} \cdot \frac{CB'}{AB'} = 1
>$$
>
>![](res/Ceva's%20Theorem.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!THEOREM]- Theorem: Ceva's Generalized Theorem
>>
>>[Ceva's theorem](Cevians.md#Properties) can be generalized to the case where $A'$, $B'$, $C'$ are three points such that two of the points lie on the extensions of two sides of $\triangle ABC$ and the third lies on the third side. However, the aforementioned equality know guarantees either that the [lines](../../../../Curves/Straight%20Lines/Straight%20Line.md) $AA'$, $BB'$ and $CC'$ are [concurrent](../../../../Curves/Straight%20Lines/Concurrent%20Lines.md) or that they are [parallel](TODO).
>>
>>
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>