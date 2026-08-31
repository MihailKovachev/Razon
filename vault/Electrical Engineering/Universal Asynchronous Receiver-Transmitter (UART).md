---
tags:
    - electrical-engineering
---

# Universal Asynchronous Receiver-Transmitter (UART)

A **universal asynchronous receiver-transmitter** (**UART**) is a simple peripheral device designed for [asynchronous](TODO) [serial communication](TODO). It is typically implemented as an [integrated circuit](TODO) or embedded directly into larger chips such as [microcontrollers](TODO). 

>[!NOTE]
>
>Since the operation of [UARTs](./Universal%20Asynchronous%20Receiver-Transmitter%20(UART).md) is highly standardized and well-known, it is also common to see [UART](./Universal%20Asynchronous%20Receiver-Transmitter%20(UART).md) described as a protocol. However, it is almost always implemented using dedicated hardware, i.e. the [UART](./Universal%20Asynchronous%20Receiver-Transmitter%20(UART).md) device itself.
>

## Data Transmission

A [UART](./Universal%20Asynchronous%20Receiver-Transmitter%20(UART).md) device consists of a clock generator, two [shift registers](TODO) connected to external lines as well as two separate [registers](TODO) for storing the received data as well as the data to be transmitted:

![UART Block Diagram](./res/UART%20Block%20Diagram.svg)

Data is sent and received in frames in a sequential, bit-by-bit manner. The idle state of a line is logic HIGH. Each individual bit is distinguished by its duration which is determined by the **baud rate**, measured in bits per second (bps). The baud rate must be configured identically on both devices before communication can take place.

>[!EXAMPLE]- Example: Baud Rate
>
>The most common baud rate is 9600 bps which means that each bit is $\frac{1}{9600}$ seconds long. 
>

![UART Frame](./res/UART%20Frame.svg)

The first bit of a frame is always logic LOW and is known as the **start bit** because it signals the beginning of the frame.

The start bit is followed by five to nine **data bits**. The precise number of data bits must be configured identically on both devices which are communicating and each frame must always contain the agreed-upon number of data bits.

The data bits may optionally be followed by a **parity bit**. This bit can be used as a rudimentary error-checking bit. Depending on the chosen mode of operation, the parity bit is set to either logic LOW or logic HIGH:

- Even parity: the parity bit's value is such that the total number of logic HIGHs in the data bits and the parity bit is an even number;
- Odd parity: the parity bit's value is such that the total number of logic HIGHs in the data bits and the parity bit is an odd number.

The mode of operation as well as whether the parity bit should even be present in the frames must be configured identically on both devices in advance.

The frame ends with one or two **stop bits** set to logic HIGH. The number of stop bits must again be configured on both ends beforehand. After the stop bits, the line either remains in its idle logic HIGH state or the next frame begins.