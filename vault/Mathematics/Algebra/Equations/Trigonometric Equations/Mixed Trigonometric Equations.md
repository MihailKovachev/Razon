>[!ALGORITHM]- Algorithm: Solving Trigonometric Equations of the Form $a \sin x + b \cos x = c$
>
>We are given a [trigonometric equation](Real%20Trigonometric%20Equation.md) of the following form.
>
>$$
>a \sin x + b \cos x = c
>$$
>
>1. Divide both sides by $\sqrt{a^2 + b^2}$.
>
>$$
>\frac{a}{\sqrt{a^2 + b^2}}\sin x + \frac{b}{\sqrt{a^2 + b^2}}\cos x = \frac{c}{\sqrt{a^2+b^2}}
>$$
>
>2. Substitute $\cos \varphi = \frac{a}{\sqrt{a^2 + b^2}}$ and $\sin \varphi = \frac{b}{\sqrt{a^2 + b^2}}$
>
>$$
>\cos \varphi \sin x + \sin \varphi \cos x = \frac{c}{\sqrt{a^2+b^2}}
>$$
>
>- The reason we can do this is that $\left(\frac{a}{\sqrt{a^2 + b^2}}\right)^2 +\left(\frac{b}{\sqrt{a^2 + b^2}}\right)^2 = 1$.
>
>3. Use an identity to simplify the left-hand side.
>
>$$
>\sin (x + \varphi) = \frac{c}{\sqrt{a^2+b^2}}
>$$
>
>- Requirements: $\frac{c}{\sqrt{a^2+b^2}} \in [-1;1]$
>
>4. Solve the [elementary trigonometric equation](Elementary%20Trigonometric%20Equations.md).
>
>$$
>\begin{align*}x + \varphi &= \arcsin\frac{c}{\sqrt{a^2+b^2}} + 2k\pi \\ x + \varphi &= -\arcsin\frac{c}{\sqrt{a^2+b^2}} + (2k+1)\pi \end{align*}
>$$
>
>5. Rearrange to isolate $x$.
>
>$$
>\begin{align*}x &= \arcsin\frac{c}{\sqrt{a^2+b^2}} -\varphi + 2k\pi \\ x &= -\arcsin\frac{c}{\sqrt{a^2+b^2}} -\varphi + (2k+1)\pi \end{align*}
>$$
>
>6.Substitute back for $\varphi$ to obtain the final set of solutions.
>
>- If you substitute back $\varphi = \arccos \frac{a}{\sqrt{a^2 + b^2}}$, you obtain
>
>$$
>\begin{align*}x &= \arcsin\frac{c}{\sqrt{a^2+b^2}} - \arccos \frac{a}{\sqrt{a^2 + b^2}} + 2k\pi \\ x &= -\arcsin\frac{c}{\sqrt{a^2+b^2}} - \arccos \frac{a}{\sqrt{a^2 + b^2}} + (2k+1)\pi \end{align*}
>$$
>
>- If you susbtitute back $\varphi = \arcsin \frac{b}{\sqrt{a^2 + b^2}}$, you obtain
>
>$$
>\begin{align*}x &= \arcsin\frac{c}{\sqrt{a^2+b^2}} - \arcsin \frac{b}{\sqrt{a^2 + b^2}} + 2k\pi \\ x &= -\arcsin\frac{c}{\sqrt{a^2+b^2}} - \arcsin \frac{b}{\sqrt{a^2 + b^2}} + (2k+1)\pi \end{align*}
>$$
>
>>[!EXAMPLE]-
>>
>>TODO
>>
>