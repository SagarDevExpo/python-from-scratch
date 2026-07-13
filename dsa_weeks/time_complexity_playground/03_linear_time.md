# 03: O(n) Linear Time

`O(n)` means the work grows with the input.

If there are 10 items, maybe about 10 checks.
If there are 1000 items, maybe about 1000 checks.

## Visual

```text
[4] [8] [2] [9] [1]
```

Code:

```python
for num in nums:
    print(num)
```

Touch pattern:

```text
[*] [*] [*] [*] [*]
```

Every item gets touched once.

That is `O(n)`.

## Search Is Usually O(n)

```python
target = 9

for num in nums:
    if num == target:
        print("found")
```

Worst case:

```text
target is last or missing
```

So Python may need to check every item.

That is `O(n)`.

## Counting Is O(n)

```python
count = 0

for char in text:
    if char == "a":
        count += 1
```

If the text has `n` characters, you check `n` characters.

That is `O(n)`.

## Building A New List Is O(n)

```python
evens = []

for num in nums:
    if num % 2 == 0:
        evens.append(num)
```

You inspect every number once.

That is `O(n)` time.

It may also use `O(n)` space if many values are added.

## Two Separate Loops Are Still O(n)

```python
for num in nums:
    print(num)

for num in nums:
    print(num * 2)
```

Work:

```text
n + n = 2n
```

Big O:

```text
O(n)
```

Big O drops constants.

## Memory Hook

```text
One loop over input = O(n)
```

## Tiny Practice

What is the Big O?

```python
total = 0

for num in nums:
    total += num
```

Answer:

```text
O(n)
```

What about:

```python
largest = nums[0]

for num in nums:
    if num > largest:
        largest = num
```

Answer:

```text
O(n)
```

You are touching each item once.
