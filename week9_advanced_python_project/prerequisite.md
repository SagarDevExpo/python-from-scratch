# Week 9 Prerequisites: Writing Code Others Can Read and Trust

Week 9 is about polish and scale: labeling your code so it explains itself, handling flexible inputs, producing values lazily, and organizing a real project. The theme is writing code a teammate (or future you) can pick up without pain.

## 1. Type hints are labels, not rules

A type hint documents what a function expects and returns.

```python
def greet(name: str) -> str:
```

```text
name: str -> this input should be a string
-> str    -> this function returns a string
```

Python will not enforce them, but readers and tools will thank you.

## 2. A docstring says WHAT, not every tiny step

One clear sentence beats a wall of comments.

```python
def is_even(n: int) -> bool:
    """Return True if n is even, otherwise False."""
```

Ask yourself:

```text
If someone only read this one line, would they know what the function does?
```

## 3. `*args` scoops up extra positional values

One star gathers loose values into a tuple.

```text
total(1, 2, 3) -> numbers becomes (1, 2, 3)
```

Use it when you do not know how many inputs will come.

## 4. `**kwargs` scoops up extra named values

Two stars gather `name=value` pairs into a dictionary.

```text
describe(name="Sagar", city="NJ") -> info becomes {"name": ..., "city": ...}
```

Memory hook:

```text
one star  -> list-like scoop
two stars -> dict-like scoop (two parts: key and value)
```

## 5. Prefer plain parameters when you know the inputs

`*args` and `**kwargs` are powerful but can hide what a function needs.

Ask:

```text
Do I actually need flexibility, or do I know the exact inputs?
```

If you know them, name them.

## 6. `yield` pauses; `return` ends

A generator hands out one value, then freezes and waits.

```text
return -> gives one answer, function is finished
yield  -> gives one value, function pauses and can resume
```

Mental model:

```text
Play the function one frame at a time, on demand.
```

## 7. Generators save memory for big or streamed data

Building a whole million-item list uses lots of memory. A generator produces values only when asked.

Ask:

```text
Do I need all the values at once, or one at a time?
```

## 8. A project is more than one file

Real programs split responsibilities:

```text
logic in one place
input/output at the edges
a main() entry point
tests beside the code
```

`if __name__ == "__main__":` marks the "start here" line so the file can be both run and imported.

## 9. Week 9 thinking habit

Before calling something done, ask:

```text
Would a stranger understand my function from its name, hints, and docstring?
Is each piece doing one clear job?
```
