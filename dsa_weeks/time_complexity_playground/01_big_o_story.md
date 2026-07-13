# 01: Big O Is A Growth Story

Big O is a way to describe how code behaves when the input gets bigger.

It does not ask:

```text
How many seconds did this run?
```

It asks:

```text
If the input doubles, does the work stay the same, double, explode, or shrink by halves?
```

## The Box Picture

Imagine a list:

```python
nums = [4, 8, 2, 9, 1]
```

Visual:

```text
index:  0   1   2   3   4
       [4] [8] [2] [9] [1]
```

Here:

```text
n = 5
```

because there are 5 items.

If the list becomes:

```python
nums = [4, 8, 2, 9, 1, 6, 3, 7, 5, 10]
```

then:

```text
n = 10
```

Big O asks:

```text
How does the work change when n changes?
```

## Three People, Three Strategies

Problem:

```text
Find whether 9 is in the list.
```

List:

```text
[4] [8] [2] [9] [1]
```

Strategy A: Look directly at index 3.

```text
Touch 1 box.
```

That is `O(1)`.

Strategy B: Start at the beginning and scan.

```text
Touch boxes until found.
```

That is `O(n)`.

Strategy C: Compare every item with every other item.

```text
Touch many pairs.
```

That is often `O(n^2)`.

## Big O Ignores Small Details

These are both `O(n)`:

```python
for num in nums:
    print(num)
```

```python
for num in nums:
    print(num)

for num in nums:
    print(num)
```

The second one does about `2n` work, but Big O simplifies:

```text
O(2n) -> O(n)
```

Why? Because Big O cares about the growth shape.

## Visual Growth

If `n = 10`:

```text
O(1)      1 step
O(n)      10 steps
O(n^2)    100 steps
```

If `n = 1000`:

```text
O(1)      1 step
O(n)      1000 steps
O(n^2)    1000000 steps
```

That is why nested loops can get expensive fast.

## Memory Hook

```text
O(1):    one peek
O(n):    one walk
O(n^2):  every pair
O(log n): half, half, half
```

## Mini Practice

For each, say the likely Big O:

```python
print(nums[0])
```

```python
for num in nums:
    print(num)
```

```python
for a in nums:
    for b in nums:
        print(a, b)
```

Answers:

```text
O(1)
O(n)
O(n^2)
```
