# Day 4: Properties, Class Methods, and Inheritance

**Time:** ~45 minutes

Today you learn:
1. Properties
2. `@classmethod`
3. Inheritance
4. `@staticmethod`
5. Class vs instance variables
6. Operator overloading (`__eq__`, `__lt__`)
7. When not to overuse classes

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

### 🧩 What `class Dog(Animal)` actually gives you

The `(Animal)` part means *"Dog is a kind of Animal — start with everything Animal has, then change what's different."* Dog gets Animal's `__init__` **for free** without rewriting it:

```python
d = Dog("Rex")     # uses Animal's __init__ (Dog didn't write one)
print(d.name)      # "Rex"   ← inherited
print(d.speak())   # "woof"  ← Dog's own version
```

### 🧩 How Python decides which `speak()` to run

When you call `d.speak()`, Python searches in order:
1. **Does Dog have its own `speak`?** Yes → use it (`"woof"`). Stop looking.

But for `d.name`, it searches:
1. Does Dog define `__init__`? No.
2. Does its parent Animal? Yes → use Animal's.

This "check the child first, then fall back to the parent" search is the whole idea of inheritance. `Dog` **overrides** `speak` (replaces it) while **inheriting** `__init__` (borrows it unchanged).

```python
class Cat(Animal):
    def speak(self):
        return "meow"

for animal in [Dog("Rex"), Cat("Milo"), Animal("Thing")]:
    print(animal.speak())   # woof, meow, ...  — each uses its own version
```

---

## Part 4: Static Methods

```python
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b


print(MathHelper.add(3, 5))   # 8  — no object needed
```

### 🧩 `@staticmethod` vs the methods you already know

Compare the three method types by **what they receive automatically**:

| Kind | First arg | Can touch object data? | Use when... |
|------|-----------|------------------------|-------------|
| instance method | `self` (the object) | ✅ yes | it needs *this object's* data |
| `@classmethod` | `cls` (the class) | ❌ only class-level | it builds/returns objects (alternate constructor) |
| `@staticmethod` | *nothing special* | ❌ no | it's a plain helper that just *belongs* in the class |

A static method is really *"just a normal function parked inside a class because it's related."* It doesn't get `self` or `cls`, so it can't read any object's data — it only works with the arguments you pass it. Reach for it when a function logically belongs with the class but doesn't depend on a specific object:

```python
class Temperature:
    @staticmethod
    def c_to_f(celsius):
        return celsius * 9 / 5 + 32

print(Temperature.c_to_f(100))   # 212.0 — called on the class, no instance
```

---

## Part 5: Class vs Instance Variables

```python
class Dog:
    species = "Canis familiaris"   # CLASS variable — shared by ALL dogs

    def __init__(self, name):
        self.name = name           # INSTANCE variable — unique per dog


a = Dog("Rex")
b = Dog("Milo")
print(a.name, b.name)        # Rex Milo   — different for each
print(a.species, b.species)  # both "Canis familiaris" — shared
```

### 🧩 One copy vs one-per-object

The difference is **where the value lives**:

- **Instance variable** (`self.name`) — created inside `__init__`, lives *on each object*. Every dog gets its **own** `name`.
- **Class variable** (`species`) — defined directly in the class body, lives *on the class itself*. There's **one** copy that all objects share.

```
          class Dog
          species = "Canis familiaris"   ← ONE shared copy
         /                    \
   a: name="Rex"          b: name="Milo"   ← each has its OWN name
```

Use a **class variable** for things true of *every* instance (a species, a default rate, a shared counter). Use an **instance variable** for anything that differs per object. Careful: assigning `a.species = "X"` makes a *new instance variable on `a`* that shadows the shared one — it does not change the class copy.

---

## Part 6: Operator Overloading

You already met one dunder ("double-underscore") method: `__str__` controls how an object prints. There are more — they let your objects work with `==`, `<`, and friends.

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount   # what == means for Money

    def __lt__(self, other):
        return self.amount < other.amount    # what < means for Money


print(Money(10) == Money(10))   # True  — uses __eq__
print(Money(5) < Money(8))       # True  — uses __lt__
```

### 🧩 Dunder methods = hooks Python calls for you

When you write `a == b`, Python secretly calls `a.__eq__(b)`. When you write `a < b`, it calls `a.__lt__(b)`. By **defining** those methods, you decide what those operators *mean* for your own type:

| You write | Python calls | You define |
|-----------|--------------|------------|
| `print(obj)` | `obj.__str__()` | how it prints |
| `a == b` | `a.__eq__(b)` | when two are "equal" |
| `a < b` | `a.__lt__(b)` | sorting/ordering rule |

Why bother? Once `__lt__` exists, Python can **sort your objects** automatically:

```python
wallets = [Money(30), Money(5), Money(12)]
wallets.sort()                       # uses __lt__ under the hood
print([w.amount for w in wallets])   # [5, 12, 30]
```

Without `__lt__`, `sort()` wouldn't know how to compare two `Money` objects and would error. Dunder methods are how you make custom classes feel like built-in types.

---

## Part 7: Do Not Force OOP

Use a class when data and behavior naturally belong together.

Use a function when the task is simple.

---

## Exercises

**Exercise 1:** Add validation to a `BankAccount` balance so it cannot start negative.

**Exercise 2:** Add `deposit()` and `withdraw()` methods.

**Exercise 3:** Create `SavingsAccount` that inherits from `BankAccount`.

**Exercise 4:** Write one example where a function is better than a class.

**Exercise 5:** Give `BankAccount` an `__eq__` so two accounts with the same balance count as equal, and an `__lt__` so a list of accounts can be sorted by balance.

**Exercise 6:** Add a class variable `bank_name` shared by all accounts, and a `@staticmethod` `is_valid_amount(n)` that returns `True` only for positive numbers.

