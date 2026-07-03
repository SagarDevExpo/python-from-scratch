# Day 2: Raising Exceptions and Debugging

**Time:** ~35 minutes

Today you learn:
1. `raise`
2. When to reject bad input
3. Reading tracebacks
4. Simple debugging habits

**Practice file:** Create `day2_practice.py`

---

## Part 1: Raising Your Own Error

Sometimes your function should refuse bad input.

```python
def calculate_age(year_born):
    if year_born < 1900:
        raise ValueError("year_born is too old")
    return 2026 - year_born
```

`raise` stops the function and creates an exception.

---

## Part 2: Validate Function Arguments

```python
def average(numbers):
    if len(numbers) == 0:
        raise ValueError("numbers cannot be empty")

    return sum(numbers) / len(numbers)
```

This is better than returning a fake answer.

---

## Part 3: Catching a Raised Error

```python
try:
    print(average([]))
except ValueError as error:
    print("Problem:", error)
```

`as error` stores the exception message.

---

## Part 4: Tracebacks

A traceback shows:

1. Which file failed
2. Which line failed
3. What kind of error happened

Read from the bottom first. The last line usually tells the main problem.

---

## Part 5: Debugging Habits

Use simple prints while learning:

```python
def total_even(numbers):
    total = 0
    for number in numbers:
        print("checking:", number)
        if number % 2 == 0:
            total += number
            print("new total:", total)
    return total
```

Remove debug prints once you understand the bug.

---

## Exercises

**Exercise 1:** Write `safe_sqrt(n)` that raises `ValueError` for negative numbers.

**Exercise 2:** Write `get_item(items, index)` that raises `IndexError` if the index is invalid.

**Exercise 3:** Intentionally create and read a `NameError`, `ValueError`, and `IndexError`.

**Exercise 4:** Add debug prints to a function that finds the largest number.

