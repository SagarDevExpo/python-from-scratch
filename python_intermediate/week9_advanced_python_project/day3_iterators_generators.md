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

