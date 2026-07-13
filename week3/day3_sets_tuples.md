# Day 3: Sets and Tuples

**Time:** ~30 minutes

Today you learn:
1. Sets — unique elements, fast lookup
2. Set operations (union, intersection, difference)
3. Tuples — immutable sequences
4. When to use each: list vs dict vs set vs tuple

**Practice file:** Create `day3_practice.py`

---

## Part 1: Sets — Unique Elements Only

A set is like a list but: **NO duplicates**, **NO order**, **FAST lookup** (O(1)).

```python
fruits = {"apple", "banana", "cherry"}
nums = {1, 2, 2, 3, 3, 3}
print(nums)  # {1, 2, 3} — duplicates removed!

# Create from a list
unique = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4}

# EMPTY SET — must use set(), NOT {}
empty_set = set()    # empty set
empty_dict = {}      # empty DICT (not set!)
```

---

## Part 2: Set operations

```python
colors = {"red", "green", "blue"}

colors.add("yellow")        # Add element
colors.discard("purple")    # Remove (no error if missing)
print("red" in colors)      # True — O(1) fast!
```

---

## Part 3: Set math

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)   # Union: {1, 2, 3, 4, 5, 6, 7, 8}
print(a & b)   # Intersection: {4, 5}
print(a - b)   # Difference: {1, 2, 3}
print(a ^ b)   # Symmetric difference: {1, 2, 3, 6, 7, 8}
```

---

## Part 4: Set patterns for DSA

```python
# PATTERN 1: Remove duplicates
unique = list(set([4, 2, 7, 2, 1, 4]))

# PATTERN 2: Fast lookup (O(1) instead of O(n))
big_set = set(range(1000000))
print(999999 in big_set)  # Instant!

# PATTERN 3: Find common elements
common = set([1,2,3,4]) & set([3,4,5,6])  # {3, 4}

# PATTERN 4: Track visited nodes (CRUCIAL for BFS/DFS!)
visited = set()
visited.add("node_A")
if "node_A" in visited:
    print("Already visited!")
```

### 🐢 Why is a set "fast"? (the O(1) idea in plain words)

Imagine looking for a name in a phone book.
- A **list** = an unsorted pile of papers. To know if a name is there, you check paper 1, then 2, then 3... maybe all of them. If there are a million papers, that's a million checks. This is **O(n)** — "grows with the size."
- A **set** = a magic filing cabinet where each name has a fixed drawer. You go *straight* to the drawer and look. It takes the same tiny amount of time whether there are 10 names or a million. This is **O(1)** — "constant, doesn't grow."

That's why `999999 in big_set` is instant even with a million items. Whenever a problem says *"have I seen this?"* or *"is this in the collection?"*, a set is your tool.

### 🐢 Tracing "find the first duplicate" with a set

```python
def first_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:      # have I met this number before?
            return num       # yes → it's the first repeat, hand it back
        seen.add(num)        # no → remember it and continue
    return None              # loop ended, everything was unique
```

Trace `first_duplicate([2, 1, 3, 1, 2])`. `seen` starts empty `set()`.

| Loop | `num` | `num in seen?` | Action | `seen` after |
|------|-------|-----------------|--------|--------------|
| 1    | 2     | No              | add 2   | `{2}` |
| 2    | 1     | No              | add 1   | `{2, 1}` |
| 3    | 3     | No              | add 3   | `{2, 1, 3}` |
| 4    | 1     | **Yes!**        | `return 1` 🛑 | (stops here) |

It returns `1` — the first number that showed up a second time. Notice this is the *exact same skeleton* as `has_duplicate` from yesterday, except we return the **number itself** instead of `True`. Recognizing that "same skeleton, small change" is the real skill.

---

## Part 5: Tuples — Immutable Lists

A tuple is like a list but you **CAN'T change it** after creation:

```python
point = (3, 4)
print(point[0])  # 3
# point[0] = 5   # ERROR!

# Unpacking
x, y = point     # x=3, y=4

# Tuples as dictionary keys (lists can't!)
locations = {(40.7, -74.0): "New York"}

# Multiple return values
def get_stats(nums):
    return min(nums), max(nums), sum(nums)

lo, hi, total = get_stats([3, 1, 4, 1, 5])
```

---

## Part 6: When to use what?

| Type | Ordered | Mutable | Duplicates | Use For |
|------|---------|---------|------------|---------|
| **list** `[]` | Yes | Yes | Yes | Most sequences, arrays |
| **dict** `{}` | Yes* | Yes | Keys: No | Lookup by key, counting |
| **set** `{}` | No | Yes | No | Uniqueness, fast "exists?" |
| **tuple** `()` | Yes | No | Yes | Fixed data, dict keys |

---

## Exercises

**Exercise 1:** Given two lists, find elements in BOTH, in first only, and in either but not both. Use set operations.
`[1, 2, 3, 4, 5, 5]` and `[4, 5, 6, 7, 8, 8]`

**Exercise 2:** Find the first duplicate element.
`[2, 1, 3, 5, 3, 2]` → `3` (first number appearing a second time)
Hint: Use a set to track what you've seen.

**Exercise 3:** Find the point closest to origin (0,0) from a list of (x, y) tuples.
`[(3, 4), (1, 1), (5, 0), (2, 2)]` → `(1, 1)`
Compare x² + y² (no need for sqrt).

**Exercise 4:** Find all characters that appear exactly once in a string (in order).
`"swiss"` → `['w', 'i']`
