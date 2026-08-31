---
tags:
    - functional-analysis
    - analysis
    - mathematics
---

# Evaluation Functional

>[!DEFINITION] Definition: Evaluation Functional
>
>Let $X$ and $Y$ be [sets](../../Set%20Theory/Sets.md), let $Y^X$ be the [set](../../Set%20Theory/Sets.md) of all [functions](../Functions/Functions.md) from $X$ to $Y$ and let $p \in X$..
>
>The **evaluation functional** centered at $p$ is the [function](../Functions/Functions.md) $E_p: Y^X \to Y$ which extracts the value of each [function](../Functions/Functions.md) $f: X \to Y$ at $p$:
>
>$$E_p (f) \overset{\text{def}}{=} f(p)$$
>
>>[!NOTATION]
>>
>>Instead of $E_p(f)$, we commonly use one of the following notations:
>>
>>$$\langle E_p , f\rangle \qquad E_p[f] \qquad E_p\{f\} \qquad f\vert_p \qquad f(x)\vert_{x=p}$$
>>
>

>[!THEOREM] Theorem: Linearity of the Evaluation Functional
>
>Let $X$ be a [set](../../Set%20Theory/Sets.md), let $Y$ be a [vector space](../../Algebra/Vector%20Spaces/Vector%20Spaces.md), let $Y^X$ be the [canonical vector space](./Function%20Spaces.md) of all [functions](../Functions/Functions.md) from $X$ to $Y$ and let $p \in X$.
>
>The [evaluation functional](./Evaluation%20Functional.md) $E_p$ is [linear](./Linearity/Linearity%20(Functions).md):
>
>$$E_p (\alpha f + \beta g) = \alpha E_p (f) + \beta E_p (g)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>