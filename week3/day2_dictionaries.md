# Day 2: Dictionaries — Key-Value Storage

**Time:** ~30 minutes

Today you learn:
1. What dictionaries are and when to use them
2. Adding, accessing, updating, removing entries
3. Looping through dictionaries
4. Counting patterns (these ARE hash maps for DSA!)

**Practice file:** Create `day2_practice.py`

---

## Part 1: What is a dictionary?

A dictionary stores **KEY: VALUE** pairs. Like a phone book: name → number.

```python
person = {
    "name": "Sagar",
    "age": 25,
    "city": "Austin"
}
```

Keys must be unique. Values can repeat.

---

## Part 2: Accessing values

```python
print(person["name"])              # "Sagar"
# person["job"]                    # KeyError!

# SAFE access with .get()
print(person.get("job"))           # None (no error!)
print(person.get("job", "N/A"))    # "N/A" (custom default)
```

---

## Part 3: Adding, updating, removing

```python
person["job"] = "DevOps"           # Add new
person["age"] = 26                 # Update existing

val = person.pop("city")          # Remove and return value
del person["age"]                 # Remove without return
```

---

## Part 4: Checking if a key exists

```python
person = {"name": "Sagar", "age": 25}

print("name" in person)    # True (checks KEYS)
print("Sagar" in person)   # False! "Sagar" is a VALUE, not a key
```

---

## Part 5: Looping through dictionaries

```python
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Keys and values together (most common)
for name, score in scores.items():
    print(f"{name}: {score}")

# Just keys
for name in scores:
    print(name)

# Just values
for score in scores.values():
    print(score)
```

---

## Part 6: Counting with dictionaries (THE key DSA skill)

```python
# Count character frequency
word = "mississippi"
freq = {}
for char in word:
    freq[char] = freq.get(char, 0) + 1
print(freq)  # {'m': 1, 'i': 4, 's': 4, 'p': 2}
```

### 🐢 Let's trace this SLOWLY

The confusing line is `freq[char] = freq.get(char, 0) + 1`. Read it right-to-left:

1. `freq.get(char, 0)` → "How many times have I seen this char so far? If never, say 0."
2. `+ 1` → "Add this new sighting."
3. `freq[char] = ...` → "Store the new count back."

In plain English: **"whatever the count was, make it one bigger."**

Let's walk through the first few letters of `"mississippi"`. The dict `freq` starts **empty** `{}`.

| Step | `char` | `freq.get(char, 0)` | `+ 1` | `freq` after this step |
|------|--------|----------------------|-------|-------------------------|
| 1    | `m`    | 0 (never seen)       | 1     | `{'m': 1}`              |
| 2    | `i`    | 0 (never seen)       | 1     | `{'m': 1, 'i': 1}`      |
| 3    | `s`    | 0 (never seen)       | 1     | `{'m': 1, 'i': 1, 's': 1}` |
| 4    | `s`    | 1 (seen once!)       | 2     | `{'m': 1, 'i': 1, 's': 2}` |
| 5    | `i`    | 1 (seen once!)       | 2     | `{'m': 1, 'i': 2, 's': 2}` |
| ...  | ...    | ...                  | ...   | keeps growing           |

By the time the loop finishes every letter, you get `{'m': 1, 'i': 4, 's': 4, 'p': 2}`.

**Why `.get(char, 0)` instead of `freq[char]`?**
The first time you see a letter, it's NOT in the dict yet. `freq[char]` would crash with a `KeyError`. `.get(char, 0)` politely returns `0` instead of crashing. That `0` is your "starting count."

```python
# Count word frequency — SAME pattern, just words instead of letters
sentence = "the cat sat on the mat the cat"
word_count = {}
for w in sentence.split():   # .split() breaks it into ['the','cat','sat',...]
    word_count[w] = word_count.get(w, 0) + 1
print(word_count)  # {'the': 3, 'cat': 2, 'sat': 1, ...}
```

Once you recognize "count how many times X appears," your brain should instantly reach for this pattern.

---

## Part 7: DSA dictionary patterns (CRUCIAL)

### PATTERN 1: "Have I seen this before?"

```python
def has_duplicate(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True      # already in the dict → it's a duplicate!
        seen[num] = True     # first time → remember it
    return False             # loop finished, no repeats found
```

**The idea:** keep a dict called `seen` as your memory. For each number, first ask *"is it already in my memory?"* If yes → duplicate, return `True` immediately (emergency exit, just like `find_target`). If no → write it into memory and move on.

Trace `has_duplicate([3, 5, 3])`. `seen` starts as `{}`.

| Loop | `num` | `num in seen?` | Action | `seen` after |
|------|-------|-----------------|--------|--------------|
| 1    | 3     | No              | store 3 | `{3: True}` |
| 2    | 5     | No              | store 5 | `{3: True, 5: True}` |
| 3    | 3     | **Yes!**        | `return True` 🛑 | (function stops) |

If the list had no repeats, the loop would end and we'd hit `return False`.

---

### PATTERN 2: Two Sum with a hash map (THE Amazon question)

```python
def two_sum(nums, target):
    seen = {}  # number → the index where we saw it
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

**The goal:** find two numbers in the list that add up to `target`, and return their *positions*.

**The clever trick:** instead of checking every pair (slow), for each number we ask: *"what OTHER number do I need to hit the target?"* That needed number is the **complement** = `target - num`. Then we just check: *"have I already seen that complement?"*

Trace `two_sum([2, 7, 11, 15], 9)`. `seen` starts as `{}`.

| Loop | `i` | `num` | `complement = 9 - num` | `complement in seen?` | Action |
|------|-----|-------|-------------------------|------------------------|--------|
| 1    | 0   | 2     | 9 - 2 = **7**           | No (`seen` is empty)   | store `2 → 0`, `seen = {2: 0}` |
| 2    | 1   | 7     | 9 - 7 = **2**           | **Yes! 2 is in seen**  | `return [seen[2], 1]` = `[0, 1]` 🛑 |

So it returns `[0, 1]` — meaning "the numbers at positions 0 and 1 (which are 2 and 7) add up to 9." ✅

**Why store `number → index`?** Because the question asks for *positions*, not the values. When we find the complement, `seen[complement]` instantly tells us *where* that earlier number was.

If no pair ever works, the loop finishes and we return `[]` (empty = "no answer found").

---

### PATTERN 3: Group items by a key

```python
def group_by_length(words):
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []      # first word of this length → make an empty bucket
        groups[length].append(word)  # drop the word into its bucket
    return groups
```

**The idea:** sort words into "buckets" based on their length. The dict maps `length → list of words`.

Trace `group_by_length(["hi", "cat", "dog", "a"])`. `groups` starts as `{}`.

| Loop | `word` | `length` | bucket exists? | `groups` after |
|------|--------|----------|-----------------|-----------------|
| 1    | `hi`   | 2        | No → create it  | `{2: ['hi']}` |
| 2    | `cat`  | 3        | No → create it  | `{2: ['hi'], 3: ['cat']}` |
| 3    | `dog`  | 3        | Yes             | `{2: ['hi'], 3: ['cat', 'dog']}` |
| 4    | `a`    | 1        | No → create it  | `{2: ['hi'], 3: ['cat', 'dog'], 1: ['a']}` |

The `if length not in groups` line is the "do I have a bucket for this yet? if not, make one" step. Without it, `groups[length].append(...)` would crash because the bucket wouldn't exist yet.

---

## Exercises

**Exercise 1:** Create a dictionary of 5 countries and their capitals.
Ask the user for a country, print the capital.
If not found, print `"Country not in database"`.

**Exercise 2:** Given `nums = [1, 3, 2, 1, 4, 1, 3, 2, 1]`, count how many times each number appears. Print the most frequent number.

**Exercise 3:** Write `are_anagrams(s1, s2)` using dictionaries to count characters.
`"listen"` and `"silent"` → `True`

**Exercise 4:** Given `[("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 95)]`, create a dict and find the student with the highest score.
