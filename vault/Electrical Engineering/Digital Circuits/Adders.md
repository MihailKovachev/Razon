---
title: Adders
tags:
    - digital-circuits
    - electrical-engineering
---

# Adders

**Adders** are [digital circuits](./Digital%20Circuits.md) which can be used to compute the addition and subtraction of binary numbers. 

## Integer Adders

### Half Adder

>[!DEFINITION] Definition: Half Adder
>
>A **half adder** is a [digital circuit](./Digital%20Circuits.md) which computes the algorithm for the addition of two binary digits.
>

>[!ALGORITHM] Algorithm: Addition of Two Bits
>
>We have two inputs - $x_0$ and $x_1$ - and two outputs - $s$ for *sum* and $c$ for *carry*:
>- If $x_0 = 0$ and $x_1 = 0$, then the output is $s = 0$ and $c = 0$.
>- If $x_0 = 0$ and $x_1 = 1$, then the output is $s = 1$ and $c = 0$.
>- If $x_0 = 1$ and $x_1 = 0$, then the output is $s = 1$ and $c = 0$.
>- If $x_0 = 1$ and $x_1 = 1$, then the output is $s = 0$ and $c = 1$.
>

A [half adder](#Half%20Adders) essentially computes the [Boolean function](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md) with the following [truth table](../../Mathematics/Algebra/Boolean%20Algebra/Truth%20Tables.md):

|$x_0$|$x_1$||$s$|$c$|
|:--:|:--:|:--:|:--:|:--:|
|$0$|$0$||$0$|$0$|
|$0$|$1$||$1$|$0$|
|$1$|$0$||$1$|$0$|
|$1$|$1$||$0$|$1$|

From this, we see that computing $s$ is equivalent to computing the [exclusive disjunction](../../Mathematics/Algebra/Boolean%20Algebra/Exclusive%20Disjunction.md) of $x_0$ and $x_1$, while computing $c$ is equivalent to computing the [conjunction](../../Mathematics/Algebra/Boolean%20Algebra/Conjunction.md) of $x_0$ and $x_1$. Therefore, a [half adder](#Half%20Adders) can be implemented as a [XOR gate](./Logic%20Gates/Logic%20Gates.md) and an [AND Gate](./Logic%20Gates/Logic%20Gates.md):

![Half Adder](./res/Adders/Half%20Adder.svg)

### Full Adders

Unfortunately, [half adders](#Half%20Adders) are insufficient for computing the addition of multi-bit numbers. In general, adding multi-bit numbers is done by adding them on a bit-by-bit basis. However, we need to know if there was a carry from the addition of the previous two bits. A [half adder](#Half%20Adders) cannot do this.

>[!DEFINITION] Definition: Full Adder
>
>An $n$**-bit full adder** is a [digital circuit](./Digital%20Circuits.md) which computes the addition of two $n$-bit numbers.
>
>>[!NOTATION]
>>
>>The following symbol is often used for a [full adder](#Full%20Adders):
>>
>>![Full Adder Symbol](./res/Adders/Full%20Adder%20Symbol.svg)
>>
>

Generally, an $n$-bit [full adder](#Full%20Adders) takes two $n$-bit numbers $a_{n-1}\cdots a_0$ and $b_{n-1} \cdots b_0$ and outputs another $n$-bit number $s_{n-1}\cdots s_0$ and a potential carry $c_{\text{out}}$. 

If the bits going into a [full adder](#Full%20Adders) are interpreted as numbers in [two's complement](../../Computer%20Science/Data%20Representation/Integers.md#Two's%20Complement), then the subtraction $a - b$ is equivalent to the addition $a + b'$, where $b'$ is the negative of $b$ in [two's complement](../../Computer%20Science/Data%20Representation/Integers.md#Two's%20Complement). This means that a full adder can both add and subtract numbers.

>[!WARNING] Warning: Integer Overflow
>
>An $n$-bit [full adder](#Full%20Adders) takes two $n$-bit numbers and outputs another $n$-bit number. If the addition or subtraction of the two inputs requires more than $n$ bits to be represented, then the result of the [full adder](#Full%20Adders) the will be incorrect. This is indicated by the carry bit $c_{\text{out}}$:
>- If $c_{\text{out}} = 0$, then the result is correct.
>- If $c_{\text{out}} = 1$, then the result is incorrect.
>
>Most commonly an integer overflow manifests in two ways:
>- If the sum of two numbers is too great to fit into $n$ bits, the output $s_{n-1}\cdots s_0$ will be a negative number when interpreted in [two's complement](../../Computer%20Science/Data%20Representation/Integers.md#Two's%20Complement).
>- If the difference of two numbers is too small to fit into $n$ bits, the output $s_{n-1}\cdots s_0$ will be a positive number when interpreted in [two's complement](../../Computer%20Science/Data%20Representation/Integers.md#Two's%20Complement).
>

### 1-Bit Full Adders

If we have a [digital circuit](./Digital%20Circuits.md) capable of adding two bits, we can use it to implement addition of binary numbers of any size, since addition is done on a bit-by-bit basis. However, for each addition of two bits, we also need to take into account a possible carry from the addition of the previous two bits. This means that our [circuit](./Digital%20Circuits.md) for adding two bits needs to have a third input which signifies whether there was a previous addition and whether it resulted in a carry.

>[!DEFINITION] Definition: 1-Bit Full Adder
>
>A **1-bit full adder** is a [digital circuit](./Digital%20Circuits.md) which takes three input bits - $a$, $b$ and $c_{\text{in}}$ - and produces two output bits:
>- $s$ is the binary sum of the bits $a$ and $b$;
>- $c_{\text{out}}$ is the carry (if any) from the addition of $a$ and $b$.
>

Essentially, a [1-bit full adder](#1-Bit%20Full%20Adders) computes the following [Boolean function](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md) with the following [truth table](../../Mathematics/Algebra/Boolean%20Algebra/Truth%20Tables.md):

|$a$|$b$|$c_{\text{in}}$||$s$|$c_{\text{out}}$|
|:--:|:--:|:--:|:--:|:--:|:--:|
|$0$|$0$|$0$||$0$|$0$|
|$0$|$0$|$1$||$1$|$0$|
|$0$|$1$|$0$||$1$|$0$|
|$0$|$1$|$1$||$0$|$1$|
|$1$|$0$|$0$||$1$|$0$|
|$1$|$0$|$1$||$0$|$1$|
|$1$|$1$|$0$||$0$|$1$|
|$1$|$1$|$1$||$1$|$1$|

From this, we can derive a [CDNF](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md#Canonical%20Disjunctive%20Normal%20Form) for $s$ and $c_{\text{out}}$:

$$
\begin{aligned}
s &= \overline{a}\overline{b}c_{\text{in}} + \overline{a}b\overline{c_{\text{in}}} + a\overline{b}\overline{c_{\text{in}}} + abc_{\text{in}} \\
c_{\text{out}} &= \overline{a}bc_{\text{in}} + a\overline{b}c_{\text{in}} + ab\overline{c_{\text{in}}} + abc_{\text{in}}
\end{aligned}
$$

Through some algebraic manipulations, we arrive at [expressions](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md) for $s$ and $c_{\text{out}}$ which use the [XOR operation](../../Mathematics/Algebra/Boolean%20Algebra/Exclusive%20Disjunction.md):

$$
\begin{aligned}
s &= a \oplus b \oplus c_{\text{in}} \\
c_{\text{out}} &= (a \oplus b)c_{\text{in}} + ab
\end{aligned}
$$

>[!EXAMPLE]- Example: 1-Bit Full Adder via Logic Gates
>
>The simplest and most common implementation for a [1-bit full adder](#1-bit%20Full%20Adder) is to implement its formulas using [XOR gates](./Logic%20Gates/Logic%20Gates.md), [AND gates](./Logic%20Gates/Logic%20Gates.md) and [OR gates](./Logic%20Gates/Logic%20Gates.md):
>
>![1-Bit Full Adder from Logic Gates](./res/Adders/1-Bit%20Full%20Adder%20from%20Logic%20Gates.svg)
>

We can label the [expressions](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md) $a \oplus b$ and $ab$ in the following way:

- **Propagate**: $P \overset{\text{def}}{=} a \oplus b$;
- **Generate**: $G \overset{\text{def}}{=} ab$.

We have:

$$\begin{aligned}s &= P \oplus c_{\text{in}} \\c_{\text{out}} &= P\cdot c_{\text{in}} + G\end{aligned}$$

We do this for two reasons:

- If $P = 1$, then $c_{\text{out}} = c_{\text{in}}$, i.e. $c_{\text{in}}$ is *propagated* to $c_{\text{out}}$.
- If $G = 1$, then $c_{\text{out}} = 1$, i.e. we know that the addition of $a$ and $b$ *generates* a carry whenever $G = 1$.
- If both $P = 0$ and $G = 0$, then $c_{\text{out}} = 0$.

### Ripple-Carry Adder

A **ripple-carry adder** is a simple implementation of an $n$-bit [full adder](#Full%20Adders) which simply chains $n$ [1-bit full adders](#1-bit%20Full%20Adder) to compute the sum of two binary numbers $a_{n-1}\cdots a_0$ and $b_{n-1} \cdots b_0$:

![Ripple-Carry Adder](./res/Adders/Ripple-Carry%20Adder.svg)

The initial carry-in $c_{\text{in}}$ is automatically set to zero because there are no previous bits. This is why we can also replace the right-most [adder](#1-bit%20Full%20Adder) with a [half adder](#Half%20Adders). The $c_{\text{out}}$ of each [1-bit full adder](#1-Bit%20Full%20Adders) is fed into the $c_{\text{in}}$ of the next one. 

