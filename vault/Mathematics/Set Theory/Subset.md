>[!DEFINITION] Definition: Subset
>
>A [set](Set.md) $A$ is a **subset** of the [set](Set.md) $B$ if all elements of $A$ are also elements of $B$.
>
>$$
>a \in A \implies a \in B
>$$
>
>>[!NOTATION]-
>>
>>If $A$ is a subset of $B$, we write $A \subseteq B$.
>>
>>If $A$ is *not* a subset of $B$, we write $A \not\subseteq B$.
>>
>
>>[!DEFINITION] Definition: True Subset
>>
>>A [set](Set.md) $A$ is a **true subset** of the [set](Set.md) $B$ if $A \subseteq B$ and $A \ne B$.
>>
>>$$
>>(a\in A \implies a\in B) \land (\exists b \in B : b \notin A)
>>$$
>>
>>In other words, there are elements in $B$ which are *not* elements of $A$.
>>
>>>[!NOTATION]-
>>>
>>>If $A$ is a true subset of $B$, we write $A \subset B$.
>>>
>>>If $A$ is a subset, but not a *true* subset, of $B$, we write $A \subsetneq B$.
>>>
>>
>>>[!NOTE]
>>>
>>>True subset are also known as **strict subsets**.
>>>
>>
>