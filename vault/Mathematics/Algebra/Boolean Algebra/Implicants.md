---
tags:
  - boolean-algebra
  - algebra
  - mathematics
---

# Implicants

>[!DEFINITION] Definition: Implicant
>
>An **implicant** of a [Boolean function](./Boolean%20Functions.md) $f(x_1, \dotsc, x_n)$ is any [product term](./Boolean%20Expressions.md) $P$ such that if the value of $P$ is $1$, then the value of $f$ is also $1$:
>
>$$
>P = 1 \implies f = 1
>$$
>
>>[!EXAMPLE]
>>
>>Consider $f(x, y, z) = \overline{x}\overline{y}\overline{z} + \overline{x}yz + xyz$.
>>
>>The [product terms](./Boolean%20Expressions.md) $\overline{x}\overline{y}\overline{z}$, $\overline{x}yz$ and $xyz$ are obviously [implicants](#Implicants) of $f$. The [product term](./Boolean%20Expressions.md) $yz$ is also an [implicant](#Implicants) of $f$.
>>
>
>
>>[!THEOREM] Theorem: Implicant Tests
>>
>>A [product term](./Boolean%20Expressions.md) $P$ is an [implicant](./Implicants.md) of a [Boolean function](./Boolean%20Functions.md) $f(x_1, \dotsc, x_n)$:
>>- if and only if $P \land F = P$;
>>- if and only if $P \land \overline{F} = 0$.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

>[!DEFINITION] Definition: Prime Implicant
>
>A **prime implicant** is an [implicant](#Implicants) such that removing any [literal](./Boolean%20Expressions.md) from it no longer results in an [implicant](#Implicants).
>
>>[!EXAMPLE]
>>
>>Consider $f(x, y, z) = \overline{x}\overline{y}\overline{z} + \overline{x}\overline{y}z + x\overline{y}z$.
>>
>>We see that $\overline{x}\overline{y}\overline{z}$ is an [implicant](#Implicants). If we remove $\overline{z}$, we obtain $\overline{x}\overline{y}$, which is also an [implicant](#Implicants). Therefore, $\overline{x}\overline{y}\overline{z}$ is *not* a [prime implicant](#Implicants).
>>
>>If we try to remove either $\overline{x}$ or $\overline{y}$ from $\overline{x}\overline{y}$, we get something which is no longer an [implicant](#Implicants). Therefore, $\overline{x}\overline{y}$ *is* a [prime implicant](#Implicants).
>>
>

>[!DEFINITION] Definition: Covering
>
>We say that an [implicant](#Implicants) $P$ **covers** a [minterm](./Boolean%20Expressions.md) $m$ if every [literal](./Boolean%20Expressions.md) in $P$ is also present in $m$.
>
>>[!EXAMPLE]
>>
>>Consider $f(x, y, z) = \overline{x} \overline{y}z + \overline{x}yz + xyz$. The [implicant](#Implicants) $yz$ [covers](#Implicants) both $\overline{x}yz$ and $xyz$. The [implicant](#Implicants) $\overline{x} \overline{y} z \overline{x}$ [covers](#Implicants) only $\overline{x} \overline{y}z$.
>>
>
>>[!THEOREM] Theorem: Covering Test
>>
>>An [implicant](#Implicants) $P$ [covers](#Implicants) a [minterm](./Boolean%20Expressions.md) $m$ if and only if $P \land m = m$.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>


>[!DEFINITION] Definition: Essential Prime Implicant
>
>Suppose that $f$ is given by a [disjunctive normal form](./Boolean%20Expressions.md).
>
>A [prime implicant](#Implicants) $P$ of a [disjunctive normal form](./Boolean%20Expressions.md) is **essential** if there exists a [minterm](./Boolean%20Expressions.md) $m$ in this [DNF](./Boolean%20Expressions.md) such that $P$ is the only [prime implicant](#Implicants) which [covers](#Implicants) $m$.
>
>>[!EXAMPLE]
>>
>>Consider the following $f$:
>>
>>$$
>>f(x,y,z,w) = \overline{x}\overline{y}\overline{z}\overline{w} + \overline{x}\overline{y}z\overline{w} + \overline{x}y\overline{z}w + \overline{x}yzw + x\overline{y}\overline{z}w + x\overline{y}z\overline{w} + xy\overline{z}w + xyzw
>>$$
>>
>>The [prime implicants](#Implicants) are $\overline{x}yw$, $y\overline{z}w$, $yzw$, $xyw$ and $\overline{y}\overline{w}$. Of these, $\overline{y}\overline{w}$ is [essential](#Implicants), since $\overline{x}\overline{y}\overline{z}\overline{w}$, $\overline{x}\overline{y}z\overline{w} + \overline{x}y\overline{z}w$, $x\overline{y}\overline{y}\overline{z}$ and $x\overline{y}z\overline{w}$ are not [covered](#Implicants) by any other [prime implicants](#Implicants).
>>
>

>[!ALGORITHM] Algorithm: Implicants from Karnaugh Maps
>
>We are given a [Karnaugh map](./Karnaugh%20Maps.md) for a [Boolean function](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}$ and want to find the [essential prime implicants](#Implicants) of $f$.
>
>1. Group the cells according to the following rules:
>    - Each group must contain only $1$s.
>    - The total number of cells in a group must be a power of $2$.
>    - The shape of a group must be rectangular. For the purposes of this, the top and bottom row are considered adjacent and so are the left-most and right-most column. 
>2. Each group constructed in the above way corresponds to a single [implicant](#Implicants) of $f$. This [implicant](#Implicants) is obtained as follows:
>    - If a [variable](./Boolean%20Expressions.md) remains a constant $1$ at all cells in the group, then include it in the [implicant](#Implicants).
>    - If a [variable](./Boolean%20Expressions.md) remains a constant $0$ at all cells in the group, then include its [negation](./Negation.md) in the [implicant](#Implicants).
>    - If a [variable](./Boolean%20Expressions.md) is a $1$ at some cells in the group and a $0$ at others, then ignore it.
>3. Do this until all possible groups have been examined to obtain all [implicants](#Implicants) of $f$.
>    - If we are specifically looking for [prime implicants](#Implicants), then we can speed up the process by first looking at the largest possible groups.
>
>>[!TIP] Tip: Prime Implicants
>>
>>If it is not possible to combine a group with an adjacent group with the same number of cells and still obtain a valid group, then this group corresponds to a [prime implicant](#Implicants).
>>
>
>>[!TIP] Tip: Essential Prime Implicants
>>
>>If a cell is contained in only a single group and this group corresponds to a [prime implicant](#Implicants), then this group corresponds to an [essential prime implicant](#Implicants).
>>
>>
>
>>[!EXAMPLE]-
>>
>>Consider the [function](./Boolean%20Functions.md) $f(x,y,z,w)$ with the following [Karnaugh Maps](./Karnaugh%20Maps.md):
>>
>>![Implicants from Karnaugh Map Example](./res/Implicants%20from%20Karnaugh%20Map%20Example.svg)
>>
>>Here are some possible groups:
>>
>>![Karnaugh Map Example Groups](./res/Karnaugh%20Map%20Example%20Groups.svg)
>>
>>The blue group can be formed thanks to the rule adjacency rule. In this group, $y$, $z$ and $w$ are always zero, so this group corresponds to the [implicant](#Implicants) $\overline{y}\overline{z}\overline{w}$. However, this is not a [prime implicant](#Implicants) because we can merge the four corners into a single group.
>>
>>The red group corresponds to the [implicant](#Implicants) $xyw$ because $x$, $y$ and $w$ are always $1$ within the group. However, this is not a [prime implicant](#Implicants) because we can combine this group with a group obtained by the cell above and the cell below to obtain a new valid group.
>>
>>The green group corresponds to the [implicant](#Implicants) $z\overline{w}$ because $z$ is always $1$ within the group and $\overline{w}$ is always $0$ within the group. Furthermore, this is a [prime implicant](#Implicants) because the group cannot be merged into a new group with any other group of the same size. Moreover, this is an [essential prime implicant](#Implicants) because it is impossible to construct another group which corresponds to a [prime implicant](#Implicants) and also contains the cell at the last row and second column.
>>
>>>[!NOTE]
>>>
>>>These are not *all* of $f$'s [implicants](#Implicants), since these are just three possible groups.
>>>
>>
>

