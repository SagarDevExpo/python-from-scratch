# Week 7 Prerequisites: Proving Code Works and Talking to Files

Week 7 is about two grown-up skills: checking that your code is actually correct, and letting programs read and write real files instead of losing everything when they close.

## 1. A test is a promise you can re-check

A test states what the answer *should* be, so the computer verifies it for you.

```python
assert square(3) == 9
```

Ask yourself:

```text
What do I already know the answer should be?
```

That known answer becomes your test.

## 2. Quiet means passing

`assert` does nothing visible when the check is true. It only shouts when something is wrong.

```text
no output -> good, the promise held
AssertionError -> the code disagreed with your expectation
```

Do not expect a cheerful message. Silence is success.

## 3. Test the edges, not just the happy path

Most bugs hide at the boundaries.

```text
empty input
zero
negative numbers
one single item
```

Before trusting code, ask:

```text
What weird input might break this?
```

## 4. Testable code returns; hard-to-test code only prints

You cannot easily test something that just prints to the screen.

```text
prints only  -> hard to check automatically
returns a value -> easy to assert on
```

Separate the "figure it out" part from the "show it" part.

## 5. `pytest` is `assert` grown up

The idea is identical; the tooling is nicer.

```text
files named test_*.py
functions named test_*
one behavior per test function
```

Ask:

```text
What single behavior does this one test prove?
```

## 6. Files must be opened in the right mode

The mode letter decides what you are allowed to do, and whether old data survives.

```text
"r" -> read (file must exist)
"w" -> write (ERASES existing content)
"a" -> append (keeps content, adds to the end)
```

The classic mistake:

```text
I used "w" and wiped the file I meant to add to.
```

## 7. Always use `with` when opening files

`with` closes the file for you automatically, even if an error happens.

Mental rule:

```text
open a file -> you must close it
with open(...) -> Python closes it for me
```

Never hand-manage `close()` while learning.

## 8. Files are just text until you give them shape

A CSV is plain text with commas. `csv.DictReader` gives each row a name-tag.

```text
row as a list  -> grab columns by number  (row[0])
row as a dict  -> grab columns by name    (row["score"])
```

Everything read from a file arrives as a **string**, so convert before doing math.

## 9. Week 7 thinking habit

Before finishing a function, ask:

```text
How would I prove this is correct without eyeballing it?
If I saved this data, could I read it back and trust it?
```
