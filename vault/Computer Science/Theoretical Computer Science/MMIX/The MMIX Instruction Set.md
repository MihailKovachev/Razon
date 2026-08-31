---
tags:
    - computer-science
---

# The MMIX Instruction Set

Instructions in the [MMIX architecture](./MMIX.md) are always 32 bits wide. These bits are divided into four groups of 8 bits. 

![MMIX Instruction Structure](./res/MMIX%20Instruction%20Structure.svg)

The **opcode** bits uniquely identify each instruction, while the other three groups specify the **operands** with which the instruction is to be executed. 

When a [general-purpose register](./The%20MMIX%20Processor.md#General-Purpose%20Registers) ``n` is used as an operand, the corresponding bits are just the `n` in [unsigned integer representation](../../Data%20Representation/Integers.md).

When a [special register](./The%20MMIX%20Processor.md#Special%20Registers), it is represented in binary according to the following table:

|Special Register|Binary Representation|
|:--:|:--:|
|`rB`|`0x00`|
|`rD`|`0x01`|
|`rE`|`0x02`|
|`rH`|`0x03`|
|`rJ`|`0x04`|
|`rM`|`0x05`|
|`rR`|`0x06`|
|`rBB`|`0x07`|
|`rC`|`0x08`|
|`rN`|`0x09`|
|`r0`|`0x0A`|
|`rS`|`0x0B`|
|`rI`|`0x0C`|
|`rT`|`0x0D`|
|`rTT`|`0x0E`|
|`rK`|`0x0F`|
|`rQ`|`0x10`|
|`rU`|`0x11`|
|`rV`|`0x12`|
|`rG`|`0x13`|
|`rL`|`0x14`|
|`rA`|`0x15`|
|`rF`|`0x16`|
|`rP`|`0x17`|
|`rW`|`0x18`|
|`rX`|`0x19`|
|`rY`|`0x1A`|
|`rZ`|`0x1B`|
|`rWW`|`0x1C`|
|`rXX`|`0x1D`|
|`rYY`|`0x1E`|
|`rZZ`|`0x1F`|

These representations overlap with those of [general-purpose register](./The%20MMIX%20Processor.md#General-Purpose%20Registers). This ambiguity is resolved by allowing only certain registers, either [general-purpose](./The%20MMIX%20Processor.md#General-Purpose%20Registers) or [special](./The%20MMIX%20Processor.md#Special%20Registers), to be used with a given instruction.

The instructions themselves and their representations can be found in the following table:

<table>
<caption>MMIX Instruction Representations</caption>
<tbody>
<tr>
<th style="text-align:center;vertical-align:middle"></th>
<th style="text-align:center;vertical-align:middle">0x0</th>
<th style="text-align:center;vertical-align:middle">0x1</th>
<th style="text-align:center;vertical-align:middle">0x2</th>
<th style="text-align:center;vertical-align:middle">0x3</th>
<th style="text-align:center;vertical-align:middle">0x4</th>
<th style="text-align:center;vertical-align:middle">0x5</th>
<th style="text-align:center;vertical-align:middle">0x6</th>
<th style="text-align:center;vertical-align:middle">0x7</th>
<th></th>
</tr>
<tr>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x0</th>
<td style="text-align:center;vertical-align:middle">TRAP</td>
<td style="text-align:center;vertical-align:middle">FCMP</td>
<td style="text-align:center;vertical-align:middle">FUN</td>
<td style="text-align:center;vertical-align:middle">FEQL</td>
<td style="text-align:center;vertical-align:middle">FADD</td>
<td style="text-align:center;vertical-align:middle">FIX</td>
<td style="text-align:center;vertical-align:middle">FSUB</td>
<td style="text-align:center;vertical-align:middle">FIXU</td>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x0</th>
</tr>
<tr>
<td colspan="2" style="text-align:center;vertical-align:middle">FLOT[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">FLOTU[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">SFLOT[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">SFLOTU[I]</td>
</tr>
<tr>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x1</th>
<td style="text-align:center;vertical-align:middle">FMUL</td>
<td style="text-align:center;vertical-align:middle">FCMPE</td>
<td style="text-align:center;vertical-align:middle">FUNE</td>
<td style="text-align:center;vertical-align:middle">FEQLE</td>
<td style="text-align:center;vertical-align:middle">FDIV</td>
<td style="text-align:center;vertical-align:middle">FSQRT</td>
<td style="text-align:center;vertical-align:middle">FREM</td>
<td style="text-align:center;vertical-align:middle">FINT</td>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x1</th>
</tr>
<tr>
<td colspan="2" style="text-align:center;vertical-align:middle">MUL[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">MULU[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">DIV[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">DIVU[I]</td>
</tr>
<tr>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x2</th>
<td colspan="2" style="text-align:center;vertical-align:middle">ADD[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">ADDU[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">SUB[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">SUBU[I]</td>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x2</th>
</tr>
<tr>
<td colspan="2" style="text-align:center;vertical-align:middle">2ADDU[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">4ADDU[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">8ADDU[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">16ADDU[I]</td>
</tr>
<tr>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x3</th>
<td colspan="2" style="text-align:center;vertical-align:middle">CMP[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">CMPU[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">NEG[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">NEGU[I]</td>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x3</th>
</tr>
<tr>
<td colspan="2" style="text-align:center;vertical-align:middle">SL[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">SLU[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">SR[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">SRU[I]</td>
</tr>
<tr>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x4</th>
<td colspan="2" style="text-align:center;vertical-align:middle">BN[B]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">BZ[B]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">BP[B]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">BOD[B]</td>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x4</th>
</tr>
<tr>
<td colspan="2" style="text-align:center;vertical-align:middle">BNN[B]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">BNZ[B]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">BNP[B]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">BEV[B]</td>
</tr>
<tr>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x5</th>
<td colspan="2" style="text-align:center;vertical-align:middle">PBN[B]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">PBZ[B]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">PBP[B]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">PBOD[B]</td>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x5</th>
</tr>
<tr>
<td colspan="2" style="text-align:center;vertical-align:middle">PBNN[B]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">PBNZ[B]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">PBNP[B]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">PBEV[B]</td>
</tr>
<tr>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x6</th>
<td colspan="2" style="text-align:center;vertical-align:middle">CSN[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">CSZ[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">CSP[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">CSOD[I]</td>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x6</th>
</tr>
<tr>
<td colspan="2" style="text-align:center;vertical-align:middle">CSNN[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">CSNZ[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">CSNP[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">CSEV[I]</td>
</tr>
<tr>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x7</th>
<td colspan="2" style="text-align:center;vertical-align:middle">ZSN[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">ZSZ[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">ZSP[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">ZSOD[I]</td>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x7</th>
</tr>
<tr>
<td colspan="2" style="text-align:center;vertical-align:middle">ZSNN[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">ZSNZ[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">ZSNP[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">ZSEV[I]</td>
</tr>
<tr>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x8</th>
<td colspan="2" style="text-align:center;vertical-align:middle">LDB[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">LDBU[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">LDW[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">LDWU[I]</td>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x8</th>
</tr>
<tr>
<td colspan="2" style="text-align:center;vertical-align:middle">LDT[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">LDTU[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">LDO[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">LDOU[I]</td>
</tr>
<tr>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x9</th>
<td colspan="2" style="text-align:center;vertical-align:middle">LDSF[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">LDHT[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">CSWAP[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">LDUNC[I]</td>
<th rowspan="2" style="text-align:center;vertical-align:middle">0x9</th>
</tr>
<tr>
<td colspan="2" style="text-align:center;vertical-align:middle">LDVTS[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">PRELD[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">PREGO[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">GO[I]</td>
</tr>
<tr>
<th rowspan="2" style="text-align:center;vertical-align:middle">0xA</th>
<td colspan="2" style="text-align:center;vertical-align:middle">STB[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">STBU[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">STW[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">STWU[I]</td>
<th rowspan="2" style="text-align:center;vertical-align:middle">0xA</th>
</tr>
<tr>
<td colspan="2" style="text-align:center;vertical-align:middle">STT[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">STTU[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">STO[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">STOU[I]</td>
</tr>
<tr>
<th rowspan="2" style="text-align:center;vertical-align:middle">0xB</th>
<td colspan="2" style="text-align:center;vertical-align:middle">STSF[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">STHT[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">STCO[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">STUNC[I]</td>
<th rowspan="2" style="text-align:center;vertical-align:middle">0xB</th>
</tr>
<tr>
<td colspan="2" style="text-align:center;vertical-align:middle">SYNCD[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">PREST[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">SYNCID[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">PUSHGO[I]</td>
</tr>
<tr>
<th rowspan="2" style="text-align:center;vertical-align:middle">0xC</th>
<td colspan="2" style="text-align:center;vertical-align:middle">OR[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">ORN[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">NOR[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">XOR[I]</td>
<th rowspan="2" style="text-align:center;vertical-align:middle">0xC</th>
</tr>
<tr>
<td colspan="2" style="text-align:center;vertical-align:middle">AND[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">ANDN[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">NAND[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">NXOR[I]</td>
</tr>
<tr>
<th rowspan="2" style="text-align:center;vertical-align:middle">0xD</th>
<td colspan="2" style="text-align:center;vertical-align:middle">BDIF[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">WDIF[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">TDIF[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">ODIF[I]</td>
<th rowspan="2" style="text-align:center;vertical-align:middle">0xD</th>
</tr>
<tr>
<td colspan="2" style="text-align:center;vertical-align:middle">MUX[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">SADD[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">MOR[I]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">MXOR[I]</td>
</tr>
<tr>
<th rowspan="2" style="text-align:center;vertical-align:middle">0xE</th>
<td style="text-align:center;vertical-align:middle">SETH</td>
<td style="text-align:center;vertical-align:middle">SETMH</td>
<td style="text-align:center;vertical-align:middle">SETML</td>
<td style="text-align:center;vertical-align:middle">SETL</td>
<td style="text-align:center;vertical-align:middle">INCH</td>
<td style="text-align:center;vertical-align:middle">INCMH</td>
<td style="text-align:center;vertical-align:middle">INCML</td>
<td style="text-align:center;vertical-align:middle">INCL</td>
<th rowspan="2" style="text-align:center;vertical-align:middle">0xE</th>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle">ORH</td>
<td style="text-align:center;vertical-align:middle">ORMH</td>
<td style="text-align:center;vertical-align:middle">ORML</td>
<td style="text-align:center;vertical-align:middle">ORL</td>
<td style="text-align:center;vertical-align:middle">ANDNH</td>
<td style="text-align:center;vertical-align:middle">ANDNMH</td>
<td style="text-align:center;vertical-align:middle">ANDNML</td>
<td style="text-align:center;vertical-align:middle">ANDNL</td>
</tr>
<tr>
<th rowspan="2" style="text-align:center;vertical-align:middle">0xF</th>
<td colspan="2" style="text-align:center;vertical-align:middle">JMP[B]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">PUSHJ[B]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">GETA[B]</td>
<td colspan="2" style="text-align:center;vertical-align:middle">PUT[I]</td>
<th rowspan="2" style="text-align:center;vertical-align:middle">0xF</th>
</tr>
<tr>
<td style="text-align:center;vertical-align:middle">POP</td>
<td style="text-align:center;vertical-align:middle">RESUME</td>
<td style="text-align:center;vertical-align:middle">SAVE</td>
<td style="text-align:center;vertical-align:middle">UNSAVE</td>
<td style="text-align:center;vertical-align:middle">SYNC</td>
<td style="text-align:center;vertical-align:middle">SWYM</td>
<td style="text-align:center;vertical-align:middle">GET</td>
<td style="text-align:center;vertical-align:middle">TRIP</td>
</tr>
<tr>
<th></th>
<th style="text-align:center;vertical-align:middle">0x8</th>
<th style="text-align:center;vertical-align:middle">0x9</th>
<th style="text-align:center;vertical-align:middle">0xA</th>
<th style="text-align:center;vertical-align:middle">0xB</th>
<th style="text-align:center;vertical-align:middle">0xC</th>
<th style="text-align:center;vertical-align:middle">0xD</th>
<th style="text-align:center;vertical-align:middle">0xE</th>
<th style="text-align:center;vertical-align:middle">0xF</th>
<th style="text-align:center;vertical-align:middle"></th>
</tr>
</tbody>
</table>

Each row corresponds to the hexadecimal value of the most-significant nibble of the cells in it:

- If a cell is in the top sub-row of its row, then the top row of the table is used for finding its least-significant nibble.
- If a cell is in the bottom sub-row of its row, then the bottom row of the table is used for finding its least-significant nibble.

Each column corresponds to the least-significant nibble of the cells under it. When a cell spans two columns:

- Use the left column for the normal variant.
- Use the right column for the `[I]` / `[B]` variant.

The row of a cell corresponds to the hexadecimal value of its most-significant nibble.