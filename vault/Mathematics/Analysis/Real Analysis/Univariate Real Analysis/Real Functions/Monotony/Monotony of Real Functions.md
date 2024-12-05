>[!THEOREM] Theorem: Bijectivity of Real Monotonous Functions
>
>Let $f: I \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Function.md).
>
>If $f$ is [continuous](../Continuity/Continuity%20of%20Real%20Functions.md) and [strictly monotonous](Monotony%20of%20Real-Valued%20Functions.md), then $f$ is a [bijective](../../../../Functions/Types%20of%20Functions/Bijection.md) between $I$ and its [image](../../../../Functions/Function.md) $f(I)$.
>
>>[!PROOF]-
>>
>>
>>
>

>[!THEOREM] Theorem: Inverses of Strictly Monotonous Real Functions
>
>Let $f: I \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Function.md).
>
>If $f$ is [continuous](../../../../../Topology/Continuity/Continuity.md) and [strictly increasing](Monotony%20of%20Real-Valued%20Functions.md) (strictly decreasing), then its [inverse](../../../../Functions/Types%20of%20Functions/Inverse%20Function.md) $f^{-1}: f(I) \to I$ is continuous and strictly increasing (strictly decreasing).
>
>>[!PROOF]-
>>
>>Suppose that $f$ is strictly increasing. To prove that $f^{-1}$ is strictly decreasing, observe two $x_1,x_2 \in I$ with $x_1 \lt x_2$. Since $f$ is strictly increasing, we have $f(x_1) \lt f(x_2)$. Let $y_1 = f(x_1)$ and $y_2 = f(x_2)$, i.e. $y_1 \lt y_2$. Therefore, $f^{-1}(y_1) = x_1$ and $f^{-1}(y_2) = x_2$ and so $f^{-1}(y_1) \lt f^{-1}(y_2)$ for $y_1 \lt y_2$ which means that $f^{-1}$ is strictly increasing. The proof is analogous for when $f$ is strictly decreasing.
>>
>>
>>
>