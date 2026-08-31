---
tags:
    - algebra
    - real-analysis
    - analysis
    - mathematics
---

# Linearly Damped Harmonic Oscillators

>[!DEFINITION] Definition: Linearly Damped Harmonic Oscillator
>
>A **linearly damped harmonic oscillator** is a [second-order](../Real%20Ordinary%20Differential%20Equations.md) [linear](../Linear%20Ordinary%20Differential%20Equations.md) [ordinary differential equation](../Real%20Ordinary%20Differential%20Equations.md) of the form
>
>$$\ddot{x} + 2\zeta\omega_0 \dot{x} + \omega_0^2 x = 0$$
>
>with $\omega_0 \in \mathbb{R}_{\gt 0}$ and $\zeta \in \mathbb{R}_{\ge 0}$.
>
>>[!DEFINITION] Definition: Undamped Natural Angular Frequency
>>
>>We call $\omega_0$ the **undamped natural angular frequency**.
>>
>
>>[!DEFINITION] Definition: Damping Ratio
>>
>>We call $\zeta$ the **damping ratio**.
>>
>
>>[!DEFINITION] Definition: Quality Factor
>>
>>The **quality factor** is the reciprocal of the double of the [damping ratio](./Linearly%20Damped%20Harmonic%20Oscillators.md).
>>
>>$$\frac{1}{2\zeta}$$
>>
>>>[!NOTATION]
>>>
>>>$$Q$$
>>>
>>
>
>>[!DEFINITION] Definition: Loss Factor
>>
>>The **loss factor** is twice the [damping ration](./Linearly%20Damped%20Harmonic%20Oscillators.md):
>>
>>$$2\zeta$$
>>
>>>[!NOTATION]
>>>
>>>$$d$$
>>>
>>
>
>>[!DEFINITION] Definition: Resonant Frequency
>>
>>The **resonant frequency** is the ratio of the [undamped natural frequency](./Linearly%20Damped%20Harmonic%20Oscillators.md) and $2\uppi$:
>>
>>$$\frac{\omega_0}{2\uppi}$$
>>
>>>[!NOTATION]
>>>
>>>$$f_r$$
>>>
>>
>

## Underdamped Case

>[!DEFINITION] Definition: Underdamped Linearly Damped Harmonic Oscillator
>
>A [linearly damped harmonic oscillator](./Linearly%20Damped%20Harmonic%20Oscillators.md)
>
>$$\ddot{x} + 2\zeta\omega_0 \dot{x} + \omega_0^2 x = 0 \qquad$$
>
>is **underdamped** if $\zeta \in [0, 1)$.
>

>[!THEOREM] Theorem: Solutions in the Underdamped Case (Cosine Form)
>
>The [solutions](../Real%20Ordinary%20Differential%20Equations.md) of an [underdamped](#Underdamped%20Case) [linearly damped harmonic oscillator](./Linearly%20Damped%20Harmonic%20Oscillators.md) 
>
>$$\ddot{x} + 2\zeta\omega_0 \dot{x} + \omega_0^2 x = 0$$
>
>on $\mathbb{R}$ can be expressed using the [real cosine function](../../../Real%20Functions/Real%20Trigonometric%20Functions/Real%20Cosine%20Function.md) and the [real exponential function](../../../Real%20Functions/Real%20Exponentiation.md) as
>
>$$x(t) = A \mathrm{e}^{-\zeta \omega_0 t} \cos(\omega_d t + \phi)$$
>
>with $A \in \mathbb{R}_{\ge 0}$, $\phi \in \mathbb{R}$ and $\omega_d = \omega_0 \sqrt{1 - \zeta^2}$.
>
>>[!DEFINITION] Definition: Amplitude
>>
>>We call $A$ the **amplitude** of $x$.
>>
>
>>[!DEFINITION] Definition: Phase
>>
>>We call $\phi$ the **phase** of $x$.
>>
>
>>[!DEFINITION] Definition: Damped Angular Frequency
>>
>>We call $\omega_d$ the **damped angular frequency**.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Underdamped Solutions (Sine Form)
>
>The [solutions](../Real%20Ordinary%20Differential%20Equations.md) of an [underdamped](#Underdamped%20Case) [linearly damped harmonic oscillator](./Linearly%20Damped%20Harmonic%20Oscillators.md) 
>
>$$\ddot{x} + 2\zeta\omega_0 \dot{x} + \omega_0^2 x = 0$$
>
>on $\mathbb{R}$ can be expressed using the [real sine function](../../../Real%20Functions/Real%20Trigonometric%20Functions/Real%20Sine%20Function.md) and the [real exponential function](../../../Real%20Functions/Real%20Exponentiation.md) as
>
>$$x(t) = A \mathrm{e}^{-\zeta \omega_0 t} \sin(\omega_d t + \phi)$$
>
>with $A \in \mathbb{R}_{\ge 0}$, $\phi \in \mathbb{R}$ and $\omega_d = \omega_0 \sqrt{1 - \zeta^2}$.
>
>>[!DEFINITION] Definition: Amplitude
>>
>>We call $A$ the **amplitude** of $x$.
>>
>
>>[!DEFINITION] Definition: Phase
>>
>>We call $\phi$ the **phase** of $x$.
>>
>
>>[!DEFINITION] Definition: Damped Angular Frequency
>>
>>We call $\omega_d$ the **damped angular frequency**.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Critically Damped Case

>[!DEFINITION] Definition: Critically Damped Linearly Damped Harmonic Oscillator
>
>A [linearly damped harmonic oscillator](./Linearly%20Damped%20Harmonic%20Oscillators.md)
>
>$$\ddot{x} + 2\zeta\omega_0 \dot{x} + \omega_0^2 x = 0 \qquad$$
>
>is **critically damped** if $\zeta = 1$.
>

>[!THEOREM] Theorem: Critically Damped Solutions
>
>The [solutions](../Real%20Ordinary%20Differential%20Equations.md) of a [critically damped](#Critically%20Damped%20Case) [linearly damped harmonic oscillator](./Linearly%20Damped%20Harmonic%20Oscillators.md) 
>
>$$\ddot{x} + 2\zeta\omega_0 \dot{x} + \omega_0^2 x = 0 \qquad$$
>
>on $\mathbb{R}$ can be expressed using the [real exponential function](../../../Real%20Functions/Real%20Exponentiation.md) as
>
>$$x(t) = (C_1 + C_2 t) \mathrm{e}^{-\omega_0 t}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Overdamped Case

>[!DEFINITION] Definition: Overdamped Linearly Damped Harmonic Oscillator
>
>A [linearly damped harmonic oscillator](./Linearly%20Damped%20Harmonic%20Oscillators.md)
>
>$$\ddot{x} + 2\zeta\omega_0 \dot{x} + \omega_0^2 x = 0 \qquad$$
>
>is **overdamped** if $\zeta \gt 1$.
>

>[!THEOREM] Theorem: Overdamped Solutions
>
>The [solutions](../Real%20Ordinary%20Differential%20Equations.md) of an [overdamped](#Overdamped%20Case) [linearly damped harmonic oscillator](./Linearly%20Damped%20Harmonic%20Oscillators.md) 
>
>$$\ddot{x} + 2\zeta\omega_0 \dot{x} + \omega_0^2 x = 0 \qquad$$
>
>on $\mathbb{R}$ can be expressed using the [real exponential function](../../../Real%20Functions/Real%20Exponentiation.md) as
>
>$$x(t) = C_1 \mathrm{e}^{r_1 t} + C_2 \mathrm{e}^{r_2 t},$$
>
>where:
>
>$$r_{1,2} = -\zeta \omega_0 \pm \omega_0 \sqrt{\zeta^2 - 1}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>