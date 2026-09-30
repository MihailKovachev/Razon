---
tags:
    - schrödinger-mechanics
    - quantum-physics
    - physics
---

# Hydrogen Atom (Schrödinger Mechanics)

The [hydrogen atom](TODO) is one of the few systems which can be modeled to a great precision by the [Schrödinger equation](./Schrödinger%20Equation.md) because it admits a closed-form solution. 

We model both the [proton](TODO) and the [electron](TODO) as [particles](../Quantum%20Particles.md) with [rest mass](TODO) $m_p$ and $m_e$, respectively. Under [canonical quantization](./Canonical%20Quantization%20(Schrödinger%20Mechanics).md), the [kinetic energy operator](./Kinetic%20Energy%20Operator%20(Schrödinger%20Mechanics).md) for this system is the following:

$$\hat{T} = - \frac{\hbar^2}{2 m_{p}}\left( \frac{\partial^2}{\partial x_p^2} + \frac{\partial^2}{\partial y_p^2} + \frac{\partial^2}{\partial z_p^2}\right) - \frac{\hbar^2}{2 m_{e}}\left( \frac{\partial^2}{\partial x_e^2} + \frac{\partial^2}{\partial y_e^2} + \frac{\partial^2}{\partial z_e^2}\right)$$

The interaction between the [proton](TODO) and the [electron](TODO) is modeled by the [Coloumb potential](TODO). The [potential energy](TODO) is

$$V(x_p, y_p, z_p, x_e, y_e, z_e, t) = -\frac{e^2}{4 \uppi \varepsilon_0} \frac{1}{\sqrt{(x_p - x_e)^2 + (y_p - y_e)^2 + (z_p - z_e)^2}}$$

and [canonical quantization](./Canonical%20Quantization%20(Schrödinger%20Mechanics).md) yields the following for the [potential energy operator](./Potential%20Energy%20Operator%20(Schrödinger%20Mechanics).md):

$$(\hat{V}\Psi)(x_p, y_p, z_p, x_e, y_e, z_e, t) = -\frac{e^2}{4 \uppi \varepsilon_0} \frac{1}{\sqrt{(x_p - x_e)^2 + (y_p - y_e)^2 + (z_p - z_e)^2}} \Psi(x_p, y_p, z_p, x_e, y_e, z_e, t)$$

We can now write out the [Hamiltonian operator](./Hamiltonian%20Operator%20(Schrödinger%20Mechanics).md):

$$\begin{aligned}\hat{H} & = \hat{T} + \hat{V} \\ & = \left(-\frac{\hbar^2}{2m_p} \nabla_p^2 - \frac{\hbar^2}{2 m_e} \nabla_{e}^2\right) + \hat{V} \\ & = -\frac{\hbar^2}{2 m_{p}}\left( \frac{\partial^2}{\partial x_p^2} + \frac{\partial^2}{\partial y_p^2} + \frac{\partial^2}{\partial z_p^2}\right) - \frac{\hbar^2}{2 m_{e}}\left( \frac{\partial^2}{\partial x_e^2} + \frac{\partial^2}{\partial y_e^2} + \frac{\partial^2}{\partial z_e^2} \right) + \hat{V}\end{aligned}$$

Substitution into the [Schrödinger equation](./Schrödinger%20Equation.md):

$$\hat{E}\Psi = \hat{H}\Psi$$

gives us the **Schrödinger model of the hydrogen atom**.

>[!IMPORTANT] Important: Schrödinger Model of the Hydrogen Atom
>
>$$\underset{\hat{E}\Psi}{\underbrace{\mathrm{i}\hbar \frac{\partial}{\partial t}\Psi}} = \underset{\hat{H}\Psi}{\underbrace{\underset{\hat{T} \Psi}{\underbrace{\left(-\frac{\hbar^2}{2 m_{p}}\left( \frac{\partial^2}{\partial x_p^2} + \frac{\partial^2}{\partial y_p^2} + \frac{\partial^2}{\partial z_p^2}\right) - \frac{\hbar^2}{2 m_{e}}\left( \frac{\partial^2}{\partial x_e^2} + \frac{\partial^2}{\partial y_e^2} + \frac{\partial^2}{\partial z_e^2} \right)\right) \Psi}} + \underset{\hat{V}\Psi}{\underbrace{\left(-\frac{e^2}{4 \uppi \varepsilon_0} \frac{1}{\sqrt{(x_p - x_e)^2 + (y_p - y_e)^2 + (z_p - z_e)^2}}\right) \Psi}}}}$$
>

Since $V$ is independent of $t$, we now that each [solution](TODO) $\Psi$ can be separated into the product of a purely spatial part and a temporal part for some $E \in \mathbb{R}_{\ge 0}$:

$$\Psi(x_p, y_p, z_p, x_e, y_e, z_e, t) = \psi(x_p, y_p, z_p, x_e, y_e, z_e)\exp\left(-\frac{E}{\hbar}\mathrm{i}t\right)$$

The spatial part $\psi(x_p, y_p, z_p, x_e, y_e, z_e)$ must satisfy the following [time-independent Schrödinger equation](./Time-Independent%20Schrödinger%20Equation%20(Schrödinger%20Mechanics).md):

$$E \psi = \left(-\frac{\hbar^2}{2 m_{p}}\left( \frac{\partial^2}{\partial x_p^2} + \frac{\partial^2}{\partial y_p^2} + \frac{\partial^2}{\partial z_p^2}\right) - \frac{\hbar^2}{2 m_{e}}\left( \frac{\partial^2}{\partial x_e^2} + \frac{\partial^2}{\partial y_e^2} + \frac{\partial^2}{\partial z_e^2} \right)\right) \psi - \left(\frac{e^2}{4 \uppi \varepsilon_0} \frac{1}{\sqrt{(x_p - x_e)^2 + (y_p - y_e)^2 + (z_p - z_e)^2}}\right) \psi$$

It turns out, this can be simplified using a substitution which writes the equation in terms of the center of mass and the relative position of the [electron](TODO) with respect to the [proton](TODO):

$$\begin{bmatrix}x_{\text{CoM}} \\ y_{\text{CoM}} \\ z_{\text{CoM}}\end{bmatrix} = \frac{1}{m_p + m_e}\left(m_p \begin{bmatrix}x_p \\ y_p \\ z_p\end{bmatrix} + m_e \begin{bmatrix} x_e \\ y_e \\ z_e \end{bmatrix}\right) = \begin{bmatrix}  \frac{m_p x_p + m_e x_e}{m_p + m_e} \\ \frac{m_p y_p + m_e y_p}{m_p + m_e} \\ \frac{m_p z_p + m_e z_e}{m_p + m_e}\end{bmatrix}$$

$$\begin{bmatrix} x_{\text{rel}} \\ y_{\text{rel}} \\ z_{\text{rel}}\end{bmatrix} = \begin{bmatrix} x_e\\ y_e \\ z_e \end{bmatrix} - \begin{bmatrix} x_p \\ y_p \\ z_p \end{bmatrix} = \begin{bmatrix}x_e - x_p \\ y_e - y_p \\ z_e - z_p\end{bmatrix}$$

To formalize this, we introduce a [coordinate transformation](../../../Mathematics/Analysis/Real%20Analysis/Euclidean%20Space/Coordinate%20Transformations.md) $\mathcal{T}_{\text{CoM, rel}}: \mathbb{R}^6 \to \mathbb{R}^6$

$$\mathcal{T}_{\text{to CoM, rel}} (x_p, y_p, z_p, x_e, y_e, z_e) = \begin{bmatrix} x_{\text{CoM}}(x_p, y_p, z_p, x_e, y_e, z_e) \\  y_{\text{CoM}}(x_p, y_p, z_p, x_e, y_e, z_e) \\ z_{\text{CoM}}(x_p, y_p, z_p, x_e, y_e, z_e) \\ x_{\text{rel}}(x_p, y_p, z_p, x_e, y_e, z_e) \\ y_{\text{rel}}(x_p, y_p, z_p, x_e, y_e, z_e) \\ z_{\text{rel}}(x_p, y_p, z_p, x_e, y_e, z_e)\end{bmatrix} = \begin{bmatrix} \frac{m_p x_p + m_e x_e}{m_p + m_e} \\ \frac{m_p y_p + m_e y_p}{m_p + m_e} \\ \frac{m_p z_p + m_e z_e}{m_p + m_e} \\ x_e - x_p \\ y_e - y_p \\ z_e - z_p \end{bmatrix}$$

and let $\psi_{\text{CoM, rel}}$ be such that $\psi$ is the [composition](../../../Mathematics/Analysis/Functions/Composition%20(Functions).md) $\psi = \psi_{\text{CoM, rel}} \circ \mathcal{T}_{\text{to CoM, rel}}$:

$$\psi(x_p, y_p, z_p, x_e, y_e, z_e) = (\psi_{\text{CoM, rel}} \circ \mathcal{T}_{\text{to CoM, rel}})(x_p, y_p, z_p, x_e, y_e, z_e)$$

The [partial derivative](../../../Mathematics/Analysis/Complex%20Analysis/Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables/Partial%20Differentiability%20(Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables).md) $\frac{\partial \psi}{\partial x_p}$ can be expressed by using the following monstrous application of the [chain rule](TODO):

$$\begin{aligned}\frac{\partial}{\partial x_p}\psi & = \frac{\partial}{\partial x_p} (\psi_{\text{CoM, rel}} \circ \mathcal{T}_{\text{to CoM, rel}}) \\ & = \frac{\partial \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}}} \frac{\partial x_{\text{CoM}}}{\partial x_p} + \frac{\partial \psi_{\text{CoM, rel}}}{\partial y_{\text{CoM}}} \frac{\partial y_{\text{CoM}}}{\partial x_p} + \frac{\partial \psi_{\text{CoM, rel}}}{\partial z_{\text{CoM}}} \frac{\partial z_{\text{CoM}}}{\partial x_p} + \frac{\partial \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}}} \frac{\partial x_{\text{rel}}}{\partial x_p} + \frac{\partial \psi_{\text{CoM, rel}}}{\partial y_{\text{rel}}} \frac{\partial y_{\text{rel}}}{\partial x_p} + \frac{\partial \psi_{\text{CoM, rel}}}{\partial z_{\text{rel}}} \frac{\partial z_{\text{rel}}}{\partial x_p}\\ & = \frac{\partial \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}}} \frac{\partial}{\partial x_p}\left\{ \frac{m_p x_p + m_e x_e}{m_p + m_e} \right\} + \frac{\partial \psi_{\text{CoM, rel}}}{\partial y_{\text{CoM}}} \cdot 0 + \frac{\partial \psi_{\text{CoM, rel}}}{\partial z_{\text{CoM}}} \cdot 0 + \frac{\partial \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}}} \frac{\partial}{\partial x_p} \left\{ x_e - x_p \right\} + \frac{\partial \psi_{\text{CoM, rel}}}{\partial y_{\text{rel}}} \cdot 0 + \frac{\partial \psi_{\text{CoM, rel}}}{\partial z_{\text{rel}}} \cdot 0 \\ & = \frac{\partial \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}}} \cdot \left( \frac{m_p}{m_p + m_e} \right) + \frac{\partial \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}}} \cdot (-1) \\ & = \frac{m_p}{m_p + m_e} \frac{\partial \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}}} - \frac{\partial \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}}}\end{aligned}$$

Another monstrous application of the [chain rule](TODO) allows us to express the [second-order partial derivative](../../../Mathematics/Analysis/Complex%20Analysis/Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables/Partial%20Differentiability%20(Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables).md) $\frac{\partial^2 \psi}{\partial x_p^2}$:

$$\begin{aligned}\frac{\partial^2 \psi}{\partial x_p^2} & = \frac{\partial}{\partial x_p} \left\{ \frac{\partial \psi}{\partial x_p} \right\} \\ & = \frac{\partial}{\partial x_p} \left \{ \frac{m_p}{m_p + m_e} \frac{\partial \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}}} - \frac{\partial \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}}}\right\} \\ & = \frac{m_p}{m_p + m_e} \frac{\partial}{\partial x_p} \left\{ \frac{\partial \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}}} \right\} - \frac{\partial}{\partial x_p} \left\{ \frac{\partial \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}}} \right\} \\ & = \frac{m_p}{m_p + m_e} \left(\frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}}^2}\frac{\partial x_{\text{CoM}}}{\partial x_p} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial y_{\text{CoM}} \partial x_{\text{CoM}}}\frac{\partial y_{\text{CoM}}}{\partial x_p} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial z_{\text{CoM}} \partial x_{\text{CoM}}}\frac{\partial z_{\text{CoM}}}{\partial x_p} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}} \partial x_{\text{CoM}}}\frac{\partial x_{\text{rel}}}{\partial x_p} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial y_{\text{rel}}\partial x_{\text{CoM}}}\frac{\partial y_{\text{rel}}}{\partial x_p} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial z_{\text{rel}}\partial x_{\text{CoM}}}\frac{\partial z_{\text{rel}}}{\partial x_p} \right) \\ & \quad - \left(\frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}} \partial x_{\text{rel}}}\frac{\partial x_{\text{CoM}}}{\partial x_p} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial y_{\text{CoM}} \partial x_{\text{rel}}}\frac{\partial y_{\text{CoM}}}{\partial x_p} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial z_{\text{CoM}} \partial x_{\text{rel}}}\frac{\partial z_{\text{CoM}}}{\partial x_p} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}}^2}\frac{\partial x_{\text{rel}}}{\partial x_p} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial y_{\text{rel}}\partial x_{\text{rel}}}\frac{\partial y_{\text{rel}}}{\partial x_p} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial z_{\text{rel}}\partial x_{\text{rel}}}\frac{\partial z_{\text{rel}}}{\partial x_p} \right) \\ & = \frac{m_p}{m_p + m_e} \left(\frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}}^2}\frac{\partial}{\partial x_p}\left\{ \frac{m_p x_p + m_e x_e}{m_p + m_e} \right\} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial y_{\text{CoM}} \partial x_{\text{CoM}}} \cdot 0 + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial z_{\text{CoM}} \partial x_{\text{CoM}}} \cdot 0 + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}} \partial x_{\text{CoM}}}\frac{\partial}{\partial x_p} \left\{ x_e - x_p \right\} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial y_{\text{rel}}\partial x_{\text{CoM}}} \cdot 0 + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial z_{\text{rel}}\partial x_{\text{CoM}}} \cdot 0 \right) \\ & \quad - \left(\frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}} \partial x_{\text{rel}}}\frac{\partial}{\partial x_p}\left\{ \frac{m_p x_p + m_e x_e}{m_p + m_e} \right\} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial y_{\text{CoM}} \partial x_{\text{rel}}} \cdot 0 + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial z_{\text{CoM}} \partial x_{\text{rel}}} \cdot 0 + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}}^2}\frac{\partial}{\partial x_p} \left\{ x_e - x_p \right\} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial y_{\text{rel}}\partial x_{\text{rel}}} \cdot 0 + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial z_{\text{rel}}\partial x_{\text{rel}}} \cdot 0 \right) \\ & = \frac{m_p}{m_p + m_e} \left( \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}}^2} \cdot \left( \frac{m_p}{m_p + m_e} \right) + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}} \partial x_{\text{CoM}}} \cdot (-1) \right) - \left( \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}} \partial x_{\text{rel}}} \cdot \left( \frac{m_p}{m_p + m_e} \right) + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}}^2} \cdot (-1) \right) \\ & = \left( \frac{m_p}{m_p + m_e} \right)^2 \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}}^2} - \frac{m_p}{m_p + m_e} \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}} \partial x_{\text{CoM}}} - \frac{m_p}{m_p + m_e} \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}} \partial x_{\text{rel}}} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}}^2} \\ & = \left( \frac{m_p}{m_p + m_e} \right)^2 \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}}^2} - 2 \left( \frac{m_p}{m_p + m_e} \right) \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}} \partial x_{\text{rel}}} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}}^2}\end{aligned}$$

The [second-order partial derivatives](../../../Mathematics/Analysis/Complex%20Analysis/Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables/Partial%20Differentiability%20(Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables).md) $\frac{\partial^2 \psi}{\partial y_p^2}$ and $\frac{\partial^2 \psi}{\partial z_p^2}$ are obtained by symmetry. With the definition of the **total mass** $M = m_p + m_e$, everything can be expressed a bit more compactly:

$$\begin{aligned}\frac{\partial^2 \psi}{\partial x_p^2} & = \left(\frac{m_p}{M}\right)^2 \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}}^2} - \frac{2 m_p}{M} \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}} \partial x_{\text{rel}}} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}}^2} \\ \frac{\partial^2 \psi}{\partial y_p^2} & = \left(\frac{m_p}{M}\right)^2 \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial y_{\text{CoM}}^2} - \frac{2 m_p}{M} \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial y_{\text{CoM}} \partial y_{\text{rel}}} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial y_{\text{rel}}^2} \\ \frac{\partial^2 \psi}{\partial z_p^2} & = \left(\frac{m_p}{M}\right)^2 \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial z_{\text{CoM}}^2} - \frac{2 m_p}{M} \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial z_{\text{CoM}} \partial z_{\text{rel}}} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial z_{\text{rel}}^2}\end{aligned}$$

An analogous derivation gives us the [second-order partial derivatives](../../../Mathematics/Analysis/Complex%20Analysis/Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables/Partial%20Differentiability%20(Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables).md) for $x_e$, $y_e$ and $z_e$:

$$\begin{aligned}\frac{\partial^2 \psi}{\partial x_e^2} & = \left(\frac{m_e}{M}\right)^2 \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}}^2} + \frac{2 m_e}{M} \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{CoM}} \partial x_{\text{rel}}} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial x_{\text{rel}}^2} \\ \frac{\partial^2 \psi}{\partial y_e^2} & = \left(\frac{m_e}{M}\right)^2 \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial y_{\text{CoM}}^2} + \frac{2 m_e}{M} \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial y_{\text{CoM}} \partial y_{\text{rel}}} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial y_{\text{rel}}^2} \\ \frac{\partial^2 \psi}{\partial z_e^2} & = \left(\frac{m_e}{M}\right)^2 \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial z_{\text{CoM}}^2} + \frac{2 m_e}{M} \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial z_{\text{CoM}} \partial z_{\text{rel}}} + \frac{\partial^2 \psi_{\text{CoM, rel}}}{\partial z_{\text{rel}}^2}\end{aligned}$$

We can plug this all into the previously derived [time-independent Schrödinger equation](./Time-Independent%20Schrödinger%20Equation%20(Schrödinger%20Mechanics).md):

$$E \psi = \left(-\frac{\hbar^2}{2 m_{p}}\left( \frac{\partial^2}{\partial x_p^2} + \frac{\partial^2}{\partial y_p^2} + \frac{\partial^2}{\partial z_p^2}\right) - \frac{\hbar^2}{2 m_{e}}\left( \frac{\partial^2}{\partial x_e^2} + \frac{\partial^2}{\partial y_e^2} + \frac{\partial^2}{\partial z_e^2} \right)\right) \psi - \left(\frac{e^2}{4 \uppi \varepsilon_0} \frac{1}{\sqrt{(x_p - x_e)^2 + (y_p - y_e)^2 + (z_p - z_e)^2}}\right) \psi$$

$$E \psi_{\text{CoM, rel}} = \left(-\frac{\hbar^2}{2 m_{p}}\left( \underbrace{\left(\frac{m_p}{M}\right)^2 \frac{\partial^2}{\partial x_{\text{CoM}}^2} - \frac{2 m_p}{M} \frac{\partial^2}{\partial x_{\text{CoM}} \partial x_{\text{rel}}} + \frac{\partial^2}{\partial x_{\text{rel}}^2}}_{=\frac{\partial^2}{\partial x_p^2}} + \underbrace{\left(\frac{m_p}{M}\right)^2 \frac{\partial^2}{\partial y_{\text{CoM}}^2} - \frac{2 m_p}{M} \frac{\partial^2}{\partial y_{\text{CoM}} \partial y_{\text{rel}}} + \frac{\partial^2}{\partial y_{\text{rel}}^2}}_{=\frac{\partial^2}{\partial y_p^2}} + \underbrace{\left(\frac{m_p}{M}\right)^2 \frac{\partial^2}{\partial z_{\text{CoM}}^2} - \frac{2 m_p}{M} \frac{\partial^2}{\partial z_{\text{CoM}} \partial z_{\text{rel}}} + \frac{\partial^2}{\partial z_{\text{rel}}^2}}_{=\frac{\partial^2}{\partial z_p^2}} \right) - \frac{\hbar^2}{2 m_{e}}\left( \underbrace{\left(\frac{m_e}{M}\right)^2 \frac{\partial^2}{\partial x_{\text{CoM}}^2} + \frac{2 m_e}{M} \frac{\partial^2}{\partial x_{\text{CoM}} \partial x_{\text{rel}}} + \frac{\partial^2}{\partial x_{\text{rel}}^2}}_{=\frac{\partial^2}{\partial x_e^2}} + \underbrace{\left(\frac{m_e}{M}\right)^2 \frac{\partial^2}{\partial y_{\text{CoM}}^2} + \frac{2 m_e}{M} \frac{\partial^2}{\partial y_{\text{CoM}} \partial y_{\text{rel}}} + \frac{\partial^2}{\partial y_{\text{rel}}^2}}_{=\frac{\partial^2}{\partial y_e^2}} + \underbrace{\left(\frac{m_e}{M}\right)^2 \frac{\partial^2}{\partial z_{\text{CoM}}^2} + \frac{2 m_e}{M} \frac{\partial^2}{\partial z_{\text{CoM}} \partial z_{\text{rel}}} + \frac{\partial^2}{\partial z_{\text{rel}}^2}}_{=\frac{\partial^2}{\partial z_e^2}} \right)\right) \psi_{\text{CoM, rel}} - \left(\frac{e^2}{4 \uppi \varepsilon_0} \frac{1}{\sqrt{x_{\text{rel}}^2 + y_{\text{rel}}^2 + z_{\text{rel}}^2}}\right) \psi_{\text{CoM, rel}}$$

>[!IMPORTANT] Import: Schrödinger Model of the Hydrogen Atom using Center-of-Mass and Relative Distance Coordinates
>
>$$E\psi_{\text{CoM, rel}} = -\frac{\hbar^2}{2M} \left( \frac{\partial^2}{\partial x_{\text{CoM}}^2} + \frac{\partial^2}{\partial y_{\text{CoM}}^2} + \frac{\partial^2}{\partial z_{\text{CoM}}^2}\right)\psi_{\text{CoM, rel}} -\frac{\hbar^2}{2\mu} \left( \frac{\partial^2}{\partial x_{\text{rel}}^2} + \frac{\partial^2}{\partial y_{\text{rel}}^2} + \frac{\partial^2}{\partial z_{\text{rel}}^2}\right)\psi_{\text{CoM, rel}} - \left(\frac{e^2}{4 \uppi \varepsilon_0} \frac{1}{\sqrt{x_{\text{rel}}^2 + y_{\text{rel}}^2 + z_{\text{rel}}^2}}\right) \psi_{\text{CoM, rel}}$$
>

We assume that $\psi_{\text{CoM, rel}}$ can be separated into a product where one part depends only on $(x_{\text{CoM}}, y_{\text{CoM}}, z_{\text{CoM}})$ and another depends only on $(x_{\text{rel}}, y_{\text{rel}}, z_{\text{rel}})$:

$$\psi_{\text{CoM, rel}}(x_{\text{CoM}}, y_{\text{CoM}}, z_{\text{CoM}}, x_{\text{rel}}, y_{\text{rel}}, z_{\text{rel}}) = \psi_{\text{CoM}}(x_{\text{CoM}}, y_{\text{CoM}}, z_{\text{CoM}}) \psi_{\text{rel}}(x_{\text{rel}}, y_{\text{rel}}, z_{\text{rel}})$$

Plugging this into the above equation, we get:

$$E \psi_{\text{CoM}}\psi_{\text{rel}} = -\frac{\hbar^2}{2M}\left( \frac{\partial^2}{\partial x_{\text{CoM}}^2} + \frac{\partial^2}{\partial y_{\text{CoM}}^2} + \frac{\partial^2}{\partial z_{\text{CoM}}^2} \right)\left\{\psi_{\text{CoM}}\psi_{\text{rel}}\right\} -\frac{\hbar^2}{2\mu} \left( \frac{\partial^2}{\partial x_{\text{rel}}^2} + \frac{\partial^2}{\partial y_{\text{rel}}^2} + \frac{\partial^2}{\partial z_{\text{rel}}^2}\right)\left\{\psi_{\text{CoM}}\psi_{\text{rel}}\right\} - \left(\frac{e^2}{4 \uppi \varepsilon_0} \frac{1}{\sqrt{x_{\text{rel}}^2 + y_{\text{rel}}^2 + z_{\text{rel}}^2}}\right)\psi_{\text{CoM}}\psi_{\text{rel}}$$

Since $\psi_{\text{rel}}$ is independent of $(x_{\text{CoM}}, y_{\text{CoM}}, z_{\text{CoM}})$, it behaves as a constant with respect to the [partial derivatives](../../../Mathematics/Analysis/Complex%20Analysis/Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables/Partial%20Differentiability%20(Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables).md) $\frac{\partial^2}{\partial x_{\text{CoM}}^2}$, $\frac{\partial^2}{\partial y_{\text{CoM}}^2}$ and $\frac{\partial^2}{\partial z_{\text{CoM}}^2}$. The same applies for $\psi_{\text{CoM}}$ and $\frac{\partial^2}{\partial x_{\text{rel}}^2}$, $\frac{\partial^2}{\partial y_{\text{rel}}^2}$, $\frac{\partial^2}{\partial z_{\text{rel}}^2}$:

$$E \psi_{\text{CoM}}\psi_{\text{rel}} = -\frac{\hbar^2}{2M}\psi_{\text{rel}}\left( \frac{\partial^2 \psi_{\text{CoM}}}{\partial x_{\text{CoM}}^2} + \frac{\partial^2 \psi_{\text{CoM}}}{\partial y_{\text{CoM}}^2} + \frac{\partial^2 \psi_{\text{CoM}}}{\partial z_{\text{CoM}}^2} \right) -\frac{\hbar^2}{2\mu} \psi_{\text{CoM}} \left( \frac{\partial^2 \psi_{\text{rel}}}{\partial x_{\text{rel}}^2} + \frac{\partial^2 \psi_{\text{rel}}}{\partial y_{\text{rel}}^2} + \frac{\partial^2 \psi_{\text{rel}}}{\partial z_{\text{rel}}^2}\right) - \left(\frac{e^2}{4 \uppi \varepsilon_0} \frac{1}{\sqrt{x_{\text{rel}}^2 + y_{\text{rel}}^2 + z_{\text{rel}}^2}}\right)\psi_{\text{CoM}}\psi_{\text{rel}}$$

We now divide by $\psi_{\text{CoM}} \psi_{\text{rel}}$:

$$E = -\frac{\hbar^2}{2M} \frac{1}{\psi_{\text{CoM}}}\left( \frac{\partial^2 \psi_{\text{CoM}}}{\partial x_{\text{CoM}}^2} + \frac{\partial^2 \psi_{\text{CoM}}}{\partial y_{\text{CoM}}^2} + \frac{\partial^2 \psi_{\text{CoM}}}{\partial z_{\text{CoM}}^2} \right) -\frac{\hbar^2}{2\mu} \frac{1}{\psi_{\text{rel}}} \left( \frac{\partial^2 \psi_{\text{rel}}}{\partial x_{\text{rel}}^2} + \frac{\partial^2 \psi_{\text{rel}}}{\partial y_{\text{rel}}^2} + \frac{\partial^2 \psi_{\text{rel}}}{\partial z_{\text{rel}}^2}\right) - \left(\frac{e^2}{4 \uppi \varepsilon_0} \frac{1}{\sqrt{x_{\text{rel}}^2 + y_{\text{rel}}^2 + z_{\text{rel}}^2}}\right)$$

This equation can be written as

$$E = F(x_{\text{CoM}}, y_{\text{CoM}}, z_{\text{CoM}}) + G(x_{\text{rel}}, y_{\text{rel}}, z_{\text{rel}})$$

with the [functions](../../../Mathematics/Analysis/Complex%20Analysis/Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables/Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $F: \mathbb{R}^3 \to \mathbb{C}$ and $G: \mathbb{R}^3 \to \mathbb{C}$ defined as follows:

$$F(x_{\text{CoM}}, y_{\text{CoM}}, z_{\text{CoM}}) = -\frac{\hbar^2}{2M} \frac{1}{\psi_{\text{CoM}}(x_{\text{CoM}}, y_{\text{CoM}}, z_{\text{CoM}})}\left( \frac{\partial^2}{\partial x_{\text{CoM}}^2} + \frac{\partial^2}{\partial y_{\text{CoM}}^2} + \frac{\partial^2}{\partial z_{\text{CoM}}^2} \right)\psi_{\text{CoM}}(x_{\text{CoM}}, y_{\text{CoM}}, z_{\text{CoM}})$$

$$G(x_{\text{rel}}, y_{\text{rel}}, z_{\text{rel}}) = -\frac{\hbar^2}{2\mu} \frac{1}{\psi_{\text{rel}}(x_{\text{rel}}, y_{\text{rel}}, z_{\text{rel}})} \left( \frac{\partial^2}{\partial x_{\text{rel}}^2} + \frac{\partial^2}{\partial y_{\text{rel}}^2} + \frac{\partial^2}{\partial z_{\text{rel}}^2}\right)\psi_{\text{rel}}(x_{\text{rel}}, y_{\text{rel}}, z_{\text{rel}}) - \left(\frac{e^2}{4 \uppi \varepsilon_0} \frac{1}{\sqrt{x_{\text{rel}}^2 + y_{\text{rel}}^2 + z_{\text{rel}}^2}}\right)$$

Therefore, we have

$$E = F(x_{\text{CoM}}, y_{\text{CoM}}, z_{\text{CoM}}) + G(x_{\text{rel}}, y_{\text{rel}}, z_{\text{rel}})$$

for all $(x_{\text{CoM}}, y_{\text{CoM}}, z_{\text{CoM}}, x_{\text{rel}}, y_{\text{rel}}, z_{\text{rel}})$, at least without the case where $x_{\text{rel}} = y_{\text{rel}} = z_{\text{rel}} = 0$. In particular, we know that $G(0,0,1)$ is equal to some constant $C$ and so

$$F(x_{\text{CoM}}, y_{\text{CoM}}, z_{\text{CoM}}) = E - C$$

is itself a constant for all $(x_{\text{CoM}}, y_{\text{CoM}}, z_{\text{CoM}}) \in \mathbb{R}^3$. Let's call this constant $E_{\text{CoM}}$. The same logic tells us that $G(x_{\text{rel}}, y_{\text{rel}}, z_{\text{rel}})$ is always equal to some constant $E_{\text{rel}}$:

$$F = E_{\text{CoM}} \qquad G = E_{\text{rel}}$$

We have successfully decoupled the big equation $E = F + G$ into two independent equations:

$$-\frac{\hbar^2}{2M}\frac{1}{\psi_{\text{CoM}}}\left( \frac{\partial^2 \psi_{\text{CoM}}}{\partial x_{\text{CoM}}^2} + \frac{\partial^2 \psi_{\text{CoM}}}{\partial y_{\text{CoM}}^2} + \frac{\partial^2 \psi_{\text{CoM}}}{\partial z_{\text{CoM}}^2} \right) = E_{\text{CoM}}$$

$$-\frac{\hbar^2}{2\mu} \frac{1}{\psi_{\text{rel}}} \left( \frac{\partial^2 \psi_{\text{rel}}}{\partial x_{\text{rel}}^2} + \frac{\partial^2 \psi_{\text{rel}}}{\partial y_{\text{rel}}^2} + \frac{\partial^2 \psi_{\text{rel}}}{\partial z_{\text{rel}}^2}\right) - \left(\frac{e^2}{4 \uppi \varepsilon_0} \frac{1}{\sqrt{x_{\text{rel}}^2 + y_{\text{rel}}^2 + z_{\text{rel}}^2}}\right) = E_{\text{rel}}$$

We immediately recognize the equation for $\psi_{\text{CoM}}$ as the [time-independent Schrödinger equation](./Time-Independent%20Schrödinger%20Equation%20(Schrödinger%20Mechanics).md) of a [free particle](./Free%20Particle%20(Schrödinger%20Mechanics).md). We therefore know that the system's center of mass behaves as such. 

It is more interesting to see how the relative distance between the [proton](TODO) and the [electron](TODO) behaves:

$$-\frac{\hbar^2}{2\mu} \frac{1}{\psi_{\text{rel}}} \left( \frac{\partial^2 \psi_{\text{rel}}}{\partial x_{\text{rel}}^2} + \frac{\partial^2 \psi_{\text{rel}}}{\partial y_{\text{rel}}^2} + \frac{\partial^2 \psi_{\text{rel}}}{\partial z_{\text{rel}}^2}\right) - \left(\frac{e^2}{4 \uppi \varepsilon_0} \frac{1}{\sqrt{x_{\text{rel}}^2 + y_{\text{rel}}^2 + z_{\text{rel}}^2}}\right) = E_{\text{rel}}$$

We multiply by $\psi_{\text{rel}}$:

$$-\frac{\hbar^2}{2\mu} \left( \frac{\partial^2 \psi_{\text{rel}}}{\partial x_{\text{rel}}^2} + \frac{\partial^2 \psi_{\text{rel}}}{\partial y_{\text{rel}}^2} + \frac{\partial^2 \psi_{\text{rel}}}{\partial z_{\text{rel}}^2}\right) - \left(\frac{e^2}{4 \uppi \varepsilon_0} \frac{1}{\sqrt{x_{\text{rel}}^2 + y_{\text{rel}}^2 + z_{\text{rel}}^2}}\right)\psi_{\text{rel}} = E_{\text{rel}} \psi_{\text{rel}}$$

The [hydrogen atom](TODO) is a simple system, so we can try to see if it can be solved via spherical symmetry. To this end, we introduce the [coordinate transformation](../../../Mathematics/Analysis/Real%20Analysis/Euclidean%20Space/Coordinate%20Transformations.md) $\mathcal{T}_{\text{to sph}}: \mathbb{R}^3 \to \mathbb{R}^3$ to [spherical coordinates](../../../Mathematics/Analysis/Real%20Analysis/Euclidean%20Space/Spherical%20Coordinates.md) with

$$\mathcal{T}_{\text{to sph}} (x_{\text{rel}}, y_{\text{rel}}, z_{\text{rel}}) = \begin{bmatrix}r(x_{\text{rel}}, y_{\text{rel}}, z_{\text{rel}}) \\ \theta(x_{\text{rel}}, y_{\text{rel}}, z_{\text{rel}}) \\ \phi(x_{\text{rel}}, y_{\text{rel}}, z_{\text{rel}}) \end{bmatrix} = \begin{bmatrix} \sqrt{x_{\text{rel}}^2 + y_{\text{rel}}^2 + z_{\text{rel}}^2} \\ \arccos\left(\frac{z_{\text{rel}}}{\sqrt{x_{\text{rel}}^2 + y_{\text{rel}}^2 + z_{\text{rel}}^2}}\right) \\ 2 \arctan\left(\frac{y_{\text{rel}}}{\sqrt{x_{\text{rel}}^2 + y_{\text{rel}}^2} + x_{\text{rel}}}\right) \end{bmatrix}$$

and let $\psi_{\text{rel}}^{\text{sph}}$ be such that $\psi_{\text{rel}}$ is the [composition](../../../Mathematics/Analysis/Functions/Composition%20(Functions).md) $\psi_{\text{rel}} = \psi_{\text{rel}}^{\text{sph}} \circ \mathcal{T}_{\text{to sph}}$.

TODO