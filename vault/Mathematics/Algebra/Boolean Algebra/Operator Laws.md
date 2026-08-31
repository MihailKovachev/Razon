---
tags:
    - boolean-algebra
    - algebra
    - mathematics 
---

# Operator Laws

>[!NOTATION] Notation: Precedence
>
>Typically, the precedence of logical connectives decreases in the following order: negation, conjunction, disjunction. 
>
>>[!EXAMPLE]
>>
>>$$
>>\neg x \land y = (\neg x) \land y \qquad \neg x \lor y = (\neg x) \lor y
>>$$
>>
>

>[!THEOREM]+ Theorem: Associativity Laws
>
>[Conjunction](../../../index.md#Fundamental%20Connectives) and [disjunction](../../../index.md#Fundamental%20Connectives) are assosiative:
>
>$$
>\begin{aligned}
>(A \land B) \land C &= A \land (B \land C) \\
>(A \lor B) \lor C &= A \lor (B \lor C)
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (1) $(A \land B) \land C = A \land (B \land C)$.
>>- (2) $(A \lor B) \lor C = A \lor (B \lor C)$.
>>
>>**Proof of (1):**
>>
>>$$
>>(A \land B) \land C = 1 \iff (A \land B) = 1 \text{ and } C = 1 \iff A = 1 \text{ and } B = 1 \text{ and } C = 1
>>$$
>>
>>$$
>>A \land (B \land C) = 1 \iff A = 1 \text{ and } (B \land C) = 1 \iff A = 1 \text{ and } B = 1 \text{ and } C = 1
>>$$
>>
>>**Proof of (2):**
>>
>>$$
>>(A \lor B) \lor C = 0 \iff (A \lor B) = 0 \text{ and } C = 0 \iff A = 0 \text{ and } B = 0 \text{ and } C = 0
>>$$
>>
>>$$
>>A \lor (B \lor C) \iff A = 0 \text{ and } (B \lor C) = 0 \iff A = 0 \text{ and } B = 0 \text{ and } C = 0
>>$$
>>
>

>[!THEOREM]+ Theorem: Distributivity Laws
>
>[Conjunction](../../../index.md#Fundamental%20Connectives), [disjunction](../../../index.md#Fundamental%20Connectives) and [exclusive disjunction](./Exclusive%20Disjunction.md) obey the following distributive laws:
>
>$$
>\begin{aligned}
>x \land (y \lor z) &= (x \land y) \lor (x \land z) \\
>x \lor (y \land z) &= (x \lor y) \land (x \lor z) \\
>x \land (y \oplus z) &= (x \land y) \oplus (x \land z)
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (1) $x \land (y \lor z) = (x \land y) \lor (x \land z)$.
>>- (2) $x \lor (y \land z) = (x \lor y) \land (x \lor z)$.
>>
>>**Proof of (1):**
>>
>>If $x = 1$, then the left-hand side is $x \land (y \lor z) = 1 \land (y \lor z) = y \lor z$. Furthermore, the right-hand side is $(x \land y) \lor (x \land z) = (1 \land y) \lor (1 \land z) = y \lor z$. The left-hand side and right-hand side are therefore equal when $x = 1$.
>>
>>If $x = 0$, then the left-hand side is $x \land (y \lor z) = 0 \land (y \lor z) = 0$. Furthermore, the right-hand side is $(x \land y) \lor (x \land z) = (0 \land y) \lor (0 \land z) = 0 \lor 0 = 0$. The left-hand side and right-hand side are therefore equal when $x = 0$.
>>
>>We have thus shown that the law holds for all possible values of $x$, i.e. it holds in general.
>>
>>**Proof of (2):**
>>
>>If $x = 1$, then the left-hand is $x \lor (y \land z) = 1 \lor (y \land z) = 1$. Furthermore, the right-hand side is $(x \lor y) \land (x \lor z) = (1 \lor y) \land (1 \lor z) = 1 \lor 1 = 1$. The left-hand side and right-hand side are therefore equal when $x = 1$.
>>
>>If $x = 0$, then the left-hand is $x \lor (y \land z) = y \land z$. Furthermore, the right-hand side is $(x \lor y) \land (x \lor z) = (0 \lor y) \land (0 \lor z) = y \land z$. The left-hand side and right-hand side are therefore equal when $x = 0$.
>>
>>We have thus shown that the law holds for all possible values of $x$, i.e. it holds in general.
>>
>

>[!THEOREM]+ Theorem: De Morgan's Laws
>
>[Negation](../../../index.md#Fundamental%20Connectives), [conjunction](../../../index.md#Fundamental%20Connectives) and [disjunction](../../../index.md#Fundamental%20Connectives) are related by the following laws:
>
>$$
>\begin{aligned}
>\overline{x \land y} &= \overline{x} \lor \overline{y} \\
>\overline{x \lor y} &= \overline{x} \land \overline{y}
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (1) $\overline{x \land y} = \overline{x} \lor \overline{y}$.
>>- (2) $\overline{x \lor y} = \overline{x} \land \overline{y}$.
>>
>>**Proof of (1):**
>>
>>If $x = 1$, then the left-hand side is $\overline{x \land y} = \overline{1 \land y} = \overline{y}$. Furthermore, the right-hand side is $\overline{x} \lor \overline{y} = \overline{1} \lor \overline{y} = 0 \lor \overline{y} = \overline{y}$.  The left-hand side and right-hand side are therefore equal when $x = 1$.
>>
>>If $x = 0$, then the left-hand side is $\overline{x \land y} = \overline{0 \land y} = \overline{0} = 1$. Furthermore, the right-hand side is $\overline{x} \lor \overline{y} = \overline{0} \lor \overline{y} = 1 \lor \overline{y} = 1$.  The left-hand side and right-hand side are therefore equal when $x = 0$.
>>
>>We have thus shown that the law holds for all possible values of $x$, i.e. it holds in general.
>>
>>**Proof of (2):**
>>
>>If $x = 1$, then the left-hand side is $\overline{x \lor y} = \overline{1 \lor y} = \overline{1} = 0$. Furthermore, the right-hand side is $\overline{x} \land \overline{y} = \overline{1} \land \overline{y} = 0 \land \overline{y} = 0$. The left-hand side and right-hand side are therefore equal when $x = 1$.
>>
>>If $x = 0$, then the left-hand side is $\overline{x \lor y} = \overline{0 \lor y} = \overline{y}$. Furthermore, the right-hand side is $\overline{x} \land \overline{y} = \overline{0} \land \overline{y} = 1 \land \overline{y} = \overline{y}$. The left-hand side and right-hand side are therefore equal when $x = 0$.
>>
>>We have thus shown that the law holds for all possible values of $x$, i.e. it holds in general.
>>
>

>[!THEOREM]+ Theorem: Absorption Laws
>
>[Conjunction](../../../index.md#Fundamental%20Connectives) and [disjunction](../../../index.md#Fundamental%20Connectives) have the following properties:
>
>$$
>\begin{aligned}
>A \lor (A \land B) &= A \\
>A \land (A \lor B) &= A
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (1) $A \lor (A \land B) = A$.
>>- (2) $A \land (A \lor B) = A$.
>>
>>**Proof of (1):**
>>
>>If $A = 1$, then the left-hand side is $A \lor (A \land B) = 1 \lor (1 \land B) = 1$. Furthermore, the right-hand side is just $1$. The left-hand side and right-hand side are therefore equal when $A = 1$.
>>
>>If $A = 0$, then the left-hand side is $A \lor (A \land B) = 0 \lor (0 \land B) = 0 \lor 0 = 0$. Furthermore, the right-hand side is just $0$. The left-hand side and right-hand side are therefore equal when $A = 0$.
>>
>>We have thus shown that the law holds for all possible values of $A$, i.e. it holds in general.
>>
>>**Proof of (2):**
>>
>>If $A = 1$, then the left-hand side is $A \land (A \lor B) = 1 \land (1 \lor B) = 1 \land 1 = 1$. Furthermore, the right-hand side is just $1$. The left-hand side and right-hand side are therefore equal when $A = 1$.
>>
>>If $A = 0$, then the left-hand side is $A \land (A \lor B) = 0 \land (0 \lor B) = 0 \land B = 0$. Furthermore, the right-hand side is just $0$. The left-hand side and right-hand side are therefore equal when $A = 0$.
>>
>>We have thus shown that the law holds for all possible values of $A$, i.e. it holds in general.
>>
>

>[!THEOREM]+ Theorem: Resolution Laws
>
>[Negation](../../../index.md#Fundamental%20Connectives), [conjunction](../../../index.md#Fundamental%20Connectives) and [disjunction](../../../index.md#Fundamental%20Connectives) have the following properties:
>
>$$
>\begin{aligned}
>(X \land A) \lor (\overline{X} \land B) &= (X \land A) \lor (\overline{X} \land B) \lor (A \land B) \\
>(X \lor A) \land (\overline{X} \lor B) &= (X \lor A) \land (\overline{X} \lor B) \land (A \lor B)
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (1) $(X \land A) \lor (\overline{X} \land B) = (X \land A) \lor (\overline{X} \land B) \lor (A \land B)$.
>>- (2) $(X \lor A) \land (\overline{X} \lor B) = (X \lor A) \land (\overline{X} \lor B) \land (A \lor B)$.
>>
>>**Proof of (1):**
>>
>>If $X = 1$, then the left-hand side is $(X \land A) \lor (\overline{X} \land B) = (1 \land A) \lor (\overline{1} \land B) = A \lor (0 \land B) = A \lor 0 = A$. Furthermore, the right-hand side is $(X \land A) \lor (\overline{X} \land B) \lor (A \land B) = (1 \land A) \lor (\overline{1} \land B) \lor (A \land B) = A \lor (0 \land B) \lor (A \land B) = A \lor 0 \lor (A \land B) = A \lor (A \land B)$. By the [absorption law](../../../index.md#Logic%20Laws), $A \lor (A \land B) = A$. The left-hand side and right-hand side are therefore equal when $X = 1$.
>>
>>If $X = 0$, then the left-hand side is $(X \land A) \lor (\overline{X} \land B) = (0 \land A) \lor (\overline{0} \land B) = 0 \lor (1 \land B) = 0 \lor B = B$. Furthermore, the right-hand side is $(X \land A) \lor (\overline{X} \land B) \lor (A \land B) = (0 \land A) \lor (\overline{0} \land B) \lor (A \land B) = 0 \lor (1 \land B) \lor (A \land B) = 0 \lor B \lor (A \land B) = B \lor (A \land B)$. By the [absorption law](../../../index.md#Logic%20Laws), $B \lor (A \land B) = B$. The left-hand side and right-hand side are therefore equal when $X = 0$.
>>
>>We have thus shown that the law holds for all possible values of $A$, i.e. it holds in general.
>>
>>**Proof of (2):**
>>
>>If $X = 1$, then the left-hand side is $(X \lor A) \land (\overline{X} \lor B) = (1 \lor A) \land (\overline{1} \lor B) = 1 \land (0 \lor B) = 1 \land B = B$. Furthermore, the right-hand side is $(X \lor A) \land (\overline{X} \lor B) \land (A \lor B) = (1 \lor A) \land (\overline{1} \lor B) \land (A \lor B) = 1 \land (0 \lor B) \land (A \lor B) = 1 \land B \land (A \lor B) = B \land (A \lor B)$. By the [absorption law](../../../index.md#Logic%20Laws), $B \land (A \lor B) = B$. The left-hand side and right-hand side are therefore equal when $1 = 0$.
>>
>>If $X = 0$, then the left-hand side is $(X \lor A) \land (\overline{X} \lor B) = (0 \lor A) \land (\overline{0} \lor B) = A \land (1 \lor B) = A \land 1 = A$. Furthermore, the right-hand side is $(X \lor A) \land (\overline{X} \lor B) \land (A \lor B) = (0 \lor A) \land (\overline{0} \lor B) \land (A \lor B) = A \land (1 \lor B) \land (A \lor B) = A \land 1 \land (A \lor B) = A \land (A \lor B)$. By the [absorption law](../../../index.md#Logic%20Laws), $A \land (A \lor B) = A$. The left-hand side and right-hand side are therefore equal when $1 = 0$.
>>
>>We have thus shown that the law holds for all possible values of $A$, i.e. it holds in general.
>>
>

>[!THEOREM]+ Theorem: Boolean Expansion of Negation
>
>If $f_{x_i}$ and $f_{\overline{x_i}}$ are the [Shannon cofactors](../../../index.md) of a [logical connective](../../../index.md) $f: \{0,1\}^n \to \{0, 1\}$ with respect to the $i$-th variable, then the [negation](../../../index.md) of $f$ can be express in the following ways:
>
>$$
>\overline{f} = (\overline{x_i} \land \overline{f_{\overline{x_i}}}) \lor (x_i \land \overline{f_{x_i}}) = (\overline{x_i} \lor \overline{f_{x_i}}) \land (x_i \lor \overline{f_{\overline{x_i}}})
>$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (1) $\overline{f} = (\overline{x_i} \land \overline{f_{\overline{x_i}}}) \lor (x_i \land \overline{f_{x_i}})$.
>>- (2) $\overline{f} = (\overline{x_i} \lor \overline{f_{x_i}}) \land (x_i \lor \overline{f_{\overline{x_i}}})$.
>>
>>**Proof of (1):** *The following proof was generated by AI and has not been human-verified. As such, it may contain mistakes.*
>>
>>This identity is derived by applying the Shannon expansion theorem directly to the function $\overline{f}$. The Shannon expansion of any function $g$ with respect to a variable $x_i$ is:
>>
>>$$
>>g = (\overline{x_i} \land g_{\overline{x_i}}) \lor (x_i \land g_{x_i})
>>$$
>>
>>Let's set $g = \overline{f}$. This gives us:
>>
>>$$
>>\overline{f} = (\overline{x_i} \land (\overline{f})_{\overline{x_i}}) \lor (x_i \land (\overline{f})_{x_i})
>>$$
>>
>>Now, we evaluate the cofactors of $\overline{f}$. The cofactor $(\overline{f})_{\overline{x_i}}$ is the function $\overline{f}$ evaluated with $x_i=0$. This is equivalent to first evaluating $f$ with $x_i=0$ (which is $f_{\overline{x_i}}$) and then negating the result. Therefore:
>>
>>$$
>>(\overline{f})_{\overline{x_i}} = \overline{f_{\overline{x_i}}}
>>$$
>>
>>Similarly, for the cofactor with respect to $x_i=1$:
>>
>>$$
>>(\overline{f})_{x_i} = \overline{f_{x_i}}
>>$$
>>
>>Substituting these back into the expansion for $\overline{f}$, we get the desired identity:
>>
>>$$
>>\overline{f} = (\overline{x_i} \land \overline{f_{\overline{x_i}}}) \lor (x_i \land \overline{f_{x_i}})
>>$$
>>
>>**Proof of (2):** *The following proof was generated by AI and has not been human-verified. As such, it may contain mistakes.*
>>
>>This identity is derived by starting with the standard Shannon expansion of the original function $f$ and applying De Morgan's laws.
>>
>>The Shannon expansion of $f$ is:
>>
>>$$
>>f = (\overline{x_i} \land f_{\overline{x_i}}) \lor (x_i \land f_{x_i})
>>$$
>>
>>Now, we negate both sides of the equation:
>>
>>$$
>>\overline{f} = \overline{(\overline{x_i} \land f_{\overline{x_i}}) \lor (x_i \land f_{x_i})}
>>$$
>>
>>Using De Morgan's law ($\overline{A \lor B} = \overline{A} \land \overline{B}$), we get:
>>
>>$$
>>\overline{f} = \overline{(\overline{x_i} \land f_{\overline{x_i}})} \land \overline{(x_i \land f_{x_i})}
>>$$
>>
>>Next, we apply De Morgan's law again to each term ($\overline{A \land B} = \overline{A} \lor \overline{B}$):
>>
>>$$
>>\overline{f} = (\overline{\overline{x_i}} \lor \overline{f_{\overline{x_i}}}) \land (\overline{x_i} \lor \overline{f_{x_i}})
>>$$
>>
>>Finally, using the law of double negation ($\overline{\overline{A}} = A$) on the term $\overline{\overline{x_i}}$, we arrive at the identity:
>>
>>$$
>>\overline{f} = (x_i \lor \overline{f_{\overline{x_i}}}) \land (\overline{x_i} \lor \overline{f_{x_i}})
>>$$
>>
>>By the commutative property of conjunction, this is equivalent to:
>>
>>$$
>>\overline{f} = (\overline{x_i} \lor \overline{f_{x_i}}) \land (x_i \lor \overline{f_{\overline{x_i}}})
>>$$
>>
>