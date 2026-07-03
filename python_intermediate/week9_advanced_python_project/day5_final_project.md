# Day 5: Final Intermediate Project

**Time:** ~60–90 minutes

Today you build a small command-line contact manager using the topics from
these intermediate weeks.

**Project folder:** Create `contact_manager/`

---

## Goal

Build a program that can:

1. Add a contact
2. List contacts
3. Search contacts
4. Save contacts to CSV
5. Load contacts from CSV

---

## Suggested Structure

```text
contact_manager/
├── app.py
├── contacts.py
└── test_contacts.py
```

---

## Requirements

Use:

- exceptions for invalid input
- regex for email validation
- a `Contact` class
- CSV for saving/loading
- functions that can be tested
- type hints and docstrings

---

## Step 1: Contact Class

Create a `Contact` class with:

- name
- email
- phone
- `__str__`

Validate that name is not empty.

---

## Step 2: Email Validation

Write:

```python
def is_valid_email(email: str) -> bool:
    ...
```

Use regex.

---

## Step 3: CSV Save and Load

Write:

```python
def save_contacts(filename: str, contacts: list[Contact]) -> None:
    ...

def load_contacts(filename: str) -> list[Contact]:
    ...
```

---

## Step 4: Menu

In `app.py`, create a while-loop menu:

```text
1. Add contact
2. List contacts
3. Search contacts
4. Save
5. Quit
```

---

## Step 5: Tests

Test:

- valid email
- invalid email
- contact creation
- search function

---

## Graduation Check

If you can build this slowly, even with mistakes, you are ready to continue to
`dsa_weeks/` with a much stronger Python base.

