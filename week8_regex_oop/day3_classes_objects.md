# Day 3: Classes and Objects

**Time:** ~45 minutes

Today you learn:
1. Classes
2. Objects
3. `__init__`
4. Instance methods

**Practice file:** Create `day3_practice.py`

---

## Part 1: Why Classes?

A class lets you group data and behavior together.

Instead of this:

```python
student = {"name": "Sagar", "house": "Python"}
```

You can create a `Student` object.

---

## Part 2: Create a Class

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


student = Student("Sagar", "Python")
print(student.name)
print(student.house)
```

`__init__` runs when a new object is created.

`self` means “this object.”

### 🏭 The cookie-cutter mental model (read this slowly)

- A **class** is a **cookie cutter** — a blueprint. It's not a cookie itself; it just describes what cookies look like.
- An **object** is an actual **cookie** you stamp out with that cutter. You can make many.

```python
class Student:      # the cookie cutter (blueprint)
    ...

student = Student("Sagar", "Python")   # one real cookie
alice   = Student("Alice", "Data")     # another real cookie, separate data
```

### 🧩 What happens, step by step, on `Student("Sagar", "Python")`

1. Python makes a fresh, empty object (a blank cookie).
2. It automatically calls `__init__`, passing that new blank object in as **`self`**, plus your arguments: `name="Sagar"`, `house="Python"`.
3. Inside `__init__`:
   - `self.name = name` means *"on THIS object, store the name 'Sagar'."*
   - `self.house = house` means *"on THIS object, store the house 'Python'."*
4. The finished object is handed back and saved in the variable `student`.

Now `student.name` reads the `name` you attached → `"Sagar"`.

### 🧩 The one thing everyone trips on: `self`

`self` is just **"the specific object this line is working on right now."** It's how each cookie keeps *its own* data separate:

```python
sagar = Student("Sagar", "Python")
alice = Student("Alice", "Data")

print(sagar.name)   # "Sagar"  — self was the sagar object
print(alice.name)   # "Alice"  — self was the alice object
```

Even though both objects came from the same class, `self.name` points to a *different* stored value for each. You never type `self` when *calling* — `Student("Sagar", "Python")` has no `self` — Python fills it in for you automatically. You only write `self` when *defining* the methods.

---

## Part 3: Instance Methods

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def introduce(self):
        return f"I'm {self.name} from {self.house}"


student = Student("Sagar", "Python")
print(student.introduce())
```

Methods are functions that belong to an object.

### 🧩 How `student.introduce()` finds the name

A **method** is just a function that lives inside a class and automatically receives the object as `self`.

When you write `student.introduce()`:
1. Python sees you called `introduce` *on* the `student` object.
2. It secretly passes `student` in as `self` (that's why the method is defined as `introduce(self)` but you call it with empty `()`).
3. Inside, `self.name` looks up the `name` stored *on that object* → `"Sagar"`, and `self.house` → `"Python"`.
4. Returns `"I'm Sagar from Python"`.

So `self` is the bridge that lets a method reach the object's own stored data. Call `alice.introduce()` instead and the exact same code reads Alice's data — because now `self` *is* alice.

---

## Part 4: __str__

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


student = Student("Sagar", "Python")
print(student)
```

`__str__` controls how the object prints.

---

## Exercises

**Exercise 1:** Create a `Book` class with `title`, `author`, and `pages`.

**Exercise 2:** Add a method `summary()` to `Book`.

**Exercise 3:** Add `__str__` to `Book`.

**Exercise 4:** Create three book objects and store them in a list.

