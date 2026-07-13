# Time Complexity Playground

Time complexity is not about scary math first. It is about asking:

```text
When the input gets bigger, how much more work does my code do?
```

This folder teaches Big O with visual memory hooks, tiny code examples, and practice questions.

## How To Use This Folder

Read in order:

```text
01_big_o_story.md
02_constant_time.md
03_linear_time.md
04_quadratic_time.md
05_logarithmic_time.md
06_space_complexity.md
07_pattern_quiz.md
```

For each file:

1. Read the visual explanation.
2. Trace the tiny code by hand.
3. Answer the "What is the work?" question.
4. Only then run or rewrite the code.

## The Main Memory Hook

Think of your input as a line of boxes:

```text
n = number of boxes

[ ] [ ] [ ] [ ] [ ]
```

Big O asks how many boxes your code touches as `n` grows.

## The Big Four

```text
O(1)      Touch one thing.
O(n)      Touch each thing once.
O(n^2)    For each thing, touch many things.
O(log n)  Keep cutting the work in half.
```

## Tiny Cheat Sheet

```text
Direct index lookup             -> O(1)
One loop through input          -> O(n)
Nested loop over same input     -> O(n^2)
Binary search                   -> O(log n)
Dictionary/set lookup average   -> O(1)
Building a new list of n items  -> O(n) space
```

## One Rule

First make the solution correct. Then ask:

```text
Can I avoid repeating work?
```

That question is the doorway into better algorithms.
