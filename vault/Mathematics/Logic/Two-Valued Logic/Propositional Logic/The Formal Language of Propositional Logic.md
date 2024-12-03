>[!DEFINITION] Definition: The Formal Language of Propositional Logic
>
>The **formal language of propositional logic** is the [formal language](../../Formal%20Languages/Formal%20Language.md) $\mathcal{L}_\text{PL}$ whose [countable](../../../Set%20Theory/Cardinality/Countable%20Set.md) [alphabet](../../Formal%20Languages/Alphabets%20and%20Symbols.md) $\mathcal{A}_\text{PL}$ and [syntax](../../Formal%20Languages/Syntax.md) $\mathcal{S}_\text{PL}$ are defined as follows.
>
>The alphabet $\mathcal{A}_\text{PL}$ contains:
>- the *parentheses* symbols "$($" and "$)$";
>- the *sentential connective* symbols "$\neg$", "$\land$", "$\lor$", "$\rightarrow$", "$\leftrightarrow$";
>- *atomic formula* symbols $A_1,A_2,\ldots$
>
>The syntax $\mathcal{S}_\text{PL}$ is comprised of the following rules:
>- Every atomic formula is a [well-formed formula](../../Formal%20Languages/Well-Formed%20Formula.md).
>- If $P$ is a wff, then $(P)$ is also a wff.
>- Any [negation](Negation.md) of a wff is also a wff.
>- Any [conjunction](Conjunction.md) of two wffs ia also a wff.
>- Any [disjunction](Disjunction.md) of two wffs is also a wff.
>- Any [conditional](Conditional.md) of two wffs is also a wff.
>- Any [biconditional](Biconditional.md) of two wffs is also a wff.
>- All other [expressions](../../Formal%20Languages/Expression.md) are *not* wffs.
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