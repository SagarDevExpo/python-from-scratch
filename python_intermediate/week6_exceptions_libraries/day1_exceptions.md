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

---

## Exercises

**Exercise 1:** Ask for two numbers and divide them. Handle invalid numbers and division by zero.

**Exercise 2:** Write `get_float(prompt)` that keeps asking until the user enters a valid decimal.

**Exercise 3:** Ask for a list index and print that item. Handle invalid index and invalid number.

**Exercise 4:** In comments, explain the difference between `except` and `else`.

