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

---

## Part 4: **kwargs

`**kwargs` collects named arguments into a dictionary.

```python
def describe_person(**info):
    for key, value in info.items():
        print(key, value)


describe_person(name="Sagar", city="New Jersey")
```

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

