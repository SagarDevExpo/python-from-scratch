# Day 1: What Are Data Structures and Algorithms?

**Time:** ~30 minutes

Today you learn:
1. What a data structure is
2. What an algorithm is
3. How to break a problem into input, process, and output
4. How to begin with a simple solution

**Practice file:** Create `day1_practice.py`

---

## Part 1: Data Structures

A **data structure** is a way to organize data.

You already use several:

| Python structure | Good for |
|---|---|
| List | Ordered values |
| Dictionary | Looking up a value by key |
| Set | Unique values and fast membership checks |
| Tuple | Ordered values that should not change |

The best structure depends on what the program must do.

```python
shopping = ["milk", "rice", "eggs"]
prices = {"milk": 4, "rice": 10}
visited = {"home", "store"}
location = (40.7, -74.0)
```

---

## Part 2: Algorithms

An **algorithm** is a sequence of steps used to solve a problem.

Example problem: find the largest number in a list.

```python
def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


print(find_largest([4, 9, 2, 7]))  # 9
```

The list is the data structure. The loop and comparison form the algorithm.

---

## Part 3: Input, Process, Output

Before coding, write down:

```text
Input:   a list of numbers
Process: compare every number with the largest seen
Output:  the largest number
```

Example:

```python
def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1

    return count
```

---

## Part 4: Start Simple

Do not search for the cleverest solution first.

Problem: Does a list contain duplicates?

```python
def contains_duplicate(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True
    return False
```

This is not the fastest solution, but it is understandable and correct.
Later you will improve it with a set.

---

## Exercises

**Exercise 1:** Write `find_smallest(numbers)` without using `min()`.

**Exercise 2:** Write `count_positive(numbers)`.

**Exercise 3:** Write `find_word(words, target)` returning its index or `-1`.

**Exercise 4:** For each exercise, write its input, process, and output in comments.

