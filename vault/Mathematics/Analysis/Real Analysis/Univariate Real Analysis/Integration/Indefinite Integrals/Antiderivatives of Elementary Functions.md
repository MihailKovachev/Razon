>[!THEOREM] Theorem: Antiderivatives of Polynomial Functions
>
>$$
>\int x^\alpha \mathop{\mathrm{d}x} = \frac{1}{\alpha + 1} x^{\alpha + 1} + C \qquad \forall \alpha \ne -1 \in \mathbb{R}
>$$
>
>$$
>\int (ax + b)^\gamma \mathop{\mathrm{d}x} = \frac{(ax+b)^{\gamma+1}}{a(\gamma +1)} + C
>$$
>
>>[!PROOF]-
>>
>>TODO
>

>[!THEOREM] Theorem: Antiderivatives of Rational Functions
>
>$$\int \frac{c}{ax+b} \mathop{\mathrm{d}x} = \frac{c}{a} \ln |ax+b| + C$$
>
>For all $n \in \mathbb{N}$ and $a \in \mathbb{R}$:
>
>$$\int \frac{\mathop{\mathrm{d}x}}{(x-a)^n} = \begin{cases}\displaystyle \ln |x-a| + C, \text{ if } n = 1 \\\displaystyle -\frac{1}{(n-1)(x-a)^{n-1}} + C, \text{ if } n\ge 2 \end{cases}$$
>
>For all $a,b \in \mathbb{R}$ and all polynomials $x^2 + px + q$ with $p^2 -4q \lt 0$:
>
>$$\int\frac{\mathop{\mathrm{d}x}}{x^2+px+q} = \frac{2}{\sqrt{4q-p^2}}\arctan \frac{2x+p}{\sqrt{4q-p^2}} + C$$
> 
>$$\int\frac{ax+b}{x^2+px+q}\mathop{\mathrm{d}x} = \frac{a}{2}\ln (x^2+px+q)- \left(b-\frac{ap}{2}\right)\int\frac{\mathop{\mathrm{d}x}}{x^2+px+q}$$
>
>For all $n\ge 2 \in \mathbb{N}$ and all polynomials $x^2+px+q$ with $p^2-4q\lt 0$:
>
>$$\int\frac{\mathop{\mathrm{d}x}}{(x^2+px+q)^n} = \frac{2x+p}{(n-1)(4q-p^2)(x^2+px+q)^{n-1}}+\frac{2(2n-3)}{(n-1)(4q-p^2)}\int\frac{\mathop{\mathrm{d}x}}{(x^2+px+q)^{n-1}}$$
> 
>$$\int\frac{ax+b}{(x^2+px+q)^n}\mathop{\mathrm{d}x} = -\frac{a}{2(n-1)(x^2+px+q)^{n-1}}+\left(b-\frac{ap}{2}\right)\int\frac{\mathop{\mathrm{d}x}}{(x^2+px+q)^{n-1}}$$
>
>>[!PROOF]-
>>
>>TODO
>

>[!THEOREM] Theorem: Antiderivatives of Exponential Functions
>
>$$\int e^{\alpha x} \mathop{\mathrm{d}x} = \frac{1}{\alpha}e^{\alpha x} + C$$
>
>$$\int f'(x) e^{f(x)} \mathop{\mathrm{d}x} = e^{f(x)} + C$$
>
>$$\int a^x \mathop{\mathrm{d}x} = \frac{a^x}{\ln a} + C$$
>
>$$\int e^x (f(x) + f'(x)) \mathop{\mathrm{d}x} = e^x f(x) + C$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antiderivatives of Logarithmic Functions
>
>$$\int \ln x \mathop{\mathrm{d}x} = x (\ln x - 1) + C$$
>
>$$\int \log_a x \mathop{\mathrm{d}x} = \frac{x}{\ln a} (\ln x - 1) + C$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antiderivatives of Trigonometric Functions
>
>$$
>\int \sin x \mathop{\mathrm{d}x} = -\cos x + C
>$$
>
>$$
>\int \cos x \mathop{\mathrm{d}x} = \sin x + C
>$$
>
>$$
>\int \tan x \mathop{\mathrm{d}x} = - \ln |\cos x| + C
>$$
>
>$$
>\int \cot x \mathop{\mathrm{d}x} = \ln |\sin x| + C
>$$
>
>$$
>\int \arctan x \mathop{\mathrm{d}x} = x \arctan x - \frac{1}{2}\ln (x^2 + 1) + C
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>