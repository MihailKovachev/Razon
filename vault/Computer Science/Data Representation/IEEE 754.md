---
tags:
    - computer-science
---

# IEEE 754

The **IEEE Standard for Floating-Point Arithmetic** (**IEEE 754**) describes a specific standard for representing [real numbers](../../Mathematics/Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md).

## Format

The standard divides a sequence of bits into three parts, each of a fixed bit length: a **sign bit** ($S$), a **biased exponent** ($E$) and a **trailing significand field** ($T$):

![IEEE 754 Format](./res/IEEE%20754%20Format.svg)

- The [sign bit](#Format) $S$ determines whether the number is negative or non-negative. If $S = 1$, then the number is negative and if $S = 0$, then the number is non-negative. 
- The [trailing significand field](#Format) $T$ is treated as number in the range $[0, 1)$ by assigning $\frac{1}{2}$, $\frac{1}{4}$, etc. to each of its bits. 

![](./res/IEEE%20754%20Mantissa.svg)

- The [biased exponent](#Format) $E$ is treated as an [unsigned integer](./Integers.md).

![](./res/IEEE%20754%20Exponent.svg)

The standard defines several formats and a **bias** for each format which is used in the calculation of its value:

|Format|Description|Exponent|Fraction|Bias|
|:--:|:--:|:--:|:--:|:--:|
|binary16|half-precision, 16 bits|5 bits|10 bits|$K = 15$|
|binary32|single precision, 32 bits|8 bits|23 bits|$K = 127$|
|binary64|double precision, 64 bits|11 bits|52 bits|$K = 1023$|
|binary128|quadruple precision, 128 bits|15 bits|112 bits|$K = 16383$|

The value represented by an [IEEE 754 floating-point number](./IEEE%20754.md) is given by the following table:

|$S$|$E$|$T$|Value|
|:--:|:--:|:--:|:--:|
|$0$|$0 \cdots 0$|$0 \cdots 0$|$+0$|
|$1$|$0 \cdots 0$|$0 \cdots 0$|$-0$|
|$0$|$1 \cdots 1$|$0 \cdots 0$|$+\infty$|
|$1$|$1 \cdots 1$|$0 \cdots 0$|$-\infty$|
|Any|$1\cdots 1$|$\ne 0\cdots 0$|$\mathrm{NaN}$ (not a number)|
|Any|$0 \cdots 0$|$\ne 0 \cdots 0$|$(-1)^\text{S} \times (T) \times 2^{1 - K}$ (**denormalized number** or **subnormal number**)|
|Any|$\ne 0\cdots 0$ and $\ne 1 \cdots 1$|Any|$(-1)^\text{S} \times (1 + T) \times 2^{E - K}$ (**normalized number**)|

>[!DEFINITION] Definition: True Exponent
>
>The value of $1 - K$ (for [subnormal numbers](#Format)) or $(E - K)$ (for [normalized numbers](#Format)) is known as the **true exponent** or **effective exponent**.
>

>[!DEFINITION] Definition: Significand / Mantissa
>
>The value of $T$ (for [subnormal numbers](#Format)) or $(1 + T)$ (for [normalized numbers](#Format)) is known as the **significand** or **mantissa**.
>

Calculating the value in this way allows for the representation of both very large and very small numbers. However, the gap between representable numbers increases (absolute precision drops) as the number moves farther away from zero.

Since $E$ is an [unsigned integer](./Integers.md), it can only take on non-negative values. To allow for negative exponents, we subtract the [bias](#Format) $K$ from $E$, which is equal to exactly half the largest representable [unsigned integer](./Integers.md) by $E$ (rounded down):

- If $K \gt E$, then the [true exponent](#Format) is negative. 
- If $K = E$, then the [true exponent](#Format) is zero.
- If $K \lt E$, then [true exponent](#Format) is positive. 

[Subnormal numbers](#Format) are used to represent numbers which are very close to zero. For [normalized number](#Format), the implicit $1$ added to the $\text{fraction}$ allows for an extra bit of precision at virtually no extra cost.

## Rounding

Each of the three formats [IEEE 754 formats](#Format) `binary32`, `binary64` and `binary128` effectively defines a [subset](../../Mathematics/Set%20Theory/Sets.md) of the [real numbers](../../Mathematics/Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) which can be represented by it. Representing a [real number](../../Mathematics/Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) outside this [subset](../../Mathematics/Set%20Theory/Sets.md) is done by rounding it to a representable [real number](../../Mathematics/Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md). The [IEEE 754](#Format) standard defines several ways to do this, which are known as **rounding modes**.

>[!ALGORITHM] Algorithm: Round to Nearest, Ties to Even
>
>We are given a specific format (`binary16`, `binary32`, `binary64` or `binary128`) and a [real number](../../Mathematics/Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) $r \in \mathbb{R}$ which is not representable in the specified format and want to find out how $r$ will be rounded:
>
>1. Round $r$ to the nearest representable value:
>
>    - If $r$ has to be rounded to $0$, its sign is preserved.
>
>2. If $r$ is exactly halfway between two representable values, then round it to the value which has $0$ as the least-significant bit of its [fraction](#Format).
>
>    - If $r$ is exactly halfway between the largest representable finite number and the theoretical next finite value (exceeding the range), then it is rounded to $+\infty$.
>    - If $r$ is exactly halfway between the smallest representable finite number and the theoretical next finite value (exceeding the range), then it is rounded to $-\infty$.
>
>3. $\mathrm{NaN}$ cannot be the result of a rounding operation.
>
>>[!EXAMPLE]-
>>
>>TODO
>>
>

TODO: Describe the other modes

## Operations

>[!ALGORITHM] Algorithm: Checking for Equality
>
>To check if two [IEEE 754 numbers](#Format) are equal according to the standard:
>
>1. Positive zero is numerically equal to negative zero, i.e. $+0 == -0$ is true.
>2. $\mathrm{NaN}$ is never equal to $\mathrm{NaN}$, i.e. $\mathrm{NaN} == \mathrm{NaN}$ is false.
>3. In all other cases, two [IEEE 754 numbers](#Format) are equal if and only if they are bitwise equal.
>

>[!ALGORITHM] Algorithm: Addition
>
>We want to compute the addition $A + B$ of two numbers $A$ and $B$ in the same [IEEE 754 format](#Format). Let $S_A$ and $S_B$ be their [sign bits](#Format), let $E_A$ and $E_B$ be their [biased exponents](#Format), let $T_A$ and $T_B$ be their [trailing significant fields](#Format) and let $K$ be the common [bias](#Format).
>
>0. Check for special values:
>
>    - If at least one of the operands is $\mathrm{NaN}$, the result is also $\mathrm{NaN}$.
>    - If both operands are [infinity](#Format) with the same sign, the result is that [infinity](#Format).
>    - If the operands are [infinity](#Format) but with different signs, the result is $\mathrm{NaN}$.
>    - If one operand is finite and the other is an [infinity](#Format), the result is that [infinity](#Format).
>    - If both operands are zero with the same sign, the result is zero with that sign.
>    - If both operands are zero but with opposite signs, the result is $+0$ (assuming default rounding).
>
>1. Calculate the [significands](#Format) $M_A$ and $M_B$ by appending the implicit hidden bit to $T_A$ and $T_B$ (1 for normalized numbers, 0 for subnormals).
>
>2. Calculate $\delta = E_A - E_B$. Initialize the result [biased exponent](#Format) $E_{\text{res}} = \max(E_A, E_B)$.
>
>    - If $\delta > 0$, then right-shift $M_B$ by $\delta$ positions: $M_B \leftarrow M_B \times 2^{-\delta}$.
>    - If $\delta < 0$, then right-shift $M_A$ by $|\delta|$ positions: $M_A \leftarrow M_A \times 2^{-|\delta|}$.
>    - If $\delta = 0$, then proceed.
>
>3. Add or subtract the [significands](#Format) and determine the [sign bit](#Format) of the result.
>
>    - If $S_A = S_B$, then add the [significands](#Format): $M_{\text{res}} \leftarrow M_A + M_B$. The [sign bit](#Format) is preserved: $S_{\text{res}} = S_A$.
>    - If $S_A \neq S_B$, then subtract the significands: $M_{\text{res}} = |M_A - M_B|$.
>
>        - If $M_{\text{res}} = 0$, then $S_{\text{res}} = +$ (for default Round to Nearest).
>        - If $M_A > M_B$, then $S_{\text{res}} = S_A$.
>        - If $M_B > M_A$, then $S_{\text{res}} = S_B$.
>
>4. Normalize $E_{\text{res}}$ and $M_{\text{res}}$ to comply with the [IEEE 754 format](#Format):
>
>    - If $M_{\text{res}} = 0$, then set $E_{\text{res}} = 0$ and $T_{\text{res}} = 0$ (the result is a signed zero).
>    - If $M_{\text{res}} \ge 2$, then right-shift $M_{\text{res}}$ by 1 position and increment $E_{\text{res}}$ by 1: $M_{\text{res}} \leftarrow M_{\text{res}} \times 2^{-1}$ and $E_{\text{res}} \leftarrow E_{\text{res}} + 1$.
>    - If $M_{\text{res}} < 1$ and $M_{\text{res}} > 0$, then repeatedly left-shift $M_{\text{res}}$ and decrement $E_{\text{res}}$ until $M_{\text{res}} \ge 1$ or $E_{\text{res}}$ reaches the minimum valid [exponent](#Format) (handling subnormal results).
>
>5. Round the [significand](#Format) $M_{\text{res}}$ to the target precision using the appropriate rounding mode (e.g., Round to Nearest, Ties to Even).
>
>    - If rounding causes a carry that makes $M_{\text{res}} \ge 2$, then right-shift $M_{\text{res}}$ by 1 position and increment $E_{\text{res}}$ by 1.
>    - Check for overflow: If $E_{\text{res}}$ exceeds the maximum [exponent](#Format) value, set $E_{\text{res}}$ to all ones and $T_{\text{res}} = 0$ (the result is $\pm \infty$).
>    - Check for underflow: If $E_{\text{res}}$ becomes smaller than the minimum normalized [exponent](#Format) and $M_{\text{res}}$ cannot be normalized, the result is subnormal.
>
>6. Construct the final result [fraction](#Format) $T_{\text{res}}$.
>
>    - If the result is normalized ($M_{\text{res}} \ge 1$), remove the leading hidden bit: $T_{\text{res}} \leftarrow M_{\text{res}} - 1$.
>    - If the result is subnormal ($M_{\text{res}} < 1$), the leading bit is already 0, so $T_{\text{res}} \leftarrow M_{\text{res}}$.
>    - Combine $S_{\text{res}}$, $E_{\text{res}}$, and $T_{\text{res}}$ into the final bit string.

>[!ALGORITHM] Algorithm: Subtraction
>
>The subtraction $A - B$ is calculated as the [addition](#Operations) of $A$ and $B$ with a flipped [sign bit](#Format).
>