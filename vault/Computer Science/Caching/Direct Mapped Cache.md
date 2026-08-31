---
tags:
    - computer-science
---

# Direct Mapped Cache

The entire address space consisting of $2^n$ addresses is split into $2^k$ blocks and each $n$-bit memory address is logically divided into three parts: an $f$-bit **index**, a $b$-bit **offset** and a $k$-bit **tag**.

![Direct Mapped Cache Address](./res/Direct%20Mapped%20Cache%20Address.svg)

The [index](./Direct%20Mapped%20Cache.md) and the [offset](./Direct%20Mapped%20Cache.md) map the memory address to a cache address. Specifically, the [index](./Direct%20Mapped%20Cache.md) maps the memory address to a specific cache line and the [offset](./Direct%20Mapped%20Cache.md) maps the memory addresses to a specific byte within the cache line.

When a b

The [tag](./Direct%20Mapped%20Cache.md) of the address address determines the [memory block](./Direct%20Mapped%20Cache.md) to which this address belongs. 

When reading data from a memory address, the 

