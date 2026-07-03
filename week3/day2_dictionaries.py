"""
DAY 2: Dictionaries — Key-Value Storage
Time: ~30 minutes

Today you learn:
1. What dictionaries are and when to use them
2. Adding, accessing, updating, removing entries
3. Looping through dictionaries
4. Dictionary patterns (these ARE hash maps for DSA!)

Run: python3 day2_dictionaries.py
"""

# ============================================================
# PART 1: What is a dictionary?
# ============================================================

# A dictionary stores KEY: VALUE pairs
# Like a real dictionary: word → definition
# Like a phone book: name → phone number

# Keys must be unique. Values can repeat.

person = {
    "name": "Sagar",
    "age": 25,
    "city": "Austin"
}

print(person)
print(type(person))  # <class 'dict'>

# Empty dictionary
empty = {}
also_empty = dict()


# ============================================================
# PART 2: Accessing values
# ============================================================

person = {"name": "Sagar", "age": 25, "city": "Austin"}

# Access by key (like array by index, but with a name)
print(person["name"])   # "Sagar"
print(person["age"])    # 25

# person["job"]  # KeyError! Key doesn't exist

# SAFE access with .get() — returns None (or default) if missing
print(person.get("job"))          # None (no error!)
print(person.get("job", "N/A"))   # "N/A" (custom default)


# ============================================================
# PART 3: Adding and updating
# ============================================================

person = {"name": "Sagar"}

# Add new key-value pair
person["age"] = 25
person["city"] = "Austin"
print(person)  # {"name": "Sagar", "age": 25, "city": "Austin"}

# Update existing value
person["age"] = 26
print(person["age"])  # 26

# Update multiple at once
person.update({"age": 27, "job": "DevOps"})
print(person)


# ============================================================
# PART 4: Removing entries
# ============================================================

data = {"a": 1, "b": 2, "c": 3}

# pop — remove by key (returns the value)
val = data.pop("b")
print(f"Removed: {val}, Dict: {data}")  # Removed: 2, Dict: {'a': 1, 'c': 3}

# pop with default (no error if missing)
val = data.pop("z", "not found")
print(val)  # "not found"

# del — remove by key
del data["a"]
print(data)  # {'c': 3}

# clear — remove everything
data.clear()
print(data)  # {}


# ============================================================
# PART 5: Checking if a key exists
# ============================================================

person = {"name": "Sagar", "age": 25}

# Use 'in' to check for KEYS (not values)
print("name" in person)     # True
print("job" in person)      # False
print("Sagar" in person)    # False! "Sagar" is a VALUE, not a key

# Common pattern: check before accessing
if "name" in person:
    print(f"Name: {person['name']}")


# ============================================================
# PART 6: Looping through dictionaries
# ============================================================

scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Loop through keys (default)
for name in scores:
    print(name)  # Alice, Bob, Charlie

# Loop through values
for score in scores.values():
    print(score)  # 85, 92, 78

# Loop through BOTH keys and values (most common)
for name, score in scores.items():
    print(f"{name}: {score}")

# Get all keys or values as lists
print(list(scores.keys()))    # ["Alice", "Bob", "Charlie"]
print(list(scores.values()))  # [85, 92, 78]


# ============================================================
# PART 7: Counting with dictionaries (THE key DSA skill)
# ============================================================

# Count occurrences — you WILL use this in almost every DSA problem

# PATTERN: Count character frequency
word = "mississippi"
freq = {}
for char in word:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)  # {'m': 1, 'i': 4, 's': 4, 'p': 2}

# SHORTER: Using .get()
freq = {}
for char in word:
    freq[char] = freq.get(char, 0) + 1
print(freq)  # Same result

# PATTERN: Count word frequency
sentence = "the cat sat on the mat the cat"
word_count = {}
for w in sentence.split():
    word_count[w] = word_count.get(w, 0) + 1
print(word_count)  # {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}


# ============================================================
# PART 8: Dictionary as a lookup table
# ============================================================

# Store information for fast lookup

# Phone book
contacts = {
    "Alice": "555-0001",
    "Bob": "555-0002",
    "Charlie": "555-0003"
}

name = "Bob"
if name in contacts:
    print(f"{name}'s number: {contacts[name]}")

# Grade converter
def letter_grade(score):
    # Using a dict instead of many if/elif
    for threshold, grade in [(90, "A"), (80, "B"), (70, "C"), (60, "D")]:
        if score >= threshold:
            return grade
    return "F"

print(letter_grade(85))  # B


# ============================================================
# PART 9: DSA dictionary patterns (CRUCIAL)
# ============================================================

# PATTERN 1: "Have I seen this before?" (Hash Set behavior)
def has_duplicate(nums):
    """Check if any value appears more than once."""
    seen = {}
    for num in nums:
        if num in seen:
            return True  # Seen it before!
        seen[num] = True
    return False

print(has_duplicate([1, 2, 3, 4]))    # False
print(has_duplicate([1, 2, 3, 2]))    # True

# PATTERN 2: Two Sum with hash map (THE Amazon question)
def two_sum(nums, target):
    """Find indices of two numbers that sum to target."""
    seen = {}  # number → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]

# PATTERN 3: Group by key
def group_by_length(words):
    """Group words by their length."""
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    return groups

print(group_by_length(["hi", "hey", "hello", "ok", "bye"]))
# {2: ['hi', 'ok'], 3: ['hey', 'bye'], 5: ['hello']}


# ============================================================
# EXERCISES
# ============================================================

"""
EXERCISE 1: Create a dictionary of 5 countries and their capitals.
Ask the user for a country, print the capital.
If not found, print "Country not in database".

EXERCISE 2: Given a list of numbers, count how many times each
number appears. Print the most frequent number.
nums = [1, 3, 2, 1, 4, 1, 3, 2, 1]
Expected: 1 appears 4 times (most frequent)

EXERCISE 3: Write a function `are_anagrams(s1, s2)` that returns
True if two strings are anagrams (same character frequencies).
Use dictionaries to count characters.
"listen" and "silent" → True
"hello" and "world" → False

EXERCISE 4: Given a list of tuples (name, score), create a dict
and find the student with the highest score.
data = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 95)]
Expected: "Diana: 95"
"""
