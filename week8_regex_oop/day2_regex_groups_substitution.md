# Day 2: Regex Groups, Find, Split, and Replace

**Time:** ~40 minutes

Today you learn:
1. `re.findall`
2. Capture groups
3. `re.sub`
4. `re.split`

**Practice file:** Create `day2_practice.py`

---

## Part 1: findall

```python
import re

text = "Call 123-456-7890 or 222-333-4444"
numbers = re.findall(r"\d{3}-\d{3}-\d{4}", text)

print(numbers)
```

`{3}` means exactly three times.

---

## Part 2: Capture Groups

```python
import re

name = "Nagireddi, Sagar"
match = re.search(r"^(.+), (.+)$", name)

if match:
    last = match.group(1)
    first = match.group(2)
    print(first, last)
```

Parentheses capture parts of a match.

### 🧩 Groups = labelled buckets you pull out later

Parentheses `( )` don't change *what* matches — they just say *"remember this piece separately so I can grab it."* Each pair of parens becomes a numbered bucket.

Matching `"Nagireddi, Sagar"` against `^(.+), (.+)$`:

```
^ (.+) ,  (.+) $
   │        │
   │        └─ group 2 → "Sagar"   (everything after the comma+space)
   └───────── group 1 → "Nagireddi" (everything before the comma)
```

After a successful match:
- `match.group(0)` = the **whole** match: `"Nagireddi, Sagar"`
- `match.group(1)` = **first** bucket: `"Nagireddi"`
- `match.group(2)` = **second** bucket: `"Sagar"`

Groups are numbered **left to right by their opening `(`**, starting at 1. This is how you pull structured pieces (last name, first name) out of one line of text and rearrange them.

---

## Part 3: Replace with re.sub

```python
import re

text = "My number is 123-456-7890"
cleaned = re.sub(r"\d", "#", text)

print(cleaned)
```

Every digit becomes `#`.

---

## Part 4: Split with Multiple Separators

```python
import re

text = "apple,banana;cherry orange"
parts = re.split(r"[,; ]+", text)

print(parts)
```

This splits on comma, semicolon, or space.

---

## Exercises

**Exercise 1:** Extract all numbers from a sentence.

**Exercise 2:** Convert `"Last, First"` into `"First Last"`.

**Exercise 3:** Replace multiple spaces with one space.

**Exercise 4:** Split a line of text on commas or semicolons.

