---
tags:
    - materials-science
    - chemistry
---

# P-N Junctions

A **P-N junction** is a physical region which forms when one region of a [semiconductor](TODO) is [doped](./Semiconductor%20Doping.md) with an [acceptor  dopant](./P-Type%20Semiconductors.md) while an adjacent region is [doped](./Semiconductor%20Doping.md) with a [donor dopant](./N-Type%20Semiconductors.md). The [N-type](./N-Type%20Semiconductors.md) region has an excess of free [electrons](TODO), while the [P-type](./N-Type%20Semiconductors.md) region possesses an excess of [holes](TODO). This concentration gradient causes [electrons](TODO) to flow towards the [P-type](./N-Type%20Semiconductors.md) region and [holes](TODO) to flow towards the [N-type](./N-Type%20Semiconductors.md) region. When an [electron](TODO) and a [hole](TODO) meet at the interface between the two regions, they recombine. Therefore, the concentration of free charge carriers in the intermediate region between the [P-type semiconductor](./N-Type%20Semiconductors.md) and the [N-type semiconductor](./N-Type%20Semiconductors.md) drops significantly, leaving behind a surplus of positively charged ions on the [N-type](./N-Type%20Semiconductors.md) side and a surplus of negatively charged ions on the [P-type](./P-Type%20Semiconductors.md) side. This slowly induces an [electric field](../Physics/Classical%20Electromagnetism/Electric%20Fields.md) pointig from the [N-type](./N-Type%20Semiconductors.md) region towards the [P-type](./N-Type%20Semiconductors.md) region. 

![PNJunctionFormation](./res/PNJunctionFormation.mp4)

![P-N Junction](./res/P-N%20Junction.svg)

## Step Junction Model

The **step junction model** treats the [P-N junction](./P-N%20Junctions.md) as an abrupt boundary between a [P-type](./P-Type%20Semiconductors.md) region with a constant uniform [dopant](./Semiconductor%20Doping.md) concentration $N_{\text{acceptor}}$ and an [N-Type](./N-Type%20Semiconductors.md) region with a constant uniform [dopant](./Semiconductor%20Doping.md) concentration $N_{\text{donor}}$.

![Step Junction Model](./res/Step%20Junction%20Model.svg)

Measured from this abrupt boundary, the [depletion region](./P-N%20Junctions.md) extends a distance of $x_{\text{p}}$ into the [P-type](./P-Type%20Semiconductors.md) side and a distance of $x_{\text{n}}$ into the [N-Type](./N-Type%20Semiconductors.md) side.

### Built-In Voltage

In equilibrium, a [voltage](../Physics/Classical%20Electromagnetism/Electric%20Potential.md) $V_{\text{built-in}}$ is established between the two boundaries of the [space charge region](./P-N%20Junctions.md). Its value can be calculated using the following formula:

$$V_{\text{built-in}} = \frac{k_B \cdot T}{e} \ln \left(\frac{N_{\text{acceptor}} \cdot N_{\text{donor}}}{N_{\text{intrinsic}}^2}\right)$$

- $k_B = 1.380\,649 \times 10^{-23} \,\mathrm{J\cdot K}^{-1}$ is the [Boltzmann constant](TODO);
- $T, [\mathrm{K}]$ is the [absolute temperature](TODO);
- $e = 1.602\,176\,634 \times 10^{-19}\,\mathrm{C}$ is the [elementary charge](../Physics/Classical%20Electromagnetism/Electric%20Charge.md);
- $N_{\text{acceptor}}, [\mathrm{m}^{-3}]$ is the [dopant](./Semiconductor%20Doping.md) concentration of the [P-type](./P-Type%20Semiconductors.md) region;
- $N_{\text{donor}}, [\mathrm{m}^{-3}]$ is the [dopant](./Semiconductor%20Doping.md) concentration of the [N-Type](./N-Type%20Semiconductors.md) region;
- $N_{\text{intrinsic}}, [\mathrm{m}^{-3}]$ is the [intrinsic carrier concentration](TODO) of the [undoped](./Semiconductor%20Doping.md) [semiconductor](./Semiconductors.md).

Typical values for $V_{\text{built-in}}$ lie in the range 0.6 V - 0.9 V.



### Built-In Electric Field

### Space Charge Width

Therefore, the total width $W$ of the [depletion region](./P-N%20Junctions.md) is the following:

$$W = \sqrt{\frac{2 \cdot \varepsilon \cdot V_{\text{built-in}}}{e}\left(\frac{N_{\text{acceptor}} + N_{\text{donor}}}{N_{\text{acceptor}} \cdot N_{\text{donor}}}\right)}$$
