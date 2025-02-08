---
title: Propositional Logic
tags:
    - two-valued-logic
    - formal-logic
    - mathematics
---

>[!DEFINITION] Definition: The Formal Language of Propositional Logic
>
>The **formal language of propositional logic** is the [formal language](../../Formal%20Languages.md) $\mathcal{L}_\text{PL}$ whose [countable](../../../Set%20Theory/Cardinality/Countable%20Sets.md) [alphabet](../../Formal%20Languages.md) $\mathcal{A}_\text{PL}$ and [syntax](../../Formal%20Languages.md) $\mathcal{S}_\text{PL}$ are defined as follows.
>
>The alphabet $\mathcal{A}_\text{PL}$ contains:
>- the *parentheses* symbols "$($" and "$)$";
>- the *sentential connective* symbols "$\neg$", "$\land$", "$\lor$", "$\rightarrow$", "$\leftrightarrow$";
>- *atomic formula* symbols $A_1,A_2,\ldots$
>
>The syntax $\mathcal{S}_\text{PL}$ is comprised of the following rules:
>- Every atomic formula is a [well-formed formula](../../Formal%20Languages.md).
>- If $P$ is a wff, then $(P)$ is also a wff.
>- Any [negation](Propositional%20Connectives.md) of a wff is also a wff.
>- Any [conjunction](Propositional%20Connectives.md) of two wffs ia also a wff.
>- Any [disjunction](Propositional%20Connectives.md) of two wffs is also a wff.
>- Any [conditional](Propositional%20Connectives.md) of two wffs is also a wff.
>- Any [biconditional](Propositional%20Connectives.md) of two wffs is also a wff.
>- All other [expressions](../../Formal%20Languages.md) are *not* wffs.
>
>>[!INTUITION]-
>>
>>Each well-formed formula $P$ can be thought of as a translation of an English [proposition](Proposition.md) into the language $\mathcal{L}_\text{PL}$. Atomic formulas then represent the most basic and fundamental propositions we have chosen to examine.
>>
>
>>[!NOTE]
>>
>>The language $\mathcal{L}_\text{PL}$ is also known as the **zeroth order language**.
>>
>