# 02: O(1) Constant Time

`O(1)` means the work stays the same no matter how big the input gets.

It is the "one move" category.

## Visual

List with 5 items:

```text
[10] [20] [30] [40] [50]
  0    1    2    3    4
```

Code:

```python
print(nums[0])
```

Touch:

```text
[*] [ ] [ ] [ ] [ ]
```

List with 1 million items:

```python
print(nums[0])
```

Still touch:

```text
only index 0
```

That is `O(1)`.

## Common O(1) Examples

Direct index access:

```python
first = nums[0]
last = nums[-1]
```

Simple variable assignment:

```python
x = 10
```

Dictionary lookup on average:

```python
person["name"]
```

Set membership on average:

```python
if target in seen:
    print("found")
```

## Important: O(1) Does Not Mean One Line

This is still `O(1)`:

```python
a = nums[0]
b = nums[-1]
c = a + b
print(c)
```

It does a few fixed steps.

If the number of steps does not grow with input size, it is constant time.

## What To Ask

```text
Does this code touch more items when the list gets bigger?
```

If no:

```text
O(1)
```

## Tiny Practice

What is the Big O?

```python
def get_first(nums):
    return nums[0]
```

Answer:

```text
O(1)
```

What about this?

```python
def get_edges(nums):
    return nums[0], nums[-1]
```

Answer:

```text
O(1)
```

Still only fixed work.
