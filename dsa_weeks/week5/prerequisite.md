# Week 5 Prerequisites: Choosing Efficient Patterns

Week 5 combines sorting, divide-and-conquer, heaps, sliding windows, and final practice. The main skill is choosing the pattern that avoids unnecessary work.

## 1. Sorting changes what is easy

After sorting, nearby values become meaningful.

Sorting can help with:

- finding pairs
- removing duplicates
- merging
- choosing smallest or largest in order

But sorting costs time, so ask:

```text
Does ordering make the rest of the problem simpler?
```

## 2. Basic sorts teach comparison thinking

Bubble sort and selection sort are not mainly about memorizing production algorithms. They teach:

```text
compare
swap
track position
shrink the unsorted area
```

Watch which part of the list is already finished.

## 3. Divide and conquer means split, solve, combine

Merge sort has three ideas:

```text
split into smaller pieces
solve each piece
merge the answers
```

Before writing divide-and-conquer code, ask:

```text
What is the smallest easy case?
How do I combine two solved halves?
```

## 4. Heaps are for repeated smallest/largest access

Use heap thinking when the problem repeatedly asks for:

- smallest item
- largest item
- top K items
- priority order

Question:

```text
Do I need the best item once, or repeatedly as data changes?
```

For one-time largest, a loop may be enough. For repeated priority, a heap may help.

## 5. Sliding window avoids redoing work

Sliding window is useful for contiguous chunks:

```text
subarray
substring
window of size k
longest segment with a rule
```

Instead of recalculating the whole chunk each time, update what changed:

```text
remove the left item
add the right item
```

## 6. Fixed window versus variable window

Fixed window:

```text
The size is known, like k = 3.
```

Variable window:

```text
The size grows and shrinks to satisfy a condition.
```

Ask:

```text
Is the window size given, or does the condition decide it?
```

## 7. Final practice is pattern recognition

Before choosing code, name the likely pattern:

- Two Sum: hash map
- Valid Parentheses: stack
- Level Order: queue/BFS
- Number of Islands: DFS/BFS with visited
- Kth Largest: heap or sorting
- Maximum Window Sum: sliding window

The win is recognizing the shape before typing.

## 8. Week 5 thinking habit

For every problem, ask:

```text
What work am I repeating?
Can I store, sort, split, prioritize, or slide to avoid repeating it?
```
