"""
DAY 3: Sets and Tuples
Time: ~30 minutes

Today you learn:
1. Sets — unique elements, fast lookup
2. Set operations (union, intersection, difference)
3. Tuples — immutable sequences
4. When to use each: list vs dict vs set vs tuple

Run: python3 day3_sets_tuples.py
"""

# ============================================================
# PART 1: Sets — Unique Elements Only
# ============================================================

# A set is like a list but:
# - NO duplicates (automatically removed)
# - NO order (can't access by index)
# - FAST lookup: checking "is X in the set?" is O(1)

# Create a set
fruits = {"apple", "banana", "cherry"}
print(fruits)
print(type(fruits))  # <class 'set'>

# Duplicates are automatically removed
nums = {1, 2, 2, 3, 3, 3}
print(nums)  # {1, 2, 3}

# Create from a list (removes duplicates!)
my_list = [1, 2, 2, 3, 3, 4]
unique = set(my_list)
print(unique)  # {1, 2, 3, 4}

# Empty set — MUST use set(), NOT {}
empty_set = set()    # This is an empty set
empty_dict = {}      # This is an empty DICT (not set!)


# ============================================================
# PART 2: Set Operations — Add, Remove, Check
# ============================================================

colors = {"red", "green", "blue"}

# Add
colors.add("yellow")
print(colors)

colors.add("red")  # Already exists — no error, no duplicate
print(colors)

# Remove
colors.remove("green")  # Raises error if not found
colors.discard("purple")  # No error if not found (safer!)

# Check membership (THIS is why sets are powerful — O(1)!)
print("red" in colors)    # True
print("pink" in colors)   # False

# Length
print(len(colors))


# ============================================================
# PART 3: Set Math — Union, Intersection, Difference
# ============================================================

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union — everything from both sets (OR)
print(a | b)       # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))  # Same thing

# Intersection — only elements in BOTH sets (AND)
print(a & b)              # {4, 5}
print(a.intersection(b))  # Same thing

# Difference — in a but NOT in b
print(a - b)             # {1, 2, 3}
print(a.difference(b))   # Same thing

# Symmetric difference — in one OR the other, but NOT both (XOR)
print(a ^ b)                        # {1, 2, 3, 6, 7, 8}
print(a.symmetric_difference(b))    # Same thing


# ============================================================
# PART 4: Set patterns for DSA
# ============================================================

# PATTERN 1: Remove duplicates from a list
nums = [4, 2, 7, 2, 1, 4, 7, 9]
unique = list(set(nums))
print(f"Unique: {unique}")

# PATTERN 2: Fast lookup (instead of list)
# BAD: checking "in" a list is O(n)
big_list = list(range(1000000))
# 999999 in big_list  # Slow! Checks every element

# GOOD: checking "in" a set is O(1)
big_set = set(range(1000000))
# 999999 in big_set  # Instant!

# PATTERN 3: Find common elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"Common: {common}")  # {4, 5}

# PATTERN 4: Find missing elements
all_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
have = {1, 3, 5, 7, 9}
missing = all_nums - have
print(f"Missing: {missing}")  # {2, 4, 6, 8, 10}

# PATTERN 5: Track visited nodes (CRUCIAL for BFS/DFS!)
visited = set()
visited.add("node_A")
visited.add("node_B")

node = "node_A"
if node in visited:
    print(f"Already visited {node}")


# ============================================================
# PART 5: Tuples — Immutable Lists
# ============================================================

# A tuple is like a list but you CAN'T change it after creation

point = (3, 4)
rgb = (255, 128, 0)
single = (42,)  # One-element tuple needs a trailing comma!

print(point[0])  # 3
print(point[1])  # 4
print(len(point))  # 2

# CAN'T modify:
# point[0] = 5  # TypeError!

# Unpacking — assign each element to a variable
x, y = point
print(f"x={x}, y={y}")  # x=3, y=4

name, age, city = ("Sagar", 25, "Austin")
print(f"{name}, {age}, {city}")

# Tuples as dictionary keys (lists can't be keys!)
locations = {
    (40.7, -74.0): "New York",
    (34.0, -118.2): "Los Angeles"
}
print(locations[(40.7, -74.0)])  # "New York"

# Tuples for returning multiple values from functions
def get_stats(numbers):
    return (min(numbers), max(numbers), sum(numbers))

lo, hi, total = get_stats([3, 1, 4, 1, 5])
print(f"Min: {lo}, Max: {hi}, Sum: {total}")


# ============================================================
# PART 6: When to use what?
# ============================================================

"""
CHEAT SHEET:

LIST []:
- Ordered, changeable, allows duplicates
- Use when: order matters, you need to modify
- DSA: most arrays/sequences

DICTIONARY {}:
- Key-value pairs, fast lookup by key
- Use when: looking up by name/id, counting things
- DSA: hash maps, frequency counting, caching

SET {}:
- Unique elements only, fast membership check
- Use when: no duplicates needed, checking "exists?"
- DSA: visited tracking, duplicate removal, lookup

TUPLE ():
- Ordered, NOT changeable (immutable)
- Use when: data shouldn't change, dict keys, function returns
- DSA: coordinates, paired data
"""


# ============================================================
# EXERCISES
# ============================================================

"""
EXERCISE 1: Given two lists, find:
a) Elements in BOTH lists
b) Elements in list1 but NOT in list2
c) ALL unique elements from both lists combined
list1 = [1, 2, 3, 4, 5, 5]
list2 = [4, 5, 6, 7, 8, 8]
Use set operations!

EXERCISE 2: Given a list, find the first duplicate element.
nums = [2, 1, 3, 5, 3, 2]
Expected: 3 (it's the first number that appears a second time)
Hint: Use a set to track what you've seen.

EXERCISE 3: Write a function that takes a list of (x, y) tuples
representing points, and returns the point closest to the origin (0, 0).
Distance formula: sqrt(x² + y²) — or just compare x² + y² (no sqrt needed!)
points = [(3, 4), (1, 1), (5, 0), (2, 2)]
Expected: (1, 1) — distance 1.41

EXERCISE 4: Given a string, find all characters that appear
exactly once (in order). Use a dict for counting, then a list for result.
"swiss" → ['w', 'i']
"aabbcc" → [] (no unique characters)
"""
