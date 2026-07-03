# Day 5: Week 6 Practice — Safer Programs

**Time:** ~45 minutes

**Practice file:** Create `day5_practice.py`

---

## Challenge 1: Safe Calculator

Ask the user for two numbers and an operation: `+`, `-`, `*`, `/`.

Handle:

- invalid numbers
- invalid operation
- division by zero

## Challenge 2: Password Validator

Write `validate_password(password)` that raises `ValueError` if:

- length is less than 8
- no digit exists
- no uppercase letter exists

Catch the error and print a helpful message.

## Challenge 3: Random Quiz

Use `random.choice()` to pick questions from a list of dictionaries.

```python
questions = [
    {"question": "2 + 2?", "answer": "4"},
    {"question": "Python file extension?", "answer": ".py"},
]
```

## Challenge 4: Command-Line Greeter

Accept a name from the command line.

```bash
python3 greet.py Sagar
```

## Challenge 5: JSON Profile

Create a dictionary for your profile and print it as formatted JSON.

