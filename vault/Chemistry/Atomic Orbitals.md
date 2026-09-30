---
tags:
    - chemistry
    - quantum-physics
---

# Atomic Orbitals

**Atomic orbitals** are a specific set of [wave functions](../Physics/Quantum%20Physics/Schrödinger%20Mechanics/Wave%20Function%20(Schrödinger%20Mechanics).md) describing [hydrogen-like atoms](../Physics/Quantum%20Physics/Schrödinger%20Mechanics/Hydrogen-like%20Atoms%20(Schrödinger%20Mechanics).md), specifically the relative position of the [electron](TODO) with respect to the [nucleus](TODO). 

Each [orbital](./Atomic%20Orbitals.md) is characterized by three [integers](TODO):

- the **principal quantum number** $n \in \{1, 2, 3, \dotsc\}$;
- the **azimuthal quantum number** $\ell \in \{0, 1, 2, \dotsc, n - 1\}$;
- the **magnetic quantum number** $m_{\ell} \in \{-\ell, -(\ell - 1), \dotsc, 0, \ell - 1, \ell\}$.

The [orbital](./Atomic%20Orbitals.md) itself can be expressed in a closed form in [spherical coordinates](../Mathematics/Analysis/Real%20Analysis/Euclidean%20Space/Spherical%20Coordinates.md):

$$\psi_{n,\ell,m_{\ell}}(r, \theta, \phi, t) = R_{n,\ell}(r) Y_{\ell,m_{\ell}} (\theta, \phi) \exp\left(-\frac{\mathrm{i}E_n}{\hbar}t\right)$$

Here, $E_n$ is given as follows:

$$E_n = -\frac{\mu q_N^2 q_e^2}{8 \varepsilon_0^2 h^2} \frac{1}{n^2}$$

- $\mu = \frac{m_N \cdot m_e}{m_N + m_e}$ is the [reduced mass](../Physics/Quantum%20Physics/Schrödinger%20Mechanics/Hydrogen-like%20Atoms%20(Schrödinger%20Mechanics).md), where $m_N, [\mathrm{kg}]$ is the [rest mass](TODO) of the [nucleus](TODO) and $m_e = 9.109\,383\,7139(28) \times 10^{-31}\,\mathrm{kg}$ is the [rest mass](TODO) of the [electron](TODO);
- $q_N, [\mathrm{C}]$ is the total [electric charge](../Physics/Classical%20Electromagnetism/Electric%20Charge.md) of the [nucleus](TODO);
- $q_e = 1.602\,176\,634 \times 10^{-19}\,\mathrm{C}$ is the [electron](TODO)'s [charge](../Physics/Classical%20Electromagnetism/Electric%20Charge.md);
- $\varepsilon_0 = 8.854\,187\,8188(14) \times 10^{-12}\,\mathrm{F\cdot m}^{-1}$ is the [vacuum permittivity](../Physics/Classical%20Electromagnetism/Vacuum%20Permittivity.md);
- $h = 6.626\,070\,15 \times 10^{-34} \,\mathrm{J\cdot s}$ is the [Planck constant](../Physics/Quantum%20Physics/Planck's%20Constant.md);
- $\hbar = \frac{h}{2\uppi}$ is the [reduced Planck constant](../Physics/Quantum%20Physics/Planck's%20Constant.md);
- $n$ is the [principal quantum number](./Atomic%20Orbitals.md) of the [atomic orbital](./Atomic%20Orbitals.md).

We call $R_{n,\ell}(r)$ the **radial wave function**:

$$R_{n,\ell}(r) = \sqrt{\left(\frac{2}{n a_{\mu}}\right)^{2\ell+3}\frac{(n-\ell-1)!}{2n (n+\ell)!}}\cdot r^{\ell} \cdot \exp\left( -\frac{1}{n a_{\mu}}r \right) \cdot \sum_{j=0}^{n-\ell-1} (-1)^j \frac{(n+\ell)!}{(n-\ell-1-j)!(2\ell+1+j)!j!}\left(\frac{2}{n a_{\mu}}\right)^j r^j$$

- $n$ is the [principal quantum number](./Atomic%20Orbitals.md);
- $\ell$ is the [azimuthal quantum number](./Atomic%20Orbitals.md);
- $a_{\mu} = \frac{\varepsilon_0 h^2}{\uppi \mu q_N |q_e|}$ is the **modified Bohr radius**;
- $\mu = \frac{m_N \cdot m_e}{m_N + m_e}$ is the [reduced mass](../Physics/Quantum%20Physics/Schrödinger%20Mechanics/Hydrogen-like%20Atoms%20(Schrödinger%20Mechanics).md), where $m_N, [\mathrm{kg}]$ is the [rest mass](TODO) of the [nucleus](TODO) and $m_e = 9.109\,383\,7139(28) \times 10^{-31}\,\mathrm{kg}$ is the [rest mass](TODO) of the [electron](TODO);

The **angular wave function** $Y_{\ell, m_{\ell}}$ is a [spherical harmonic](TODO):

$$Y_{\ell, m_{\ell}}(\theta, \phi) = (-1)^{\frac{m_{\ell}+|m_{\ell}|}{2}} \sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell - |m_{\ell}|)!}{(\ell + |m_{\ell}|)!}} \frac{\sin^{|m_{\ell}|}\theta}{2^\ell} \left( \sum_{k=0}^{\left\lfloor \frac{\ell - |m_{\ell}|}{2} \right\rfloor} \frac{(-1)^k (2\ell - 2k)!}{k!\, (\ell - k)!\, (\ell - 2k - |m_{\ell}|)!} \cos^{\ell - 2k - |m_{\ell}|}\theta \right) e^{\mathrm{i} m_{\ell}\phi}$$

- $\ell$ is the [azimuthal quantum number](./Atomic%20Orbitals.md);
- $m_{\ell}$ is the [magnetic quantum number](./Atomic%20Orbitals.md).

## Probability Density

Each [atomic orbital](./Atomic%20Orbitals.md) is a stationary state because the resulting probability density is time-independent:

$$\begin{aligned}|\psi_{n,\ell,m}|^2 & = \psi_{n,\ell,m}^{\ast}\psi_{n,\ell,m} \\ & = R_{n,\ell}(r) Y_{\ell,m} (\theta, \phi) \exp\left(+\frac{\mathrm{i}E_n}{\hbar}t\right) R_{n,\ell}(r) Y_{|\ell,m} (\theta, \phi) \exp\left(-\frac{\mathrm{i}E_n}{\hbar}t\right) \\ & = R_{n,\ell}(r)^2 Y_{\ell,m} (\theta, \phi)^2 \exp\left(0\right) \\ & = R_{n,\ell}(r)^2 Y_{\ell,m} (\theta, \phi)^2\end{aligned}$$

