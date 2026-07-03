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

---

## Exercises

**Exercise 1:** Create `strings.py` with `is_palindrome(text)` and test it.

**Exercise 2:** Create `numbers.py` with `average(nums)` and test empty list behavior.

**Exercise 3:** Write one test for normal input, one for edge input, one for error input.

**Exercise 4:** Break a function on purpose and watch pytest catch it.

