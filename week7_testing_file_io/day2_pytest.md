# Day 2: pytest — Testing Like a Real Project

**Time:** ~40 minutes

Today you learn:
1. Test files
2. `pytest`
3. Multiple test functions
4. Testing exceptions

**Practice file:** Create `calculator.py` and `test_calculator.py`

---

## Part 1: Code File

Create `calculator.py`:

```python
def square(n):
    return n * n


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
```

---

## Part 2: Test File

Create `test_calculator.py`:

```python
from calculator import square, divide


def test_square_positive():
    assert square(3) == 9


def test_square_negative():
    assert square(-4) == 16
```

Run:

```bash
pytest test_calculator.py
```

---

## Part 3: Test Names Matter

Pytest finds:

- files named `test_*.py`
- functions named `test_*`

That naming is the convention.

---

## Part 4: Testing Exceptions

```python
import pytest
from calculator import divide


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

This test passes only if `divide(10, 0)` raises `ValueError`.

### 🧩 Why the logic feels "backwards"

Normally an error crashing your code is *bad*. But here, the error is the **expected, correct** result — we're testing that `divide` properly *refuses* to divide by zero.

`with pytest.raises(ValueError):` sets a trap that says: *"I expect the code inside this block to blow up with a `ValueError`."*

- If `divide(10, 0)` **does** raise `ValueError` → ✅ test **passes** (the trap caught what it expected).
- If `divide(10, 0)` runs without error, or raises a *different* error → ❌ test **fails** (the trap was disappointed).

So you're not testing that the code works — you're testing that it *breaks correctly* when given bad input.

---

## Exercises

**Exercise 1:** Create `strings.py` with `is_palindrome(text)` and test it.

**Exercise 2:** Create `numbers.py` with `average(nums)` and test empty list behavior.

**Exercise 3:** Write one test for normal input, one for edge input, one for error input.

**Exercise 4:** Break a function on purpose and watch pytest catch it.

