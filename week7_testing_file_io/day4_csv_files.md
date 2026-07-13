# Day 4: CSV Files

**Time:** ~40 minutes

Today you learn:
1. What CSV files are
2. `csv.reader`
3. `csv.DictReader`
4. Writing CSV rows

**Practice file:** Create `day4_practice.py`

---

## Part 1: What Is CSV?

CSV means comma-separated values.

```text
name,score
Ana,90
Ben,85
Cara,95
```

CSV is common for spreadsheets and simple datasets.

---

## Part 2: Read CSV Rows

```python
import csv

with open("scores.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

Each row becomes a list of strings.

---

## Part 3: DictReader

```python
import csv

with open("scores.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["score"])
```

`DictReader` uses the first row as column names.

### 🧩 `reader` vs `DictReader` — same file, two views

Given this file:

```text
name,score
Ana,90
Ben,85
```

**`csv.reader`** hands each row back as a plain **list**, and you grab columns by *number*:

| row | you get | `row[0]` | `row[1]` |
|-----|---------|----------|----------|
| 1 | `['name', 'score']` | `'name'` | `'score'` |
| 2 | `['Ana', '90']` | `'Ana'` | `'90'` |
| 3 | `['Ben', '85']` | `'Ben'` | `'85'` |

Notice the header row comes back too — you deal with it yourself. And `row[0]` / `row[1]` are easy to mix up.

**`csv.DictReader`** is smarter: it reads the first row as **column names**, then hands every following row back as a **dict**, so you grab columns by *name*:

| row | you get |
|-----|---------|
| 1 (Ana) | `{'name': 'Ana', 'score': '90'}` → `row['name']` = `'Ana'` |
| 2 (Ben) | `{'name': 'Ben', 'score': '85'}` → `row['score']` = `'85'` |

The header is used up automatically, and `row['name']` is far clearer than `row[0]`. Prefer `DictReader` when the file has headers. Note: everything comes back as a **string**, so `int(row['score'])` before doing math.

---

## Part 4: Write CSV

```python
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerow({"name": "Sagar", "score": 100})
```

---

## Exercises

**Exercise 1:** Create `scores.csv` manually and read it with `DictReader`.

**Exercise 2:** Find the highest score in the CSV.

**Exercise 3:** Ask the user for name and score, then append to `scores.csv`.

**Exercise 4:** Convert a list of dictionaries into a CSV file.

