>[!THEOREM] The Squeeze Theorem for Sequences
>
>Let $(a_n)_{n \in \mathbb{N}}$ and $(b_n)_{n \in \mathbb{N}}$ be two [convergent](Convergence%20of%20Real%20Sequences.md) [sequences](../Real%20Sequence.md) with the same [limit](Convergence%20of%20Real%20Sequences.md) $L$.
>
>If $(c_n)_{n \in \mathbb{N}}$ is a [sequence](../Real%20Sequence.md) and there exists an integer $N_0$ such that $a_n \le c_n \le b_n$ for all $n \ge N_0$, then $(c_n)_{n \in \mathbb{N}}$ is also [convergent](Convergence%20of%20Real%20Sequences.md) and [approaches](Convergence%20of%20Real%20Sequences.md) $L$.
>
>$$\lim_{n\to\infty} c_n = \lim_{n\to\infty} a_n = \lim_{n\to\infty} b_n = L$$
>
>>[!PROOF]-
>>Let $\varepsilon \gt 0$. Since $(a_n)_{n \in \mathbb{N}}$ and $(b_n)_{n \in \mathbb{N}}$ are convergent, there exist $N_a, N_b \in \mathbb{N}$ such that
>>
>>$$|a_n - L| \lt \varepsilon \qquad \forall n \gt N_a$$
>>
>>$$|b_n - L| \lt \varepsilon \qquad \forall n \gt N_b$$
>>
>>We also assumed that there is an integer $N_0$ such that
>>
>>$$a_n \le c_n \le b_n \qquad \forall n \gt N_0$$
>>
>>It follows then
>>
>>$$L - \varepsilon \lt a_n \le c_n \le b_n \lt L + \varepsilon \qquad \forall n \ge \max \{N_0, N_a, N_b\}$$
>>
>>From this we see that
>>
>>$$L - \varepsilon \le c_n \le L + \varepsilon \qquad \forall n \ge \max \{N_0, N_a, N_b\}$$
>>
>>This is the same as
>>
>>$$|c_n - L| \lt \varepsilon \qquad n \ge \max \{N_0, N_a, N_b\}$$
>>