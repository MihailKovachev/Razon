>[!ALGORITHM] Algorithm: Matrix Inversion
>
>To find the [inverse](Invertibility.md) of an [invertible](Invertibility.md) [matrix](../Square%20Matrix.md) $A \in F^{n \times n}$:
>1. Notate an $n\times 2n$-[matrix](../../Matrix.md) $(A\mid I_n)$ by sticking the [identity matrix](../Identity%20Matrix.md) $I_n$ to the right of $A$.
>2. Perform [Gauss-Jordan elimination](../../../Systems%20of%20Linear%20Equations/Gauss-Jordan%20Elimination.md) on $(A \mid I_n)$. If $A$ is indeed [invertible](Invertibility.md), the final result will be $(I_n \mid A^{-1})$.
>
>>[!EXAMPLE]-
>>
>>Let's find the inverse of $A = \begin{bmatrix}6 & 8 & 3 \\ 4 & 7 & 3 \\ 1 & 2 & 1\end{bmatrix}$. Notate
>>
>>$$
>>[A\mid I_3] = \left[\begin{array}{ccc|ccc}6 & 8 & 3 & 1 & 0 & 0\\ 4 & 7 & 3 & 0 & 1 & 0 \\ 1 & 2 & 1 & 0 & 0 & 1\end{array}\right]
>>$$
>>
>>Perform [Gauss-Jordan elimination](../../../Systems%20of%20Linear%20Equations/Gauss-Jordan%20Elimination.md)
>>
>>$$
>>\left[\begin{array}{ccc|ccc}6 & 8 & 3 & 1 & 0 & 0\\ 4 & 7 & 3 & 0 & 1 & 0 \\ 1 & 2 & 1 & 0 & 0 & 1\end{array}\right] \approx \left[\begin{array}{ccc|ccc}1 & 2 & 1 & 0 & 0 & 1 \\ 6 & 8 & 3 & 1 & 0 & 0\\ 4 & 7 & 3 & 0 & 1 & 0 \end{array}\right] \approx \left[\begin{array}{ccc|ccc}1 & 2 & 1 & 0 & 0 & 1 \\ 0 & -4 & -3 & 1 & 0 & -6\\ 0 & -1 & -1 & 0 & 1 & -4 \end{array}\right]
>>$$
>>
>>$$
>>\left[\begin{array}{ccc|ccc}1 & 2 & 1 & 0 & 0 & 1 \\ 0 & -4 & -3 & 1 & 0 & -6\\ 0 & -1 & -1 & 0 & 1 & -4 \end{array}\right] \approx \left[\begin{array}{ccc|ccc}1 & 0 & -1 & 0 & 2 & -7 \\ 0 & 1 & 1 & 0 & -1 & 4\\ 0 & 0 & 1 & 1 & -4 & 10 \end{array}\right] \approx \left[\begin{array}{ccc|ccc}1 & 0 & 0 & 1 & -2 & 3 \\ 0 & 1 & 0 & -1 & 3 & -6\\ 0 & 0 & 1 & 1 & -4 & 10 \end{array}\right]
>>$$
>>
>>$$
>>A^{-1} = \begin{bmatrix}1 & -2 & 3 \\ -1 & 3 & -6 \\ 1 & -4 & 10\end{bmatrix}
>>$$
>>
>

>[!THEOREM] Theorem: Inverting $2\times2$-Matrices
>
>A $2\times 2$-[matrix](../Square%20Matrix.md) $A = \begin{bmatrix}a & b \\ c & d\end{bmatrix}$ is [invertible](Invertibility.md) if and only if
>
>$$
>ad - bc \ne 0
>$$
>
>If $A$ is [invertible](Invertibility.md), then
>
>$$
>A^{-1} = \frac{1}{ad-bc}\begin{bmatrix}d & -b \\ -c & a\end{bmatrix}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>