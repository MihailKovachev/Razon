---
tags:
    - digital-circuits
    - electrical-engineering
---

# Comparators

**Comparators** are [digital circuits](./Digital%20Circuits.md) which serve to compare binary values. 

Two binary values are equal only when they have the same bits. If one bit differs, then the values must be different. Therefore, checking if two binary values $(a_{n-1},\dotsc,a_0$ and $(b_{n-1},\dotsc,b_0)$ are different is equivalent to computing the following [Boolean function](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md):

$$
a \ne b: \qquad (a_{n-1} \oplus b_{n-1}) + \cdots + (a_0 \oplus b_0)
$$

To check if a binary value $A$ is smaller than another binary value $B$, we can use a [subtractor](./Subtractors.md) to calculate $A - B$ and then examine the most significant bit of the result. If it is one, then $A - B \lt 0$ and we know that $A \lt B$. If it is zero, then $A - B \ge 0$ and we know that $A \ge B$.