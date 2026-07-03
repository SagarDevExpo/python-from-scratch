# Day 3: Stacks — Last In, First Out

**Time:** ~35 minutes

Today you learn:
1. Push, pop, and peek
2. How Python lists act as stacks
3. How stacks solve matching problems

**Practice file:** Create `day3_practice.py`

---

## Part 1: Stack Behavior

Imagine plates stacked on a table. The newest plate is removed first.

```python
stack = []

stack.append("page 1")  # push
stack.append("page 2")
stack.append("page 3")

print(stack[-1])   # peek: page 3
print(stack.pop()) # pop: page 3
```

Appending and popping from the end are `O(1)`.

---

## Part 2: Reverse with a Stack

```python
def reverse_word(word):
    stack = []

    for character in word:
        stack.append(character)

    result = ""
    while stack:
        result += stack.pop()

    return result
```

---

## Part 3: Valid Parentheses

```python
def is_valid(text):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for character in text:
        if character in "([{":
            stack.append(character)
        else:
            if not stack or stack.pop() != pairs[character]:
                return False

    return len(stack) == 0
```

The stack remembers opening brackets waiting to be closed.

---

## Exercises

1. Reverse a list using a stack.
2. Test Valid Parentheses with `"()[]{}"`, `"([)]"`, and `"((("`.
3. Simulate browser back history.
4. Explain why `pop(0)` is not used for a stack.

