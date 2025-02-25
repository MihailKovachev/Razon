---
title: Formal Languages
tags:
  - formal-logic
  - mathematics
---

# Symbols and Alphabets

>[!DEFINITION] Definition: Alphabet
>
>An **alphabet** is a [set](../Set%20Theory/Sets.md) whose elements we call **symbols**.
>

## Expressions

>[!DEFINITION] Definition: Expression
>
>Let $\mathcal{A}$ be an [alphabet](Formal%20Languages.md#symbols%20and%20alphabets).
>
>An **expression** over $\mathcal{A}$ is a [tuple](../../Set%20Theory/Tuples.md) of [symbols](Formal%20Languages.md#symbols%20and%20alphabets) from $\mathcal{A}$.
>
>>[!NOTE] Note: Strings
>>
>>Expressions are also called **strings**.
>>
>
>>[!NOTATION]-
>>
>>Expressions are usually written by listing their symbols directly, instead of placing them between parentheses in a comma-separated list, as is usually the case with tuples. For example, the expression $(a, 2, s, s, 1,w)$ is written as $a2ss1w$.
>>
>>The [set](../Set%20Theory/Sets.md) of all expressions which can be formed using the alphabet $\mathcal{A}$ is denoted by $\mathcal{A}^\ast$.
>>

>[!DEFINITION] Definition: Concatenation
>
>Let $\alpha$ and $\beta$ be two [expressions](Formal%20Languages.md#expressions) formed from the same [alphabet](Formal%20Languages.md#symbols%20and%20alphabets).
>
>The **concatenation** of $\beta$ to $\alpha$ is the expression obtained by listing the symbols of $\alpha$ first and then the symbols of $\beta$.
>
>>[!NOTATION]-
>>
>>$$
>>\alpha \beta
>>$$
>>
>

# Syntax

>[!DEFINITION] Definition: Well-Formed Formula
>
>Let $\mathcal{L} = (\mathcal{A}, \mathcal{S})$ be a [formal language](Formal%20Languages.md#formal%20languages).
>
>A **well-formed formula** in $\mathcal{L}$ is an [expression](Formal%20Languages.md#expressions) in the [alphabet](Formal%20Languages.md#symbols%20and%20alphabets) $\mathcal{A}$ which is considered valid under the [syntax](Formal%20Languages.md#syntax) $\mathcal{S}$.
>
>>[!NOTE]
>>
>>The term "well-formed formula" is often abbreviated to "wff".
>>
>
>>[!INTUITION]-
>>
>>Well-formed formulas can be thought of as expressions which are meaningful in the context of a given language. For example, the sentence "Yesterday, Harry went to the bar" is meaningful and can be considered a wff in English. In constrast, the sentence "Fall on the in chair sock" does not carry any meaning and is, therefore, *not* a wff in English.
>>
>

>[!DEFINITION] Definition: Syntax
>
>Let $\mathcal{A}$ be an [alphabet](Formal%20Languages.md#symbols%20and%20alphabets).
>
>A **syntax** is a [set](../Set%20Theory/Sets.md) of rules that specify which [expressions](Formal%20Languages.md#expressions) in $\mathcal{A}$ are considered [well-formed formulas](Formal%20Languages.md#syntax) and how to generate new wffs from existing ones.
>

# Formal Languages

>[!DEFINITION] Definition: Formal Language
>
>A **formal language** is an [ordered pair](../../Set%20Theory/Ordered%20Pairs.md) $(\mathcal{A}, \mathcal{S})$ consisting of an [alphabet](Formal%20Languages.md#symbols%20and%20alphabets) $\mathcal{A}$ and a [syntax](Formal%20Languages.md#syntax) $\mathcal{S}$.
>
>>[!NOTATION]-
>>
>>Formal languages are often denoted by $\mathcal{L}$ with or without subscripts.
>>
>