---
tags:
    - boolean-algebra
    - algebra
    - mathematics
---

# Boolean Functions

>[!DEFINITION] Definition: Boolean Function
>
>A **Boolean function** is a [function](../../Analysis/Functions/Functions.md) which takes a [tuple](../../Set%20Theory/Tuples.md) whose elements come from a [set](../../Set%20Theory/Sets.md) of two elements and outputs one of the elements of the same [set](../../Set%20Theory/Sets.md).
>
>>[!NOTATION]
>>
>>Most commonly, the elements of such a [set](../../Set%20Theory/Sets.md)  are denoted by $0$ and $1$. This means that [Boolean functions](./Boolean%20Functions.md) are usually written in the following way:
>>
>>$$
>>f: \{0,1\}^n \to \{0,1\}
>>$$
>>
>>Sometimes, the labels $\mathrm{F}$ and $\mathrm{T}$ may be used instead of $0$ and $1$ because [Boolean algebra](./Boolean%20Algebra.md) is used ubiquitously in [propositional logic](../../Logic/Propositional%20Logic.md).
>>
>
>>[!DEFINITION] Definition: Off-Set
>>
>>The **off-set** of $f$ is the [set](../../Set%20Theory/Sets.md) of all inputs for which $f$ outputs $0$:
>>
>>$$
>>\overline{F} \overset{\text{def}}{=} \{x \in \{0,1\}^n \mid f(x) = 0\}
>>$$
>>
>
>>[!DEFINITION] Definition: On-Set
>>
>>The **on-set** of $f$ is the [set](../../Set%20Theory/Sets.md) of all inputs for which $f$ outputs $1$:
>>
>>$$
>>F \overset{\text{def}}{=} \{x \in \{0,1\}^n \mid f(x) = 1\}
>>$$
>>
>
>>[!DEFINITION] Definition: Shannon Cofactors
>>
>>The **positive Shannon cofactor** of $f$ with respect to the $i$-th variable is the [restriction](../../Analysis/Functions/Functions.md) of $f$ to $\{(x_1, \dotsc, x_{i-1}, 1, x_{i+1}, \dotsc, x_n) \mid x_k \in \{0,1\}\}$.
>>
>>>[!NOTATION]
>>>
>>>$$
>>>f_{x_i}
>>>$$
>>>
>>
>>The **negative Shannon cofactor** of $f$ with respect to the $i$-th variable is the [restriction](../../Analysis/Functions/Functions.md) of $f$ to $\{(x_1, \dotsc, x_{i-1}, 0, x_{i+1}, \dotsc, x_n) \mid x_k \in \{0,1\}\}$.
>>
>>>[!NOTATION]
>>>
>>>$$
>>>f_{\overline{x_i}}
>>>$$
>>>
>>
>

>[!DEFINITION] Definition: Contradiction
>
>A [Boolean function](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}$ is a **contradiction** or **contradictory** when $f(x) = 0$ for all $x \in \{0, 1\}^n$.
>

>[!DEFINITION] Definition: Tautology
>
>A [Boolean function](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}$ is a **tautology** or **tautological** when $f(x) = 1$ for all $x \in \{0, 1\}^n$.
>

>[!DEFINITION] Definition: Dependence and Independence
>
>Let $f: \{0,1\}^n \to \{0,1\}$ be a [Boolean function](./Boolean%20Functions.md).
>
>We say that $f$ is:
>- **dependent** on $x_i$ if $f(x_1, \dotsc, x_i, \dotsc, x_n) \ne f(x_1, \dotsc, \neg x_i, \dotsc, x_n)$;
>- **independent** of $x_i$ if $f(x_1, \dotsc, x_i, \dotsc, x_n) = f(x_1, \dotsc, \neg x_i, \dotsc, x_n)$.
>

>[!DEFINITION] Definition: Boolean Vector Function
>
>A **Boolean vector function** is a [function](../../Analysis/Functions/Functions.md) which takes and outputs [tuples](../../Set%20Theory/Tuples.md) whose elements come from the same [set](../../Set%20Theory/Sets.md) of two elements:
>
>$$
>f: \{0,1\}^m \to \{0,1\}^n
>$$
>
>>[!TIP] Tip
>>
>>Every [Boolean vector function](./Boolean%20Functions.md) $f: \{0,1\}^m \to \{0,1\}^n$ is equivalent to $n$ [Boolean functions](./Boolean%20Functions.md) $f_1, \dotsc, f_n: \{0,1\}^m \to \{0,1\}$.
>>
>

>[!THEOREM] Theorem: Cofactor Substitution
>
>The [Shannon cofactors](./Boolean%20Functions.md) of a [Boolean function](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}$ obey the following rules:
>
>$$
>\begin{aligned}
>x_i \land f &= x_i \land f_{x_i} \\
>\overline{x_i} \land f &= \overline{x_i} \land f_{\overline{x_i}} \\
>x_i \lor f &= x_i \lor f_{\overline{x_i}} \\
>\overline{x_i} \lor f &= \overline{x_i} \lor f_{x_i}
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>We need to prove four things:
>>- (1) $x_i \land f = x_i \land f_{x_i}$.
>>- (2) $\overline{x_i} \land f = \overline{x_i} \land f_{\overline{x_i}}$.
>>- (3) $x_i \lor f = x_i \lor f_{\overline{x_i}}$.
>>- (4) $\overline{x_i} \lor f = \overline{x_i} \lor f_{x_i}$.
>>
>>**Proof of (1):**
>>
>>If $x_i = 0$, then the left-hand side is $x_i \land f = 0 \land f = 0$. Similarly, the right-hand side is $x_i \land f_{x_i} = 0 \land f_{x_i} = 0$. The left-hand side and right-hand side are therefore equal when $x_i = 0$.
>>
>>If $x_i = 1$, then the left-hand side is $x_i \land f = 1 \land f = f$. Similarly, the right-hand side is $x_i \land f_{x_i} = 1 \land f_{x_i} = f_{x_i}$. However, in this case, $f$ and $f_{x_i}$ are the same by definition. The left-hand side and right-hand side are therefore equal when $x_i = 1$.
>>
>>We have thus shown that the law holds for all possible values of $x_i$, i.e. it holds in general.
>>
>>**Proof of (2):**
>>
>>If $x_i = 0$, then the left-hand side is $\overline{x_i} \land f = 1 \land f = f$. Similarly, the right-hand side is $\overline{x_i} \land f_{\overline{x_i}} = \overline{0} \land f_{\overline{x_i}} = 1 \land f_{\overline{x_i}} = f_{\overline{x_i}}$. However, in this case, $f$ and $f_{\overline{x_i}}$ are the same by definition. The left-hand side and right-hand side are therefore equal when $x_i = 1$. The left-hand side and right-hand side are therefore equal when $x_i = 0$.
>>
>>If $x_i = 1$, then the left-hand side is $\overline{x_i} \land f = \overline{1} \land f = 0 \land f = 0$. Similarly, the right-hand side is $\overline{x_i} \land f_{\overline{x_i}} = \overline{1} \land f_{\overline{x_i}} = 0 \land f_{\overline{x_i}} = 0$. The left-hand side and right-hand side are therefore equal when $x_i = 1$.
>>
>>We have thus shown that the law holds for all possible values of $x_i$, i.e. it holds in general.
>>
>>**Proof of (3):**
>>
>>Analogous.
>>
>>**Proof of (4):**
>>
>>Analogous.
>>
>

>[!THEOREM] Boole's Expansion Theorem
>
>If $f_{x_i}$ and $f_{\overline{x_i}}$ are the [Shannon cofactors](./Boolean%20Functions.md) of a [logical connective](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0, 1\}$ with respect to the $i$-th variable, then:
>
>$$
>f = (x_i \land f_{x_i}) \lor (\overline{x_i} \land f_{\overline{x_i}}) = (x_i \lor f_{\overline{x_i}}) \land (\overline{x_i} \lor f_{x_i})
>$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (1) $f = (x_i \land f_{x_i}) \lor (\overline{x_i} \land f_{\overline{x_i}})$.
>>- (2) $f = (x_i \lor f_{\overline{x_i}}) \land (\overline{x_i} \lor f_{x_i})$.
>>
>>**Proof of (1):** *The following proof was generated by AI and has not been human-verified. As such, it may contain mistakes.*
>>
>>If $x_i = 1$:
>>- The LHS becomes $f(x_1, \dots, 1, \dots, x_n)$, which by definition is the cofactor $f_{x_i}$.
>>- The RHS becomes $(1 \land f_{x_i}) \lor (\overline{1} \land f_{\overline{x_i}})$.
>>- Since $\overline{1} = 0$, this simplifies to $(1 \land f_{x_i}) \lor (0 \land f_{\overline{x_i}})$.
>>- Using the identities $1 \land A = A$ and $0 \land B = 0$, we get $f_{x_i} \lor 0$.
>>- Using the identity $A \lor 0 = A$, the RHS simplifies to $f_{x_i}$.
>>- Thus, for $x_i=1$, LHS = RHS.
>>
>>If $x_i = 0$:
>>- The LHS becomes $f(x_1, \dots, 0, \dots, x_n)$, which by definition is the cofactor $f_{\overline{x_i}}$.
>>- The RHS becomes $(0 \land f_{x_i}) \lor (\overline{0} \land f_{\overline{x_i}})$.
>>- Since $\overline{0} = 1$, this simplifies to $(0 \land f_{x_i}) \lor (1 \land f_{\overline{x_i}})$.
>>- Using the identities $0 \land A = 0$ and $1 \land B = B$, we get $0 \lor f_{\overline{x_i}}$.
>>- Using the identity $0 \lor B = B$, the RHS simplifies to $f_{\overline{x_i}}$.
>>- Thus, for $x_i=0$, LHS = RHS.
>>
>>Since the equality holds for both possible values of $x_i$, the identity is proven true for all inputs.
>>
>>**Proof of (2):** *The following proof was generated by AI and has not been human-verified. As such, it may contain mistakes.*.
>>
>>If $x_i = 1$:
>>- The LHS is again $f(x_1, \dots, 1, \dots, x_n) = f_{x_i}$.
>>- The RHS becomes $(1 \lor f_{\overline{x_i}}) \land (\overline{1} \lor f_{x_i})$.
>>- Since $\overline{1} = 0$, this simplifies to $(1 \lor f_{\overline{x_i}}) \land (0 \lor f_{x_i})$.
>>- Using the identities $1 \lor A = 1$ and $0 \lor B = B$, we get $1 \land f_{x_i}$.
>>- Using the identity $1 \land A = A$, the RHS simplifies to $f_{x_i}$.
>>- Thus, for $x_i=1$, LHS = RHS.
>>
>>If $x_i = 0$:
>>- The LHS is again $f(x_1, \dots, 0, \dots, x_n) = f_{\overline{x_i}}$.
>>- The RHS becomes $(0 \lor f_{\overline{x_i}}) \land (\overline{0} \lor f_{x_i})$.
>>- Since $\overline{0} = 1$, this simplifies to $(0 \lor f_{\overline{x_i}}) \land (1 \lor f_{x_i})$.
>>- Using the identities $0 \lor A = A$ and $1 \lor B = 1$, we get $f_{\overline{x_i}} \land 1$.
>>- Using the identity $A \land 1 = A$, the RHS simplifies to $f_{\overline{x_i}}$.
>>- Thus, for $x_i=0$, LHS = RHS.
>>
>

>[!THEOREM] Theorem: Function Equivalence
>
>Two [Boolean functions](./Boolean%20Functions.md) $f, g: \{0,1\}^n \to \{0,1\}$ are the same if and only if the [function](./Boolean%20Functions.md) 
>
>$$
>(\neg f \lor g) \land (f \lor \neg g)
>$$
>
>is [tautological](./Boolean%20Functions.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Canonical Conjunctive Normal Form

>[!THEOREM] Theorem: Canonical Conjunctive Normal Form
>
>Every [non-tautological](./Boolean%20Functions.md) [Boolean function](./Boolean%20Functions.md) can be [expressed](./Boolean%20Expressions.md) as a [conjunctive normal form](./Boolean%20Expressions.md) of $p$ [maxterms](./Boolean%20Expressions.md), where $p$ is the [cardinality](../../Set%20Theory/Cardinality.md) of $f$'s [off-set](./Boolean%20Functions.md).
>
>>[!DEFINITION] Definition: Canonical Conjunctive Normal Form (CCNF)
>>
>>Such an expression is known as a **canonical conjunctive normal form** (**CCNF**) of $f$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!ALGORITHM] Algorithm: Finding CCNFs
>
>We are given a [Boolean function](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}$:
>
>$$f(x_1, \dotsc, x_n)$$
>
>1. Identify the [off-set](./Boolean%20Functions.md) $\overline{F}$ of $f$.
>
>2. For each $(x_1^{\ast}, \dotsc, x_n^{\ast}) \in \overline{F}$ construct the [maxterm](./Boolean%20Expressions.md) $\mathop{\operatorname{OR}}(x_1', \dotsc, x_n')$, where
>
>    - $x_k' = x_k$ if $x_k^{\ast} = 0$;
>    - $x_k' = \neg x_k$ if $x_k^{\ast} = 1$.
>
>3. The [conjunctive normal form](#Conjunctive%20Normal%20Form) of $f$ is the [conjunction](./Conjunction.md) of all the [maxterms](./Boolean%20Expressions.md) from step 2.
>
>>[!EXAMPLE]-
>>
>>The easiest way is to use the [truth table](./Truth%20Tables.md) of $f$. Suppose $f(x_1, x_2, x_3)$ has the following [truth table](./Truth%20Tables.md):
>>
>>|$x_1$|$x_2$|$x_3$|$f(x_1, x_2, x_3)$|
>>|:--:|:--:|:--:|:--:|
>>|$0$|$0$|$0$|$0$|
>>|$0$|$0$|$1$|$1$|
>>|$0$|$1$|$0$|$1$|
>>|$0$|$1$|$1$|$1$|
>>|$1$|$0$|$0$|$0$|
>>|$1$|$0$|$1$|$0$|
>>|$1$|$1$|$0$|$1$|
>>|$1$|$1$|$1$|$0$|
>>
>>The [off-set](./Boolean%20Functions.md) of $f$ is easily determined by looking at the rows which contain $0$ in the column for $f(x_1, x_2, x_3)$. In this example, these rows are $1$, $5$, $6$, and $8$.
>>
>>On row $1$ we see that $x_1$, $x_2$ and $x_3$ are all $0$. We therefore construct the [maxterm](./Boolean%20Expressions.md) $x_1 \lor x_2 \lor x_3$.
>>
>>On row $5$ we see that $x_1$ is $1$, while $x_2$ and $x_3$ are both $0$. We therefore construct the [maxterm](./Boolean%20Expressions.md) $\neg x_1 \lor x_2 \lor x_3$.
>>
>>On row $6$ we see that $x_1$ and $x_3$ are both $1$, while $x_2$ is $0$. We therefore construct the [maxterm](./Boolean%20Expressions.md) $\neg x_1 \lor x_2 \lor \neg x_3$.
>>
>>On row $6$ we see that $x_1$, $x_2$ and $x_3$ are all $1$. We therefore construct the [maxterm](./Boolean%20Expressions.md) $\neg x_1 \lor \neg x_2 \neg \lor x_3$.
>>
>>Finally, we build the [conjunction](./Conjunction.md) of all [maxterms](./Disjunction.md):
>>
>>$$
>>f(x_1, x_2, x_3) = (x_1 \lor x_2 \lor x_3)  \land (\neg x_1 \lor x_2 \lor x_3) \land (\neg x_1 \lor x_2 \lor \neg x_3) \land (\neg x_1 \lor \neg x_2 \neg \lor x_3)
>>$$
>>
>

>[!ALGORITHM] Algorithm: CCNF to DNF
>
>We are given the [CNF](#Conjunctive%20Normal%20Form) of a [Boolean function](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}$ and want to find its [DNF](./Disjunction.md#Disjunctive%20Normal%20Form):
>
>2. Apply the [distributive law](./Operator%20Laws.md) for [conjunction](./Conjunction.md) recursively, starting left to right.
>3. It may be possible to further simplify the resulting [conjunctions](./Conjunction.md) in the [DNF](./Disjunction.md#Disjunctive%20Normal%20Form).
>
>>[!EXAMPLE]-
>>
>>TODO
>>
>

>[!ALGORITHM] Algorithm: CNF to CCNF
>
>We are given a [CNF](#Conjunctive%20Normal%20Form) of a [Boolean function](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}$ and want to find a [CCNF](#Conjunctive%20Normal%20Form):
>
>$$f(x_1, \dotsc, x_n) = \prod_{i=1}^c C_i$$
>
>1. For each [clause](./Boolean%20Expressions.md) $C_i$ and each variable $x_j$:
>
>    - If $C_i$ contains $x_j$ or $\overline{x}_j$, then do nothing.
>    - If $C_i$ does *not* contain $x_j$ or $\overline{x}_j$, then replace it by the product $(C_i + x_j)(C_i + \overline{x_j})$.
>    - Recursively repeat the same process for each of the newly generated [clauses](./Boolean%20Expressions.md), until you only have [maxterms](./Boolean%20Expressions.md).
>
>2. If you have multiple identical [maxterms](./Boolean%20Expressions.md), then merge them into a single one.
>3. The result from step 2 is a [CCNF](#Conjunctive%20Normal%20Form) of $f$.
>

## Canonical Disjunctive Normal Form

>[!THEOREM] Theorem: Canonical Disjunctive Normal Form (CDNF)
>
>Every [non-contradictory](./Boolean%20Functions.md) [Boolean function](./Boolean%20Functions.md) $f: \{0, 1\}^n \to \{0,1\}$ can be expressed as a [disjunctive normal form](./Boolean%20Expressions.md) of $p$ [minterms](./Boolean%20Expressions.md), where $p$ is the [cardinality](../../Set%20Theory/Cardinality.md) of $f$'s [on-set](./Boolean%20Functions.md).
>
>>[!DEFINITION] Definition: Canonical Disjunctive Normal Form
>>
>>Such an expression is known as a **canonical disjunctive normal form** (**CDNF**) of $f$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!ALGORITHM] Algorithm: Finding CDNFs
>
>We are given a [Boolean operator](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}$:
>
>$$f(x_1, \dotsc, x_n)$$
>
>1. Identify the [on-set](./Boolean%20Functions.md) $F$ of $f$.
>
>2. For each $(x_1^{\ast}, \dotsc, x_n^{\ast}) \in F$ construct the [minterm](./Boolean%20Expressions.md) $\mathop{\operatorname{AND}}(x_1', \dotsc, x_n')$, where
>
>    - $x_k' = x_k$ if $x_k^{\ast} = 1$;
>    - $x_k' = \neg x_k$ if $x_k^{\ast} = 0$.
>
>3. The [disjunctive normal form](#Disjunctive%20Normal%20Form) of $f$ is the [disjunction](./Disjunction.md) of all the [minterms](./Boolean%20Expressions.md) from step 2.
>
>>[!EXAMPLE]-
>>
>>The easiest way is to use the [truth table](./Truth%20Tables.md) of $f$. Suppose $f(x_1, x_2, x_3)$ has the following [truth table](./Truth%20Tables.md):
>>
>>|$x_1$|$x_2$|$x_3$|$f(x_1, x_2, x_3)$|
>>|:--:|:--:|:--:|:--:|
>>|$0$|$0$|$0$|$0$|
>>|$0$|$0$|$1$|$1$|
>>|$0$|$1$|$0$|$1$|
>>|$0$|$1$|$1$|$1$|
>>|$1$|$0$|$0$|$0$|
>>|$1$|$0$|$1$|$0$|
>>|$1$|$1$|$0$|$1$|
>>|$1$|$1$|$1$|$0$|
>>
>>The [on-set](./Boolean%20Functions.md) of $f$ is easily determined by looking at the rows which contain $1$ in the column for $f(x_1, x_2, x_3)$. In this example, these rows are $2$, $3$, $4$, and $7$.
>>
>>On row $2$ we see that $x_1$ and $x_2$ are both $0$, while $x_3$ is $1$. We therefore construct the [minterm](./Boolean%20Expressions.md) $\neg x_1 \land \neg x_2 \land x_3$.
>>
>>On row $3$ we see that $x_1$ and $x_3$ are both $0$, while $x_2$ is $1$. We therefore construct the [minterm](./Boolean%20Expressions.md) $\neg x_1 \land x_2 \land \neg x_3$.
>>
>>On row $4$ we see that $x_1$ is $0$, while $x_2$ and $x_3$ are both $1$. We therefore construct the [minterm](./Boolean%20Expressions.md) $\neg x_1 \land x_2 \land x_3$.
>>
>>On row $7$, we see that $x_1$ and $x_2$ are both $1$, while $x_3$ is $0$. We therefore construct the [minterm](./Boolean%20Expressions.md) $x_1 \land x_2 \land \neg x_3$.
>>
>>Finally, we build the [disjunction](./Disjunction.md) of all [minterms](./Conjunction.md):
>>
>>$$
>>f(x_1, x_2, x_3) = (\neg x_1 \land \neg x_2 \land x_3) \lor (\neg x_1 \land x_2 \land \neg x_3) \lor (\neg x_1 \land x_2 \land x_3) \lor (x_1 \land x_2 \land \neg x_3)
>>$$
>>
>

>[!ALGORITHM] Algorithm: DNF to CNF
>
>We are given a [CCNF](#Disjunctive%20Normal%20Form) of a [Boolean function](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}$ and want to find its [CNF](./Conjunction.md#Conjunctive%20Normal%20Form):
>
>2. Apply the [distributive law](./Operator%20Laws.md) for [disjunction](./Disjunction.md) recursively, starting left to right.
>3. It may be possible to further simplify the resulting [disjunctions](./Disjunction.md) in the [CNF](./Conjunction.md#Conjunctive%20Normal%20Form).
>
>>[!EXAMPLE]-
>>
>>TODO
>>
>

>[!ALGORITHM] Algorithm: DNF to CDNF
>
>We are given are given a [DNF](#Disjunctive%20Normal%20Form) of a [Boolean function](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}$ and want to find a [CDNF](#Disjunctive%20Normal%20Form):
>
>$$f(x_1, \dotsc, x_n) = \sum_{i=1}^p P_i$$
>
>1. For each [product term](./Boolean%20Expressions.md) $P_i$ and each variable $x_j$:
>
>    - If $P_i$ contains $x_j$ or $\overline{x}_j$, then do nothing.
>    - If $P_i$ does *not* contain $x_j$ or $\overline{x}_j$, then replace it with $P_i x_j + P_i \overline{x_j}$.
>    - Recursively repeat the same process for the newly generated [product terms](./Boolean%20Expressions.md) until you have only [minterms](./Boolean%20Expressions.md).
>
>2. If you have multiple identical [minterms](./Boolean%20Expressions.md), then merge them into a single one.
>3. The result from step 2 is a [CDNF](#Disjunctive%20Normal%20Form) of $f$.
>
>>[!EXAMPLE]-
>>
>>Consider $f(A, B, C) = A + \overline{B}C$.
>>
>>The first is $A$. We need to perform two expansions on it:
>>
>>$$
>>\begin{aligned}
>>A &= A(B + \overline{B}) = AB + A \overline{B} \\
>>A &= A(C + \overline{C}) =  AC + A \overline{C}
>>\end{aligned}
>>$$
>>
>>We also need to expand the each of the newly generated terms once:
>>
>>$$
>>\begin{aligned}
>>AB &= AB(C + \overline{C}) = ABC + AB\overline{C} \\
>>A\overline{B} &= A\overline{B}(C + \overline{C}) = A\overline{B}C + A\overline{B}\overline{C} \\
>>AC &= AC(B + \overline{B}) = ACB + AC\overline{B} \\
>>A\overline{C} &= A\overline{C}(B + \overline{B}) = A\overline{C}B + A\overline{C}\overline{B}
>>\end{aligned}
>>$$
>>
>>We thus generated the following [minterms](./Boolean%20Expressions.md): $ABC$, $AB\overline{C}$, $A\overline{B}C$, $A\overline{B}\overline{C}$.
>>
>>Now, we do the same for the other original [product term](./Boolean%20Expressions.md) $\overline{B}C$. We only need to expand it once:
>>
>>$$
>>\overline{B}C = \overline{B}C(A + \overline{A}) = \overline{B}CA + \overline{B}C\overline{A} 
>>$$
>>
>>We thus generated the following [minterms](./Boolean%20Expressions.md): $\overline{B}CA$ and $\overline{B}C\overline{A}$.
>>
>>To obtain a [CDNF](#Disjunctive%20Normal%20Form) of $f$, we sum all generated  [minterms](./Boolean%20Expressions.md):
>>
>>$$
>>f(A, B, C) = ABC + AB\overline{C} + A\overline{B}C + A\overline{B}\overline{C} + \overline{B}CA + \overline{B}C\overline{A}
>>$$
>>
>>We see that $A\overline{B}C$ and $\overline{B}CA$ are the same, so we just leave $A\overline{B}C$:
>>
>>$$
>>f(A, B, C) = ABC + AB\overline{C} + A\overline{B}C + A\overline{B}\overline{C} + \overline{B}C\overline{A}
>>$$
>> 
>