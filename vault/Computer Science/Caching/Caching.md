---
tags:
    - computer-science
---

# Caching

Structurally, a [cache](./Caching.md) is organized into blocks of fixed size called **cache blocks** or **cache lines**. Data can be transfer into and out of a [cache](./Caching.md) only as entire [cache lines](./Caching.md).

## Reading

>[!DEFINITION] Definition: Cache Hit
>
>A **cache hit** is a situation in which data to be read is found within a given [cache](./Caching.md).
>
>>[!DEFINITION] Definition: Hit Time
>>
>>The time it takes to read data from a [cache](./Caching.md) in case of a [cache hit](./Caching.md).
>>
>
>>[!DEFINITION] Definition: Hit Rate
>>
>>The **hit rate** is the probability of a [cache hit](./Caching.md) occurring.
>>
>

>[!DEFINITION] Definition: Cache Miss
>
>A **cache miss** is a situation in which data to be read is not found within a given [cache](./Caching.md).
>
>>[!DEFINITION] Definition: Miss Time
>>
>>
>>
>
>>[!DEFINITION] Definition: Miss Rate
>>
>>The **miss rate** is the probability of a [cache hit](./Caching.md) occurring.
>>
>

## Replacement Policies

**Replacement** occurs when a [cache](./Caching.md) needs to store a new cache line but it has no free space left. To store the new cache line, the cache must flush out one of its occupied cache lines to another place and replace it with the contents of the new cache line.

>[!DEFINITION] Definition: Replacement Policy
>
>The **replacement policy** of a [cache](./Caching.md) determines which [cache line](./Caching.md) is to be replaced.
>

>[!DEFINITION] Definition: Least Recently Used
>
>The **
>