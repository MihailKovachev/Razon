---
tags:
  - programming-in-c
  - programming
  - computer-science
---

# Input and Output

## Streams

[C](./The%20C%20Programming%20Language.md) handles input and output using **streams**. One can think of them as three pipes. We have access to one end of each pipe and the operating system has access to the other:
- Whatever is placed at the other end of an input [stream](#Introduction), makes its way to our end.
- Whatever we place at our end of an output [stream](#Introduction), makes its way to the operating system's end.

Functionality for operating with [streams](./Input%20and%20Output.md) is provided by the `<stdio.h>` [header](TODO).


## Input

Reading from an [input stream](#Introduction) is most commonly done using the `fscanf` [function](./Functions.md):

```c
int fscanf(FILE * restrict stream, const char * restrict format, ...);
```

The `fscanf` [function](./Functions.md) reads from the [stream](#Introduction) [pointed](./Data%20Types/Pointers.md) to by `stream`, interprets the read data according to `format` and stores it using the subsequent arguments as [pointers](./Data%20Types/Pointers.md) to the locations which should receive the converted data.

The `format` [string](./Data%20Types/Strings.md) can be comprised of three types of **directives**: [whitespace characters](./Data%20Types/Strings.md), non-[whitespace characters](./Data%20Types/Strings.md) and **conversion specification**. The `fscanf` [function](./Functions.md) goes through these [directives](#Input) one by one and tries to interpret the data from `stream` accordingly. It terminates once it has gone through all [directives](#Input) or if a [directive](#Input) fails to match data from `stream`:
- A [directive](#Input) composed of one or more [whitespace characters](./Data%20Types/Strings.md) tells `fscanf` to read and discard the data from `stream` until a non-[whitespace character](./Data%20Types/Strings.md) is encountered in `stream` or there are no more [characters](./Data%20Types/Characters.md) to be read. Such [directives](#Input) never fail. 
- A [directive](#Input) which is a sequence of $n$ ordinary, non-[whitespace characters](./Data%20Types/Strings.md) tells `fscanf` read the next $n$ [characters](./Data%20Types/Characters.md) from `stream` and compare them with the sequence in `format`. If the sequences do not match, then the [directive](#Input) fails, but the differing and subsequent [characters](./Data%20Types/Characters.md) remain in `stream`. The [directive](#Input) also fails if an [EOF](./Data%20Types/Characters.md) is reached or there is an encoding error or other read error.
- A [conversion specification](#Input) [directive](#Input) is used to match a pattern of [characters](./Data%20Types/Characters.md) in `stream` and interpret them in a specific way so as to be stored at the locations specified by the additional arguments.

A [conversion specification](#Input) has the following syntax:

```c
%[*][width][length]specifier
```

The fields in `[]` are optional and are not literally separated by brackets in the `format` [string](./Data%20Types/Strings.md).

If the `*` is present, then no argument should be provided for this [conversion specification](#Input). The execution of `fscanf` remains unaltered, but the interpreted value is discarded and not stored anywhere.

The `width` field is a positive decimal integer which specifies the maximum number of [characters](./Data%20Types/Characters.md) to read as part of this [conversion specification](#Input).

The `specifier` field is mandatory and describes the pattern to be matched:

|Value of `specifier`|Description|
|:--:|:--|
|`i`|Matches any number of digits, optionally preceded by a sign (+ or -). The format is the same as expected by [strtol](./Data%20Types/Casting.md) with `base` equal to 0. By default, the digits are assumed to be decimal (0-9), but if they start with `0`, they are treated as octal digits (0-7) and if they start with `0x`, they are treated as hexadecimal digits (0-f). By default, the argument is treated as a [pointer](./Data%20Types/Pointers.md) to [int](./Data%20Types/Integers.md).|
|`d`|Matches any number of decimal digits (0-9), optionally preceded by a sign (+ or -). The format is the same as expected by [strtol](./Data%20Types/Casting.md) with `base` equal to 10. By default, the corresponding argument is treated as a [pointer](./Data%20Types/Pointers.md) to [int](./Data%20Types/Integers.md).|
|`u`|The same as `d`, but the argument is treated as a [pointer](./Data%20Types/Pointers.md) to [unsigned int](./Data%20Types/Integers.md) by default.|
|`b`|Matches any number of binary digits (0-1), optionally preceded by a sign (+ or -). The format is the same as expected by [strtoul](./Data%20Types/Casting.md) with `base` equal to 2. By default, the corresponding argument is treated as a [pointer](./Data%20Types/Pointers.md) to [unsigned int](./Data%20Types/Integers.md).|
|`o`|Matches any number of octal digits (0-7), optionally preceded by a sign (+ or -). The format is the same as expected by [strtoul](./Data%20Types/Casting.md) with `base` equal to 8. By default, the corresponding argument is treated as a [pointer](./Data%20Types/Pointers.md) to [unsigned int](./Data%20Types/Integers.md).|
|`x`, `X`|Matches any number of hexadecimal digits (both 0-f and 0-F), optionally preceded by a sign (+ or -). The format is the same as expected by [strtoul](./Data%20Types/Casting.md) with `base` equal to 16. By default, the corresponding argument is treated as a [pointer](./Data%20Types/Pointers.md) to [unsigned int](./Data%20Types/Integers.md).|
|`a`, `A`, `e`, `E`, `f`, `F`, `g`, `G`|Matches an optionally signed [floating-point number](./Data%20Types/Floating-Point%20Numbers.md), [infinity](./Data%20Types/Floating-Point%20Numbers.md) or [NaN](./Data%20Types/Floating-Point%20Numbers.md). The format is the same as expected by [strtod](./Data%20Types/Casting.md). By default, the corresponding argument is treated as a [pointer](./Data%20Types/Pointers.md) to [float](./Data%20Types/Floating-Point%20Numbers.md).|
|`c`|Matches a sequence of [characters](./Data%20Types/Characters.md) whose number is equal to the `width` field. If `width` is not present, it matches a single [character](./Data%20Types/Characters.md). By default, the corresponding argument is treated as [pointer](./Data%20Types/Pointers.md) to [char](./Data%20Types/Characters.md), [signed char](./Data%20Types/Characters.md), [unsigned char](./Data%20Types/Characters.md) or [void](./Data%20Types/Pointers.md) that [points](./Data%20Types/Pointers.md) to a large enough chunk of memory to store the read sequence. No [null terminator](./Data%20Types/Strings.md) is appended.|
|`s`|Matches a sequence of non-[whitespace characters](./Data%20Types/Strings.md). By default, the corresponding argument is treated as [pointer](./Data%20Types/Pointers.md) to [char](./Data%20Types/Characters.md), [signed char](./Data%20Types/Characters.md), [unsigned char](./Data%20Types/Characters.md) or [void](./Data%20Types/Pointers.md) that [points](./Data%20Types/Pointers.md) to a large enough chunk of memory to store the read sequence and a [null terminator](./Data%20Types/Characters.md), which is added automatically.|
|`[characters]`|Matches any non-empty sequence of [characters](./Data%20Types/Characters.md) which is composed only of the [characters](./Data%20Types/Characters.md) in `characters`. If we want to include `]` in `characters` we must always place it directly after the opening `[`. By default, the corresponding argument is treated as [pointer](./Data%20Types/Pointers.md) to [char](./Data%20Types/Characters.md), [signed char](./Data%20Types/Characters.md), [unsigned char](./Data%20Types/Characters.md) or [void](./Data%20Types/Pointers.md) that [points](./Data%20Types/Pointers.md) to a large enough chunk of memory to store the read sequence and a [null terminator](./Data%20Types/Characters.md), which is added automatically.|
|`[^characters]`|Matches any non-empty sequence of [characters](./Data%20Types/Characters.md) which is composed only of the [characters](./Data%20Types/Characters.md) *not* in `characters`. If we want to include `]` in `characters` we must always place it directly after the opening `[^`. By default, the corresponding argument is treated as [pointer](./Data%20Types/Pointers.md) to [char](./Data%20Types/Characters.md), [signed char](./Data%20Types/Characters.md), [unsigned char](./Data%20Types/Characters.md) or [void](./Data%20Types/Pointers.md) that [points](./Data%20Types/Pointers.md) to a large enough chunk of memory to store the read sequence and a [null terminator](./Data%20Types/Characters.md), which is added automatically.|
|`n`|No data is read from `stream`. Instead, the total number of [characters](./Data%20Types/Characters.md) read by the call of `fscanf` so far is stored at the location specified by the argument, which is treated as a [pointer](./Data%20Types/Pointers.md) to a [signed int](./Data%20Types/Integers.md).|
|`%`|Matches a single `%` [character](./Data%20Types/Characters.md) in exactly the same manner as a [directive](#Input) which matches non-[whitespace characters](./Data%20Types/Strings.md).|
|`p`|Matches a sequence which can be produced by the `%p` [conversion specification](#Output) of [fprintf](#Output). By default, the corresponding argument is treated as a [pointer](./Data%20Types/Pointers.md) to a [void pointer](./Data%20Types/Pointers.md).|

The `length` field can be used to modify how the corresponding argument of the [conversion specification](#Output) is to be treated:

|Value of `length`|Description|
|:--:|:--|
|`hh`|Specifies that the argument of a `b`, `d`, `i`, `o`, `u`, `x`, `X` or `n` [conversion specification](#Input) should be a [pointer](./Data%20Types/Pointers.md) to [`unsigned char`](./Data%20Types/Characters.md) or [`signed char`](./Data%20Types/Characters.md).|
|`h`|Specifies that the argument of a `b`, `d`, `i`, `o`, `u`, `x`, `X` or `n` [conversion specification](#Input) should be a [pointer](./Data%20Types/Pointers.md) to [`short int`](./Data%20Types/Integers.md) or [`unsigned short int`](./Data%20Types/Integers.md).|
|`l`|Specifies that the argument of a `b`, `d`, `i`, `o`, `u`, `x`, `X` or `n` [conversion specification](#Input) should be a [pointer](./Data%20Types/Pointers.md) to [`long int`](./Data%20Types/Integers.md) or [`unsigned long int`](./Data%20Types/Integers.md).<br><br>Specifies that the argument of an `a`, `A`, `e`, `E`, `f`, `F`, `g` or `G` [conversion specification](#Input) should be a [pointer](./Data%20Types/Pointers.md) to [double](./Data%20Types/Floating-Point%20Numbers.md).<br><br>Specifies that the argument of a `c`, `s`, `[characters]` or `[^characters]` [conversion specification](#Input) should be a [pointer](./Data%20Types/Pointers.md) to [wchar_t](./Data%20Types/Characters.md).|
|`ll`|Specifies that the argument of a `b`, `d`, `i`, `o`, `u`, `x`, `X` or `n` [conversion specification](#Input) should be a [pointer](./Data%20Types/Pointers.md) to [`long long int`](./Data%20Types/Integers.md) or [`unsigned long long int`](./Data%20Types/Integers.md).|
|`j`|Specifies that the argument of a `b`, `d`, `i`, `o`, `u`, `x`, `X` or `n` [conversion specification](#Input) should be a [pointer](./Data%20Types/Pointers.md) to [`intmax_t`](./Data%20Types/Integers.md) or [`uintmax_t`](./Data%20Types/Integers.md).|
|`z`|Specifies that the argument of a `b`, `d`, `i`, `o`, `u`, `x`, `X` or `n` [conversion specification](#Input) should be a [pointer](./Data%20Types/Pointers.md) to [`size_t`](./Data%20Types/Integers.md).|
|`t`|Specifies that the argument of a `b`, `d`, `i`, `o`, `u`, `x`, `X` or `n` [conversion specification](#Input) should be a [pointer](./Data%20Types/Pointers.md) to [`ptrdiff_t`](TODO).|
|`L`|Specifies that the argument of a `a`, `A`, `e`, `E`, `f`, `F`, `g` or `G` [conversion specification](#Input) should be a [pointer](./Data%20Types/Pointers.md) to [`long double`](./Data%20Types/Floating-Point%20Numbers.md).|
|`H`|Specifies that the argument of a `a`, `A`, `e`, `E`, `f`, `F`, `g` or `G` [conversion specification](#Input) should be a [pointer](./Data%20Types/Pointers.md) to [`_Decimal32`](./Data%20Types/Floating-Point%20Numbers.md).|
|`D`|Specifies that the argument of a `a`, `A`, `e`, `E`, `f`, `F`, `g` or `G` [conversion specification](#Input) should be a [pointer](./Data%20Types/Pointers.md) to [`_Decimal64`](./Data%20Types/Floating-Point%20Numbers.md).|
|`DD`|Specifies that the argument of a `a`, `A`, `e`, `E`, `f`, `F`, `g` or `G` [conversion specification](#Input) should be a [pointer](./Data%20Types/Pointers.md) to [`_Decimal128`](./Data%20Types/Floating-Point%20Numbers.md).|

The [`fscanf`](#Input) [function](./Functions.md) returns [EOF](./Input%20and%20Output.md) if it fails before any [conversion specification](#Input) is completed. Otherwise, it returns the number of input assignments it performed, which is greater than or equal to zero. 

## Output

The most common way to write to a [stream](./Input%20and%20Output.md) is using the `fprintf` [function](./Functions.md):

```c
int printf(const char *format, ...);
```

The `printf` [function](./Functions.md) takes a [string](./Data%20Types/Strings.md) `format` and a variable number of arguments. The [string](./Data%20Types/Strings.md) `format` is what ultimately gets written to `stdout`, but it is first interpreted and modified by `printf`. This allows us to provide additional data to `printf` and also specify how this data should be formatted. 

This formatting is done using **format specifiers** in `format`. The first additional argument corresponds to the first specifier, the second argument to the second specifier and so on. Therefore, the number of additional arguments must be at least as much as the number of specifiers. Additional arguments are ignored. 

These specifiers have the following syntax:

```c
%[flags][width][precision][length]specifier
```

Everything in `[]` is optional. The fields themselves have the following possible values:

|`specifier`|Interpret and format as|Example Output|
|:--:|:--|:--:|
|`d`, `i`|Signed decimal integer|`-392`, `392`|
|`u`|Unsigned decimal integer|`7235`|
|`o`|Unsigned octal integer|`610`|
|`x`|Unsigned hexadecimal integer, lowercase|`7fa`|
|`X`|Unsigned hexadecimal integer, uppercase|`7FA`|
|`f`|Decimal floating point, lowercase|`392.65`, `nan`, `inf`|
|`F`|Decimal floating point, uppercase|`392.65`, `NAN`, `INF`|
|`e`|Decimal scientific notation, lowercase|`3.9265e+2`|
|`E`|Decimal scientific notation, uppercase|`3.9265E+2`|
|`g`|The shortest of `e` or `f`|`392.65`|
|`G`|The shortest of `E` or `F`|`392.5`|
|`a`|Binary scientific notation, represented using hexadecimal digits, lowercase|`0xc.90fep-2`|
|`A`|Binary scientific notation, represented using hexadecimal digits, uppercase|`0XC.90FEP-2`|
|`c`|Single character|`a`|
|`s`|[Null-terminated string](./Data%20Types/Strings.md) of characters|`sample`|
|`p`|Memory address|`b8000000`|
|`n`|The corresponding argument must be a [pointer](./Data%20Types/Pointers.md) to `signed int`. Prints nothing but the total number of characters written so far is stored in the provided location.||
|`%`|Writes a single `%`|`%`|

The `width` field is optional and can be used to specify the minimum number of characters to be printed:

|`width`|Description|
|:--:|:--|
|Number|Minimum number of characters to be printed. If the value to be printed is shorter than this number, blank spaces are additionally printed.||
|`*`|The number of minimum characters is specified in an additional argument which preces the argument to be formatted.|

The `precision`field is used to specify the precision with which the number is to be printed:

|`precision`|Description|
|:--:|:--|
|`.number`|For the [specifiers](./Input%20and%20Output.md) `d`, `i`, `o`, `u`, `x`, `X` this specifies the minimum number of digits to be written. If the value to be written is shorter, leading zeros are added. If `number` is $0$ and the argument is also $0$, then nothing is written.<br><br>For the [specifiers](./Input%20and%20Output.md) `a`, `A`, `e`, `E`, `f`, `F` this specifies the number of digits to be printed *after* the decimal point (6 by default).|
|`.*`|The `precision` is specified in an additional integer value argument preceding the argument to be formatted.<br><br>For the [specifiers](./Input%20and%20Output.md) `g` and `G` this is the maximum number of significant digits to be printed.<br><br>For the [specifier](./Input%20and%20Output.md) `s` this is the maximum number of character to write. The defaut is to write until the [null terminator](TODO) is reached.<br><br>If only the dot (`.`) is present, then an implicit `number` of $0$ is assumed.|

The `length` field specifies as what [data type](./Data%20Types/Data%20Types.md) the argument should be interpreted:

<table>
<tr>
<th style="text-align:center;vertical-align:middle" rowspan = 2><code>length</code></th>
<th style="text-align:center;vertical-align:middle" colspan = 7><code>specifier</code></th>
</tr>
<tr>
<th style="text-align:center;vertical-align:middle"><code>d</code>, <code>i</code></th>
<th style="text-align:center;vertical-align:middle"><code>u</code>, <code>o</code>, <code>x</code>, <code>X</code></th>
<th style="text-align:center;vertical-align:middle"><code>f</code>, <code>F</code>, <code>e</code>, <code>E</code>, <code>g</code>, <code>G</code>, <code>a</code>, <code>A</code></th>
<th style="text-align:center;vertical-align:middle"><code>c</code></th>
<th style="text-align:center;vertical-align:middle"><code>s</code></th>
<th style="text-align:center;vertical-align:middle"><code>p</code></th>
<th style="text-align:center;vertical-align:middle"><code>n</code></th>
</tr>
<tr>
<td th style="text-align:center;vertical-align:middle">None</td>
<td th style="text-align:center;vertical-align:middle"><code>int</code></td>
<td th style="text-align:center;vertical-align:middle"><code>unsigned int</code></td>
<td th style="text-align:center;vertical-align:middle"><code>double</code></td>
<td th style="text-align:center;vertical-align:middle"><code>int</code></td>
<td th style="text-align:center;vertical-align:middle"><code>char*</code></td>
<td th style="text-align:center;vertical-align:middle"><code>void*</code></td>
<td th style="text-align:center;vertical-align:middle"><code>int*</code></td>
</tr>
<tr>
<td th style="text-align:center;vertical-align:middle"><code>hh</code></td>
<td th style="text-align:center;vertical-align:middle"><code>signed char</code></td>
<td th style="text-align:center;vertical-align:middle"><code>unsigned char</code></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"><code>signed char*</code></td>
</tr>
<tr>
<td th style="text-align:center;vertical-align:middle"><code>h</code></td>
<td th style="text-align:center;vertical-align:middle"><code>short int</code></td>
<td th style="text-align:center;vertical-align:middle"><code>unsigned short int</code></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"><code>short int*</code></td>
</tr>
<tr>
<td th style="text-align:center;vertical-align:middle"><code>l</code></td>
<td th style="text-align:center;vertical-align:middle"><code>short int</code></td>
<td th style="text-align:center;vertical-align:middle"><code>unsigned short int</code></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"><code>wint_t</code></td>
<td th style="text-align:center;vertical-align:middle"><code>wchar_t*</code></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"><code>long int*</code></td>
</tr>
<tr>
<td th style="text-align:center;vertical-align:middle"><code>ll</code></td>
<td th style="text-align:center;vertical-align:middle"><code>long long int</code></td>
<td th style="text-align:center;vertical-align:middle"><code>unsigned long long int</code></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"><code>long long int*</code></td>
</tr>
<tr>
<td th style="text-align:center;vertical-align:middle"><code>j</code></td>
<td th style="text-align:center;vertical-align:middle"><code>intmax_t</code></td>
<td th style="text-align:center;vertical-align:middle"><code>unitmax_t</code></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"><code>intmax_t*</code></td>
</tr>
<tr>
<td th style="text-align:center;vertical-align:middle"><code>z</code></td>
<td th style="text-align:center;vertical-align:middle"><code>size_t</code></td>
<td th style="text-align:center;vertical-align:middle"><code>size_t</code></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"><code>size_t*</code></td>
</tr>
<tr>
<td th style="text-align:center;vertical-align:middle"><code>t</code></td>
<td th style="text-align:center;vertical-align:middle"><code>ptrdiff_t</code></td>
<td th style="text-align:center;vertical-align:middle"><code>ptrdiff_t</code></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"></td>
<td th style="text-align:center;vertical-align:middle"><code>ptrdiff_t*</code></td>
</tr>
</table>


## Standard I / O

[C](./The%20C%20Programming%20Language.md) provides three standard [streams](#Introduction) for input and output: **standard input** (`stdin`), **standard output** (`stdout`) and **standard error** (`stderr`). 
- Whatever is placed at the other end of `stdin`, makes its way to our end.
- Whatever we place at our end of `stdout` or `stderr`, makes its way to the other end, respectively.

Most commonly, all three streams end up in the console, but it may also be a file or a network socket and it is also not necessary that all streams end up in the same place.

### Standard Input

Reading from `stdin` is most commonly done using the `scanf` function:

```c
int scanf ( const char * format, ... );
```

It behaves in the same way as [`fscanf`](#Input), but `stream` is automatically set to `stdin`.

### Standard Output

