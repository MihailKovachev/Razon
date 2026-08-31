---
title: Strings
tags:
    - programming-in-c
    - programming
    - computer-science
---

# Strings

The [C Programming Language](../The%20C%20Programming%20Language.md) does not have a separate [data type](./Data%20Types.md) for strings. Instead, a [string](./Strings.md) can be represented either as an [array](./Arrays.md) of [characters](./Characters.md) or as a [pointer](./Pointers.md) to a [character](./Characters.md). 

By convention, every [string](./Strings.md) must end with a [null terminator](./Characters.md). Forgetting this is a common source of bugs because all [standard library](TODO) [functions](../Functions.md) dealing with [strings](./Strings.md) rely on it to know when a [string](./Strings.md) ends.

[String](./Strings.md) literals are given between double quotation marks: `"string literal goes here"`. To represent [special characters](./Characters.md), we use their [escape sequences](./Characters.md). A [null terminator](./Characters.md) is automatically inserted at the end of each literal by the [compiler](TODO).

A [string](./Strings.md) literals can be directly assigned to an [array](./Arrays.md) of [characters](./Characters.md) or to a [pointer](./Pointers.md) to a [character](./Characters.md):

```c
char helloAsArray[6] = "Hello"; // 6 instead of 5 because of the implicit null-terminator
char *helloAsPointer = "Hello";
```

When assigning to an [array](./Arrays.md) of [characters](./Characters.md), the [array](./Arrays.md) can be any number so long as it can fit the [string](./Strings.md) literal:

```c
char helloAsArray[27] = "Hello"; // just as valid
```

The literals themselves are stored in the resulting binary file.

## Operations

The [header](TODO) `<string.h>` provides functionality for various operations with [strings](./Strings.md).

