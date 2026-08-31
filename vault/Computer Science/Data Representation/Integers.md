---
tags:
    - computer-science
---

# Integers

## Fixed-Point Numbers

**Fixed-point numbers** are a way of representing [real numbers](../../Mathematics/Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) by fixing the position of the decimal point in advance and using a [positional numeral system](../../Mathematics/Algebra/Fields/The%20Real%20Numbers/Positional%20Numeral%20Systems.md). Given $n$ places for [digits](../../Mathematics/Algebra/Fields/The%20Real%20Numbers/Positional%20Numeral%20Systems.md), the idea is to write a [real number](../../Mathematics/Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) $v$ in the form

$$v = (d_{n-1} \cdot b^{n-1} + \cdots + d_1 \cdot b^1 + d_0 \cdot b^0) \cdot b^r,$$

where $d_k$ is the [digits](../../Mathematics/Algebra/Fields/The%20Real%20Numbers/Positional%20Numeral%20Systems.md) at the $k$-th place going right to left, $b$ is the chosen [base](../../Mathematics/Algebra/Fields/The%20Real%20Numbers/Positional%20Numeral%20Systems.md) and $r \in \mathbb{Z}$ is the **radix** which determines the position of the decimal point.

>[!NOTE]
>
>Despite the name, $r$ has nothing to do with the [base](../../Mathematics/Algebra/Fields/The%20Real%20Numbers/Positional%20Numeral%20Systems.md) $b$. 
>

The radix $r$ determines the position of the decimal point in the following way:
- When $r = 0$, the number is multiplied with $b^0 = 1$, i.e. it remains just $v = d_{n-1} \cdot b^{n-1} + \cdots + d_1 \cdot b^1 + d_0 \cdot b^0$, meaning that $v$ is an integer.
- When $r \gt 0$, the number is multiplied with $b^r \gt 1$. Its digits are shifted $r$ places towards the most significant digit and the gaps are filled with zeros. The decimal point disappears, which means that we sacrifice precision but can represent larger numbers.
- When $r \lt 0$, the number is multiplied with $b^r \lt 1$ . The decimal point moves $r$ places towards the most significant digit. We increase the precision, but the largest representable number becomes smaller.

The distance between consecutive representable numbers using this format is constant and is equal to $b^{r}$.

## Algebraic Sign

So far, the [fixed-point numbers](./Integers.md) format can only represent non-negative (**unsigned**) numbers. We thus need to find a way to extend it to allow for negative (**signed**) numbers. There are three main ways to do this when $b = 2$:
- sign and absolute value;
- ones' complement;
- twos' complement.

### Sign and Absolute Value

In the **sign and absolute value** system, we treat the first [bit](TODO) as the sign: $1$ indicates a negative sign, while $0$ indicates a positive sign. The rest of the [bits](TODO) are treated as the absolute value of the number. 

![](./res/Fixed-Point%20Sign%20and%20Abs.svg)

For example, $0010_2$ represents $2$, while $1010_2$ represents $-2$.

The main advantage of this format is its simplicity. However, it comes with the problem that there are always two ways to represent zero, namely $10\cdots 0_2$ and $00\cdots 0_2$. This makes computations more difficult for computers.

### Ones' Complement

In the **ones' complement** system, the negative of a number is constructed by inverting all its [bits](TODO). For example, $0010_2$ represents $2$, while $1101_2$ represents $-2$. This has the advantage that addition and subtraction work in (mostly) the same way as usual:

$$\begin{array}{ccccc} 0011_2 & + & 0010_2 & = & 0101_2 \\ 3 & + & 2 & = & 5 \end{array}$$

$$\begin{array}{ccccc} 1011_2 & + & 0010_2 & = & 1101_2 \\ -4 & + & 2_{10} & = & -2 \end{array}$$

However, this format still has the problem that there are two ways to represent zero, namely $1\cdots 1$ and $0 \cdots 0$. Moreover, adding $1\cdots 1_2$ ($-0$) to $00\cdots 1_2$ ($1$) results in $0\cdots 0_2$ ($0$) instead of $00\cdots 1_2$ ($1$).

Range:

$$- (2^{n-1} - 1)\cdot 2^r,\dotsc,-0,+0,\dotsc,(2^{n-1} - 1)\cdot 2^r$$

### Two's Complement

In the **two's complement** system, the negative of a number is built by first constructing its [ones' complement](#Ones'%20Complement) and then adding the $1_2$ to it. For example, $0010_2$ represents $2$, while $1110_2$ represents $-2$.

This solves all problems with the double representation of zero and so addition and subtraction always work as possible. The only problem is that it makes the positive and negative numbers asymmetric: for any fixed number of [bits](TODO), the total number of representable negative numbers is always greater by one than the total number of representable positive numbers.

>[!IMPORTANT]
>
>All modern computers use [two's complement](#Two's%20Complement).
>

Range:

$$-2^{n-1} \cdot 2^r,\dotsc,0,\dotsc,(2^{n-1} - 1)\cdot 2^r$$
