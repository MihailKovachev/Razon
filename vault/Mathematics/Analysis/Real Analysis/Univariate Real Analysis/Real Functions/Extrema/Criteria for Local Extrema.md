>[!THEOREM] Theorem: Critical Points and Local Extrema
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Function.md).
>
>All [local extrema](Local%20Extrema.md) of $f$ occur at [critical points](../../Differentiation/Critical%20Point.md) of $f$.
>
>>[!PROOF]-
>>
>>TODO
>
>>[!THEOREM] Theorem: Criteria of the First Derivative
>>If $f$ is [continuous](../Continuity/Continuity.md) and [differentiable](../../Differentiation/Differentiability%20of%20Real%20Functions.md) at a [critical point](../../Differentiation/Critical%20Point.md) $x_0$, then:
>>- $f$ has a [local minimum](Local%20Extrema.md) at $x_0$ if there is some $\varepsilon \gt 0$ such that
>>
>>$$f'(x) \lt 0 \qquad \forall x \in (x_0 - \varepsilon; x_0) \qquad \text{ and } \qquad f'(x) \gt 0 \qquad \forall x \in (x_0; x_0 + \varepsilon)$$
>>
>>- $f$ has a [local maximum](Local%20Extrema.md) at $x_0$ if there is some $\varepsilon \gt 0$ such that
>>
>>$$f'(x) \gt 0 \quad \forall x \in (x_0-\varepsilon; x_0)\qquad \text{ and } \qquad f'(x) \lt 0 \quad \forall x\in (x_0; x_0+\varepsilon)$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>
>
>>[!THEOREM] Theorem: Criteria of the Second Derivative
>>
>>If $f$ is [continuous](../Continuity/Continuity.md) and [twice differentiable](../../Differentiation/Differentiability%20of%20Real%20Functions.md) at a [critical point](../../Differentiation/Critical%20Point.md) $x_0$, then:
>>
>>- $f$ has a [local minimum](Local%20Extrema.md) at $x_0$ if its [second derivative](../../Differentiation/Differentiability%20of%20Real%20Functions.md) at $x_0$ is positive, i.e. $f''(x_0) \gt 0$;
>>- $f$ has a [local maximum](Local%20Extrema.md) at $x_0$ if its [second derivative](../../Differentiation/Differentiability%20of%20Real%20Functions.md) at $x_0$ is negative, i.e. $f''(x_0) \lt 0$.
>>
>>>[!WARNING]
>>>If $f''(x_0) = 0$ or $f$ is not [twice differentiable](../../Differentiation/Differentiability%20of%20Real%20Functions.md) at $x_0$, then $f$ may or may not have a [local extremum](Local%20Extrema.md) at $x_0$, but we cannot use the second derivative to verify this.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>
>
