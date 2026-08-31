---
title: Pointers
tags:
    - programming-in-c
    - programming
    - computer-science
---

# Pointers

[C](../The%20C%20Programming%20Language.md) provides a special [data type](./Data%20Types.md) known as a **pointer** for storing memory addresses. There are two types of [pointers](./Pointers.md) depending on how the memory at the stored address should be treated:
- A **pointer to a variable** stores the memory address of a [variables](../../../System%20Internals/Windows/PowerShell/Variables.md).
- A **pointer to a function** or a **function pointer** stores the memory address of a [function](../Functions.md) (since the code of [functions](../Functions.md) is stored in memory as well).

Declaring a [pointer to variable](./Pointers.md) is done in the following way:

```c
data-type *pointer;
```

>[!EXAMPLE] Example: Pointer to Variable
>
>The following is a declaration of a [pointer](./Pointers.md) to `int`:
>
>```c
>int *ptr;
>```
>
>>[!IMPORTANT] Important
>>
>>Each [pointer](./Pointers.md) must have an asterisk (`*`) before its name:
>>
>>```c
>>int *ptr, notAPointer;
>>```
>>
>>Here, `ptr` is a [pointer](./Pointers.md) to `int`, but `notAPointer` is just an `int`.
>>
>

Declaring a [function pointer](./Pointers.md) is done in the following way:

```c
return-type (*pointer)(param-type-1, param-type-2, ...);
```

You can optionally give names to the parameters as well:

```c
return-type (*pointer)(param-type-1 param1, param-type-2 param2, ...);
```

>[!EXAMPLE] Example: Pointer to Function
>
>The following is a declaration of a [pointer](./Pointers.md) `ptr` to a [function](../Functions.md) returns an `int` and takes two parameters - a `double` and a [pointer](./Pointers.md) to `float`:
>
>```c
>int (*ptr)(double, float*);
>int (*ptr)(double doubleParam, float *floatPointerParam);
>```
>
>The following is a declaration of a [pointer](./Pointers.md) `ptr` to a [function](../Functions.md) which returns nothing and takes one parameter which is another [function pointer](./Pointers.md) to a [functions](../Functions.md) which returns an `int` and takes no parameters:
>
>```c
>void (*ptr)(int (*)());
>void (*ptr)(int (*func)());
>```
>

## Address-Of Operator

We can assign a value to a [pointer](./Pointers.md) as we would do with any other [variable](../Variables.md):

```c
int *ptrToInt = 0x66f1;
double (*ptrToFunc)(int) = 0x900010;
```

However, this is not very useful because we are rarely aware of the underlying memory layout. Instead, we can use the address-of operator (`&`) to obtain the address of another object in memory:

```c
int var = 4;
int *pointerToVar = &var; // pointerToVar holds the memory address of var
```

```c
double func(int p) 
{
	return (double) (p / 2);
}

// ...

double (*ptrToFunc)(int) = &func; // ptrToFunc holds the memory address of func
```

For [function pointers](./Pointers.md), the [address-of operator](#Addess-Of%20Operator) can also be omitted:

```c
double (*ptrToFunc)(int) = func;
```

## Dereferencing

[Pointers](./Pointers.md) are useful because they allow us to access [variables](../Variables.md) indirectly. If we have a [pointer](./Pointers.md) `data-type *pointer`, we can access the memory at the stored address and treat it as `data-type` by using the dereference operator (`*`).

```c
int var = 1;
int *pointerToVar = &var; // pointerToVar is now equal to the address of var
*pointerToVar = 2; // var is now equal to 2
*pointerToVar += 4; // var is now equal to 6
int anotherVar = *ip; // anotherVar is now equal to var, which is six
```
