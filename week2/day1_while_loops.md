# Day 1: while Loops — Repeat While True

**Time:** ~30 minutes

Today you learn:
1. `while` loops — repeat code as long as a condition is true
2. `break` — exit a loop early
3. `continue` — skip to next iteration
4. Infinite loops and how to avoid them

**Practice file:** Create `day1_practice.py`

---

## Part 1: Basic while loop

A while loop keeps running as long as its condition is True:

```python
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1  # count = count + 1 (CRUCIAL — without this, infinite loop!)

print("Loop finished!")
```

Output: `Count: 1`, `Count: 2`, ... `Count: 5`, `Loop finished!`

**How it works:**
1. Check condition (`count <= 5`)
2. If True → run the body → go back to step 1
3. If False → skip the body → continue after the loop

### 🔁 Trace every loop (watch the condition flip)

A `while` loop is a **gate that keeps reopening as long as the answer is True**. The key is spotting *what changes each round* to eventually make it False. Here it's `count += 1`. Trace it:

| Round | `count` | `count <= 5`? | Body runs? | `count` after `+= 1` |
|-------|---------|----------------|------------|-----------------------|
| 1 | 1 | True | prints `Count: 1` | 2 |
| 2 | 2 | True | prints `Count: 2` | 3 |
| 3 | 3 | True | prints `Count: 3` | 4 |
| 4 | 4 | True | prints `Count: 4` | 5 |
| 5 | 5 | True | prints `Count: 5` | 6 |
| 6 | 6 | **False** | skipped → exit loop | — |

That last row is the whole point: on round 6 the condition is finally False, so the loop stops and `"Loop finished!"` runs. **If you forget `count += 1`, count stays 1 forever → the gate never closes → infinite loop.** Always ask: *"what makes this condition eventually become False?"*

---

## Part 2: Counting patterns

```python
# Count DOWN
n = 5
while n > 0:
    print(n)
    n -= 1
print("Liftoff!")

# Count by 2s
i = 0
while i <= 10:
    print(i, end=" ")  # end=" " prints on same line
    i += 2
print()  # New line
# Output: 0 2 4 6 8 10

# Sum numbers from 1 to 100
total = 0
num = 1
while num <= 100:
    total += num
    num += 1
print(f"Sum of 1-100: {total}")  # 5050
```

---

## Part 3: break — Exit the loop early

`break` immediately exits the loop, no matter what:

```python
count = 1
while True:  # This would run forever WITHOUT break
    print(count)
    if count == 5:
        break  # EXIT!
    count += 1
print("Escaped the loop!")
```

Common pattern — keep asking until valid input:

```python
while True:
    answer = input("Type 'quit' to exit: ")
    if answer == "quit":
        break
    print(f"You typed: {answer}")
print("Goodbye!")
```

---

## Part 4: continue — Skip this iteration

`continue` skips the REST of the loop body and goes to the next iteration:

```python
# Print only odd numbers from 1-10
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i, end=" ")
print()
# Output: 1 3 5 7 9
```

---

## Part 5: Avoiding infinite loops

If the condition never becomes False, the loop runs forever!
If this happens, press **Ctrl+C** in the terminal to stop it.

```python
# BAD (infinite loop):
# x = 1
# while x > 0:
#     print(x)
#     x += 1  # x keeps growing, always > 0!

# GOOD: Make sure the condition WILL eventually be False
x = 10
while x > 0:
    print(x, end=" ")
    x -= 1  # x shrinks toward 0
print()
```

> **SAFETY TIP:** When writing a while loop, always ask:
> *"What makes this condition become False?"*

---

## Part 6: While loop with user input — Guessing game

```python
import random

secret = random.randint(1, 10)  # Random number 1-10
attempts = 0

print("I'm thinking of a number between 1 and 10...")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess == secret:
        print(f"Correct! You got it in {attempts} tries!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
```

---

## Exercises

**Exercise 1:** Print the multiplication table for 7.
`7 x 1 = 7`, `7 x 2 = 14`, ... `7 x 10 = 70`

**Exercise 2:** Ask the user to keep entering numbers.
When they enter 0, stop and print the sum of all numbers entered.
Hint: Use `while True` with `break`

**Exercise 3:** Find the first power of 2 that is greater than 1000.
Start with n=1 and keep doubling. Print the result.
*(Answer should be 1024)*

**Exercise 4:** Print a countdown with a twist:
`10, 9, 8, 7, 6, 5, 4, 3, 2, 1`
But **SKIP** any number divisible by 3.
Expected: `10, 8, 7, 5, 4, 2, 1`
