---
tags:
    - programming-in-c
    - programming
    - computer-science
---

# Operators

The [C programming language](./The%20C%20Programming%20Language.md) has almost 50 different [operators](../Programming%20Language%20Theory/Operators.md).

<table>
<caption>Operator Precedence in C</caption>
<thead>
<tr>
<th style="text-align:center;vertical-align:middle">Category</th>
<th style="text-align:center;vertical-align:middle">Operators</th>
<th style="text-align:center;vertical-align:middle">Priority</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;vertical-align:middle">Primary Operators</td>
<td style="text-align:center;vertical-align:middle"><code>()</code></td>
<td style="text-align:center;vertical-align:middle">Highest</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle">Unary Operators</td>
<td style="text-align:center;vertical-align:middle"><code>- &#43; ! &#43;&#43; --</code></td>
<td style="text-align:center;vertical-align:middle"></td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle">Multiplicative Operators</td>
<td style="text-align:center;vertical-align:middle"><code>* / %</code></td>
<td style="text-align:center;vertical-align:middle"></td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle">Additive Operators</td>
<td style="text-align:center;vertical-align:middle"><code>&#43; -</code></td>
<td style="text-align:center;vertical-align:middle"></td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle">Shift Operators</td>
<td style="text-align:center;vertical-align:middle"><code>&lt;&lt; &gt;&gt;</code></td>
<td style="text-align:center;vertical-align:middle"></td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle">Relational Operators</td>
<td style="text-align:center;vertical-align:middle"><code>&lt; &lt;&#61; &gt; &gt;&#61;</code></td>
<td style="text-align:center;vertical-align:middle"></td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle">Equality Operators</td>
<td style="text-align:center;vertical-align:middle"><code>&#61;&#61; !&#61;</code></td>
<td style="text-align:center;vertical-align:middle"></td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle">Bitwise AND</td>
<td style="text-align:center;vertical-align:middle"><code>&amp;</code></td>
<td style="text-align:center;vertical-align:middle"></td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle">Bitwise XOR</td>
<td style="text-align:center;vertical-align:middle"><code>^</code></td>
<td style="text-align:center;vertical-align:middle"></td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle">Bitwise OR</td>
<td style="text-align:center;vertical-align:middle"><code>|</code></td>
<td style="text-align:center;vertical-align:middle"></td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle">Logical AND</td>
<td style="text-align:center;vertical-align:middle"><code>&amp;&amp;</code></td>
<td style="text-align:center;vertical-align:middle"></td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle">Logical OR</td>
<td style="text-align:center;vertical-align:middle"><code>||</code></td>
<td style="text-align:center;vertical-align:middle"></td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle">Assignment Operators</td>
<td style="text-align:center;vertical-align:middle"><code>&#61;</code></td>
<td style="text-align:center;vertical-align:middle">Lowest</td>
</tr>
</tbody>
</table>

## Arithmetic Operators

The [C programming language](./The%20C%20Programming%20Language.md) has the following [operators](../Programming%20Language%20Theory/Operators.md) for doing arithmetic:

<table>
<caption>Arithmetic Operators in C</caption>
<thead>
<tr>
<th style="text-align:center;vertical-align:middle">Operator</th>
<th style="text-align:center;vertical-align:middle">Name</th>
<th style="text-align:center;vertical-align:middle">Syntax</th>
<th style="text-align:center;vertical-align:middle">Associativity</th>
<th style="text-align:center;vertical-align:middle">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;vertical-align:middle"><code>&#43;</code></td>
<td style="text-align:center;vertical-align:middle">addition</td>
<td style="text-align:center;vertical-align:middle"><code>Operand1 &#43; Operand2</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">Adds the value of <code>Operand 1</code> to the value of <code>Operand 2</code>.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>-</code></td>
<td style="text-align:center;vertical-align:middle">subtraction</td>
<td style="text-align:center;vertical-align:middle"><code>Operand1 - Operand2</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">Subtracts the value of <code>Operand 2</code> from the value of <code>Operand 1</code>.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>*</code></td>
<td style="text-align:center;vertical-align:middle">multiplication</td>
<td style="text-align:center;vertical-align:middle"><code>Operand1 * Operand2</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">Multiplies the value of <code>Operand 1</code> by the value of <code>Operand 2</code>.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>/</code></td>
<td style="text-align:center;vertical-align:middle">division</td>
<td style="text-align:center;vertical-align:middle"><code>Operand1 / Operand2</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">Divides the value of <code>Operand 1</code> by the value of <code>Operand 2</code>.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>%</code></td>
<td style="text-align:center;vertical-align:middle">modulus</td>
<td style="text-align:center;vertical-align:middle"><code>Operand1 % Operand2</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">Returns the remainder of the division of <code>Operand 1</code> by <code>Operand 2</code>.</td>
</tr>
</tbody>
</table>

## Logical Operators

<table>
<caption>Logical Operators in C</caption>
<thead>
<tr>
<th style="text-align:center;vertical-align:middle">Operator</th>
<th style="text-align:center;vertical-align:middle">Name</th>
<th style="text-align:center;vertical-align:middle">Syntax</th>
<th style="text-align:center;vertical-align:middle">Associativity</th>
<th style="text-align:center;vertical-align:middle">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;vertical-align:middle"><code>&amp;&amp;</code></td>
<td style="text-align:center;vertical-align:middle">logical AND</td>
<td style="text-align:center;vertical-align:middle"><code>Exp1 &amp;&amp; Exp2</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">True if both operands are non-zero.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>||</code></td>
<td style="text-align:center;vertical-align:middle">logical OR</td>
<td style="text-align:center;vertical-align:middle"><code>Exp1 || Exp2</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">True if at least one operand is non-zero.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>!</code></td>
<td style="text-align:center;vertical-align:middle">logical NOT</td>
<td style="text-align:center;vertical-align:middle"><code>!Expression</code></td>
<td style="text-align:center;vertical-align:middle"><strong>Right-to-Left</strong></td>
<td style="text-align:left;vertical-align:middle">Reverses the logical state of the operand.</td>
</tr>
</tbody>
</table>

## Relational Operators

The [C programming language](./The%20C%20Programming%20Language.md) has the following [operators](../Programming%20Language%20Theory/Operators.md) for comparisons:

<table>
<caption>Relational Operators in C</caption>
<thead>
<tr>
<th style="text-align:center;vertical-align:middle">Operator</th>
<th style="text-align:center;vertical-align:middle">Name</th>
<th style="text-align:center;vertical-align:middle">Syntax</th>
<th style="text-align:center;vertical-align:middle">Associativity</th>
<th style="text-align:center;vertical-align:middle">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;vertical-align:middle"><code>&#61;&#61;</code></td>
<td style="text-align:center;vertical-align:middle">equal to</td>
<td style="text-align:center;vertical-align:middle"><code>Exp1 &#61;&#61; Exp2</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">Evaluates to <code>1</code> if values are equal.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>!&#61;</code></td>
<td style="text-align:center;vertical-align:middle">not equal to</td>
<td style="text-align:center;vertical-align:middle"><code>Exp1 !&#61; Exp2</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">Evaluates to <code>1</code> if values are not equal.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>&lt;&#61;</code></td>
<td style="text-align:center;vertical-align:middle">less or equal</td>
<td style="text-align:center;vertical-align:middle"><code>Exp1 &lt;&#61; Exp2</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">Evaluates to <code>1</code> if Exp1 is less than or equal to Exp2.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>&gt;&#61;</code></td>
<td style="text-align:center;vertical-align:middle">greater or equal</td>
<td style="text-align:center;vertical-align:middle"><code>Exp1 &gt;&#61; Exp2</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">Evaluates to <code>1</code> if Exp1 is greater than or equal to Exp2.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>&lt;</code></td>
<td style="text-align:center;vertical-align:middle">less than</td>
<td style="text-align:center;vertical-align:middle"><code>Exp1 &lt; Exp2</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">Evaluates to <code>1</code> if Exp1 is less than Exp2.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>&gt;</code></td>
<td style="text-align:center;vertical-align:middle">greater than</td>
<td style="text-align:center;vertical-align:middle"><code>Exp1 &gt; Exp2</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">Evaluates to <code>1</code> if Exp1 is greater than Exp2.</td>
</tr>
</tbody>
</table>

## Bitwise Operators

<table>
<caption>Bitwise Operators in C</caption>
<thead>
<tr>
<th style="text-align:center;vertical-align:middle">Operator</th>
<th style="text-align:center;vertical-align:middle">Name</th>
<th style="text-align:center;vertical-align:middle">Syntax</th>
<th style="text-align:center;vertical-align:middle">Associativity</th>
<th style="text-align:center;vertical-align:middle">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;vertical-align:middle"><code>&amp;</code></td>
<td style="text-align:center;vertical-align:middle">bitwise AND</td>
<td style="text-align:center;vertical-align:middle"><code>Op1 &amp; Op2</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">Copies a bit to the result if it exists in both operands.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>|</code></td>
<td style="text-align:center;vertical-align:middle">bitwise OR</td>
<td style="text-align:center;vertical-align:middle"><code>Op1 | Op2</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">Copies a bit to the result if it exists in either operand.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>^</code></td>
<td style="text-align:center;vertical-align:middle">bitwise XOR</td>
<td style="text-align:center;vertical-align:middle"><code>Op1 ^ Op2</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">Copies a bit to the result if set in one operand but not both.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>~</code></td>
<td style="text-align:center;vertical-align:middle">ones complement</td>
<td style="text-align:center;vertical-align:middle"><code>~Operand</code></td>
<td style="text-align:center;vertical-align:middle"><strong>Right-to-Left</strong></td>
<td style="text-align:left;vertical-align:middle">Inverts the bits of the operand.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>&lt;&lt;</code></td>
<td style="text-align:center;vertical-align:middle">left shift</td>
<td style="text-align:center;vertical-align:middle"><code>Op &lt;&lt; n</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">Shifts bits to the left by <code>n</code> positions.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>&gt;&gt;</code></td>
<td style="text-align:center;vertical-align:middle">right shift</td>
<td style="text-align:center;vertical-align:middle"><code>Op &gt;&gt; n</code></td>
<td style="text-align:center;vertical-align:middle">Left-to-Right</td>
<td style="text-align:left;vertical-align:middle">Shifts bits to the right by <code>n</code> positions.</td>
</tr>
</tbody>
</table>

## Assignment Operators

<table>
<caption>Assignment Operators in C</caption>
<thead>
<tr>
<th style="text-align:center;vertical-align:middle">Operator</th>
<th style="text-align:center;vertical-align:middle">Name</th>
<th style="text-align:center;vertical-align:middle">Syntax</th>
<th style="text-align:center;vertical-align:middle">Associativity</th>
<th style="text-align:center;vertical-align:middle">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;vertical-align:middle"><code>&#61;</code></td>
<td style="text-align:center;vertical-align:middle">simple assignment</td>
<td style="text-align:center;vertical-align:middle"><code>Var &#61; Exp</code></td>
<td style="text-align:center;vertical-align:middle"><strong>Right-to-Left</strong></td>
<td style="text-align:left;vertical-align:middle">Assigns the value of the right operand to the left operand.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>&#43;&#61;</code></td>
<td style="text-align:center;vertical-align:middle">add and assign</td>
<td style="text-align:center;vertical-align:middle"><code>Var &#43;&#61; Exp</code></td>
<td style="text-align:center;vertical-align:middle"><strong>Right-to-Left</strong></td>
<td style="text-align:left;vertical-align:middle">Adds right operand to left and assigns result to left.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>-&#61;</code></td>
<td style="text-align:center;vertical-align:middle">subtract and assign</td>
<td style="text-align:center;vertical-align:middle"><code>Var -&#61; Exp</code></td>
<td style="text-align:center;vertical-align:middle"><strong>Right-to-Left</strong></td>
<td style="text-align:left;vertical-align:middle">Subtracts right operand from left and assigns result to left.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>*&#61;</code></td>
<td style="text-align:center;vertical-align:middle">multiply and assign</td>
<td style="text-align:center;vertical-align:middle"><code>Var *&#61; Exp</code></td>
<td style="text-align:center;vertical-align:middle"><strong>Right-to-Left</strong></td>
<td style="text-align:left;vertical-align:middle">Multiplies left by right and assigns result to left.</td>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle"><code>/&#61;</code></td>
<td style="text-align:center;vertical-align:middle">divide and assign</td>
<td style="text-align:center;vertical-align:middle"><code>Var /&#61; Exp</code></td>
<td style="text-align:center;vertical-align:middle"><strong>Right-to-Left</strong></td>
<td style="text-align:left;vertical-align:middle">Divides left by right and assigns result to left.</td>
</tr>
</tbody>
</table>
