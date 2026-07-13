# Day 4: Linear Search and Binary Search

**Time:** ~40 minutes

Today you learn:
1. Linear search
2. Binary search
3. Why binary search requires sorted data

**Practice file:** Create `day4_practice.py`

---

## Part 1: Linear Search

Linear search checks values from left to right.

```python
def linear_search(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1
```

Time: `O(n)`  
Extra space: `O(1)`

---

## Part 2: Binary Search Idea

For sorted data, compare with the middle:

```text
[2, 5, 8, 12, 16, 23, 38]
          ^
target = 23

23 is greater than 12, so ignore the entire left half.
```

---

## Part 3: Binary Search Code

```python
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
```

Time: `O(log n)`  
Extra space: `O(1)`

---

## Part 4: Trace It

For `[2, 5, 8, 12, 16, 23, 38]`, target `23`:

```text
left=0, right=6, middle=3, value=12
left=4, right=6, middle=5, value=23
found at index 5
```

Binary search on unsorted data is incorrect because choosing a half would not
tell you where the target can be.

### 🔍 Full trace, one row per loop (target = 23)

The list, with indexes:

```
index:   0   1   2   3    4    5    6
value:   2   5   8   12   16   23   38
```

`left` and `right` mark the section still worth searching. `middle` is the midpoint we check each round.

| Loop | `left` | `right` | `middle = (left+right)//2` | `numbers[middle]` | Compare to 23 | What we do |
|------|--------|---------|-----------------------------|--------------------|----------------|------------|
| 1 | 0 | 6 | (0+6)//2 = **3** | 12 | 12 < 23 → target is to the **right** | throw away left half: `left = 3+1 = 4` |
| 2 | 4 | 6 | (4+6)//2 = **5** | 23 | 23 == 23 → **match!** | `return 5` 🛑 |

Each loop **halves** what's left to search — that's why it's `O(log n)`. Notice the two "steering" lines:
- `numbers[middle] < target` → the answer must be bigger, so move `left` up past the middle.
- else → the answer must be smaller, so move `right` down below the middle.

**Why it needs sorted data:** the whole trick is "if the middle is too small, the answer is definitely to the right." That's only guaranteed to be true when the list is in order. On unsorted data, throwing away a half could throw away the answer.

---

## Exercises

**Exercise 1:** Type both searches from memory.

**Exercise 2:** Modify linear search to return the first repeated occurrence.

**Exercise 3:** Use binary search to find `7` in `[1, 3, 5, 7, 9, 11]`.
Write each `left`, `right`, and `middle` value on paper.

**Exercise 4:** Test absent targets and empty lists.

