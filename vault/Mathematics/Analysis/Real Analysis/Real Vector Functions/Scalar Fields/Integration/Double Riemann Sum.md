>[!DEFINITION] Definition: Double Riemann Sum
>
>Let $f: R \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) over some rectangle $R = [a;b] \times [c;d] \subset \mathbb{R}^2$.
>
>1. Subdivide the interval $[a;b]$ into $m$ intervals $[x_{i-1}; x_i]$ of length $\Delta x = \frac{b - a}{m}$.
>
>2. Subdivide the interval $[c;d]$ into $n$ intervals $[y_{i-1}; y_i]$ of length $\Delta x = \frac{d - c}{n}$.
>
>3. These subdivision result in smaller rectangles $R_{ij} = \{(x,y)\mid x_{i-1} \le x \le x_i, y_{j-1} \le y \le y_j\},$ each with area $\Delta A = \Delta x \Delta y$.
>
>- For every choice of $(x_{ij}^\ast, y_{ij}^\ast) \in R_{ij}$ we get a **double Riemann sum** of $f$ **over** $R$.
>
>$$
>\sum_{i=1}^m\sum_{j=1}^n f(x_{ij}^\ast, y_{ij}^\ast)\Delta A
>$$
>