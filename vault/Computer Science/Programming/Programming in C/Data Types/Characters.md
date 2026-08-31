---
title: Characters
tags:
    - programming-ing-c
    - programming
    - computer-science
---

# Characters

[C](../The%20C%20Programming%20Language.md) has three data types for representing [characters](TODO): `char`, `signed char` and `unsigned char`. The three are the same size and each is guaranteed to be large enough to hold a single value from the basic execution character set. Typically, this size is 8 bits, but this is not guaranteed. 

```c
char letter = 'a';
letter += 1; // letter is now 'b'
```

The types are treated the same way as [integers](#Integers), hence the `signed` and `unsigned` variants. The plain `char` type can be either `signed` or `unsigned`, depending on the compiler's implementation.