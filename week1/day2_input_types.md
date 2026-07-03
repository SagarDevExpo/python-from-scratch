# Day 2: input() and Type Conversion

**Time:** ~30 minutes

Today you learn:
1. How to get input from the user
2. How to convert between types (string ↔ number)
3. f-strings (the cleanest way to format output)

**Practice file:** Create `day2_practice.py` and type everything yourself.

---

## Part 1: input() — Get data from the user

`input()` pauses the program and waits for the user to type something.
It **ALWAYS returns a STRING** (text), even if they type a number.

```python
name = input("What is your name? ")
print("Hello,", name)

# IMPORTANT: input() ALWAYS gives you a string!
age_text = input("How old are you? ")
print(type(age_text))  # <class 'str'> — it's a STRING, not a number!

# This means you CAN'T do math with it directly:
# next_year = age_text + 1  # ERROR! Can't add string + number
```

---

## Part 2: Type conversion — Changing types

```python
# Convert string to integer: int()
age_text = "25"
age = int(age_text)        # "25" becomes 25
next_year = age + 1
print("Next year you'll be", next_year)

# Convert string to float: float()
price_text = "19.99"
price = float(price_text)  # "19.99" becomes 19.99
tax = price * 0.08
print("Tax:", tax)

# Convert number to string: str()
count = 42
message = "The answer is " + str(count)
print(message)

# Common pattern: input → convert → use
height = float(input("Your height in meters? "))
print("Double your height:", height * 2)
```

---

## Part 3: f-strings — The BEST way to format text

Instead of clunky string concatenation, use **f-strings**.
Put `f` before the quote, then use `{variable}` inside.

```python
name = "Sagar"
age = 25
city = "Austin"

# OLD way (messy):
print("My name is " + name + " and I am " + str(age) + " years old")

# NEW way (f-string — clean!):
print(f"My name is {name} and I am {age} years old")
print(f"I live in {city}")

# You can put any expression inside {}
a = 5
b = 3
print(f"{a} + {b} = {a + b}")   # 5 + 3 = 8
print(f"{a} x {b} = {a * b}")   # 5 x 3 = 15

# Format decimals
pi = 3.14159
print(f"Pi is approximately {pi:.2f}")  # Pi is approximately 3.14
# :.2f means "2 decimal places, float format"
```

---

## Part 4: Common type errors and how to fix them

```python
# ERROR 1: Adding string + number
# print("Score: " + 100)  # TypeError!
# FIX:
print("Score: " + str(100))  # or better:
print(f"Score: {100}")

# ERROR 2: Doing math with string input
# age = input("Age: ")
# print(age + 1)  # TypeError!
# FIX:
age = int(input("Age: "))
print(age + 1)

# ERROR 3: Converting non-numeric string to int
# num = int("hello")  # ValueError!
# Only convert strings that actually contain numbers
```

Safe pattern:

```python
user_input = input("Enter a number: ")
if user_input.isdigit():
    number = int(user_input)
    print(f"Your number doubled: {number * 2}")
else:
    print("That's not a valid number!")
```

---

## Part 5: Useful string operations (preview)

```python
text = "Hello, World"

print(len(text))        # 12 (length — counts characters)
print(text.upper())     # HELLO, WORLD
print(text.lower())     # hello, world
print(text.strip())     # Removes extra spaces from edges

# Check what's in a string
print("Hello" in text)  # True
print("xyz" in text)    # False
```

---

## Exercises

**Exercise 1:** Ask the user for their name and birth year.
Calculate their age and print: `Hello {name}, you are {age} years old!`
Hint: current year - birth year = age

**Exercise 2:** Ask for the price of an item and the quantity.
Print the total cost.
Example: price=9.99, quantity=3 → `Total: $29.97`
Use an f-string with `:.2f` to show exactly 2 decimal places.

**Exercise 3:** Ask the user for a temperature in Fahrenheit.
Convert to Celsius: `C = (F - 32) × 5/9`
Print: `{F}°F is {C}°C`

**Exercise 4:** Ask for the user's first name and last name separately.
Print their full name in ALL CAPS and also in all lowercase.
