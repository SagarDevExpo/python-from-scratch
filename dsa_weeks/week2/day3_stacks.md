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

### 🧩 The idea before the trace

When you see an **opening** bracket, you push it — "here's something that still needs closing." When you see a **closing** bracket, the most recent opener *must* be its match (that's why a stack: last opened = first that should close). `pairs` maps each closer to the opener it expects.

Trace `is_valid("([])")`. `stack` starts empty `[]`.

| Char | Opening or closing? | Action | `stack` after |
|------|---------------------|--------|----------------|
| `(`  | opening             | push it | `['(']` |
| `[`  | opening             | push it | `['(', '[']` |
| `]`  | closing             | pop `'['`; does it match `pairs[']']='['`? ✅ yes | `['(']` |
| `)`  | closing             | pop `'('`; does it match `pairs[')']='('`? ✅ yes | `[]` |

Loop ends, `stack` is empty → `return len(stack) == 0` is `True`. ✅ Balanced!

Now trace a **broken** one, `is_valid("([)]")`:

| Char | Action | `stack` after |
|------|--------|----------------|
| `(`  | push | `['(']` |
| `[`  | push | `['(', '[']` |
| `)`  | pop `'['`; but `pairs[')']='('` — `'['` ≠ `'('` ❌ | — `return False` 🛑 |

The mismatch is caught instantly. And `not stack` guards the case where a closer appears with nothing to match (like `")"` on its own).

---

## Exercises

1. Reverse a list using a stack.
2. Test Valid Parentheses with `"()[]{}"`, `"([)]"`, and `"((("`.
3. Simulate browser back history.
4. Explain why `pop(0)` is not used for a stack.

