# Day 4: Command-Line Arguments and JSON

**Time:** ~40 minutes

Today you learn:
1. `sys.argv`
2. Exiting early with `sys.exit`
3. JSON basics
4. Reading API-like data

**Practice file:** Create `day4_practice.py`

---

## Part 1: Command-Line Arguments

Command-line arguments are words typed after the file name.

```bash
python3 greet.py Sagar
```

Inside `greet.py`:

```python
import sys

print(sys.argv)
```

`sys.argv[0]` is the filename. `sys.argv[1]` is the first real argument.

---

## Part 2: Check Argument Count

```python
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python3 greet.py NAME")

name = sys.argv[1]
print("Hello,", name)
```

`sys.exit()` stops the program with a message.

---

## Part 3: JSON

JSON is a text format for storing structured data.

```python
import json

text = '{"name": "Sagar", "age": 30}'
data = json.loads(text)

print(data["name"])
```

JSON objects become Python dictionaries.

---

## Part 4: Pretty Printing JSON

```python
import json

person = {"name": "Sagar", "skills": ["Python", "DSA"]}
print(json.dumps(person, indent=2))
```

---

## Exercises

**Exercise 1:** Create `hello.py` that accepts one command-line name.

**Exercise 2:** Create `add.py` that accepts two numbers and prints their sum.

**Exercise 3:** Parse this JSON string and print each course:

```python
'{"courses": ["Python", "DSA", "SQL"]}'
```

**Exercise 4:** Create a dictionary and print it as formatted JSON.

