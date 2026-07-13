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

### 🧩 The whole recursion in one picture

Merge sort is recursion with a simple promise: *"I don't know how to sort a big list, but I DO know how to (a) split it in half, (b) trust myself to sort each half, and (c) merge two sorted halves."* The base case (`len <= 1`) is "a list this small is already sorted."

Trace `merge_sort([8, 3, 5, 1])`. Read **down** = splitting, **up** = merging back sorted:

```text
merge_sort([8, 3, 5, 1])
   split → left half [8,3], right half [5,1]
   ├─ merge_sort([8, 3])
   │     ├─ merge_sort([8]) → [8]   (len 1, base case)
   │     ├─ merge_sort([3]) → [3]   (len 1, base case)
   │     └─ merge([8], [3]) → [3, 8]   ← sorted!
   ├─ merge_sort([5, 1])
   │     ├─ merge_sort([5]) → [5]
   │     ├─ merge_sort([1]) → [1]
   │     └─ merge([5], [1]) → [1, 5]   ← sorted!
   └─ merge([3, 8], [1, 5]) → [1, 3, 5, 8]   ← fully sorted!
```

Notice the pattern: it keeps splitting until each piece is a single item (which is trivially "sorted"), then `merge` stitches pairs back together in order as the calls return. The sorting *happens during the merges on the way back up* — same "answers bubble up" idea as `max_depth`, just combining lists instead of numbers.

---

## Exercises

1. Merge `[1, 4, 8]` and `[2, 3, 9]`.
2. Draw all splits for `[6, 2, 5, 1]`.
3. Type merge sort from memory.
4. Compare it with bubble sort for large input.

