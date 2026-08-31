---
title: The MMIX Storage
tags:
    - computer-science
---

# The MMIX Storage

The [MMIX processor](./The%20MMIX%20Processor.md) has access via a 64-bit [bus](TODO) to a storage device consisting of $2^{64}$ cells, each 8 bits wide. They are addressed from `0x0000 0000 0000 0000` to `0xFFFF FFFF FFFF FFFF` inclusively.

>[!NOTATION]
>
>The cell at address $i$ is denoted by $M[i]$.
>

## Alignment

Not all groups can be stored at the same addresses:

- a [byte](./The%20MMIX%20Processor.md#Data%20Organization) can be stored at any address;
- a [wyde](./The%20MMIX%20Processor.md#Data%20Organization) can only be stored at addresses divisible by $2$;
- a [tetra](./The%20MMIX%20Processor.md#Data%20Organization) can only be stored at addresses divisible by $4$;
- an [octa](./The%20MMIX%20Processor.md#Data%20Organization) can only be stored at addresses divisible by $8$.

## Segments

The [MMIX storage](./The%20MMIX%20Storage.md) is divided into 5 **segments** which group cells based on their address and serve specific purposes:

- The **text segment** (`Text_Segment`) contains the cells with addresses in the range $[\texttt{0x0000 0000 0000 0000}; \texttt{0x1FFF FFFF FFFF FFFF}]$.
- The **data segment** (`Data_Segment`) contains the cells with addresses in the range $[\texttt{0x2000 0000 0000 0000}; \texttt{0x3FFF FFFF FFFF FFFF}]$.
- The **pool segment** (`Pool_Segment`) contains the cells with addresses in the range $[\texttt{0x4000 0000 0000 0000}; \texttt{0x5FFF FFFF FFFF FFFF}]$.
- The **stack segment** (`Stack_Segment`) contains the cells with addresses in the range $[\texttt{0x6000 0000 0000 0000}; \texttt{0x7FFF FFFF FFFF FFFF}]$.
- The **kernel segment** contains the cells with addresses in the range $[\texttt{0x8000 0000 0000 0000}; \texttt{0xFFFF FFFF FFFF FFFF}]$.

![MMIX Memory Segments](./res/MMIX%20Memory%20Segments.svg)

### Text Segment

The **text segment** contains the cells with addresses in the range $\texttt{0x0000 0000 0000 0000}.. \texttt{0x1FFF FFFF FFFF FFFF}$. It stores the [machine instructions](../../Cybersecurity/Reverse%20Engineering/Assembly%20Programming/x86-64/Instruction%20Set.md) of the user's program program and the rest of it is filled with zeros.

### Data Segment

The **data segment** contains the cells with addresses in the range $\texttt{0x2000 0000 0000 0000}.. \texttt{0x3FFF FFFF FFFF FFFF}$. Its purpose is store data required or generated at runtime.

It is divided into two sections:

- The **heap** begins at $\texttt{0x2000 0000 0000 0000}$ and grows upwards. It is used for global and static variables as well as large pieces or data.
- The **stack** begins at $\texttt{0x3FFF FFFF FFFF FFFF}]$ and grows downwards. It is used for local variables and smaller pieces of data. 

### Pool Segment

The **pool segment** contains the cells with the addresses in the range $\texttt{0x4000 0000 0000 0000}.. \texttt{0x5FFF FFFF FFFF FFFF}$. 

The [octa](./The%20MMIX%20Processor.md) at $\texttt{0x4000 0000 0000 0000}$ stores the address of the first free cell in the [pool segment](#Pool%20Segment).

Starting from $\texttt{0x4000 0000 0000 0008}$, each [octa](./The%20MMIX%20Processor.md) stores the address of a command-line argument. This list of addresses is terminated by a null [octa](./The%20MMIX%20Processor.md). The command-line arguments themselves follow after this terminating [octa](./The%20MMIX%20Processor.md).

### Stack Segment

TODO

### Kernel Segment

The **kernel segment** contains the cells with addresses in the range $[\texttt{0x8000 0000 0000 0000}; \texttt{0xFFFF FFFF FFFF FFFF}]$. It is reserved.

