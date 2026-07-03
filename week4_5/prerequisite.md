# Weeks 4-5 Prerequisites: Problem-Solving Patterns

Weeks 4-5 are not about many new syntax rules. They are about recognizing problem shapes. This is where the "why couldn't I think of it?" feeling starts to turn into pattern memory.

## 1. Do not start with code

For each challenge, first write:

```text
Input:
Output:
Small example:
What must I remember while looping?
```

This is not wasted time. It is how you make the solution visible.

## 2. Look for the problem shape

Most beginner/interview problems are one of these:

- search for something
- count frequencies
- track best so far
- build a new result
- compare two sides
- group items by a key
- keep a stack of unfinished things
- scan while remembering previous values

Once you name the shape, the code becomes less mysterious.

## 3. "Best so far" solves many problems

Use this when the problem asks for largest, smallest, longest, shortest, maximum profit, or best score.

Mental model:

```text
Start with a champion.
Each new item challenges the champion.
Replace only if better.
```

The variable might be called:

```python
largest
smallest
best_profit
longest_word
max_sum
```

## 4. Frequency maps solve counting problems

When a problem asks:

```text
How many times?
Most common?
Same letters?
First unique?
```

think dictionary.

You are usually mapping:

```text
item -> count
```

## 5. Two pointers solve "from both ends" and "merge" problems

Use two pointer thinking when:

- checking a palindrome
- comparing start and end
- merging sorted lists
- moving zeros
- finding a pair in sorted data

Ask:

```text
Where should the left pointer start?
Where should the right pointer start?
What makes each one move?
```

## 6. Stack thinking solves "last opened, first closed"

Valid parentheses is the classic stack problem.

Mental model:

```text
When I see an opening thing, remember it.
When I see a closing thing, it must match the most recent opening thing.
```

If the most recent thing matters, think stack.

## 7. Matrix problems are nested-loop problems with coordinates

For a 2D list, think:

```text
row index
column index
value at grid[row][col]
```

Do not try to hold the whole grid in your head. Trace one cell at a time.

## 8. When stuck, test a tiny version

Use a smaller input than the problem gives.

Instead of:

```python
[3, 7, 2, 9, 1, 5]
```

try:

```python
[3, 7]
```

If your logic works for two or three items, it is easier to grow it.

## 9. The debug question

When code surprises you, ask:

```text
What did I think this variable was?
What is it actually at this line?
```

Most bugs are not syntax bugs. They are mismatches between your mental model and the current value.
