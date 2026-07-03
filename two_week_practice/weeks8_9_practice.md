# Weeks 8-9 Practice: Recursion, Linked Lists, Two Pointers, Trees, Graphs

**Time:** 75-90 minutes

**Practice file:** Create `weeks8_9_review.py`

This review is about movement through structures: smaller inputs, next links, two indexes, child nodes, and grid neighbors.

---

## Warm-Up: Write the State

For each pattern, write the main state variable:

1. Recursion
2. Linked-list traversal
3. Two-pointer pair search
4. Tree BFS
5. Grid DFS

Example:

```text
Linked list traversal -> current
```

---

## Challenge 1: Recursive Countdown

Write a recursive function that prints:

```text
5 4 3 2 1
```

Then stops.

Pattern focus: base case and smaller input.

---

## Challenge 2: Recursive String Reverse

Write:

```python
reverse_string(s)
```

Example:

```python
reverse_string("sagar") -> "ragas"
```

Pattern focus: use the answer from the smaller string.

---

## Challenge 3: Linked List Length

Given a simple `Node` class, write:

```python
length(head)
```

Pattern focus: move `current = current.next`.

---

## Challenge 4: Linked List Search

Write:

```python
contains(head, target)
```

Return `True` or `False`.

Pattern focus: traverse until `None`.

---

## Challenge 5: Reverse a Linked List

Reverse a linked list using:

```python
prev
current
next_node
```

Pattern focus: save the next node before changing the link.

---

## Challenge 6: Palindrome With Two Pointers

Write:

```python
is_palindrome(text)
```

Ignore case and spaces.

Use two pointers: one from the left, one from the right.

Pattern focus: compare opposite ends.

---

## Challenge 7: Pair Sum in Sorted List

Given:

```python
nums = [1, 2, 4, 6, 8, 9]
target = 10
```

Find whether any pair adds to the target using two pointers.

Pattern focus: sorted data tells pointer direction.

---

## Challenge 8: Tree Maximum Depth

Given a binary tree, return its maximum depth.

Pattern focus:

```text
1 + max(left depth, right depth)
```

---

## Challenge 9: Tree Level Order

Return values level by level using a queue.

Example:

```python
[[1], [2, 3], [4, 5]]
```

Pattern focus: BFS and queue size per level.

---

## Challenge 10: Number of Islands

Given a grid of `"1"` and `"0"`, count islands.

Pattern focus:

```text
Find land.
Start DFS/BFS.
Mark connected land visited.
Increase island count once per start.
```

---

## Pattern Checklist

You are ready for Week 10 if you can explain:

- the base case in recursion
- why linked lists use `current` instead of indexes
- when two pointers move inward
- why BFS uses a queue
- why graphs and grids need `visited`
