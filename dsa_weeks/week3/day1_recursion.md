# Day 1: Recursion — A Function Calling Itself

**Time:** ~40 minutes

Today you learn:
1. Base cases
2. Recursive cases
3. How the call stack grows and returns

**Practice file:** Create `day1_practice.py`

---

## Part 1: The Two Required Parts

Every recursive function needs:

1. A **base case** that stops recursion
2. A **recursive case** that moves toward the base case

```python
def countdown(number):
    if number == 0:      # base case
        print("Done!")
        return

    print(number)
    countdown(number - 1)  # recursive case
```

Without a reachable base case, recursion never stops.

---

## Part 2: Factorial

```text
4! = 4 × 3 × 2 × 1
4! = 4 × 3!
```

```python
def factorial(number):
    if number <= 1:
        return 1

    return number * factorial(number - 1)
```

Trace:

```text
factorial(4)
4 × factorial(3)
4 × 3 × factorial(2)
4 × 3 × 2 × factorial(1)
4 × 3 × 2 × 1 = 24
```

---

## Part 3: Recursion Costs

Factorial makes `n` calls:

- Time: `O(n)`
- Call-stack space: `O(n)`

An iterative loop often uses only `O(1)` extra space.

---

## Exercises

1. Print numbers from `1` to `n` recursively.
2. Sum numbers from `1` to `n`.
3. Sum all values in a list recursively.
4. Write both loop and recursive versions of factorial.

