# Day 3: Strings — Text Manipulation

**Time:** ~30 minutes

Today you learn:
1. Strings are sequences of characters
2. Indexing and slicing
3. Common string methods
4. String iteration patterns (used heavily in DSA!)

**Practice file:** Create `day3_practice.py`

---

## Part 1: String indexing — Access individual characters

```python
s = "PYTHON"
#    P  Y  T  H  O  N
#    0  1  2  3  4  5    (index from left)
#   -6 -5 -4 -3 -2 -1   (index from right)

print(s[0])    # P  (first character)
print(s[5])    # N  (last character)
print(s[-1])   # N  (last character — easier!)
print(s[-2])   # O  (second to last)
```

> Strings are **IMMUTABLE** — you can't change individual characters.
> `s[0] = "J"` → ERROR!

---

## Part 2: Slicing — Get a piece of a string

```python
s = "Hello, World!"

# s[start:end] — from start up to (but NOT including) end
print(s[0:5])     # "Hello"
print(s[7:12])    # "World"

# Shortcuts
print(s[:5])      # "Hello" (from beginning)
print(s[7:])      # "World!" (to end)
print(s[:])       # "Hello, World!" (copy entire string)

# Step
print(s[::2])     # "Hlo ol!" (every 2nd character)
print(s[::-1])    # "!dlroW ,olleH" (REVERSED! Very useful in DSA!)
```

### 🧩 How to read a slice `s[start:end]`

A slice grabs a *piece* of the string. The rule mirrors `range`: it starts **at** `start` and stops **just before** `end` (the end index is not included).

```
s = "Hello, World!"
     0123456789...

s[0:5]  → indexes 0,1,2,3,4  → "Hello"   (index 5 NOT included)
s[7:12] → indexes 7,8,9,10,11 → "World"
```

The shortcuts just leave a side blank: `s[:5]` = "from the start to 5", `s[7:]` = "from 7 to the end".

**The famous one — `s[::-1]` reverses:** the three slots are `[start:end:step]`. A `step` of `-1` means *"walk backwards one at a time,"* so it reads the whole string end-to-front. That's the go-to trick for reversing and palindrome checks:

```python
original = "racecar"
print(original == original[::-1])   # True — same forwards and backwards
```

---

## Part 3: Common string methods

```python
text = "  Hello, World!  "

# Case
print(text.upper())          # "  HELLO, WORLD!  "
print(text.lower())          # "  hello, world!  "
print("hello".capitalize())  # "Hello"

# Whitespace
print(text.strip())    # "Hello, World!" (remove spaces from edges)

# Find and check
print("World" in text)        # True
print(text.find("World"))     # 9 (index where "World" starts)
print(text.find("xyz"))       # -1 (not found)
print(text.count("l"))        # 3

# Replace
print(text.replace("World", "Python"))

# Split and join
sentence = "Python is awesome"
words = sentence.split(" ")     # ["Python", "is", "awesome"]
rejoined = "-".join(words)      # "Python-is-awesome"
```

---

## Part 4: Character checking methods

```python
print("abc".isalpha())     # True (all letters)
print("123".isdigit())     # True (all digits)
print("abc123".isalnum())  # True (letters or digits)
print("ABC".isupper())     # True
print("abc".islower())     # True
```

---

## Part 5: String patterns for DSA

```python
# PATTERN 1: Loop through each character
for char in "hello":
    print(char, end=" ")

# PATTERN 2: Count character frequencies (EXTREMELY common!)
text = "banana"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(f"Frequencies: {freq}")  # {'b': 1, 'a': 3, 'n': 2}

# PATTERN 3: ASCII values
print(ord('a'))   # 97
print(ord('z'))   # 122
print(chr(97))    # 'a'

# PATTERN 4: Build a new string character by character
original = "Hello World"
no_spaces = ""
for char in original:
    if char != " ":
        no_spaces += char
print(no_spaces)  # "HelloWorld"
```

---

## Exercises

**Exercise 1:** Ask for a word. Print it reversed.
Then check if it's a palindrome.
Test with: `"racecar"` (yes), `"hello"` (no), `"madam"` (yes)

**Exercise 2:** Count how many uppercase, lowercase, digits, and
spaces are in: `"Hello World 123"`

**Exercise 3:** Given `"the quick brown fox jumps over the lazy dog"`,
split into words, then print only words with more than 3 letters.

**Exercise 4:** Replace all vowels with `*` in a string.
`"programming"` → `"pr*gr*mm*ng"`

**Exercise 5:** Check if two strings are anagrams (same letters, different order). Case-insensitive.
`"Listen"` and `"Silent"` → `True`
Hint: `sorted("abc")` → `['a', 'b', 'c']`
