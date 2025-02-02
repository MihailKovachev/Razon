>[!THEOREM] Theorem: Differentiability of Parametric Curves
>
>Let $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [parametric curve](../Parametric%20Curve.md) and let $t$ be an [accumulation point](../../../../../Topology/Interior,%20Exterior,%20Boundary/Accumulation%20Point.md) of $I$.
>
>Then $\gamma$ is [differentiable](../../../Real%20Vector%20Functions/Differentiation/Differentiability%20of%20Real%20Vector%20Functions.md) at $t_0 \in I$ if and only if the following [limit](../Limits%20of%20Parametric%20Curves.md) exists
>
>$$
>\lim_{t \to t_0} \frac{\gamma(t) - \gamma(t_0)}{t - t_0}
>$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>
>>- (I) If $\displaystyle \lim_{t \to t_0} \frac{\gamma(t) - \gamma(t_0)}{t - t_0}$ exists, then there is a [linear transformation](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Linear%20Transformation.md) $T: I \to \mathbb{R}^n$ such that 
>>
>>$$
>>\lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - T(t - t_0)||}{|t- t_0|} = 0
>>$$
>>
>>- (II) If there is a [linear transformation](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Linear%20Transformation.md) $T: I \to \mathbb{R}^n$ such that $\displaystyle \lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - T(t - t_0)||}{||t- t_0||} = 0$, then $\displaystyle \lim_{t \to t_0} \frac{\gamma(t) - \gamma(t_0)}{t - t_0}$ exists.
>>
>>**Proof of (I):**
>>
>>Let $\mathbf{L} = \lim_{t \to t_0} \frac{\gamma(t) - \gamma(t_0)}{t - t_0}$. Define $T: I \to \mathbb{R}^n$ as
>>
>>$$
>>T(x) = x\mathbf{L}
>>$$
>>
>>We can easily check that $T$ is a [linear transformation](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Linear%20Transformation.md):
>>
>>$$
>>T(\alpha x + \beta y) = (\alpha x + \beta y)\mathbf{L} = \alpha x \mathbf{L} + \beta y \mathbf{L} = \alpha T(x) + \beta T(y)
>>$$
>>
>>Then
>>
>>$$
>>\begin{align*}
>>
>>\lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - T(t - t_0)||}{||t- t_0||} &= \lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - (t - t_0)\mathbf{L}||}{|t- t_0|} \\
>>
>>&= \lim_{t \to t_0} \frac{ |t-t_0| \cdot \left|\left|\frac{\gamma(t) - \gamma(t_0)}{t-t_0} - \mathbf{L}\right|\right|}{|t- t_0|} \\
>>
>>&= \lim_{t \to t_0} \left|\left|\frac{\gamma(t) - \gamma(t_0)}{t-t_0} - \mathbf{L}\right|\right| \\
>>
>>&= \left|\left| \lim_{t \to t_0} \left( \frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \mathbf{L}\right) \right|\right| \\
>>
>>&= \left|\left|\lim_{t \to t_0} \left( \frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \frac{\gamma(t) - \gamma(t_0)}{t-t_0}\right)\right|\right| \\
>>
>>&= ||\mathbf{0}|| = 0
>>
>>\end{align*}
>>$$
>>
>>
>>**Proof of (II):**
>>
>>Let $\mathbf{T}$ be the [matrix representation](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Matrix%20Representations%20of%20Linear%20Transformations.md) of $T$ with respect to the [standard bases](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Standard%20Basis%20of%20the%20Real%20Vector%20Space.md) of $\mathbb{R}$ and $\mathbb{R}^n$. Then,
>>
>>$$
>>\lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - \mathbf{T}\begin{bmatrix}t-t_0\end{bmatrix}||}{|t- t_0|} = \lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - (t-t_0)\mathbf{T}||}{|t- t_0|} = 0
>>$$
>>
>>Factor out $t-t_0$ from the numerator and move it outside the magnitude.
>>
>>$$
>>\begin{align*}
>>
>>\lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - (t-t_0)\mathbf{T}||}{|t- t_0|} &= \lim_{t - t_0} \frac{|t-t_0|\cdot \left|\left| \frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \mathbf{T} \right|\right|}{|t-t_0|} \\ 
>>
>>&= \lim_{t \to t_0} \left|\left| \frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \mathbf{T} \right|\right| \\ 
>>
>>&= \left|\left| \lim_{t \to t_0} \left( \frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \mathbf{T} \right) \right|\right| = 0
>>
>>\end{align*}
>>$$
>>
>>Therefore,
>>
>>$$
>>\begin{align*}
>>
>>&\lim_{t \to t_0} \left(\frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \mathbf{T}\right) = \mathbf{0} \\
>>
>>&\lim_{t \to t_0} \left(\frac{\gamma(t) - \gamma(t_0)}{t - t_0}\right) - \mathbf{T} = \mathbf{0} \\
>>
>>&\lim_{t \to t_0} \frac{\gamma(t) - \gamma(t_0)}{t - t_0} = \mathbf{T}
>>
>>\end{align*}
>>$$
>>
>
>>[!DEFINITION] Definition: Derivative of a Parametric Curve
>>
>>The **derivative** of $\gamma$ at $t_0$ is the [limit](../Limits%20of%20Parametric%20Curves.md)
>>
>>$$
>>\lim_{t \to t_0} \frac{\gamma(t) - \gamma(t_0)}{t - t_0},
>>$$
>>
>>provided that it exists.
>>
>>If there is no specific $t_0 \in I$ mentioned, then "derivative" refers to the [function](../Parametric%20Curve.md) which to each $t^\ast$ assigns the aforementioned limit (if said limit exists).
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\frac{\mathrm{d}\gamma}{\mathrm{d}t}(t_0) \qquad \left.\frac{\mathrm{d}\gamma}{\mathrm{d}t}\right|_{t_0} \qquad \frac{\mathrm{d}}{\mathrm{d}t}\gamma (t_0) \qquad \gamma'(t_0) \qquad \dot{\gamma}(t_0)
>>>$$
>>>
>>
>>>[!NOTE]- Note: Derivative Terminology
>>>
>>>Referring to this limit as the "derivative" is technically a misnomer, since the [derivative of a vector function](../../../Real%20Vector%20Functions/Differentiation/Differentiability%20of%20Real%20Vector%20Functions.md) is a [linear transformation](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Linear%20Transformation.md) and the aforementioned limit is only a [matrix representation](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Matrix%20Representations%20of%20Linear%20Transformations.md) of said transformation. However, in the case of parametric curves, using the matrix representation of the derivative is very common. This is why, in this context, the term "derivative" is usually used for the matrix representation of the transformation instead of the transformation itself.
>>>
>>
>

>[!TIP] Tip: (Continuous) Differentiability of Curve Parameterisations
>
>A [curve parameterisation](../Parametric%20Curve.md) $\gamma$ is $k$**-times (continuously) differentiable** if its $k$-th order [derivative](Differentiability%20of%20Parametric%20Curves.md) exists (and is [continuous](../../../Real%20Vector%20Functions/Continuity%20of%20Real%20Vector%20Functions.md)).
>
>^continuous-differentiability
>

>[!TIP] Tip: Piecewise (Continuous) Differentiability of Curve Parameterisations
>
>A [curve parameterisation](../Parametric%20Curve.md) $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ is $k$**-times piecewise (continuously) differentiable** if $I$ can be expressed as a [disjoint](../../../../../Set%20Theory/Disjoint%20Sets.md) [union](../../../../../Set%20Theory/Operations%20with%20Sets/Union.md) $I = I_1 \cup \cdots \cup I_n$ such that the [restrictions](../../../../Functions/Restriction.md) $\gamma \big|_{I_1}, \cdots, \gamma \big|_{I_n}$ are $k$-times [continuously differentiable](Differentiability%20of%20Parametric%20Curves.md).
>
>^piecewise-continuous-differentiablity
>

>[!TIP] Tip: Smoothness of Curve Parameterisations
>
>A [curve parameterisation](../Parametric%20Curve.md) is **smooth** if it is $k$-times [continuously differentiable](Differentiability%20of%20Parametric%20Curves.md) for all $k \in \mathbb{N}$.
>
>^smoothness
>

>[!TIP] Tip: Piecewise Smoothness of Curve Parameterisations
>
>A [curve parameterisation](../Parametric%20Curve.md) $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ is **piecewise smooth** if $I$ can be expressed as a [union](../../../../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of a finite [collection](../../../../../Set%20Theory/Collections/Collection.md) of [intervals](../../../../../Set%20Theory/Ordering/Intervals.md) $I = I_1 \cup \cdots \cup I_p$ such that the [restrictions](../../../../Functions/Restriction.md) $\gamma \big|_{I_1}, \ldots, \gamma \big|_{I_n}$ are [smooth](Differentiability%20of%20Parametric%20Curves.md).
>
>^piecewise-smoothness
>