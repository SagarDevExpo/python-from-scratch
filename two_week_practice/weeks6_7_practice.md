# Weeks 6-7 Practice: DSA Basics, Arrays, Searching, Hash Maps, Stacks, Queues

**Time:** 60-75 minutes

**Practice file:** Create `weeks6_7_review.py`

This review is about recognizing when simple loops are enough and when remembering previous information helps.

---

## Warm-Up: Complexity Guess

For each, write the Big O:

1. Read `numbers[0]`.
2. Loop once through a list.
3. Nested loop over the same list.
4. Binary search in a sorted list.
5. Check `target in seen_set`.

---

## Challenge 1: Smallest and Largest

Write one function:

```python
min_max(numbers)
```

Return both the smallest and largest number without using `min()` or `max()`.

Pattern focus: two best-so-far trackers.

---

## Challenge 2: Prefix Sums

Given:

```python
nums = [3, 1, 4, 2]
```

Build:

```python
[3, 4, 8, 10]
```

Then answer:

```text
What is the sum from index 1 to index 3?
```

Pattern focus: running total and range-sum thinking.

---

## Challenge 3: Linear Search Details

Write:

```python
find_all_positions(nums, target)
```

Example:

```python
find_all_positions([4, 2, 4, 3, 4], 4)
```

Expected:

```python
[0, 2, 4]
```

Pattern focus: indexes, not just values.

---

## Challenge 4: Binary Search From Memory

Write binary search for a sorted list.

Return the index if found, otherwise `-1`.

Test:

```python
[1, 3, 5, 7, 9, 11], target = 7
[1, 3, 5, 7, 9, 11], target = 8
[]
```

Pattern focus: `left`, `right`, `mid`.

---

## Challenge 5: Contains Duplicate

Write:

```python
contains_duplicate(nums)
```

Use a set.

Pattern focus: "have I seen this before?"

---

## Challenge 6: First Unique Character

Write:

```python
first_unique_index(text)
```

Example:

```python
first_unique_index("loveleetcode") -> 2
```

Pattern focus: frequency dictionary, then second pass.

---

## Challenge 7: Two Sum With Hash Map

Return the two values that add to target.

Example:

```python
nums = [2, 7, 11, 15]
target = 9
```

Expected:

```text
2 + 7 = 9
```

Pattern focus: complement lookup.

---

## Challenge 8: Valid Parentheses

Check whether a string of brackets is valid.

Examples:

```python
"()[]{}" -> True
"([)]" -> False
"({[]})" -> True
```

Pattern focus: stack for most recent opening bracket.

---

## Challenge 9: Queue Simulation

Create a support ticket queue.

Functions:

- `add_ticket(queue, ticket)`
- `serve_ticket(queue)`
- `show_queue(queue)`

Pattern focus: first-in, first-out.

---

## Challenge 10: Choose the Tool

For each, write list, dict, set, stack, or queue:

1. Count word frequency.
2. Remove duplicates.
3. Reverse the most recent actions.
4. Process customers in arrival order.
5. Store student names and scores.
6. Find whether a number was seen before.

---

## Pattern Checklist

You are ready for Week 8 if you can explain:

- why binary search needs sorted data
- why sets are faster than list scanning for membership
- what a dictionary maps in Two Sum
- why stack fits parentheses
- why queue fits arrival-order processing
