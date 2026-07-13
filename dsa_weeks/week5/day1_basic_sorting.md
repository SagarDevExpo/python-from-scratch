# Day 1: Basic Sorting Algorithms

**Time:** ~45 minutes

Today you learn:
1. Bubble sort
2. Selection sort
3. Why simple sorting algorithms are `O(n²)`

**Practice file:** Create `day1_practice.py`

---

## Part 1: Bubble Sort

Compare neighbors and swap them when they are in the wrong order.

```python
def bubble_sort(numbers):
    numbers = numbers[:]

    for end in range(len(numbers) - 1, 0, -1):
        for index in range(end):
            if numbers[index] > numbers[index + 1]:
                numbers[index], numbers[index + 1] = (
                    numbers[index + 1],
                    numbers[index],
                )

    return numbers
```

Large values “bubble” toward the end.

### 🧩 Watch one full pass of the inner loop

The inner loop walks left to right comparing each pair of neighbours; if the left one is bigger, they **swap**. After each full pass, the largest unsorted value has floated to its correct spot at the end.

Trace the **first pass** on `[4, 2, 3, 1]` (the inner loop, comparing `numbers[index]` with its right neighbour):

| `index` | pair compared | left > right? | list after |
|---------|---------------|----------------|------------|
| 0 | `4, 2` | 4 > 2 ✅ swap | `[2, 4, 3, 1]` |
| 1 | `4, 3` | 4 > 3 ✅ swap | `[2, 3, 4, 1]` |
| 2 | `4, 1` | 4 > 1 ✅ swap | `[2, 3, 1, 4]` |

After pass 1, `4` (the biggest) has bubbled to the far right — it's now locked in place. The outer loop's `end` shrinks by one so the next pass ignores that settled tail:

- Pass 2 works on `[2, 3, 1]` → becomes `[2, 1, 3, 4]`
- Pass 3 works on `[2, 1]` → becomes `[1, 2, 3, 4]` ✅ sorted

Two nested loops (each up to `n`) = `n × n` comparisons = **O(n²)**. That's why bubble sort is fine for learning but slow for big lists compared to merge sort's `O(n log n)`.

---

## Part 2: Selection Sort

Find the smallest remaining value and place it next.

```python
def selection_sort(numbers):
    numbers = numbers[:]

    for start in range(len(numbers)):
        smallest = start

        for index in range(start + 1, len(numbers)):
            if numbers[index] < numbers[smallest]:
                smallest = index

        numbers[start], numbers[smallest] = numbers[smallest], numbers[start]

    return numbers
```

Both algorithms use nested loops, so time is `O(n²)`.

---

## Exercises

1. Trace bubble sort on `[4, 2, 3, 1]`.
2. Type selection sort from memory.
3. Add a `swapped` flag so bubble sort stops when already sorted.
4. Test empty, sorted, reversed, and duplicate values.

