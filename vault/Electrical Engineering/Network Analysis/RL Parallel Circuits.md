---
tags:
    - network-analysis
    - electrical-engineering
---

# RL Parallel Circuits

![RL Parallel Circuit](./res/RL%20Parallel%20Circuit.svg)

## Current Input

![RL Parallel Circuit Current Input](./res/RL%20Parallel%20Circuit%20Current%20Input.svg)

By applying [Kirchhoff's voltage law](./Lumped%20Circuits.md#Kirchhoff's%20Voltage%20Law), we get:

$$v(t) = v_{L}(t)$$

Using [Kirchhoff's current law](./Lumped%20Circuits.md#Kirchhoff's%20Current%20Law), we get:

$$i_G(t) + i_L(t) = i_{\text{in}}(t)$$

The [strictly linear resistive one-port](./One-Ports/Strictly%20Linear%20Resistive%20One-Ports.md) gives us the following:

$$i_G(t) = G v(t)$$

The [strictly linear inductive one-port](./One-Ports/Strictly%20Linear%20Inductive%20One-Ports.md) tells us that $v_L(t)$ is the [derivative](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Differentiability%20(Real%20Functions).md) of $i_L(t)$ multiplied by $L$:

$$v_L(t) = L \frac{\mathrm{d}i_L}{\mathrm{d}t}(t)$$

Plugging this into the [KVL](./Lumped%20Circuits.md#Kirchhoff's%20Voltage%20Law) and then into the [KCL](./Lumped%20Circuits.md#Kirchhoff's%20Current%20Law), we get:

$$v(t) = L \frac{\mathrm{d}i_L}{\mathrm{d}t}(t)$$

$$-i_{\text{in}}(t) + GL \frac{\mathrm{d}i_L}{\mathrm{d}t}(t) + i_L(t) = 0$$

$$\frac{\mathrm{d}i_L}{\mathrm{d}t}(t) = -\frac{1}{GL} i_L(t) + \frac{1}{GL}i_{\text{in}}(t)$$

>[!DEFINITION] Definition: Time Constant
>
>We call $GL$ the **time constant**.
>
>>[!NOTATION]
>>
>>$$\tau$$
>>
>

Therefore, we get the following [first-order](../../Mathematics/Analysis/Real%20Analysis/Differential%20Equations/Ordinary%20Differential%20Equations/Real%20Ordinary%20Differential%20Equations.md) [linear ODE](../../Mathematics/Analysis/Real%20Analysis/Differential%20Equations/Ordinary%20Differential%20Equations/Linear%20Ordinary%20Differential%20Equations.md):

$$\frac{\mathrm{d}i_L}{\mathrm{d}t}(t) = -\frac{1}{\tau} i_L(t) + \frac{1}{\tau}i_{\text{in}}(t)$$

If the [current](./One-Ports/One-Ports.md) through $L$ at some time $t_0$ is $i_L(t_0)$, then solving for $i_L(t)$ yields the following for $t \ge t_0$:

$$i_L(t) = i_L(t_0) \mathrm{e}^{-\frac{t - t_0}{GL}} + \int_{t_0}^t \frac{1}{GL} i_{\text{in}}(t') \mathrm{e}^{-\frac{t - t'}{GL}} \, \mathrm{d}t'$$

Expressed via $\tau$, we get:

$$i_L(t) = i_L(t_0) \mathrm{e}^{-\frac{t - t_0}{\tau}} + \int_{t_0}^t \frac{1}{\tau} i_{\text{in}}(t') \mathrm{e}^{-\frac{t - t'}{\tau}} \, \mathrm{d}t'$$

Since $i_{\text{out}} = i_L$, we get:

$$i_{\text{out}}(t) = i_L(t_0) \mathrm{e}^{-\frac{t - t_0}{\tau}} + \int_{t_0}^t \frac{1}{\tau} i_{\text{in}}(t') \mathrm{e}^{-\frac{t - t'}{\tau}} \, \mathrm{d}t'$$

## Zero-Input Response

If $i_{\text{in}}(t)$ is zero for all $t$, then the solution reduces to just the first term:

$$i_{\text{out}}(t) = i_L(t_0) \mathrm{e}^{-\frac{t - t_0}{\tau}}$$

## Zero-State Response

If the [current](./One-Ports/One-Ports.md) through $L$ at $t_0$ is zero, then the solution reduces to just the second term:

$$i_{\text{out}}(t) = \int_{t_0}^t \frac{1}{\tau} i_{\text{in}}(t') \mathrm{e}^{-\frac{t - t'}{\tau}} \, \mathrm{d}t'$$

## Constant Input

If the input $i_{\text{in}}(t)$ does not change with time, i.e. $i_{\text{in}}(t) = I_{\text{in}}$, the state equation reduces to the following:

$$\frac{\mathrm{d}i_L}{\mathrm{d}t}(t) = -\frac{1}{LG} i_L(t) + \frac{I_{\text{in}}}{LG}$$

The solution is the following:

$$\begin{aligned}i_{\text{out}}(t) & = i_L(t_0) \mathrm{e}^{-\frac{t - t_0}{LG}} + \int_{t_0}^t \frac{1}{LG} i_{\text{in}}(t') \mathrm{e}^{-\frac{t - t'}{LG}} \, \mathrm{d}t' \\ & = i_L(t_0) \mathrm{e}^{-\frac{t - t_0}{LG}} + \int_{t_0}^t \frac{I_{\text{in}}}{LG} \mathrm{e}^{-\frac{t - t'}{LG}} \, \mathrm{d}t' \\ & = i_L(t_0) \mathrm{e}^{-\frac{t - t_0}{LG}} + I_{\text{in}} \left[ \mathrm{e}^{-\frac{t - t'}{LG}} \right]_{t'=t_0}^{t'=t} \\ & = i_L(t_0) \mathrm{e}^{-\frac{t - t_0}{LG}} + I_{\text{in}} \left( 1 - \mathrm{e}^{-\frac{t - t_0}{LG}} \right) \\ & = I_{\text{in}} + \left( i_L(t_0) - I_{\text{in}} \right) \mathrm{e}^{-\frac{t - t_0}{LG}}\end{aligned}$$

### Stable Case

For $GL \gt 0$, the output $i_{\text{out}}$ [approaches](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Limits%20(Real%20Functions).md) $I_{\text{in}}$ for $t \to \infty$:

$$\lim_{t \to \infty} i_{\text{out}}(t) = I_{\text{in}}$$

Since it is [exponential](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Exponentiation.md), this also happens fairly quickly. After a period of just one [time constant](./RL%20Parallel%20Circuits.md) $\tau = LG$ after $t_0$, $i_{\text{out}}$ has moved approximately two-thirds of $I_{\text{in}} - i_{L,0}$ away from $i_{L,0}$ and towards $I_{\text{in}}$:

$$\begin{aligned} i(t_0 + \tau) & = I_{\text{in}} + (i_{L,0} - I_{\text{in}}) \mathrm{e}^{-\frac{t_0 + LG - t_0}{LG}} \\ & = I_{\text{in}} + (i_{L,0} - I_{\text{in}}) \mathrm{e}^{-1} \\ & \approx I_{\text{in}} + (i_{L,0} - I_{\text{in}}) \cdot 0.37 \\ & \approx I_{\text{in}} + (i_{L,0} - I_{\text{in}})\left( 1 - \frac{2}{3} \right) \\ & = I_{L, 0} + \frac{2}{3}(I_{\text{in}} - I_{L, 0})\end{aligned}$$

For practical purposes, we can consider this value to be reached after a period of just $7$ [time constants](./RL%20Parallel%20Circuits.md), since the error then is just $10^{-3} |i_{L,0} - I_{\text{in}}|$.

### Unstable Case

For $GL \lt 0$, the output $i_{\text{out}}$ explodes away from $I_{\text{in}}$ for $t \to \infty$. The direction in which this happens depends on whether $I_{L, 0}$ is greater than or less than $I_{\text{in}}$:

- If $I_{L, 0} \lt I_{\text{in}}$, then $i_{\text{out}}$ [approaches](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Limits%20(Real%20Functions).md) $-\infty$ for $t \to \infty$.

$$I_{L, 0} \lt I_{\text{in}} \implies \lim_{t \to \infty} i_{\text{out}}(t) = -\infty$$

- If $I_{L, 0} \gt I_{\text{in}}$, then $i_{\text{out}}$ [approaches](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Limits%20(Real%20Functions).md) $\infty$ for $t \to \infty$.

$$I_{L, 0} \gt I_{\text{in}} \implies \lim_{t \to \infty} i_{\text{out}}(t) = \infty$$

However, for $t \to -\infty$, the output $i_{\text{out}}$ stabilizes at $I_{\text{in}}$:

$$\lim_{t \to -\infty} i_{\text{out}}(t) = I_{\text{in}}$$
