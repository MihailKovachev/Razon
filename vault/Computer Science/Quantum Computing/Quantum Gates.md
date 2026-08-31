---
title: Quantum Gates
tags:
    - quantum-computing
    - computer-science
---

# Quantum Gates

Due to the physical nature of quantum systems, all operations with [quantum information](./Quantum%20Information.md) are subject to a few constraints:
- All operations must be [norm-preserving](../../Mathematics/Algebra/Linear%20Algebra/Complex%20Vectors/Complex%20Vectors.md) because they take a [quantum state](./Quantum%20Information.md) as an input and also produce a [quantum state](./Quantum%20Information.md) as an output and all [quantum states](./Quantum%20Information.md) must have a [norm](../../Mathematics/Algebra/Linear%20Algebra/Complex%20Vectors/Complex%20Vectors.md) of $1$.
- With the exception of [measurement](./Measurement.md), all operations must be [linear](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md).
- With the exception of [measurement](./Measurement.md), all operations must be [reversible](../../Mathematics/Analysis/Functions/Injections,%20Surjections%20and%20Bijections.md#Injections).

Since [quantum states](./Quantum%20Information.md) are [complex vectors](../../Mathematics/Algebra/Linear%20Algebra/Complex%20Vectors/Complex%20Vectors.md), all of the above criteria are satisfied by [unitary matrices](../../Mathematics/Algebra/Matrices/Complex%20Matrices/Unitary%20Matrices.md), i.e. every quantum operation can be represented by a [unitary matrix](../../Mathematics/Algebra/Matrices/Complex%20Matrices/Unitary%20Matrices.md) and every [unitary matrix](../../Mathematics/Algebra/Matrices/Complex%20Matrices/Unitary%20Matrices.md) represents some quantum operation.

>[!DEFINITION] Definition: Quantum Gate
>
>The [matrix](../../Mathematics/Algebra/Matrices/Complex%20Matrices/Unitary%20Matrices.md) representations of quantum operations are known as **quantum gates**.
>