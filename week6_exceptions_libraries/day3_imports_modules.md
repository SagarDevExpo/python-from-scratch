# Day 3: Libraries, Imports, and Modules

**Time:** ~40 minutes

Today you learn:
1. `import`
2. `from ... import ...`
3. Standard-library modules
4. Installing third-party libraries with `pip`
5. Writing your own module

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

## Part 4: Third-Party Libraries (pip)

The standard library is big, but not infinite. For everything else, other people have published libraries you can download and use. These are **third-party** libraries — they do **not** come with Python, so you must install them first with `pip` (Python's package installer).

```bash
# run this in your TERMINAL, not inside a .py file
pip install requests
```

Then import and use it like any other module:

```python
import requests   # only works AFTER pip install requests
```

### 🧩 Standard library vs third-party — the key difference

| | Standard library | Third-party |
|---|------------------|-------------|
| Examples | `math`, `random`, `json`, `datetime` | `requests`, `numpy`, `flask` |
| Comes with Python? | ✅ yes, already there | ❌ no |
| Need to install? | Never | **Yes**, once, via `pip install` |
| Then import? | `import math` | `import requests` |

Think of it like apps: the standard library is the software **pre-installed** on a new phone; third-party libraries are apps you **download from the store** (`pip`) before you can open them. If you `import` a third-party library without installing it first, Python raises `ModuleNotFoundError`.

**Where do they come from?** The public catalog is [PyPI](https://pypi.org) (the Python Package Index). `pip install <name>` fetches the package from there. Check what you've installed with `pip list`.

> ⚠️ Installing needs internet and touches your environment. If you're not ready to install anything yet, just read this part — you'll actually use `requests` in Day 4.

---

## Part 5: Create Your Own Module

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

## Part 6: __name__

```python
def main():
    print("Running directly")


if __name__ == "__main__":
    main()
```

This means: run `main()` only when this file is executed directly, not when it
is imported.

### 🧩 What is `__name__` really?

Every Python file secretly has a variable called `__name__` that Python fills in automatically. Its value depends on **how the file is being used**:

- If you **run the file directly** (`python day3_practice.py`), Python sets `__name__` to the special string `"__main__"`.
- If someone **imports your file** (`import day3_practice`), Python sets `__name__` to the file's name instead (`"day3_practice"`).

So the line `if __name__ == "__main__":` is really asking: *"Am I being run directly, or am I being imported by someone else?"*

| How the file is used | `__name__` equals | Does `main()` run? |
|----------------------|-------------------|---------------------|
| `python myfile.py` (run directly) | `"__main__"` | ✅ Yes |
| `import myfile` (imported elsewhere) | `"myfile"` | ❌ No |

**Why bother?** It lets a file do two jobs: be a runnable program *and* a reusable library. When imported, only its functions are borrowed — the demo/test code under the `if` block stays quiet. It's the standard "start here" marker in real Python programs.

---

## Exercises

**Exercise 1:** Use `random.choice()` to pick a random food from a list.

**Exercise 2:** Use `statistics.mean()` to calculate average score.

**Exercise 3:** Create `helpers.py` with `is_even(n)` and import it.

**Exercise 4:** Add a `main()` function and `if __name__ == "__main__"` block.

**Exercise 5:** Run `pip list` in your terminal and read the names. Then, in a comment, explain the difference between a standard-library module and a third-party one, giving one example of each.

