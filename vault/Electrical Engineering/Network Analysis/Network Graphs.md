---
tags:
    - network-analysis
    - electrical-engineering
---

# Network Graphs

The structure of a [lumped circuit](./Lumped%20Circuits.md) is analyzed using [graph theory](../../Mathematics/Graph%20Theory/Graph%20Theory.md). 

>[!DEFINITION] Definition: Network Graph
>
>The **network graph** of a [lumped circuit](./Lumped%20Circuits.md) $\mathcal{C}$ is a [directed multigraph](../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) $\mathcal{G}$ constructed as follows:
>
>    - Each [node](../Electronic%20Circuits.md) in $\mathcal{C}$ corresponds to one and only one [vertex](../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) in $\mathcal{G}$.
>
>    - For each [component](../Electronic%20Components.md) modeled as a [multiport](./Ports.md), draw an [edge](../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) between the [vertices](../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) corresponding to the two [node](../Electronic%20Circuits.md) to which the [terminals](../Electronic%20Components.md) of each [port](./Ports.md) are connected.
>
>    - For each [component](../Electronic%20Components.md) modeled as a generic [lumped element](./Lumped%20Elements.md), pick one [terminal](../Electronic%20Components.md) and draw an [edge](../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) between the [vertex](../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) corresponding to the [node](../Electronic%20Circuits.md) which the [terminal](../Electronic%20Components.md) is connected to and the [vertices](../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) corresponding to the [nodes](../Electronic%20Circuits.md) which the other [terminals](../Electronic%20Components.md) are connected to.
>
>    - Assign an arbitrary direction to each [edge](../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md).
>
>Each [vertex](../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) is called a **node** and each [edge](../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) is known as a **branch**.
>

