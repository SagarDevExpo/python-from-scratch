# Day 2: Linked Lists — Values Connected by Links

**Time:** ~40 minutes

Today you learn:
1. Nodes and `next`
2. The head of a linked list
3. Traversing one node at a time

**Practice file:** Create `day2_practice.py`

---

## Part 1: A Node

Unlike a Python list, linked-list values do not use numbered positions.
Each node stores a value and a link to the next node.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

Connect nodes:

```python
first = Node(10)
second = Node(20)
third = Node(30)

first.next = second
second.next = third

head = first
```

Visual:

```text
head → [10] → [20] → [30] → None
```

---

## Part 2: Traverse

```python
def print_list(head):
    current = head

    while current is not None:
        print(current.value)
        current = current.next
```

Never forget `current = current.next`, or the loop stays on one node forever.

---

## Part 3: Search

```python
def contains(head, target):
    current = head

    while current:
        if current.value == target:
            return True
        current = current.next

    return False
```

Searching is `O(n)`. A linked list cannot jump directly to index 100.

---

## Exercises

1. Build `5 → 10 → 15 → None`.
2. Print every value.
3. Count the nodes.
4. Return the final node's value.

