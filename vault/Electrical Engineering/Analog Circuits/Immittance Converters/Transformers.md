---
tags:
  - analog-circuits
  - electrical-engineering
---

# Transformers

**Transformers** or **positive immittance converters** (**PICs**) are [immittance converters](./Immittance%20Converters.md) which allow us to transform the behavior of an [electronic component](../../Electronic%20Circuits.md), whilst retaining both its [voltage polarity](TODO) and its [current polarity](../../Current.md).

## Theoretical Model

>[!DEFINITION] Definition: Transformer
>
>A **transformer** is a [time-invariant](../../Network%20Analysis/Lumped%20Elements.md) [two-port](../../Network%20Analysis/Two-Ports/Two-Ports.md) for which there exists some $n \in \mathbb{R}$ with the following property:
>
>$$\left\vert\begin{aligned}v_1 &= n v_2 \\i_1 &= -\frac{1}{n} i_2\end{aligned}\right.$$
>
>We call $n$ the **turn ratio** and usually write it as $n = \frac{N_1}{N_2}$ for some [integers](TODO) $N_1, N_2$.
>
>>[!NOTATION]
>>
>>The following symbols are used for [transformers](#Theoretic%20Model):
>>
>>![Transformer Symbol](./res/Transformer%20Symbol.svg)
>>
>

>[!THEOREM] Theorem: Strict Linearity
>
>Every [transformer](#Theoretic%20Model) is [strictly linear](../../Network%20Analysis/Two-Ports/Linear%20Two-Ports.md#Strictly%20Linear%20Two-Ports).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Implicit Representation
>
>If a [transformer](#Theoretic%20Model) has [turning ratio](#Theoretic%20Model) $n$, then it has the following [implicit representation](../../Network%20Analysis/Ports.md#Representations):
>
>$$\begin{bmatrix}1 & -n \\ 0 & 0\end{bmatrix}\boldsymbol{v} + \begin{bmatrix}0 & 0 \\ n & 1\end{bmatrix}\boldsymbol{i} = \boldsymbol{0}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Explicit Representations
>
>If a [transformer](#Theoretic%20Model) has an [admittance representation](../../Network%20Analysis/Two-Ports/Two-Ports.md#Representations)
>
>$$\boldsymbol{i} = \boldsymbol{G}\boldsymbol{v},$$
>
>then $\boldsymbol{G}$ is zero.
>
>If a [transformer](#Theoretic%20Model) has an [admittance representation](../../Network%20Analysis/Two-Ports/Two-Ports.md#Representations)
>
>$$\boldsymbol{v} = \boldsymbol{R}\boldsymbol{i},$$
>
>then $\boldsymbol{R}$ is zero.
>
>Every [transformer](#Theoretic%20Model) has a [hybrid representation](../../Network%20Analysis/Two-Ports/Two-Ports.md#Representations):
>
>$$\begin{bmatrix}v_1 \\ i_2\end{bmatrix} = \boldsymbol{H} \begin{bmatrix}i_1 \\ v_2\end{bmatrix} \qquad \boldsymbol{H} = \begin{bmatrix}0 & n \\ -n & 0\end{bmatrix}$$
>
>Every [transformer](#Theoretic%20Model) has an [inverse hybrid representation](../../Network%20Analysis/Two-Ports/Two-Ports.md#Representations):
>
>$$\begin{bmatrix}i_1 \\ v_2\end{bmatrix} = \boldsymbol{H}' \begin{bmatrix}v_1 \\ i_2\end{bmatrix} \qquad \boldsymbol{H}' = \begin{bmatrix}0 & -\frac{1}{n} \\ \frac{1}{n} & 0\end{bmatrix}$$
>
>Every [transformer](#Theoretic%20Model) has a [forwards transmission representation](../../Network%20Analysis/Two-Ports/Two-Ports.md#Representations):
>
>$$\begin{bmatrix}v_1 \\ i_1\end{bmatrix} = \boldsymbol{T} \begin{bmatrix}v_2 \\ -i_2\end{bmatrix} \qquad \boldsymbol{T} = \begin{bmatrix}n & 0 \\ 0 & \frac{1}{n}\end{bmatrix}$$
>
>Every [transformer](#Theoretic%20Model) has a [backwards transmission representation](../../Network%20Analysis/Two-Ports/Two-Ports.md#Representations):
>
>$$\begin{bmatrix} v_2 \\ i_2 \end{bmatrix} = \boldsymbol{T}'\left(\begin{bmatrix}v_1 \\ -i_1\end{bmatrix}\right) \qquad \boldsymbol{T}' = \begin{bmatrix}\frac{1}{n} & 0 \\ 0 & n\end{bmatrix}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Losslessness of the Transformer
>
>Every [transformer](#Theoretic%20Model) is [lossless](../../Network%20Analysis/Ports.md#Power).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Reciprocity of the Ideal Transformer
>
>Every [transformer](#Theoretic%20Model) is [reciprocal](../../Network%20Analysis/Strictly%20Linear%20Multiports.md#Reciprocity).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Symmetry Condition for the Transformer
>
>A [transformer](#Theoretic%20Model) is [symmetrical](../../Network%20Analysis/Two-Ports/Two-Ports.md#Symmetry) if and only if its [turn ratio](#Theoretic%20Model) $n$ is $1$ or $-1$:
>
>$$n = \pm 1$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Transformer as a Port Enforcer
>
>Chaining a 4[-terminal network](../../Network%20Analysis/Lumped%20Elements.md) $E$ with two $1:1$ [transformers](./Transformers.md) results in a [two-port](../../Network%20Analysis/Two-Ports/Two-Ports.md):
>
>![Transformer as Port-Enforcer](./res/Transformer%20as%20Port-Enforcer.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

### Multiport Transformer

