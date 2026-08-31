---
title: Quantum Information
tags:
  - quantum-computing
  - computer-science
---

# Quantum Information

## Qubits

The fundamental unit of information for classical computers is the bit, which can be one of two numbers - zero or one. In contrast, the fundamental unit of information for [quantum computers](../../index.md) are [complex vectors](../../Mathematics/Algebra/Linear%20Algebra/Complex%20Vectors/Complex%20Vectors.md).

>[!DEFINITION] Definition: Qubit
>
>A **quantum bit** (**qubit**) is a two-dimensional [complex vector](../../Mathematics/Algebra/Linear%20Algebra/Complex%20Vectors/Complex%20Vectors.md) whose [Euclidean norm](../../Mathematics/Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) is $1$.
>
>>[!NOTATION] Bra-Ket Notation
>>
>>[Qubits](./Quantum%20Information.md) are always expressed via [bra-ket notation](../../Mathematics/Algebra/Matrices/Row%20and%20Column%20Vectors.md).
>>
>
>>[!NOTE] Note: Euclidean Norm
>>
>>The condition that the [Euclidean norm](../../Mathematics/Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) must be equal to $1$ reflects a fundamental truth about the physical nature of [quantum systems](TODO).
>>
>

>[!NOTATION] Notation: Common States
>
>Four common [qubit states](#Qubits) have reserved names and notations:
>
>|Name|Notation|State|
>|:--:|:--:|:--:|
>|Zero|$\left\vert 0 \right\rangle$|$\begin{bmatrix}1 \\ 0\end{bmatrix}$|
>|One|$\left\vert 1 \right\rangle$|$\begin{bmatrix}0 \\ 1\end{bmatrix}$|
>|Plus|$\left\vert + \right\rangle$|$\begin{bmatrix}\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}}\end{bmatrix}$|
>|Minus|$\left\vert - \right\rangle$|$\begin{bmatrix}\frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}}\end{bmatrix}$|
>|i|$\left\vert \mathrm{i} \right\rangle$|$\begin{bmatrix}\frac{1}{\sqrt{2}} \\ \mathrm{i}\frac{1}{\sqrt{2}}\end{bmatrix}$|
>|Minus i|$\left\vert -\mathrm{i} \right\rangle$|$\begin{bmatrix}\frac{1}{\sqrt{2}} \\ -\mathrm{i}\frac{1}{\sqrt{2}}\end{bmatrix}$||
>

### Bloch Sphere

A single [qubit](./Quantum%20Information.md) can be visualized intuitively as an arrow pointing from the origin to a point on the so-called **Bloch sphere**.

## Quantum Registers

>[!DEFINITION] Definition: Quantum Register
>
>A **quantum register** is a sequence of [qubits](./Quantum%20Information.md).
>

>[!DEFINITION] Definition: Quantum State
>
>The **state** of a [quantum register](./Quantum%20Information.md) with $n$ [qubits](./Quantum%20Information.md) $\left\vert q_{n-1} \right\rangle, \dotsc, \left\vert q_{0} \right\rangle$ or $\left\langle q_{n-1} \right\vert, \dotsc, \left\langle q_{0} \right\vert$ is their [Kronecker product](../../Mathematics/Algebra/Matrices/Matrix%20Operations.md#Kronecker%20Product):
>
>$$
>\left\vert q_{n-1} \right\rangle \otimes \dotsc \otimes \left\vert q_{0} \right\rangle \qquad \text{or} \qquad \left\langle q_{n-1} \right\vert \otimes \dotsc \otimes \left\langle q_{0} \right\vert
>$$
>
>>[!NOTATION]
>>
>>We use some shorthand notations for such products:
>>
>>$$
>>\begin{aligned}
>>\left\vert q_{n-1} \right\rangle \left\vert q_{n-2} \right\rangle  \cdots \left\vert q_{0} \right\rangle &\qquad \left\langle q_{n-1} \right\vert \left\langle q_{n-2} \right\vert \cdots \left\langle q_{0} \right\vert \\
>>\left\vert q_{n-1}, q_{n-2}, \dotsc,  q_{0} \right\rangle &\qquad \left\langle q_{n-1}, q_{n-2}, \dotsc, q_{0} \right\vert \\
>>\left\vert q_{n-1} q_{n-2} \cdots  q_{0} \right\rangle &\qquad \left\langle q_{n-1} q_{n-2} \cdots q_{0} \right\vert
>>\end{aligned}
>>$$
>>
>>>[!EXAMPLE]-
>>>
>>>The [state](./Quantum%20Information.md) $\left\vert 10 \right\rangle$ is
>>>
>>>$$
>>>\left\vert 10 \right\rangle = \left\vert 1 \right\rangle \left\vert 0 \right\rangle = \left\vert 1 \right\rangle \otimes \left\vert 0 \right\rangle = \begin{bmatrix}0 \cdot \begin{bmatrix}1 \\ 0\end{bmatrix} \\ 1 \cdot \begin{bmatrix}1 \\ 0\end{bmatrix}\end{bmatrix} = \begin{bmatrix}0 \\ 0 \\ 1 \\ 0\end{bmatrix}
>>>$$
>>>
>>
>

The [state](./Quantum%20Information.md) of an $n$-[qubit](./Quantum%20Information.md) [quantum register](./Quantum%20Information.md) is a [complex vector](../../Mathematics/Algebra/Linear%20Algebra/Complex%20Vectors/Complex%20Vectors.md) of dimension $2^n$.

>[!NOTATION]
>
>The most common label for [quantum states](./Quantum%20Information.md) is the Greek letter $\psi$:
>
>$$
>\left\langle \psi \right\vert \qquad \left\vert \psi \right\rangle
>$$
>

### Computational Bases

>[!DEFINITION] Definition: Computational Basis
>
>An $n$-dimensional **computational basis** is any [orthonormal basis](../../Mathematics/Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md#Orthogonality) for the [vector space](../../Mathematics/Algebra/Linear%20Algebra/Complex%20Vectors/Complex%20Vectors.md) $\mathbb{C}^n$ or $\mathbb{C}^{1 \times n}$.
>
>>[!EXAMPLE]-
>>
>>The [states](./Quantum%20Information.md) $\left\vert 0 \right\rangle$ and $\left\vert 1 \right\rangle$ are a [computational basis](./Quantum%20Information.md) for $\mathbb{C}^2$. Similarly, so are $\left\vert + \right\rangle$ and $\left\vert - \right\rangle$ as well as $\left\vert \mathrm{i} \right\rangle$ and $\left\vert -\mathrm{i} \right\rangle$.
>>
>>The [states](./Quantum%20Information.md) $\left\langle 00 \right\vert$, $\left\langle 01 \right\vert$, $\left\langle 10 \right\vert$ and $\left\langle 11 \right\vert$ are a [computational basis](./Quantum%20Information.md) for $\mathbb{C}^{1\times 4}$.
>>
>

Suppose we have some $n$-dimensional [quantum state](./Quantum%20Information.md) $\left\vert \psi \right\rangle$ and a [computational basis](./Quantum%20Information.md) $\left\vert b_1 \right\rangle, \dotsc, \left\vert b_n \right\rangle$ such that $\left\vert \psi \right\rangle$ has the representation

$$
\left\vert \psi \right\rangle = \sum_{k = 1}^n c_k \left\vert b_k \right\rangle = c_1 \left\vert b_1 \right\rangle + \cdots c_n \left\vert b_n \right\rangle,
$$

where $c_1, \dotsc, c_k \in \mathbb{C}$.

>[!DEFINITION] Definition: Pure State
>
>We say that $\left\vert \psi \right\rangle$ is a **pure state** if it is equal to one of $\left\vert b_1 \right\rangle, \dotsc, \left\vert b_n \right\rangle$.
>

>[!DEFINITION] Definition: Superposition (Mixed State)
>
>We say that $\left\vert \psi \right\rangle$ is a **mixed state** or a **superposition** of $\left\vert b_1 \right\rangle, \dotsc, \left\vert b_n \right\rangle$ if it is *not* equal to any of $\left\vert b_1 \right\rangle, \dotsc, \left\vert b_n \right\rangle$.
>
>>[!EXAMPLE]-
>>
>>The [state](./Quantum%20Information.md) $\left\vert + \right\rangle$ is a [superposition](./Quantum%20Information.md) of $\left\vert 0 \right\rangle$ and $\left\vert 1 \right\rangle$. The [state](./Quantum%20Information.md) $\left\vert 1 \right\rangle$ is a [superposition](./Quantum%20Information.md) of $\left\vert \mathrm{i} \right\rangle$ and $\left\vert -\mathrm{i} \right\rangle$.
>>
>>The [state](./Quantum%20Information.md) $\left\vert -+ \right\rangle$ is a [superposition](./Quantum%20Information.md) of $\left\vert 00 \right\rangle$, $\left\vert 01 \right\rangle$, $\left\vert 10 \right\rangle$ and $\left\vert 11 \right\rangle$.
>>
>

>[!NOTATION] Notation: Special Bases
>
>A few [computational bases](#Computational%20Bases) have been given names:
>
>$$
>\begin{aligned}
>Z &\overset{\text{def}}{=} \{\left\vert 0\right\rangle, \left\vert 1\right\rangle\} \\
>X &\overset{\text{def}}{=} \{\left\vert -\right\rangle, \left\vert +\right\rangle\} \\
>Y &\overset{\text{def}}{=} \{\left\vert -\mathrm{i}\right\rangle, \left\vert \mathrm{i} \right\rangle\}
>\end{aligned}
>$$
>

The definitions are analogous for [states](./Quantum%20Information.md) in $\mathbb{C}^{1 \times n}$.

### Entanglement

>[!DEFINITION] Definition: Product State
>
>An $n$-bit [quantum state](./Quantum%20Information.md) $\left\vert \Psi \right\rangle \in \mathbb{C}^{2^n}$ is a **product state** or a **separable state** if there exist $n$ [qantum states](./Quantum%20Information.md) $\left\vert v_1 \right\rangle, \dotsc, \left\vert v_n \right\rangle \in \mathbb{C}^{2}$ whose [Kronecker product](../../Mathematics/Algebra/Matrices/Matrix%20Operations.md) is $\left\vert \Psi \right\rangle$:
>
>$$
>\left\vert \Psi \right\rangle = \bigotimes_{k = 1}^n \left\vert v_k \right\rangle = \left\vert v_1 \right\rangle \otimes \cdots \otimes \left\vert v_n \right\rangle 
>$$
>

>[!DEFINITION] Definition: Entangled State
>
>A [quantum state](./Quantum%20Information.md) is **entangled** if it is *not* a [product state](#Entanglement).
>

[Entangled states](#Entanglement) are peculiar because [measuring](./Measurement.md) some of the [qubits](./Quantum%20Information.md) of a [quantum register](./Quantum%20Information.md) in an [entangled state](#Entanglement) directly influences the other.