---
tags:
    - algebra
    - real-analysis
    - analysis
    - mathematics
---

# Sinusoidally Driven Linearly Damped Harmonic Oscillators

>[!DEFINITION] Definition: Sinusoidally Driven Linearly Damped Harmonic Oscillator
>
>A **sinusoidally driven linearly damped harmonic oscillator** is a [second-order](../Real%20Ordinary%20Differential%20Equations.md) [linear](../Linear%20Ordinary%20Differential%20Equations.md) [ordinary differential equation](../Real%20Ordinary%20Differential%20Equations.md) of the form
>
>$$\ddot{x} + 2\zeta\omega_0 \dot{x} + \omega_0^2 x = A_d \cos(\omega t)$$
>
>with $\omega_0, \omega \in \mathbb{R}_{\gt 0}$, $\zeta \in \mathbb{R}_{\ge 0}$, and $A_d \in \mathbb{R}$.
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
>>[!DEFINITION] Definition: Driving Angular Frequency
>>
>>We call $\omega$ the **driving angular frequency**.
>>
>
>>[!DEFINITION] Definition: Driving Amplitude
>>
>>We call $A_d$ the **driving amplitude**.
>>
>

## Underdamped Case

>[!DEFINITION] Definition: Underdamped Linearly Damped Harmonic Oscillator
>
>A [sinusoidally driven linearly damped harmonic oscillator](./Sinusoidally%20Driven%20Linearly%20Damped%20Harmonic%20Oscillators.md)
>
>$$\ddot{x} + 2\zeta\omega_0 \dot{x} + \omega_0^2 x = A_d \cos(\omega t)$$
>
>is **underdamped** if $\zeta \in [0, 1)$.
>

>[!THEOREM] Theorem: Solutions in the Underdamped Case (Cosine Form)
>
>The [solutions](../Real%20Ordinary%20Differential%20Equations.md) of an [underdamped](#Underdamped%20Case) [sinusoidally driven linearly damped harmonic oscillator](./Sinusoidally%20Driven%20Linearly%20Damped%20Harmonic%20Oscillators.md)
>
>$$\ddot{x} + 2\zeta\omega_0 \dot{x} + \omega_0^2 x = A_d \cos(\omega t)$$
>
>on $\mathbb{R}$ can be expressed using the [real cosine function](../../../Real%20Functions/Real%20Trigonometric%20Functions/Real%20Cosine%20Function.md) and the [real exponential function](../../../Real%20Functions/Real%20Exponentiation.md) as
>
>$$x(t) = e^{-\zeta\omega_0 t} \left( C_1 \cos(\omega_d t) + C_2 \sin(\omega_d t) \right) + A \cos(\omega t - \phi),$$
>
>where:
>
>$$\omega_d = \omega_0 \sqrt{1 - \zeta^2}$$
>
>$$A = \frac{A_d}{\sqrt{(\omega_0^2 - \omega^2)^2 + (2\zeta\omega_0\omega)^2}}$$
>
>$$\tan \phi = \frac{2\zeta \omega_0 \omega}{\omega_0^2 - \omega^2}$$
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
>A [sinusoidally driven linearly damped harmonic oscillator](./Sinusoidally%20Driven%20Linearly%20Damped%20Harmonic%20Oscillators.md)
>
>$$\ddot{x} + 2\zeta\omega_0 \dot{x} + \omega_0^2 x = A_d \cos(\omega t)$$
>
>is **critically damped** if $\zeta = 1$.
>

>[!THEOREM] Theorem: Critically Damped Solutions
>
>The [solutions](../Real%20Ordinary%20Differential%20Equations.md) of a [critically damped](#Critically%20Damped%20Case) [sinusoidally driven linearly damped harmonic oscillator](./Sinusoidally%20Driven%20Linearly%20Damped%20Harmonic%20Oscillators.md)
>
>$$\ddot{x} + 2\zeta\omega_0 \dot{x} + \omega_0^2 x = A_d \cos(\omega t)$$
>
>on $\mathbb{R}$ can be expressed using the [real exponential function](../../../Real%20Functions/Real%20Exponentiation.md) as
>
>$$x(t) = (C_1 + C_2 t) e^{-\omega_0 t} + A \cos(\omega t - \phi),$$
>
>where:
>
>$$A = \frac{A_d}{\sqrt{(\omega_0^2 - \omega^2)^2 + (2\zeta\omega_0\omega)^2}}$$
>
>$$\tan \phi = \frac{2\zeta \omega_0 \omega}{\omega_0^2 - \omega^2}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Overdamped Case

>[!DEFINITION] Definition: Overdamped Linearly Damped Harmonic Oscillator
>
>A [sinusoidally driven linearly damped harmonic oscillator](./Sinusoidally%20Driven%20Linearly%20Damped%20Harmonic%20Oscillators.md)
>
>$$\ddot{x} + 2\zeta\omega_0 \dot{x} + \omega_0^2 x = A_d \cos(\omega t)$$
>
>is **overdamped** if $\zeta \gt 1$.
>

>[!THEOREM] Theorem: Overdamped Solutions
>
>The [solutions](../Real%20Ordinary%20Differential%20Equations.md) of an [overdamped](#Overdamped%20Case) [sinusoidally driven linearly damped harmonic oscillator](./Sinusoidally%20Driven%20Linearly%20Damped%20Harmonic%20Oscillators.md) 
>
>$$\ddot{x} + 2\zeta\omega_0 \dot{x} + \omega_0^2 x = A_d \cos(\omega t)$$
>
>on $\mathbb{R}$ can be expressed using the [real exponential function](../../../Real%20Functions/Real%20Exponentiation.md) as
>
>$$x(t) = C_1 \mathrm{e}^{r_1 t} + C_2 \mathrm{e}^{r_2 t} + A \cos (\omega t - \phi),$$
>
>where:
>
>$$r_{1,2} = -\zeta \omega_0 \pm \omega_0 \sqrt{\zeta^2 - 1}$$
>
>$$A = \frac{A_d}{\sqrt{(\omega_0^2 - \omega^2)^2 + (2\zeta\omega_0\omega)^2}}$$
>
>$$\tan \phi = \frac{2\zeta \omega_0 \omega}{\omega_0^2 - \omega^2}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>