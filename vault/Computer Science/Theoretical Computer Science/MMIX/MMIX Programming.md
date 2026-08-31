---
tags:
    - computer-science   
---

# MMIX Programming

[MMIX](./MMIX.md) comes with its own human-readable [programming language](TODO) known as **MMIXAL**.

## Syntax

Each line in an [MMIXAL](./MMIX%20Programming.md) file represents one command and is divided into four columns: **label**, **mnemonic**, **operands** and **comment** which are separated from each other by one or more [whitespace characters](TODO).

|Label|Mnemonic|Operands|Comment|
|:--|:--|:--|:--|
|An optional name which can be used as an address to the current row. If there is no label, then the line should begin with a [whitespace](TODO).|Determines what action should be performed. Some commands are executed by the assembler, some by the loader and some by the processor at runtime.|These are the operands of the command (if any). Multiple operands are given as a comma-separated list without any spaces in-between.|Everything here is ignored, including [whitespace](TODO).|

A line which begins with a non-[whitespace](TODO) character other than `0-9A-Za-z` is ignored.

## Assembler Instructions

<table>
<caption>Assembler Instructions</caption>
<thead>
<tr>
<th style="text-align:center;vertical-align:middle">Mnemonic</th>
<th style="text-align:center;vertical-align:middle">Description</th>
<th style="text-align:center;vertical-align:middle">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;vertical-align:middle"><code>IS</code></td>
<td style="text-align:start;vertical-align:middle">Takes a single general-purpose register as an operand and tells the assembler that the register can henceforth be referred to by the label of this row.</td>
<td style="text-align:start;vertical-align:middle"><code>SideLength IS $3 // From now on, SideLength is the same as $3</code></td>
</tr>
</tbody>
</table>

## Loader Instructions

<table>
<caption>Assembler Instructions</caption>
<thead>
<tr>
<th style="text-align:center;vertical-align:middle">Mnemonic</th>
<th style="text-align:center;vertical-align:middle">Description</th>
<th style="text-align:center;vertical-align:middle">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;vertical-align:middle"><code>GREG</code></td>
<td style="text-align:start;vertical-align:middle">Initializes a general-purpose register as a global register with its operand. This register can henceforth be referred to by the label of this row.</td>
<td style="text-align:start;vertical-align:middle"><code>SP GREG &#35;4000000000000000 // A new global register was reserved and initialized with the value &#35;4000000000000000. This register can be referred to by the name SP.</code></td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>LOC</code></td>
<td style="text-align:start;vertical-align:middle">Sets the loader's location counter to its operand. Subsequent data and instructions are then placed in memory beginning from this new location counter. The current value of the location counter can be obtained via @.</td>
<td style="text-align:start;vertical-align:middle"><code>LOC Data_Segment // Subsequent data and instruction will be stored beginning from the Data_Segment.</code></td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>BYTE</code></td>
<td style="text-align:start;vertical-align:middle">Initializes bytes in memory using its operands and increases the location counter appropriately. This first of these bytes can subsequently be accessed via the label of this row. Alignment is automatically taken into account by inserting empty bytes.</td>
<td style="text-align:start;vertical-align:middle"><code>Arr BYTE 10,20,30 // Initializes an array of bytes in memory which contains the elements 10, 20 and 30. The first element, 10, can be accessed via the label Arr.</code></td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>WYDE</code></td>
<td style="text-align:start;vertical-align:middle">Initializes wydes in memory using its operands and increases the location counter appropriately. This first of these bytes can subsequently be accessed via the label of this row. Alignment is automatically taken into account by inserting empty bytes.</td>
<td style="text-align:start;vertical-align:middle"><code>Arr WYDE 10,20,30 // Initializes an array of wydes in memory which contains the elements 10, 20 and 30. The first element, 10, can be accessed via the label Arr.</code></td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>TETRA</code></td>
<td style="text-align:start;vertical-align:middle">Initializes tetras in memory using its operands and increases the location counter appropriately. This first of these bytes can subsequently be accessed via the label of this row. Alignment is automatically taken into account by inserting empty bytes.</td>
<td style="text-align:start;vertical-align:middle"><code>Arr TETRA 10,20,30 // Initializes an array of tetras in memory which contains the elements 10, 20 and 30. The first element, 10, can be accessed via the label Arr.</code></td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>OCTA</code></td>
<td style="text-align:start;vertical-align:middle">Initializes octas in memory using its operands and increases the location counter appropriately. This first of these bytes can subsequently be accessed via the label of this row. Alignment is automatically taken into account by inserting empty bytes.</td>
<td style="text-align:start;vertical-align:middle"><code>Arr OCTA 10,20,30 // Initializes an array of octas in memory which contains the elements 10, 20 and 30. The first element, 10, can be accessed via the label Arr.</code></td>
</tr>
</tbody>
</table>