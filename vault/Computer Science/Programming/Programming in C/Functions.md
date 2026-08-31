---
tags:
    - programming-in-c
    - programming
    - computer-science
---

# Functions

[C](./The%20C%20Programming%20Language.md) provides basic support for [functions](TODO). Before a [function](./Functions.md) can be used, it must be **declared**:

```c
return-type name(param-type-1, param-type-2, ...);
```

The `return-type` is the [data type](./Data%20Types/Data%20Types.md) of the [function](./Functions.md)'s return value. If the [function](./Functions.md) does not return anything, we use `void` for `return-type`.

The `param-type`s are the [data types](./Data%20Types/Data%20Types.md) of the [function](./Functions.md)'s parameters. We can optionally provide names for these parameters as well:

```c
return-type name(param-type-1 param1, param-type-2 param2, ...);
```

If the [function](./Functions.md) does not take any parameters, then we just put `void` between the parentheses. 

We also need to provide a **definition** for the [function](./Functions.md) which contains the code that the [function](./Functions.md) executes:

```c
return-type name(param-type-1 param1, param-type-2 param2, ...) {
	// Code
}
```

A definition also counts as a declaration, so we do not need to explicitly declare a  [function](./Functions.md) if we have defined it. 

>[!EXAMPLE]- Example
>
>TODO
>