---
title: Physical Systems
tags:
    - classical-mechanics
    - physics
---

# Physical System

>[!DEFINITION] Definition: Physical System
>
>A **physical system** is any set of physical objects which we have chosen to model and examine using physics.
>

>[!DEFINITION] Definition: Environment
>
>The **environment** of a [physical system](./Physical%20Systems.md) are all physical objects which are not part of the system.
>

>[!DEFINITION] Definition: Isolated System
>
>A [physical system](./Physical%20Systems.md) is **isolated** if the objects inside it cannot interact with the objects in the [environment](./Physical%20Systems.md).
>

## Parametrization

We are rarely interested in all properties of a given [physical system](./Physical%20Systems.md). Much more often we are considered with just a subset of its properties which are relevant to solving a given problem. However, to use mathematics and physics in order to solve problems, we need a way to quantify these properties mathematically by using [numbers](../Mathematics/Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md), [vectors](../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md), etc.

>[!DEFINITION] Definition: Parameter
>
>A **parameter** of a [physical system](./Physical%20Systems.md) is any one of its characteristics which can be quantified mathematically.
>
>>[!EXAMPLE]- Example
>>
>>Imagine a [physical system](./Physical%20Systems.md) which consists of a room full of people. The average age of these people is a [parameter](#Parametrization) of the [system](./Physical%20Systems.md) because we can quantify it using a [number](../Mathematics/Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md).
>>
>
>>[!EXAMPLE]- Example
>>
>>Imagine a [physical system](./Physical%20Systems.md) which consists of a person staring at a wall. The direction from which they are looking at a wall is a [parameter](#Parametrization) of the [system](./Physical%20Systems.md) because we can quantify it using a [vector](../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md).
>>
>
>>[!DEFINITION] Definition: Independent Parameters
>>
>>A set of $n$ [parameters](#Parametrization) is **independent** if the value of each [parameter](#Parametrization) does not dependent on the values of the other $n-1$ [parameters](#Parametrization).
>>
>

[Parameters](#Parametrization) can be pretty arbitrary, but we are usually only interested in those which are useful for physical predictions and obey certain laws such as position, momentum, temperature, pressure, etc. Moreover, we are usually interested only in [parameters](#Parametrization) which are [numbers](../Mathematics/Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) because each [vector](../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) [parameter](#Parametrization) can be broken down into [numbers](../Mathematics/Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) which are its components.

>[!DEFINITION] Definition: Parametrization
>
>A **parametrization** $(P_1, \dotsc, P_n)$ of a [physical system](./Physical%20Systems.md) is any set of [parameters](#Parametrization) $P_1, \dotsc, P_n$ which we have chosen to examine and consider relevant. 
>
>>[!DEFINITION] Definition: Degrees of Freedom
>>
>>The **number of degrees of freedom** is the smallest number $k \le n$ of [parameters](#Parametrization) (without loss of generality $P_1, \dotsc, P_k$) whose values need to be known in order to determine the values of *all* [parameters](#Parametrization) $P_1, \dotsc, P_n$, i.e. there exist $n$ [functions](../Mathematics/Analysis/Functions/Functions.md) $f_1, \dotsc, f_n$ such that
>>
>>$$
>>P_i = f_i (P_1, \dotsc, P_k) \qquad i \in \{1, \dotsc, n\}
>>$$
>>
>

>[!DEFINITION] Definition: Equivalence of Parametrizations
>
>Two [parametrizations](#Parametrization) $(P_1, \dotsc, P_n)$ and $(P_1', \dotsc, P_m')$ of a [physical system](./Physical%20Systems.md) are **equivalent** if it is possible to determine the values of $P_1, \dotsc, P_n$ given the values of $P_1', \dotsc, P_m'$ and vice versa, i.e. there exists a [bijection](../Mathematics/Analysis/Functions/Injections,%20Surjections%20and%20Bijections.md) $f$ such that
>
>$$
>f(P_1, \dotsc, P_n) = (P_1', \dotsc, P_m') \qquad f^{-1}(P_1', \dotsc, P_m') = (P_1, \dotsc, P_n)
>$$
>

>[!DEFINITION] Definition: Physical State
>
>Given a [parametrization](#Parametrization) $(P_1, \dotsc, P_n)$ of a [physical system](./Physical%20Systems.md), we call any $n$-[tuple](../Mathematics/Set%20Theory/Tuples.md) $(v_1, \dotsc, v_n)$ of *values* for $P_1, \dotsc, P_n$ a **(physical) state** of the [system](./Physical%20Systems.md).
>
>
>>[!DEFINITION] Definition: Phase Space
>>
>>The [set](../Mathematics/Set%20Theory/Sets.md) of all [physical states](./Physical%20Systems.md) is known as **phase space**.
>>
>