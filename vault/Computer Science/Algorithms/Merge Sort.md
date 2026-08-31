---
tags:
    - algorithms
    - computer-science
---

# Merge Sort

```rust
fn mergeSort(s: Sequence) -> Sequence
{
    if s.length() <= 1
    {
        return s;
    }
    
    let (left, right) = split(s);
    return merge(mergeSort(left), mergeSort(right));
}

fn merge(left: Sequence, right: Sequence) -> Sequence
{
    if left.is_empty()
        return right;
    
    if right.is_empty()
        return left;

    if left.first() <= right.first()
        return concat(left.first(), merge(left.tail_after(0), right));
    else
        return concat(right.first(), merge(left, right.tail_after(0)));
}
```

- Worst-case: $O(n \log n)$
- Average: $\Theta (n \log n)$

## Singly Linked List

```cpp

```
