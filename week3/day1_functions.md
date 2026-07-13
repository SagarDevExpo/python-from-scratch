# Day 1: Functions — Reusable Blocks of Code

**Time:** ~30 minutes

Today you learn:
1. How to define and call functions
2. Parameters and return values
3. Default values and multiple returns
4. Scope (where variables live)

**Practice file:** Create `day1_practice.py`


Mental Model:

`````
def = create the machine
check(age) = run the machine
return = machine gives an answer back
print = show the answer
`````

---

## Part 1: Defining and calling a function

```python
def greet():
    print("Hello!")
    print("Welcome to Python!")

# Call it
greet()
greet()  # Call as many times as you want
```

---

## Part 2: Parameters — Passing data IN

```python
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Sagar")
greet_person("Alice")

# Multiple parameters
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add(3, 5)
add(10, 20)
```

---

## Part 3: return — Getting data OUT

`return` sends a value BACK to where the function was called:

```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(f"4 x 5 = {result}")  # 20
```

### 🏰 The vending-machine model (the key idea)

Think of a function as a **vending machine**:

- You put something **in** (the arguments — like money + a button press)
- The machine does work **inside** (hidden from you)
- It gives something **out** (the `return` value — your snack)

```python
def multiply(a, b):   # ← the "in" slots: two numbers
    return a * b      # ← the snack comes out

result = multiply(4, 5)   # result "catches" the 20 that comes out
```

`return` = **"here is your answer, hand it back to whoever called me."**

Without return, a function gives back `None`:

```python
def say_hi():
    print("Hi!")

x = say_hi()  # Prints "Hi!" but x is None
```

Why? `print` shows text on screen, but the function never `return`ed a value to *catch*. So `x` catches nothing = `None`. **Printing and returning are different jobs.**

### 🛑 return ENDS the function immediately

The moment `return` runs, the function **stops right there** — nothing after it runs. It's like an emergency exit:

```python
def check_age(age):
    if age < 0:
        return "Invalid age"  # if this fires, we STOP here...
    if age >= 18:
        return "Adult"        # ...never reaching the lines below
    return "Minor"
```

Trace `check_age(25)`:
1. `age < 0`? → `25 < 0` is False → skip.
2. `age >= 18`? → `25 >= 18` is True → `return "Adult"` 🛑 function ends. The last `return "Minor"` never runs.

Trace `check_age(-4)`:
1. `age < 0`? → `-4 < 0` is True → `return "Invalid age"` 🛑 stops instantly.

Remember this 🛑 "return = emergency exit" idea — it's the key to understanding the DSA patterns in Part 7.

---

## Part 4: Default parameters

```python
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25 (defaults to square)
print(power(5, 3))   # 125
print(power(2, 10))  # 1024
```

---

## Part 5: Multiple return values

```python
def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([3, 1, 4, 1, 5, 9])
print(f"Min: {lo}, Max: {hi}")

def divide(a, b):
    return a // b, a % b  # quotient, remainder

q, r = divide(17, 5)
print(f"17 ÷ 5 = {q} remainder {r}")
```

---

## Part 6: Scope — Where variables live

Variables inside a function are **LOCAL** — they don't exist outside:

```python
def my_function():
    local_var = "I only exist inside"
    print(local_var)

my_function()
# print(local_var)  # ERROR!
```

Parameters are also local:

```python
def double(x):
    x = x * 2
    return x

my_num = 5
result = double(my_num)
print(f"my_num: {my_num}")   # 5 (unchanged!)
print(f"result: {result}")    # 10
```

---

## Part 7: DSA function patterns

### PATTERN 1: Search and return an index

```python
def find_target(nums, target):
    for i, num in enumerate(nums):
        if num == target:
            return i      # found it! hand back the position, STOP
    return -1             # loop finished, never found it
```

This is *the* pattern that confuses everyone at first. Let's trace it **super slowly**.

Call it like this — we want to find *where* 30 lives in the list:

```python
result = find_target([10, 20, 30, 40], 30)
```

**What `enumerate` gives you:** two things each loop — the position `i` AND the value `num`.

| Loop | `i` (position) | `num` (value) | `num == target`? (is it 30?) | What happens |
|------|----------------|----------------|-------------------------------|--------------|
| 1    | 0              | 10             | No                            | skip, keep looping |
| 2    | 1              | 20             | No                            | skip, keep looping |
| 3    | 2              | 30             | **Yes!** ✅                    | `return 2` 🛑 STOP |

On loop 3 the `return i` (which is `return 2`) fires. The function **stops immediately** — it never checks 40, never reaches `return -1`. The value `2` flies back out:

```python
result = find_target([10, 20, 30, 40], 30)   # result becomes 2
```

**When does `return -1` run?** Only if the loop finishes *without ever finding* the target. Trace `find_target([10, 20, 30, 40], 99)`: none of them equal 99, the loop ends naturally, so Python moves to the next line → `return -1` (the "not found" signal).

So the two returns are two different endings:
- `return i` → "Found it! Here's the position."
- `return -1` → "Searched everything, it's not here."

### PATTERN 2: Build and return a list

```python
def get_evens(nums):
    result = []            # start with an empty basket
    for num in nums:
        if num % 2 == 0:   # is it even?
            result.append(num)  # yes → drop it in the basket
    return result          # hand back the whole basket at the end
```

Notice the `return` is at the **very end this time**, not inside the loop — because we want to collect *everything* before handing it back, not stop early.

Trace `get_evens([1, 2, 3, 4])`. `result` starts as `[]`:

| Loop | `num` | `num % 2 == 0`? | `result` after |
|------|-------|------------------|-----------------|
| 1    | 1     | No               | `[]` |
| 2    | 2     | Yes → append     | `[2]` |
| 3    | 3     | No               | `[2]` |
| 4    | 4     | Yes → append     | `[2, 4]` |

Loop ends → `return [2, 4]`.

### PATTERN 3: Accumulator (add things up)

```python
def sum_list(nums):
    total = 0          # start the running total at 0
    for num in nums:
        total += num   # add each number onto the total
    return total       # hand back the final total
```

`total += num` means "make total bigger by num." Trace `sum_list([10, 20, 30])`:

| Loop | `num` | `total` before | `total` after |
|------|-------|-----------------|----------------|
| 1    | 10    | 0               | 10             |
| 2    | 20    | 10              | 30             |
| 3    | 30    | 30              | 60             |

Loop ends → `return 60`.

**The big lesson across all three:** notice *where* the `return` sits.
- `find_target` returns **inside** the loop → it can stop early the moment it finds the answer.
- `get_evens` and `sum_list` return **after** the loop → they need to finish looking at everything first.

---

## Exercises

**Exercise 1:** Write `is_palindrome(s)` — returns `True` if string is a palindrome.
`is_palindrome("racecar")` → `True`

**Exercise 2:** Write `factorial(n)` — returns n! using a loop.
`factorial(5)` = 5 × 4 × 3 × 2 × 1 = 120

**Exercise 3:** Write `remove_duplicates(lst)` — returns new list with duplicates removed, keeping order.
`[1, 2, 2, 3, 1, 4]` → `[1, 2, 3, 4]`

**Exercise 4:** Write `two_sum(nums, target)` — returns indices of two numbers that add to target.
`two_sum([2, 7, 11, 15], 9)` → `[0, 1]`
Use brute force (two loops) for now.
