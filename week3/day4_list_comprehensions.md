# Day 4: List Comprehensions + Useful Tools

**Time:** ~30 minutes

Today you learn:
1. List comprehensions — build lists in one line
2. Dictionary and set comprehensions
3. Useful built-ins: `any()`, `all()`, `zip()`, `sorted()`
4. Lambda functions (tiny one-line functions)

**Practice file:** Create `day4_practice.py`

---

## Part 1: List Comprehension

```python
# REGULAR way:
squares = []
for i in range(6):
    squares.append(i ** 2)

# LIST COMPREHENSION way (same result, one line):
squares = [i ** 2 for i in range(6)]  # [0, 1, 4, 9, 16, 25]
```

**Syntax:** `[expression FOR variable IN iterable]`

### 🧩 How to READ it (this is the trick)

A comprehension is just a `for` loop folded into one line. Match the pieces:

```
squares = [   i ** 2      for i in range(6)   ]
              │──────│      │───────────│
              what to        the loop
              collect        (same as "for i in range(6):")
```

Read it out loud **right-to-left**: *"for each `i` in range(6), collect `i ** 2`."*

Same three moving parts as the long version:

| Long version                | Comprehension part |
|-----------------------------|--------------------|
| `for i in range(6):`        | `for i in range(6)` (at the end) |
| `i ** 2`                    | `i ** 2` (at the front) |
| `squares.append(...)`       | the `[ ]` brackets do the collecting automatically |

So the loop runs `i = 0, 1, 2, 3, 4, 5`, and each time it drops `i ** 2` into the new list → `[0, 1, 4, 9, 16, 25]`. Nothing new is happening — it's the loop you already know, just written compactly.

---

## Part 2: With condition (filter)

```python
# Only even numbers
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Only words longer than 3 letters
words = ["the", "quick", "brown", "fox"]
long = [w for w in words if len(w) > 3]  # ["quick", "brown"]
```

### 🧩 The `if` at the END is a bouncer

When `if` comes **after** the `for`, it's a **filter** — a bouncer at the door deciding who gets in.

```
evens = [  x   for x in range(10)   if x % 2 == 0  ]
           │                          │───────────│
           keep it        only if this is True (the bouncer)
```

Read it: *"for each `x` in range(10), IF `x` is even, keep `x`."* Numbers that fail the test are simply skipped — they never enter the list.

| `x` | `x % 2 == 0`? | in the list? |
|-----|---------------|--------------|
| 0   | Yes           | ✅ kept |
| 1   | No            | ❌ skipped |
| 2   | Yes           | ✅ kept |
| 3   | No            | ❌ skipped |
| ... | ...           | ... |

Result: `[0, 2, 4, 6, 8]`.

---

## Part 3: If-else in comprehension (transform)

> When using if-else, position changes! It goes **BEFORE** the `for`.

```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
# ["even", "odd", "even", "odd", "even", "odd"]

nums = [-3, -1, 0, 2, -5]
absolutes = [n if n >= 0 else -n for n in nums]  # [3, 1, 0, 2, 5]
```

### 🧩 `if` at the FRONT is a chooser, not a bouncer

This is the #1 confusion, so pin it down:

- **`if` at the END** = filter (decides *whether* to keep the item). Some items get dropped.
- **`if...else` at the FRONT** = transform (decides *what value* to put in). Every item stays, but it's changed.

```
labels = [  "even" if x % 2 == 0 else "odd"    for x in range(6)  ]
            │───────────── the value ──────────│    │── the loop ──│
            "if it's even use 'even', otherwise 'odd'"
```

Read it: *"for each `x`, put in 'even' if `x` is even, else put in 'odd'."* The list stays length 6 — nothing is filtered out, each number is just relabeled.

**Quick memory hook:**
- `[X for i in ... if COND]` → filter (if at the back = "back door bouncer")
- `[X if COND else Y for i in ...]` → choose (if at the front = "front-desk chooser")

---

## Part 4: Dictionary & Set Comprehension

```python
# Dict comprehension
squares = {x: x ** 2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Set comprehension
first_letters = {w[0] for w in ["apple", "avocado", "banana"]}
# {'a', 'b'}
```

---

## Part 5: Useful built-in functions

```python
nums = [3, 1, 4, 1, 5, 9]

# Basics
sum(nums)   # 23
min(nums)   # 1
max(nums)   # 9

# any() — True if ANY element is True
any(n < 0 for n in nums)       # False
any(n > 8 for n in nums)       # True

# all() — True if ALL elements are True
all(n > 0 for n in nums)       # True
all(n > 3 for n in nums)       # False

# zip() — pair up two lists
names = ["Alice", "Bob"]
scores = [85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Create dict from two lists
grade_book = dict(zip(names, scores))

# sorted() with key
words = ["banana", "pie", "apple"]
sorted(words, key=len)       # ["pie", "apple", "banana"]
sorted(words, key=len, reverse=True)  # longest first
```

---

## Part 6: Lambda — Tiny functions

```python
# Regular function:
def square(x):
    return x * x

# Lambda version:
square = lambda x: x * x

# Most useful with sorted():
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

# Sort by score
by_score = sorted(students, key=lambda s: s[1])
# [('Charlie', 78), ('Alice', 85), ('Bob', 92)]
```

---

## Exercises

**Exercise 1:** Using list comprehension, create:
- Cubes from 1 to 10: `[1, 8, 27, ..., 1000]`
- Strings: `["1!", "2!", "3!", ..., "10!"]`
- Numbers 1-100 divisible by both 3 AND 5

**Exercise 2:** Dict comprehension — map words to their lengths.
`["python", "is", "awesome"]` → `{"python": 6, "is": 2, "awesome": 7}`

**Exercise 3:** Use `any()` and `all()`:
- Does `[2, 4, 6, 8, 10]` contain any odd numbers?
- Are all elements in `[1, 2, 3, 4, 5]` less than 10?

**Exercise 4:** Sort `[("Alice", 17), ("Bob", 25), ("Charlie", 15), ("Diana", 30)]` by age, then print only people over 18.
