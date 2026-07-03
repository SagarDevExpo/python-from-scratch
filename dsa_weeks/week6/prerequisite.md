# Week 6 Prerequisites: Entering DSA Thinking

Week 6 starts formal DSA. The biggest change is that you now care not only whether code works, but how the work grows as input gets bigger.

## 1. DSA is about choosing a shape

For each problem, ask:

```text
What data do I have?
What operation do I need often?
What result should come out?
```

The answer guides both the data structure and the algorithm.

## 2. Input size matters

Think of `n` as "how many things are in the input."

If the list has 6 items, `n = 6`.
If the string has 100 characters, `n = 100`.

Big O asks:

```text
As n grows, how much more work does my code do?
```

## 3. Count loops, not seconds

When estimating complexity:

- one simple pass through a list is usually `O(n)`
- nested loops over the same list are usually `O(n^2)`
- direct index access is usually `O(1)`
- repeatedly cutting the search area in half is usually `O(log n)`

You do not need perfect math yet. You need the habit of noticing growth.

## 4. Search problems have two basic shapes

Linear search:

```text
Check one item at a time.
Works even if data is unsorted.
```

Binary search:

```text
Check the middle.
Throw away half.
Requires sorted data.
```

Before using binary search, always ask:

```text
Is the data sorted?
```

## 5. Arrays/lists are great at index access

Lists are strong when you know the position:

```python
numbers[3]
```

But inserting or removing near the front can be slower because other items must shift.

Think:

```text
Am I jumping to a position, or moving many items around?
```

## 6. In-place versus new result

Some problems ask you to modify the original list. Others are easier if you build a new one.

Ask:

```text
Am I allowed to create a new list?
Do I need to preserve the original?
```

This question prevents many messy solutions.

## 7. Prefix thinking means "running total"

Prefix sums are just remembered totals.

Instead of adding the same range again and again, store useful totals as you go.

Mental model:

```text
What have I accumulated up to this point?
```

## 8. Week 6 trace habit

For every algorithm, trace with a table:

```text
index | value | current answer | reason
```

This trains your brain to see state changes, not just code lines.
