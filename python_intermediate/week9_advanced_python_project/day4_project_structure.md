# Day 4: Project Structure

**Time:** ~40 minutes

Today you learn:
1. Splitting code into files
2. `main()`
3. Keeping logic testable
4. A small project layout

**Practice folder:** Create `mini_project/`

---

## Part 1: Simple Layout

```text
mini_project/
├── app.py
├── helpers.py
└── test_helpers.py
```

- `app.py` runs the program
- `helpers.py` stores reusable functions
- `test_helpers.py` stores tests

---

## Part 2: helpers.py

```python
def normalize_name(name: str) -> str:
    """Return name cleaned and title-cased."""
    return name.strip().title()
```

---

## Part 3: app.py

```python
from helpers import normalize_name


def main():
    name = input("Name: ")
    print(normalize_name(name))


if __name__ == "__main__":
    main()
```

---

## Part 4: test_helpers.py

```python
from helpers import normalize_name


def test_normalize_name():
    assert normalize_name("  sagar ") == "Sagar"
```

---

## Part 5: Keep Boundaries Clean

Good habit:

- input and print in `app.py`
- logic in functions
- tests for logic

This makes your projects easier to grow.

---

## Exercises

**Exercise 1:** Create the `mini_project/` structure.

**Exercise 2:** Add `is_valid_email(email)` to `helpers.py`.

**Exercise 3:** Test `is_valid_email()`.

**Exercise 4:** Use it from `app.py`.

