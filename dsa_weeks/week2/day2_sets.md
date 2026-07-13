# Day 2: Sets — Unique Values and Fast Membership

**Time:** ~30 minutes

Today you learn:
1. What sets store
2. How sets remove duplicates
3. How to track previously seen values

**Practice file:** Create `day2_practice.py`

---

## Part 1: Set Basics

A set stores unique values without indexes.

```python
numbers = {2, 4, 4, 6}
print(numbers)  # {2, 4, 6}

numbers.add(8)
numbers.remove(2)
print(6 in numbers)  # True
```

Average membership checking is `O(1)`.

---

## Part 2: Contains Duplicate

```python
def contains_duplicate(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True
        seen.add(number)

    return False
```

The earlier nested-loop version used `O(n²)` time.
This version uses `O(n)` time and `O(n)` extra space.

---

## Part 3: Keep Original Order

Converting directly to a set can lose order. Track seen values while building
a result:

```python
def remove_duplicates(items):
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result
```

---

## Part 4: Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)  # intersection: {3}
print(a | b)  # union: {1, 2, 3, 4, 5}
print(a - b)  # difference: {1, 2}
```

---

## Exercises

1. Find common values in two lists.
2. Return the first repeated value.
3. Check whether every character in a word is unique.
4. Remove duplicates while preserving order.

