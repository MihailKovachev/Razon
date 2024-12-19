>[!THEOREM] Theorem: Cartesian Coordinate System
>
>The [identity function](../../../../Analysis/Functions/Identity%20Function.md) $x: \mathbb{R}^n \to \mathbb{R}^n$ on the [Euclidean space](../Euclidean%20Space.md) $\mathbb{R}^n$ is a [global coordinate system](../../../Manifolds/Coordinates/Global%20Coordinate%20System.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Cartesian Coordinate System
>>
>>We call $x$ the **Cartesian coordinate system** on $\mathbb{R}^n$ and its [component functions](../../../../Analysis/Real%20Analysis/Multivariate%20Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Function.md) $x^1,\dotsc, x^n: \mathbb{R}^n \to \mathbb{R}$ are known as the Cartesian coordinates *on* $\mathbb{R}^n$. 
>>
>>Given some $p = \begin{bmatrix} p_1 & \cdots & p_n \end{bmatrix}^{\mathsf{T}} \in \mathbb{R}^n$, we call 
>>
>>$$
>>p^1 = x^1(p) = p_1 \qquad \cdots \qquad p^n = x^n(p) = p_n
>>$$
>>
>>the Cartesian coordinates *of* $p$.
>>
>>>[!NOTATION]- 
>>>
>>>Coordinates are typically denoted using superscripts - $x^1, \dotsc, x^n$ and $p^1, \dotsc, p^n$. However, since the Cartesian coordinates of $p$ coincide with its components by definition, we often ignore the distinction between them and use subscripts for both. This means that Cartesian coordinates *on* $\mathbb{R}^n$ are often denoted as $x_1, \dotsc, x_n$ instead of $x^1, \dotsc, x^n$ and the Cartesian coordinates of $p$ are often denoted as $p_1, \dotsc, p_n$ instead of $p^1, \dotsc, p^n$. 
>>>
>>
>>>[!NOTATION]- Notation: Cartesian Coordinates in 2D, 3D, and 4D
>>>
>>>The Cartesian coordinates $x^1$ and $x^2$ on $\mathbb{R}^2$ are often denoted as $x$ and $y$.
>>>
>>>The Cartesian coordinates $x^1, x^2$ and $x^3$ on $\mathbb{R}^3$ are often denoted as $x, y$ and $z$.
>>>
>>>The Cartesian coordinates $x^1, x^2, x^3$ and $x^4$ on $\mathbb{R}^4$ are often denoted as $x, y, z$ and $w$.
>>>
>>
>>>[!INTUITION]-
>>>
>>>The components $p_1, \dotsc, p_n$ of $p = \begin{bmatrix}p_1 & \dotso & p_n\end{bmatrix}^\mathsf{T} \in \mathbb{R}^n$ are also natural [coordinates](../../../Manifolds/Coordinates/Coordinate%20System.md) for it. We use $x^i$ to denote the function which returns the $i$-th component of $p$, i.e.
>>>
>>>$$
>>>x^i(p) \overset{\text{def}}{=} p_i
>>>$$
>>>
>>>Cartesian coordinates of $p$ are equal to its components by definition, but when we want to emphasise their coordinate nature instead of their component nature, we denote them as $p^1, \dotsc, p^n$ instead of $p_1, \dotsc, p_n$.
>>>
>>
>
