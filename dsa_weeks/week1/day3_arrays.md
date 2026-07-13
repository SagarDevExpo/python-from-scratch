# Day 3: Arrays and Python Lists

**Time:** ~35 minutes

Today you learn:
1. Why Python lists behave like dynamic arrays
2. The cost of common list operations
3. In-place changes versus new lists

**Practice file:** Create `day3_practice.py`

---

## Part 1: Fast Index Access

Python can directly access a list position.

```python
names = ["Ana", "Ben", "Cara", "Dev"]
print(names[2])  # Cara
```

Index access is `O(1)`.

---

## Part 2: Appending and Inserting

```python
numbers = [10, 20, 30]
numbers.append(40)      # usually O(1)
numbers.insert(0, 5)    # O(n)
```

Inserting at the beginning moves all existing values one position right.

Deleting from the beginning has the same issue:

```python
numbers.pop(0)  # O(n)
numbers.pop()   # O(1)
```

---

## Part 3: Search Is O(n)

```python
def find_index(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1
```

The target may be last or absent, so every value may be checked.

---

## Part 4: In Place Versus New List

An in-place algorithm changes the original list:

```python
numbers = [1, 2, 3]
numbers[0], numbers[2] = numbers[2], numbers[0]
print(numbers)  # [3, 2, 1]
```

Building a result uses extra memory:

```python
def only_even(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result
```

Neither choice is always better. Understand the trade-off.

---

## Part 5: Prefix Sums

A prefix sum stores the running total.

```python
numbers = [2, 4, 1, 3]
prefix = []
running_total = 0

for number in numbers:
    running_total += number
    prefix.append(running_total)

print(prefix)  # [2, 6, 7, 10]
```

This pattern helps answer repeated range-sum questions.

---

## Exercises

**Exercise 1:** Remove all negative numbers by building a new list.

**Exercise 2:** Reverse a list in place using `left` and `right` indexes.

**Exercise 3:** Build prefix sums for `[3, 1, 4, 2]`.

**Exercise 4:** Explain why `pop(0)` is slower than `pop()`.

