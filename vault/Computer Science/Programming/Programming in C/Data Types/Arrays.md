---
tags:
    - programming-in-c
    - programming
    - computer-science
---

# Arrays

An **array** in the [C programming language](../The%20C%20Programming%20Language.md) is a sequence of values of the same [data type](./Data%20Types.md). 

The syntax for [declaring](../Variables.md) an [array](./Arrays.md) is the following:

```c
data-type array-name[array-length];
```

- The `data-type` is the [data type](./Data%20Types.md) of the elements in the sequence. 
- The `array-name` is the name of the sequence.
- The `array-length` is the total number of elements in the sequence.

To access an element in the [array](./Arrays.md), we use the following syntax:

```c
array-name[index]
```

Here, `index` is the index of the element (starting at $0$) which we want to access. Trying to access an element at an `index >= array-length` is undefined behavior.

## Decay

[Arrays](./Arrays.md) are very similar to [pointers](./Pointers.md) which allows for an [implicit conversion](./Casting.md) of the former to the latter. Specifically, [converting](./Casting.md) an [array](./Arrays.md) of elements of a specific [data type](./Data%20Types.md) returns the address of the first element in the [array](./Arrays.md) as a [pointer](./Pointers.md) to the [data type](./Data%20Types.md). This process is known as **array decay** because the information about the size of the [array](./Arrays.md) is lost.

Most commonly, [decay](#Decay) happens when trying to pass an [array](./Arrays.md) to a [function](../Functions.md), which is impossible to do directly. The syntax `data-type array-name[]` as a [parameter declaration](../Functions.md) in a [function](../../../../Mathematics/Analysis/Functions/Functions.md) is just [syntactic sugar](TODO) for `data-type *array-name`. This means that you can only pass a [pointer](./Pointers.md) to the first element in the [array](./Arrays.md).