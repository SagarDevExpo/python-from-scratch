# Weeks 3-5 Practice: Functions, Dictionaries, Sets, Mixed Problems

**Time:** 60-75 minutes

**Practice file:** Create `weeks3_4_5_review.py`

This review is about turning repeated logic into functions and choosing the right data structure.

---

## Warm-Up: Name the Shape

For each prompt, write the likely pattern before coding:

1. Count how many times each word appears.
2. Remove duplicate numbers while keeping order.
3. Find the student with the highest score.
4. Check whether two words use the same letters.
5. Group words by their first letter.

Use words like:

```text
frequency dictionary
seen set
best-so-far
group by key
```

---

## Challenge 1: Function Return Practice

Write `classify_number(n)` that returns:

- `"zero"` if `n` is `0`
- `"positive even"`
- `"positive odd"`
- `"negative even"`
- `"negative odd"`

Do not print inside the function. Print only after calling it.

Pattern focus: `return` gives a result back.

---

## Challenge 2: Word Frequency Function

Write:

```python
word_frequencies(text)
```

Return a dictionary mapping each lowercase word to its count.

Example:

```python
word_frequencies("Python is fun and python is useful")
```

Expected:

```python
{"python": 2, "is": 2, "fun": 1, "and": 1, "useful": 1}
```

Pattern focus: `dict.get(key, 0) + 1`.

---

## Challenge 3: Most Frequent Word

Using the result from Challenge 2, find the most frequent word.

If there is a tie, keep the first one found.

Pattern focus: dictionary loop plus best-so-far.

---

## Challenge 4: Unique While Keeping Order

Write:

```python
remove_duplicates_keep_order(nums)
```

Example:

```python
[4, 1, 4, 2, 1, 3] -> [4, 1, 2, 3]
```

Pattern focus: set for `seen`, list for `result`.

---

## Challenge 5: Anagram Checker Two Ways

Write `is_anagram(a, b)` two ways:

1. using `sorted()`
2. using dictionaries

Make it case-insensitive.

Pattern focus: same output, different solution shape.

---

## Challenge 6: Contact Book Functions

Use a dictionary where:

```text
name -> phone number
```

Write:

- `add_contact(book, name, phone)`
- `find_contact(book, name)`
- `delete_contact(book, name)`
- `list_contacts(book)`

Pattern focus: key-value lookup and safe missing-key handling.

---

## Challenge 7: Group Words by Length

Given:

```python
words = ["hi", "cat", "dog", "hello", "sun", "python"]
```

Return:

```python
{
    2: ["hi"],
    3: ["cat", "dog", "sun"],
    5: ["hello"],
    6: ["python"]
}
```

Pattern focus: dictionary of lists.

---

## Challenge 8: Matrix Summary

Given:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Write functions for:

- total sum
- row sums
- column sums
- largest number

Pattern focus: nested loops over rows and values.

---

## Challenge 9: Simple Two Sum, Then Hash Map Two Sum

Given:

```python
nums = [2, 7, 11, 15]
target = 9
```

First solve with two nested loops.

Then solve with a dictionary:

```text
needed = target - current
```

Pattern focus: brute force first, then remember useful previous values.

---

## Challenge 10: Mini Analyzer

Write:

```python
analyze_sentence(text)
```

Return a dictionary with:

- `"characters"`: character count ignoring spaces
- `"words"`: word count
- `"unique_words"`: number of unique words
- `"longest_word"`: first longest word
- `"has_digit"`: True if any character is a digit

Pattern focus: combine small patterns cleanly.

---

## Pattern Checklist

You are ready to move deeper into DSA if you can explain:

- when a function should return instead of print
- what dictionary key and value mean
- when to use a set instead of a dictionary
- how `for key, value in data.items()` works
- why `seen` sets help avoid duplicate work
- how to choose between list, dict, set, and tuple
