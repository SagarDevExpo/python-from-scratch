# Day 3: Reading and Writing Text Files

**Time:** ~40 minutes

Today you learn:
1. `open()`
2. `with`
3. Reading files
4. Writing and appending files

**Practice file:** Create `day3_practice.py`

---

## Part 1: Write a File

```python
with open("notes.txt", "w") as file:
    file.write("Learning Python\n")
    file.write("File I/O is useful\n")
```

Mode `"w"` means write. It creates the file or overwrites it.

---

## Part 2: Append to a File

```python
with open("notes.txt", "a") as file:
    file.write("Adding one more line\n")
```

Mode `"a"` means append.

---

## Part 3: Read the Whole File

```python
with open("notes.txt", "r") as file:
    contents = file.read()

print(contents)
```

Mode `"r"` means read.

---

## Part 4: Read Line by Line

```python
with open("notes.txt") as file:
    for line in file:
        print(line.strip())
```

`.strip()` removes the newline at the end.

---

## Part 5: Why with?

`with` automatically closes the file when you are done. Use it by default.

---

## Exercises

**Exercise 1:** Write three favorite foods to `foods.txt`.

**Exercise 2:** Read `foods.txt` and print each food numbered.

**Exercise 3:** Ask the user for a task and append it to `todo.txt`.

**Exercise 4:** Count how many lines are in a text file.

