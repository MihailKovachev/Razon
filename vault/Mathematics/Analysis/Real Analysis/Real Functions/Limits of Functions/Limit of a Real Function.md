>[!DEFINITION] Definition: Limit of a Function (Cauchy)
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Function.md).
>
>A real number $L \in \mathbb{R}$ is called the **limit of** $f$ **as** $x$ **approaches** $c \in \mathbb{R}$ if for every $\varepsilon \gt 0$ there is a $\delta \gt 0$ such that for all $x \in D$ with $x \ne c$
>
>$$
>|x-c| \lt \delta \implies |f(x)-L| \lt \varepsilon
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\lim_{x\to c} f(x) = L
>>$$
>
>>[!THEOREM] Theorem: Existence of the Limit
>>
>>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Function.md).
>>
>>The [limit](Limit%20of%20a%20Real%20Function.md) of $f$ as $x$ approaches $c \in D$ exists if and only if both [one-sided limits](One-Sided%20Limits.md) of $f$ at $c$ exist and are equal.
>>
>>$$\lim_{x \to c} f(x) = L \in \mathbb{R} \iff \lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = L$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>
>>[!DEFINITION] Definition: Limit at Positive Infinity
>>
>>A real number $L \in \mathbb{R}$ is called the **limit of** $f$ **as** $x$ **approaches positive infinity** if for every $\varepsilon \gt 0$ there is a $A \in \mathbb{R}$ such that
>>
>>$$
>>|f(x) - L| \lt \varepsilon \qquad \forall x \ge A
>>$$
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>\lim_{x\to \infty} f(x) = L
>>>$$
>>>
>>
>
>>[!DEFINITION] Definition: Limit at Negative Infinity
>>
>>A real number $L \in \mathbb{R}$ is called the **limit of** $f$ **as** $x$ **approaches negative infinity** if for every $\varepsilon \gt 0$ there is a $A \in \mathbb{R}$ such that
>>
>>$$
>>|f(x) - L| \lt \varepsilon \qquad \forall x \le A
>>$$
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>\lim_{x\to -\infty} f(x) = L
>>>$$
>>>
>>
>
>If $f$ has a limit $L \in \mathbb{R}$, then the limit is said to exist.
>