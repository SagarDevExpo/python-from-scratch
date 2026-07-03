# Day 3: if / elif / else — Making Decisions

**Time:** ~30 minutes

Today you learn:
1. How to make your program choose between options
2. Comparison operators (`>`, `<`, `==`, etc.)
3. `if` / `elif` / `else` structure

**Practice file:** Create `day3_practice.py`

---

## Part 1: Comparison operators — True or False?

These **compare** two values and give you `True` or `False`:

```python
a = 10
b = 5

print(a > b)     # True   (greater than)
print(a < b)     # False  (less than)
print(a >= 10)   # True   (greater than or equal)
print(a <= 9)    # False  (less than or equal)
print(a == 10)   # True   (equal to — use TWO equals signs!)
print(a != b)    # True   (not equal to)
```

> **COMMON MISTAKE:**
> - `=` is **assignment** (put value in variable)
> - `==` is **comparison** (check if equal)
> - `x = 5` means "set x to 5"
> - `x == 5` means "is x equal to 5?"

---

## Part 2: if — Do something when a condition is True

```python
age = 20

if age >= 18:
    print("You are an adult")
    print("You can vote")
```

**IMPORTANT:** The indented lines (4 spaces) are the "body".
They ONLY run if the condition is True.
Python uses **indentation** to know what's inside the if block.

```python
temperature = 35

if temperature > 30:
    print("It's hot outside!")  # This runs (35 > 30 is True)

if temperature > 40:
    print("It's extremely hot!")  # This does NOT run (35 > 40 is False)
```

---

## Part 3: if / else — Two choices

```python
age = 15

if age >= 18:
    print("You can drive")
else:
    print("You're too young to drive")
```

One of these **ALWAYS** runs — never both, never neither.

```python
number = 7

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

---

## Part 4: if / elif / else — Multiple choices

`elif` means "else if" — check another condition:

```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")    # This one runs (75 >= 70)
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

Python checks **top to bottom** and **STOPS** at the first True condition.
Even though 75 >= 60 is also True, it already matched 75 >= 70.

> **ORDER MATTERS:** If you put `score >= 60` first, it would match and skip the rest!

---

## Part 5: Nested if (if inside if)

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive!")
    else:
        print("You're old enough but need a license")
else:
    print("You're too young to drive")
```

---

## Part 6: Combining conditions with and / or / not

```python
age = 25
has_ticket = True

# and — BOTH must be True
if age >= 18 and has_ticket:
    print("You can enter the concert")

# or — AT LEAST ONE must be True
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

# not — flips True to False and vice versa
is_raining = False
if not is_raining:
    print("No umbrella needed")

# You can combine them:
temperature = 25
is_sunny = True
if temperature > 20 and is_sunny and not is_raining:
    print("Perfect day for a walk!")
```

---

## Part 7: Common patterns

```python
# Check if a number is in a range
age = 25
if 18 <= age <= 65:
    print("Working age")

# Check if a string is empty
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Name is empty!")
# Empty string is "falsy" in Python — treated as False

# Check if something is in a list/string
vowels = "aeiou"
letter = "e"
if letter in vowels:
    print(f"{letter} is a vowel")
```

---

## Exercises

**Exercise 1:** Ask the user for a number. Print whether it's
positive, negative, or zero.

**Exercise 2:** Ask for the user's age. Print which category:
- 0-12: `"Child"`
- 13-17: `"Teenager"`
- 18-64: `"Adult"`
- 65+: `"Senior"`

**Exercise 3:** Ask for a year. Determine if it's a leap year.
Rules: Divisible by 4 BUT not by 100, UNLESS also divisible by 400.
- 2000 → leap year (divisible by 400)
- 1900 → NOT a leap year (divisible by 100 but not 400)
- 2024 → leap year (divisible by 4, not by 100)

Hint: Use `%` (modulo) and `and`/`or`

**Exercise 4:** Simple calculator. Ask for two numbers and an operator
(`+`, `-`, `*`, `/`). Print the result. Handle division by zero!
