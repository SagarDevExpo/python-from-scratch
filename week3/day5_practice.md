# Day 5: Week 3 Practice — Functions, Dicts, Sets, Comprehensions

**Time:** ~30 minutes

These combine EVERYTHING from all 3 weeks.
If you can do these, **you're ready for DSA!**

**Practice file:** Create `day5_practice.py`

---

## Challenge 1: Inventory System

Build a simple inventory tracker. Write these functions:

- `add_item(inventory, name, quantity)` — add/update item
- `remove_item(inventory, name)` — remove (print error if not found)
- `get_total(inventory)` — return total quantity of all items
- `get_items_above(inventory, threshold)` — names with quantity above threshold

Test:
```python
inventory = {}
add_item(inventory, "apples", 50)
add_item(inventory, "bananas", 30)
add_item(inventory, "oranges", 45)
add_item(inventory, "apples", 20)  # Should update to 70
print(get_total(inventory))         # 145
print(get_items_above(inventory, 40))  # ["apples", "oranges"]
```

---

## Challenge 2: Unique Characters

Write a function that takes two strings and returns:
- Characters in **BOTH**
- Characters in first but **NOT** second
- Characters in either but **NOT** both

Use **SET operations**.

Example: `"hello"`, `"world"` → Common: `{'l', 'o'}`

---

## Challenge 3: Word Frequency Analyzer

Write `analyze(text)` returning a dict with:
- `"word_count"`: total words
- `"unique_words"`: unique word count
- `"most_common"`: most frequent word
- `"frequencies"`: word → count dict

Make it case-insensitive.

---

## Challenge 4: Matrix Operations

Given a 2D list, write:
- `matrix_sum(m)` — sum of all elements
- `row_sums(m)` — list of each row's sum
- `col_sums(m)` — list of each column's sum
- `diagonal_sum(m)` — sum of main diagonal

Test with: `[[1,2,3],[4,5,6],[7,8,9]]`

---

## Challenge 5: Mini Contact Book

Build an interactive contact book with a while loop menu:
1. Add contact (name → phone)
2. Search contact
3. Delete contact
4. List all contacts
5. Quit

---

## Challenge 6: DSA Warm-up Problems

These are simplified LeetCode problems:

**A) Contains Duplicate:** `[1, 2, 3, 1]` → `True`

**B) Single Number:** Every number appears twice except one. Find it.
`[4, 1, 2, 1, 2]` → `4`

**C) Valid Anagram:** `"anagram"`, `"nagaram"` → `True`

**D) Intersection of Two Arrays:** `[1, 2, 2, 1]`, `[2, 2]` → `[2]`

---

## Graduation Check

You're ready for DSA (`amazon-dsa-prep/`) if you can:

- ✓ Write functions with parameters and return values
- ✓ Use dictionaries for counting and lookup
- ✓ Use sets for uniqueness and fast membership checks
- ✓ Loop through lists/strings/dicts comfortably
- ✓ Use list comprehensions
- ✓ Combine data structures (dict of lists, list of tuples)

**If YES → Start with `amazon-dsa-prep/01_hashmap.py`**
