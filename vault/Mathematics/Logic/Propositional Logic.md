---
title: Propositional Logic
tags:
    - two-valued-logic
    - formal-logic
    - mathematics
---

# Propositional Logic

>[!DEFINITION] Definition: Propositional Logic
>
>**Propositional logic** / **Sentential calculus** / **Sentential logic** / **Statement logic** / **Zeroth-order logic** is the study of [zeroth-order formal languages](Propositional%20Logic.md).
>
>

>[!DEFINITION] Definition: Zeroth-Order Language
>
>A **zeroth-order language** is a [formal language](../../Formal%20Languages.md) $\mathcal{L}_0$ whose [alphabet](../../Formal%20Languages.md) $\Sigma$ consists of:
>- a [set](../../../Set%20Theory/Sets.md) of [symbols](../../Formal%20Languages.md) $S_1, S_2, \dotsc$ known as **atomic formulas** / **primitive symbols** / **atomic sentences** / **propositional variables**;
>- a [set](../../../Set%20Theory/Sets.md) of [symbols](../../Formal%20Languages.md) $\{\neg, \land, \lor, \implies, \iff\}$ known as **(logical) connectives** / **propositional connectives** / **logical operators**. These are called **negation** ($\neg$), **conjunction** / **(logical) and** ($\land$), **disjunction** / **(logical) or** ($\lor$), **implication** $(\implies)$ and **equivalence** ($\iff$).
>- a [set](../../../Set%20Theory/Sets.md) of [symbols](../../Formal%20Languages.md) $\{(, )\}$ called **parentheses**.
>
>The [words](../../Formal%20Languages.md) of $\mathcal{L}_0$ are called **well-formed formulas**.
>
>We define the **formula-building operations** for any two [well-formed formulas](Propositional%20Logic.md) $\alpha, \beta \in \mathcal{L}_0$:
>- $\mathcal{E}_{\neg}(\alpha) = (\neg \alpha)$;
>- $\mathcal{E}_{\land}(\alpha, \beta) = (\alpha \land \beta)$;
>- $\mathcal{E}_{\lor}(\alpha, \beta) = (\alpha \lor \beta)$;
>- $\mathcal{E}_{\implies}(\alpha, \beta) = \alpha \implies \beta$;
>- $\mathcal{E}_{\iff}(\alpha, \beta) = \alpha \iff \beta$;
>
>We define the [well-formed formulas](Propositional%20Logic.md) of $\mathcal{L}_0$ to be precisely:
>- All [propositional variables](Propositional%20Logic.md) $S_1, S_2, \dotsc$.
>- All [expressions](../../Formal%20Languages.md) $\varepsilon$ for which there exists a [finite sequence](../../../Analysis/Functional%20Analysis/Sequences/Sequences.md) of [expressions](../../Formal%20Languages.md) $\varepsilon_1, \dotsc, \varepsilon_n$ such that for each $i \le n$ we have at least one of the following: 
>	- $\varepsilon_i$ is a [propositional variable](Propositional%20Logic.md);
>	- $\varepsilon_i = \mathcal{E}_{\neg}(\varepsilon_j)$ for some $j \lt i$;
>	- $\varepsilon_i = \mathcal{E}_{\square}(\varepsilon_j, \varepsilon_k)$ for some $j \lt i$ and $k \lt i$, where $\square$ is one of the [logical connectives](Propositional%20Logic.md) $\land$, $\lor$, $\implies$, $\iff$.
>

## Binary Logic

Given a [zeroth-order language](Propositional%20Logic.md), we are most commonly interested in binary [truth assignments](Truth%20Assignment.md) $v: \mathcal{L}_{0} \to \{T, F\}$. We call $T$ **truth** and $F$ **falsity**. We further impose the following conditions on $v$. Given any [well-formed formulas](Propositional%20Logic.md) $\alpha, \beta$:
- *parentheses extraction*:

$$
v((\alpha)) = v(\alpha)
$$

|$(\alpha)$|$\alpha$|
|:--:|:--:|
|$T$|$T$|
|$F$|$F$|

- *truth assignment of negation*:

$$
v(\neg \alpha) = \begin{cases}T \qquad \text{if } v(\alpha) = F \\ F \qquad \text{otherwise}\end{cases}
$$

|$\alpha$|$\neg\alpha$|
|:--:|:--:|
|$T$|$F$|
|$F$|$T$|

- *truth assignment of conjunction*:

$$
v(\alpha \land \beta) = \begin{cases}T \qquad \text{if } v(\alpha) = T \text{ and } v(\beta) = T \\ F \qquad \text{otherwise}\end{cases}
$$

|$\alpha$|$\beta$|$\alpha \land \beta$|
|:--:|:--:|:--:|
|$F$|$F$|$F$|
|$T$|$F$|$F$|
|$F$|$T$|$F$|
|$T$|$T$|$T$|

- *truth assignment of disjunction*:

$$
v(\alpha \lor \beta) = \begin{cases}T \qquad \text{if } v(\alpha) = T \text{ or } v(\beta) = T \text{ or both}\\ F \qquad \text{otherwise}\end{cases}
$$

|$\alpha$|$\beta$|$\alpha \lor \beta$|
|:--:|:--:|:--:|
|$F$|$F$|$F$|
|$T$|$F$|$T$|
|$F$|$T$|$T$|
|$T$|$T$|$T$|

- *truth assignment of implication*:

$$
v(\alpha \implies \beta) = \begin{cases}F \qquad \text{if } v(\alpha) = T \text{ and } v(\beta) = F \\ T \qquad \text{otherwise}\end{cases}
$$

|$\alpha$|$\beta$|$\alpha \implies \beta$|
|:--:|:--:|:--:|
|$F$|$F$|$T$|
|$T$|$F$|$F$|
|$F$|$T$|$T$|
|$T$|$T$|$T$|

- *truth assignment of equivalence*:

$$
v(\alpha \implies \beta) = \begin{cases}T \qquad \text{if } v(\alpha) = v(\beta) \\ F \qquad \text{otherwise}\end{cases}
$$

|$\alpha$|$\beta$|$\alpha \implies \beta$|
|:--:|:--:|:--:|
|$F$|$F$|$T$|
|$T$|$F$|$F$|
|$F$|$T$|$F$|
|$T$|$T$|$T$|

>[!THEOREM] Theorem: Equivalent Statements of Implication
>
>Given any two [well-formed formulas](Propositional%20Logic.md) $A$ and $B$, we have:
>
>$$
>v(A \implies B) = v(\neg B \implies \neg A) = v(\neg A \lor B)  
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>