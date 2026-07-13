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

### 🧩 Why this beats checking every pair

The obvious way is two nested loops comparing every pair — that's `O(n²)`. The hash-map trick does it in **one pass** by remembering numbers as it goes. For each number it asks *"have I already seen the partner I need?"* — an `O(1)` dict lookup.

Trace `two_sum([2, 7, 11, 15], 9)`. `seen` starts `{}` (stores `number → its index`).

| `index` | `number` | `needed = 9 - number` | `needed in seen?` | Action |
|---------|----------|------------------------|--------------------|--------|
| 0 | 2 | 7 | No (empty) | store `2 → 0`, `seen = {2: 0}` |
| 1 | 7 | 2 | **Yes! 2 is at index 0** | `return [0, 1]` 🛑 |

It returns `[0, 1]` — positions of the two numbers (2 and 7) that sum to 9. This is the same pattern from Week 3 dictionaries; here you're seeing *why* it's fast: trading a little memory (`seen`) for a huge speed win. Whenever a problem says "find two things that relate to a target," reach for this.

---

## Exercises

1. Count each character in a string.
2. Return the most frequent number in a list.
3. Group words by their first letter.
4. Type `two_sum()` again without looking.

