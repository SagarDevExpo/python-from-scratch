"""
WEEKS 4-5: Easy Coding Challenges
Bridge from Python basics → DSA thinking

These are real-world-ish problems that use your Python skills.
Solve 2-3 per day. No new concepts — just practice THINKING.

Each problem says what tools you need (loops, dicts, sets, etc.)

Run: python3 easy_challenges.py
"""


# ============================================================
# 1. Reverse Words (tools: split, join, slicing)
# ============================================================

"""
Reverse the order of words in a sentence (not the characters).
"Hello World Python" → "Python World Hello"

Write a function: reverse_words(sentence) → string
"""

# Your code:




# ============================================================
# 2. Count Vowels and Consonants (tools: loops, if, sets)
# ============================================================

"""
Given a string, return a dict with counts of vowels and consonants.
Ignore non-letter characters.

"Hello World!" → {"vowels": 3, "consonants": 7}

Write a function: count_vc(text) → dict
"""

# Your code:




# ============================================================
# 3. Remove Duplicates Keep Order (tools: sets, lists)
# ============================================================

"""
Remove duplicates from a list while keeping the original order.
[4, 2, 7, 2, 1, 4, 7] → [4, 2, 7, 1]

Note: set() removes duplicates but loses order!
Hint: Use a set to track seen items, build a new list.

Write a function: remove_dupes(lst) → list
"""

# Your code:




# ============================================================
# 4. Caesar Cipher (tools: ord, chr, modulo)
# ============================================================

"""
Shift each letter by n positions. Wrap around (z+1 = a).
Only shift letters, leave everything else unchanged.

encrypt("hello", 3) → "khoor"
encrypt("xyz", 3) → "abc"
encrypt("Hello, World!", 5) → "Mjqqt, Btwqi!"

Hint: ord('a')=97, chr(97)='a'. Use modulo 26 for wrapping.

Write: encrypt(text, shift) → string
"""

# Your code:




# ============================================================
# 5. Flatten a 2D List (tools: nested loops)
# ============================================================

"""
Convert a list of lists into a single flat list.
[[1, 2], [3, 4], [5, 6]] → [1, 2, 3, 4, 5, 6]
[[1], [2, 3, 4], [5]] → [1, 2, 3, 4, 5]

Write a function: flatten(lst) → list
"""

# Your code:




# ============================================================
# 6. Most Common Element (tools: dict counting)
# ============================================================

"""
Find the element that appears most often in a list.
If there's a tie, return any one of them.

[1, 3, 2, 1, 4, 1, 3] → 1

Write a function: most_common(lst) → element
"""

# Your code:




# ============================================================
# 7. Valid Palindrome (tools: strings, two-pointer)
# ============================================================

"""
Check if a string is a palindrome, ignoring non-alphanumeric
characters and case.

"A man, a plan, a canal: Panama" → True
"race a car" → False
"" → True

Write a function: is_palindrome(s) → bool
Hint: Clean the string first (remove non-alnum, lowercase).
"""

# Your code:




# ============================================================
# 8. Second Largest (tools: loops, comparisons)
# ============================================================

"""
Find the second largest number in a list.
Do NOT use sort() — do it in one pass.

[3, 1, 4, 1, 5, 9, 2, 6] → 6
[10, 10, 10] → None (no second largest)

Write a function: second_largest(nums) → int or None
Hint: Track both largest and second_largest variables.
"""

# Your code:




# ============================================================
# 9. Merge Two Sorted Lists (tools: two-pointer, lists)
# ============================================================

"""
Given two sorted lists, merge them into one sorted list.
Do NOT use sort() — this should be O(n).

[1, 3, 5], [2, 4, 6] → [1, 2, 3, 4, 5, 6]
[1, 1, 2], [1, 3, 4] → [1, 1, 1, 2, 3, 4]

Write a function: merge_sorted(a, b) → list
Hint: Two pointers, one for each list. Compare and pick smaller.
"""

# Your code:




# ============================================================
# 10. Group By First Letter (tools: dicts, lists)
# ============================================================

"""
Group words by their first letter.

["apple", "banana", "avocado", "blueberry", "cherry", "apricot"]
→ {'a': ['apple', 'avocado', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

Write a function: group_by_first(words) → dict
"""

# Your code:




# ============================================================
# 11. Run-Length Encoding (tools: loops, strings)
# ============================================================

"""
Compress consecutive repeated characters.

"aaabbbccca" → "a3b3c3a1"
"abcd" → "a1b1c1d1"
"aabbb" → "a2b3"

Write a function: rle_encode(s) → string
"""

# Your code:




# ============================================================
# 12. Matrix Transpose (tools: nested loops, 2D lists)
# ============================================================

"""
Transpose a matrix (swap rows and columns).

[[1, 2, 3],    →    [[1, 4],
 [4, 5, 6]]          [2, 5],
                      [3, 6]]

Write a function: transpose(matrix) → list of lists
Hint: result[j][i] = matrix[i][j]
"""

# Your code:




# ============================================================
# 13. Is Subsequence (tools: two-pointer)
# ============================================================

"""
Check if string s is a subsequence of string t.
(Characters of s appear in t in the same order, but not necessarily
consecutively.)

s="abc", t="ahbgdc" → True (a...b...c)
s="axc", t="ahbgdc" → False

Write a function: is_subsequence(s, t) → bool
Hint: Two pointers — one for s, one for t.
"""

# Your code:




# ============================================================
# 14. Pascal's Triangle (tools: lists, loops)
# ============================================================

"""
Generate the first n rows of Pascal's triangle.

n=5:
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]

Each number = sum of the two numbers above it.

Write a function: pascals_triangle(n) → list of lists
"""

# Your code:




# ============================================================
# 15. Spiral Print (tools: 2D lists, tricky loops)
# ============================================================

"""
Print a matrix in spiral order (right → down → left → up → repeat).

[[1,  2,  3],
 [4,  5,  6],
 [7,  8,  9]]

→ [1, 2, 3, 6, 9, 8, 7, 4, 5]

Write a function: spiral_order(matrix) → list
Hint: Track top/bottom/left/right boundaries, shrink inward.
This is a real LeetCode problem! (LC 54)
"""

# Your code:

