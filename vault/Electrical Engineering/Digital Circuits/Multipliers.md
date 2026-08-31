---
tags:
    - digital-circuits
    - electrical-engineering
---

# Multipliers

>[!DEFINITION] Definition: Multiplier
>
>An $n\times n$**-multiplier** is a [digital circuit](./Digital%20Circuits.md) which calculates the $2n$-bit product of two unsigned $n$-bit binary integers.
>

## Integer Multipliers

### Array Multiplier

A [multiplier](./Multipliers.md) can be implemented via a [combinational circuit](./Digital%20Circuits.md#Combinational%20Circuits) which computes the following algorithm:

>[!ALGORITHM] Algorithm: Multiplication of Unsigned $n$-bit Binary Integers
>
>We want to compute the product $A \cdot B$ of two $n$-bit unsigned binary integers $A = a_{n-1} \cdots a_0$ and $B = b_{n - 1}\cdots b_0$.
>
>1. We compute $n$ partial products $C_{n-1}, \dotsc, C_0$, where the $j$-th bit $C_{k,j}$ of $C_k$ is given by the following product:
>
>$$
>C_{k, j} = a_k \cdot b_j
>$$
>
>2. We bit-shift the $k$-th partial product $C_k$ to the left by $k$ bits, adding trailing $0$s to obtain $C_k'$.
>3. The final product is the sum of the bit-shifted partial products:
>
>$$
>A \cdot B = \sum_{k = 0}^{n-1} C_k'
>$$
>
>![Combinational Multiplication Algorithm](./res/Multipliers/Combinational%20Multiplication%20Algorithm.svg)
>

At the bit level, multiplication is equivalent to a [conjunction](../../Mathematics/Algebra/Boolean%20Algebra/Conjunction.md):

|$a$|$b$|$a \cdot b$|
|:--:|:--:|:--:|
|$0$|$0$|$0$|
|$1$|$0$|$0$|
|$0$|$1$|$0$|
|$1$|$1$|$1$|

We can thus compute the above algorithm using [AND gates](./Logic%20Gates/Logic%20Gates.md) and [adders](./Adders.md):

>[!EXAMPLE]- Example: $4\times 4$-Multiplier (Combinational)
>
>![Combinational Multiplier](./res/Multipliers/Combinational%20Multiplier.svg)
>

[Combinational multipliers](#Combinational%20Multipliers) are expensive and slow because they require $\approx n^2$ [gates](./Logic%20Gates/Logic%20Gates.md) for computing the product of two $n$-bit numbers.

### Sequential Multipliers

We can also implement [multipliers](./Multipliers.md) via a [sequential circuit](./Digital%20Circuits.md#Combinational%20Circuits).

>[!ALGORITHM] Algorithm: Sequential Multiplication Algorithm
>
>We want to compute the product of two $n$-bit unsigned binary integers $A = A[n-1] \cdots A[0]$ and $B = B[n - 1] \cdots B[0]$.
>
>1. Initialize a $(2n+1)$-bit number $PR$ by padding $B$ with $n+1$ leading zeros, i.e. $PR \leftarrow \underset{n+1}{\underbrace{0\cdots0}}B[n - 1] \cdots B[0]$.
>2. Check the least significant bit of $PR$:
>    - If $PR[0] = 1$, then add $PR[2n] PR[2n - 1] \cdots PR[n]$ to $A$ and store the result in $PR[2n+1] PR[2n] \cdots PR[n]$. Shift $PR$ one bit to the right, filling the gap with a zero.
>
>$$
>\begin{aligned}
>&PR[2n+1] PR[2n] \cdots PR[n] \leftarrow A + PR[2n] PR[2n - 1] \cdots PR[n] \\ 
>&PR \leftarrow \operatorname{ShiftRight}(PR, 1) 
>\end{aligned}
>$$
>    - If $PR[0] = 0$, then just shift $PR$ one bit to the right, filling the gap with a zero.
>
>$$
>PR \leftarrow \operatorname{ShiftRight}(PR, 1) 
>$$
>
>3. Repeat Step 2 $n$ times. At the end, $PR$ will contain the product of $A$ and $B$.
>

This algorithm can be realized using a $(2n+1)$-bit [parallel right shift register](./Registers.md) for $PR$, a [register](./Registers.md) for the multiplicand, an [adder](./Adders.md), two [multiplexers](./Multiplexers.md) and some control circuitry:

![Sequential Multiplier Circuit](./res/Sequential%20Multiplier%20Circuit.svg)

The control circuitry is responsible for realizing the following [state machine](../../Computer%20Science/Theoretical%20Computer%20Science/Finite%20State%20Machines.md):

![Sequential Multiplier State Machine](./res/Sequential%20Multiplier%20State%20Machine.svg)

This can be implemented fairly easily. First, we assign a unique number to each state:

|State|Number|
|:--:|:--:|
|Initialization 1|0|
|Initialization 2|1|
|Addition 1|2|
|Addition 2|3|
|Shift 1|4|
|Shift 2|5|
|Finished|6|

We need a 3-bit [register](./Registers.md) $\text{State}$ to store the number of the circuit's current state and a $\lceil \log_2 n \rceil$-bit [register](./Registers.md) $\text{Round}$ to store the current round. The four outputs of the control circuit are $\text{clk\_product}$, $\overline{\text{init}}\text{ / shift}$, $\text{multiplexer}$ and $\text{clk\_multiplicand}$ and they can be determined using a [multiplexer](./Multiplexers.md) which switches on the $\text{State}$ [register](./Registers.md):

![Sequential Multiplier Control 1](./res/Sequential%20Multiplier%20Control%201.svg)

The `x`s indicate that the value is irrelevant - we can choose either $0$ or $1$ and nothing would change. 

We also need circuitry which the determines the next value of the $\text{State}$ [register](./Registers.md). To achieve this, we construct the [transition table](TODO) of the [state machine](TODO):

|Current State|$PR[0]$|$\text{Round}_n$|Next State|
|:--:|:--:|:--:|:--:|
|Initialization 1|Irrelevant|Irrelevant|Initialization 2|
|Initialization 2|0|Irrelevant|Shift 1|
|Initialization 2|1|Irrelevant|Addition 1|
|Addition 1|Irrelevant|Irrelevant|Addition 2|
|Addition 2|Irrelevant|Irrelevant|Shift 1|
|Shift 1|Irrelevant|Irrelevant|Shift 2|
|Shift 2|$0$|$0$|Shift 1|
|Shift 2|$1$|$0$|Addition 1|
|Shift 2|Irrelevant|$1$|Finished|

Apart from `Initialization 2` and `Shift 1`, each state has only one possible next state. This means that a [multiplexer](./Multiplexers.md) is a good candidate for determining the next state based on the current state:

![Sequential Multiplier State Transition Circuit](./res/Sequential%20Multiplier%20State%20Transition%20Circuit.svg)

The last thing we need to implement is circuitry which increments the $\text{Round}$ [register](./Registers.md). We want this to happen whenever we are in the `Shift 1` state:

![Sequential Multiplier Round Incrementer](./res/Sequential%20Multiplier%20Round%20Incrementer.svg)