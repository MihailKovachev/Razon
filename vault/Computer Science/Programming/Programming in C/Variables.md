---
title: Variables
tags:
    - programming-in-c
    - programming
    - computer-science
---

# Variables

[C](./The%20C%20Programming%20Language.md) is a [statically typed](TODO) [programming language](../index.md) and so the [data type](TODO) of every [variable](TODO) must be known at [compile-time](TODO).

A [variable](./Variables.md) must be **declared** before it can be used:

```c
data-type variable_name;
```

Multiple [variables](./Variables.md) of the same [data type](TODO) can also be declared on the same line by listing their names separated by commas:

```c
data-type variable1, variable2, ...;
```

Names of [variables](./Variables.md) can only contain uppercase and lowercase letters, underscores and numbers, but cannot begin with a number. They also can't be reserved keywords like `for`, `char`, etc.

The first time a value is assigned to a [variable](./Variables.md) is known as its **initialization**:

```c
int var; // Declaration
var = 2; // Initialization
```

[Declarations](./Variables.md) and [initializations](./Variables.md) can also be combined on a single line:

```c
double pi = 3.14, e = 2.72; // Declaration and initialization
```

If a [variable](./Variables.md) is [declared](./Variables.md) in one file but it is [initialized](./Variables.md) in another, its [declaration](./Variables.md) must be marked with the `extern` keyword:

```c
// other.cpp
double pi = 3.14;

// main.cpp
extern double pi; // extern tells the compiler to look for the initialization of pi in the other files
double double_pi = pi * 2;
```