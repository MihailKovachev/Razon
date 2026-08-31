---
tags:
    - network-analysis
    - electrical-engineering
---

# Linear Multiports

>[!DEFINITION] Definition: Linear Multiport
>
>An $n$[-port](./Ports.md) is **linear** if its [I-V characteristic](./Ports.md#I-V%20Characteristic) $\mathcal{F}$ is an $n$-[dimensional](TODO) [affine subspace](TODO) of $\mathbb{R}^{2n}$.
>

## Representations

>[!THEOREM] Theorem: Existence of an Affine Implicit Representation
>
>Let $\mathcal{F}$ be the [I-V characteristic](./Ports.md#I-V%20Characteristic) of an $n$-[port](./Ports.md).
>
>If $\mathcal{F}$ is [affine](./Linear%20Multiports.md), then $\mathcal{F}$ has an [implicit representation](./Ports.md#Representations) 
>
>$$f\left(\begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix}\right) = \boldsymbol{0} \qquad \iff \qquad \begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix} \in \mathcal{F},$$
>
>where $f: \mathbb{R}^{2n} \to \mathbb{R}^{n}$ is an [affine](TODO) [function](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Functions.md).
>
>Specifically, there exist a [surjective](../../Mathematics/Analysis/Functions/Injections,%20Surjections%20and%20Bijections.md) [linear](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md) [function](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Functions.md) $f_{\text{lin}}: \mathbb{R}^{2n} \to \mathbb{R}^{n}$ and some $\boldsymbol{c} \in \mathbb{R}^n$ such that
>
>$$f\left(\begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix}\right) = f_{\text{lin}}\left(\begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix}\right) + \boldsymbol{c}.$$
>
>In other words:
>
>$$f_{\text{lin}}\left(\begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix}\right) + \boldsymbol{c} = \boldsymbol{0} \iff \begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix} \in \mathcal{F}$$
>
>>[!NOTATION] Notation: Matrix Representation of $f$
>>
>>Since $f_{\text{lin}}$ is a [linear transformation](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md), it can be represented as a [matrix](../../Mathematics/Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) $F$ with $n$ rows and $2n$ columns:
>>
>>$$F \begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i} \end{bmatrix} + \boldsymbol{c} = 0 \iff \begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i} \end{bmatrix} \in \mathcal{F}$$
>>
>>We can, however, split $F$ exactly into two $n\times n$-[matrices](../../Mathematics/Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) $\boldsymbol{A}$ and $\boldsymbol{B}$, where $\boldsymbol{A}$ holds the first $n$ columns of $F$ and $\boldsymbol{B}$ holds the last $n$ columns of $F$:
>>
>>$$F = \begin{bmatrix} \boldsymbol{A} & \boldsymbol{B} \end{bmatrix} \qquad \boldsymbol{A}, \boldsymbol{B} \in \mathbb{R}^{n\times n}$$
>>
>>If we do this, we get an alternative formulation for the [implicit representation](./Ports.md#Representations):
>>
>>$$\boldsymbol{A}\boldsymbol{v} + \boldsymbol{B}\boldsymbol{i} = \boldsymbol{e} \qquad \boldsymbol{e} = -\boldsymbol{c}$$
>>
>>Sometimes, we also use $\boldsymbol{M}$ and $\boldsymbol{N}$ for $\boldsymbol{A}$ and $\boldsymbol{B}$, respectively.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Parametric Representation of Affine Multiports
>
>Let $\mathcal{F}$ be an [affine](./Linear%20Multiports.md) $n$-[port](./Ports.md), let $\begin{bmatrix}\boldsymbol{v}_0 \\ \boldsymbol{i_0}\end{bmatrix}, \begin{bmatrix}\boldsymbol{v}^{(1)} \\ \boldsymbol{i^{(1)}}\end{bmatrix}, \dotsc, \begin{bmatrix}\boldsymbol{v}^{(n)} \\ \boldsymbol{i^{(n)}}\end{bmatrix} \in \mathcal{F}$, let $\Delta\boldsymbol{v}^{(k)} = \boldsymbol{v}^{(k)} - \boldsymbol{v}_0$ and let $\Delta \boldsymbol{i}^{(k)} = \boldsymbol{i}^{(k)} - \boldsymbol{i}_0$.
>
>If $\begin{bmatrix}\Delta\boldsymbol{v}^{(1)} \\ \Delta \boldsymbol{i}^{(1)}\end{bmatrix}, \dotsc, \begin{bmatrix}\Delta\boldsymbol{v}^{(n)} \\ \Delta \boldsymbol{i}^{(n)}\end{bmatrix}$ are [linearly independent](../../Mathematics/Algebra/Vector%20Spaces/Linear%20Combinations.md#Linear%20Independence), then
>
>$$\begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix} = \begin{bmatrix}\vert & \vert & \vert \\ \Delta\boldsymbol{v}^{(1)} & \cdots & \Delta\boldsymbol{v}^{(n)} \\ \vert & \vert & \vert \\ \vert & \vert & \vert \\ \Delta \boldsymbol{i}^{(1)} & \cdots & \Delta \boldsymbol{i}^{(n)}\\ \vert & \vert & \vert\end{bmatrix}\boldsymbol{\lambda} + \begin{bmatrix}\boldsymbol{v}_0 \\ \boldsymbol{i_0}\end{bmatrix}$$
>
>is a [parametric representation](./Ports.md#Representations) of $\mathcal{F}$.
>
>>[!NOTATION]
>>
>>We often denote the aforementioned [matrix](../../Mathematics/Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) as $\begin{bmatrix} \boldsymbol{V} \\ \boldsymbol{I} \end{bmatrix}$, where:
>>
>>$$\boldsymbol{V} = \begin{bmatrix}\vert & \vert & \vert \\ \Delta \boldsymbol{v}^{(1)} & \cdots & \Delta \boldsymbol{v}^{(n)} \\ \vert & \vert & \vert\end{bmatrix} \qquad \boldsymbol{I} = \begin{bmatrix}\vert & \vert & \vert \\ \Delta \boldsymbol{i}^{(1)} & \cdots & \Delta \boldsymbol{i}^{(n)} \\ \vert & \vert & \vert \end{bmatrix}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Linearization

>[!DEFINITION] Definition: Linearization
>
>Suppose we have an $n$[-port](./Ports.md) with [I-V characteristic](./Ports.md#I-V%20Characteristic) $\mathcal{F}$ and a point $(\boldsymbol{v}_0, \boldsymbol{i}_0) \in \mathcal{F}$.
>
>**Linearization** is the process of finding an [affine multiport](./Strictly%20Linear%20Multiports.md) whose [I-V characteristic](./Network%20Analysis.md#I-V%20Characteristic) $\mathcal{F}_{\text{affine}}$ resembles $\mathcal{F}$ as much as possible around the point $(\boldsymbol{v}_0, \boldsymbol{i}_0)$.
>

>[!THEOREM] Theorem: Linearization via Implicit Representations
>
>Suppose we have a non-linear $n$[-port](./Ports.md) with [I-V characteristic](./Ports.md#I-V%20Characteristic) $\mathcal{F}$ and a point $(\boldsymbol{v}_0, \boldsymbol{i}_0) \in \mathcal{F}$.
>
>If $\mathcal{F}$ has an [implicit representation](./Ports.md#Representations)
>
>$$f\left(\begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix}\right) = \boldsymbol{0},$$
>
>then the [I-V characteristic](./Ports.md#I-V%20Characteristic) $\mathcal{F}_{\text{affine}}$ of the $n$[-port](./Ports.md) which best approximates $\mathcal{F}$ around $(\boldsymbol{v}_0, \boldsymbol{i}_0)$ has an [implicit representation](./Ports.md#Representations) which can be obtained using the [Jacobian](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md#Differentiability) of $f$:
>
>$$\left.\mathbf{J}_f\right\vert_{(\boldsymbol{v}_0, \boldsymbol{i}_0)}\left(\begin{bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix} -\begin{bmatrix}\boldsymbol{v}_0 \\ \boldsymbol{i}_0\end{bmatrix}\right) = \boldsymbol{0}$$
>
>>[!NOTATION] Notation
>>
>>The [Jacobian](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md#Differentiability) $\mathbf{J}_f$ has $n$ rows and $2n$ columns which means that we can split it into two $n\times n$ [matrices](../../Mathematics/Algebra/Matrices/Real%20Matrices/Real%20Matrices.md), denoted as $\frac{\partial f}{\partial \boldsymbol{v}}$ and $\frac{\partial f}{\partial \boldsymbol{i}}$:
>>
>>$$\mathbf{J}_f = \begin{bmatrix}\frac{\partial f}{\partial \boldsymbol{v}} & \frac{\partial f}{\partial \boldsymbol{i}}\end{bmatrix}$$
>>
>>The above equation can thus be rewritten in the following form:
>>
>>$$\left.\frac{\partial f}{\partial \boldsymbol{v}}\right\vert_{(\boldsymbol{v}_0, \boldsymbol{i}_0)}(\boldsymbol{v} - \boldsymbol{v}_0) + \left.\frac{\partial f}{\partial \boldsymbol{i}}\right\vert_{(\boldsymbol{v}_0, \boldsymbol{i}_0)}(\boldsymbol{i} - \boldsymbol{i}_0) = \boldsymbol{0}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Linearization via Explicit Representations
>
>Suppose we have an $n$[-port](./Ports.md) with [I-V characteristic](./Ports.md#I-V%20Characteristic) $\mathcal{F}$ and a point $\begin{bmatrix}\boldsymbol{v}_0 \\ \boldsymbol{i}_0 \end{bmatrix} \in \mathcal{F}$.
>
>If $\mathcal{F}$ has an [admittance representation](./Ports.md) $\boldsymbol{i} = G(\boldsymbol{v})$, then the [I-V characteristic](./Ports.md#I-V%20Characteristic) $\mathcal{F}_{\text{affine}}$ of the $n$[-port](./Ports.md) which best approximates $\mathcal{F}$ around $(\boldsymbol{v}_0, \boldsymbol{i}_0)$ has an [admittance representation](./Ports.md) which can be obtained using $G$'s [Jacobian](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md#Differentiability):
>
>$$\boldsymbol{i}= J_G(\boldsymbol{v}_0) (\boldsymbol{v} - \boldsymbol{v}_0) + \boldsymbol{i}_0 $$
>
>If $\mathcal{F}$ has an [impedance representation](./Ports.md) $\boldsymbol{v} = R(\boldsymbol{i})$, then the [I-V characteristic](./Ports.md#I-V%20Characteristic) $\mathcal{F}_{\text{affine}}$ of the $n$[-port](./Ports.md) which best approximates $\mathcal{F}$ around $(\boldsymbol{v}_0, \boldsymbol{i}_0)$ has an [impedance representation](./Ports.md) which can be obtained using $R$'s [Jacobian](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md#Differentiability):
>
>$$\boldsymbol{v} = J_R(\boldsymbol{i}_0) (\boldsymbol{i} - \boldsymbol{i}_0) + \boldsymbol{v}_0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
