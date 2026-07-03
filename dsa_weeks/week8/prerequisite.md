# Week 8 Prerequisites: Pointers, Links, and Recursive Shape

Week 8 introduces problems where the path matters: recursion, linked lists, and two pointers.

## 1. Recursion needs two promises

Every recursive function needs:

```text
Base case: when to stop.
Recursive step: how the problem gets smaller.
```

Before coding recursion, write those in comments.

If the problem does not get smaller, recursion will not stop.

## 2. Trust the smaller problem

Recursive thinking feels strange because you do not manually trace every call forever.

Ask:

```text
If the function already works for the smaller input, how do I use that answer?
```

That is the core move.

## 3. Linked lists are not index-based

With a normal list, you can jump to an index.

With a linked list, you move from node to node:

```text
current -> current.next -> current.next
```

So the main variable is usually:

```python
current
```

Ask:

```text
Where is current now?
Where should it move next?
```

## 4. Links must be saved before changing them

When reversing or deleting linked-list nodes, changing `.next` can disconnect the rest of the list.

Mental safety rule:

```text
Save what you still need before rewiring a link.
```

Common names:

```python
prev
current
next_node
```

## 5. Two pointers are controlled movement

Two-pointer problems are not about having two variables randomly. Each pointer has a job.

Before coding, decide:

```text
Where does left start?
Where does right start?
When does left move?
When does right move?
When do we stop?
```

## 6. Sorted data gives direction

In pair-sum problems, sorted data tells you how to move.

If the sum is too small, move the left pointer right.
If the sum is too large, move the right pointer left.

That works because moving in a sorted list has predictable meaning.

## 7. Draw tiny diagrams

For linked lists and pointers, draw:

```text
1 -> 2 -> 3 -> None
```

Then mark:

```text
prev
current
next_node
```

This is not childish. It is exactly how experienced engineers reason about pointer changes.

## 8. Week 8 thinking habit

At each step, ask:

```text
What is the current position?
What information must I not lose?
What gets smaller or moves forward?
```
