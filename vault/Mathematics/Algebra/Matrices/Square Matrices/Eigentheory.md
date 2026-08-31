---
tags:
  - linear-algebra
  - algebra
  - mathematics
---

# Eigentheory

>[!DEFINITION] Definition: Eigenvector
>
>Let $A \in F^{n \times n}$ be a [square matrix](./Square%20Matrices.md).
>
>The **eigenvectors** of a [square matrix](./Square%20Matrices.md) $A \in F^{n \times n}$ are the [eigenvectors](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Eigentheory.md) of the [endomorphism](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Vector%20Space%20Endomorphisms.md) $f: F^n \to F^n$ whose [matrix representation](../../../Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md#Matrix%20Representations) with respect to the [standard basis](../Row%20and%20Column%20Vectors.md) of $F^n$ is $A$.
>

>[!DEFINITION] Definition: Eigenvalue
>
>The **eigenvalues** of a [square matrix](./Square%20Matrices.md) $A \in F^{n \times n}$ are the [eigenvalues](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Eigentheory.md#Eigenvalues%20and%20Eigenvectors) of the [endomorphism](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Vector%20Space%20Endomorphisms.md) $f: F^n \to F^n$ whose [matrix representation](../../../Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md#Matrix%20Representations) with respect to the [standard basis](../Row%20and%20Column%20Vectors.md) of $F^n$ is $A$.
>
>>[!DEFINITION] Definition: Eigenspace
>>
>>The **eigenspace** of an [eigenvalue](./Eigentheory.md) of $A$ is its [eigenspace](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Eigentheory.md#Eigenvalues%20and%20Eigenvectors) as an [eigenvalue](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Eigentheory.md#Eigenvalues%20and%20Eigenvectors) of $f$.
>>
>
>>[!DEFINITION] Definition: Geometric Multiplicity
>>
>>The **geometric multiplicity** of an [eigenvalue](./Eigentheory.md) of $A$ is its [geometric multiplicity](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Eigentheory.md#Eigenvalues%20and%20Eigenvectors) as an [eigenvalue](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Eigentheory.md#Eigenvalues%20and%20Eigenvectors) of $f$.
>>
>
>>[!DEFINITION] Definition: Algebraic Multiplicity
>>
>>The **algebraic multiplicity** of an [eigenvalue](./Eigentheory.md) of $A$ is its [algebraic multiplicity](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Eigentheory.md#Characteristic%20Polynomials) as an [eigenvalue](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Eigentheory.md#Eigenvalues%20and%20Eigenvectors) of $f$.
>>
>

>[!DEFINITION] Definition: Characteristic Polynomial
>
>The **characteristic polynomial** of a [square matrix](./Square%20Matrices.md) $A \in F^{n \times n}$ is the [characteristic polynomial](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Eigentheory.md) of the [endomorphism](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Vector%20Space%20Endomorphisms.md) $f: F^n \to F^n$ whose [matrix representation](../../../Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md#Matrix%20Representations) with respect to the [standard basis](../Row%20and%20Column%20Vectors.md) of $F^n$ is $A$.
>
>>[!EXAMPLE]- Example: $A \in \mathbb{R}^{2\times 2}$ and $A \in \mathbb{C}^{2 \times 2}$
>>
>>Consider the following [real matrix](../Real%20Matrices/Real%20Matrices.md):
>>
>>$$A = \begin{bmatrix}0 & 1 \\ -1 & 0\end{bmatrix} \in \mathbb{R}^{2 \times 2}$$
>>
>>Its [characteristic polynomial](./Eigentheory.md) is 
>>
>>$$\chi_A (\lambda) = \det \left(\begin{bmatrix}0 & 1 \\ -1 & 0\end{bmatrix} - \lambda I_2\right) = \det \left(\begin{bmatrix}- \lambda & 1 \\ -1 & -\lambda \end{bmatrix}\right) = \lambda^2 + 1$$
>>
>>This [real polynomial](../../Fields/The%20Real%20Numbers/Real%20Polynomials.md) has no [roots](../../Fields/The%20Real%20Numbers/Real%20Polynomials.md) and so $A$ has no [eigenvalues](./Eigentheory.md).
>>
>>Now consider the following [complex matrix](../Complex%20Matrices/Complex%20Matrices.md):
>>
>>$$A = \begin{bmatrix}0 & 1 \\ -1 & 0\end{bmatrix} \in \mathbb{C}^{2 \times 2}$$
>>
>>Its [characteristic polynomial](./Eigentheory.md) is 
>>
>>$$\chi_A (\lambda) = \det \left(\begin{bmatrix}0 & 1 \\ -1 & 0\end{bmatrix} - \lambda I_2\right) = \det \left(\begin{bmatrix}- \lambda & 1 \\ -1 & -\lambda \end{bmatrix}\right) = \lambda^2 + 1$$
>>
>>This [complex polynomial](../../Fields/The%20Complex%20Numbers/Complex%20Polynomials.md) has the [roots](../../Fields/The%20Complex%20Numbers/Complex%20Polynomials.md) $-\mathrm{i}$ and $\mathrm{i}$. Therefore, $A$ has the [eigenvalues](./Eigentheory.md)  $-\mathrm{i}$ and $\mathrm{i}$.
>>
>


