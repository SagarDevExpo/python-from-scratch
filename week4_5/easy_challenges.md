# Weeks 4-5: Easy Coding Challenges

Bridge from Python basics → DSA thinking.
Solve 2-3 per day. No new concepts — just practice **THINKING**.

**Practice file:** Create `easy_practice.py` and solve each one.

---

## 1. Reverse Words
Reverse the order of words in a sentence (not the characters).
`"Hello World Python"` → `"Python World Hello"`

Tools: split, join, slicing

---

## 2. Count Vowels and Consonants
Given a string, return a dict with counts of vowels and consonants (ignore non-letters).
`"Hello World!"` → `{"vowels": 3, "consonants": 7}`

---

## 3. Remove Duplicates Keep Order
`[4, 2, 7, 2, 1, 4, 7]` → `[4, 2, 7, 1]`
Hint: Use a set to track seen items, build a new list.

---

## 4. Caesar Cipher
Shift each letter by n positions. Wrap around (z+1 = a). Leave non-letters unchanged.
`encrypt("hello", 3)` → `"khoor"`
`encrypt("xyz", 3)` → `"abc"`
Hint: `ord('a')=97`, `chr(97)='a'`, modulo 26 for wrapping.

---

## 5. Flatten a 2D List
`[[1, 2], [3, 4], [5, 6]]` → `[1, 2, 3, 4, 5, 6]`

---

## 6. Most Common Element
`[1, 3, 2, 1, 4, 1, 3]` → `1`

---

## 7. Valid Palindrome
Ignore non-alphanumeric and case.
`"A man, a plan, a canal: Panama"` → `True`
Hint: Clean the string first (remove non-alnum, lowercase).

---

## 8. Second Largest
Find second largest **WITHOUT** sort(). One pass.
`[3, 1, 4, 1, 5, 9, 2, 6]` → `6`
`[10, 10, 10]` → `None`
Hint: Track both `largest` and `second_largest`.

---

## 9. Merge Two Sorted Lists
Given two sorted lists, merge into one sorted list. **Don't use sort().**
`[1, 3, 5]`, `[2, 4, 6]` → `[1, 2, 3, 4, 5, 6]`
Hint: Two pointers, compare and pick smaller.

---

## 10. Group By First Letter
`["apple", "banana", "avocado", "blueberry", "cherry"]`
→ `{'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}`

---

## 11. Run-Length Encoding
`"aaabbbccca"` → `"a3b3c3a1"`

---

## 12. Matrix Transpose
Swap rows and columns.
`[[1,2,3],[4,5,6]]` → `[[1,4],[2,5],[3,6]]`

---

## 13. Is Subsequence
Check if s appears in t in order (not necessarily consecutive).
`s="abc"`, `t="ahbgdc"` → `True`
Hint: Two pointers.

---

## 14. Pascal's Triangle
Generate first n rows:
```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

---

## 15. Spiral Print
Print a matrix in spiral order (right → down → left → up → repeat).
`[[1,2,3],[4,5,6],[7,8,9]]` → `[1, 2, 3, 6, 9, 8, 7, 4, 5]`
This is LeetCode 54!
