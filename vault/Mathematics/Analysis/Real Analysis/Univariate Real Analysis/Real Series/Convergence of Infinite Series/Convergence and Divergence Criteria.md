>[!THEOREM] Theorem
>
>An [infinite series](../Infinite%20Series.md) $\displaystyle \sum_{k = 1}^\infty a_k$ [diverges](Divergence%20of%20an%20Infinite%20Series.md) if $(a_n)_{n\in \mathbb{N}}$ does not [approach](../../Real%20Sequences/Limits%20of%20Sequences/Convergence%20of%20Real%20Sequences.md) $0$.
>
>>[!PROOF]-
>>
>>TODO
>>

>[!THEOREM] Theorem: Minorant Criterion
>
>An [infinite series](../Infinite%20Series.md) $\displaystyle \sum_{k = 1}^\infty a_k$ [diverges](Divergence%20of%20an%20Infinite%20Series.md) if there are a [divergent](Divergence%20of%20an%20Infinite%20Series.md) [series](../Infinite%20Series.md) $\displaystyle \sum_{k = 1}^\infty b_k$ and some $N \in \mathbb{N}$ such that
>
>$$0 \le b_k \le a_k \qquad \forall k \ge N$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Majorant Criterion
>
>An [infinite series](../Infinite%20Series.md) $\displaystyle \sum_{k = 1}^\infty a_k$  [converges absolutely](Absolute%20Convergence%20of%20Infinite%20Series.md) if there are a [convergent](Convergence%20of%20an%20Infinite%20Series.md) [series](../Infinite%20Series.md) $\displaystyle \sum_{k = 1}^\infty b_k$ and some $N \in \mathbb{N}$ such that
>
>$$|a_k| \le b_k \qquad \forall k\ge N$$
>
>>[!PROOF]-
>>
>>TODO
>>

>[!THEOREM] Theorem: Quotient Criterion
>
>An [infinite series](../Infinite%20Series.md) $\displaystyle \sum_{k = 1}^\infty a_k$ is:
>- [absolutely convergent](Absolute%20Convergence%20of%20Infinite%20Series.md) if the following [limit](../../Real%20Functions/Limits%20of%20Functions/Limits%20of%20a%20Function.md) exists and is smaller than $1$
>
>$$\lim_{k\to\infty} \left|\frac{a_{k+1}}{a_k}\right| \lt 1$$
>
>- [divergent](Divergence%20of%20an%20Infinite%20Series.md) if the [limit](../../Real%20Functions/Limits%20of%20Functions/Limits%20of%20a%20Function.md) exists but is greater than $1$
>
>$$\lim_{k\to\infty} \left|\frac{a_{k+1}}{a_k}\right| \gt 1$$
>
>>[!NOTE]
>>
>>If $\displaystyle \lim_{k\to\infty} \left|\frac{a_{k+1}}{a_k}\right| = 1$, then this theorem cannot tell us anything.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Square Root Criterion
>
>An [infinite series](../Infinite%20Series.md) $\displaystyle \sum_{k = 1}^\infty a_k$ is:
>- [absolutely convergent](Absolute%20Convergence%20of%20Infinite%20Series.md) if the following [limit](../../Real%20Functions/Limits%20of%20Functions/Limits%20of%20a%20Function.md) exists and is smaller than $1$
>
>$$\lim_{k\to\infty} \sqrt[k]{|a_k|} \lt 1$$
>
>- [divergent](Divergence%20of%20an%20Infinite%20Series.md) if the [limit](../../Real%20Functions/Limits%20of%20Functions/Limits%20of%20a%20Function.md) exists but is greater than $1$
>
>$$\lim_{k\to\infty} \sqrt[k]{|a_k|} \gt 1$$
>
>>[!NOTE]
>>
>>If $\displaystyle \lim_{k\to\infty} \sqrt[k]{a_k} = 1$, then this theorem cannot tell us anything.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>