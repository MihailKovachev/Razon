---
tags:
    - set-theory
    - mathematics
---

# Interval

>[!DEFINITION] Definition: Interval
>
>Let $(S, \le)$ be a [totally ordered set](./Totally%20Ordered%20Set.md).
>
>An **interval** is a [subset](../Subsets.md) $I$ of $S$ such that, for all $x,z \in I$ and all $y \in S$, if $x \le y$ and $y \le z$, then $y \in I$:
>
>$$\forall x,z \in I, \forall y \in S: (x \le y \le z) \implies y \in I$$
>
>>[!DEFINITION] Definition: Open Interval
>>
>>An **open interval** is an [interval](./Interval.md) $I$ for which there exist $a, b \in S$ with $a \lt b$ and $a \lt x \lt b$ for all $x \in I$:
>>
>>$$\exists a, b \in S: I = \{x \in S \mid a \lt x \lt b\}$$
>>
>>>[!NOTATION]
>>>
>>>We denote $I$ by $(a,b)$ or $]a,b[$.
>>>
>>
>
>>[!DEFINITION] Definition: Left-Open, Right-Closed Interval
>>
>>A **left-open, right-closed interval** (or half-open interval) is an [interval](./Interval.md) $I$ for which there exist $a, b \in S$ with $a \lt b$ and $a \lt x \le b$ for all $x \in I$:
>>
>>$$\exists a, b \in S: I = \{x \in S \mid a \lt x \le b\}$$
>>
>>>[!NOTATION]
>>>
>>>We denote $I$ by $(a,b]$ or $]a,b]$.
>>>
>>
>
>>[!DEFINITION] Definition: Left-Closed, Right-Open Interval
>>
>>A **left-closed, right-open interval** (or half-open interval) is an [interval](./Interval.md) $I$ for which there exist $a, b \in S$ with $a \lt b$ and $a \le x \lt b$ for all $x \in I$:
>>
>>$$\exists a, b \in S: I = \{x \in S \mid a \le x \lt b\}$$
>>
>>>[!NOTATION]
>>>
>>>We denote $I$ by $[a,b)$ or $[a,b[$.
>>>
>>
>
>>[!DEFINITION] Definition: Closed Interval
>>
>>A **closed interval** is an [interval](./Interval.md) $I$ for which there exist $a, b \in S$ with $a \le b$ and $a \le x \le b$ for all $x \in I$:
>>
>>$$\exists a, b \in S: I = \{x \in S \mid a \le x \le b\}$$
>>
>>>[!NOTATION]
>>>
>>>We denote $I$ by $[a,b]$.
>>>
>>
>
>>[!DEFINITION] Definition: Left-Bounded Open Ray
>>
>>A **left-bounded open ray** (or open upward ray) is an [interval](./Interval.md) $I$ for which there exists $a \in S$ such that $a \lt x$ for all $x \in I$:
>>
>>$$\exists a \in S: I = \{x \in S \mid a \lt x\}$$
>>
>>>[!NOTATION]
>>>
>>>We denote $I$ by $(a, \infty)$ or $]a, \infty[$.
>>>
>>
>
>>[!DEFINITION] Definition: Left-Bounded Closed Ray
>>
>>A **left-bounded closed ray** (or closed upward ray) is an [interval](./Interval.md) $I$ for which there exists $a \in S$ such that $a \le x$ for all $x \in I$:
>>
>>$$\exists a \in S: I = \{x \in S \mid a \le x\}$$
>>
>>>[!NOTATION]
>>>
>>>We denote $I$ by $[a, \infty)$ or $[a, \infty[$.
>>>
>>
>
>>[!DEFINITION] Definition: Right-Bounded Open Ray
>>
>>A **right-bounded open ray** (or open downward ray) is an [interval](./Interval.md) $I$ for which there exists $b \in S$ such that $x \lt b$ for all $x \in I$:
>>
>>$$\exists b \in S: I = \{x \in S \mid x \lt b\}$$
>>
>>>[!NOTATION]
>>>
>>>We denote $I$ by $(-\infty, b)$ or $]-\infty, b[$.
>>>
>>
>
>>[!DEFINITION] Definition: Right-Bounded Closed Ray
>>
>>A **right-bounded closed ray** (or closed downward ray) is an [interval](./Interval.md) $I$ for which there exists $b \in S$ such that $x \le b$ for all $x \in I$:
>>
>>$$\exists b \in S: I = \{x \in S \mid x \le b\}$$
>>
>>>[!NOTATION]
>>>
>>>We denote $I$ by $(-\infty, b]$ or $]-\infty, b]$.
>>>
>>
>

>[!THEOREM] Theorem: Empty Set is Interval
>
>If $(S, \le)$ is a [totally ordered set](./Totally%20Ordered%20Set.md), then the [empty set](TODO) is an [interval](./Interval.md).
>
>>[!NOTE]
>>
>>Sometimes we denote $\varnothing$ in one of the following ways for any $a \in S$:
>>
>>$$(a, a) \qquad (a, a] \qquad ]a,a] \qquad [a,a) \qquad [a,a[$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Singletons are Intervals
>
>If $(S, \le)$ is a [totally ordered set](./Totally%20Ordered%20Set.md), then every [singleton](TODO) is an [interval](./Interval.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Set Itself is Interval
>
>If $(S, \le)$ is a [totally ordered set](./Totally%20Ordered%20Set.md), then the [set](../Sets.md) $S$ is an [interval](./Interval.md).
>
>>[!NOTATION]
>>
>>We sometimes denote $S$ by $(-\infty, \infty)$ or $]-\infty,\infty[$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>