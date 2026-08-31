---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - geometry
    - mathematics
---

# Coordinate Transformations

>[!THEOREM] Theorem: Cartesian $\leftrightarrow$ Polar
>
>If $\mathbf{p} \in \mathbb{R}^2$ has [Cartesian coordinates](./Cartesian%20Coordinate%20System.md) $(x,y)$, then its [polar coordinates](./Polar%20Coordinates.md) $(r, \theta)$ are:
>
>- Using the convention $r \ge 0$ and $\theta \in (-\pi; \pi]$: 
>
>$$
>\begin{aligned}
>r &= \sqrt{x^2 + y^2} \\
>
>\theta &=
>
>\begin{cases}
>
>\arctan \left( \frac{y}{x} \right) \qquad \qquad \text{if } x \gt 0 \\
>
>\arctan \left( \frac{y}{x} \right) + \pi \qquad \text{ if } x \lt 0, y \ge 0 \\
>
>\arctan \left( \frac{y}{x} \right) - \pi \qquad \text{ if } x \lt 0, y \lt 0 \\
>
>\frac{\pi}{2} \qquad \qquad \qquad \qquad \text{if } x = 0, y \gt 0 \\
>
>-\frac{\pi}{2} \qquad \qquad \qquad \, \, \, \, \, \, \text{ if } x = 0, y \lt 0 \\
>
>0 \qquad \qquad \qquad \qquad \, \text{ if } x = y = 0
>
>\end{cases}
>
>\end{aligned}
>$$
>
>- Using the convention $r \ge 0$ and $\theta \in [[Polar Coordinate System|0; 2\pi)$: 
>
>$$
>\begin{aligned}
>
>r &= \sqrt{x^2 + y^2} \\
>
>\theta &= 
>
>\begin{cases}
>
>\arccos \frac{x}{\sqrt{x^2 + y^2}} \qquad \qquad \text{ if } y > 0 \\
>
>2\pi - \arccos \frac{x}{\sqrt{x^2 + y^2}} \qquad \text{if } y < 0 \\
>
>0 \qquad \qquad \qquad \qquad \hphantom{,,,,} \text{if } y = 0, x \ge 0 \\
>
>\pi \qquad \qquad \qquad \qquad \hphantom{,,,,} \text{if } y = 0, x \lt 0
>
>\end{cases}
>
>\end{aligned}
>$$
>
>If $\mathbf{p} \in \mathbb{R}^2$ has [polar coordinates]] $(r, \theta)$, then its [Cartesian coordinates](./Cartesian%20Coordinate%20System.md) $(x,y)$ are
>
>$$
>\begin{aligned}
>
>x &= r \cos \theta \\
>
>y &= r \sin \theta
>
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Cartesian $\leftrightarrow$ Spherical
>
>If $\mathbf{p} \in \mathbb{R}^3$ has [Cartesian coordinates](./Cartesian%20Coordinate%20System.md) $(x,y,z)$, then its [spherical coordinates](./Spherical%20Coordinates.md) $(r, \theta, \phi)$ are:
>
>- Using the convention $r \ge 0$, $\theta \in [0; \pi]$ and $\phi \in (-\pi; \pi]$:
>
>$$
>\begin{aligned}
>
>r &= \sqrt{x^2 + y^2 + z^2} \\
>
>\theta &= 
>\begin{cases}
>
>0 \qquad \qquad \qquad \hphantom{,,,,,} \text{if } x = y = z = 0 \\
>
>\arccos \frac{z}{\sqrt{x^2 + y^2 + z^2}} \hphantom{,,,,} \text{otherwise }
>
>\end{cases} \\ 
>
>\phi &=
>
>\begin{cases}
>
>\arctan \left( \frac{y}{x} \right) \qquad \qquad \text{if } x \gt 0 \\
>
>\arctan \left( \frac{y}{x} \right) + \pi \qquad \text{ if } x \lt 0, y \ge 0 \\
>
>\arctan \left( \frac{y}{x} \right) - \pi \qquad \text{ if } x \lt 0, y \lt 0 \\
>
>\frac{\pi}{2} \qquad \qquad \qquad \qquad \text{if } x = 0, y \gt 0 \\
>
>-\frac{\pi}{2} \qquad \qquad \qquad \, \, \, \, \, \, \text{ if } x = 0, y \lt 0 \\
>
>0 \qquad \qquad \qquad \qquad \, \text{ if } x = y = 0
>
>\end{cases}
>
>\end{aligned}
>$$
>
>- Using the convention $r \ge 0$, $\theta \in [0; \pi]$ and $\phi \in [[Spherical Coordinate System|0; 2\pi)$:
>
>$$
>\begin{aligned}
>
>r &= \sqrt{x^2 + y^2 + z^2} \\
>
>\theta &= 
>\begin{cases}
>
>0 \qquad \qquad \qquad \hphantom{,,,,,} \text{if } x = y = z = 0 \\
>
>\arccos \frac{z}{\sqrt{x^2 + y^2 + z^2}} \hphantom{,,,,} \text{otherwise }
>
>\end{cases} \\ 
>
>\phi &=
>
>\begin{cases}
>
>\arccos \frac{x}{\sqrt{x^2 + y^2}} \qquad \qquad \text{ if } y > 0 \\
>
>2\pi - \arccos \frac{x}{\sqrt{x^2 + y^2}} \qquad \text{if } y < 0 \\
>
>0 \qquad \qquad \qquad \qquad \hphantom{,,,,} \text{if } y = 0, x \ge 0 \\
>
>\pi \qquad \qquad \qquad \qquad \hphantom{,,,,} \text{if } y = 0, x \lt 0
>
>\end{cases}
>
>\end{aligned}
>$$
>
>If $\mathbf{p} \in \mathbb{R}^3$ has [spherical coordinates]] $(r, \theta, \phi)$, then its [Cartesian coordinates](./Cartesian%20Coordinate%20System.md) $(x,y,z)$ are
>
>$$
>\begin{aligned}
>
>x &= r \sin \theta \cos \phi \\
>
>y &= r \sin \theta \sin \phi \\
>
>z &= r \cos \theta
>
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Cartesian $\leftrightarrow$ Cylindrical
>
>If $\mathbf{p} \in \mathbb{R}^3$ has [Cartesian coordinates](./Cartesian%20Coordinate%20System.md) $(x,y,z)$, then its [Cylindrical coordinates](./Cylindrical%20Coordinates.md) $(\rho, \phi, z)$ are:
>
>- Using the convention $\rho \ge 0$ and $\phi \in (-\pi; \pi]$:
> 
>$$
>\begin{aligned}
>
>\rho &= \sqrt{x^2 + y^2} \\
>
>\phi &= 
>
>\begin{cases}
>
>\arctan \left( \frac{y}{x} \right) \qquad \qquad \text{if } x \gt 0 \\
>
>\arctan \left( \frac{y}{x} \right) + \pi \qquad \text{ if } x \lt 0, y \ge 0 \\
>
>\arctan \left( \frac{y}{x} \right) - \pi \qquad \text{ if } x \lt 0, y \lt 0 \\
>
>\frac{\pi}{2} \qquad \qquad \qquad \qquad \text{if } x = 0, y \gt 0 \\
>
>-\frac{\pi}{2} \qquad \qquad \qquad \, \, \, \, \, \, \text{ if } x = 0, y \lt 0 \\
>
>0 \qquad \qquad \qquad \qquad \, \text{ if } x = y = 0
>
>\end{cases} \\
>
>z &= z
>
>\end{aligned}
>$$
>
>- Using the convention $\rho \ge 0$ and $\phi \in [[Cylindrical Coordinate System|0; 2\pi)$:
>
>$$
>\begin{aligned}
>
>\rho &= \sqrt{x^2 + y^2} \\
>
>\phi &= 
>
>\begin{cases}
>
>\arccos \frac{x}{\sqrt{x^2 + y^2}} \qquad \qquad \text{ if } y > 0 \\
>
>2\pi - \arccos \frac{x}{\sqrt{x^2 + y^2}} \qquad \text{if } y < 0 \\
>
>0 \qquad \qquad \qquad \qquad \hphantom{,,,,} \text{if } y = 0, x \ge 0 \\
>
>\pi \qquad \qquad \qquad \qquad \hphantom{,,,,} \text{if } y = 0, x \lt 0
>
>\end{cases} \\
>
>z &= z
>
>\end{aligned}
>$$
>
>If $\mathbf{p} \in \mathbb{R}^3$ has [Cylindrical coordinates]] $(\rho, \phi, z)$, then its [Cartesian coordinates](./Cartesian%20Coordinate%20System.md) $(x,y,z)$ are
>
>$$
>\begin{aligned}
>
>x &= \rho \cos \phi \\
>
>y &= \rho \sin \phi \\
>
>z &= z
>
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>