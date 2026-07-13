# 05: O(log n) Logarithmic Time

`O(log n)` means the work shrinks by cutting the problem down again and again.

The classic example is binary search.

## The Big Requirement

Binary search needs sorted data.

```python
nums = [1, 3, 5, 7, 9, 11, 13]
target = 9
```

Sorted means:

```text
small -> big
```

That lets us throw away half safely.

## Visual

Start:

```text
[1] [3] [5] [7] [9] [11] [13]
 L           M              R
```

Middle is `7`.

Target is `9`.

Since `9 > 7`, the target must be on the right side.

Throw away the left half:

```text
                [9] [11] [13]
                 L    M    R
```

Middle is `11`.

Target is `9`.

Since `9 < 11`, throw away the right side:

```text
                [9]
                 L
                 M
                 R
```

Found.

## Code

```python
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

## Why It Is Fast

If `n = 16`:

```text
16 -> 8 -> 4 -> 2 -> 1
```

Only about 4 cuts.

If `n = 1024`:

```text
1024 -> 512 -> 256 -> 128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
```

Only about 10 cuts.

That is `O(log n)`.

## Memory Hook

```text
Keep cutting in half = O(log n)
```

## What To Ask

```text
Can I safely throw away half of the remaining input?
```

If yes, you may have `O(log n)`.

If no, probably not.

## Tiny Practice

What is the Big O?

```python
while left <= right:
    mid = (left + right) // 2
    ...
```

Answer:

```text
Usually O(log n), if each step cuts the search space in half.
```

What if the list is unsorted?

```text
Binary search does not apply safely.
```
