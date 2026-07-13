# Day 2: Unpacking, *args, and **kwargs

**Time:** ~40 minutes

Today you learn:
1. Unpacking lists and tuples
2. `*args`
3. `**kwargs`
4. When to avoid being too clever

**Practice file:** Create `day2_practice.py`

---

## Part 1: Unpacking

```python
point = (3, 4)
x, y = point

print(x)
print(y)
```

The number of variables must match the number of values.

---

## Part 2: Star Unpacking

```python
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers

print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

---

## Part 3: *args

`*args` collects extra positional arguments into a tuple.

```python
def total(*numbers):
    answer = 0
    for number in numbers:
        answer += number
    return answer


print(total(1, 2, 3))
```

### 🧩 The `*` is a "scoop them all up" symbol

Normally a function has a fixed number of slots: `def add(a, b)` takes exactly two. But `*numbers` says *"I don't know how many they'll pass — scoop ALL of them into one tuple called `numbers`."*

```python
total(1, 2, 3)        # numbers becomes (1, 2, 3)
total(5, 10)          # numbers becomes (5, 10)
total(7)              # numbers becomes (7,)
total()               # numbers becomes ()  — empty, still works
```

Inside the function `numbers` is just a normal tuple you loop over. Trace `total(1, 2, 3)`:

| Loop | `number` | `answer` before | `answer` after |
|------|----------|------------------|-----------------|
| 1    | 1        | 0                | 1               |
| 2    | 2        | 1                | 3               |
| 3    | 3        | 3                | 6               |

Returns `6`. The name `args` is just convention — it's the `*` that does the magic. Use it when a function should accept *any number* of inputs (like `print` does).

---

## Part 4: **kwargs

`**kwargs` collects named arguments into a dictionary.

```python
def describe_person(**info):
    for key, value in info.items():
        print(key, value)


describe_person(name="Sagar", city="New Jersey")
```

### 🧩 `**` scoops up NAMED arguments into a dict

Where `*args` catches loose values, `**kwargs` catches loose **name=value** pairs and packs them into a dictionary:

```python
describe_person(name="Sagar", city="New Jersey")
# inside, info becomes:
# {"name": "Sagar", "city": "New Jersey"}
```

So the keyword you type on the way in becomes a **key**, and its value becomes the **value**. Then `info.items()` just loops that dict:

```
name Sagar
city New Jersey
```

Quick side-by-side:

| Symbol | Catches | Packs into |
|--------|---------|------------|
| `*args` | extra plain values: `f(1, 2, 3)` | a **tuple** |
| `**kwargs` | extra named values: `f(a=1, b=2)` | a **dict** |

Memory hook: one star = a list-like scoop, two stars = a dict-like scoop (two stars for the two parts of a key–value pair).

---

## Part 5: Keep It Readable

`*args` and `**kwargs` are powerful, but regular parameters are clearer when you
already know exactly what the function needs.

---

## Exercises

**Exercise 1:** Unpack `(name, age, city)` into three variables.

**Exercise 2:** Write `multiply_all(*numbers)`.

**Exercise 3:** Write `print_profile(**info)`.

**Exercise 4:** Use star unpacking to get first, middle, and last values.

