```
function quicksort(array, left, right)
    if right <= left
        return
        
    pivotIndex = partition(array, left, right)
    
    quicksort(array, left, pivotIndex - 1)
    quicksort(array, pivotIndex + 1, right)

function partition(array, left, right)
    p = selectPivotIndex(array, left, right)
    swap array[p] and array[right]
    
    i = left

    for (j = left; j <= right; j++)
        if array[j] <= array[right]
            swap array[i] and array[j]
            i++
    
    return i - 1

quicksort(array, 0, array.length() - 1)
```

- Worst-Case: $O(n^2)$
- Average: $O(n \log n)$