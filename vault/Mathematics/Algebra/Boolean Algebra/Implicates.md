---
tags:
    - boolean-algebra
    - algebra
    - mathematics
---

# Implicates

>[!DEFINITION] Definition: Implicate
>
>An **implicate** of a [Boolean function](./Boolean%20Functions.md) $f(x_1, \dotsc, x_n)$ is any [clause](./Boolean%20Expressions.md) $C$ such that if the value of $f$ is $1$, then the value of $C$ is also $1$:
>
>$$
>f \implies C
>$$
>
>>[!EXAMPLE]
>>
>>Consider $f(x, y, z) = \overline{x}\overline{y} + z$. The [clause](./Boolean%20Expressions.md) $\overline{x} + z$ is an [implicate](./Implicates.md) of $f$.
>>
>
>>[!THEOREM] Theorem: Implicate Test
>>
>>A [clause](./Boolean%20Expressions.md) $C$ is an [implicate](#Implicates) of $f$ if and only if
>>
>>$$
>>C = 0 \implies f = 0.
>>$$ 
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

>[!DEFINITION] Definition: Prime Implicate
>
>A **prime implicate** is an [implicate](#Implicates) such that removing any [literal](./Boolean%20Expressions.md) from it no longer results in an [implicate](#Implicates).
>
>>[!EXAMPLE]
>>
>>Consider $f(x, y, z) = (x + y + \overline{z})(\overline{x} + y + \overline{z})(\overline{x} + \overline{y} + \overline{z})$. Here, $x + y + \overline{z}$ is an [implicate](#Implicates) of $f$, but it is *not* a [prime implicate](#Implicates), since removing $x$ results in $y + \overline{z}$, which is still an [implicate](#Implicates). 
>>
>>However, $y + \overline{z}$ *is* a [prime implicate](./Implicates.md) because removing either $y$ or $\overline{z}$ results in something which is no longer an [implicate](#Implicates). 
>>
>

>[!DEFINITION] Definition: Covering
>
>We say that an [implicate](#Implicates) $C$ **covers** a [maxterm](./Boolean%20Expressions.md) $M$ if the [literals](./Boolean%20Expressions.md) in $C$ are a [subset](../../Set%20Theory/Sets.md) of the [literals](./Boolean%20Expressions.md) in $M$.
>
>>[!EXAMPLE]
>>
>>Consider $f(x, y, z) = (x + \overline{y} + z)(x + \overline{y} + \overline{z})(\overline{x} + y + z)(\overline{x} + \overline{y} + z)$.
>>
>>The [implicate](./Implicates.md) $x + \overline{y}$ [covers](./Implicates.md) both $(x + \overline{y} + z)$ and $(x + \overline{y} + \overline{z})$.
>>
>>The [implicate](./Implicates.md) $\overline{x} + y + z + \overline{x}$ [covers](./Implicates.md) only $\overline{x} + y + z$.
>>
>
>>[!THEOREM] Theorem: Alternative Definitions
>>
>>An [implicate](#Implicates) $C$ [covers](#Implicates) a [maxterm](./Boolean%20Expressions.md) $M$ if and only if $C \implies M$.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

>[!DEFINITION] Definition: Essential Prime Implicate
>
>A [prime implicate](#Implicates) $C$ of a [conjunctive normal form](./Boolean%20Expressions.md) is **essential** if there exists a [maxterm](./Boolean%20Expressions.md) $M$ in the [CNF](./Boolean%20Expressions.md) such that $C$ is the only [prime implicate](#Implicates) which [covers](#Implicates) $M$.
>
>>[!EXAMPLE]
>>
>>Consider $f(x, y, z) = (x + \overline{y} + z)(x + \overline{y} + \overline{z})(\overline{x} + y + z)(\overline{x} + \overline{y} + z)$.
>>
>>Its [prime implicates](#Implicates) are $(x + \overline{y})$, $(\overline{y} + z)$ and $(\overline{x} + z)$. Of these, $(x + \overline{y})$ and $(\overline{x} + z)$ are [essential](#Implicates) because $x + \overline{y} + \overline{z}$ is only [covered](#Implicates) by $(x + \overline{y})$ and $\overline{x} + y + z$ is only [covered](#Implicates) by $(\overline{x} + z)$.
>>
>

>[!ALGORITHM] Algorithm: Implicates from Karnaugh Maps
>
>We are given a [Karnaugh map](./Karnaugh%20Maps.md) for a [Boolean function](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}$ and want to find the [essential prime implicates](#Implicates) of $f$.
>
>1. Group the cells according to the following rules:
>    - Each group must contain only $0$s.
>    - The total number of cells in a group must be a power of $2$.
>    - The shape of a group must be rectangular. For the purposes of this, the top and bottom row are considered adjacent and so are the left-most and right-most column. 
>2. Each group constructed in the above way corresponds to a single [implicate](#Implicates) of $f$. This [implicate](#Implicates) is obtained as follows:
>    - If a [variable](./Boolean%20Expressions.md) remains a constant $0$ at all cells in the group, then include it in the [implicate](#Implicates).
>    - If a [variable](./Boolean%20Expressions.md) remains a constant $1$ at all cells in the group, then include its [negation](./Negation.md) in the [implicate](#Implicates).
>    - If a [variable](./Boolean%20Expressions.md) is a $1$ at some cells in the group and a $0$ at others, then ignore it.
>3. Do this until all possible groups have been examined to obtain all [implicates](#Implicates) of $f$.
>    - If we are specifically looking for [prime implicates](#Implicates), then we can speed up the process by first looking at the largest possible groups.
>
>>[!TIP] Tip: Prime implicates
>>
>>If it is not possible to combine a group with an adjacent group with the same number of cells and still obtain a valid group, then this group corresponds to a [prime implicate](#Implicates).
>>
>
>>[!TIP] Tip: Essential Prime implicates
>>
>>If a cell is contained in only a single group and this group corresponds to a [prime implicate](#Implicates), then this group corresponds to an [essential prime implicate](#Implicates).
>>
>>
>
>>[!EXAMPLE]-
>>
>>Consider the [function](./Boolean%20Functions.md) $f(x,y,z,w)$ with the following [Karnaugh Maps](./Karnaugh%20Maps.md):
>>
>>
>>![Implicates from Karnaugh Map Example](./res/Implicates%20from%20Karnaugh%20Map%20Example.svg)
>>
>>Here are some possible groups:
>>
>>![Implicate Groups Example](./res/Implicate%20Groups%20Example.svg)
>>
>>The blue group can be formed thanks to the rule adjacency rule. In this group, $y$, $z$ and $w$ are always zero, so this group corresponds to the [implicate](#Implicates) $y + z + w$. However, this is not a [prime implicate](#Implicates) because we can merge the four corners into a single group.
>>
>>The red group corresponds to the [implicate](#Implicates) $\overline{x} + \overline{y} +\overline{w}$ because $x$, $y$ and $w$ are always $1$ within the group. However, this is not a [prime implicate](#Implicates) because we can combine this group with a group obtained by the cell above and the cell below to obtain a new valid group.
>>
>>The green group corresponds to the [implicate](#Implicates) $\overline{z} + w$ because $z$ is always $1$ within the group and $\overline{w}$ is always $0$ within the group. Furthermore, this is a [prime implicate](#Implicates) because the group cannot be merged into a new group with any other group of the same size. Moreover, this is an [essential prime implicate](#Implicates) because it is impossible to construct another group which corresponds to a [prime implicate](#Implicates) and also contains the cell at the last row and second column.
>>
>>>[!NOTE]
>>>
>>>These are not *all* of $f$'s [implicates](#Implicates), since these are just three possible groups.
>>>
>>
>>
>
