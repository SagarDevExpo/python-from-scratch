"""
DAY 4: List Comprehensions + Useful Tools
Time: ~30 minutes

Today you learn:
1. List comprehensions — build lists in one line
2. Dictionary and set comprehensions
3. Useful built-in functions for DSA
4. Lambda functions (tiny one-line functions)

Run: python3 day4_list_comprehensions.py
"""

# ============================================================
# PART 1: List Comprehension — Build lists cleanly
# ============================================================

# REGULAR way to build a list:
squares = []
for i in range(6):
    squares.append(i ** 2)
print(squares)  # [0, 1, 4, 9, 16, 25]

# LIST COMPREHENSION way (same result, one line):
squares = [i ** 2 for i in range(6)]
print(squares)  # [0, 1, 4, 9, 16, 25]

# SYNTAX: [expression FOR variable IN iterable]

# More examples:
doubles = [x * 2 for x in range(5)]        # [0, 2, 4, 6, 8]
words = [w.upper() for w in ["hi", "bye"]]  # ["HI", "BYE"]
lengths = [len(w) for w in ["apple", "pie", "cake"]]  # [5, 3, 4]


# ============================================================
# PART 2: List Comprehension with condition (filter)
# ============================================================

# Add IF to filter which items are included

# Only even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Only positive numbers
nums = [-3, -1, 0, 2, 5, -4, 7]
positives = [n for n in nums if n > 0]
print(positives)  # [2, 5, 7]

# Only words longer than 3 letters
words = ["the", "quick", "brown", "fox", "jumps"]
long_words = [w for w in words if len(w) > 3]
print(long_words)  # ["quick", "brown", "jumps"]

# SYNTAX: [expression FOR variable IN iterable IF condition]


# ============================================================
# PART 3: If-else in comprehension (transform)
# ============================================================

# Note: when using if-else, the position changes!

# With filter (IF only — goes AFTER):
# [x for x in items if condition]

# With transform (IF-ELSE — goes BEFORE):
# [a if condition else b for x in items]

labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print(labels)  # ["even", "odd", "even", "odd", "even", "odd"]

# Absolute values
nums = [-3, -1, 0, 2, -5]
absolutes = [n if n >= 0 else -n for n in nums]
print(absolutes)  # [3, 1, 0, 2, 5]


# ============================================================
# PART 4: Dictionary & Set Comprehension
# ============================================================

# Dictionary comprehension: {key: value for ...}
squares_dict = {x: x ** 2 for x in range(6)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Count character frequencies in one line
word = "banana"
freq = {char: word.count(char) for char in set(word)}
print(freq)  # {'b': 1, 'a': 3, 'n': 2}

# Set comprehension: {value for ...}
first_letters = {w[0] for w in ["apple", "avocado", "banana", "blueberry"]}
print(first_letters)  # {'a', 'b'}


# ============================================================
# PART 5: Useful built-in functions for DSA
# ============================================================

nums = [3, 1, 4, 1, 5, 9, 2, 6]

# sum, min, max
print(f"Sum: {sum(nums)}")  # 31
print(f"Min: {min(nums)}")  # 1
print(f"Max: {max(nums)}")  # 9

# any() — True if ANY element is True
print(any([False, False, True]))   # True
print(any([False, False, False]))  # False

# Check if any number is negative:
has_negative = any(n < 0 for n in nums)
print(f"Has negative: {has_negative}")  # False

# all() — True if ALL elements are True
print(all([True, True, True]))    # True
print(all([True, False, True]))   # False

# Check if all numbers are positive:
all_positive = all(n > 0 for n in nums)
print(f"All positive: {all_positive}")  # True

# zip() — pair up elements from two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Create dict from two lists:
grade_book = dict(zip(names, scores))
print(grade_book)  # {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# map() — apply function to every element
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # [2, 4, 6, 8]
# (list comprehension is usually cleaner: [x*2 for x in nums])

# filter() — keep elements that pass a test
evens = list(filter(lambda x: x % 2 == 0, range(10)))
print(evens)  # [0, 2, 4, 6, 8]

# sorted() with key
words = ["banana", "pie", "apple", "cake"]
by_length = sorted(words, key=len)
print(by_length)  # ['pie', 'cake', 'apple', 'banana']

# Sort by last character
by_last = sorted(words, key=lambda w: w[-1])
print(by_last)  # ['banana', 'apple', 'cake', 'pie']


# ============================================================
# PART 6: Lambda — Tiny functions
# ============================================================

# lambda is a function in one line (no name needed)

# Regular function:
def square(x):
    return x * x

# Lambda version:
square = lambda x: x * x

print(square(5))  # 25

# Lambda with multiple parameters:
add = lambda a, b: a + b
print(add(3, 4))  # 7

# Most useful with sorted(), map(), filter():
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

# Sort by score (second element of tuple)
by_score = sorted(students, key=lambda s: s[1])
print(by_score)  # [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# Sort by score descending
by_score_desc = sorted(students, key=lambda s: s[1], reverse=True)
print(by_score_desc)


# ============================================================
# EXERCISES
# ============================================================

"""
EXERCISE 1: Using list comprehension, create:
a) A list of cubes from 1 to 10: [1, 8, 27, ..., 1000]
b) A list of strings: ["1!", "2!", "3!", ..., "10!"]
c) A list of numbers 1-100 that are divisible by both 3 AND 5

EXERCISE 2: Given a list of words, use dict comprehension to create
a dict mapping each word to its length.
words = ["python", "is", "awesome", "and", "fun"]
Expected: {"python": 6, "is": 2, "awesome": 7, "and": 3, "fun": 3}

EXERCISE 3: Use any() and all() to check:
a) Does the list [2, 4, 6, 8, 10] contain any odd numbers?
b) Are all elements in [1, 2, 3, 4, 5] less than 10?

EXERCISE 4: Given a list of tuples (name, age), sort by age
then print only people over 18.
people = [("Alice", 17), ("Bob", 25), ("Charlie", 15), ("Diana", 30)]
"""
