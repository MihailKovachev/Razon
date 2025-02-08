---
title: Propositional Logic
tags:
    - two-valued-logic
    - formal-logic
    - mathematics
---

>[!DEFINITION] Definition: Atomic Truth Assignment
>
>An **atomic truth assignment** in the [formal language of propositional logic](The%20Formal%20Language%20of%20Propositional%20Logic.md) $\mathcal{L}_\text{PL}$ is a [function](../../../Analysis/Functions/index.md) $v$ which assigns a [truth value](../Truth%20Values.md) to every atomic formula in $\mathcal{L}_\text{PL}$.
>
>>[!INTUITION]-
>>
>>The truth assignment $v$ can be thought of as translating the English [propositions](Proposition.md) we choose to study into atomic formulas $A_1, A_2, \cdots$. Specifying $v$ is analogous to the process of saying "Let $A_1$ denote this proposition, let $A_2$ denote that proposition, etc". The truth value of an atomic formula is then determined solely by whether its English translation is true or false.
>>
>>This, in turn, limits what English sentences can be translated into atomic formulas - questions and imperative sentences cannot be represented by atomic formulas, since it does not make sense to say that a question or a command is true or false.
>>
>>Logic does not care how we determine the truth values of atomic formulas - it only studies the relationships we can infer after we have specified which atomic formulas (i.e. basic statements) are true and which are false. Although it might seem counterintuitive at first, it is actually very natural - all reasoning is based on certain assumptions which we take to be true or false simply because they *seem* to be that way. We *have* to start somewhere.
>>
>

>[!DEFINITION] Definition: Extended Truth Assignment
>
>Let $v$ be an [atomic truth assignment](Truth%20Assignment.md) in the [formal language of propositional logic](The%20Formal%20Language%20of%20Propositional%20Logic.md) $\mathcal{L}_{PL}$.
>
>An **extended truth assignment** is a [function](../../../Analysis/Functions/index.md) $\bar{v}$ which assigns a [truth value](../Truth%20Values.md) to every [well-formed formula](../../Formal%20Languages.md) in $\mathcal{L}_\text{PL}$ according to the following rules:
>1. The truth value assigned to each atomic formula by $\bar{v}$ is the same as the truth value assigned to it by $v$.
>2. The truth value assigned to wffs of the form $(P)$, where $P$ is a wff, is the same as the truth value assigned to $P$, i.e. $\bar{v}((P)) = \bar{v}(P)$.
>3. The truth value assigned to a wff formed using the [sentential connectives](Propositional%20Connectives.md) on two other wffs $P$ and $Q$ is defined by the following truth tables:
>	- [Propositional Connectives](Propositional%20Connectives.md)
>	
>	|$P$|$\neg P$|
>	|:--:|:--:|
>	|$T$|$F$|
>	|$F$|$T$|
>	
>	- [Propositional Connectives](Propositional%20Connectives.md)
>	
>	|$P$|$Q$|$P \land Q$|
>	|:--:|:--:|:--:|
>	|$T$|$T$|$T$|
>	|$T$|$F$|$F$|
>	|$F$|$T$|$F$|
>	|$F$|$F$|$F$|
>	
>	- [Propositional Connectives](Propositional%20Connectives.md)
>	
>	|$P$|$Q$|$P \lor Q$|
>	|:--:|:--:|:--:|
>	|$T$|$T$|$T$|
>	|$T$|$F$|$T$|
>	|$F$|$T$|$T$|
>	|$F$|$F$|$F$|
>	
>	- [Propositional Connectives](Propositional%20Connectives.md)
>	
>	|$P$|$Q$|$P \rightarrow Q$|
>	|:--:|:--:|:--:|
>	|$T$|$T$|$T$|
>	|$T$|$F$|$F$|
>	|$F$|$T$|$T$|
>	|$F$|$F$|$T$|
>	
>	- [Propositional Connectives](Propositional%20Connectives.md)
>	
>	|$P$|$Q$|$P \leftrightarrow Q$|
>	|:--:|:--:|:--:|
>	|$T$|$T$|$T$|
>	|$T$|$F$|$F$|
>	|$F$|$T$|$F$|
>	|$F$|$F$|$T$|