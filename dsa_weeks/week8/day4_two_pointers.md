# Day 4: Two Pointers

**Time:** ~40 minutes

Today you learn:
1. Pointers moving from opposite ends
2. Pointers moving in the same direction
3. Common two-pointer problems

**Practice file:** Create `day4_practice.py`

---

## Part 1: Opposite Ends

Palindrome check:

```python
def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True
```

Time: `O(n)`  
Space: `O(1)`

---

## Part 2: Pair Sum in Sorted Data

```python
def pair_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1

    return []
```

This requires sorted input.

---

## Part 3: Merge Sorted Lists

Use one pointer for each list. Compare the current values, append the smaller
one, then move that pointer.

```python
left = [1, 4, 7]
right = [2, 3, 8]
# result: [1, 2, 3, 4, 7, 8]
```

---

## Exercises

1. Reverse a list in place.
2. Solve pair sum for sorted numbers.
3. Merge two sorted lists without `.sort()`.
4. Remove duplicates from a sorted list.

