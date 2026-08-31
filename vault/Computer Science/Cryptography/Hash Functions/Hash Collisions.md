---
tags:
    - cryptography
    - computer-science
---

# Hash Collisions

>[!DEFINITION] Definition: Hash Collision
>
>Let $h: \mathcal{M} \to \mathcal{H}$ be a [hash function](./Hash%20Functions.md).
>
>A **hash collision** is an [unordered pair](TODO) $\{m_1, m_2\} \subseteq \mathcal{M}$ with $m_1 \ne m_2$ and $h(m_1) = h(m_2)$.
>

>[!THEOREM] Theorem: Lower Bound for Collision Probability with Uniform Hashing
>
>Let $h: \mathcal{M} \to \mathcal{H}$ be a [hash function](./Hash%20Functions.md) [chosen uniformly](TODO) from $\{f: \mathcal{M} \to \mathcal{H}\}$ and let $m_1, \dotsc, m_p \in \mathcal{M}$ be distinct.
>
>The [probability](TODO) that there exists a [collision](./Hash%20Collisions.md) $\{m_i, m_j\} \subseteq \{m_1, \dotsc, m_p\}$ is at least the following:
>
>$$\Pr(\text{collision}) \ge 1 - \exp\left(-\frac{p(p-1)}{2|\mathcal{H}|}\right)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>