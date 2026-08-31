---
tags:
    - programming-in-c
    - programming
    - computer-science
---

# Enums

**Enums** (from "enumerable") allow us to create [data types](./Data%20Types.md) with finitely many possible values (**variants**), each of which we want to give a specific name. 

The syntax for the declaration of an [enum](./Enums.md) type is the following

```c
enum-specifier:
    enum identifieropt { enumerator-list }
    enum identifieropt { enumerator-list , }
    enum identifier

enumerator-list:
    enumerator
    enumerator-list , enumerator

enumerator:
    enumeration-constant
    enumeration-constant = constant-expression

```

>[!EXAMPLE]
>
>Here an example declaration of an [enum type](./Enums.md):
>
>```c
>enum Day { Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday };
>```
>
>To [declare](../Variables.md) [variables](../Variables.md) we use the following syntax:
>
>```c
>enum Day day1, day2;
>```
>
>We can also merge the two:
>
>```c
>enum Day { Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday } day1, day2;
>```
>
>For assignment, we use the [enum variants](./Enums.md) directly:
>
>```c
>day1 = Monday;
>day2 = Tuesday;
>```
>

Internally, an [enum](./Enums.md) is represented as an [integer](./Integers.md) and [enum variants](./Enums.md) are represented as [integer literals](./Integers.md). You can change the representation of a specific [variant](./Enums.md) by assigning it a value in the [enum declaration](./Enums.md). All [variants](./Enums.md) thar do not have representations assigned explicitly get assigned numbers in increasing order, starting at zero.



