# Day 2: for Loops and range() — The Loop You'll Use Most

**Time:** ~30 minutes

Today you learn:
1. `for` loops — iterate over sequences
2. `range()` — generate number sequences
3. `enumerate()` — loop with index AND value
4. Nested loops

**Practice file:** Create `day2_practice.py`

---

## Part 1: for loop — Iterate over anything

A for loop goes through each item in a sequence, one at a time:

```python
# Loop through a string
for char in "hello":
    print(char)
# h, e, l, l, o

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
```

The variable name (`char`, `fruit`) is YOUR choice — pick something meaningful.

---

## Part 2: range() — Generate numbers

```python
# range(stop) → 0, 1, 2, ..., stop-1
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4

# range(start, stop)
for i in range(3, 8):
    print(i, end=" ")  # 3 4 5 6 7

# range(start, stop, step)
for i in range(0, 20, 5):
    print(i, end=" ")  # 0 5 10 15

# Count DOWN with negative step
for i in range(10, 0, -1):
    print(i, end=" ")  # 10 9 8 7 6 5 4 3 2 1

# Do something n times (ignore the variable with _)
for _ in range(3):
    print("Hello!")
```

### 🧩 The #1 range() gotcha: stop is NOT included

`range` **stops one short** of the number you give it. `range(5)` gives you five numbers starting at 0 — `0, 1, 2, 3, 4` — but **not 5**. Think of it as *"go up to, but don't touch, the stop number."*

| Call | Produces | Note |
|------|----------|------|
| `range(5)` | `0 1 2 3 4` | starts at 0, stops before 5 |
| `range(3, 8)` | `3 4 5 6 7` | starts at 3, stops before 8 |
| `range(0, 20, 5)` | `0 5 10 15` | step of 5, stops before 20 |
| `range(10, 0, -1)` | `10 9 8 ... 1` | negative step counts down |

So `range(5)` runs the loop **5 times** (count them: 0,1,2,3,4). This "stops before" rule trips up everyone at first — when a loop misses its last number, this is usually why.

---

## Part 3: for vs while — When to use which?

- **Use `for`** when you know how many times to loop (looping through a list, doing something n times)
- **Use `while`** when you don't know when to stop (waiting for user input, searching)
- Most DSA problems use `for` loops

---

## Part 4: enumerate() — Get index AND value

```python
fruits = ["apple", "banana", "cherry"]

# WITHOUT enumerate (works but clunky):
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# WITH enumerate (clean!):
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Start index at 1:
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple, 2. banana, 3. cherry
```

### 🧩 What enumerate hands you (you'll use this constantly)

`enumerate` gives you **two things each loop**: the position `i` AND the value. It saves you from the clumsy `range(len(...))` dance.

Trace `for i, fruit in enumerate(["apple", "banana", "cherry"])`:

| Loop | `i` (position) | `fruit` (value) | prints |
|------|----------------|------------------|--------|
| 1 | 0 | `"apple"` | `0: apple` |
| 2 | 1 | `"banana"` | `1: banana` |
| 3 | 2 | `"cherry"` | `2: cherry` |

The two names get filled in *together* each round. This is the exact tool the DSA search pattern uses (`for i, num in enumerate(nums)`) — when you need *both* "where am I" and "what's here," reach for `enumerate`.

---

## Part 5: Nested loops — A loop inside a loop

The inner loop runs **COMPLETELY** for each iteration of the outer loop:

```python
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()  # New line after each row
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)
```

Star triangle pattern:

```python
for row in range(1, 6):
    print("*" * row)
# *
# **
# ***
# ****
# *****
```

---

## Part 6: Useful loop patterns for DSA

```python
# PATTERN: Find something in a list
numbers = [4, 8, 15, 16, 23, 42]
target = 15
found = False
for num in numbers:
    if num == target:
        found = True
        break
print(f"Found {target}: {found}")

# PATTERN: Count occurrences
text = "mississippi"
count = 0
for char in text:
    if char == 's':
        count += 1
print(f"Number of 's': {count}")

# PATTERN: Build a new list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(f"Even numbers: {evens}")

# PATTERN: Sum with condition
total = 0
for num in numbers:
    if num > 5:
        total += num
print(f"Sum of numbers > 5: {total}")  # 6+7+8+9+10 = 40
```

---

## Exercises

**Exercise 1:** Print all numbers from 1 to 50 that are divisible by 7.

**Exercise 2:** Count how many vowels are in `"programming is fun"`. (Vowels: a, e, i, o, u)

**Exercise 3:** Print this pattern using nested loops:
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

**Exercise 4:** Given the list `[3, 7, 2, 9, 1, 5]`, find and print the largest number **WITHOUT** using the `max()` function.
Hint: Keep track of the biggest you've seen so far.

**Exercise 5: FizzBuzz** (classic interview warm-up!):
Print numbers 1-30, but:
- If divisible by 3, print `"Fizz"` instead
- If divisible by 5, print `"Buzz"` instead
- If divisible by both, print `"FizzBuzz"` instead
