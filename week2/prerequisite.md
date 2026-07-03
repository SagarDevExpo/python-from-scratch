# Week 2 Prerequisites: Loop and Sequence Thinking

Week 2 introduces repetition and ordered data. The main mental shift is this: instead of writing one action, you describe a pattern that runs many times.

## 1. A loop needs a purpose

Before writing a loop, ask:

```text
Am I repeating until a condition changes?
Am I going through known items?
Am I building, counting, searching, or printing?
```

This helps you choose the right loop shape.

## 2. `while` is condition-driven

Use `while` when you do not know exactly how many times the loop will run.

Examples:

- keep asking until the user enters `0`
- keep doubling until the number is big enough
- keep retrying until the answer is correct

The key question:

```text
What changes so this loop eventually stops?
```

If nothing changes, the loop can run forever.

## 3. `for` is item-driven

Use `for` when Python can give you the next item automatically.

Examples:

- each number in a range
- each character in a string
- each item in a list

The key question:

```text
What collection or range am I walking through?
```

## 4. Loop variables are temporary names

In this code:

```python
for char in text:
```

`char` is not special. It just means "the current character".

You could call it `i`, `letter`, or `x`, but the meaning should help your brain.

Good names reduce confusion:

```python
for number in numbers:
for word in words:
for char in text:
```

## 5. Index and value are different things

For a list:

```python
numbers = [3, 7, 2]
```

Indexes are positions:

```text
0, 1, 2
```

Values are the actual items:

```text
3, 7, 2
```

If you write:

```python
for number in numbers:
```

then `number` is already the value. You do not need `numbers[number]`.

## 6. Learn the four tracker patterns

Many loop problems are one of these:

Counting:

```python
count = 0
```

Adding:

```python
total = 0
```

Finding the best so far:

```python
largest = numbers[0]
```

Building a result:

```python
result = ""
result_list = []
```

When stuck, ask:

```text
What do I need to remember while looping?
```

That answer usually becomes your variable.

## 7. Nested loops mean rows and inner work

For pattern problems, think:

```text
Outer loop: which row am I on?
Inner loop: what should be printed inside this row?
```

If each row grows, the inner loop probably depends on the outer loop variable.

## 8. Strings and lists both have positions

Both support indexing and slicing:

```python
word[0]
items[0]
```

The difference: strings cannot be changed in place, but lists can.

So for strings, you often build a new string. For lists, you can sometimes modify the existing list.

## 9. Slow down at boundaries

Most loop bugs happen at the edge:

- starts too early or too late
- stops too early or too late
- prints an extra comma
- skips the first or last item

Check the first iteration and the last iteration by hand.
