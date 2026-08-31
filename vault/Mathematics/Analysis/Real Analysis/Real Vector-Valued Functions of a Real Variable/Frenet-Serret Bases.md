---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Frenet-Serret Bases

>[!DEFINITION] Definition: Tangent Vector (Velocity)
>
>Let $\gamma: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [vector-valued function](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md).
>
>The **tangent vector** or **velocity** of $\gamma$ is its [derivative](./Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) (provided that it exists):
>
>$$\dot{\gamma}$$
>
>>[!DEFINITION] Definition: Speed
>>
>>The [Euclidean norm](../Euclidean%20Space/Euclidean%20Space.md) of $\gamma$'s [velocity](#Frenet-Serret%20Bases) is known as $\gamma$'s **speed**.
>>
>
>>[!DEFINITION] Definition: Unit Tangent Vector
>>
>>The [normalization](../../../Algebra/Vector%20Spaces/Norms.md) of $\gamma$'s [tangent vector](#Frenet-Serret%20Bases) is known as $\gamma$'s **unit tangent vector**:
>>
>>$$\frac{1}{||\dot{\gamma}||}\dot{\gamma}$$
>>
>>>[!NOTATION]
>>>
>>>$$\mathbf{T}$$
>>>
>>
>

>[!DEFINITION] Definition: Normal Vector
>
>Let $\gamma: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [vector-valued function](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md).
>
>The **normal vector** of $\gamma$ is the [derivative](./Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) of its [tangent vector](#Frenet-Serret%20Bases) (provided that it exists):
>
>$$\ddot{\gamma}$$
>
>>[!DEFINITION] Definition: Unit Normal Vector
>>
>>The [normalization](../../../Algebra/Vector%20Spaces/Norms.md) of $\gamma$'s [normal vector](#Frenet-Serret%20Bases) is known as $\gamma$'s **unit normal vector**:
>>
>>$$\frac{1}{||\ddot{\gamma}||} \ddot{\gamma}$$
>>
>>>[!NOTATION]
>>>
>>>$$\mathbf{N}$$
>>>
>>
>

>[!DEFINITION] Definition: Binormal Vector
>
>Let $\gamma: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}^3$ be a [vector-valued function](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md).
>
>The **binormal vector** of $\gamma$ is the [cross product](../../../Algebra/Linear%20Algebra/Real%20Vectors/Cross%20Product.md) of its [unit tangent vector](#Frenet-Serret%20Bases) and its [unit normal vector](#Frenet-Serret%20Bases) (provided that these exist):
>
>$$\mathbf{T} \times \mathbf{N}$$
>
>>[!NOTATION] Notation
>>
>>$$\mathbf{B}$$
>>
>