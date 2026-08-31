---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Symmetric Multilinear Forms

>[!DEFINITION] Definition: Symmetric Multilinear Form
>
>A [multilinear form](./Multilinear%20Forms.md) $f: V^n \to F$ is **symmetric** if for each [permutation](../../../Combinatorics/Permutations.md) $\sigma$ of $\{1,\dotsc, n\}$ and for all $\mathbf{v}_1, \dotsc, \mathbf{v}_n \in V$, we have
>
>$$f(\mathbf{v}_1, \dotsc, \mathbf{v}_n) = f(\mathbf{v}_{\sigma(1)}, \dotsc, \mathbf{v}_{\sigma(n)})$$
>

A [multilinear form](./Multilinear%20Forms.md) is [symmetric](./Symmetric%20Multilinear%20Forms.md) if it remains the same under every rearrangement of its arguments. 

## Definiteness

>[!DEFINITION] Definition: Definiteness
>
>A [symmetric multilinear form](./Symmetric%20Multilinear%20Forms.md) $f: V^n \to F$ is:
>
>- **positive definite** if $f(v, \dotsc, v) \gt 0$ for all $v \in V \setminus \{0\}$;
>- **positive semi-definite** if $f(v, \dotsc, v) \ge 0$ for all $v \in V$;
>- **negative definite** if $f(v, \dotsc, v) \lt 0$ for all $v \in V \setminus \{0\}$;
>- **negative semi-definite** if $f(v, \dotsc, v) \le 0$ for all $v \in V$;
>- **indefinite** if there exist $v, w \in V$ such that $f(v, \dotsc, v) \gt 0$ and $f(w, \dotsc, w) \lt 0$.
>