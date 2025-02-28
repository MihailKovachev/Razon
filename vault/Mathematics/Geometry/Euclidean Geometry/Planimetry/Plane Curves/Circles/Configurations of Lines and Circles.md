---
title: Configurations of Lines and Circles
tags:
  - planimetry
  - euclidean-geometry
  - geometry
  - mathematics
---

# Configurations of Lines and Circles

>[!THEOREM] Theorem: Line and Circle Intersections
>
>There are three possible cases for a [straight line](../../../Curves/Straight%20Lines/Straight%20Line.md) and a [circle](Circle.md):
>- They have *no* points of intersections.
>- They intersect at *one* point.
>- They intersect at *two* points.
>
>![](res/Circle%20and%20Line%20Intersections.svg)
>
>>[!PROOF]-
>>
>>Suppose, towards contradiction, that the [straight line](../../../Curves/Straight%20Lines/Straight%20Line.md) $p$ and the [circle](Circle.md) $k(O; r)$ intersect at three points.
>>
>>TODO
>> 
>

# External Lines

>[!DEFINITION] Definition: External Line
>
>Let $p$ be a [straight line](../../../Curves/Straight%20Lines/Straight%20Line.md) and let $k(O; r)$ be a [circle](Circle.md#Circle) such that all points of  [circle](Circle.md#Circle)
>
>If all points of $p$ lie outside of $k$, then $p$ is known as an **external line** for $k$.
>

>[!THEOREM] Theorem: External Lines in a Plane
>
>If a [straight line](../../../Curves/Straight%20Lines/Straight%20Line.md) $p$ and a [circle](Circle.md#Circle) $k(O; r)$ lie in the same [plane](../../../Surfaces/Planes.md) and do not intersect, then $p$ is an [external line](Configurations%20of%20Lines%20and%20Circles.md) for $k$.
>
>$$
>d(O; P) \gt r \qquad \forall P \in p
>$$
>
>![](res/External%20Line%20of%20Circle.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Tangent Lines

>[!DEFINITION] Definition: Tangent Line
>
>A [straight line](../../../Curves/Straight%20Lines/Straight%20Line.md) is a **tangent line** to a [circle](Circle.md) iff they have only one point of intersection.
>
>![](res/Tangent%20Line%20to%20Circle.svg)
>

## Characterizations

>[!THEOREM]- Theorem: Perpendicularity of Tangent Lines
>
>Let $k(O;r)$ be a [circle](Circle.md#Circle) and let $p$ be a [straight line](../../../Curves/Straight%20Lines/Straight%20Line.md) which intersects $k$ at a point $P$.
>
>The line $p$ is a [tangent line](Configurations%20of%20Lines%20and%20Circles.md#Tangent%20Lines) if and only if the [radius](Circle.md#Circle) from $O$ to $P$ is [perpendicular](TODO) to $p$.
>
>![](res/Perpendicularity%20of%20Tangent%20Lines%20and%20Circles.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Properties

>[!THEOREM]-
>
>If $k(O; r)$ is a [circle](Circle.md#Circle) and $p$ is a [tangent line](Configurations%20of%20Lines%20and%20Circles.md#Tangent%20Lines), then all points of $p$, apart from the point of intersection with $k$, lie outside of $k$. 
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Tangent Lines through External Points
>
>Let $k(O; r)$ be a [circle](Circle.md#Circle).
>
>If $P$ is a point outside of $k$ but which lies in the [plane](../../../Surfaces/Planes.md) of $k$, then there exist precisely two [tangent lines](Configurations%20of%20Lines%20and%20Circles.md#Tangent%20Lines) to $k$ which pass through $P$. Moreover, the [triangles](../../Polygons/Triangles/Triangles.md) formed by $P$, $O$ and the points of intersection are [congruent](../../Polygons/Triangles/Triangles.md).
>
>$$
>\triangle PTO \cong \triangle PT'O
>$$
>
>![](res/Tangents%20to%20Circle%20Through%20External%20Point.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Secant Lines

>[!DEFINITION] Definition: Secant Line
>
>A [straight line](../../../Curves/Straight%20Lines/Straight%20Line.md) is a **secant line** to a [circle](Circle.md#Circle) iff they intersect at two points.
>
>![](res/Secant%20Line%20through%20Circle.svg)
>

## Properties

>[!THEOREM]- Intersecting Secants Theorem
>
>Let $k(O; r)$ be a [circle](Circle.md#Circle).
>
>If $s_1$ and $s_2$ are two [secant lines](Configurations%20of%20Lines%20and%20Circles.md#Secant%20Lines) such that $s_1$ intersects $k$ at the points $A$ and $A'$, $s_2$ intersects $k$ at the points $B$ and $B'$, and the two secant lines intersect each other at $C$, then the [triangles](../../Polygons/Triangles/Triangles.md) $\triangle CAB'$ and $\triangle CBA'$ are [similar](TODO).
>
>$$
>\triangle CAB' \sim \triangle CBA'
>$$
>
>![](res/Intersecting%20Secants%20Theorem.svg)
>
>>[!PROOF]-
>>
>>The [inscribed angles](Angles.md#Inscribed%20Angles) $\angle AB'B$ and $\angle BA'A$ are equal, since they have the same [corresponding arc](Angles.md#Inscribed%20Angles), namely $\overset{\frown}{AB}$. The angle $\angle A'CB'$ is shared by both triangles. The third angles of the triangles are then equal because the sum of the angles in a triangle is always $180\degree$. Since the triangles have equal 
>>
>

# Bibliography

