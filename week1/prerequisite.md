# Week 1 Prerequisites: Thinking Before Syntax

Before starting Week 1, focus on these ideas. They are not extra lessons to memorize. They are mental handles that make the daily exercises easier to reason about.

## 1. A program runs top to bottom

Python reads your code one line at a time, from top to bottom, unless a condition changes the path.

When confused, trace like this:

```text
Line 1 happens.
Then line 2 happens.
Then line 3 happens.
What value does each variable have right now?
```

This habit matters more than speed.

## 2. Variables are labels, not boxes forever

A variable name points to the current value you assigned.

```python
age = 25
age = 26
```

After the second line, `age` means `26`. The old value is gone unless you saved it somewhere else.

Ask yourself:

```text
What does this variable mean at this exact line?
```

## 3. Types decide what operations make sense

The same symbol can behave differently depending on the type.

```python
2 + 3        # math addition
"2" + "3"    # string joining
```

Before using a value, ask:

```text
Is this text, a whole number, a decimal, or True/False?
```

This is especially important with `input()`, because user input starts as text.

## 4. Boolean questions produce `True` or `False`

Conditions are questions.

```python
age >= 18
password == "secret"
```

Each question becomes either `True` or `False`. An `if` statement simply decides what to do with that answer.

## 5. Separate "calculate" from "display"

Try to avoid doing everything inside `print()`.

Clear thinking often looks like:

```python
total = price * quantity
print(total)
```

This makes debugging easier because you can inspect the middle value.

## 6. Read conditions in plain English

Translate code into words:

```python
if temp <= 15:
```

means:

```text
If the temperature is 15 or lower...
```

If you cannot say the condition in plain English, pause and simplify it.

## 7. One decision chain chooses one path

An `if / elif / else` chain picks the first matching branch and skips the rest.

Separate `if` statements are independent checks.

Ask:

```text
Do I want only one result, or can multiple things be true?
```

Use an `if / elif / else` chain for one result. Use separate `if` statements when several labels can apply.

## 8. Common beginner traps to watch for

- `=` assigns a value.
- `==` compares two values.
- `input()` gives a string.
- Empty strings are falsy.
- `not` flips truthiness.
- `is None` is for checking absence of a value, not empty user input.

## 9. Practice question before each exercise

Before coding, write one sentence:

```text
The input is ___.
The output should be ___.
The rule is ___.
```

That tiny pause trains the problem-solving part of your brain.
