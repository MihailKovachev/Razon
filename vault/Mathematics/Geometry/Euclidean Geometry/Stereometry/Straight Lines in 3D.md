---
title: Straight Lines in 3D
tags:
    - stereometry
    - geometry
    - mathematics
---

# Straight Lines in 3D

>[!DEFINITION] Definition: Straight Line
>
>A **straight line** in [3D space](Stereometry.md) is an [unbounded](TODO) [locus of points](Stereometry.md) which is [homeomorphic](../../../Topology/Continuity/Homeomorphisms/Homeomorphic%20Spaces.md) to the [real numbers](../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) $\mathbb{R}$.
>

>[!DEFINITION] Definition: Angle between Straight Lines
>
>Let $a$ and $b$ be [straight lines](Straight%20Lines%20in%203D.md) in 3D.
>
>The **angle** between $a$ and $b$ is the [angle](../../../Algebra/Linear%20Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Angle.md) between any pair of [vectors](../Euclidean%20Geometry.md) such that one of the [vectors](../Euclidean%20Geometry.md) is between [points](../Euclidean%20Geometry.md) which lie on $a$ and the other is between [points](../Euclidean%20Geometry.md) which lie on $b$.
>
>>[!NOTATION]
>>
>>$$
>>\angle (a;b)
>>$$
>
>>[!DEFINITION] Definition: Perpendicularity
>>
>>Two [straight lines](Straight%20Lines%20in%203D.md) in 3D are **perpendicular** if the [angle](Straight%20Lines%20in%203D.md) between them is a right angle.
>>
>

## Properties

>[!THEOREM]- Theorem: Intersecting Lines $\implies$ Plane
>
>For each pair of intersecting [straight lines](Straight%20Lines%20in%203D.md) there exists a unique [plane](Planes%20in%203D.md) which contains them.
>
>![](res/Intersecting%20Lines%20Imply%20Plane.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Parallel Lines

>[!THEOREM]- Theorem: Parallel Lines and Points
>
>If $a$ is a [straight line](Straight%20Lines%20in%203D.md) in [3D space](Stereometry.md), then for each point $P$ there exists a unique [straight line](Straight%20Lines%20in%203D.md) $b$ which goes through $P$ and is [parallel](TODO) to $a$.
>
>$$
>\forall P, \exists! b: a \parallel b \land P \in b
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Parallel Lines $\implies$ Plane
>
>If two [straight lines](Straight%20Lines%20in%203D.md) in [3D space](Stereometry.md) are [parallel](TODO), then there exists a unique [plane](../Surfaces/Planes.md) which contains both of them.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Parallel Lines and Plane Intersections
>
>If two [straight lines](Straight%20Lines%20in%203D.md) in [3D space](Stereometry.md) are [parallel](TODO), then every [plane](../Surfaces/Planes.md) which intersects one of them also intersects the other.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Three Parallel Lines
>
>Let $a,b,c$ be [straight lines](Straight%20Lines%20in%203D.md) in [3D space](Stereometry.md).
>
>If $a$ and $b$ are [parallel](Straight%20Lines%20in%203D.md#Parallel%20Lines) and $b$ and $c$ are [parallel](Straight%20Lines%20in%203D.md#Parallel%20Lines), then $a$ and $c$ are also [parallel](Straight%20Lines%20in%203D.md#Parallel%20Lines).
>
>$$
>a \parallel b \land b \parallel c \implies a \parallel c
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Skew Lines

>[!DEFINITION] Definition: Skew Lines
>
>**Skew lines** are two [straight lines](../Curves/Straight%20Lines/Straight%20Line.md) in [3D space](Stereometry.md) which do not lie in the same [plane](../Surfaces/Planes.md).
>

>[!THEOREM] Theorem: Angle between Skew Lines
>
>Let $a$ and $b$ be [skew lines](Straight%20Lines%20in%203D.md#Skew%20Lines), let $a_1$ and $a_2$ be [parallel](Straight%20Lines%20in%203D.md#Parallel%20Lines) to $a$ and let $b_1$ and $b_2$ be [parallel](Straight%20Lines%20in%203D.md#Parallel%20Lines) to $b$.
>
>If $a_1$ and $b_1$ intersect and $a_2$ and $b_2$ also intersect, then the [angles](../Curves/Straight%20Lines/Angle%20between%20Lines.md) they form are equal.
>
>$$
>\angle (a_1, b_1) = \angle (a_2, b_2)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Angle between Skew Lines
>>
>>The **angle** between two [skew lines](Straight%20Lines%20in%203D.md) $a$ and $b$ is the [angle](../Curves/Straight%20Lines/Angle%20between%20Lines.md) between any pair of intersecting [lines](Straight%20Lines%20in%203D.md) $a'$ and $b'$ such that $a$ and $a'$ are [parallel](Straight%20Lines%20in%203D.md#Parallel%20Lines) and $b$ and $b'$ are also [parallel](Straight%20Lines%20in%203D.md#Parallel%20Lines).
>>
>

