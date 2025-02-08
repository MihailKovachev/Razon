---
title: Horizontal Coordinate System
tags:
    - coordinate-systems
    - astronomy
---

# Horizontal Coordinate System

The **horizontal coordinate system** uses an observer's [celestial horizon](The%20Celestial%20Sphere.md#the%20celestial%20horizon) to assign coordinates to each celestial body on the [celestial sphere](The%20Celestial%20Sphere.md). 

On the celestial horizon, we plot the points $N$, $S$, $E$ and $W$ such that when the observer is looking at $N$, they are looking north, when they are looking at $S$, they are looking south, when they are looking at $E$, they are looking east, and when they are looking at $W$, they are looking west.

![](res/NSEW%20Celestial%20Horizon.svg)

Usually, $N$ is placed on the left of the celestial horizon and $S$ on the right, but they could also be switched around. The choice of the actual positions for $N$ and $S$ on the diagram is irrelevant as long as they are kept diametrically opposed. The same goes for $E$ and $W$ - they must be diametrically opposed and $E$ should be on the right of the observer when they are looking at $N$. 

>[!IMPORTANT]
>
>Each of the points $N$, $S$, $E$ and $W$ is at $90 \degree$ angles with the observer and its two neighbors.
>

We do not draw the Earth itself as it is largely irrelevant for the coordinate assignment. We just have to keep in mind that the observer cannot see celestial bodies which are under their celestial horizon.

## Altitude and Azimuth

Consider a celestial body $X$ and imagine the arc which goes through $X$ and the observer's zenith $Z$.This arc intersects the observer's celestial horizon at a point which we will call $X'$. Now we can use the points on the celestial sphere to assign coordinates to $X$.

>[!DEFINITION] Definition: Altitude (Elevation)
>
>The **altitude** or **elevation** of $X$ is the angle between $X'$, the observer and $X$.
>
>>[!NOTATION]
>>
>>$$
>>a \qquad h
>>$$
>>
>

>[!DEFINITION] Definition: Azimuth
>
>The **azimuth** of $X$ is the angle between $N$, the observer and $X'$.
>
>>[!NOTATION]
>>
>>$$
>>A
>>$$
>>
>

![](res/Horizontal%20Coordinate%20System.svg)

>[!NOTE]
>
>The horizontal coordinate system is also called the **az/el**, **alt/az** or **alt-azimuth** system.
>

### Conventions for Azimuth and Altitude

Most commonly, the altitude $a$ lies in the range $[-90 \degree; +90 \degree]$. Positive values are assigned to celestial bodies above the horizon and negative values are used for objects below it. The zenith has altitude $+90 \degree$ and the nadir has altitude $-90 \degree$.

The azimuth $A$ lies in the range $[0; 360 \degree)$. The point $N$ is assigned an azimuth of $0$ and the coordinate increases clockwise, i.e. in the direction $N \to E \to S \to W$. Here is a table summarizing the horizontal coordinates for key points on the celestial sphere.

|Point|Altitude|Azimuth|
|:--:|:--:|:--:|
|$Z$|$+90 \degree$||
|$Z'$|$-90 \degree$||
|$N$|$0 \degree$|$0 \degree$|
|$E$|$0 \degree$|$90 \degree$|
|$S$|$0 \degree$|$180 \degree$|
|$W$|$0 \degree$|$270 \degree$|

