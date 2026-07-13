# Day 4: More Comparisons and Logic

**Time:** ~30 minutes

Today you learn:
1. Truthy and falsy values
2. Ternary expressions (one-line if/else)
3. match/case (Python's switch statement)
4. Common logical patterns

**Practice file:** Create `day4_practice.py`

---

## Part 1: Truthy and Falsy — What counts as True/False?

In Python, some values are **"falsy"** (treated as False):
- `False`
- `0` (zero)
- `""` (empty string)
- `[]` (empty list)
- `None` (represents "nothing")

Everything else is **"truthy"** (treated as True):
- `True`
- Any non-zero number (1, -5, 3.14)
- Any non-empty string ("hello", " ")
- Any non-empty list ([1, 2])

```python
name = "Sagar"
if name:  # Same as: if name != ""
    print(f"Hello, {name}")

count = 0
if not count:  # Same as: if count == 0
    print("Count is zero")

items = []
if not items:  # Same as: if len(items) == 0
    print("List is empty")
```

---

## Part 2: Ternary expression — One-line if/else

```python
# Regular if/else:
age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Same thing in ONE line (ternary):
status = "adult" if age >= 18 else "minor"
print(status)
```

### 🧩 How to read a ternary out loud

A ternary is just an if/else folded onto one line. Read it in this order:

```
status = "adult"  if age >= 18  else "minor"
         │          │              │
         │          │              └─ value if the test is False
         │          └─ the test (the question)
         └─ value if the test is True
```

Say it as: *"status becomes 'adult' **if** age >= 18, **otherwise** 'minor'."* The **middle** is the question; the value **before** `if` is used when it's True; the value **after** `else` when it's False. It picks exactly one and stores it.

```python
# More examples:
x = 10
result = "even" if x % 2 == 0 else "odd"
print(f"{x} is {result}")

temperature = 35
feeling = "hot" if temperature > 30 else "comfortable"
print(f"It's {feeling}")
```

Don't overuse this — if it's complicated, use regular if/else.

---

## Part 3: match/case — Clean multiple choice (Python 3.10+)

Instead of many if/elif, you can use match/case:

```python
command = "start"

match command:
    case "start":
        print("Starting the server...")
    case "stop":
        print("Stopping the server...")
    case "restart":
        print("Restarting...")
    case _:                          # _ means "anything else" (default)
        print(f"Unknown command: {command}")
```

```python
http_status = 404

match http_status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print(f"Status: {http_status}")
```

---

## Part 4: Common logic patterns you'll use in DSA

```python
# PATTERN 1: Find the maximum of two numbers
a = 15
b = 23
maximum = a if a > b else b
print(f"Max of {a} and {b} is {maximum}")

# Or use the built-in:
print(f"Max: {max(a, b)}")
print(f"Min: {min(a, b)}")

# PATTERN 2: Clamp a value to a range
value = 150
clamped = max(0, min(100, value))  # Keep between 0 and 100
print(f"{value} clamped to 0-100: {clamped}")  # 100

# PATTERN 3: Toggle a boolean
flag = True
flag = not flag
print(f"Flag is now: {flag}")  # False

# PATTERN 4: Check if a number is in a range
x = 5
if 1 <= x <= 10:
    print(f"{x} is between 1 and 10")

# PATTERN 5: Check character type
char = "A"
print(f"'{char}' is a letter: {char.isalpha()}")
print(f"'{char}' is a digit: {char.isdigit()}")
print(f"'{char}' is uppercase: {char.isupper()}")
print(f"'{char}' is lowercase: {char.islower()}")
```

---

## Part 5: None — Representing "nothing"

```python
result = None

if result is None:
    print("No result yet")

# Use `is` (not ==) to check for None
# For None, always use `is None` or `is not None`

result = 42
if result is not None:
    print(f"Got a result: {result}")
```

---

## Exercises

**Exercise 1:** Write a one-line ternary that checks if a number
is divisible by 3. Store `"fizz"` or `"not fizz"` in a variable.

**Exercise 2:** Use match/case to print the day type:
- "Monday" through "Friday" → `"Weekday"`
- "Saturday" or "Sunday" → `"Weekend"`
- Anything else → `"Invalid day"`

Hint: You can use `case "Saturday" | "Sunday":` for multiple matches

**Exercise 3:** Given three numbers a, b, c — find and print the largest
**WITHOUT** using the `max()` function. Use only if/elif/else.

**Exercise 4:** Write a program that asks for a username and password.
- If username is empty → print `"Username required"`
- If password is less than 8 characters → print `"Password too short"`
- If both are valid → print `"Login successful"`

Use truthy/falsy checks where possible.
