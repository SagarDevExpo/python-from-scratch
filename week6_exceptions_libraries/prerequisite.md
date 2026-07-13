# Week 6 Prerequisites: Handling Failure and Reusing Other People's Code

Week 6 shifts your focus from "make it work" to "make it survive the real world." Programs meet bad input, missing files, and messy data. This week is about failing gracefully and standing on code others already wrote.

## 1. Errors are normal, not shameful

An error is just Python telling you something went wrong at run time.

```python
int("hello")   # ValueError
```

The code is valid. The *value* is the problem.

Ask yourself:

```text
Which single line could realistically blow up?
```

That line is the one to protect.

## 2. `try` means "attempt this risky thing"

Only wrap the part that might fail, not your whole program.

Mental model:

```text
try: attempt the risky line
except: what to do if it fails
```

If you wrap too much, you can no longer tell *what* failed.

## 3. Catch the specific error you expect

Catching everything hides real bugs.

```text
except ValueError:   good, you expected this
except:              too broad, you may silence a typo
```

Ask:

```text
What exact kind of failure am I planning for?
```

## 4. Success path and failure path are different rooms

Read the four blocks as one flow:

```text
try     -> attempt
except  -> ran only if it failed
else    -> ran only if it succeeded
finally -> always runs, either way
```

If you can say out loud which block runs for a given input, you understand it.

## 5. `raise` is the opposite of `return`

`return` says "here is your answer."
`raise` says "stop, this input is wrong."

Use `raise` when a function should refuse bad data instead of returning a fake answer.

```text
empty list -> raise, do not return 0
negative age -> raise, do not guess
```

## 6. Read tracebacks from the bottom up

A traceback is a breadcrumb trail.

```text
bottom line -> WHAT went wrong (the error type)
lines above -> WHO called WHO to get there
```

Always read the last line first.

## 7. A library is code you did not have to write

`import` borrows ready-made tools.

```python
import random
import math
import json
```

Before writing something tricky, ask:

```text
Has someone already solved this in the standard library?
```

## 8. Know where a function came from

Prefer clarity about origins:

```text
import module      -> module.function()  (clear source)
from module import name -> name()         (shorter, less obvious)
```

When reading unfamiliar code, always ask:

```text
Where does this name come from?
```

## 9. Week 6 thinking habit

Before running risky code, write:

```text
What could go wrong here?
What should happen if it does?
Whose job is it to catch it?
```
