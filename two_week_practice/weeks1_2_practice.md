# Weeks 1-2 Practice: Basics, Decisions, Loops, Strings, Lists

**Time:** 45-60 minutes

**Practice file:** Create `weeks1_2_review.py`

Try these without opening old solutions. The goal is not speed. The goal is recognizing the shape.

---

## Warm-Up: Predict First

Before running, predict the output.

```python
x = "5"
y = 2
print(x * y)
```

```python
name = "  Sagar  "
print(name.strip().lower().capitalize())
```

```python
count = 0
if count:
    print("yes")
else:
    print("no")
```

---

## Challenge 1: Input Cleaner

Ask for a username and password.

Rules:

- spaces around the username should not count
- username cannot be empty
- password cannot be empty
- password must be at least 8 characters
- print one clear message

Pattern focus: truthy/falsy checks, `strip()`, `if / elif / else`.

---

## Challenge 2: Number Labels

Ask for a number and print all labels that apply:

- even or odd
- positive, negative, or zero
- divisible by 3
- divisible by 5

If the number is zero, print only `Zero`.

Pattern focus: separate `if` statements versus one `if / elif / else` chain.

---

## Challenge 3: Menu With Match

Ask for a command: `start`, `stop`, `restart`, or `status`.

Make the command case-insensitive.

Print a message for each command. Print `Invalid command` for anything else.

Pattern focus: normalize input before comparing.

---

## Challenge 4: Sum Until Stop

Keep asking for numbers until the user enters `0`.

Print:

- total sum
- how many non-zero numbers were entered
- average of non-zero numbers

Pattern focus: `while True`, `break`, running total, counter.

---

## Challenge 5: First Power Greater Than Limit

Ask for:

- base number
- limit

Start with `n = 1`. Keep multiplying by the base until `n` is greater than the limit.

Print:

```text
base^power = result
```

Example:

```text
3^7 = 2187
```

Pattern focus: loop until condition changes, counter as exponent.

---

## Challenge 6: Vowel Replacer

Ask for a word. Build a new word where every vowel becomes `*`.

Example:

```text
programming -> pr*gr*mm*ng
```

Pattern focus: build a new string character by character.

---

## Challenge 7: List Rotation, Both Directions

Given:

```python
nums = [1, 2, 3, 4, 5]
```

Rotate right by `2`:

```python
[4, 5, 1, 2, 3]
```

Rotate left by `2`:

```python
[3, 4, 5, 1, 2]
```

Solve once with slicing and once with `pop()` / `insert()` / `append()`.

Pattern focus: split into chunks versus simulate movement.

---

## Challenge 8: Longest Word With Tie

Given a sentence, find the longest word. If there is a tie, keep the first one found.

Pattern focus: best-so-far tracker.

---

## Challenge 9: Character Type Counter

Given:

```python
text = "Hello World 123"
```

Count:

- uppercase letters
- lowercase letters
- digits

Expected idea:

```python
{"upper": 2, "lower": 8, "digits": 3}
```

Pattern focus: dictionary as category counters.

---

## Challenge 10: Consecutive String Compression

Compress consecutive repeated characters.

Examples:

```text
aaabbbccca -> a3b3c3a1
abcd -> abcd
```

If the compressed string is not shorter, return the original.

Pattern focus: compare current character with previous character.

---

## Pattern Checklist

Before moving on, make sure you can explain:

- why `input()` returns a string
- when to use `if`, `elif`, and separate `if`
- why `while` can run forever
- how `for item in list` differs from `for i in range(len(list))`
- why strings use `+=` but lists use `.append()`
- why dictionaries use `dict[key] = value`
