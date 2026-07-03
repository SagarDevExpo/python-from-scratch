# Day 5: Week 2 Practice — Loops, Strings, Lists

**Time:** ~30 minutes

Solve these using what you learned this week.
Try without looking at previous files first!

**Practice file:** Create `day5_practice.py`

---

## Challenge 1: Character Counter

Ask the user for a sentence. Print how many times each character appears (ignore spaces, case-insensitive).

Example: `"Hello World"`
```
h: 1
e: 1
l: 3
o: 2
w: 1
r: 1
d: 1
```

Hint: Convert to lowercase, loop through characters, use a dict.

---

## Challenge 2: List Rotation

Given a list and a number k, rotate the list to the right by k steps.

- `[1, 2, 3, 4, 5], k=2` → `[4, 5, 1, 2, 3]`
- `[1, 2, 3, 4, 5], k=3` → `[3, 4, 5, 1, 2]`

Hint: Use slicing! Think about where to split the list.

---

## Challenge 3: Longest Word

Given a sentence, find the longest word.
`"The quick brown fox jumped over the lazy dog"` → `"jumped"` (6 letters)

If there's a tie, return the first one found.

---

## Challenge 4: Two Sum (Simple version)

Given a list of numbers and a target, find TWO numbers that add up to the target. Print their values.

```
nums = [2, 7, 11, 15], target = 9
→ "2 + 7 = 9"
```

Use two nested loops (brute force is fine for now — you'll learn the hash map way in the DSA section!).

---

## Challenge 5: Matrix Printer

Create a 3×3 multiplication table as a 2D list, then print it.

```
1  2  3
2  4  6
3  6  9
```

Hint: A 2D list is a list of lists: `matrix = [[1, 2, 3], [4, 5, 6]]`

---

## Challenge 6: String Compression

Compress a string by counting consecutive repeated characters.

- `"aaabbbccca"` → `"a3b3c3a1"`
- `"abcd"` → `"a1b1c1d1"`

If the "compressed" string is NOT shorter, return the original.

---

## Reflection

Can you:
1. Write a for loop with range without looking anything up?
2. Loop through a string character by character?
3. Use append to build a new list?
4. Use slicing to get part of a list or string?
5. Swap two elements in a list?

All "yes"? → **Ready for Week 3 (functions + dictionaries)!**
