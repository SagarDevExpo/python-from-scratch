# Day 4: Lists — Your Most Important Data Structure

**Time:** ~30 minutes

Today you learn:
1. Creating and accessing lists
2. Adding, removing, modifying elements
3. Slicing, sorting, looping
4. List patterns used in DSA

**Practice file:** Create `day4_practice.py`

---

## Part 1: Creating and accessing lists

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
empty = []

print(fruits[0])    # "apple" (first)
print(fruits[-1])   # "cherry" (last)
print(fruits[1:3])  # ["banana", "cherry"] (slice)
print(len(fruits))  # 3

# Unlike strings, lists ARE mutable — you CAN change them
fruits[0] = "mango"
print(fruits)  # ["mango", "banana", "cherry"]
```

---

## Part 2: Adding elements

```python
nums = [1, 2, 3]

nums.append(4)         # Add to END → [1, 2, 3, 4]
nums.insert(0, 0)      # Insert at index 0 → [0, 1, 2, 3, 4]
nums.extend([5, 6])    # Add multiple → [0, 1, 2, 3, 4, 5, 6]

# Combine with +
c = [1, 2] + [3, 4]    # [1, 2, 3, 4]
```

---

## Part 3: Removing elements

```python
items = ["a", "b", "c", "d", "e"]

removed = items.pop()     # Removes last: "e"
removed = items.pop(0)    # Removes first: "a"

items = [1, 2, 3, 2, 1]
items.remove(2)           # Removes FIRST 2 → [1, 3, 2, 1]

del nums[1]               # Remove by index (no return value)
```

---

## Part 4: Checking and searching

```python
fruits = ["apple", "banana", "cherry", "banana"]

print("banana" in fruits)      # True
print(fruits.index("cherry"))  # 2
print(fruits.count("banana"))  # 2
```

---

## Part 5: Sorting

```python
nums = [3, 1, 4, 1, 5, 9]

nums.sort()               # Modifies original: [1, 1, 3, 4, 5, 9]
nums.sort(reverse=True)   # Descending: [9, 5, 4, 3, 1, 1]

# sorted() creates a NEW list (original unchanged)
original = [3, 1, 4]
new_sorted = sorted(original)  # original stays [3, 1, 4]

# Reverse a list
nums = [1, 2, 3]
print(nums[::-1])  # [3, 2, 1]
```

---

## Part 6: Looping through lists

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# Values only
for name in names:
    print(name)

# Index and value
for i, name in enumerate(names):
    print(f"{i}: {name}")

# Two lists together
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

---

## Part 7: List patterns for DSA (memorize these!)

```python
# PATTERN 1: Two-pointer (compare from both ends)
nums = [1, 2, 3, 4, 5]
left = 0
right = len(nums) - 1
while left < right:
    print(f"Left: {nums[left]}, Right: {nums[right]}")
    left += 1
    right -= 1
```

### 🧩 Trace the two-pointer walk

Two pointers start at **opposite ends** and step toward the middle. The loop runs while `left < right` (they haven't crossed yet). Trace `nums = [1, 2, 3, 4, 5]`:

| Round | `left` | `right` | `left < right`? | prints | after (`left+1`, `right-1`) |
|-------|--------|---------|------------------|--------|------------------------------|
| 1 | 0 | 4 | True | Left: 1, Right: 5 | left=1, right=3 |
| 2 | 1 | 3 | True | Left: 2, Right: 4 | left=2, right=2 |
| 3 | 2 | 2 | **False** (equal) | — stop | — |

They meet in the middle and the loop ends. This is the backbone of palindrome checks, reversing in place, and pair-finding — you'll reuse it many times.

---

# PATTERN 2: Build a result list
evens = []
for num in [1, 2, 3, 4, 5, 6]:
    if num % 2 == 0:
        evens.append(num)

# PATTERN 3: Find max manually
nums = [7, 2, 9, 4, 1]
max_val = nums[0]
for num in nums:
    if num > max_val:
        max_val = num

# PATTERN 4: Swap two elements (Python style!)
nums[0], nums[4] = nums[4], nums[0]

# PATTERN 5: Create a list of zeros
zeros = [0] * 5  # [0, 0, 0, 0, 0]

# PATTERN 6: Copy a list (= does NOT copy!)
a = [1, 2, 3]
b = a       # b points to SAME list! Changes to b affect a!
b = a[:]    # COPY — b is separate
```

### 🧩 The aliasing trap: why `b = a` doesn't copy

This is one of the sneakiest beginner bugs. With a list, `b = a` does **not** make a second list — it makes `b` a *second label on the same box*. Both names point at one list, so a change through either name shows up in both.

```python
a = [1, 2, 3]
b = a          # b and a are two labels on ONE list
b.append(4)
print(a)       # [1, 2, 3, 4]  😱 a changed too!
```

```
 a ──┐
    ├─→ [1, 2, 3, 4]   (one list, two labels)
 b ──┘
```

To get a **real, separate copy**, slice the whole thing with `a[:]` (or `a.copy()`):

```python
a = [1, 2, 3]
b = a[:]       # b is now its OWN list
b.append(4)
print(a)       # [1, 2, 3]   ✅ a is untouched
```

Rule of thumb: **`=` copies the label, not the list.** When you want an independent copy, use `[:]`.

---

## Exercises

**Exercise 1:** Create a list of 5 numbers. Print the sum, the average, and the largest — using loops, NOT `sum()` or `max()`.

**Exercise 2:** Given `nums = [4, 2, 7, 1, 9, 3]`, remove all odd numbers. Print: `[4, 2]`.
Hint: Build a NEW list with only even numbers.

**Exercise 3:** Given two lists, find elements that appear in BOTH.
`[1, 2, 3, 4, 5]` and `[4, 5, 6, 7, 8]` → `[4, 5]`

**Exercise 4:** Reverse a list WITHOUT `.reverse()` or `[::-1]`.
Use a loop and swap from both ends.
`[1, 2, 3, 4, 5]` → `[5, 4, 3, 2, 1]`

**Exercise 5:** Move all zeros to the end.
`[0, 1, 0, 3, 12]` → `[1, 3, 12, 0, 0]`
*(This is LeetCode 283 — you're already doing DSA!)*
