---
tags:
    - statistics
    - probability
    - mathematics
---

# Linear Regression

**Linear regression** refers to finding linear models which best approximate the relationship between a set of variables $x_1, \dotsc, x_m$ and another set of variables $y_1, \dotsc, y_n$ based on data samples.

## Multiple Linear Regression

In **multiple linear regression**, we want to find a linear model which best describes how a single variable $y$ depends on some other variables $x_1, \dotsc, x_m$. 

>[!DEFINITION] Definition: Multiple Linear Regression
>
>Let $(x_1^{(1)}, \dotsc, x_m^{(1)}, y^{(1)}), \dotsc, (x_1^{(p)}, \dotsc, x_m^{(p)}, y^{(p)})$ be a [set](../Set%20Theory/Sets.md) of data points.
>
>A **multiple linear regression model** is a [linear](../Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md) [function](../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^m \to \mathbb{R}$.

For computational reasons, we exclusively work with a modified [matrix representation](../Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md#Matrix%20Representations) 

$$f(\boldsymbol{x}) = \boldsymbol{\beta}^{\mathsf{T}} \begin{bmatrix}1 \\ x_1 \\ \vdots \\ x_m\end{bmatrix},$$

where $\boldsymbol{\beta} = \begin{bmatrix} \beta_0, \beta_1,\dotsc, \beta_m\end{bmatrix}^{\mathsf{T}} \in \mathbb{R}^{m+1}$.

>[!DEFINITION] Definition: Residual
>
>The **residual** of a sample $(x_1^{(k)}, \dotsc, x_m^{(k)}, y^{(k)})$ under $f$ is a [real scalar field](../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $r_k: \mathbb{R}^{m+1} \to \mathbb{R}$ defined as follows:
>
>$$r_k(\boldsymbol{\beta}) \overset{\text{def}}{=} y^{(k)} - \boldsymbol{\beta}^{\mathsf{T}}\begin{bmatrix}1 \\ x_1^{(k)} \\ \vdots \\ x_m^{(k)} \end{bmatrix}$$
>

The goal is to find $\boldsymbol{\beta}$ such that the [residuals](#Multiple%20Linear%20Regression) are "minimal" (what this means exactly, varies by context).

### Ordinary Least Squares

In the **ordinary least squares method**, we want to minimize the sum of the squares of all [residuals](#Multiple%20Linear%20Regression):

$$\sum_{k = 1}^p r_k(\boldsymbol{\beta})^2$$

To achieve this, we define a [real vector function](../Analysis/Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Functions.md) $r: \mathbb{R}^{m+1} \to \mathbb{R}^p$ which contains the [residuals](#Multiple%20Linear%20Regression):

$$r(\boldsymbol{\beta}) = \begin{bmatrix} r_1 (\boldsymbol{\beta}) \\ \vdots \\ r_p (\boldsymbol{\beta})\end{bmatrix}$$

This can be expressed as

$$r(\boldsymbol{\beta}) = \boldsymbol{y} - \boldsymbol{A} \boldsymbol{\beta}$$

where $\boldsymbol{A} \in \mathbb{R}^{p \times (m+1)}$ is the [real matrix](../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) containing our features (with $x_0^{(k)} = 1$ in the first column)

$$\boldsymbol{A} =  \begin{bmatrix} 1 & x_1^{(1)} & x_2^{(1)} & \cdots & x_m^{(1)} \\ 1 & x_1^{(2)} & x_2^{(2)} & \cdots & x_m^{(2)} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_1^{(p)} & x_2^{(p)} & \cdots & x_m^{(p)} \end{bmatrix}$$

and

$$\boldsymbol{y} = \begin{bmatrix}y^{(1)} \\ \vdots \\ y^{(p)}\end{bmatrix}.$$

We have

$$\sum_{k = 1}^p r_k(\boldsymbol{\beta})^2 = ||r(\boldsymbol{\beta})||^2$$

and so the goal now is to find the [minima](../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Extrema%20(Real%20Scalar%20Fields).md) of the [real scalar field](../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $g(\boldsymbol{\beta}) = ||r(\boldsymbol{\beta})||^2$. 

>[!THEOREM] Theorem: The Normal Equation
>
>In the [ordinary least squares method](#Ordinary%20Least%20Squares), if $g$ has a [local minimum](../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Extrema%20(Real%20Scalar%20Fields).md#Local%20Extrema) at $\boldsymbol{\beta}$, then:
>
>$$\boldsymbol{A}^{\mathsf{T}}\boldsymbol{A} \boldsymbol{\beta} = \boldsymbol{A}^{\mathsf{T}}\boldsymbol{y}$$
>
>>[!PROOF]-
>>
>>We have:
>>
>>$$\begin{aligned}g(\boldsymbol{\beta}) & = ||r(\boldsymbol{\beta})||^2 \\ & = ||\boldsymbol{y} - \boldsymbol{A} \boldsymbol{\beta}||^2 \\ & = (\boldsymbol{y} - \boldsymbol{A} \boldsymbol{\beta})^{\mathsf{T}} (\boldsymbol{y} - \boldsymbol{A} \boldsymbol{\beta}) \\ & = \boldsymbol{y}^{\mathsf{T}} \boldsymbol{y} - 2\boldsymbol{\beta}^{\mathsf{T}} \boldsymbol{A}^{\mathsf{T}} \boldsymbol{y} + \boldsymbol{\beta}^{\mathsf{T}} \boldsymbol{A}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{\beta}\end{aligned}$$
>>
>>We see that $g$ is [continuously partially differentiable](../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) everywhere. For $g$'s [gradient](../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Gradient%20(Real%20Scalar%20Fields).md), we have
>>
>>$$\begin{aligned}\nabla g(\boldsymbol{\beta}) & = \nabla (\boldsymbol{y}^{\mathsf{T}} \boldsymbol{y} - 2\boldsymbol{\beta}^{\mathsf{T}} \boldsymbol{A}^{\mathsf{T}} \boldsymbol{y} + \boldsymbol{\beta}^{\mathsf{T}} \boldsymbol{A}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{\beta}) \\ & = \nabla(\boldsymbol{y}^{\mathsf{T}} \boldsymbol{y}) - \nabla(2\boldsymbol{\beta}^{\mathsf{T}} \boldsymbol{A}^{\mathsf{T}} \boldsymbol{y}) + \nabla(\boldsymbol{\beta}^{\mathsf{T}} \boldsymbol{A}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{\beta}) \\ & = \boldsymbol{0} - 2\boldsymbol{A}^{\mathsf{T}}\boldsymbol{y} + (\boldsymbol{A}^{\mathsf{T}}\boldsymbol{A} + (\boldsymbol{A}^{\mathsf{T}}\boldsymbol{A})^{\mathsf{T}})\boldsymbol{\beta} \\ & = -2\boldsymbol{A}^{\mathsf{T}}\boldsymbol{y} + 2\boldsymbol{A}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{\beta}\end{aligned}$$
>>
>>Since $g$ has a [local minimum](../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Extrema%20(Real%20Scalar%20Fields).md#Local%20Extrema) at $\boldsymbol{\beta}$, all of its [directional derivatives](../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Directional%20Differentiability%20(Real%20Scalar%20Fields).md) there are zero and so $\nabla g(\boldsymbol{\beta})$ must be zero:
>>
>>$$\nabla g(\boldsymbol{\beta}) = -2\boldsymbol{A}^{\mathsf{T}}\boldsymbol{y} + 2\boldsymbol{A}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{\beta} = \boldsymbol{0}$$
>>
>>Finally, this implies the following:
>>
>>$$\boldsymbol{A}^{\mathsf{T}}\boldsymbol{y} = \boldsymbol{A}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{\beta}$$
>>
>

>[!THEOREM] Theorem: Unique Solution
>
>If $\boldsymbol{A}$ has full [rank](../Algebra/Matrices/Matrix%20Rank.md) with $p \ge m+1$ and $\boldsymbol{A}^{\mathsf{T}}\boldsymbol{A} \boldsymbol{\beta} = \boldsymbol{A}^{\mathsf{T}}\boldsymbol{y}$, then $g$ has a [global minimum](../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Extrema%20(Real%20Scalar%20Fields).md) at $\boldsymbol{\beta}$.
>
>>[!PROOF]-
>>
>>For the [Hessian matrix](../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Hessian%20Matrix.md) of $g$, we have:
>>
>>$$H_g(\boldsymbol{\beta}) = 2\boldsymbol{A}^{\mathsf{T}}\boldsymbol{A}$$
>>
>>Since $p \ge m+1$ and since $\boldsymbol{A}$ has full [rank](../Algebra/Matrices/Matrix%20Rank.md), we know that $\boldsymbol{A}^{\mathsf{T}}\boldsymbol{A}$ is [positive definite](../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md#Definiteness) and so $H_g(\boldsymbol{\beta})$ is [positive definite](../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md#Definiteness). Therefore, $g$ has a [local minimum](../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Extrema%20(Real%20Scalar%20Fields).md) at $\boldsymbol{\beta}$.
>>
>>TODO: Prove [global minimum](../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Extrema%20(Real%20Scalar%20Fields).md).
>>
>

>[!EXAMPLE]-
>
>Consider the following data sets:
>
>|$x_k$|$-2$|$-1$|$0$|$1$|$2$|
>|:--:|:--:|:--:|:--:|:--:|:--:|
>|$y_k$|$0.5$|$0.8$|$2$|$3.2$|$3.5$|
>
>We have:
>
>$$\boldsymbol{A} = \begin{bmatrix}1 & -2 \\ 1 & -1 \\ 1 & 0 \\ 1 & 1 \\ 1 & 2 \end{bmatrix} \qquad \boldsymbol{A}^{\mathsf{T}}\boldsymbol{A} = \begin{bmatrix}5 & 0 \\ 0 & 10\end{bmatrix} \qquad \boldsymbol{y} = \begin{bmatrix}0.5 \\ 0.8 \\ 2 \\ 3.2 \\ 3.5\end{bmatrix}$$
>
>Let's examine $\boldsymbol{A}^{\mathsf{T}}\boldsymbol{A} \boldsymbol{\beta} = \boldsymbol{A}^{\mathsf{T}}\boldsymbol{y}$:
>
>$$\begin{bmatrix}5 & 0 \\ 0 & 10\end{bmatrix} \boldsymbol{\beta} = \begin{bmatrix}10 \\ 8.4\end{bmatrix}$$
>
>We get:
>
>$$\boldsymbol{\beta} = \begin{bmatrix}\beta_0 \\ \beta_1\end{bmatrix} = \begin{bmatrix}5 & 0 \\ 0 & 10\end{bmatrix}^{-1}\begin{bmatrix}10 \\ 8.4\end{bmatrix} = \begin{bmatrix}2 \\ 0.84\end{bmatrix}$$
>
>Since $p = 5 \ge m + 1 = 2$ and since $\boldsymbol{A}$ has full [rank](../Algebra/Matrices/Matrix%20Rank.md), we know that $\boldsymbol{b} = (2, 0.84)$ minimizes the square of the [residuals](#Multiple%20Linear%20Regression). Therefore, the [ordinary least squares method](#Ordinary%20Least%20Squares) gives us the following [linear regression model](#Multiple%20Linear%20Regression):
>
>$$y = 0.84x + 2$$
>