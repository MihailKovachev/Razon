---
tags:
    - printed-circuit-boards
    - electrical-engineering
---

# Printed Circuit Board

A **printed circuit board** (**PCB**) is a sandwich-like structure used for connecting [electronic components](../Electronic%20Components.md) in a unified [circuit](../Electronic%20Circuits.md). Each PCB comprises a stack of insulating and conductive layers in an alternating pattern:

![PCB Structure](./res/PCB%20Structure.svg)

A single PCB can feature anywhere between 1 layer and a few dozen layers. The primary characteristics of each layer are its type (insulating or conductive), its thickness and the [dielectric constant](../../Physics/Classical%20Electromagnetism/Dielectric%20Constant.md) of its [dielectric](../../Physics/Classical%20Electromagnetism/Dielectric.md) material.

Each **insulating layer** is essentially a rectangular block made of [dielectric](../../Physics/Classical%20Electromagnetism/Dielectric.md) material. These layers provide the structural backbone of the PCB and are what holds it together. With the exception of [vias](./Via.md) passing through them, they are not allowed to contain any electrical connections.

A conductive layer represents space which can be occupied by electrical connections. These connections are exclusively made of copper with purity ≥99.8 %. Conductive layers are what enable [electronic components](../Electronic%20Components.md) to communicate with each other. The space within conductive layers which is not occupied by copper is occupied by a [dielectric](../../Physics/Classical%20Electromagnetism/Dielectric.md), just like insulating layers.

For insulating layers, the thickness is given in mils or millimeters. However, in the context of conductive layers, thickness is called **copper weight** and is specified in ounces per square foot (oz/ft²), although this is ubiquitously written as just oz. Specifically, a copper weight of "$x$ oz" corresponds to the thickness of a copper sheet which you would get if you took exactly $x$ ounces of raw copper and rolled them out perfectly flat to cover an area of exactly 1 square foot. 

>[!EXAMPLE]- Example: Commonly Used Copper Weights
>
>Below is a table of some commonly used copper weights with the physical thicknesses they correspond to in both mils (thousandths of an inch) and millimeters:
>
>|Copper Weight|Thickness (mils)|Thickness (mm)|
>|:--:|:--:|:--:|
>|0.5 oz|0.69 mils|≈0.0175 mm|
>|1.0 oz|1.37 mils|≈0.035 mm|
>|2.0 oz|2.74 mils|≈0.070 mm|
>
>A very common standard is 1 oz for the two outer conductive layers and 0.5 oz for inner conductive layers. 
>

The other important characteristic to consider, especially for insulating layers, is the [dielectric constant](../../Physics/Classical%20Electromagnetism/Dielectric%20Constant.md). Different insulating layers may be made of slightly different materials which have different [dielectric constants](../../Physics/Classical%20Electromagnetism/Dielectric%20Constant.md). For conductive layers, the space which is not occupied with copper is filled with the same material as the surrounding insulating layers.

## Build-Up

The **build-up** of a [PCB](./Printed%20Circuit%20Board.md) refers to the physical organization of its layers, specifically:

- the total number of layers;
- the total thickness of the PCB;
- the characteristics of each layer.

Choosing a build-up is the first step in the PCB layout process and should be done with careful consideration of the physical and functional constraints of the target product. Each manufacturer has their own set of "standard" build-ups which they support. Choosing a non-standard build-up necessitates consultation with the manufacturer to check if it is manufacturable in the first place and usually comes with additional manufacturing costs.

Some typical total thicknesses are 1.6 mm and 1.2 mm, although it is possible to also manufacture [PCB's](./Printed%20Circuit%20Board.md) as thin as 0.8 mm and as thick as several millimeters. 

## Stack-Up

**Stack-up** refers to the assignment of roles to the conductive layers in a given [PCB](./Printed%20Circuit%20Board.md):

- **Signal layers** are used for electrical connections which are relevant to the functions of [components](../Electronic%20Components.md).
- **Ground layers** are used as the common reference point for [voltages](TODO) in the [PCB](./Printed%20Circuit%20Board.md). Usually, they are completely filled with copper in order to provide low [resistance](TODO) and direct access to [ground](./Ground.md) through [vias](./Via.md). Apart from only the simplest designs, every [PCB](./Printed%20Circuit%20Board.md) has at least one such layer.
- **Power layers** are used for providing direct access to power through [vias](./Via.md).
- **Mixed layers** are used for any of the above. It is common to compartmentalize them in a way where each physical region of the layer serves a specific purpose.

Since both [ground layers](#Stack-Up) and [power layers](#Stack-Up) are typically filled with copper as much as possible, they also serve as protection from [electromagnetic interference](TODO).

>[!NOTE]
>
>Many people also use the term "stack-up" for both the [build-up](#Build-Up) and the [stack-up](#Stack-Up).
>