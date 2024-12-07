>[!DEFINITION] Definition: Addition and Subtraction of Complex Numbers
>
>The **addition** and **subtraction** of two [complex numbers](Complex%20Number.md) $z_1 = a + \mathrm{i}b$ and $z_2 = c +\mathrm{i}d$ are defined as
>
>$$
>z_1 \pm z_2 \overset{\text{def}}{=} (a\pm c) + \mathrm{i}(b \pm d)
>$$

>[!DEFINITION] Definition: Multiplication of Complex Numbers
>
>The **multiplication** of two [complex numbers](Complex%20Number.md) $z_1 = a + \mathrm{i}b$ and $z_2 = c +\mathrm{i}d$ is defined as
>
>$$
>z_1 \cdot z_2 \overset{\text{def}}{=} (ac - bd) + \mathrm{i}(ad + bc)
>$$
>
>>[!THEOREM] Theorem: Multiplication in Polar Form
>>
>>If $z_1$ and $z_2$ have the [polar forms](Polar%20Form%20of%20Complex%20Numbers.md) $z_1 = r_1(\cos \varphi_1 +\mathrm{i}\sin\varphi_1)$ and $z_2 = r_2(\cos \varphi_2 +\mathrm{i}\sin\varphi_2)$, then
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
>>If $z_1$ and $z_2$ have the [exponential forms](Exponential%20Form%20of%20Complex%20Numbers.md) $z_1 = r_1\mathrm{e}^{\mathrm{i}\varphi_1}$ and $z_2 = r_2\mathrm{e}^{\mathrm{i}\varphi_2}$, then
>>
>>$$
>>z_1 \cdot z_2 = r_1r_2\mathrm{e}^{\mathrm{i}(\varphi_1+\varphi_2)}
>>$$
>>
>>>[!PROOF]-
>>>
>>>This follows directly from the multiplication formula in polar form and [Euler's formula](Euler's%20Formula.md).
>>>
>>
>>

>[!DEFINITION] Definition: Division of Complex Numbers
>
>The **division** of two [complex numbers](Complex%20Number.md) $z_1 = a + \mathrm{i}b$ and $z_2 = c +\mathrm{i}d$ is defined through the [absolute value](Absolute%20Value%20of%20a%20Complex%20Number.md) and the [complex conjugation](Complex%20Conjugation/Complex%20Conjugation.md):
>
>$$
>\frac{z_1}{z_2} \overset{\text{def}}{=} \frac{z_1\cdot \bar{z}_2}{|z_2|^2}
>$$
>
>