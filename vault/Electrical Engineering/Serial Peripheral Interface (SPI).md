---
tags:
    - electrical-engineering
---

# Serial Peripheral Interface (SPI)

**Serial peripheral interface** (**SPI**) is a protocol for [synchronized](TODO) [serial communication](TODO) used mainly for short-distance wired communication in embedded systems. It was originally designed by Motorola in the 1980s.

>[!WARNING] Warning
>
>There is no official specification for [SPI](./Serial%20Peripheral%20Interface%20(SPI).md). Naming conventions and implementation details vary greatly from one device to another and always require consultation with the data sheet of each device. 
>

## Data Transmission

[SPI](./Serial%20Peripheral%20Interface%20(SPI).md) is based on a master-slave architecture in which the master has complete control over the communication with one or more slaves. Communication happens via (up to) unidirectional 4 channels:

- **Slave Select** ($\overline{\text{SS}}$) / **Chip Select** ($\overline{\text{CS}}$): Used by the master to signal when it is sending and / or listening for data.  
- **Serial Clock** ($\text{SCLK}$): This is the serial clock signal, also controlled by the master. 
- **Master Out Slave In** ($\text{MOSI}$): Used by the master to send data to the slave.
- **Master In Slave Out** ($\text{MISO}$): Used by the slave to send data to the master.

![SPI Channels](./res/SPI%20Channels.svg)

The [slave select](./Serial%20Peripheral%20Interface%20(SPI).md) $\overline{\text{SS}}$ is an active low signal. The master holds it HIGH to indicate that it is neither sending nor listening for data, i.e. both master and slave should ignore everything on the $\text{SCLK}$, $\text{MOSI}$ and $\text{MISO}$ lines. When the master wants to send data or listen for such, it sets $\overline{\text{SS}}$ LOW and holds it LOW while sending / receiving data. To cease communication, the master pulls $\overline{\text{SS}}$ HIGH and holds it there until the next transmission.

The **clock polarity** $\text{CPOL}$ is a parameter which determines the idle state at which the master must hold $\text{SCLK}$:

- For $\text{CPOL} = 0$, the idle state of $\text{SCLK}$ must be held LOW. This means that the leading edge (first edge of a clock period) is a rising edge and the trailing edge (last edge of a clock period) is a falling edge. 
- For $\text{CPOL} = 1$, the idle state of $\text{SCLK}$ must be held HIGH. This means that the leading edge (first edge of a clock period) is a falling edge and the trailing edge (last edge of a clock period) is a rising edge. 

![SPI Idle Clock State](./res/SPI%20Idle%20Clock%20State.svg)

When the master pulls $\overline{\text{SS}}$ LOW, it needs to wait a minimum delay to ensure that the change has propagated to the slave. After this, it is free to being driving the oscillation of $\text{SCLK}$. Similarly, before pulling $\overline{\text{SS}}$ back HIGH, the master needs to return $\text{SCLK}$ to the idle state and wait a minimum delay to ensure the change has propagated to the slave.

![SPI Clock Signal](./res/SPI%20Clock%20Signal.svg)

The master sends data to the slave on the $\text{MOSI}$ line and samples the $\text{MISO}$ to receive data from the slave. The slave sends data to the master on the $\text{MISO}$ line and samples the $\text{MOSI}$ line to receive data from the master. The times at which a sender can change the logical value on a line and the times at which a receiver should sample a line are determined by the **clock phase** $\text{CPHA}$ parameter:

- For $\text{CPHA} = 0$, a receiver samples the line on the leading edge of each clock cycle. A sender can change the state of a line only before the leading edge of the first clock cycle (typically on the edge when $\overline{\text{SS}}$ is pulled LOW) or on the trailing edges of subsequent clock cycles.
- For $\text{CPHA} = 1$, a receiver samples the line on the trailing edge of each clock cycle and a sender can change the state of a line only on a leading edge.

In practice, the four possible combinations of clock polarity and clock phase are often called **SPI modes**:

|Clock Polarity ($\text{CPOL}$)|Clock Phase ($\text{CPHA}$)|SPI Mode|
|:--:|:--:|:--:|
|$0$|$0$|$0$|
|$0$|$1$|$1$|
|$1$|$0$|$2$|
|$1$|$1$|$3$|

![SPI Modes](./res/SPI%20Modes.svg)

>[!INFO] Info: Proper Configuration
>
>Both master and slave must be configured with the same SPI mode. In practice, this usually means that you must configure the master, typically a microcontroller, to use the same parameters as the slave, typically a peripheral device whose parameters have been chosen by the manufacturer and are described in the corresponding data sheet.
>
>Additionally, [SPI](./Serial%20Peripheral%20Interface%20(SPI).md) does not provide any reference values for signals such as what values constitute a HIGH or LOW signal. Again, consultation with data sheets is necessary.
>

>[!TIP] Tip: Dropping Lines
>
>In cases where the communication between master and slave is entirely unidirectional such as when the slave only does what is told by the master without providing any data back or when the master only listens to the slaves without needing to send any commands to it one line is unused all of the time and can thus be dropped entirely to save physical space and costs. 
>