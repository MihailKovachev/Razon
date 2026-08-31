---
title: Linear Two-Ports
tags:
    - circuit-theory
    - electrical-engineering
---

# Linear Two-Ports

A [two-port](./Two-Ports.md) is [strictly linear](../Strictly%20Linear%20Multiports.md) if its [I-V characteristic](./Two-Ports.md#I-V%20Characteristic) is a [two-dimensional](../../../Mathematics/Algebra/Vector%20Spaces/Hamel%20Bases.md) [subspace](../../../Mathematics/Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $\mathbb{R}^4$.

## Representations

>[!INFO] Info: Implicit Representation
>
>A [strictly linear two-port](#Strictly%20Linear%20Two-Ports) has an [implicit representation](../Strictly%20Linear%20Multiports.md)
>
>$$
>\boldsymbol{M} \boldsymbol{v} + \boldsymbol{N} \boldsymbol{i} = \boldsymbol{0},
>$$
>
>where $\boldsymbol{M} \in \mathbb{R}^{2\times 2}$ and $\boldsymbol{N} \in \mathbb{R}^{2 \times 2}$.
>

>[!INFO] Info: Parametric Representation
>
>A [strictly linear two-port](#Strictly%20Linear%20Two-Ports) has a [parametric representation](../Ports.md)
>
>$$
>\begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix} = \begin{bmatrix}\boldsymbol{V} \\ \boldsymbol{I}\end{bmatrix}\boldsymbol{\lambda}
>$$
>
>where $\boldsymbol{V} \in \mathbb{R}^{2\times 2}$ and $\boldsymbol{I} \in \mathbb{R}^{2 \times 2}$.
>

>[!THEOREM] Theorem: Conversions between Implicit and Explicit Representations
>
>Let $\mathcal{F}$ be a [two-port](./Two-Ports.md) with the following [implicit representation](../Ports.md):
>
>$$
>\boldsymbol{M}\boldsymbol{v} + \boldsymbol{N}\boldsymbol{i} = \boldsymbol{0},
>$$
>
>where
>
>$$
>\boldsymbol{M} = \begin{bmatrix}\vert & \vert \\ \boldsymbol{m}_1 & \boldsymbol{m}_2 \\ \vert & \vert \end{bmatrix} \qquad \boldsymbol{N} = \begin{bmatrix}\vert & \vert \\ \boldsymbol{n}_1 & \boldsymbol{n}_2 \\ \vert & \vert \end{bmatrix}.
>$$
>
>The [explicit representations](./Two-Ports.md#Representations) of $\mathcal{F}$ are given below, provided the respective [matrix inverses](../../../Mathematics/Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md) exist:
>
>|$\boldsymbol{G}$|$\boldsymbol{R}$|$\boldsymbol{H}$|$\boldsymbol{H}'$|$\boldsymbol{T}$|$\boldsymbol{T}'$|$\boldsymbol{T}'$ defined via $\begin{bmatrix} V_2 \\ I_2 \end{bmatrix} = T^{-1}\left(\begin{bmatrix}V_1 \\ -I_1\end{bmatrix}\right)$|
>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>|$-\boldsymbol{N}^{-1}\boldsymbol{M}$|$-\boldsymbol{M}^{-1}\boldsymbol{N}$|$-\begin{bmatrix}\vert & \vert \\ \boldsymbol{m}_1 & \boldsymbol{n}_2 \\ \vert & \vert\end{bmatrix}^{-1}\begin{bmatrix}\vert & \vert \\ \boldsymbol{n}_1 & \boldsymbol{m}_2 \\ \vert & \vert\end{bmatrix}$|$-\begin{bmatrix}\vert & \vert \\ \boldsymbol{n}_1 & \boldsymbol{m}_2 \\ \vert & \vert\end{bmatrix}^{-1}\begin{bmatrix}\vert & \vert \\ \boldsymbol{m}_1 & \boldsymbol{n}_2 \\ \vert & \vert\end{bmatrix}$|$-\begin{bmatrix}\vert & \vert \\ \boldsymbol{m}_1 & \boldsymbol{n}_1 \\ \vert & \vert\end{bmatrix}^{-1}\begin{bmatrix}\vert & \vert \\ \boldsymbol{m}_2 & -\boldsymbol{n}_2 \\ \vert & \vert\end{bmatrix}$|$-\begin{bmatrix}\vert & \vert \\ \boldsymbol{m}_2 & -\boldsymbol{n}_2 \\ \vert & \vert\end{bmatrix}^{-1}\begin{bmatrix}\vert & \vert \\ \boldsymbol{m}_1 & \boldsymbol{n}_1 \\ \vert & \vert\end{bmatrix}$|$-\begin{bmatrix}\vert & \vert \\ \boldsymbol{m}_2 & \boldsymbol{n}_2 \\ \vert & \vert\end{bmatrix}^{-1}\begin{bmatrix}\vert & \vert \\ \boldsymbol{m}_1 & -\boldsymbol{n}_1 \\ \vert & \vert\end{bmatrix}$|
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Conversions between Explicit Representations
>
>If all six [explicit representations](./Two-Ports.md) exist and are [linear](../../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md), then their [standard matrix representations](../../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md) are related as follows:
>
>||$R$|$G$|$H$|$H'$|$T$|$T'$|$T'$ defined via $\begin{bmatrix} V_2 \\ I_2 \end{bmatrix} = T'\left(\begin{bmatrix}V_1 \\ -I_1\end{bmatrix}\right)$|
>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>|$R$|$\displaystyle\begin{bmatrix}r_{11} & r_{12} \\ r_{21} & r_{22}\end{bmatrix}$|$\displaystyle\frac{1}{\det G} \begin{bmatrix}g_{22} & -g_{12} \\ -g_{21} & g_{11}\end{bmatrix}$|$\displaystyle\frac{1}{h_{22}}\begin{bmatrix}\det H & h_{12} \\ -h_{21} & 1\end{bmatrix}$|$\displaystyle\frac{1}{h_{11}'}\begin{bmatrix}1 & -h_{12}' \\ h_{21}' & \det H'\end{bmatrix}$|$\displaystyle\frac{1}{t_{21}}\begin{bmatrix}t_{11} & \det T \\ 1 & t_{22}\end{bmatrix}$|TODO|$\displaystyle\frac{1}{t_{21}'}\begin{bmatrix}t_{22}' & 1 \\ \det T' & t_{11}'\end{bmatrix}$|
>|$G$|$\displaystyle\frac{1}{\det R} \begin{bmatrix}r_{22} & -r_{12} \\ -r_{21} & r_{11}\end{bmatrix}$|$\displaystyle\begin{bmatrix}g_{11} & g_{12} \\ g_{21} & g_{22}\end{bmatrix}$|$\displaystyle\frac{1}{h_{11}} \begin{bmatrix}1 & -h_{12} \\ h_{21} & \det H\end{bmatrix}$|$\displaystyle\frac{1}{h_{22}'} \begin{bmatrix}\det H' & h_{12}' \\ -h_{21}' & 1\end{bmatrix}$|$\displaystyle\frac{1}{t_{12}}\begin{bmatrix}t_{22} & -\det T \\ -1 & t_{11}\end{bmatrix}$|TODO|$\displaystyle\frac{1}{t_{12}'}\begin{bmatrix}t_{11}' & -1 \\ -\det T' & t_{22}'\end{bmatrix}$|
>|$H$|$\displaystyle\frac{1}{r_{22}}\begin{bmatrix}\det R & r_{12} \\ -r_{21} & 1\end{bmatrix}$|$\displaystyle\frac{1}{g_{11}}\begin{bmatrix}1 & -g_{12} \\ g_{21} & \det G\end{bmatrix}$|$\displaystyle\begin{bmatrix}h_{11} & h_{12} \\ h_{21} & h_{22}\end{bmatrix}$|$\displaystyle\frac{1}{\det H'}\begin{bmatrix}h_{22}' & -h_{12}' \\ -h_{21}' & h_{11}'\end{bmatrix}$|$\displaystyle\frac{1}{t_{22}}\begin{bmatrix}t_{12} & \det T \\ -1 & t_{21}\end{bmatrix}$|TODO|$\displaystyle \frac{1}{t_{11}'}\begin{bmatrix}t_{12}' & 1 \\ -\det T' & t_{21}'\end{bmatrix}$|
>|$H'$|$\displaystyle\frac{1}{r_{11}}\begin{bmatrix}1 & -r_{12} \\ r_{21} & \det R\end{bmatrix}$|$\displaystyle\frac{1}{g_{22}}\begin{bmatrix}\det G & g_{12} \\ -g_{21} & 1\end{bmatrix}$|$\displaystyle\frac{1}{\det H} \begin{bmatrix}h_{22} & -h_{12} \\ -h_{21} & h_{11}\end{bmatrix}$|$\displaystyle\begin{bmatrix}h_{11}' & h_{12}' \\ h_{21}' & h_{22}'\end{bmatrix}$|$\displaystyle\frac{1}{t_{11}}\begin{bmatrix}t_{21} & -\det T \\ 1 & t_{12}\end{bmatrix}$|TODO|$\displaystyle \frac{1}{t_{22}'} \begin{bmatrix}t_{21}' & -1 \\ \det T' & t_{12}'\end{bmatrix}$|
>|$T$|$\displaystyle\frac{1}{r_{21}}\begin{bmatrix}r_{11} & \det R \\ 1 & r_{22}\end{bmatrix}$|$\displaystyle\frac{1}{g_{21}}\begin{bmatrix}-g_{22} & -1 \\ -\det G & -g_{11}\end{bmatrix}$|$\displaystyle\frac{1}{h_{21}}\begin{bmatrix}-\det H & -h_{11} \\ -h_{22} & -1\end{bmatrix}$|$\displaystyle\frac{1}{h_{21}'}\begin{bmatrix}1 & h_{22}' \\ h_{11}' & \det H'\end{bmatrix}$|$\displaystyle\begin{bmatrix}t_{11} & t_{12} \\ t_{21} & t_{22}\end{bmatrix}$|$\displaystyle\frac{1}{\det T'}\begin{bmatrix}t_{22}' & -t_{12}' \\ -t_{21}' & t_{11}'\end{bmatrix}$|$\displaystyle \frac{1}{\det T'} \begin{bmatrix}t_{22}' & t_{12}' \\ t_{21}' & t_{11}'\end{bmatrix}$|
>|$T'$|TODO|TODO|TODO|TODO|$\displaystyle\frac{1}{\det T}\begin{bmatrix}t_{22} & -t_{12} \\ -t_{21} & t_{11}\end{bmatrix}$|$\displaystyle\begin{bmatrix}t_{11}' & t_{12}' \\ t_{21}' & t_{22}'\end{bmatrix}$|TODO|
>|$T'$ **defined via** $\begin{bmatrix} V_2 \\ I_2 \end{bmatrix} = T'\left(\begin{bmatrix}V_1 \\ -I_1\end{bmatrix}\right)$|$\displaystyle \frac{1}{r_{12}}\begin{bmatrix}r_{22} & \det R \\ 1 & r_{11}\end{bmatrix}$|$\displaystyle \frac{1}{g_{12}} \begin{bmatrix}-g_{11} & -1 \\ -\det G & -g_{22}\end{bmatrix}$|$\displaystyle \frac{1}{h_{12}} \begin{bmatrix}1 & h_{11} \\ h_{22} & \det H\end{bmatrix}$|$\displaystyle \frac{1}{h_{12}'} \begin{bmatrix}- \det H' & -h_{22}' \\ -h_{11}' & -1\end{bmatrix}$|$\displaystyle \frac{1}{\det T} \begin{bmatrix}t_{22} & t_{12} \\ t_{21} & t_{11}\end{bmatrix}$|TODO|$\displaystyle\begin{bmatrix}t_{11}' & t_{12}' \\ t_{21}' & t_{22}'\end{bmatrix}$|
>
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Reciprocity

>[!THEOREM] Theorem: Reciprocity Based on Elements
>
>If a [two-port](./Two-Ports.md) does not contain any elements other than [linear resistors](../../Analog%20Circuits/Resistors.md), [transformers](../../Analog%20Circuits/Immittance%20Converters/Transformers.md), [capacitors](TODO) and [inductors](TODO), then it is [reciprocal](../Strictly%20Linear%20Multiports.md#Reciprocity).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Ratios of Reciprocal Two-Ports
>
>Let $\mathcal{F}$ be a [strictly linear two-port](./Linear%20Two-Ports.md).
>
>If $\mathcal{F}$ is [reciprocal](../Strictly%20Linear%20Multiports.md#Reciprocity), then we have the following properties:
>- The ratio of $v_1$ to $v_2$ whenever $i_1 = 0$ is the same as the negative of the ratio of $i_2$ to $i_1$ whenever $v_2 = 0$.
>
>$$
>\left.\frac{v_1}{v_2}\right\vert_{i_1 = 0} = \left.-\frac{i_2}{i_1}\right\vert_{v_2 = 0}
>$$
>
>- The ratio of $v_2$ to $v_1$ whenever $i_2 = 0$ is the same as the negative of the ratio of $i_1$ to $i_2$ whenever $v_1 = 0$.
>
>$$
>\left.\frac{v_2}{v_1}\right\vert_{i_2 = 0} = \left. -\frac{i_1}{i_2}\right\vert_{v_1 = 0}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Reciprocity via Transmission Representation
>
>If $\mathcal{F}$ has a [forwards transmission matrix](#Strictly%20Linear%20Multiports) $\boldsymbol{T}$, then it is [reciprocal](../Strictly%20Linear%20Multiports.md#Reciprocity) if and only if the [determinant](../../../Mathematics/Algebra/Matrices/Square%20Matrices/Determinants.md) of $\boldsymbol{T}$ is $1$:
>
>$$
>\det \boldsymbol{T} = 1
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Symmetry

>[!THEOREM] Theorem: Symmetry via Admittance Representation
>
>A [strictly linear](#Strictly%20Linear%20Two-Ports) [two-port](./Two-Ports.md) with [admittance representation](#Strictly%20Linear%20Two-Ports)
>
>$$
>\boldsymbol{i} = \boldsymbol{G} \boldsymbol{v}
>$$
>
>is [symmetrical](./Two-Ports.md#Symmetry) if and only if
>
>$$
>\boldsymbol{G} = \begin{bmatrix}0 & 1 \\ 1 & 0\end{bmatrix}\boldsymbol{G}\begin{bmatrix}0 & 1 \\ 1 & 0\end{bmatrix},
>$$
>
>i.e. $\boldsymbol{G}$ remains the same if you swap the elements on its diagonals.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Symmetry via Impedance Representation
>
>A [strictly linear](#Strictly%20Linear%20Two-Ports) [two-port](./Two-Ports.md) with [impedance representation](#Strictly%20Linear%20Two-Ports)
>
>$$
>\boldsymbol{v} = \boldsymbol{R} \boldsymbol{i}
>$$
>
>is [symmetrical](./Two-Ports.md#Symmetry) if and only if
>
>$$
>\boldsymbol{R} = \begin{bmatrix}0 & 1 \\ 1 & 0\end{bmatrix}\boldsymbol{R}\begin{bmatrix}0 & 1 \\ 1 & 0\end{bmatrix},
>$$
>
>i.e. $\boldsymbol{R}$ remains the same if you swap the elements on its diagonals.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Symmetry via Transmission Representations
>
>A [strictly linear](#Strictly%20Linear%20Two-Ports) [two-port](./Two-Ports.md) with existing [forwards transmission representation](./Two-Ports.md#Representations)
>
>$$
>\begin{bmatrix} v_1 \\ i_1 \end{bmatrix} = \boldsymbol{T} \begin{bmatrix}v_2 \\ -i_2\end{bmatrix}
>$$
>
>and [backwards transmission representation](./Two-Ports.md#Representations)
>
>$$
>\begin{bmatrix} v_2 \\ i_2 \end{bmatrix} = \boldsymbol{T}' \begin{bmatrix}v_1 \\ -i_1\end{bmatrix}
>$$
>
>is [symmetrical](./Two-Ports.md#Symmetry) if and only if
>
>$$
>\boldsymbol{T} = \boldsymbol{T}'.
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Symmetry $\implies$ Reciprocity
>
>If a [strictly linear two-port](./Linear%20Two-Ports.md) [two-port](./Two-Ports.md) is [symmetrical](./Two-Ports.md#Symmetry), then it is also [reciprocal](../Strictly%20Linear%20Multiports.md#Reciprocity).
>
>>[!PROOF]-
>>
>>TODO
>>
>