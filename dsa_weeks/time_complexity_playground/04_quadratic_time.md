# 04: O(n^2) Quadratic Time

`O(n^2)` usually appears when you have nested loops over the same input.

It means:

```text
For each item, compare/check many other items.
```

## Visual

List:

```text
[1] [2] [3] [4]
```

All pairs:

```text
1 with 1, 2, 3, 4
2 with 1, 2, 3, 4
3 with 1, 2, 3, 4
4 with 1, 2, 3, 4
```

That is:

```text
4 * 4 = 16 checks
```

If `n = 100`:

```text
100 * 100 = 10000 checks
```

That is why `O(n^2)` grows quickly.

## Code Shape

```python
for a in nums:
    for b in nums:
        print(a, b)
```

Outer loop runs `n` times.
Inner loop runs `n` times for each outer loop.

Work:

```text
n * n = n^2
```

Big O:

```text
O(n^2)
```

## Pair Sum Brute Force

```python
nums = [1, 2, 3, 4, 5]
target = 5

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i], nums[j])
```

This avoids reverse duplicates, but it is still nested-loop pair checking.

Big O:

```text
O(n^2)
```

Why? Because as the list grows, possible pairs grow roughly like a grid.

## The Pair Grid

For 5 items:

```text
      1  2  3  4  5
   ----------------
1 |   x  *  *  *  *
2 |      x  *  *  *
3 |         x  *  *
4 |            x  *
5 |               x
```

Even if you only check the upper half, the growth is still quadratic.

## Memory Hook

```text
Nested loops over same input = usually O(n^2)
```

## Tiny Practice

What is the Big O?

```python
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            print(i, j)
```

Answer:

```text
O(n^2)
```

What about this?

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print(nums[i], nums[j])
```

Answer:

```text
O(n^2)
```

Fewer checks than the full grid, but same growth family.
