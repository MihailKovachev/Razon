---
title: Cylindrical Coordinate System
tags:
    - coordinate-systems
    - euclidean-geometry
    - geometry
    - mathematics
---

# Cylindrical Coordinates

Cylindrical coordinates are a natural extension of the [polar coordinate system](Polar%20Coordinate%20System.md) to three dimensions. They identify each point in the [Euclidean space](../../../../Analysis/Real%20Analysis/The%20Topology%20of%20Euclidean%20Space.md) $\mathbb{R}^3$ by its distance from the $z$-axis, the angle $\phi$ its projection in the $xy$-plane makes with the $x$-axis and its $z$ component.

![](res/Cylindrical%20Coordinates.drawio.svg)

>[!DEFINITION] Definition: Radial Distance
>
>The number $\rho$ is known as the **radial distance**.
>
>>[!WARNING]
>>
>>This is not the same as the radial distance used in [spherical coordinates](Spherical%20Coordinate%20System.md).
>>
>

>[!DEFINITION] Definition: Azimuthal Angle (Azimuth)
>
>The number $\phi$ is known as the **azimuthal angle** or **azimuth**.
>

>[!DEFINITION] Definition: Axial Coordinate (Height)
>
>The number $z$ is known as the **axial coordinate** or **height**. 
>
>>[!NOTE]
>>
>>Despite the word "height", the axial coordinate's algebraic sign is crucial.
>>
>

## Conventions

Some people prefer to use $\theta$ or $\varphi$ for the azimuth.

Additionally, a single point has infinitely many possible values for its azimuth, since adding or subtracting a multiple of $2\pi$ to an angle has no effect. However, in order to have a [coordinate system](index.md), coordinates must be unique. This means that the possible values for $\phi$ must be restricted. Common conventions for the range of $\phi$ are $[0; 2\pi)$ and $(-\pi, \pi]$.