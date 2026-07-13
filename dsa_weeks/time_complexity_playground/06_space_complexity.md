# 06: Space Complexity

Time complexity asks:

```text
How much work?
```

Space complexity asks:

```text
How much extra memory?
```

## O(1) Space

If you only use a few variables, space is constant.

```python
total = 0

for num in nums:
    total += num
```

Extra memory:

```text
total
num
```

Even if `nums` has 1 million items, you are not creating another 1-million-item structure.

Space:

```text
O(1)
```

## O(n) Space

If you build a new list that can grow with the input:

```python
evens = []

for num in nums:
    if num % 2 == 0:
        evens.append(num)
```

If many numbers are even, `evens` can grow almost as large as `nums`.

Space:

```text
O(n)
```

## Dictionary Counting Uses O(n) Space

```python
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1
```

If there are many unique characters or words, the dictionary grows.

Space:

```text
O(n)
```

## Set Seen Uses O(n) Space

```python
seen = set()

for num in nums:
    seen.add(num)
```

In the worst case, every number is unique.

Space:

```text
O(n)
```

## In-Place Means Modify Existing Data

Example:

```python
left = 0
right = len(nums) - 1

while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
```

This reverses the list without creating another list.

Extra space:

```text
O(1)
```

## Memory Hook

```text
Few variables only        -> O(1) space
New list/dict/set grows   -> O(n) space
```

## Tiny Practice

What is the space complexity?

```python
result = []

for word in words:
    result.append(word.upper())
```

Answer:

```text
O(n)
```

What about:

```python
count = 0

for word in words:
    if len(word) > 3:
        count += 1
```

Answer:

```text
O(1)
```
