---
title: Horizontal Coordinate System
tags:
    - coordinate-systems
    - astronomy
---

# The Celestial Horizon

Due to its size, the Earth always obstructs about half of the celestial sphere, irrespective of what the location of an observer is. 

>[!DEFINITION] Definition: The Celestial Horizon
>
>The plane tangent to the Earth at the location of an observer intersects the celestial sphere in a great circle known as the **celestial horizon** of the observer.
>
>![](res/The%20Celestial%20Horizon.svg)
>

The celestial horizon of an observer divides the celestial sphere into two hemispheres. The Earth obstructs the light coming from all celestial bodies in the lower hemisphere and so these objects cannot be seen by the observer.

>[!NOTE]- Note: Astronomical Horizon vs True Horizon
>
>The aforementioned celestial horizon is also known as the observer's **astronomical horizon**. It is a simplification because it assumes that the observer has no size and is just a point on the surface of the Earth.
>
>In practice, however, all observers have a size. For example, your eyes are some 180 cm above Earth's surface. As height increases, so does the part of the lower hemisphere which an observer can see. The new plane below which all celestial bodies are obstructed by Earth and are thus invisible to the observer is called the **true horizon**.
>
>Usually, the observer's distance from the surface of the Earth is negligibly small and the astronomical horizon aligns more-or-less perfectly with the true horizon. Therefore, most of the time, we ignore the distinction between the two.
>

## Zenith and Nadir

Imagine the line joining Earth's center and an observer. This line is perpendicular to the observer's celestial horizon and intersects the celestial sphere in two points.

![](res/Zenith%20and%20Nadir.svg)

>[!DEFINITION] Definition: Zenith
>
>The **zenith** of an observer is the point on the celestial sphere which is directly above them.
>
>>[!NOTATION]
>>
>>$$
>>Z
>>$$
>>

>[!DEFINITION] Definition: Nadir
>
>The **nadir** of an observer is the point on the celestial sphere which is directly below them.
>
>>[!NOTATION]
>>
>>$$
>>Z'
>>$$
>>
>

## Drawing Celestial Spheres

No single way to draw the celestial sphere for a given observer is more correct than another. However, there are certain conventions which have been established so as to ease the deciphering of the information on diagrams with celestial spheres.

Most commonly, the celestial sphere is drawn such that the zenith of the observer is right at the top and their nadir is right at the bottom.

![](res/Celestial%20Sphere%20Drawing%20Convention.svg)

# Horizontal Coordinate System

The **horizontal coordinate system** uses an observer's celestial horizon to assign coordinates to each celestial body on the [celestial sphere](The%20Celestial%20Sphere.md). 

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

The azimuth $A$ lies in the range $[0 \degree; 360 \degree)$. The point $N$ is assigned an azimuth of $0$ and the coordinate increases clockwise, i.e. in the direction $N \to E \to S \to W$. Here is a table summarizing the horizontal coordinates for key points on the celestial sphere.

|Point|Altitude|Azimuth|
|:--:|:--:|:--:|
|$Z$|$+90 \degree$||
|$Z'$|$-90 \degree$||
|$N$|$0 \degree$|$0 \degree$|
|$E$|$0 \degree$|$90 \degree$|
|$S$|$0 \degree$|$180 \degree$|
|$W$|$0 \degree$|$270 \degree$|

## Pros and Cons

The horizontal coordinate system is the most natural choice of a coordinate system for each observer because it allows them to easily determine the positions of celestial bodies relative to them as they are in the current moment. It is particularly useful for quickly finding and observing objects as it requires little more than a compass to determine where the cardinal directions for the observer are. For example, if you want to look at Venus tonight, then you will be using its altitude and azimuth.

The main disadvantage of this system is that the coordinates of celestial bodies depend on the observer's location on Earth and are always changing due to Earth's rotation.
