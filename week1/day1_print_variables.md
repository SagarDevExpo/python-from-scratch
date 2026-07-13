# Day 1: print() and Variables

**Time:** ~30 minutes

Today you learn two things:
1. How to make Python show text on screen (`print`)
2. How to store values (`variables`)

**How to practice:**
- Read each section below
- Open `day1_practice.py` (create it yourself!)
- Type the code **from memory** — don't copy-paste
- Run it: `python3 day1_practice.py`
- Do the exercises at the bottom

---

## Part 1: print() — Show things on screen

`print()` displays whatever you put inside the parentheses.

```python
print("Hello, World!")
print("My name is Sagar")
```

You can print numbers too:

```python
print(42)
print(3.14)
```

You can print multiple things separated by commas:

```python
print("I am", 25, "years old")
# Output: I am 25 years old
# (Python adds spaces between them automatically)
```

---

## Part 2: Variables — Store values with a name

A variable is like a labeled box. You put a value in it.
Use `=` to assign a value to a variable name.

```python
name = "Sagar"
age = 25
city = "Austin"

# Now you can use the variable name instead of the value
print(name)    # prints: Sagar
print(age)     # prints: 25

# You can use variables inside print with commas
print("Hello, my name is", name)
print("I live in", city)

# You can change a variable's value at any time
age = 26
print("Next year I'll be", age)
```

### 📦 The labeled-box model

Picture a variable as a **labeled box**. `=` means *"put this value in the box with this label."*

```python
name = "Sagar"   # box labeled `name` now holds "Sagar"
age = 25         # box labeled `age`  now holds 25
```

When you **reassign**, the old value is thrown out and replaced. Trace this:

| Line | What happens | `age` now holds |
|------|--------------|------------------|
| `age = 25` | put 25 in the box | 25 |
| `age = 26` | replace with 26 (25 is gone) | 26 |

So `=` is **not** "equals" like in math — it's an *action*: "store this now." Read `age = 26` as *"make age hold 26,"* not *"age equals 26."* Always ask: **what does this variable hold at THIS exact line?**

---

## Part 3: Variable naming rules

```python
# GOOD variable names:
first_name = "Sagar"     # Use underscores for spaces
user_age = 25            # Descriptive names
total_count = 100        # Tells you what it stores

# BAD (these will ERROR):
# 2fast = "error"        # Can't start with a number
# my-name = "error"      # Can't use hyphens
# my name = "error"      # Can't have spaces
```

Names are **CASE SENSITIVE**:

```python
Name = "Alice"
name = "Bob"
print(Name)  # Alice
print(name)  # Bob — these are DIFFERENT variables
```

---

## Part 4: Types of values

Python has different types of values:

```python
# String (str) — text, always in quotes
greeting = "Hello"
message = 'Single quotes work too'

# Integer (int) — whole numbers
count = 42
temperature = -5

# Float — decimal numbers
price = 19.99
pi = 3.14159

# Boolean (bool) — True or False (capital T and F!)
is_sunny = True
is_raining = False
```

You can check the type of any value:

```python
print(type(greeting))     # <class 'str'>
print(type(count))        # <class 'int'>
print(type(price))        # <class 'float'>
print(type(is_sunny))     # <class 'bool'>
```

---

## Part 5: Basic math with numbers

```python
a = 10
b = 3

print(a + b)    # 13  (addition)
print(a - b)    # 7   (subtraction)
print(a * b)    # 30  (multiplication)
print(a / b)    # 3.333... (division — always gives a float!)
print(a // b)   # 3   (integer division — removes the decimal)
print(a % b)    # 1   (modulo — remainder after division)
print(a ** b)   # 1000 (exponent — 10 to the power of 3)

# You can store results in variables
total = a + b
print("Total:", total)  # Total: 13
```

---

## Part 6: Combining strings (concatenation)

```python
first = "Sagar"
last = "Nagireddi"

# Join strings with +
full_name = first + " " + last
print(full_name)  # Sagar Nagireddi

# You CANNOT add a string and a number directly:
# print("Age: " + 25)  # ERROR!

# Fix: convert number to string with str()
age = 25
print("Age: " + str(age))  # Age: 25

# OR just use commas in print (easier):
print("Age:", age)  # Age: 25
```

---

## Exercises — Do these in your `day1_practice.py`!

**Exercise 1:** Create variables for your name, age, and favorite food.
Print a sentence using all three.
Expected output: `My name is ___, I am ___ years old, and I love ___`

**Exercise 2:** Calculate and print:
- The number of hours in a week (7 days × 24 hours)
- The number of minutes in a year (365 × 24 × 60)

Store each in a variable first, then print.

**Exercise 3:** Create two variables with decimal numbers.
Print their sum, difference, product, and division result.

**Exercise 4:** What does this print? Predict FIRST, then run it.

```python
x = 5
y = x
x = 10
print(y)
```

*(Hint: does y change when x changes?)*
