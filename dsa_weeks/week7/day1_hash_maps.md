# Day 1: Hash Maps — Fast Lookup with Dictionaries

**Time:** ~35 minutes

Today you learn:
1. Why dictionaries are called hash maps
2. Fast lookup and counting
3. The complement pattern used in Two Sum

**Practice file:** Create `day1_practice.py`

---

## Part 1: Key and Value

A hash map stores a value under a unique key. Python's `dict` is a hash map.

```python
ages = {"Sagar": 30, "Ana": 27}
print(ages["Sagar"])  # 30

ages["Ben"] = 35
print("Ana" in ages)  # True
```

Average lookup, insertion, and deletion are `O(1)`.

---

## Part 2: Frequency Counting

```python
def count_words(words):
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


print(count_words(["cat", "dog", "cat"]))
# {"cat": 2, "dog": 1}
```

This pattern appears constantly in DSA.

---

## Part 3: Two Sum

For each number, ask: “What number do I need to reach the target?”

```python
def two_sum(numbers, target):
    seen = {}

    for index, number in enumerate(numbers):
        needed = target - number

        if needed in seen:
            return [seen[needed], index]

        seen[number] = index

    return []
```

Time: `O(n)`  
Space: `O(n)`

---

## Exercises

1. Count each character in a string.
2. Return the most frequent number in a list.
3. Group words by their first letter.
4. Type `two_sum()` again without looking.

