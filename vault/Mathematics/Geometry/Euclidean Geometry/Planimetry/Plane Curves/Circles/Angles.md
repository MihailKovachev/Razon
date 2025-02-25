---
title: Angles in a Circle
tags:
    - euclidean-geomtetry
    - geometry
    - mathematics
---

# Central Angles

>[!DEFINITION] Definition: Central Angle
>
>Let $k(O; r)$ be a [circle](Circle.md#Circle).
>
>A **central angle** is an [angle](../../../Angles/Plane%20Angles/Plane%20Angle.md) whose vertex is $O$ and whose rays are [radii](Circle.md#Circle) of $k$.
>
>![](res/Central%20Angle.svg)
>

## Arcs

>[!DEFINITION] Definition: Arc
>
>An **arc** of a [circle](Circle.md) is a part of the circle bound between a [central angle](Angles.md#Central%20Angles).
>
>![](res/Arc.svg)
>

It is obvious that each [central angle](Angles.md#Central%20Angles) corresponds to a single [arc](Angles.md#Arcs) and that each [arc](Angles.md#Arcs) corresponds to a single [central angle](Angles.md#Central%20Angles). Hence, we often use the terms "arc" and "central angle" interchangeably. 

# Inscribed Angles

>[!DEFINITION] Definition: Inscribed Angle
>
>Let $k(O; r)$ be a [circle](Circle.md#Circle).
>
>An **inscribed angle** is an [angle](../../../Angles/Plane%20Angles/Plane%20Angle.md) whose vertex lies on $k$ and whose rays intersect $k$ at differents point from the vertex.
>
>![](res/Inscribed%20Angle.svg)
>
>>[!DEFINITION]- Definition: Corresponding Arc
>>
>>The **corresponding arc** of $\angle ABC$ is the[arc](Angles.md#Arcs)$\overset{\frown}{AC}$ which does *not* pass through $B$.
>>
>>![](res/Corresponding%20Arc%20of%20Inscribed%20Angle.svg)
>>
>
>>[!DEFINITION]- Definition: Corresponding Chord
>>
>>The **corresponding chord** of $\angle ABC$ is the [chord](Chords.md) which corresponds to $\angle ABC$'s corresponding arc.
>>
>>![](res/Corresponding%20Chord%20of%20Inscribed%20Angle.svg)
>>
>
>>[!DEFINITION]- Definition: Corresponding Central Angle
>>
>>The **corresponding central angle** of $\angle ABC$ is the [central angle](Circle.md#Central%20Angles) $\angle AOC$ whose corresponding[arc](Angles.md#Arcs)is the same as $\angle ABC$'s corresponding arc.
>>
>>![](res/Corresponding%20Central%20Angle%20of%20Inscribed%20Angle.svg)
>>
>

## Properties

>[!THEOREM]- Theorem: Measure of Inscribed Angles
>
>Let $k(O; r)$ be a [circle](Circle.md#Circle).
>
>The measure of an [inscribed angle](Angles.md#Inscribed%20Angles) is always half the measure of its [corresponding central angle](Angles.md#Inscribed%20Angles).
>
>$$
>\angle ABC = \frac{1}{2}\angle AOC
>$$
>
>![](res/Measure%20of%20Inscribed%20Angle.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!TIP]
>>
>>This means that inscribed angles which have the same corresponding[arc](Angles.md#Arcs)/ chord / central angle are equal.
>>
>

>[!THEOREM]- Theorem: Right Inscribed Angles
>
>An [inscribed angle](Angles.md#Inscribed%20Angles) has a measure of $90^\degree$ ($\frac{\pi}{2} \mathrm{rad}$) if and only if its [corresponding chord](Angles.md#Inscribed%20Angles) is a [diameter](Circle.md).
>
>![](res/Right%20Inscribed%20Angle.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Tangent Chord Angles

>[!DEFINITION] Definition: Tangent Chord Angle
>
>Let $k(O; r)$ be a [circle](Circle.md).
>
>A **tangent chord angle** or **peripheral angle** is an [angle](../../../Angles/Plane%20Angles/Plane%20Angle.md) whose vertex lies on $k$, whose one ray is a [chord](Chords.md) and whose other ray lies on a [tangent line](Configurations%20of%20Lines%20and%20Circles.md) to $k$.
>
>![](res/Tangent%20Chord%20Angle.svg)
>
>>[!DEFINITION]- Definition: Corresponding Arc
>>
>>The **corresponding arc** of a [tangent chord angle](Angles.md#Tangent%20Chord%20Angles) is the[arc](Angles.md#Arcs)which lies in its interior.
>>
>>![](res/Corresponding%20Arc%20of%20Tangent%20Chord%20Angle.svg)
>>
>
>>[!DEFINITION]- Definition: Corresponding Central Angle
>>
>>The **corresponding central angle** of a [tangent chord angle](Angles.md#Tangent%20Chord%20Angles) is the [central angle](Angles.md#Central%20Angles) whose [corresponding arc](Angles.md#Central%20Angles) is the same as the [corresponding arc](Angles.md#Tangent%20Chord%20Angles) of the [tangent chord angle](Angles.md#Tangent%20Chord%20Angles).
>>
>>![](res/Corresponding%20Central%20Angle%20of%20Tangent%20Chord%20Angle.svg)
>>
>

## Properties

>[!THEOREM]- Theorem: Measure of Tangent Chord Angles
>
>The measure of a [tangent chord angle](Angles.md#Tangent%20Chord%20Angles) is always half of its [corresponding central angle](Angles.md#Tangent%20Chord%20Angles).
>
>$$
>\varphi = \frac{1}{2} \angle AOB
>$$
>
>![](res/Measure%20of%20Tangent%20Chord%20Angle.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!TIP]
>>
>>This means that all tangent chord angles with the same corresponding central angle are equal.
>>
>

# Interior Angles

>[!DEFINITION] Definition: Interior Angle
>
>Let $k(O; r)$ be a [circle](Circle.md#Circle).
>
>An **interior angle** is an [angle](../../../Angles/Plane%20Angles/Plane%20Angle.md) whose vertex lies inside of $k$ and whose rays intersect $k$.
>
>![](res/Interior%20Angle%20in%20a%20Circle.svg)
>
>>[!DEFINITION]- Definition: Corresponding Arcs
>>
>>The **corresponding arcs** of an [interior angle](Angles.md#Interior%20Angles) are the arcs enclosed between its rays and the extensions of those rays.
>>
>>![](res/Corresponding%20Arcs%20of%20Interior%20Angle.svg)
>>
>
>>[!DEFINITION]- Definition: Corresponding Central Angles
>>
>>The **corresponding central angles** of an [interior angle](Angles.md#Interior%20Angles) are the [central angles](Angles.md#Central%20Angles) with the same [corresponding arcs](Angles.md#Central%20Angles) as the interior angle.
>>
>>$$
>>\angle AOC, \angle A'OC'
>>$$
>>
>>![Corresponding Central Angles of Interior Angle](res/Corresponding%20Central%20Angles%20of%20Interior%20Angle.svg)
>>
>

## Properties

>[!THEOREM]- Theorem: Measure of Interior Angles
>
>The measure of an [interior angle](Angles.md#Interior%20Angles) is always half of the sum of the measures of its [corresponding central angles](Angles.md#Interior%20Angles).
>
>$$
>\angle ABC = \frac{1}{2}(\angle AOC + \angle A'OC')
>$$
>
>![Corresponding Central Angles of Interior Angle](res/Corresponding%20Central%20Angles%20of%20Interior%20Angle.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Exterior Angles

>[!DEFINITION] Definition: Exterior Angle
>
>Let $k(O; r)$ be a [circle](Circle.md#Circle).
>
>An **exterior angle** is an [angle](../../../Angles/Plane%20Angles/Plane%20Angle.md) whose vertex lies outside of $k$ but whose rays intersect $k$.
>
>![](res/Exterior%20Angle.svg)
>
>>[!DEFINITION]- Definition: Corresponding Arcs
>>
>>The **corresponding arcs** of an [exterior angle](Angles.md#Exterior%20Angles) are the arcs between the [chords](Chords.md) cut off by the angle's rays.
>>
>>![](res/Corresponding%20Arcs%20of%20Exterior%20Angle.svg)
>>
>
>>[!DEFINITION]- Definition: Corresponding Central Angles
>>
>>The **corresponding central angles** of an [exterior angle](Angles.md#Exterior%20Angles) are the [corresponding central angles](Angles.md#Central%20Angles) of its [corresponding arcs](Angles.md#Exterior%20Angles).
>>
>>![](res/Corresponding%20Central%20Angles%20of%20Exterior%20Angle.svg)
>>
>

## Properties

>[!THEOREM]- Theorem: Measure of Exterior Angles
>
>The measure of an [exterior angle](Angles.md#Exterior%20Angles) is always half of the difference between the measures of its [corresponding central angles](Angles.md#Exterior%20Angles).
>
>$$
>\angle ABC = \frac{1}{2} (\angle AOC - \angle A'OC')
>$$
>
>![](res/Corresponding%20Central%20Angles%20of%20Exterior%20Angle.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>