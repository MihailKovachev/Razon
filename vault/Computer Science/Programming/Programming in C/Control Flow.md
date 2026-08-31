---
tags:
    - programming-in-c
    - programming
    - computer-science
---

# Control Flow

## If-Else Statements

The [C programming language](./The%20C%20Programming%20Language.md) supports if-else [statements](./Statements.md) for conditional code execution. They have the following syntax:

```c
if (expression) statement
if (expression) statement else statement
```

The `statement` of the `if` is executed whenever `expression` is different from zero and the `statement` of the `else` is executed whenever `expression` is zero.

## Switch Statements

The [C programming language](./The%20C%20Programming%20Language.md) supports `switch` [statements](./Statements.md) for conditional code execution when multiple possible branches are possible. It has the following syntax:

```c
switch (expression) statement
```

The `expression` must evaluate to an [integer](./Data%20Types/Integers.md). The `statement` consists of zero or more `case` [labeled statements](./Statements.md) and zero or one `default` [labeled statement](./Statements.md).

```c
case constant-expression : statement
default : statement
```

The `switch` evaluates its `expression`, jumps to the `case` whose `constant-expression` matches `expression` and proceeds to execution. This means that all subsequent `case` [statements](./Statements.md) are also executed. If this is not desired, a `break` [statement](./Statements.md) should be at the end of each `case`. The `switch` [statement](./Statements.md) jumps to `default` if no `case` matches and similarly proceeds with execution.

```c
switch (month)
{
    case 1:  printf("January"); break;
    case 2:  printf("February"); break;
    case 3:  printf("March"); break;
    case 4:  printf("April"); break;
    case 5:  printf("May"); break;
    case 6:  printf("June"); break;
    case 7:  printf("July"); break;
    case 8:  printf("August"); break;
    case 9:  printf("September"); break;
    case 10: printf("October"); break;
    case 11: printf("November"); break;
    case 12: printf("December"); break;
    default: printf("No such month!"); break;
}
```

## While Loops

The [C programming language](./The%20C%20Programming%20Language.md) provides `while` [statements](./Statements.md) for repeated code execution Its syntax is the following:

```c
while (expression) statement
```

The `while` [statement](./Statements.md) executes `statement` as long as `expression` does not evaluate to `zero`.

## Do-While Loops

A `do-while` [statement](./Statements.md) is like a [while loop](#While%20Loops) but it guarantees that its `statement` will be executed at least once.

```c
do statement while (expression);
```

## For Loops

A `for` [statement](./Statements.md) provides more complex loop functionality. Its syntax is the following:

```c
for (expression1; expression2; expression3) statement
```

All [expressions](TODO) are optional.

First, `expression1` is evaluated only once. Then, `statement` is executed repeatedly as long as `expression2` is non-zero. After each execution, `expression3` is evaluated.
