---
title: Formal Languages
tags:
  - mathematical-logic
  - mathematics
---

# Introduction

Doing [[../index|mathematics]] requires the use of language for writing down formulas and expressions. However, the languages we use to communicate on a daily basis are not really suitable for this purpose because they are overly complex and inconsistent due to the large number of rules and exceptions they have.

This is why mathematicians have devised languages, known as **formal languages**, which are simple and without exceptions.

# Formal Languages

>[!DEFINITION] Definition: Alphabets and Symbols
>
>An **alphabet** is a non-empty [[../Set Theory/Sets|set]] whose elements we call **symbols** or **letters**.
>
>>[!NOTATION]
>>
>>Alphabets are commonly denoted by the uppercase Greek letter sigma ($\Sigma$).
>>
>
>>[!EXAMPLE]- Example
>>
>>As per the definition, any non-empty [[../Set Theory/Sets|set]] can be an alphabet. This includes the uppercase English alphabet $\{A, B, \dotsc, Y, Z\}$, the lowercase Greek alphabet $\{\alpha, \beta, \dotsc, \omega\}$, the natural numbers $\mathbb{N}$, the set $\{\circ, +, -, \triangle\}$ and so on.
>>
>

>[!DEFINITION] Definition: Expression
>
>Let $\Sigma$ be an [[Formal Languages|alphabet]].
>
>An **expression** (or **string** or **word**) over $\Sigma$ is any $n$-[[../Set Theory/Tuples|tuple]] whose elements are symbols from $\Sigma$.
>
>>[!NOTATION]
>>
>>Expressions are usually written by listing their symbols directly, instead of placing them between parentheses in a comma-separated list, as is usually the case with tuples. For example, the expression $(a, 2, s, s, 1,w)$ is written as $a2ss1w$.
>>
>
>>[!NOTATION] Notation: Kleene Star
>>
>>The [[Sets|set]] of *all* finite-length [[Formal Languages|expressions]] over a given alphabet $\Sigma$ is denoted by $\Sigma^\ast$.
>>
>
>>[!EXAMPLE]- Example: Expressions
>>
>>If $\Sigma = \{a, b, 1, +, -\}$, then some expressions over $\Sigma$ are $a$, $1b$, $aba$, $11abb$, $1b+-a$, etc.
>>
>

>[!DEFINITION] Definition: Formal Language
>
>A **formal language** over an [[Formal Languages|alphabet]] $\Sigma$ is any [[../Set Theory/Sets|subset]] of the [[../Set Theory/Sets|set]] of all finite-length [[Formal Languages|expressions]] $\Sigma^\ast$ over $\Sigma$.
>
>>[!NOTATION]- Notation
>>
>>Formal languages are commonly denoted by $\mathcal{L}$.
>>
>
