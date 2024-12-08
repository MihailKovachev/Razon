>[!DEFINITION] Definition: Vertical Asymptote
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Function.md).
>
>The line $x = c \in \mathbb{R}$ is a **vertical asymptote** of $f$ if $f$ has at least one [infinite one-sided limit](Infinite%20One-Sided%20Limits.md) at $c$, i.e. at least one of the following holds:
>
>- $\displaystyle \lim_{x \to c^-} f(x) = -\infty$
>- $\displaystyle \lim_{x \to c^+} f(x) = -\infty$
>- $\displaystyle \lim_{x \to c^-} f(x) = \infty$ 
>- $\displaystyle \lim_{x \to c^+} f(x) = \infty$
>
>>[!INTUITION]-
>>
>>Intuitively, this definition means that the value of $f(x)$ gets closer and closer to $\pm \infty$ as $x$ approaches $c$ either from the left or from the right.
>>
>

>[!DEFINITION] Definition: Horizontal Asymptote
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Function.md).
>
>The line $y = a \in \mathbb{R}$ is a **horizontal asymptote** of $f$ if the [limit](Limit%20of%20a%20Function.md) of $f$ as $x$ approaches positive or negative infinity is $a$, i.e. if at least one of the following holds:
>
>- $\displaystyle \lim_{x \to -\infty} f(x) = a$
>- $\displaystyle \lim_{x \to \infty} f(x) = a$
>
>>[!INTUITION]-
>>
>>Intuitively, this definition means that the value of $f(x)$ gets closer and closer to $a$ as $x$ approaches either positive or negative infinity.
>>
>

>[!DEFINITION] Definition: Oblique Asymptote
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Function.md).
>
>The line $y = ax + b$ is an **oblique** or **slanted asymptote** of $f$ if at least one of the following is true:
>- $\displaystyle \lim_{x \to -\infty} [f(x) - (ax + b)] = 0$
>- $\displaystyle \lim_{x \to \infty} [f(x) - (ax + b)] = 0$
>
>>[!INTUITION]-
>>
>>Intuitively, this definition means $f(x)$ gets closer and closer to the line $y = ax + b$ as $x$ approaches either positive or negative infinity.
>>
>