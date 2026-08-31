---
tags:
    - experimental-physics
    - physics
---

# Uncertainty

No physical quantity can ever be measured to an exact value.


## Statistical Errors

>[!DEFINITION] Definition: Statistical Error
>
>A **statistical error** is a uncertainty in the value of the measurement which arises from probabilistic processes.
>

[Statistical errors](#Statisical%20Errors) are typically mitigated by conducting multiple measurements $x_1, \dotsc, x_n$ and taking their [arithmetic average]:

$$\overline{x} = \frac{1}{n} \sum_{k = 1}^n x_k$$

To quantify how these measurements are distributed around $\overline{x}$, we use the [standard deviation](TODO):

$$s = \sqrt{\frac{1}{n-1} \sum_{k=1}^n (x_k - \overline{x})^2} = \sqrt{\frac{1}{n-1}\left( \sum_{k = 1}^n x_k^2 - \frac{1}{n} \left(\sum_{k = 1}^n x_k\right)^2 \right)}$$