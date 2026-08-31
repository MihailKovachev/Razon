---
tags:
    - digital-circuits
    - electrical-engineering
---

# Subtractors

>[!DEFINITION] Definition: Subtractor
>
>A **subtractor** is a [digital circuit](./Digital%20Circuits.md) which can perform the subtraction of binary numbers.
>

$$\text{Minuend} - \text{Subtrahend} = \text{Difference}$$

## Integer Subtractors

### Half Subtractor

>[!DEFINITION] Definition: Half Subtractor
>
>A **half subtractor** is a [digital circuit](./Digital%20Circuits.md) which implements the subtraction of two bits:
>
>    - Inputs: a **minuend** bit $x$ and a **subtrahend** bit $y$;
>    - Outputs: a **difference** bit $d$ and a **borrow out** bit $b_{\text{out}}$.
>    - Functionality: The $d$ bit is equal to the difference $x - y$. The $b_{\text{out}}$ is set when the operation would require a borrow from a previous bit.
>

A [half subtractors](#Half%20Subtractor) essentially computes the following [Boolean function](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md):

|$x$|$y$||$d$|$b_{\text{out}}$|
|:--:|:--:|:--:|:--:|:--:|
|$0$|$0$||$0$|$0$|
|$0$|$1$||$1$|$1$|
|$1$|$0$||$0$|$1$|
|$1$|$1$||$0$|$0$|

From the above [truth table](../../Mathematics/Algebra/Boolean%20Algebra/Truth%20Tables.md), we can derive [expressions](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md) for $d$ and $b_{\text{out}}$:

$$\begin{aligned}d & = x \oplus y \\ b_{\text{out}} & = \neg x \land y\end{aligned}$$

>[!EXAMPLE]- Example: Logic Gate Implementation
>
>Using the above [expressions](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md), we can construct a [half subtractor](#Half%20Subtractors) via [logic gates](./Logic%20Gates/Logic%20Gates.md):
>
>![Half Subtractor via Logic Gates](./res/Subtractors/Half%20Subtractor%20via%20Logic%20Gates.svg)
>

### Full Subtractor

>[!DEFINITION] Definition: Full Subtractor
>
>A **full subtractor** is a [digital circuit](./Digital%20Circuits.md) which implements the subtraction of bits, accounting for a borrow from a lower significant position:
>
>    - Inputs: a **minuend** bit $x$, a **subtrahend** bit $y$, and a **borrow in** bit $b_{\text{in}}$;
>    - Outputs: a **difference** bit $d$ and a **borrow out** bit $b_{\text{out}}$.
>    - Functionality: The $d$ bit is the result of $x - y - b_{\text{in}}$. The $b_{\text{out}}$ is set when the operation requires a borrow from the next higher bit.
>

A [full subtractor](#Full%20Subtractor) essentially computes the following [Boolean function](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md):

|$x$|$y$|$b_{\text{in}}$||$d$|$b_{\text{out}}$|
|:--:|:--:|:--:|:--:|:--:|:--:|
|$0$|$0$|$0$||$0$|$0$|
|$0$|$0$|$1$||$1$|$1$|
|$0$|$1$|$0$||$1$|$1$|
|$0$|$1$|$1$||$0$|$1$|
|$1$|$0$|$0$||$1$|$0$|
|$1$|$0$|$1$||$0$|$0$|
|$1$|$1$|$0$||$0$|$0$|
|$1$|$1$|$1$||$1$|$1$|

From the above [truth table](../../Mathematics/Algebra/Boolean%20Algebra/Truth%20Tables.md), we can derive [expressions](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md) for $d$ and $b_{\text{out}}$. Note that $d$ is high when an odd number of inputs are high, and $b_{\text{out}}$ logic can be constructed by combining two half subtractors:

$$\begin{aligned}d & = x \oplus y \oplus b_{\text{in}} \\ b_{\text{out}} & = (\neg x \land y) \lor (\neg(x \oplus y) \land b_{\text{in}})\end{aligned}$$

>[!EXAMPLE]- Example: Logic Gate Implementation
>
>Using the above [expressions](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md), we can construct a [full subtractor](#Full%20Subtractor) via [logic gates](./Logic%20Gates/Logic%20Gates.md):
>
>![Full Subtractor via Logic Gates](./res/Subtractors/Full%20Subtractor%20via%20Logic%20Gates.svg)
>

### Ripple-Borrow Subtractor

A **ripple-borrow subtractor** is a [digital circuit](./Digital%20Circuits.md) which can calculate the difference $x - y$ of two $n$-bit numbers either in [unsigned integer representation](../../Computer%20Science/Data%20Representation/Integers.md) or in [two's complement representation](../../Computer%20Science/Data%20Representation/Integers.md#Two's%20Complement). It is constructed by chaining $n$ [full subtractors](./Subtractors.md):

![Ripple-Borrow Subtractor](./res/Ripple-Borrow%20Subtractor.svg)

When $x$ and $y$ are [unsigned integers](../../Computer%20Science/Data%20Representation/Integers.md):

- If the final $b_{\text{out}}$ is $0$, then $x \ge y$ and $d$ is the [unsigned integer representation](../../Computer%20Science/Data%20Representation/Integers.md) of the difference $x - y$.
- If the final $b_{\text{out}}$ is $1$ (underflow), then $x \lt y$ and $d$ is the [two's complement representation](../../Computer%20Science/Data%20Representation/Integers.md) of the difference $x - y$.

When $x$ and $y$ are [two's complement integers](../../Computer%20Science/Data%20Representation/Integers.md#Two's%20Complement):

- If $b_{\text{in}}$ and $b_{\text{out}}$ of the most-significant [full subtractor](./Subtractors.md) are different, then overflow has occurred and $d$ is invalid.
- If $b_{\text{in}}$ and $b_{\text{out}}$ of the most-significant [full subtractor](./Subtractors.md) are equal, then $d$ is the the difference $x - y$ as a [two's complement integer](../../Computer%20Science/Data%20Representation/Integers.md#Two's%20Complement).

## Adder Implementation

When using [two's complement](../../Computer%20Science/Data%20Representation/Integers.md#Two's%20Complement), the subtraction $a - b$ is equivalent to the addition of the [two's complement](../../Computer%20Science/Data%20Representation/Integers.md#Two's%20Complement) of $b$ to $a$. This means that we can easily implement a [subtractor](./Subtractors.md) by slightly modifying a [full adder](./Adders.md#Full%20Adders):

![Subtractor via Adder](./res/Subtractors/Subtractor%20via%20Adder.svg)

When $\overline{\text{add}}/\text{sub} = 0$, the [multiplexer](./Multiplexers.md) forwards $b$ to the [adder](./Adders.md) and the addition $a + b$ is performed. When $\overline{\text{add}}/\text{sub} = 1$, the [multiplexer](./Multiplexers.md) forwards the [bitwise negation](./Logic%20Gates/Logic%20Gates.md) $\overline{b}$ of $b$ to [full adder](./Adders.md#Full%20Adders). Furthermore, $c_{\text{in}}$ is set to $1$ which is equivalent to adding $1$ to $\overline{b}$. This means that the [adder](./Adders.md#Full%20Adders) essentially adds the [two's complement](../../Computer%20Science/Data%20Representation/Integers.md#Two's%20Complement) of $b$ to $a$, resulting in the subtraction $a - b$.