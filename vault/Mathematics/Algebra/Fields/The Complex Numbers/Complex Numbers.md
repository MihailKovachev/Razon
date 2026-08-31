---
tags:
    - algebra
    - mathematics
---

# Complex Numbers

>[!DEFINITION] Definition: Complex Numbers
>
>The **set of complex numbers** is the [set](../../../Set%20Theory/Sets.md) $\mathbb{R}^2$ of all [ordered pairs](../../../Set%20Theory/Tuples.md) of [real numbers](../The%20Real%20Numbers/The%20Real%20Numbers.md) equipped with an addition [operation](../../../Analysis/Functions/Functions.md) $+: \mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}^2$ and a multiplication [operation](../../../Analysis/Functions/Functions.md) $\cdot: \mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}^2$ defined for all $(a,b) \in \mathbb{R}^2$ and all $(c,d) \in \mathbb{R}^2$ as follows:
>
>$$(a,b) + (c,d) \overset{\text{def}}{=} (a + b, c+d)$$
>
>$$(a,b) \cdot (c,d) \overset{\text{def}}{=} (ac-bd, ad+bc)$$
>
>>[!NOTATION]
>>
>>The configuration $(\mathbb{R}^2, +, \cdot)$ is denoted by $\mathbb{C}$. In the context of [complex numbers](./Complex%20Numbers.md), we write $z \in \mathbb{C}$ instead of $z \in \mathbb{R}^2$. Furthermore, instead of writing $(a,b)$, we write $a+\mathrm{i}b$ or $a + b\mathrm{i}$. Sometimes, instead of $\mathrm{i}$, we use the symbol $\mathrm{j}$ or some other symbol specified in the context.
>>
>
>>[!DEFINITION] Definition: Real Part
>>
>>The **real part** of a [complex number](./Complex%20Numbers.md) $z = a + \mathrm{i}b$ is $a$.
>>
>>>[!NOTATION]
>>>
>>>$$\operatorname{Re}(z) \qquad \Re (z)$$
>>>
>>
>
>>[!DEFINITION] Definition: Imaginary Part
>>
>>The **imaginary part** of a [complex number](./Complex%20Numbers.md) $z = a + \mathrm{i}b$ is $b$.
>>
>>>[!NOTATION]
>>>
>>>$$\operatorname{Im}(z) \qquad \Im (z)$$
>>>
>>
>

>[!DEFINITION] Definition: Modulus
>
>The **modulus** of a [complex number](./Complex%20Numbers.md) $z = a + b\mathrm{i}$ is the [square root](TODO) of the sum of the squares of its [real part](./Complex%20Numbers.md) and its [imaginary part](./Complex%20Numbers.md):
>
>$$
>|z| \overset{\text{def}}{=} \sqrt{\Re (z)^2 + \Im (z)^2} = \sqrt{a^2 + b^2}
>$$
>

>[!DEFINITION] Definition: Argument
>
>The **argument** of a [complex number](./Complex%20Numbers.md) $z = x + y \mathrm{i} \ne 0$ is defined using the [arctan function](../../../Analysis/Real%20Analysis/Real%20Functions/Real%20Trigonometric%20Functions/Inverse%20Real%20Trigonometric%20Functions.md) as
>
>$$
>\arg(z) \overset{\text{def}}{=} \begin{cases}\displaystyle\hphantom{-}\arccos \left(\frac{x}{|z|}\right) \qquad \text{ if } y \ge 0 \\ \displaystyle -\arccos \left(\frac{x}{|z|}\right) \qquad \text{ if } y \lt 0\end{cases}
>$$
>
>>[!THEOREM] Theorem: Image of $\arg$
>>
>>The [range](../../../Analysis/Functions/Functions.md) of $\arg$ is $(-\pi; \pi]$.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

## Forms

>[!DEFINITION] Definition: Cartesian Form
>
>Given a [complex number](./Complex%20Numbers.md) $z = a + \mathrm{i}b$, we call $a + \mathrm{i}b$ the **Cartesian form** of $z$.
>

The Cartesian form of a [complex number](./Complex%20Numbers.md) is just the one resulting from its definition. However, there are other, equivalent ways to specify $z$ which often make the solutions of some problems easier and more intuitive.

>[!THEOREM] Theorem: Polar Form
>
>Each [complex number](./Complex%20Numbers.md) $z \ne 0$ can be specified using its [modulus](./Complex%20Numbers.md) $r = |z|$ and the [real trigonometric functions](../../../Analysis/Real%20Analysis/Real%20Functions/Real%20Trigonometric%20Functions/Real%20Trigonometric%20Functions.md) of its [argument](./Complex%20Numbers.md) $\varphi = \arg z$:
>
>$$
>z = r(\cos \varphi + \mathrm{i} \sin \varphi)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Polar Form
>>
>>We call $r(\cos \varphi + \mathrm{i} \sin \varphi)$ the **polar form** of $z$.
>>
>
>>[!NOTE] Note: Infinitely Many Polar Forms
>>
>>We can also construct other, still equivalent [polar forms](#Forms) of $z$ by adding an [integer](TODO) multiple of $2\pi$ to $\varphi$ because $\cos$ and $\sin$ are [periodic](../../../Analysis/Real%20Analysis/Real%20Functions/Periodicity.md).
>>
>

There is also a third way to specify [complex numbers](./Complex%20Numbers.md) using [Euler's formula](../../../Analysis/Complex%20Analysis/Complex%20Functions/Complex%20Exponential%20Function.md).

>[!THEOREM] Theorem: Exponential Form
>
>Each [complex number](./Complex%20Numbers.md) $z \ne 0$ can be specified using its [modulus](./Complex%20Numbers.md) and the [complex exponential](../../../Analysis/Complex%20Analysis/Complex%20Functions/Complex%20Exponential%20Function.md) of its [argument](./Complex%20Numbers.md):
>
>$$
>z = |z| \mathrm{e}^{\mathrm{i} \arg(z)}
>$$
>
>>[!PROOF]-
>>
>>Using [Euler's formula](../../../Analysis/Complex%20Analysis/Complex%20Functions/Complex%20Exponential%20Function.md) we obtain
>>
>>$$
>>|z|\mathrm{e}^{\mathrm{i} \arg(z)} = |z|(\cos (\arg (z)) + \mathrm{i} \sin (\arg (z))),
>>$$
>>
>>which is the canonical [polar form](#Forms) of $z$.
>>
>
>>[!DEFINITION] Definition: Exponential Form
>>
>>We call $|z| \mathrm{e}^{\mathrm{i} \arg(z)}$ the **exponential form** of $z$.
>>
>

# Operations

>[!DEFINITION] Definition: Complex Conjugation
>
>The **(complex) conjugate** of a [complex number](./Complex%20Numbers.md) $z = a + \mathrm{i}b$ is the [complex number](./Complex%20Numbers.md)
>
>$$
>\bar{z} \overset{\text{def}}{=} a + \mathrm{i}(-b) = a - \mathrm{i}b
>$$
>

>[!DEFINITION] Definition: Addition
>
>The **sum** of two [complex numbers](./Complex%20Numbers.md) $z_1 = a_1 + \mathrm{i}b_1$ and $z_2 = a_2 + \mathrm{i} b_2$ is defined as the [complex number](./Complex%20Numbers.md)
>
>$$
>z_1 + z_2 \overset{\text{def}}{=} (a_1 + a_2) + \mathrm{i}(b_1 + b_2)
>$$
>
>>[!NOTATION] Notation: Subtraction
>>
>>We write $-z_2$ for $-a_2 - \mathrm{i}b_2$ and write $z_1 - z_2$ instead of $z_1 + (-z_2)$.
>>
>

>[!DEFINITION] Definition: Multiplication
>
>The **product** of two [complex numbers](./Complex%20Numbers.md) $z_1 = a_1 + \mathrm{i}b_1$ and $z_2 = a_2 + \mathrm{i} b_2$ is defined as the [complex number](./Complex%20Numbers.md)
>
>$$
>z_1 \cdot z_2 \overset{\text{def}}{=} (a_1 a_2 - b_1 b_2) + \mathrm{i}(a_1 b_2 + b_1 a_2)
>$$
>
>>[!THEOREM] Theorem: Multiplication in Polar Form
>>
>>If the [polar forms](#Forms) of $z_1$ and $z_2$ are
>>
>>$$
>>\begin{aligned}
>>&z_1 = r_1 (\cos \varphi_1 + \mathrm{i} \sin \varphi_1) \\
>>&z_2 = r_2 (\cos \varphi_2 + \mathrm{i} \sin \varphi_2)
>>\end{aligned}
>>$$
>>
>>then the [polar form](#Forms) of $z_1 \cdot z_2$ is
>>
>>$$
>>z_1 \cdot z_2 = r_1 r_2 (\cos (\varphi_1 + \varphi_2) + \mathrm{i} \sin (\varphi_1 + \varphi_2))
>>$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>
>>[!THEOREM] Theorem: Multiplication in Exponential Form
>>
>>The [exponential form](#Forms) of $z_1 \cdot z_2$ is
>>
>>$$
>>z_1 \cdot z_2 = |z_1| \, |z_2| \mathrm{e}^{\mathrm{i}(\arg z_1 + \arg z_2)}
>>$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

>[!DEFINITION] Definition: Division
>
>The **division** of a [complex number](./Complex%20Numbers.md) $z_1$ by a [complex number](./Complex%20Numbers.md) $z_2$ is the [complex number](./Complex%20Numbers.md)
>
>$$
>\frac{z_1}{z_2} \overset{\text{def}}{=} \frac{z_1\cdot \bar{z}_2}{|z_2|^2}
>$$
>
>>[!THEOREM] Theorem: Division in Polar Form
>>
>>If the [polar forms](#Forms) of $z_1$ and $z_2$ are
>>
>>$$
>>\begin{aligned}
>>&z_1 = r_1 (\cos \varphi_1 + \mathrm{i} \sin \varphi_1) \\
>>&z_2 = r_2 (\cos \varphi_2 + \mathrm{i} \sin \varphi_2)
>>\end{aligned}
>>$$
>>
>>then the [polar form](#Forms) of $\frac{z_1}{z_2}$ is
>>
>>$$
>>\frac{z_1}{z_2} = \frac{r_1}{r_2} (\cos (\varphi_1 - \varphi_2) + \mathrm{i} \sin (\varphi_1 - \varphi_2))
>>$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>
>>[!THEOREM] Theorem: Division in Exponential Form
>>
>>The [exponential form](#Forms) of $\frac{z_1}{z_2}$ is
>>
>>$$
>>\frac{z_1}{z_2} = \frac{|z_1|}{|z_2|} \mathrm{e}^{\mathrm{i}(\arg z_1 - \arg z_2)}
>>$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

>[!THEOREM] Theorem: The Field of Complex Numbers
>
>The [complex numbers](./Complex%20Numbers.md) $\mathbb{C}$ form a [field](../Fields.md) $(\mathbb{C}, +, \cdot)$ with the [addition](#Operations), [multiplication](#Operations) defined on them.
>
>>[!PROOF]-
>>
>>We need to prove the following:
>>
>>- (1) $z_1 + (z_2 + z_3) = (z_1 + z_2) + z_3$ for all $z_1, z_2, z_3 \in \mathbb{C}$;
>>- (2) $z_1 \cdot (z_2 \cdot z_3) = (z_1 \cdot z_2) \cdot z_3$ for all $z_1, z_2, z_3 \in \mathbb{C}$;
>>- (3) $z + w = w + z$ for all $z, w \in \mathbb{C}$;
>>- (4) $z \cdot w = w \cdot z$ for all $z, w \in \mathbb{C}$;
>>- (5) $z + 0 = z$ for all $z \in \mathbb{C}$;
>>- (6) $z \cdot 1 = z$ for all $z \in \mathbb{C}$;
>>- (7) $z - z = 0$ for all $z \in \mathbb{C}$;
>>- (8) $z \cdot \frac{1}{z} = 1$ for all $z \in \mathbb{C}$;
>>- (9) $z \cdot (u + v) = z \cdot u + z \cdot v$ for all $z, u, v \in \mathbb{C}$.
>>
>>**Proof of (1):** *The following proof was generated by AI and has not been human-verified. As such, it may contain mistakes.*
>>
>>We want to show $z_1 + (z_2 + z_3) = (z_1 + z_2) + z_3$.
>>
>>$$
>>\begin{aligned}
>>z_1 + (z_2 + z_3) &= (a_1 + b_1i) + ((a_2 + b_2i) + (a_3 + b_3i)) \\
>>&= (a_1 + b_1i) + ((a_2 + a_3) + (b_2 + b_3)i) \\
>>&= (a_1 + (a_2 + a_3)) + (b_1 + (b_2 + b_3))i \\
>>&= ((a_1 + a_2) + a_3) + ((b_1 + b_2) + b_3)i \\
>>&= ((a_1 + a_2) + (b_1 + b_2)i) + (a_3 + b_3i) \\
>>&= ((a_1 + b_1i) + (a_2 + b_2i)) + (a_3 + b_3i) \\
>>&= (z_1 + z_2) + z_3
>>\end{aligned}
>>$$
>>
>>**Proof of (2):** *The following proof was generated by AI and has not been human-verified. As such, it may contain mistakes.*
>>
>>We want to show $z_1 \cdot (z_2 \cdot z_3) = (z_1 \cdot z_2) \cdot z_3$.
>>
>>First, we compute the left-hand side:
>>$$
>>\begin{aligned}
>>z_2 \cdot z_3 &= (a_2a_3 - b_2b_3) + (a_2b_3 + b_2a_3)i \\
>>z_1 \cdot (z_2 \cdot z_3) &= (a_1 + b_1i) \cdot ((a_2a_3 - b_2b_3) + (a_2b_3 + b_2a_3)i) \\
>>&= (a_1(a_2a_3 - b_2b_3) - b_1(a_2b_3 + b_2a_3)) + (a_1(a_2b_3 + b_2a_3) + b_1(a_2a_3 - b_2b_3))i \\
>>&= (a_1a_2a_3 - a_1b_2b_3 - b_1a_2b_3 - b_1b_2a_3) + (a_1a_2b_3 + a_1b_2a_3 + b_1a_2a_3 - b_1b_2b_3)i
>>\end{aligned}
>>$$
>>
>>**Proof of (3):** *The following proof was generated by AI and has not been human-verified. As such, it may contain mistakes.*
>>
>>
>>
>>**Proof of (4):** *The following proof was generated by AI and has not been human-verified. As such, it may contain mistakes.*
>>
>>
>>
>>**Proof of (5):** *The following proof was generated by AI and has not been human-verified. As such, it may contain mistakes.*
>>
>>
>>
>>**Proof of (6):** *The following proof was generated by AI and has not been human-verified. As such, it may contain mistakes.*
>>
>>
>>
>>**Proof of (7):** *The following proof was generated by AI and has not been human-verified. As such, it may contain mistakes.*
>>
>>
>>
>>**Proof of (8):** *The following proof was generated by AI and has not been human-verified. As such, it may contain mistakes.*
>>
>>
>>
>>**Proof of (9):** *The following proof was generated by AI and has not been human-verified. As such, it may contain mistakes.*
>>
>>
>>
>

>[!THEOREM] Theorem: Distributivity of Complex Conjugation
>
>[Complex conjugation](#Operations) is distributive over [addition](#Operations), [multiplication](#Operations) and [division](#Operations):
>
>$$
>\begin{aligned}
>\overline{z_1 + z_2} &= \bar{z}_1 + \bar{z}_2 \\
>\overline{z_1 \cdot z_2} &= \bar{z}_1 \cdot \bar{z}_2 \\
>\overline{\left(\frac{z_1}{z_2}\right)} &= \frac{\bar{z}_1}{\bar{z}_2} \qquad z_2 \ne 0
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Conjugate Multiplication and Modulus
>
>[Multiplying](#Operations) a [complex number](./Complex%20Numbers.md) by its [conjugate](#Operations) results in the square of its [modulus](./Complex%20Numbers.md):
>
>$$
>z\cdot\bar{z} = |z|^2
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Triangle Inequality
>
>The [modulus](./Complex%20Numbers.md) has the following property for all $z_1, z_2 \in \mathbb{C}$:
>
>$$
>|z_1 + z_2| \le |z_1| + |z_2|
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Modulus Product
>
>The [modulus](./Complex%20Numbers.md) has the following property for all $z, w \in \mathbb{C}$:
>
>$$
>|z \cdot w| = |z|\cdot|w|
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## The Complex Plane

[Complex numbers](../../../../index.md) can be plotted on a plane where the horizontal axis contains the [real numbers](../The%20Real%20Numbers/The%20Real%20Numbers.md) and the vertical axis contains the [imaginary numbers](../../../../index.md#imaginary%20numbers).

![The Complex Plane](../res/The%20Complex%20Plane.svg)
