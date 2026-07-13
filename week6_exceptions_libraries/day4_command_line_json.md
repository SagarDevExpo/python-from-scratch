# Day 4: Command-Line Arguments and JSON

**Time:** ~40 minutes

Today you learn:
1. `sys.argv`
2. Exiting early with `sys.exit`
3. JSON basics
4. Reading API-like data
5. Fetching live data from an API with `requests`

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

### 🧩 Picture `sys.argv` as a list of words

When you type `python3 greet.py Sagar hello`, Python chops that command into a **list of strings** and hands it to you as `sys.argv`:

```
command:   python3   greet.py   Sagar   hello
                        │          │       │
sys.argv = [ "greet.py" ,  "Sagar" , "hello" ]
index:          0            1          2
```

Notice `sys.argv[0]` is always the **script name itself**, not your first input. That's why *your* first real argument is at index **1**, not 0. Everything in the list is a **string** — even numbers, so `"5"` needs `int("5")` before math.

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

### 🔄 `loads` vs `dumps` — which direction?

The two names look almost identical, so lock in the direction. Think of JSON text as being "outside" (a string, e.g. from a file or the internet) and a Python dict as being "inside" your program:

| Function | Direction | Turns... | ...into |
|----------|-----------|----------|---------|
| `json.loads(text)` | **load IN** | a JSON **s**tring | a Python dict |
| `json.dumps(data)` | **dump OUT** | a Python dict | a JSON **s**tring |

Memory hook: the **`s`** on the end = **"string"**. `loads` = "load *from* a string." `dumps` = "dump *to* a string." If you're reading data someone gave you → `loads`. If you're preparing data to save or send → `dumps`.

---

## Part 5: Fetching Live Data with `requests`

So far the JSON came from a string *you* wrote. In the real world, JSON usually arrives from the **internet** — from an API (a web address that returns data instead of a web page). The third-party `requests` library (from Day 3) fetches it.

```bash
pip install requests        # once, in your terminal (needs internet)
```

```python
import requests

response = requests.get("https://api.github.com/users/octocat")
data = response.json()      # parse the JSON body into a Python dict

print(data["name"])         # Octocat
print(data["public_repos"]) # some number
```

### 🧩 What actually happens, step by step

1. `requests.get(url)` sends a request over the internet and waits for the server to answer. The answer comes back as a `response` object.
2. `response.json()` reads the JSON text in that answer and **turns it into a Python dict** — it's basically `json.loads(response.text)` done for you.
3. From there it's just dictionary access (`data["name"]`) — exactly the skill from Part 3.

```
  your code ──get()──→ [ API server ]
            ←─JSON text──
  response.json() → Python dict → data["name"]
```

### 🛡️ Check it worked (APIs can fail)

The network is unreliable, so real code checks the **status code** before trusting the data. `200` means OK:

```python
response = requests.get("https://api.github.com/users/octocat")

if response.status_code == 200:
    data = response.json()
    print(data["name"])
else:
    print("Request failed:", response.status_code)
```

> ⚠️ This part needs `pip install requests` **and** an internet connection. If you're offline, just read it — the JSON parsing you learned in Parts 3-4 is the same skill; `requests` only changes *where the JSON comes from*.

---

## Exercises

**Exercise 1:** Create `hello.py` that accepts one command-line name.

**Exercise 2:** Create `add.py` that accepts two numbers and prints their sum.

**Exercise 3:** Parse this JSON string and print each course:

```python
'{"courses": ["Python", "DSA", "SQL"]}'
```

**Exercise 4:** Create a dictionary and print it as formatted JSON.

**Exercise 5:** Using `requests`, fetch `https://api.github.com/users/octocat` and print the user's `name` and `public_repos`. Check `response.status_code == 200` first, and print an error message if the request fails. *(Needs internet + `pip install requests`.)*

