# Day 1: Functions — Reusable Blocks of Code

**Time:** ~30 minutes

Today you learn:
1. How to define and call functions
2. Parameters and return values
3. Default values and multiple returns
4. Scope (where variables live)

**Practice file:** Create `day1_practice.py`

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

Without return, a function gives back `None`:

```python
def say_hi():
    print("Hi!")

x = say_hi()  # Prints "Hi!" but x is None
```

Return **ENDS** the function immediately:

```python
def check_age(age):
    if age < 0:
        return "Invalid age"  # Stops here
    if age >= 18:
        return "Adult"
    return "Minor"
```

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

```python
# PATTERN 1: Search and return index
def find_target(nums, target):
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1  # Not found

# PATTERN 2: Build and return a list
def get_evens(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result

# PATTERN 3: Accumulator
def sum_list(nums):
    total = 0
    for num in nums:
        total += num
    return total
```

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
