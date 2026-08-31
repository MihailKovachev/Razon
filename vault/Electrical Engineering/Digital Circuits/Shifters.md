---
tags:
    - digital-circuits
    - electrical-engineering
---

# Barrel Shifters

A **barrel shifter** is a [combinational circuit](TODO) capable of shifting a an $n$-bit value by $0 \le s \lt n$ places in a single [clock cycle](./Circuit%20Triggering.md).

>[!ALGORITHM] Algorithm: Left-Shift Barrel Shifter Implementation
>
>We have an $n$-bit input $X = x_{n-1}\cdots x_0$ and want to shift its value $s$ places ($0 \le k \lt n$) to the left.
>
>1. Represent $s$ as a $m = \lceil \log_2 n \rceil$-bit number $s_{q-1}\cdots s_{0}$.
>2. Construct $m$ layers of $2:1$ [multiplexers](./Multiplexers.md). Each layer should have $n$ [multiplexers](./Multiplexers.md).
>    - Connect the [selector lines](./Multiplexers.md) of all [multiplexers](./Multiplexers.md) in the $k$-th layer ($k \in \{0, \dotsc, q-1\}$) to $s_k$.
>3. For the [multiplexer](./Multiplexers.md) at row $i \in \{0,\dotsc,n-1\}$ and column $j \in \{0,\dotsc,m\}$:
>    - Connect the $0$ input to the output of the [multiplexer](./Multiplexers.md) at row $i$ and column $j-1$. For $j = 0$, connect the $0$ input to $x_i$.
>    - Connect the $1$ input to the output of the [multiplexer](./Multiplexers.md) at row $i - 2^j$ and column $j-1$. For $i - 2^j \lt 0$, connect the $1$ input either to a constant $0$ or a constant $1$ depending on what you want to fill the new bits with.
>
>>[!EXAMPLE]-
>>
>>![Barrel Shifter Example](./res/Barrel%20Shifter%20Example.svg)
>>
>