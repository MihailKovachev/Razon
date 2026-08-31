---
title: Boolean
tags:
    - programming-in-c
    - programming
    - computer-science
---

# Boolean

Since the [C23](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3220.pdf) standard, the [C programming language](../The%20C%20Programming%20Language.md) has the [data type](TODO) `bool` for storing [Boolean values](TODO). It is guaranteed to be large enough to hold one of the two values `true` or `false`:

```c
bool example = true;
example = false;
```

Typically, a [boolean](#Boolean) is 8 bits, but this is not guaranteed.

In practice, `bool` is not used often. Instead, [integers](#Integers) are used with $0$ being treated as `false` and everything else as `true`.