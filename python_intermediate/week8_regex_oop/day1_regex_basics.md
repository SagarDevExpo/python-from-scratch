# Day 1: Regular Expressions — Pattern Matching

**Time:** ~40 minutes

Today you learn:
1. Why regex exists
2. `re.search`
3. Common pattern symbols
4. Validating input

**Practice file:** Create `day1_practice.py`

---

## Part 1: Why Regex?

Regular expressions help find patterns in text.

Without regex, checking an email or phone number takes many string checks.
With regex, you describe the pattern once.

---

## Part 2: re.search

```python
import re

email = input("Email: ")

if re.search("@", email):
    print("Has @")
else:
    print("Missing @")
```

This is simple, but not strict yet.

---

## Part 3: Useful Symbols

| Symbol | Meaning |
|---|---|
| `.` | any character |
| `.*` | zero or more characters |
| `.+` | one or more characters |
| `^` | start of string |
| `$` | end of string |
| `\d` | digit |
| `\w` | letter, number, or underscore |

---

## Part 4: Validate Email Shape

```python
import re

email = input("Email: ")

if re.search(r"^.+@.+\.com$", email):
    print("Valid enough for now")
else:
    print("Invalid")
```

The `r` before the string means raw string. Use raw strings for regex.

---

## Part 5: Character Sets

```python
import re

plate = "ABC123"

if re.search(r"^[A-Z]+[0-9]+$", plate):
    print("Letters followed by numbers")
```

`[A-Z]` means any uppercase letter. `[0-9]` means any digit.

---

## Exercises

**Exercise 1:** Check whether a string contains any digit.

**Exercise 2:** Validate a simple ZIP code: exactly 5 digits.

**Exercise 3:** Validate a username containing only letters, numbers, and underscores.

**Exercise 4:** Explain what `^` and `$` do.

