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

