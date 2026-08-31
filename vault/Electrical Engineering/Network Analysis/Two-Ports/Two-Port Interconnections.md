---
title: Two-Port Interconnections
tags:
    - circuit-theory
    - electrical-engineering
---

# Introduction

We can connect [two-ports](./Two-Ports.md) in ways similar to [one-ports](../One-Ports/One-Ports.md).

## Series-Series Connection

>[!DEFINITION] Definition: Series-Series Connection
>
>Two [two-ports](./Two-Ports.md) are **series-series connected** when their [input ports](./Two-Ports.md) are [connected in series](../One-Ports/One-Port%20Interconnections.md#One-Ports%20in%20Series) with one another and their [output ports](./Two-Ports.md) are also [connected in series](../One-Ports/One-Port%20Interconnections.md#One-Ports%20in%20Series) with one another:
>
>![Series-Series Two-Ports](./res/Series-Series%20Two-Ports.svg)
>

In a [series-series connection](#Series-Series%20Connection), we have the following:

$$
\boldsymbol{i}_{\mathcal{F}_1} = \boldsymbol{i}_{\mathcal{F}_2}
$$

>[!THEOREM] Theorem: Series-Series Equivalent
>
>Two [two-ports](./Two-Ports.md) $\mathcal{F}_1$ and $\mathcal{F}_2$ in a [series-series connection](#Series-Series%20Connection) are equivalent to a single [two-port](./Two-Port%20Interconnections.md) $\mathcal{F}$:
>
>![Series-Series Two-Ports Equivalence](./res/Series-Series%20Two-Ports%20Equivalence.svg)
>
>We have the following:
>
>$$
>\boldsymbol{i}^{\mathcal{F}} = \boldsymbol{i}^{\mathcal{F}_1} = \boldsymbol{i}^{\mathcal{F}_2} \qquad \boldsymbol{v}^{\mathcal{F}} = \boldsymbol{v}^{\mathcal{F}_1} + \boldsymbol{v}^{\mathcal{F}_2}
>$$
>
>If $\mathcal{F}_1$ and $\mathcal{F}_2$ have [impedance representations](./Two-Ports.md#Representations) $\boldsymbol{v}^{\mathcal{F}_1} = R_1 (\boldsymbol{i}^{\mathcal{F}_1})$ and $\boldsymbol{v}^{\mathcal{F}_2} = R_2 (\boldsymbol{i}^{\mathcal{F}_2})$, then $\mathcal{F}$ also has an [impedance representation](./Two-Ports.md#Representations)
>
>$$
>\boldsymbol{v}^{\mathcal{F}} = R(\boldsymbol{i}^{\mathcal{F}}),
>$$
>
>where $R$ is the sum of the [functions](../../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Functions.md) $R_1$ and $R_2$:
>
>$$
>R = R_1 + R_2
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Series-Parallel Connection

>[!DEFINITION] Definition: Series-Parallel Connection
>
>Two [two-ports](./Two-Ports.md) are **series-parallel connected** when their [input ports](./Two-Ports.md) are [connected in series](../One-Ports/One-Port%20Interconnections.md#One-Ports%20in%20Series) with one another and their [output ports](./Two-Ports.md) are [connected in parallel](../One-Ports/One-Port%20Interconnections.md#One-Ports%20in%20Parallel) with one another:
>
>![Series-Parallel Two-Ports](./res/Series-Parallel%20Two-Ports.svg)
>

In a [series-parallel connection](#Series-Parallel%20Connection), we have the following:

$$
i_1^{\mathcal{F}_1} = i_1^{\mathcal{F}_2} \qquad v_2^{\mathcal{F}_1} = v_2^{\mathcal{F}_2}
$$

>[!THEOREM] Theorem: Series-Parallel Equivalent
>
>Two [two-ports](./Two-Ports.md) $\mathcal{F}_1$ and $\mathcal{F}_2$ in a [series-parallel connection](#Series-Parallel%20Connection) are equivalent to a single [two-port](./Two-Port%20Interconnections.md) $\mathcal{F}$:
>
>![Series-Parallel Two-Ports Equivalence](./res/Series-Parallel%20Two-Ports%20Equivalence.svg)
>
>We have the following:
>
>$$
>\begin{aligned}i_1^{\mathcal{F}} &= i_1^{\mathcal{F}_1} = i_1^{\mathcal{F}_2} \\ \\ v_1^{\mathcal{F}} &= v_1^{\mathcal{F}_1} + v_1^{\mathcal{F}_2} \end{aligned} \qquad \qquad \begin{aligned} i_2^{\mathcal{F}} &= i_2^{\mathcal{F}_1} + i_2^{\mathcal{F}_2} \\ \\ v_2^{\mathcal{F}} &= v_2^{\mathcal{F}_1} = v_2^{\mathcal{F}_2}\end{aligned}
>$$
>
>If $\mathcal{F}_1$ and $\mathcal{F}_2$ have [hybrid representations](./Two-Ports.md#Representations) $\begin{bmatrix}v_1^{\mathcal{F}_1} \\ i_2^{\mathcal{F}_1}\end{bmatrix} = H_1 \left(\begin{bmatrix}i_1^{\mathcal{F}_1} \\ v_2^{\mathcal{F}_1}\end{bmatrix}\right)$ and $\begin{bmatrix}v_1^{\mathcal{F}_2} \\ i_2^{\mathcal{F}_2}\end{bmatrix} = H_2 \left(\begin{bmatrix}i_1^{\mathcal{F}_2} \\ v_2^{\mathcal{F}_2}\end{bmatrix}\right)$, then $\mathcal{F}$ also has a [hybrid representation](./Two-Ports.md#Representations)
>
>$$
>\begin{bmatrix}v_1^{\mathcal{F}} \\ i_2^{\mathcal{F}}\end{bmatrix} = H \left(\begin{bmatrix}i_1^{\mathcal{F}} \\ v_2^{\mathcal{F}}\end{bmatrix}\right),
>$$
>
>where $H$ is the sum of the [functions](../../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Functions.md) $H_1$ and $H_2$:
>
>$$
>H = H_1 + H_2
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Parallel-Series Connection

>[!DEFINITION] Definition: Parallel-Series Connection
>
>Two [two-ports](./Two-Ports.md) are **parallel-series connected** when their [input ports](./Two-Ports.md) are [connected in parallel](../One-Ports/One-Port%20Interconnections.md#One-Ports%20in%20Parallel) with one another and their [output ports](./Two-Ports.md) are [connected in series](../One-Ports/One-Port%20Interconnections.md#One-Ports%20in%20Series) with one another:
>
>![Parallel-Series Two-Ports](./res/Parallel-Series%20Two-Ports.svg)
>

In a [parallel-series connection](#Parallel-Series%20Connection), we have the following:

$$
v_1^{\mathcal{F}_1} = v_1^{\mathcal{F}_2} \qquad i_2^{\mathcal{F}_1} = i_2^{\mathcal{F}_2}
$$

>[!THEOREM] Theorem: Parallel-Series Equivalent
>
>Two [two-ports](./Two-Ports.md) $\mathcal{F}_1$ and $\mathcal{F}_2$ in a [parallel-series connection](#Parallel-Series%20Connection) are equivalent to a single [two-port](./Two-Port%20Interconnections.md) $\mathcal{F}$:
>
>![Parallel-Series Two-Ports Equivalence](./res/Parallel-Series%20Two-Ports%20Equivalence.svg)
>
>We have the following:
>
>$$
>\begin{aligned}i_1^{\mathcal{F}} &= i_1^{\mathcal{F}_1} + i_1^{\mathcal{F}_2} \\ \\ v_1^{\mathcal{F}} &= v_1^{\mathcal{F}_1} = v_1^{\mathcal{F}_2} \end{aligned}\qquad \qquad\begin{aligned}i_2^{\mathcal{F}} &= i_2^{\mathcal{F}_1} = i_2^{\mathcal{F}_2} \\ \\ v_2^{\mathcal{F}} &= v_2^{\mathcal{F}_1} + v_2^{\mathcal{F}_2}\end{aligned}
>$$
>
>If $\mathcal{F}_1$ and $\mathcal{F}_2$ have [inverse hybrid representations](./Two-Ports.md#Representations) $\begin{bmatrix}i_1^{\mathcal{F}_1} \\ v_2^{\mathcal{F}_1}\end{bmatrix} = H_1' \left(\begin{bmatrix}v_1^{\mathcal{F}_1} \\ i_2^{\mathcal{F}_1}\end{bmatrix}\right)$ and $\begin{bmatrix}i_1^{\mathcal{F}_2} \\ v_2^{\mathcal{F}_2}\end{bmatrix} = H_2' \left(\begin{bmatrix}v_1^{\mathcal{F}_2} \\ i_2^{\mathcal{F}_2}\end{bmatrix}\right)$, then $\mathcal{F}$ also has an [inverse hybrid representation](./Two-Ports.md#Representations)
>
>$$
>\begin{bmatrix}i_1^{\mathcal{F}} \\ v_2^{\mathcal{F}}\end{bmatrix} = H' \left(\begin{bmatrix}v_1^{\mathcal{F}} \\ i_2^{\mathcal{F}}\end{bmatrix}\right),
>$$
>
>where $H'$ is the sum of the [functions](../../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Functions.md) $H_1'$ and $H_2'$:
>
>$$
>H' = H_1' + H_2'
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Parallel-Parallel Connection

>[!DEFINITION] Definition: Parallel-Parallel Connection
>
>Two [two-ports](./Two-Ports.md) are **parallel-parallel connected** when their [input ports](./Two-Ports.md) are [connected in parallel](../One-Ports/One-Port%20Interconnections.md#One-Ports%20in%20Parallel) with one another and their [output ports](./Two-Ports.md) are also [connected in parallel](../One-Ports/One-Port%20Interconnections.md#One-Ports%20in%20Parallel) with one another:
>
>![Parallel-Parallel Two-Ports](./res/Parallel-Parallel%20Two-Ports.svg)
>

In a [parallel-parallel connection](#Parallel-Parallel%20Connection), we have the following:

$$
\boldsymbol{v}^{\mathcal{F}_1} = \boldsymbol{v}^{\mathcal{F}_2}
$$

>[!THEOREM] Theorem: Parallel-Parallel Equivalent
>
>Two [two-ports](./Two-Ports.md) $\mathcal{F}_1$ and $\mathcal{F}_2$ in a [parallel-parallel connection](#Parallel-Parallel%20Connection) are equivalent to a single [two-port](./Two-Port%20Interconnections.md) $\mathcal{F}$:
>
>![Parallel-Parallel Two-Ports Equivalence](./res/Parallel-Parallel%20Two-Ports%20Equivalence.svg)
>
>We always have:
>
>$$
>\boldsymbol{v}^{\mathcal{F}} = \boldsymbol{v}^{\mathcal{F}_1} = \boldsymbol{v}^{\mathcal{F}_2} \qquad \boldsymbol{i}^{\mathcal{F}} = \boldsymbol{i}^{\mathcal{F}_1} + \boldsymbol{i}^{\mathcal{F}_2}
>$$
>
>If $\mathcal{F}_1$ and $\mathcal{F}_2$ have [admittance representations](./Two-Ports.md) $\boldsymbol{i}^{\mathcal{F}_1} = G_1(\boldsymbol{v}^{\mathcal{F}_1})$ and $\boldsymbol{i}^{\mathcal{F}_2} = G_2(\boldsymbol{v}^{\mathcal{F}_2})$, then $\mathcal{F}$ also has an [admittance representation](./Two-Ports.md):
>
>$$
>\boldsymbol{i}^{\mathcal{F}} = G(\boldsymbol{v}^{\mathcal{F}}),
>$$
>
>where $G$ is the sum of the [functions](../../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Functions.md) $G_1$ and $G_2$:
>
>$$
>G = G_1 + G_2
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Cascade Connection

>[!DEFINITION] Definition: Cascade Connection
>
>Two [two-ports](./Two-Ports.md) are **cascade connected** when the [output port](./Two-Ports.md) of the first is connected to the [input port](./Two-Ports.md) of the second:
>
>![Cascaded Two-Ports](./res/Cascaded%20Two-Ports.svg)
>

We have the following:

$$
v_2^{\mathcal{F}_1} = v_1^{\mathcal{F}_2} \qquad i_2^{\mathcal{F}_1} = - i_1^{\mathcal{F}_2}
$$

>[!THEOREM] Theorem: Cascade Equivalent
>
>Two [two-ports](./Two-Ports.md) $\mathcal{F}_1$ and $\mathcal{F}_2$ in a [cascade connection](#Cascade%20Connection) are equivalent to a single [two-port](./Two-Port%20Interconnections.md) $\mathcal{F}$:
>
>![Cascaded Two-Ports Equivalence](./res/Cascaded%20Two-Ports%20Equivalence.svg)
>
>We have the following:
>
>$$
>\begin{aligned}
>v_1^{\mathcal{F}} &= v_1^{\mathcal{F}_1} \\ \\
>i_1^{\mathcal{F}} &= i_1^{\mathcal{F}_1}
>\end{aligned}
>\qquad \qquad
>\begin{aligned}
>v_2^{\mathcal{F}_1} &= v_1^{\mathcal{F}_2} \\ \\
>i_2^{\mathcal{F}_1} &= -i_1^{\mathcal{F}_2}
>\end{aligned}
>\qquad \qquad
>\begin{aligned}
>v_2^{\mathcal{F}} &= v_2^{\mathcal{F}_2} \\ \\
>i_2^{\mathcal{F}} &= i_2^{\mathcal{F}_2}
>\end{aligned}
>$$
>
>If $\mathcal{F}_1$ and $\mathcal{F}_2$ have [forwards transmission representations](./Two-Ports.md#Representations) $\begin{bmatrix}v_1^{\mathcal{F}_1} \\ i_1^{\mathcal{F}_1}\end{bmatrix} = T_1 \left(\begin{bmatrix}v_2^{\mathcal{F}_1} \\ -i_2^{\mathcal{F}_1}\end{bmatrix}\right)$ and $\begin{bmatrix}v_1^{\mathcal{F}_2} \\ i_1^{\mathcal{F}_2}\end{bmatrix} = T_2 \left(\begin{bmatrix}v_2^{\mathcal{F}_2} \\ -i_2^{\mathcal{F}_2}\end{bmatrix}\right)$, then $\mathcal{F}$ also has a [forwards transmission representation](./Two-Ports.md#Representations)
>
>$$
>\begin{bmatrix}v_1^{\mathcal{F}} \\ i_1^{\mathcal{F}}\end{bmatrix} = T \left(\begin{bmatrix}v_2^{\mathcal{F}} \\ -i_2^{\mathcal{F}}\end{bmatrix}\right),
>$$
>
>where $T$ is the [composition](../../../Mathematics/Analysis/Functions/Functions.md) of the [functions](../../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Functions.md) $T_1$ and $T_2$:
>
>$$
>T = T_1 \circ T_2
>$$
>
>If $\mathcal{F}_1$ and $\mathcal{F}_2$ have [backwards transmission representations](./Two-Ports.md#Representations) $\begin{bmatrix}v_2^{\mathcal{F}_1} \\ i_2^{\mathcal{F}_1}\end{bmatrix} = T_1' \left(\begin{bmatrix}v_1^{\mathcal{F}_1} \\ -i_1^{\mathcal{F}_1}\end{bmatrix}\right)$ and $\begin{bmatrix}v_2^{\mathcal{F}_2} \\ i_2^{\mathcal{F}_2}\end{bmatrix} = T_2' \left(\begin{bmatrix}v_1^{\mathcal{F}_2} \\ -i_1^{\mathcal{F}_2}\end{bmatrix}\right)$, then $\mathcal{F}$ also has a [backwards transmission representation](./Two-Ports.md#Representations)
>
>$$
>\begin{bmatrix}v_2^{\mathcal{F}} \\ i_2^{\mathcal{F}}\end{bmatrix} = T' \left(\begin{bmatrix}v_1^{\mathcal{F}} \\ -i_1^{\mathcal{F}}\end{bmatrix}\right),
>$$
>
>where $T$ is the [composition](../../../Mathematics/Analysis/Functions/Functions.md) of the [functions](../../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Functions.md) $T_2$ and $T_1$:
>
>$$
>T' = T_2' \circ T_1'
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>