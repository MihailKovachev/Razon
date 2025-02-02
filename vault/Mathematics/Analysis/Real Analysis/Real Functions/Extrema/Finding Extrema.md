>[!ALGORITHM] Algorithm: Finding the Extrema of a Function
>
>Requirements: $f: D \subseteq \mathbb{R} \to \mathbb{R}$ is [continuous](../Continuity/Continuity%20of%20Real%20Functions.md).
>
>1. Determine the [critical points](../Differentiation/Critical%20Point.md) $x_1, x_2, \cdots, x_n \in D$ of $f$ by solving $f'(x) = 0$ and also seeing where $f$ is not [differentiable](../Differentiation/Differentiability%20of%20Real%20Functions.md).
>2. Use the above criteria to check at which [critical points](../Differentiation/Critical%20Point.md) $f$ has [local extrema](Local%20Extrema.md).
>3. Evaluate $f$ at the places of its [local extrema](Local%20Extrema.md) to obtain the values of the [local minima](Local%20Extrema.md) and [local maxima](Local%20Extrema.md).
>4. Evaluate $f$ at the following locations:
>	- If $D = [a;b]$ where $a,b \in \mathbb{R}$, evaluate $f(a)$ and $f(b)$;
>	-  If $D = [a;b)$ where $a \in \mathbb{R}$ and $b \in \mathbb{R} \cup \{\infty\}$, evaluate $f(a)$ and $\lim_{x\to b} f(x)$;
>	- If $D = (a;b]$ where $a \in \mathbb{R} \cup \{-\infty \}$ and $b \in \mathbb{R}$, evaluate $\lim_{x\to a} f(x)$ and $f(b)$;
>	- If $D = (a;b)$ where $a \in \mathbb{R} \cup \{-\infty \}$ and $b \in \mathbb{R} \cup \{\infty\}$, evaluate $\lim_{x\to a} f(x)$ and $\lim_{x\to b} f(x)$;
>	- If $D = D_1 \cup \cdots \cup D_n$ is a [union](../../../../../Set%20Theory/Operations%20with%20Sets/Union.md) of [disjoint](../../../../../Set%20Theory/Disjoint%20Sets.md) intervals $D_1, \cdots, D_n$, then perform Step 4 separately for each interval.
>5. Compare the [local extrema](Local%20Extrema.md) of $f$ with the values from Step 4:
>	- If there is a greatest value, then it is the [global maximum](Global%20Extrema.md) of $f$;
>	- If there is a smallest value, then it is the [global minimum](Global%20Extrema.md) of $f$;