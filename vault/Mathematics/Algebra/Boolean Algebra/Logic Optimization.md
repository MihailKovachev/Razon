---
tags:
    - boolean-algebra
    - algebra
    - mathematics
---

# Logic Optimization

>[!DEFINITION] Definition: Complete Cover
>
>Let $f: \{0,1\}^n \to \{0, 1\}$ be a [Boolean function](./Boolean%20Functions.md).
>
>A **complete cover** of $f$ **by implicants** is a [set](../../Set%20Theory/Sets.md) of [implicants](./Implicants.md) $\{P_1, \dotsc, P_m\}$ of $f$ whose [disjunction](./Disjunction.md) [computes](./Boolean%20Expressions.md) $f$:
>
>$$
>f = \sum_{k = 1}^m P_k
>$$
>
>A **complete cover** of $f$ **by implicates**  is a [set](../../Set%20Theory/Sets.md) of [implicates](./Implicates.md) $\{C_1, \dotsc, C_l\}$ of $f$ whose [conjunction](./Conjunction.md) [computes](./Boolean%20Expressions.md) $f$:
>
>$$
>f = \prod_{k = 1}^l C_k
>$$
>
>A **complete cover** of $f$ is either a [complete cover by implicants](./Logic%20Optimization.md) or a [complete cover by implicates](./Logic%20Optimization.md).
>
>>[!DEFINITION] Definition: Minimality
>>
>>A [complete cover by implicants](./Logic%20Optimization.md) is **minimal** if it satisfies the following conditions:
>>- (I) It has the minimum number of [implicants](./Implicants.md) among all [complete covers by implicants](./Logic%20Optimization.md).
>>- (II) It has the minimum total number of [literals](./Boolean%20Expressions.md) among all [complete covers by implicants](./Logic%20Optimization.md) which satisfy (I).
>>
>>A [complete cover by implicates](./Logic%20Optimization.md) is **minimal** if it satisfies the following conditions:
>>- (I) It has the minimum number of [implicates](./Implicates.md) among all [complete covers by implicates](./Logic%20Optimization.md).
>>- (II) It has the minimum total number of [literals](./Boolean%20Expressions.md) among all [complete covers by implicates](./Logic%20Optimization.md) which satisfy (I).
>>
>

In general, [minimal complete covers by implicants](./Logic%20Optimization.md) and [minimal complete covers by implicates](./Logic%20Optimization.md) are *not* unique. Moreover, the number of terms [literals](./Boolean%20Expressions.md) can be different between a [minimal complete cover by implicants](./Logic%20Optimization.md) and a [minimal complete cover by implicates](./Logic%20Optimization.md).

>[!THEOREM] Theorem: Quines Theorem
>
>Let $f: \{0,1\}^n \to \{0,1\}$ be a [Boolean function](./Boolean%20Functions.md).
>
>If $\sum_{k = 1}^p P_k$ is a [minimal complete cover by implicants](./Logic%20Optimization.md) for $f$, then all of $P_k$ are [prime implicants](./Implicants.md).
>
>If $\prod_{k = 1}^c C_k$ is a [minimal complete cover by implicates](./Logic%20Optimization.md) for $f$, then all of $C_k$ are [prime implicates](./Implicants.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!DEFINITION] Definition: Minimal Boolean Expression
>
>A **minimal Boolean expression** for a [Boolean function](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0, 1\}$ is a [minimal complete cover by implicants](./Logic%20Optimization.md) or [minimal complete covers by implicates](./Logic%20Optimization.md) which satisfies the following conditions:
>- (I) It has the minimum number of terms among all [minimal complete covers by implicants](./Logic%20Optimization.md) and all [minimal complete covers by implicate](./Logic%20Optimization.md).
>- (II) It has the minimum total number of [literals](./Boolean%20Expressions.md) among all [Boolean expressions](./Boolean%20Expressions.md) for $f$ which satisfy (I). 
>

Given a [Boolean function](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0, 1\}$, **logic optimization** is the process of finding a [minimal complete cover by implicants](./Implicants.md) or [minimal complete cover by implicates](./Implicates.md) for $f$.

>[!ALGORITHM] Algorithm: Quine–McCluskey Minimization (DNF)
>
>We are given a [Boolean function](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}^n$ and want to find a [minimal complete cover by implicants](./Implicants.md) for it.
>
>1. Find a [CDNF](./Boolean%20Functions.md#Canonical%20Disjunctive%20Normal%20Form) for $f$:
>
>    $$f = \sum_{k = 1}^p P_k$$
>
>    - If you already have any [DNF](./Boolean%20Expressions.md) you can just [expand](./Boolean%20Functions.md#Canonical%20Disjunctive%20Normal%20Form) it to a [CDNF](./Boolean%20Functions.md#Canonical%20Disjunctive%20Normal%20Form).
>
>2. Group the [minterms](./Boolean%20Expressions.md) $P_1, \dotsc, P_p$ based on the [Hamming weight](TODO) of their [binary representation](./Boolean%20Expressions.md), i.e. the group $G_k$ contains the [minterms](./Boolean%20Expressions.md) whose [binary representations](./Boolean%20Expressions.md) contain exactly $i$ ones.
>
>3. For each pair of consecutive groups $G_k$ and $G_{k+1}$, compare each [product term](./Boolean%20Expressions.md) $t_i \in G_k$ with each [product term](./Boolean%20Expressions.md) $t_j' \in G_{k+1}$. If they differ in exactly one bit, create a new term $t_{\text{new}}$ by replacing this bit with a dash (`-`) and add it to a new list. Mark $t_i$ and $t_j'$ as "checked".
>
>4. Recursively repeat steps 2 and 3 until no more merges are possible.
>
>    - For newly generated terms to be mergeable, they need to have dashes in the exact same position and they must differ by exactly one bit.
>    - At the end, the [product terms](./Boolean%20Expressions.md) which are not marked as "checked" are the [prime implicants](./Implicants.md) of $f$.
>
>5. Create a table whose rows represent the [prime implicants](./Implicants.md) of $f$ and whose columns represent the [minterms](./Boolean%20Expressions.md) in the original [CDNF](./Boolean%20Functions.md#Canonical%20Disjunctive%20Normal%20Form) for $f$.
>    - If a [prime implicant](./Implicants.md) [covers](./Implicants.md) a [minterm](./Boolean%20Expressions.md), then mark the corresponding cell.
>    - If at the end a column has only one marked cell, then the row of this cell corresponds to an [essential prime implicant](./Implicants.md).
>
>6. Remove all rows which correspond to the [essential prime implicants](./Implicants.md) and all columns which are [covered](./Implicants.md) by  [essential prime implicants](./Implicants.md).
>7. Select the fewest possible remaining rows which  [cover](./Implicants.md) all remaining columns.
>8. The sum of all  [essential prime implicants](./Implicants.md) and all  [prime implicants](./Implicants.md) from step 7 is a [minimal complete cover by implicants](./Implicants.md) for $f$.
>
>>[!EXAMPLE]-
>>
>>TODO
>>
>

>[!ALGORITHM] Algorithm: Quine–McCluskey Minimization (CNF)
>
>We are given a [Boolean function](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}^n$ and want to find a [minimal complete cover by implicates](./Implicants.md) for it.
>
>1. Find a [CDNF](./Boolean%20Functions.md#Canonical%20Disjunctive%20Normal%20Form) for $f$:
>
>    $$f = \prod_{k = 1}^c C_k$$
>
>    - If you already have any [CNF](./Boolean%20Expressions.md) you can just [expand](./Boolean%20Functions.md#Canonical%20Conjunctive%20Normal%20Form) it to a [CCNF](./Boolean%20Functions.md#Canonical%20Conjnctive%20Normal%20Form).
>
>2. Group the [maxterms](./Boolean%20Expressions.md) $C_1, \dotsc, C_c$ based on the [Hamming weight](TODO) of their [binary representation](./Boolean%20Expressions.md), i.e. the group $G_k$ contains the [maxterm](./Boolean%20Expressions.md) whose [binary representations](./Boolean%20Expressions.md) contain exactly $i$ ones.
>
>3. For each pair of consecutive groups $G_k$ and $G_{k+1}$, compare each [clause](./Boolean%20Expressions.md) $t_i \in G_k$ with each [clause](./Boolean%20Expressions.md) $t_j' \in G_{k+1}$. If they differ in exactly one bit, create a new term $t_{\text{new}}$ by replacing this bit with a dash (`-`) and add it to a new list. Mark $t_i$ and $t_j'$ as "checked".
>
>4. Recursively repeat steps 2 and 3 until no more merges are possible.
>    - For newly generated terms to be mergeable, they need to have dashes in the exact same position and they must differ by exactly one bit.
>    - At the end, the [clauses](./Boolean%20Expressions.md) which are not marked as "checked" are the [prime implicates](./Implicates.md) of $f$.
>
>5. Create a table whose rows represent the [prime implicates](./Implicates.md) of $f$ and whose columns represent the [maxterms](./Boolean%20Expressions.md) in the original [CCNF](./Boolean%20Functions.md#Canonical%20Disjunctive%20Normal%20Form) for $f$.
>
>    - If a [prime implicate](./Implicates.md) [covers](./Implicates.md) a [maxterm](./Boolean%20Expressions.md), then mark the corresponding cell.
>    - If at the end a column has only one marked cell, then the row of this cell corresponds to an [essential prime implicate](./Implicates.md).
>
>6. Remove all rows which correspond to the [essential prime implicates](./Implicants.md) and all columns which are [covered](./Implicates.md) by  [essential prime implicates](./Implicates.md).
>7. Select the fewest possible remaining rows which [cover](./Implicates.md) all remaining columns.
>8. The sum of all [essential prime implicates](./Implicants.md) and all [prime implicates](./Implicates.md) from step 7 is a [minimal complete cover by implicates](./Implicates.md) for $f$.
>
>>[!EXAMPLE]-
>>
>>TODO
>>
>