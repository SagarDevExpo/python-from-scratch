# Day 4: Sliding Window

**Time:** ~45 minutes

Today you learn:
1. Fixed-size windows
2. Avoiding repeated work
3. Variable-size windows

**Practice file:** Create `day4_practice.py`

---

## Part 1: The Slow Approach

Find the largest sum of `k` consecutive values:

```python
def max_sum_slow(numbers, k):
    best = 0

    for start in range(len(numbers) - k + 1):
        current = sum(numbers[start:start + k])
        best = max(best, current)

    return best
```

Each window is summed again, causing repeated work.

---

## Part 2: Slide the Window

When moving right:

- Subtract the value leaving
- Add the value entering

```python
def max_window_sum(numbers, k):
    if k > len(numbers):
        return None

    window_sum = sum(numbers[:k])
    best = window_sum

    for right in range(k, len(numbers)):
        left = right - k
        window_sum -= numbers[left]
        window_sum += numbers[right]
        best = max(best, window_sum)

    return best
```

Time: `O(n)`  
Extra space: `O(1)`

---

## Part 3: Variable Window

Some windows grow and shrink. For “longest substring without repeated
characters”:

1. Move the right edge forward.
2. If a duplicate appears, move the left edge.
3. Track the largest valid window.

This commonly combines two pointers with a set or dictionary.

---

## Exercises

1. Find the average of every window of size `k`.
2. Find the smallest sum of `k` consecutive numbers.
3. Trace window boundaries on paper.
4. Attempt longest substring without repeated characters.

