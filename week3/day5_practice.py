"""
DAY 5: Week 3 Practice — Functions, Dicts, Sets, Comprehensions
Time: ~30 minutes

These challenges combine EVERYTHING from all 3 weeks.
If you can do these, you're ready for DSA!

Run: python3 day5_practice.py
"""

# ============================================================
# CHALLENGE 1: Inventory System
# ============================================================

"""
Build a simple inventory tracker using a dictionary.

Functions to write:
- add_item(inventory, name, quantity): add/update item
- remove_item(inventory, name): remove item (print error if not found)
- get_total(inventory): return total quantity of all items
- get_items_above(inventory, threshold): return list of item names
  with quantity above threshold

Test:
inventory = {}
add_item(inventory, "apples", 50)
add_item(inventory, "bananas", 30)
add_item(inventory, "oranges", 45)
add_item(inventory, "apples", 20)  # Should update to 70
print(get_total(inventory))  # 145
print(get_items_above(inventory, 40))  # ["apples", "oranges"]

Your code here:
"""




# ============================================================
# CHALLENGE 2: Unique Characters
# ============================================================

"""
Write a function that takes two strings and returns characters that:
a) Appear in BOTH strings
b) Appear in the first but NOT the second
c) Appear in either string but NOT both

Use SET operations.

Example: "hello", "world"
a) Common: {'l', 'o'}
b) Only in first: {'h', 'e'}
c) In one but not both: {'h', 'e', 'w', 'r', 'd'}

Your code here:
"""




# ============================================================
# CHALLENGE 3: Word Frequency Analyzer
# ============================================================

"""
Write a function `analyze(text)` that returns a dict with:
- "word_count": total number of words
- "unique_words": number of unique words
- "most_common": the most frequently used word
- "frequencies": dict of word → count

Make it case-insensitive. Ignore punctuation (just use .lower()).

Test: "The cat sat on the mat The cat is a good cat"
Expected most_common: "the" or "cat" (both appear 3 times)

Your code here:
"""




# ============================================================
# CHALLENGE 4: Matrix Operations
# ============================================================

"""
Given a 2D list (matrix), write functions:

a) matrix_sum(m) — sum of all elements
b) row_sums(m) — list of sum of each row
c) col_sums(m) — list of sum of each column
d) diagonal_sum(m) — sum of main diagonal (top-left to bottom-right)

Test with:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_sum → 45
row_sums → [6, 15, 24]
col_sums → [12, 15, 18]
diagonal_sum → 15 (1 + 5 + 9)

Your code here:
"""




# ============================================================
# CHALLENGE 5: Mini Contact Book
# ============================================================

"""
Build an interactive contact book using a dictionary.
Use a while loop with input() for the menu:

1. Add contact (name → phone)
2. Search contact (by name)
3. Delete contact
4. List all contacts
5. Quit

Handle edge cases:
- Searching/deleting non-existent contacts
- Adding a contact that already exists (ask to update)

Your code here:
"""




# ============================================================
# CHALLENGE 6: DSA Warm-up Problems
# ============================================================

"""
These are simplified versions of real LeetCode problems.
Solve them using only what you've learned in 3 weeks.

A) Contains Duplicate:
   Given a list, return True if any value appears twice.
   [1, 2, 3, 1] → True
   [1, 2, 3, 4] → False

B) Single Number:
   Every number appears twice except one. Find it.
   [4, 1, 2, 1, 2] → 4
   Hint: Count frequencies, find the one with count 1.

C) Valid Anagram:
   Return True if two strings are anagrams.
   "anagram", "nagaram" → True
   "rat", "car" → False

D) Intersection of Two Arrays:
   Return common elements (no duplicates).
   [1, 2, 2, 1], [2, 2] → [2]

Your code here:
"""




# ============================================================
# GRADUATION CHECK
# ============================================================

"""
You're ready for DSA (amazon-dsa-prep/) if you can:

✓ Write functions with parameters and return values
✓ Use dictionaries for counting and lookup
✓ Use sets for uniqueness and fast membership checks
✓ Loop through lists/strings/dicts comfortably
✓ Use list comprehensions for simple transforms
✓ Combine data structures (dict of lists, list of tuples, etc.)

If YES → Start with amazon-dsa-prep/01_hashmap.py
The 00_python_basics.py file there will now be review for you!
"""
