# Day 1: assert — Quick Checks for Your Code

**Time:** ~35 minutes

Today you learn:
1. Why testing matters
2. `assert`
3. Testing normal and edge cases
4. Separating logic from input/output

**Practice file:** Create `day1_practice.py`

---

## Part 1: What Is a Test?

A test checks whether your code returns the answer you expect.

```python
def square(n):
    return n * n


assert square(2) == 4
assert square(0) == 0
assert square(-3) == 9
```

If all assertions pass, nothing prints. Quiet is good.

### 🧩 What `assert` actually does

Read `assert` as the sentence: **"I promise this is True — if it's not, stop everything."**

```
assert   square(2) == 4
  │          │
  │          └─ a question that's either True or False
  └─ "this had better be True"
```

Python evaluates the part after `assert`:
- If it's **True** → nothing happens, the program continues silently. (That's why passing tests are quiet.)
- If it's **False** → Python throws `AssertionError` and stops, telling you exactly which check failed.

So `assert square(2) == 4` runs `square(2)`, gets `4`, checks `4 == 4` → True → silence. It's an automatic "did my function give the right answer?" alarm that only goes off when something's wrong.

---

## Part 2: Failed assert

```python
def double(n):
    return n + 2


assert double(3) == 6
```

This raises `AssertionError` because `double(3)` returns `5`, not `6`.

---

## Part 3: Test Edge Cases

Do not only test happy paths.

```python
def first_letter(word):
    if word == "":
        return None
    return word[0]


assert first_letter("python") == "p"
assert first_letter("") is None
```

---

## Part 4: Keep Logic Separate

Hard to test:

```python
name = input("Name: ")
print(name.upper())
```

Easy to test:

```python
def loud(name):
    return name.upper()


assert loud("sagar") == "SAGAR"
```

Functions that return values are easier to test than code that only prints.

---

## Exercises

**Exercise 1:** Write `is_even(n)` and test it with at least four asserts.

**Exercise 2:** Write `add(a, b)` and intentionally make one assert fail. Read the error.

**Exercise 3:** Write `get_initials(first, last)` and test normal and empty strings.

**Exercise 4:** Convert an input/print script into a testable function.

