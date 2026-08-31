---
tags:
    - computer-science
---

# Instruction Set Architectures

>[!DEFINITION] Definition: Instruction Set
>
>The **instruction set** of a [processor](TODO) is the [set](../Mathematics/Set%20Theory/Sets.md) of all [instructions](TODO) it understands.
>

## Classification by Complexity

[Instruction set architectures](./Instruction%20Set%20Architectures.md) fall into two broad categories based on their complexity.

**Complex instruction set computer** (**CISC**) [architectures](./Instruction%20Set%20Architectures.md) have very powerful instructions. One instruction might be able to load two operands from memory, multiply them and store the result back in memory. [CISC](./Instruction%20Set%20Architectures.md) [architectures](./Instruction%20Set%20Architectures.md) were common in the 1970s because memory back then was limited. Furthermore, there were no real compilers and writing out many instructions by hand was tedious. Another common feature is that [CISC](./Instruction%20Set%20Architectures.md) instructions usually vary in length due to the fact that they can do so many different things.

On the other hand, a single instruction of a **reduced instruction set computer** (**RISC**) [architecture](./Instruction%20Set%20Architectures.md) is very limited in what it can do. Complex operations are performed by chaining multiple simple instructions such as two load instructions to load two operands from memory into two registers, a multiplication instruction to calculate their product and a store instruction to store the result back in memory.

## Classification by Operand Location

In a **register-memory architecture**, the operands of an instructions can be in registers, in memory or in both.

In a **load-store architecture** (**register-register architecture**) the instructions are divided into two types. Memory access instructions can load data from memory into registers or store data from registers back into memory. All other instructions can only operate on registers.

## Classification by Number of Operands

In a **three-address architecture** each instruction can have up to three operands. For most instructions, one operand serves as the place to store the result of the instruction, while the other two serve as its inputs.

In a **two-address architecture** each instruction can have up to two operands. For many instructions, one of the operands doubles as both an input as well as the destination for the result.

In a **one-address architecture** or **accumulator architecture** each instruction can have either one or zero operands. There is a [register](../Electrical%20Engineering/Digital%20Circuits/Registers.md) which stores another implicit operand and doubles as both a second input operand and a destination for the result when necessary.

In a **zero-address architecture** or **stack architecture**, most instruction don't take any operands. Instead, the operands are taken directly from memory, which is organized in a [stack](TODO). A few instructions (like `PUSH` and `POP`) take a single operand in order to move data between the stack and main memory.