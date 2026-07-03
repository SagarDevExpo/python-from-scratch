# Day 3: Heaps — Quickly Access the Smallest Value

**Time:** ~40 minutes

Today you learn:
1. Min-heaps
2. Python's `heapq`
3. Priority queues and Top K problems

**Practice file:** Create `day3_practice.py`

---

## Part 1: Heap Property

In a min-heap, the smallest value is always at index `0`.
The entire list is not necessarily sorted.

```python
import heapq

numbers = [7, 2, 9, 1, 5]
heapq.heapify(numbers)

print(numbers[0])          # 1
print(heapq.heappop(numbers))  # removes 1
heapq.heappush(numbers, 3)
```

- Read smallest: `O(1)`
- Push: `O(log n)`
- Pop smallest: `O(log n)`

---

## Part 2: Priority Queue

Store `(priority, task)` tuples:

```python
tasks = []
heapq.heappush(tasks, (3, "send email"))
heapq.heappush(tasks, (1, "fix outage"))
heapq.heappush(tasks, (2, "review code"))

while tasks:
    priority, task = heapq.heappop(tasks)
    print(priority, task)
```

Smaller priority numbers come out first.

---

## Part 3: Kth Largest

Keep a min-heap of only `k` values. When it grows beyond `k`, remove the
smallest. At the end, the heap's smallest value is the kth largest overall.

---

## Exercises

1. Process tasks by priority.
2. Find the three smallest numbers.
3. Implement kth largest with a heap of size `k`.
4. Explain why a heap is not the same as a fully sorted list.

