# Day 1: Exceptions — Handling Errors Gracefully

**Time:** ~35 minutes

Today you learn:
1. What exceptions are
2. `try` and `except`
3. `else` and `finally`
4. Safer user input

**Practice file:** Create `day1_practice.py`

---

## Part 1: What Is an Exception?

An exception is Python saying, “Something went wrong while running.”

```python
age = int("hello")  # ValueError
```

The code is valid Python, but the value cannot be converted to an integer.

---

## Part 2: try and except

Use `try` around code that might fail.

```python
try:
    age = int(input("Age: "))
    print("Next year:", age + 1)
except ValueError:
    print("Please enter a number.")
```

Only catch the error you expect. Catching everything can hide bugs.

---

## Part 3: else

`else` runs only if no exception happened.

```python
try:
    number = int(input("Number: "))
except ValueError:
    print("Invalid number")
else:
    print("Square:", number * number)
```

---

## Part 4: finally

`finally` runs no matter what.

```python
try:
    x = int(input("x: "))
except ValueError:
    print("Bad input")
finally:
    print("This always runs")
```

You will not use `finally` every day, but it is useful for cleanup.

### 🔀 The whole flow in one picture

Think of `try` as "attempt this risky thing." What runs next depends on whether it blew up:

```
        try: (attempt the risky code)
           │
     ┌─────┴─────┐
     ▼           ▼
  it WORKED   it FAILED
     │           │
   else:      except:
  (bonus)    (rescue plan)
     │           │
     └────┬────┘
          ▼
      finally:  (always runs, success OR failure)
```

Walk it twice with `int(input(...))`:

**If you type `5` (success):**
1. `try` runs, `int("5")` works → no error.
2. `except` is **skipped** (nothing went wrong).
3. `else` runs (the "only if it worked" block).
4. `finally` runs.

**If you type `hello` (failure):**
1. `try` starts, `int("hello")` **crashes** with `ValueError`.
2. Python jumps *straight* to `except ValueError` — the rest of the `try` block is abandoned.
3. `else` is **skipped** (it only runs on success).
4. `finally` runs.

So: `except` = failure path, `else` = success path, `finally` = both paths.

---

## Part 5: Keep Asking Until Valid

```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


age = get_int("Age: ")
print("You entered:", age)
```

### 🔁 Why `while True` here isn't an infinite loop

It *looks* like it loops forever, but the `return` is the escape hatch. Trace a user who fumbles then succeeds:

| Attempt | User types | `int(...)` result | What happens |
|---------|-----------|--------------------|--------------|
| 1       | `abc`     | crashes → ValueError | `except` prints the warning, loop repeats |
| 2       | `-`       | crashes → ValueError | `except` prints the warning, loop repeats |
| 3       | `30`      | works → `30`        | `return 30` fires 🛑 loop ends, function hands back 30 |

The loop keeps spinning **only while input is bad**. The moment `int()` succeeds, `return` ends the function entirely (remember: `return` = emergency exit). This "loop until valid, then return" is the standard way to bulletproof user input.

---

## Exercises

**Exercise 1:** Ask for two numbers and divide them. Handle invalid numbers and division by zero.

**Exercise 2:** Write `get_float(prompt)` that keeps asking until the user enters a valid decimal.

**Exercise 3:** Ask for a list index and print that item. Handle invalid index and invalid number.

**Exercise 4:** In comments, explain the difference between `except` and `else`.

