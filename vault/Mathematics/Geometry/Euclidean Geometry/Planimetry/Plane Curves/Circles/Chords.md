---
title: Chords in a Circle
tags:
    - euclidean geometry
    - geometry
    - mathematics
---

# Chords

>[!DEFINITION] Definition: Chord
>
>A **chord** in a [circle](Circle.md) is any [line segment](../../../Curves/Straight%20Lines/Line%20Segments.md) whose endpoints are [points](../../../Euclidean%20Space/Points%20vs%20Vectors/index.md) of the circle.
>
>![](res/Chord%20in%20a%20Circle.svg)
>

## Properties

>[!THEOREM]- Intersecting Chords Theorem
>
>If $AC$ and $BD$ are [chords](Chords.md) in a [circle](Circle.md) $k(O; r)$ and they intersect at $S$, then $S$ divides each chord such that the product of the lengths of the two segments of one chord is equal to the product of the lengths of the segments of the other chord. Moreover, this product is given by the [radius](Circle.md#Circle) $r$ and the distance $l$ between $O$ as follows:
>
>$$
>|AS| \cdot |SC| = |BS| \cdot |BD| = r^2 - l^2
>$$
>
>![](res/Intersecting%20Chords%20Theorem.svg)
>
>The converse is also true - if two [line segments](../../../Curves/Straight%20Lines/Line%20Segments.md) $AC$ and $BD$ intersect at a point $S$ which divides each segment such that $|AS| \cdot |SC| = |BS| \cdot |BD|$, then $AC$ and $BD$ are [chords](Chords.md) in a [circle](Circle.md#Circle).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Subtended Arcs and Chords
>
>Two [chords](Chords.md) $AB$ and $CD$ in a [circle](Circle.md) $k(O; r)$ have equal length if and only if the arcs they subtend have equal length.
>
>$$
>|AB| = |CD| \iff |\overset{\frown}{AB}| = |\overset{\frown}{CD}|
>$$
>
>![](res/Equal%20Chords%20iff%20Equal%20Arcs.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Chords and Distances
>
>Two [chords](Chords.md) $AB$ and $CD$ in a [circle](Circle.md) $k(O; r)$ have equal length if and only if the distance between $O$ and $AB$ is is the same as the distance between $O$ and $CD$.
>
>$$
>|AB| = |CD| \iff d(O; AB) = d(O; CD)
>$$
>
>![](res/Equal%20Chords%20iff%20Equal%20Distances.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Parallel Chords $\implies$ Equal Arcs
>
>The arcs subtended between two [parallel](TODO) [chords](Chords.md) $AB$ and $CD$ in a [circle](Circle.md#Circle) always have equal length.
>
>$$
>AB \parallel CD \implies |\overset{\frown}{AC}| = |\overset{\frown}{BD}|
>$$
>
>![](res/Parallel%20Chords%20imply%20Equal%20Arcs.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Diameter and Chord Perpendicularity
>
>Let $AB$ be a non-[diameter](Circle.md#Circle) [chord](Chords.md) in a [circle](Circle.md#Circle) $k(O;r)$.
>
>A [diameter](Circle.md#Circle) $d$ of $k$ is [perpendicular](TODO) to $AB$ if and only if it splits $AB$ in half.
>
>$$
>d \perp AB \iff |AS| = |BS|
>$$
>
>![](res/Diameter%20and%20Chord%20Perpendicularity.svg)
>
>>[!PROOF]-
>>
>>TODO
>> 
>
