# Day 3: Linked-List Operations

**Time:** ~45 minutes

Today you learn:
1. Insert at the front
2. Delete a value
3. Reverse a linked list

**Practice file:** Create `day3_practice.py`

Use yesterday's `Node` class.

---

## Part 1: Insert at Front

```python
def insert_front(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node
```

This is `O(1)` because no existing nodes move.

---

## Part 2: Delete a Value

```python
def delete_value(head, target):
    if head is None:
        return None

    if head.value == target:
        return head.next

    current = head

    while current.next:
        if current.next.value == target:
            current.next = current.next.next
            return head
        current = current.next

    return head
```

We change the link so it skips the deleted node.

---

## Part 3: Reverse

Before:

```text
1 → 2 → 3 → None
```

After:

```text
3 → 2 → 1 → None
```

```python
def reverse_list(head):
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous
```

Always save `next_node` before changing `current.next`.

---

## Exercises

1. Insert three values at the front.
2. Delete the head, a middle value, and an absent value.
3. Draw every variable during one reversal.
4. Rebuild `reverse_list()` from memory.

