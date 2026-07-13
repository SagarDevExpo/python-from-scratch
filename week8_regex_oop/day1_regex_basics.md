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

### 🧩 Reading the pattern `^.+@.+\.com$` piece by piece

A regex looks like line noise until you read it left-to-right as a checklist. Here's what each chunk demands for `sagar@gmail.com`:

| Piece | Means | Matches in `sagar@gmail.com` |
|-------|-------|-------------------------------|
| `^`   | start of the string | (the very beginning) |
| `.+`  | one or more of any character | `sagar` |
| `@`   | a literal `@` sign | `@` |
| `.+`  | one or more of any character | `gmail` |
| `\.`  | a literal dot (the `\` means "real dot, not any-char") | `.` |
| `com` | the literal letters c-o-m | `com` |
| `$`   | end of the string | (the very end) |

So the whole thing reads: *"from start to end: some stuff, then `@`, then some stuff, then `.com`."* If the text can be fully matched against that checklist, `re.search` returns a match; otherwise `None`.

**Two gotchas worth memorizing:**
- `^` and `$` are anchors — they don't match characters, they pin the pattern to the **start** and **end** so junk can't sneak in before or after.
- A plain `.` means "any character." To match a *real* dot you must escape it as `\.` — that's why the domain dot is `\.` but the earlier `.+` uses a wildcard dot.

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

