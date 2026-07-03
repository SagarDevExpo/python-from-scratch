# Day 3: Libraries, Imports, and Modules

**Time:** ~40 minutes

Today you learn:
1. `import`
2. `from ... import ...`
3. Standard-library modules
4. Writing your own module

**Practice file:** Create `day3_practice.py`

---

## Part 1: import

A library is code someone already wrote so you can reuse it.

```python
import random

number = random.randint(1, 10)
print(number)
```

Here, `random` is the module and `randint` is a function inside it.

---

## Part 2: from import

```python
from random import choice

names = ["Ana", "Ben", "Cara"]
print(choice(names))
```

Use regular `import module` when you want the code to clearly show where a
function came from.

---

## Part 3: Useful Standard Libraries

```python
import math
import statistics
import datetime

print(math.sqrt(25))
print(statistics.mean([10, 20, 30]))
print(datetime.date.today())
```

The standard library comes with Python.

---

## Part 4: Create Your Own Module

Create `helpers.py`:

```python
def shout(text):
    return text.upper() + "!"
```

Create `day3_practice.py`:

```python
import helpers

print(helpers.shout("hello"))
```

Files in the same folder can import each other.

---

## Part 5: __name__

```python
def main():
    print("Running directly")


if __name__ == "__main__":
    main()
```

This means: run `main()` only when this file is executed directly, not when it
is imported.

---

## Exercises

**Exercise 1:** Use `random.choice()` to pick a random food from a list.

**Exercise 2:** Use `statistics.mean()` to calculate average score.

**Exercise 3:** Create `helpers.py` with `is_even(n)` and import it.

**Exercise 4:** Add a `main()` function and `if __name__ == "__main__"` block.

