---
title: Operations with Complex Numbers
tags:
  - operations
  - complex-numbers
  - abstract-algebra
  - algebra
  - mathematics
---

# Complex Conjugation

>[!DEFINITION] Definition: Complex Conjugate
>
>The **complex conjugate** of a [complex number](./index.md#complex%20numbers) $z = a +\mathrm{i}b$ is the number
>
>$$
>\bar z \overset{\text{def}}{=} a - \mathrm{i}b
>$$
>

>[!THEOREM] Theorem: Distributivity of Complex Conjugation
>
>The [complex conjugation](Operations.md) of is distributive over [addition](Operations.md) and [multiplication](Operations.md):
>
>$$
>\overline{z_1 + z_2} = \bar{z}_1 + \bar{z}_2
>$$
>
>$$
>\overline{z_1 \cdot z_2} = \bar{z}_1 \cdot \bar{z}_2
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Arithmetic with Complex Numbers

>[!DEFINITION] Definition: Addition and Subtraction of Complex Numbers
>
>The **addition** and **subtraction** of two [complex numbers](./index.md) $z_1 = a + \mathrm{i}b$ and $z_2 = c +\mathrm{i}d$ are defined as
>
>$$
>z_1 \pm z_2 \overset{\text{def}}{=} (a\pm c) + \mathrm{i}(b \pm d)
>$$

>[!DEFINITION] Definition: Multiplication of Complex Numbers
>
>The **multiplication** of two [complex numbers](./index.md) $z_1 = a + \mathrm{i}b$ and $z_2 = c +\mathrm{i}d$ is defined as
>
>$$
>z_1 \cdot z_2 \overset{\text{def}}{=} (ac - bd) + \mathrm{i}(ad + bc)
>$$
>
>>[!THEOREM] Theorem: Multiplication in Polar Form
>>
>>If $z_1$ and $z_2$ have the [polar forms](./index.md#the%20forms%20of%20a%20complex%20number) $z_1 = r_1(\cos \varphi_1 +\mathrm{i}\sin\varphi_1)$ and $z_2 = r_2(\cos \varphi_2 +\mathrm{i}\sin\varphi_2)$, then
>>
>>$$
>>z_1\cdot z_2 = r_1r_2(\cos (\varphi_1+\varphi_2) +\mathrm{i}\sin(\varphi_1+\varphi_2))
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
>>If $z_1$ and $z_2$ have the [exponential forms](./index.md#the%20forms%20of%20a%20complex%20number) $z_1 = r_1\mathrm{e}^{\mathrm{i}\varphi_1}$ and $z_2 = r_2\mathrm{e}^{\mathrm{i}\varphi_2}$, then
>>
>>$$
>>z_1 \cdot z_2 = r_1r_2\mathrm{e}^{\mathrm{i}(\varphi_1+\varphi_2)}
>>$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>>

>[!DEFINITION] Definition: Division of Complex Numbers
>
>The **division** of two [complex numbers](./index.md) $z_1 = a + \mathrm{i}b$ and $z_2 = c +\mathrm{i}d$ is
>
>$$
>\frac{z_1}{z_2} \overset{\text{def}}{=} \frac{z_1\cdot \bar{z}_2}{|z_2|^2}
>$$
>

>[!THEOREM] Theorem: The Field of the Complex Numbers
>
>The [set](../../../Set%20Theory/index.md) of all [complex numbers](./index.md) $\mathbb{C}$ forms a [field](../index.md) together with the [addition and multiplication](Operations.md) defined on it.
>
>>[!PROOF]-
>>
>>TODO
>>
>