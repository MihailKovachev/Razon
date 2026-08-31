---
tags:
    - programming-in-c
    - programming
    - computer-science
---

# Structures

**Structures** in the [C programming language](../The%20C%20Programming%20Language.md) are user-defined [data types](./Data%20Types.md) which allow for the grouping of multiple values of different [data types](./Data%20Types.md) in a single unit. 

The syntax for declaring a [structure](./Structures.md) is the following:

```c
struct StructTag {
    data-type-1 memberName1;
    data-type-2 memberName2;
    // ...
};
```

The syntax for declaring a [structure](./Structures.md) [variable](../Variables.md) is the following:

```c
struct StructTag variableName; 
```

## Memory Layout

The order of the members of a [structure](./Structures.md) in memory is the same as their order in the declaration. However, **padding bytes** are inserted by the [compiler](TODO) to enforce the [alignment](TODO) of each member. The values of these bytes is undefined.

