---
title: Truth Assignment
tags:
    - mathematical-logic
    - mathematics
---

# Introduction

In every language, some expressions are meaningful, while others are meaningless. For example, the sentence "The kid is playing with the dog" has a very clear meaning, while the expression "of the on the if in" does not. Notice, however, that which expressions are meaningful and which are meaningless is entirely decided by us. Maybe not specifically us, but at least by all our ancestors who, through a lengthy historical process, established the rules of English syntax and thus decided which expressions are meaningful and which are not.

The situation with [formal languages](./Formal%20Languages.md) is pretty much analogous. However, since their purpose is to be simple and consistent, the ideas which they can express are limited to a very small number. This restriction is, of course, arbitrarily imposed by us and by nothing else. While we could technically have a [formal language](./Formal%20Languages.md) which could expresses thousands if not hundreds of thousands of different notions, this language would not be of much use to us because it would be pretty much indistinguishable from normal languages such as English or Arabic.

# Truth Assignment

Unfortunately, the terminology used to refer to the ideas expressed by a given [formal language](./Formal%20Languages.md) is rather confusing.

>[!DEFINITION] Definition: Truth Assignment
>
>Let $\mathcal{L}$ be a [formal language](./Formal%20Languages.md) and let $v: S \subseteq \mathcal{L} \to \mathcal{T}$ be some [function](../Analysis/Functions/Functions.md) from a [subset](../Set%20Theory/Sets.md) $S$ of $\mathcal{L}$ to some other [set](../Set%20Theory/Sets.md) $\mathcal{T}$:
>- The elements of $\mathcal{T}$ we call **truth values**;
>- The elements of $S$ we call **truth-apt expressions**;
>- The [function](../Analysis/Functions/Functions.md) $v$ we call a **truth assignment**.
>
>>[!EXAMPLE]- Example
>>
>>Suppose $\mathcal{L}$ is some language over the lowercase English alphabet which contained the expressions "green dog", "warm chair", "slightly annoying person" and "cat". Furthermore, suppose $\mathcal{T} = \{\alpha, \beta, \omega\}$. 
>>
>>One possible truth assignment would be
>>
>>$$
>>\begin{aligned}
>>&v(\text{green dog}) = \alpha \\
>>&v(\text{warm chair}) = \beta \\
>>&v(\text{slightly annoying person}) = \omega \\
>>&v(\text{cat}) = \beta
>>\end{aligned}
>>$$
>>
>>Another possible truth assignment would be
>>
>>$$
>>\begin{aligned}
>>&v(\text{green dog}) = \beta \\
>>&v(\text{warm chair}) = \beta \\
>>&v(\text{slightly annoying person}) = \beta \\
>>&v(\text{cat}) = \beta
>>\end{aligned}
>>$$
>> 
>

Most commonly, $\mathcal{T}$ has just two values, usually denoted as $\{T, F\}$ or $\{0, 1\}$. However, this choice is arbitrary and one can choose a set of truth values with any number of elements. It just so happens that we often deal with just two values because they are useful for modelling "true" and "false" in a way which agrees empirically with logical (in the philosophical sense) conundrums we encounter on a daily basis. The set $\mathcal{T}$ and its elements themselves have little to do with metaphysical truth - if not for any other reason, then for the fact that there are mathematical system where $\mathcal{T}$ has three or more elements (although usually three).