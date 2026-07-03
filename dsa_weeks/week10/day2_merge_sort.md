# Day 2: Merge Sort — Divide and Conquer

**Time:** ~50 minutes

Today you learn:
1. Divide and conquer
2. Merging sorted lists
3. Why merge sort is `O(n log n)`

**Practice file:** Create `day2_practice.py`

---

## Part 1: Divide

Merge sort repeatedly splits a list:

```text
[8, 3, 5, 1]
[8, 3] [5, 1]
[8] [3] [5] [1]
```

A list of zero or one item is already sorted.

---

## Part 2: Merge

```python
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

---

## Part 3: Merge Sort

```python
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    return merge(left, right)
```

There are about `log n` split levels. Each level merges `n` values.

Time: `O(n log n)`  
Extra space: `O(n)`

---

## Exercises

1. Merge `[1, 4, 8]` and `[2, 3, 9]`.
2. Draw all splits for `[6, 2, 5, 1]`.
3. Type merge sort from memory.
4. Compare it with bubble sort for large input.

