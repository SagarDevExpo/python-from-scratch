# Day 1: Type Hints and Docstrings

**Time:** ~35 minutes

Today you learn:
1. Type hints
2. Function return hints
3. Docstrings
4. Why readable code matters

**Practice file:** Create `day1_practice.py`

---

## Part 1: Type Hints

Type hints describe what kind of values a function expects.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

Python does not force these at runtime, but they help readers and tools.

---

## Part 2: Common Hints

```python
def add(a: int, b: int) -> int:
    return a + b


def average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)


def get_scores() -> dict[str, int]:
    return {"Ana": 90, "Ben": 85}
```

---

## Part 3: Optional Values

```python
def find_user(users: list[str], target: str) -> str | None:
    for user in users:
        if user == target:
            return user
    return None
```

`str | None` means the function returns a string or `None`.

---

## Part 4: Docstrings

```python
def is_even(n: int) -> bool:
    """Return True if n is even, otherwise False."""
    return n % 2 == 0
```

A docstring explains what the function does, not every tiny step.

---

## Exercises

**Exercise 1:** Add type hints and docstrings to three old functions.

**Exercise 2:** Write `count_words(text: str) -> dict[str, int]`.

**Exercise 3:** Write `first_even(numbers: list[int]) -> int | None`.

**Exercise 4:** Explain in comments why type hints are useful.

