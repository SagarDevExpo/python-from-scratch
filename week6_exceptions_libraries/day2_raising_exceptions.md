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

### 🚨 `raise` vs `return` — two different exits

Both end the function, but they mean opposite things:

| | `return value` | `raise ValueError(...)` |
|---|----------------|--------------------------|
| Meaning | "Here's your answer." | "Stop — something is wrong." |
| Where it goes | back to the caller as a normal value | jumps to the nearest `except` (or crashes) |
| Feels like | handing over a finished result | pulling the fire alarm |

Trace `calculate_age(1850)`:
1. `year_born < 1900` → `1850 < 1900` is **True**.
2. `raise ValueError(...)` fires → the function stops **immediately**. The `return 2026 - year_born` line is never reached.
3. Control flies out to whoever called it, looking for a `try/except` to catch it.

Trace `calculate_age(1990)`:
1. `1990 < 1900` is **False** → skip the `raise`.
2. `return 2026 - 1990` → hands back `36` normally.

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

### 🔎 How to actually read one

Say you run code and get this:

```
Traceback (most recent call last):
  File "app.py", line 10, in <module>
    print(average([]))
  File "app.py", line 4, in average
    return sum(numbers) / len(numbers)
ValueError: numbers cannot be empty
```

Read it like a story, **bottom to top**:

1. **Last line first** → `ValueError: numbers cannot be empty`. This is *what* went wrong. Always start here.
2. **Next line up** → `line 4, in average` → the error happened *inside* the `average` function, at line 4.
3. **Line above that** → `line 10, in <module>` → that function was *called* from line 10 of your main code.

So the trail reads: "line 10 called `average`, which failed at line 4, because the list was empty." The middle lines are the **breadcrumb trail** of who-called-who; the bottom line is the actual crash.

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

