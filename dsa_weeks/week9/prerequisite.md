# Week 9 Prerequisites: Trees, Graphs, and Traversal

Week 9 is about connected data. The important question becomes: how do I visit everything without getting lost?

## 1. A tree is connected directionally

Think in relationships:

```text
parent
child
root
leaf
left
right
```

Do not think of a tree as a list. Think of it as nodes connected by references.

## 2. Traversal means visit in a chosen order

DFS and BFS are not random movement. They are rules for visiting.

DFS:

```text
Go deep before coming back.
```

BFS:

```text
Visit level by level.
```

Ask:

```text
Does this problem care about depth or levels?
```

## 3. Recursion naturally fits trees

A tree node often has smaller trees inside it:

```text
left subtree
right subtree
```

That makes recursion useful.

Common tree question:

```text
What should I do for this node?
What should I ask the left side?
What should I ask the right side?
```

## 4. BFS needs a queue

Level-order traversal uses a queue because the oldest waiting node should be processed first.

Mental model:

```text
Take one node out.
Add its children to the back.
Repeat.
```

## 5. Graphs may have cycles

Trees do not loop back. Graphs can.

That means graph and grid traversal usually needs:

```python
visited = set()
```

Without `visited`, you may revisit the same place forever.

## 6. Grids are graphs in disguise

In a grid, each cell can be a node.

Neighbors are usually:

```text
up, down, left, right
```

For each neighbor, check:

```text
Is it inside the grid?
Is it valid land/path?
Have I visited it already?
```

## 7. Separate "visit" from "decide neighbors"

Traversal problems become clearer if you separate:

```text
What do I do when I reach a node/cell?
Which neighbors should I try next?
```

This keeps DFS/BFS code less tangled.

## 8. Week 9 thinking habit

Before solving, identify:

```text
What counts as a node?
What counts as an edge/connection?
What does visited mean?
Should I use DFS or BFS?
```
