# Day 2: Big O — Measuring Algorithm Speed

**Time:** ~35 minutes

Today you learn:
1. Why we measure algorithms
2. `O(1)`, `O(n)`, `O(n²)`, and `O(log n)`
3. Basic space complexity

**Practice file:** Create `day2_practice.py`

---

## Part 1: Big O Measures Growth

Big O describes how work grows when the input grows.
It does not measure exact seconds.

If a list doubles in size, how much more work is needed?

### 🧩 The "finding a name in a phone book" analogy

Big O is just answering: *"if the input gets 10× bigger, does my work get 10× bigger? 100×? barely change?"* Picture searching a phone book with `n` names:

| Big O | Nickname | Phone-book version | If input doubles... |
|-------|----------|--------------------|----------------------|
| `O(1)` | constant | flip straight to page 1 | work stays the same |
| `O(log n)` | logarithmic | open the middle, throw away half, repeat | work grows by just **one** step |
| `O(n)` | linear | read every name top to bottom | work **doubles** |
| `O(n²)` | quadratic | compare every name with every other name | work **quadruples** |

The whole point: we care about the *shape of the growth*, not the exact time. A slow-growing curve wins on big inputs even if it's clumsier on tiny ones. Lower on this table = faster as data grows.

---

## Part 2: O(1) — Constant Time

The work does not grow with the list.

```python
def first_item(items):
    return items[0]
```

Whether the list has 5 or 5 million values, one position is accessed.

---

## Part 3: O(n) — Linear Time

The algorithm may inspect every value once.

```python
def contains(items, target):
    for item in items:
        if item == target:
            return True
    return False
```

For `n` items, up to `n` checks are made.

---

## Part 4: O(n²) — Quadratic Time

A nested loop often creates quadratic work.

```python
def print_pairs(items):
    for first in items:
        for second in items:
            print(first, second)
```

If there are 10 items, this prints 100 pairs.
If there are 100 items, this prints 10,000 pairs.

---

## Part 5: O(log n) — Cut the Work in Half

Binary search repeatedly removes half of the remaining possibilities.

```text
16 values → 8 → 4 → 2 → 1
```

This is much faster than checking all 16 one by one.

---

## Part 6: Ignore Constants

These are both `O(n)`:

```python
for item in items:
    print(item)

for item in items:
    print(item)
    print(item)
```

The second does more exact work, but both grow linearly.

---

## Part 7: Space Complexity

Space complexity measures extra memory.

```python
def double_values(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result
```

`result` grows with the input, so extra space is `O(n)`.

```python
def total(numbers):
    answer = 0
    for number in numbers:
        answer += number
    return answer
```

Only one extra variable is used, so extra space is `O(1)`.

---

## Exercises

State the time complexity and explain why:

1. Returning the last item in a list
2. Printing every item
3. Comparing every item with every other item
4. Building a new list containing every doubled value
5. Two separate loops over the same list

