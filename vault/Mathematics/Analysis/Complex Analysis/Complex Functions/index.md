---
title: Complex Functions
tags:
    - complex-functions
    - complex-analysis
---

# Complex Functions

>[!DEFINITION] Definition: Univariate Complex Function
>
>A **complex function** is a [complex-valued function](Complex-Valued%20Function.md), whose [domain](../../Functions/Function.md) is a [subset](../../../Set%20Theory/Subset.md) of the [complex numbers](../../../Algebra/Fields/Complex%20Numbers/Complex%20Numbers.md):
>
>$$
>f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}
>$$
>

# Visualizing Complex Functions

Visualizing a complex function $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ is tricky because it requires four dimensions - one dimension for the real part of $z$, one dimension for the imaginary part of $z$, one dimension for the real part of $f(z)$ and one dimension for the imaginary part of $f(z)$. However, we cannot really visualize four-dimensional structures and thus have to resort to certain tricks for condensing or expressing information about the graph of $f$.

## $z$-$w$ Planes

The simplest way to visualize a complex function is to use two instances of the [complex plane](../../../Algebra/Fields/Complex%20Numbers/The%20Complex%20Plane.md). On one plane, illustrate the [domain](../../Functions/Domain%20of%20a%20Function.md) of $f$. This plane is usually called the $z$-plane. On the other plane, illustrate $f$'s [image](../../Functions/Image%20of%20a%20Function.md). This plane is usually called the $w$-plane.

![](Complex%20Functions/res/z-w%20Planes.svg)

The main advantage of this type of visualization is that it provides a general idea of how $f$ transforms its domain and what the end result looks like. However, this type of plot does not make it clear what the functional value of each individual point is. Given a specific $w \in \mathbb{C}$, one cannot infer from this visualization which $z \in \mathbb{C}$ result in $w$, i.e. which $z$ give $f(z) = w$.  

## Domain Coloring

Domain coloring uses colors to represent the function's values. The [domain](../../Functions/Domain%20of%20a%20Function.md) $\mathcal{D}$ of $f$ is illustrated on the [complex plane](../../../Algebra/Fields/Complex%20Numbers/The%20Complex%20Plane.md) and each $z \in \mathcal{D}$ is colored depending on $f(z)$. 

There are multiple conventions for how colors should be assigned. The most common one is to use [argument](../../../Algebra/Fields/Complex%20Numbers/Argument%20of%20a%20Complex%20Number.md) of $f(z)$ to determine the hue (whether the color is red, green, blue, yellow, etc.) and the [absolute value](../../../Algebra/Fields/Complex%20Numbers/Absolute%20Value%20of%20a%20Complex%20Number.md) of $f(z)$ to determine the color's lightness. As the absolute value approaches zero, the color gets darker until it eventually becomes black when $f(z) = 0$. As the absolute value shoots off to infinity, the color gets lighter and lighter, approaching pure white.

Here is the domain coloring plot for $\displaystyle f(z) = z^2 + \frac{1}{z}$:

![](Complex%20Functions/res/Domain%20Coloring.png)

The main advantage of domain coloring is that it clearly shows the places where $f(z)$ is zero (dark spots) or shoots off to infinity in some direction (bright spots).