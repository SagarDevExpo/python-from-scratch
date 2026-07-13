# Week 2 Prerequisites: Fast Lookup and Order Rules

Week 2 is about containers that remember things in special ways: dictionaries, sets, stacks, and queues.

## 1. Fast lookup is the main idea

Lists search by checking items one by one.

Dictionaries and sets are built for quick membership checks.

Ask:

```text
Will I keep asking "have I seen this before?"
```

If yes, think set or dictionary.

## 2. Dictionary versus set

Use a set when you only need existence:

```text
seen item
```

Use a dictionary when you need information attached:

```text
item -> count
item -> index
item -> group
```

The question is:

```text
Do I need a value for each key?
```

## 3. Frequency counting is a core pattern

Many problems become easier when you count first.

Common mappings:

```text
character -> count
number -> count
word -> count
```

This helps with anagrams, first unique values, duplicates, and most-common problems.

## 4. Complement thinking helps with Two Sum

For a target sum:

```text
current number + needed number = target
```

So:

```text
needed number = target - current number
```

The dictionary remembers numbers you already passed.

Do not compare every pair first. Ask:

```text
What number would complete this pair?
Have I seen it already?
```

## 5. Stack means Last In, First Out

Use stack thinking when the newest unfinished thing must be handled first.

Examples:

- parentheses
- undo behavior
- reversing
- nested structures

Question:

```text
Does the most recent item matter first?
```

## 6. Queue means First In, First Out

Use queue thinking when items should be processed in arrival order.

Examples:

- support tickets
- print jobs
- BFS later

Question:

```text
Should the oldest waiting item go first?
```

## 7. Be precise about what is stored

Before coding, write:

```text
My set stores ___.
My dictionary maps ___ to ___.
My stack stores ___.
My queue stores ___.
```

This prevents "I know I need a dictionary but I don't know what goes in it" confusion.

## 8. Week 2 thinking habit

When a solution feels too nested, ask:

```text
Can I remember useful information from earlier so I do not search again?
```

That is the doorway into hash maps and sets.
