---
tags:
    - algebra
    - mathematics
---

# Newton's Method

**Newton's method** is a numerical algorithm for finding solutions to equations of the form $f(x) = 0$, where $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ is a [real function](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md), or to systems of equations which can be written as $f(\boldsymbol{x}) = \boldsymbol{0}$ for some [real vector field](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Fields/Real%20Vector%20Fields.md) $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$.

## In One Dimension

>[!ALGORITHM] Algorithm: Newton's Method in One Dimension
>
>We want to find a solution $x^{\ast} \in I$ to the equation
>
>$$f(x) = 0,$$
>
>where $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ is a [real function](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) and $I \subseteq \mathcal{D}$ is some [open interval](../../Mathematics/Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line). 
>
>1. Pick an initial guess $x_0 \in I$.
>2. Define the [sequence](../../Mathematics/Analysis/Real%20Analysis/Real%20Sequences.md) $(x_n)_{n \in \mathbb{N}_0}$ as follows:
>
>$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \qquad \forall n \ge 0$$
>
>3. Evaluate $(x_n)_{n \in \mathbb{N}_0}$ until $|x_{n+1} - x_n| \lt \tau$, where $\tau \gt 0$ is your acceptable error tolerance.
>

Provided that $f$ satisfies some conditions and if the initial guess is chosen appropriately, the above algorithm converges quadratically to a [root](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) of $f$.

>[!THEOREM] Theorem: Local Quadratic Convergence
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) and let $I \subseteq \mathcal{D}$ be [open interval](../../Mathematics/Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line).
>
>If $f$ satisfies the following conditions:
>
>- It is [twice continuously differentiable](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Differentiability%20(Real%20Functions).md) on $I$;
>- There exists some $x^{\ast} \in I$ such that $f(x^{\ast}) = 0$;
>- $f'(x^{\ast}) \ne 0$;
>
>then there exists some  [open neighborhood](../../Mathematics/Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $N(x^{\ast})$ such that for any $x_{0} \in N(x^{\ast})$ we have the following:
>
>- $f'(x_n) \ne 0$ for all $n \ge 0$;
>- The [sequence](../../Mathematics/Analysis/Real%20Analysis/Real%20Sequences.md) $(x_n)_{n \in \mathbb{N}_0}$ with $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$ for all $n \ge 0$ [converges](../../Mathematics/Analysis/Real%20Analysis/Real%20Sequences.md#Convergence) to $x^{\ast}$;
>- This [convergence](../../Mathematics/Analysis/Real%20Analysis/Real%20Sequences.md#Convergence) is quadratic:
>
>$$\lim_{n \to \infty} \frac{|x_{n+1} - x^{\ast}|}{|x_n - x^{\ast}|^2} = \left\vert \frac{f''(x^{\ast})}{2f'(x^{\ast})} \right\vert$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Global Monotone Convergence
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) and let $[a,b] \subseteq \mathcal{D}$ be [closed interval](../../Mathematics/Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line).
>
>If $f$ satisfies all of the following conditions:
>
>- It is [continuous](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Continuity%20(Real%20Functions).md) on $[a,b]$ and [twice continuously differentiable](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Differentiability%20(Real%20Functions).md) on $(a,b)$;
>- It is [monotone](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Monotonicity%20of%20Real%20Functions.md) on $[a,b]$.
>- There is some $x^{\ast} \in (a,b)$ with $f(x^{\ast}) = 0$;
>- It is either [strictly concave](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Concavity%20and%20Convexity%20of%20Real%20Functions.md) or [strictly convex](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Concavity%20and%20Convexity%20of%20Real%20Functions.md) on $[a,b]$;
>
>then for any $x_0 \in [a,b]$ with $f(x_0) \cdot f''(x_0) \gt 0$ we have the following:
>
>- $f'(x_n) \ne 0$ for all $n \ge 0$;
>- The [sequence](../../Mathematics/Analysis/Real%20Analysis/Real%20Sequences.md) $(x_n)_{n \in \mathbb{N}_0}$ with $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$ for all $n \ge 0$ is [monotone](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Monotonicity%20of%20Real%20Functions.md) and [converges](../../Mathematics/Analysis/Real%20Analysis/Real%20Sequences.md#Convergence) to $x^{\ast}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

## In Multiple Dimensions

>[!ALGORITHM] Algorithm: Newton's Method
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Fields/Real%20Vector%20Fields.md) which is [totally differentiable](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) on some [open set](../../Mathematics/Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md) $U \subseteq \mathcal{D}$.
>
>We want to find some $\boldsymbol{p} \in U$ such that $f(\boldsymbol{p}) = \boldsymbol{0}$.
>
>1. Pick an initial guess $\boldsymbol{p}_0 \in U$, an iteration limit $N_{\text{max}} \in \mathbb{N}$ and an acceptable error tolerance $\tau \gt 0$.
>2. For $i \in \{0, 1, \dotsc, N_{\text{max}}\}$:
>
>    - Attempt to solve $J_f(\boldsymbol{p}_i) \Delta \boldsymbol{p}_i = -f(\boldsymbol{p}_i)$ for $\Delta \boldsymbol{p}_i$. Return if an error occurs.
>    - If $||\Delta \boldsymbol{p}_i|| \lt \tau$, then return $\boldsymbol{p}_{i+1}$.
>    - Set $\boldsymbol{p}_{i+1} = \boldsymbol{p}_i + \Delta \boldsymbol{p}_i$.
>
>3. If step 2 did not return, then return an error, since a desirable approximation of $\boldsymbol{p}$ could not be found within the allotted number of iterations.
>

Provided that $f$ satisfies some conditions and if the initial guess is chosen appropriately, the above algorithm converges quadratically to a [root](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Functions.md) of $f$.

>[!THEOREM] Theorem: Local Quadratic Convergence (Multivariate Newton's Method)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Fields/Real%20Vector%20Fields.md) and let $U \subseteq \mathcal{D}$ be an [open set](../../Mathematics/Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md).
>
>If $f$ satisfies the following conditions:
>
>- It is [twice continuously differentiable](../../Analysis/Real%20Analysis/Real%20Vector%20Fields/Differentiation%20of%20Real%20Vector%20Fields.md) on $U$;
>- There exists some $x^{\ast} \in U$ such that $f(\boldsymbol{x}^{\ast}) = \mathbf{0}$;
>- The [Jacobian](../../Analysis/Real%20Analysis/Real%20Vector%20Fields/Differentiation%20of%20Real%20Vector%20Fields.md)  $J_f(\boldsymbol{x}^{\ast})$ is [invertible](../../Mathematics/Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md);
>
>then there exists some [open neighborhood](../../Mathematics/Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md) $N(\boldsymbol{x}^{\ast})$ such that for any $\boldsymbol{x}_{0} \in N(\boldsymbol{x}^{\ast})$ we have the following:
>
>- $J_f(\boldsymbol{x}_n)$ is [invertible](../../Mathematics/Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md) for all $n \ge 0$;
>- The [sequence](TODO) $(\boldsymbol{x}_n)_{n \in \mathbb{N}_0}$ defined as $\boldsymbol{x}_{n+1} = \boldsymbol{x}_n - J^{-1}_f(\boldsymbol{x}_n)\cdot f(\boldsymbol{x}_n)$ for all $n \ge 0$ [converges](TODO) to $x^{\ast}$;
>- This [convergence](TODO) is quadratic:
>
>$$\limsup_{n \to \infty} \frac{\|x_{n+1} - x^{\ast}\|}{\|x_n - x^{\ast}\|^2} \le \frac{1}{2} \| J_f(x^{\ast})^{-1} \| \, \| D^2 f(x^{\ast}) \|$$
>
>>[!PROOF]-
>>
>>TODO
>>
>