---
tags:
    - network-analysis
    - electrical-engineering
---

# Strictly Linear Multiports

>[!DEFINITION] Definition: Strictly Linear Multiport
>
>An $n$[-port](./Ports.md) is **strictly linear** if its [I-V characteristic](./Ports.md#I-V%20Characteristic) $\mathcal{F}$ is an $n$[-dimensional](../../Mathematics/Algebra/Vector%20Spaces/Hamel%20Bases.md) [subspace](../../Mathematics/Algebra/Vector%20Spaces/Vector%20Spaces.md) of $\mathbb{R}^{2n}$.
>

>[!THEOREM] Theorem: Strict Linearity $\implies$ Affinity
>
>Every [linear](#Strictly%20Linear%20Multiports) [multiport](./Ports.md) is also [affine](./Linear%20Multiports.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Implicit Representation of Linear Multiports
>
>The [I-V characteristic](./Ports.md#I-V%20Characteristic) $\mathcal{F}$ of each [linear](./Strictly%20Linear%20Multiports.md) $n$-[port](./Strictly%20Linear%20Multiports.md) has an [implicit representation](./Ports.md#Representations) as the [kernel](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md) of a [linear](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md) [function](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Functions.md) $f: \mathbb{R}^{2n} \to \mathbb{R}^{n}$:
>
>$$\begin{aligned}\mathcal{F} &= \ker(f) \\ \\ f\left(\begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i} \end{bmatrix}\right) = \boldsymbol{0} &\iff \begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i} \end{bmatrix} \in \mathcal{F} \\ \end{aligned}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!NOTE] Note: Matrix Representation of $f$
>>
>>Since $f$ is a [linear transformation](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md), it can be represented as a [matrix](../../Mathematics/Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) $F$ with $n$ rows and $2n$ columns:
>>
>>$$F \begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i} \end{bmatrix} = 0 \iff \begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i} \end{bmatrix} \in \mathcal{F}$$
>>
>>We can, however, split $F$ exactly into two $n\times n$-[matrices](../../Mathematics/Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) $M$ and $N$, where $M$ holds the first $n$ columns of $F$ and $N$ holds the last $n$ columns of $F$:
>>
>>$$F = \begin{bmatrix} \boldsymbol{M} & \boldsymbol{N} \end{bmatrix} \qquad \boldsymbol{M}, \boldsymbol{N} \in \mathbb{R}^{n\times n}$$
>>
>>If we do this, we get an alternative formulation for the [implicit representation](./Ports.md#Representations):
>>
>>$$\boldsymbol{M}\boldsymbol{v} + \boldsymbol{N}\boldsymbol{i} = \boldsymbol{0}$$
>>
>

>[!THEOREM] Theorem: Parametric Representation of linear Multiports
>
>The [I-V characteristic](./Ports.md#I-V%20Characteristic) $\mathcal{F}$ of each [linear](./Strictly%20Linear%20Multiports.md) $n$-[port](./Strictly%20Linear%20Multiports.md) can be expressed as the [image](../../Mathematics/Analysis/Functions/Functions.md) of a [linear](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md) [function](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Fields/Real%20Vector%20Fields.md) $f: \mathbb{R}^n \to \mathbb{R}^{2n}$:
>
>$$\mathcal{F} = f(\mathbb{R}^n)$$
>
>>[!WARNING] Warning: Non-Uniqueness
>>
>>This $f$ need not be unique.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!NOTE] Note: Matrix Representation of $f$
>>
>>If $\begin{bmatrix}\boldsymbol{v}^{(1)} \\ \boldsymbol{i^{(1)}}\end{bmatrix}, \dotsc, \begin{bmatrix}\boldsymbol{v}^{(n)} \\ \boldsymbol{i^{(n)}}\end{bmatrix}$ are a [basis](../../Mathematics/Algebra/Vector%20Spaces/Hamel%20Bases.md) for $\mathcal{F}$, then the $2n\times n-$[matrix](../../Mathematics/Algebra/Matrices/Real%20Matrices/Real%20Matrices.md)
>>
>>$$\begin{bmatrix}\vert & \vert & \vert \\ \boldsymbol{v}^{(1)} & \cdots & \boldsymbol{v}^{(n)} \\ \vert & \vert & \vert \\ \vert & \vert & \vert \\ \boldsymbol{i^{(1)}} & \cdots & \boldsymbol{i^{(n)}} \\ \vert & \vert & \vert\end{bmatrix}$$
>>
>>is the [matrix representation](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md) of $f$:
>>
>>We thus have:
>>
>>$$\mathcal{F} = \left\{ \begin{bmatrix}\boldsymbol{V} \\ \boldsymbol{I} \end{bmatrix}\in \mathbb{R}^{2n}: \begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i} \end{bmatrix} = \begin{bmatrix}\vert & \vert & \vert \\ \boldsymbol{v}^{(1)} & \cdots & \boldsymbol{v}^{(n)} \\ \vert & \vert & \vert \\ \vert & \vert & \vert \\ \boldsymbol{i^{(1)}} & \cdots & \boldsymbol{i^{(n)}} \\ \vert & \vert & \vert\end{bmatrix} \boldsymbol{\lambda}, \boldsymbol{\lambda} \in \mathbb{R}^n\right\}$$
>>
>>We often denote the aforementioned [matrix](../../Mathematics/Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) as $\begin{bmatrix} \boldsymbol{V} \\ \boldsymbol{I} \end{bmatrix}$, where $\boldsymbol{V} = \begin{bmatrix}\boldsymbol{v}^{(1)} & \cdots & \boldsymbol{v}^{(n)}\end{bmatrix}$ and $\boldsymbol{I} = \begin{bmatrix}\boldsymbol{i^{(1)}} & \cdots & \boldsymbol{i^{(n)}}\end{bmatrix}$:
>>
>>$$\mathcal{F} = \left\{ \begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i} \end{bmatrix}\in \mathbb{R}^{2n}: \begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i} \end{bmatrix} = \begin{bmatrix} \boldsymbol{V} \\ \boldsymbol{I} \end{bmatrix} \boldsymbol{\lambda}, \boldsymbol{\lambda} \in \mathbb{R}^n\right\}$$
>>
>

>[!THEOREM] Theorem: Admittance Parameters
>
>If a [linear multiport](./Strictly%20Linear%20Multiports.md) $\mathcal{F}$ is also [voltage-controlled](./Ports.md#Representations), then its [admittance representation](./Ports.md#Representations) $g$ is a [linear transformation](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md).
>
>>[!DEFINITION] Definition: Admittance Parameters
>>
>>The [standard matrix representation](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md) of $g$ is known as the **admittance matrix** or **conductance matrix** of $\mathcal{F}$ and its components are known as the **admittance parameters** or **conductance parameters** of $\mathcal{F}$.
>>
>>>[!NOTATION]
>>>
>>>The [admittance matrix](./Strictly%20Linear%20Multiports.md) is usually denoted in one of the following ways:
>>>
>>>$$Y \qquad \boldsymbol{Y} \qquad G \qquad \boldsymbol{G}$$
>>>
>>
>
>If $\mathcal{F}$ has an [implicit representation](./Strictly%20Linear%20Multiports.md)
>
>$$\boldsymbol{M}\boldsymbol{v} + \boldsymbol{N}\boldsymbol{i} = \boldsymbol{0} \iff \begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i} \end{bmatrix} \in \mathcal{F}$$
>
>and $\boldsymbol{N}$ is [invertible](../../Mathematics/Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md), then $\mathcal{F}$'s [admittance matrix](./Strictly%20Linear%20Multiports.md) $\boldsymbol{G}$ is
>
>$$\boldsymbol{G} = -\boldsymbol{N}^{-1}\boldsymbol{M}.$$
>
>If $\mathcal{F}$ has a [parametric representation](./Strictly%20Linear%20Multiports.md)
>
>$$\begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix} = \begin{bmatrix} \boldsymbol{V} \\ \boldsymbol{I} \end{bmatrix} \boldsymbol{\lambda},$$
>
>and $\boldsymbol{V}$ is [invertible](../../Mathematics/Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md), then $\mathcal{F}$'s [admittance matrix](./Strictly%20Linear%20Multiports.md) $\boldsymbol{G}$ is
>
>$$\boldsymbol{G} = \boldsymbol{I}\boldsymbol{V}^{-1}.$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Impedance Parameters
>
>If a [linear multiport](./Strictly%20Linear%20Multiports.md) $\mathcal{F}$ is also [current-controlled](./Ports.md#Representations), then its [impedance representation](./Ports.md#Representations) $r$ is a [linear transformation](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md).
>
>>[!DEFINITION] Definition: Impedance Parameters
>>
>>The [standard matrix representation](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md) of $r$ is known as the **impedance matrix** or **resistance matrix** of $\mathcal{F}$ and its components are known as the **impedance parameters** or **resistance parameters** of $\mathcal{F}$.
>>
>>>[!NOTATION]
>>>
>>>The [impedance matrix](./Strictly%20Linear%20Multiports.md) is usually denoted in one of the following ways:
>>>
>>>$$Z \qquad \boldsymbol{Z} \qquad R \qquad \boldsymbol{R}$$
>>>
>>
>
>If $\mathcal{F}$ has an [implicit representation](./Strictly%20Linear%20Multiports.md)
>
>$$\boldsymbol{M}\boldsymbol{v} + \boldsymbol{N}\boldsymbol{i} = \boldsymbol{0}$$
>
>and $\boldsymbol{M}$ is [invertible](../../Mathematics/Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md), then $\mathcal{F}$'s [impedance matrix](./Strictly%20Linear%20Multiports.md) $\boldsymbol{R}$ is
>
>$$\boldsymbol{R} = -\boldsymbol{M}^{-1}\boldsymbol{N}.$$
>
>If $\mathcal{F}$ has a [parametric representation](./Strictly%20Linear%20Multiports.md)
>
>$$\begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix} = \begin{bmatrix} \boldsymbol{V} \\ \boldsymbol{I} \end{bmatrix} \boldsymbol{\lambda},$$
>
>and $\boldsymbol{I}$ is [invertible](../../Mathematics/Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md), then $\mathcal{F}$'s [impedance matrix](./Strictly%20Linear%20Multiports.md) $\boldsymbol{R}$ is
>
>$$\boldsymbol{R} = \boldsymbol{V}\boldsymbol{I}^{-1}.$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Inverse Hybrid Representations
>
>If a [linear multiport](./Strictly%20Linear%20Multiports.md) $\mathcal{F}$ has an [inverse hybrid representation](./Ports.md#Representation)
>
>$$\begin{bmatrix}\boldsymbol{i}_a \\ \boldsymbol{v}_b \end{bmatrix}= H'\left( \begin{bmatrix}\boldsymbol{v}_a \\ \boldsymbol{i}_b\end{bmatrix} \right),$$
>
>where
>
>$$\boldsymbol{i}_a = \begin{bmatrix} i_1 \\ \vdots \\ i_m\end{bmatrix} \qquad \boldsymbol{v}_a = \begin{bmatrix} v_1 \\ \vdots \\ v_m\end{bmatrix} \qquad \boldsymbol{i}_b = \begin{bmatrix} i_{m+1} \\ \vdots \\ i_n \end{bmatrix} \qquad \boldsymbol{v}_b = \begin{bmatrix} v_{m+1} \\ \vdots \\ v_n\end{bmatrix}$$
>
>for some $m \in \{1, \dotsc, n\}$, then $H'$ is [linear](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md):
>
>$$\begin{bmatrix}\boldsymbol{i}_a \\ \boldsymbol{v}_b \end{bmatrix} = \boldsymbol{H}' \begin{bmatrix}\boldsymbol{v}_a \\ \boldsymbol{i}_b\end{bmatrix}$$
>
>We can further divide $\boldsymbol{H}'$ into four [matrices](../../Mathematics/Algebra/Matrices/Matrices.md):
>
>$$\boldsymbol{H}' = \begin{bmatrix} \boldsymbol{H}_{a,a}' & \boldsymbol{H}_{a,b}' \\ \boldsymbol{H}_{b,a}' & \boldsymbol{H}_{b,b}' \end{bmatrix}$$
>
>- $\boldsymbol{H}_{a,a}'$ contains entries $H_{jk}'$ where $j, k \in \{1, \dotsc, m\}$;
>- $\boldsymbol{H}_{a,b}'$ contains entries $H_{jk}'$ where $j \in \{1, \dotsc, m\}$ and $k \in \{m+1, \dotsc, n\}$;
>- $\boldsymbol{H}_{b,a}'$ contains entries $H_{jk}'$ where $j \in \{m+1, \dotsc, n\}$ and $k \in \{1, \dotsc, m\}$;
>- $\boldsymbol{H}_{b,b}'$ contains entries $H_{jk}'$ where $j, k \in \{m+1, \dotsc, n\}$.
>
>We then have:
>
>$$\boldsymbol{v} = \begin{bmatrix} \boldsymbol{v}_a \\ \boldsymbol{v}_b\end{bmatrix} = \begin{bmatrix}\boldsymbol{1} & \boldsymbol{0} \\ \boldsymbol{H}_{b, a}' & \boldsymbol{H}_{b, b}'\end{bmatrix}\begin{bmatrix} \boldsymbol{v}_a \\ \boldsymbol{i}_b \end{bmatrix} \qquad \boldsymbol{i} = \begin{bmatrix} \boldsymbol{i}_a \\ \boldsymbol{i}_b\end{bmatrix} = \begin{bmatrix} \boldsymbol{H}_{a, a}' & \boldsymbol{H}_{a, b}' \\ \boldsymbol{0} & \boldsymbol{1} \end{bmatrix} \begin{bmatrix} \boldsymbol{v}_a \\ \boldsymbol{i}_b \end{bmatrix}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Power

>[!THEOREM] Theorem: Losslessness of linear Multiports
>
>Let $\mathcal{F}$ be a [linear multiport](#Linear%20Multiports).
>
>If $\mathcal{F}$ has a [parametric representation](./Ports.md) $\begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix} = \begin{bmatrix}\boldsymbol{V} \\ \boldsymbol{I}\end{bmatrix}\boldsymbol{\lambda}$, then it is [lossless](./Ports.md#Power) if and only if $\boldsymbol{V}^{\mathsf{T}} \boldsymbol{I} + \boldsymbol{I}^{\mathsf{T}}\boldsymbol{V} = \boldsymbol{0}$.
>
>If $\mathcal{F}$ has an [admittance representation](./Strictly%20Linear%20Multiports.md) $\boldsymbol{i} = \boldsymbol{Y}\boldsymbol{v}$, then it is [lossless](./Ports.md#Power) if and only if $\boldsymbol{Y}$ is [skew symmetric](../../Mathematics/Algebra/Matrices/Square%20Matrices/Symmetric%20Matrices.md), i.e. $\boldsymbol{Y} = -\boldsymbol{Y}^{\mathsf{T}}$.
>
>If $\mathcal{F}$ has an [impedance representation](./Strictly%20Linear%20Multiports.md) $\boldsymbol{v} = \boldsymbol{Z}\boldsymbol{i}$, then it is [lossless](./Ports.md#Power) if and only if $\boldsymbol{Z}$ is [skew symmetric](../../Mathematics/Algebra/Matrices/Square%20Matrices/Symmetric%20Matrices.md), i.e. $\boldsymbol{Z} = -\boldsymbol{Z}^{\mathsf{T}}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Passivity of linear Multiports
>
>A [linear multiport](#Linear%20Multiports) with a [parametric representation](./Ports.md)
>
>$$\begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix} = \begin{bmatrix}\boldsymbol{V} \\ \boldsymbol{I}\end{bmatrix}\boldsymbol{\lambda}$$
>
>is [passive](./Ports.md#Power) if and only if $\boldsymbol{V}^{\mathsf{T}} \boldsymbol{I} + \boldsymbol{I}^{\mathsf{T}}\boldsymbol{V}$ is [positive semi-definite](../../Mathematics/Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md):
>
>$$\boldsymbol{V}^{\mathsf{T}} \boldsymbol{I} + \boldsymbol{I}^{\mathsf{T}}\boldsymbol{V} \succeq \boldsymbol{0}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Activity of linear Multiports
>
>A [linear multiport](#Linear%20Multiports) with a [parametric representation](./Ports.md)
>
>$$\begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix} = \begin{bmatrix}\boldsymbol{V} \\ \boldsymbol{I}\end{bmatrix}\boldsymbol{\lambda}$$
>
>is [active](./Ports.md#Power) if and only if $\boldsymbol{V}^{\mathsf{T}} \boldsymbol{I} + \boldsymbol{I}^{\mathsf{T}}\boldsymbol{V}$ is *not* [positive semi-definite](../../Mathematics/Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md):
>
>$$\boldsymbol{V}^{\mathsf{T}} \boldsymbol{I} + \boldsymbol{I}^{\mathsf{T}}\boldsymbol{V} \not\succeq \boldsymbol{0}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Duality

>[!THEOREM] Theorem: Duality of linear Multiports
>
>Let $\mathcal{F}$ and $\mathcal{G}$ be [linear multiports](./Strictly%20Linear%20Multiports.md) with the following [parametric representations](./Ports.md#Represetations):
>
>$$\begin{aligned}\mathcal{F} &= \left\{ \begin{bmatrix} \boldsymbol{v} \\ \boldsymbol{i} \end{bmatrix} \in \mathbb{R}^{2n} : \begin{bmatrix} \boldsymbol{v} \\ \boldsymbol{i} \end{bmatrix} = \begin{bmatrix}\boldsymbol{V}_{\mathcal{F}} \\ \boldsymbol{I}_{\mathcal{F}} \end{bmatrix} \boldsymbol{\lambda}, \boldsymbol{\lambda} \in \mathbb{R}^{n} \right\} \\ \mathcal{G} &= \left\{ \begin{bmatrix} \boldsymbol{v} \\ \boldsymbol{i} \end{bmatrix} \in \mathbb{R}^{2n} : \begin{bmatrix} \boldsymbol{v} \\ \boldsymbol{i} \end{bmatrix} = \begin{bmatrix}\boldsymbol{V}_{\mathcal{G}} \\ \boldsymbol{I}_{\mathcal{G}} \end{bmatrix} \boldsymbol{\lambda}, \boldsymbol{\lambda} \in \mathbb{R}^{n} \right\} \end{aligned}$$
>
>If $\mathcal{F}$ and $\mathcal{G}$ are [dual](./Ports.md#Duality) with [duality constant](./Ports.md#Duality) $D$, then
>
>$$\begin{bmatrix}\boldsymbol{V}_{\mathcal{G}} \\ \boldsymbol{I}_{\mathcal{G}}\end{bmatrix} = \begin{bmatrix}D\boldsymbol{I}_{\mathcal{F}} \\ \frac{1}{D}\boldsymbol{V}_{\mathcal{F}}\end{bmatrix}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Reciprocity

>[!DEFINITION] Definition: Reciprocity
>
>An $n$-[port](./Ports.md) is **reciprocal** if
>
>$$\boldsymbol{v}_a^{\mathsf{T}}\boldsymbol{i}_b = \boldsymbol{v}_b^{\mathsf{T}}\boldsymbol{i}_a$$
>
>for all $(\boldsymbol{v}_a, \boldsymbol{i}_a) \in \mathcal{F}$ and all $(\boldsymbol{v}_b, \boldsymbol{i}_b) \in \mathcal{F}$.
>

>[!THEOREM] Theorem: Reciprocity $\implies$ Linearity
>
>If a [multiport](./Ports.md) is [reciprocal](#Reciprocity), then it is also [linear](#Linear%20Multiports).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Reciprocity via Parametric Representations
>
>If a [linear](#Linear%20Multiports) [multiport](./Ports.md) $\mathcal{F}$ has an [implicit representation](#Strictly-Linear%20Two-Ports)
>
>$$\begin{bmatrix} \boldsymbol{v} \\ \boldsymbol{i} \end{bmatrix} = \begin{bmatrix}\boldsymbol{V} \\ \boldsymbol{I}\end{bmatrix} \boldsymbol{\lambda},$$
>
>then it is [reciprocal](#Reciprocity) if and only if
>
>$$\boldsymbol{V}^{\mathsf{T}}\boldsymbol{I} - \boldsymbol{I}^{\mathsf{T}}\boldsymbol{V} = \boldsymbol{0}.$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Reciprocity via Explicit Representations
>
>Let $\mathcal{F}$ be a [linear](#Linear%20Multiports) [multiport](./Ports.md)
>
>If $\mathcal{F}$ has an [admittance matrix](#Linear%20Multiports) $\boldsymbol{G}$, then it is [reciprocal](#Reciprocity) if and only if $\boldsymbol{G}$ is [symmetric](../../Mathematics/Algebra/Matrices/Square%20Matrices/Symmetric%20Matrices.md):
>
>$$\boldsymbol{G} = \boldsymbol{G}^{\mathsf{T}}$$
>
>If $\mathcal{F}$ has an [impedance matrix](#Linear%20Multiports) $\boldsymbol{R}$, then it is [reciprocal](#Reciprocity) if and only if $\boldsymbol{R}$ is [symmetric](../../Mathematics/Algebra/Matrices/Square%20Matrices/Symmetric%20Matrices.md):
>
>$$\boldsymbol{R} = \boldsymbol{R}^{\mathsf{T}}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>