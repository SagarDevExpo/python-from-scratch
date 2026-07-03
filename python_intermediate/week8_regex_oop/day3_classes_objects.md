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

