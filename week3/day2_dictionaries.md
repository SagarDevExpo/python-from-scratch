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

# Count word frequency
sentence = "the cat sat on the mat the cat"
word_count = {}
for w in sentence.split():
    word_count[w] = word_count.get(w, 0) + 1
print(word_count)  # {'the': 3, 'cat': 2, 'sat': 1, ...}
```

---

## Part 7: DSA dictionary patterns (CRUCIAL)

```python
# PATTERN 1: "Have I seen this before?"
def has_duplicate(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = True
    return False

# PATTERN 2: Two Sum with hash map (THE Amazon question)
def two_sum(nums, target):
    seen = {}  # number → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# PATTERN 3: Group by key
def group_by_length(words):
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    return groups
```

---

## Exercises

**Exercise 1:** Create a dictionary of 5 countries and their capitals.
Ask the user for a country, print the capital.
If not found, print `"Country not in database"`.

**Exercise 2:** Given `nums = [1, 3, 2, 1, 4, 1, 3, 2, 1]`, count how many times each number appears. Print the most frequent number.

**Exercise 3:** Write `are_anagrams(s1, s2)` using dictionaries to count characters.
`"listen"` and `"silent"` → `True`

**Exercise 4:** Given `[("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 95)]`, create a dict and find the student with the highest score.
