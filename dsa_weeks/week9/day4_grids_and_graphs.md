# Day 4: Grids and Graphs

**Time:** ~45 minutes

Today you learn:
1. Nodes and edges
2. How a grid can act like a graph
3. The visited-set pattern

**Practice file:** Create `day4_practice.py`

---

## Part 1: Graph Idea

A graph contains:

- **Nodes:** things
- **Edges:** connections between things

A social network has people as nodes and friendships as edges.

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
}
```

---

## Part 2: Grid Neighbors

In a grid, a cell can connect to four neighbors:

```python
directions = [
    (-1, 0),  # up
    (1, 0),   # down
    (0, -1),  # left
    (0, 1),   # right
]
```

Always check boundaries:

```python
if 0 <= new_row < rows and 0 <= new_col < cols:
    print("valid cell")
```

---

## Part 3: DFS Through Land

```python
def visit(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])

    if row < 0 or row >= rows or col < 0 or col >= cols:
        return
    if grid[row][col] != "1":
        return

    grid[row][col] = "0"  # mark visited

    visit(grid, row - 1, col)
    visit(grid, row + 1, col)
    visit(grid, row, col - 1)
    visit(grid, row, col + 1)
```

This is the core of Number of Islands.

---

## Exercises

1. Print all valid neighbors of a cell.
2. Traverse a small graph with DFS.
3. Count connected groups of `"1"` cells.
4. Explain why visited cells must be marked.

