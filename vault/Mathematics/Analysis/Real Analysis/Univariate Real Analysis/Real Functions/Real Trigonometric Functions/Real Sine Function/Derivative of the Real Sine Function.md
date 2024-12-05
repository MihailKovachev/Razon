>[!THEOREM] Theorem: Derivative of the Real Sine Function
>
>The [derivative](../../../Differentiation/Differentiability%20of%20Real%20Functions.md) of the [real sine function](Real%20Sine%20Function.md) is the [real cosine function](../Real%20Cosine%20Function/Real%20Cosine%20Function.md).
>
>$$
>(\sin x)' = \cos x
>$$
>
>>[!PROOF]-
>>
>>$$
>>\begin{align*}(\sin x)'  &= \lim_{\Delta x\to 0} \frac{\sin (x + \Delta x) - \sin x}{\Delta x} = \lim_{\Delta x\to 0} \frac{2\sin\frac{\Delta x}{2}\cos\frac{2x + \Delta x}{2}}{\Delta x} \\ &= \lim_{\Delta x \to 0}\frac{\sin\frac{\Delta x}{2}}{\frac{\Delta x}{2}}\lim_{\Delta x \to 0} \cos\left(x + \frac{\Delta x}{2}\right) = 1 \cdot \cos x = \cos x\end{align*}
>>$$
>>
>