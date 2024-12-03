>[!DEFINITION] Definition: Homogeneous Trigonometric Equation
>
>A **homogeneous trigonometric equation** is a [trigonometric equation](Real%20Trigonometric%20Equation.md) of the form
>
>$$
>a_0 \sin^n x + a_1 \sin^{n-1} x \cos x + \cdots + a_{n-1}\sin x \cos^{n-1} x + a_n \cos^n x = 0,
>$$
>
>where $a_k \in \mathbb{R}$.
>

>[!ALGORITHM]- Algorithm: Solving Homogeneous Trigonometric Equations (Tangent Substitution)
>
>We are given the following [homogeneous trigonometric equations](Homogeneous%20Trigonometric%20Equations.md).
>
>$$
>a_0 \sin^n x + a_1 \sin^{n-1} x \cos x + \cdots + a_{n-1}\sin x \cos^{n-1} x + a_n \cos^n x = 0
>$$
>
>1. Check whether $\cos^n (x) = 0$, i.e. $x = \pm\frac{\pi}{2} + 2k\pi$ for $k \in \mathbb{Z}$, is a solution.
>2. Divide by $\cos^n (x)$.
>
>$$
>a_0 \frac{\sin^n x}{\cos^n x} + a_1 \frac{\sin^{n-1} x}{\cos^{n-1} x} + \cdots + a_{n-1} \frac{\sin x}{\cos x} + a_n = 0
>$$
>
>$$
>a_0 \tan^n x + a_1 \tan^{n-1} x + \cdots + a_{n-1} \tan x + a_n = 0
>$$
>
>3. Substitute $t = \tan x$ and solve the [polynomial equation](../Polynomial%20Equations/Polynomial%20Equation.md)
> 
>$$
>a_0 t^n + a_1 t^{n-1} + \cdots + a_{n-1} t + a_n = 0
>$$
>
>4. For each solution $t^\ast$ to the equation in Step 3, solve the [elementary trigonometric equation](Elementary%20Trigonometric%20Equations.md) $\tan x = t^\ast$.
>
>>[!EXAMPLE]-
>>
>>TODO
>>
>

>[!ALGORITHM]- Algorithm: Solving Homogeneous Trigonometric Equations (Cotangent Substitution)
>
>We are given the following [homogeneous trigonometric equation](Homogeneous%20Trigonometric%20Equations.md).
>
>$$
>a_0 \sin^n x + a_1 \sin^{n-1} x \cos x + \cdots + a_{n-1}\sin x \cos^{n-1} x + a_n \cos^n x = 0
>$$
>
>1. Check whether $\sin^n (x) = 0$, i.e. $x = k\pi$ for $k \in \mathbb{Z}$, is a solution.
>2. Divide by $\sin^n (x)$.
>
>$$
>a_0 + a_1 \frac{\cos x}{\sin x} + \cdots + a_{n-1} \frac{\cos^{n-1} x}{\sin^{n-1} x} + a_n \frac{\cos^n x}{\sin^n x} = 0
>$$
>
>$$
>a_0 + a_1 \cot x + \cdots + a_{n-1} \cot^{n-1} x + a_n\cot^n x = 0
>$$
>
>3. Substitute $t = \cot x$ and solve the [polynomial equation](../Polynomial%20Equations/Polynomial%20Equation.md)
> 
>$$
>a_0 + a_1 t + \cdots + a_{n-1} t^{n-1} + a_n t^n = 0
>$$
>
>4. For each solution $t^\ast$ to the equation in Step 3, solve the [elementary trigonometric equation](Elementary%20Trigonometric%20Equations.md) $\cot x = t^\ast$.
>
>>[!EXAMPLE]-
>>
>>TODO
>>
>
