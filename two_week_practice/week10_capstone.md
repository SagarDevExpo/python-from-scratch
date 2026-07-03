# Week 10 Capstone: Sorting, Heaps, Sliding Window, Final Pattern Review

**Time:** 75-90 minutes

**Practice file:** Create `week10_capstone_review.py`

This is the final review. The goal is to choose the right pattern before coding.

---

## Warm-Up: Pattern Match

Choose the likely pattern:

1. Need the top 3 largest values.
2. Need the maximum sum of 4 consecutive numbers.
3. Need to sort without using `sorted()`.
4. Need to merge two sorted lists.
5. Need to repeatedly process the smallest item.
6. Need to find if two numbers add to target.

Use:

```text
heap
sliding window
sorting
merge
hash map
two pointers
```

---

## Challenge 1: Selection Sort Trace

Implement selection sort.

After each outer loop, print the list so you can see the sorted section grow.

Pattern focus: find smallest in unsorted area, swap into place.

---

## Challenge 2: Bubble Sort Trace

Implement bubble sort.

After each pass, print the list.

Pattern focus: compare neighbors and push larger values right.

---

## Challenge 3: Merge Two Sorted Lists

Given:

```python
a = [1, 3, 7]
b = [2, 4, 8]
```

Return:

```python
[1, 2, 3, 4, 7, 8]
```

Pattern focus: two pointers and result list.

---

## Challenge 4: Merge Sort From Memory

Write merge sort.

First write comments:

```text
base case
split
sort left
sort right
merge
```

Pattern focus: divide, solve, combine.

---

## Challenge 5: Kth Largest

Given:

```python
nums = [3, 2, 1, 5, 6, 4]
k = 2
```

Return:

```python
5
```

Solve one way with sorting.

Then write what a heap would help with.

Pattern focus: choose based on whether you need repeated priority.

---

## Challenge 6: Maximum Fixed Window Sum

Given:

```python
nums = [2, 1, 5, 1, 3, 2]
k = 3
```

Return:

```python
9
```

Because:

```python
5 + 1 + 3 = 9
```

Pattern focus: add new right item, remove old left item.

---

## Challenge 7: Longest Substring Without Repeating Characters

Given:

```python
"abcabcbb"
```

Return:

```python
3
```

Because `"abc"` is the longest substring without repeats.

Pattern focus: variable sliding window and seen positions.

---

## Challenge 8: Final Mixed Set

Solve each and write the pattern name first:

1. Valid parentheses
2. Two Sum
3. Number of Islands
4. Binary Search
5. First Unique Character
6. Rotate List

Pattern focus: recognition before implementation.

---

## Final Checklist

You are ready to keep practicing DSA if you can say:

- "This is a counting problem, so I need a dictionary."
- "This is sorted, so two pointers or binary search may help."
- "This asks for consecutive chunks, so sliding window may help."
- "This asks for level order, so BFS with a queue fits."
- "This asks for top K, so sorting or heap fits."
- "This asks for connected land, so DFS/BFS with visited fits."
