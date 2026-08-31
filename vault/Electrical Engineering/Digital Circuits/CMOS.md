---
tags:
    - digital-circuits
    - electrical-engineering
---

# CMOS

**Complementary MOS** (**CMOS**) refers to the use of both [PMOS](../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) and [NMOS](../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) to build [digital circuits](./Digital%20Circuits.md).

There are many reasons why [CMOS](./CMOS.md) dominates [digital circuits](./Digital%20Circuits.md) in today's world.

Technical reasons:

- Low power dissipation: It consumes very little power compared to other technologies.
- High noise immunity: It is largely insensitive to electrical interference or disturbances. Moreover, noise is reduced as a signal propagates further through a circuit.
- Clean logic levels: It produces distinct and reliable high/low voltage signals.
- Single supply voltage: It only requires one power source to operate.
- Cascadability: Components can be easily connected in series.

Economic reasons:

- Simple design: Circuits are relatively easy to design using [CMOS](./CMOS.md).
- Mature manufacturing: The production process has been well-understood and mastered.
- High integration: It allows for a very high density of transistors, making it suitable for complex integrated circuits (chips).

## CMOS Design

Every [Boolean function](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}$ can be implemented via [CMOS](./CMOS.md).

>[!ALGORITHM] Algorithm: CMOS Design from Boolean Expression
>
>We are given an arbitrary [Boolean expression](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md) of a [Boolean function](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md) $f: \{0,1\}^n \to \{0,1\}$ and want to implement $f$ via [CMOS](./CMOS.md):
>
>1. Create a **pull-up network** (**PUN**) from [PMOS transistors](../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) by traversing the expression recursively.
>
>    - Each [conjunction (AND)](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md) in the expression is physically implemented by arranging the corresponding sub-networks in parallel.
>    - Each [disjunction (OR)](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md) in the expression is physically implemented by arranging the corresponding sub-networks in series.
>    - The [gate](../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of each [PMOS](../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) is connected to exactly one [literal](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md).
>    - The [sources](../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of the top-most [PMOS transistors](../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) are connected to the supply $V_{\text{DD}}$.
>
>2. Create a **pull-down network** (**PDN**) from [NMOS transistors](../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) by traversing the expression recursively.
>
>    - Each [conjunction (AND)](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md) in the expression is physically implemented by arranging the corresponding sub-networks in series.
>    - Each [disjunction (OR)](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md) in the expression is physically implemented by arranging the corresponding sub-networks in parallel.
>    - The [gate](../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of each [NMOS](../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) is connected to exactly one [literal](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md).
>    - The [sources](../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of the bottom-most [NMOS transistors](../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) are connected to [ground](TODO).
>
>3. Connect the two networks by connecting the [drains](../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of the bottom-most [PMOS transistors](../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) to the [drains](../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of the top-most [NMOS transistors](../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) and drives this common connection into an [inverter](./Logic%20Gates/Inverters.md).
>
>    - The output of this [inverter](./Logic%20Gates/Inverters.md) is $f$.
>