# Week 3 Prerequisites: Organizing Data and Reusing Ideas

Week 3 is where Python starts feeling bigger. The goal is not just to know new tools. The goal is to choose the right shape for the problem.

## 1. Functions hide a repeatable idea behind a name

A function is useful when you can say:

```text
Given this input, produce this output.
```

Before writing a function, write:

```text
Name:
Inputs:
Output:
```

If you cannot name the output, the function is probably still fuzzy.

## 2. `print` shows; `return` gives back

Use `print()` when you only want to display something.

Use `return` when another part of the program needs the answer.

Mental test:

```text
Will I need this result later?
```

If yes, return it.

## 3. Dictionaries answer "given this, what is that?"

A dictionary stores relationships.

```text
name -> phone number
letter -> count
word -> frequency
student -> score
```

Before using a dictionary, ask:

```text
What is the key?
What is the value?
```

This one question removes a lot of confusion.

## 4. Assignment creates or updates dictionary keys

This works even if the dictionary starts empty:

```python
freq = {}
freq["a"] = 1
```

If the key does not exist, Python creates it. If it already exists, Python replaces the old value.

That is why frequency counting works:

```python
freq[ch] = freq.get(ch, 0) + 1
```

Read it as:

```text
Take the old count, or 0 if missing, then add 1.
```

## 5. Sets answer "have I seen this?"

A set is useful when you only care whether something exists, not how many times or where.

Good uses:

- remove duplicates
- check membership quickly
- track visited items
- find common values

Ask:

```text
Do I need a value attached to this item?
```

If yes, use a dictionary. If no, a set may be enough.

## 6. Tuples are fixed small groups

A tuple is good for values that belong together and should not change:

```python
(x, y)
("Alice", 85)
```

Think of a tuple as one record with a few fields.

## 7. Comprehensions are compressed loops

A list comprehension is not new magic. It is a loop written tightly.

First understand the regular loop. Then compress it.

Ask:

```text
Am I transforming each item?
Am I filtering some items?
Am I doing both?
```

If it feels unreadable, use the regular loop.

## 8. Choose the data structure by the question

- Need order and duplicates? Use a list.
- Need unique values? Use a set.
- Need key-value relationships? Use a dictionary.
- Need a fixed pair or small record? Use a tuple.

The right data structure often makes the solution feel obvious.

## 9. Week 3 thinking habit

Before coding, classify the problem:

```text
Is this search, count, group, transform, filter, or lookup?
```

That classification points you toward the pattern.
