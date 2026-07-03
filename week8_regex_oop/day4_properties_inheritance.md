# Day 4: Properties, Class Methods, and Inheritance

**Time:** ~45 minutes

Today you learn:
1. Properties
2. `@classmethod`
3. Inheritance
4. When not to overuse classes

**Practice file:** Create `day4_practice.py`

---

## Part 1: Properties

Properties let you validate values when setting attributes.

```python
class Student:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("name cannot be empty")
        self._name = value
```

`_name` is the internal storage. `name` is the controlled public attribute.

---

## Part 2: Class Methods

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    @classmethod
    def from_string(cls, text):
        name, house = text.split(",")
        return cls(name.strip(), house.strip())


student = Student.from_string("Sagar, Python")
```

Class methods are often used as alternate constructors.

---

## Part 3: Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Dog(Animal):
    def speak(self):
        return "woof"
```

`Dog` inherits from `Animal` and customizes `speak`.

---

## Part 4: Do Not Force OOP

Use a class when data and behavior naturally belong together.

Use a function when the task is simple.

---

## Exercises

**Exercise 1:** Add validation to a `BankAccount` balance so it cannot start negative.

**Exercise 2:** Add `deposit()` and `withdraw()` methods.

**Exercise 3:** Create `SavingsAccount` that inherits from `BankAccount`.

**Exercise 4:** Write one example where a function is better than a class.

