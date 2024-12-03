>[!THEOREM] The Intermediate Value Theorem
>Let $f: D \subset \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Function.md) on a closed interval $D = [a;b]$.
>
>If $f$ is [continuous](Continuity.md) on $D$, then for every $y$ between $f(a)$ and $f(b)$, i.e. $\min\{f(a), f(b)\} \le y \le \max\{f(a), f(b)\}$, there exists an $x \in D$ such that $f(x) = y$.
>
>>[!NOTE]
>>The theorem says that if a function is continuous on a closed interval, then it must generate all values between the values on the interval's endpoints.
>
>>[!PROOF]-
>>TODO

>[!THEOREM] Bolzano's Theorem
>Let $f: D \subset \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Function.md) on a closed interval $D = [a;b]$.
>
>If $f$ is [continuous](Continuity.md) on $D$ and $f(a) \lt 0$ and $f(b) \gt 0$ (or vice-versa), then there exists at least one $x \in D$ such that $f(x) = 0$.
>
>>[!PROOF]-
>>This is just a special case of the intermediate value theorem.