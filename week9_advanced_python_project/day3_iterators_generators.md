# Day 3: Iterators and Generators

**Time:** ~40 minutes

Today you learn:
1. Iterables
2. Iterators
3. `yield`
4. Why generators save memory

**Practice file:** Create `day3_practice.py`

---

## Part 1: Iterables

An iterable is something you can loop over.

```python
for letter in "python":
    print(letter)

for number in [1, 2, 3]:
    print(number)
```

Strings, lists, dictionaries, sets, tuples, and files are iterable.

---

## Part 2: Generator Function

A generator uses `yield` instead of `return`.

```python
def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1


for n in count_up_to(3):
    print(n)
```

It produces values one at a time.

### 🧩 `yield` = "hand one out, then PAUSE"

The key difference from `return`:
- `return` gives back **one** value and the function is **done forever**.
- `yield` gives back one value, then **freezes the function in place** (remembering all its variables). Next time you ask for a value, it **resumes right where it paused**.

Trace `for n in count_up_to(3)` — watch how it ping-pongs:

| The `for` asks... | Function resumes... | `number` | `yield` hands out | `for` prints |
|-------------------|---------------------|----------|--------------------|---------------|
| 1st value | starts, `number=1`, `1<=3` True | 1 | **yields 1**, freezes | 1 |
| 2nd value | wakes up, `number=2`, `2<=3` True | 2 | **yields 2**, freezes | 2 |
| 3rd value | wakes up, `number=3`, `3<=3` True | 3 | **yields 3**, freezes | 3 |
| 4th value | wakes up, `number=4`, `4<=3` **False** → loop ends → function finishes | 4 | (nothing) | (loop stops) |

The function isn't run all at once — it's paused and resumed on demand, like a video you play one frame at a time. That "pause and remember" ability is what `yield` gives you and `return` cannot.

---

## Part 3: Why Generators?

This builds the whole list:

```python
numbers = [n for n in range(1_000_000)]
```

This produces values when needed:

```python
numbers = (n for n in range(1_000_000))
```

Generators are useful when data is large or streamed.

---

## Part 4: Generator Expressions

```python
squares = (n * n for n in range(5))

for square in squares:
    print(square)
```

Looks like a list comprehension, but uses parentheses.

---

## Exercises

**Exercise 1:** Write a generator that yields even numbers up to `n`.

**Exercise 2:** Write a generator that yields words from a sentence one by one.

**Exercise 3:** Compare list comprehension and generator expression syntax.

**Exercise 4:** Explain why generators can save memory.

