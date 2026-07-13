# 07: Pattern Quiz

This file is for active recall. Try to answer before looking at the answer.

## Quick Rules

```text
Direct lookup                 -> O(1)
One loop                      -> O(n)
Two separate loops            -> O(n)
Nested loops over same input  -> O(n^2)
Cut in half repeatedly        -> O(log n)
Build new list/dict/set       -> often O(n) space
```

---

## Quiz 1

```python
def first_item(nums):
    return nums[0]
```

Answer:

```text
Time: O(1)
Space: O(1)
```

Why:

```text
One direct index lookup.
```

---

## Quiz 2

```python
def contains(nums, target):
    for num in nums:
        if num == target:
            return True
    return False
```

Answer:

```text
Time: O(n)
Space: O(1)
```

Why:

```text
Worst case checks every item.
Only uses a few variables.
```

---

## Quiz 3

```python
def all_pairs(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(nums[i], nums[j])
```

Answer:

```text
Time: O(n^2)
Space: O(1)
```

Why:

```text
Pair checking grows like a grid.
```

---

## Quiz 4

```python
def make_squares(nums):
    squares = []

    for num in nums:
        squares.append(num * num)

    return squares
```

Answer:

```text
Time: O(n)
Space: O(n)
```

Why:

```text
One loop.
Builds a new list.
```

---

## Quiz 5

```python
def count_words(words):
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts
```

Answer:

```text
Time: O(n)
Space: O(n)
```

Why:

```text
One pass through words.
Dictionary can grow with unique words.
```

---

## Quiz 6

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

Answer:

```text
Time: O(log n)
Space: O(1)
```

Why:

```text
Each loop throws away half.
Only uses left, right, and mid.
```

---

## Quiz 7

```python
def has_pair_sum(nums, target):
    seen = set()

    for num in nums:
        needed = target - num

        if needed in seen:
            return True

        seen.add(num)

    return False
```

Answer:

```text
Time: O(n)
Space: O(n)
```

Why:

```text
One loop.
Set lookup is average O(1).
Set can grow with the input.
```

---

## Final Memory Drill

Fill these in from memory:

```text
O(1) means:
O(n) means:
O(n^2) means:
O(log n) means:
O(n) space often means:
```

Suggested answers:

```text
O(1): same amount of work no matter input size
O(n): work grows with number of items
O(n^2): pair/grid-style growth
O(log n): keep cutting the work in half
O(n) space: extra storage can grow with input
```
