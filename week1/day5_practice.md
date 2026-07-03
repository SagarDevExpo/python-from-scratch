# Day 5: Week 1 Practice — Reinforce Everything

**Time:** ~30 minutes

NO new concepts today! Just practice.
Try to solve these **WITHOUT looking at previous files**.
If stuck for 5+ minutes, peek at the relevant day's `.md` file.

**Practice file:** Create `day5_practice.py`

---

## Warm-Up: Fill in the blanks

Try writing these from memory:

1. Store your name and print a greeting using an f-string
2. Get a number from user, double it, print the result (remember to convert!)
3. Check if a number is positive or negative using if/else

---

## Challenge 1: Temperature Advisor

Ask the user for the temperature (as a number).
Print advice based on the temperature:
- Below 0: `"Freezing! Stay inside."`
- 0-15: `"Cold. Wear a jacket."`
- 16-25: `"Nice weather!"`
- 26-35: `"Warm. Stay hydrated."`
- Above 35: `"Too hot! Find shade."`

---

## Challenge 2: Simple Tip Calculator

Ask for:
1. The bill amount (decimal number)
2. The tip percentage (whole number, like 15 or 20)
3. Number of people splitting the bill

Calculate and print:
- Tip amount
- Total (bill + tip)
- Amount per person

Example: bill=$100, tip=20%, people=4
→ `Tip: $20.00, Total: $120.00, Per person: $30.00`

Use f-strings with `:.2f` for money formatting.

---

## Challenge 3: Number Classifier

Ask for a number. Print **ALL** that apply:
- `"Even"` or `"Odd"`
- `"Positive"`, `"Negative"`, or `"Zero"`
- `"Divisible by 5"` (if it is)
- `"Divisible by 3"` (if it is)

Example: 15 → `Odd, Positive, Divisible by 5, Divisible by 3`
Example: -4 → `Even, Negative`

---

## Challenge 4: Password Strength Checker

Ask the user to create a password. Rate its strength:

- Less than 6 characters: `"Weak"`
- 6-9 characters: `"Medium"`
- 10+ characters: `"Strong"`

**BONUS:** If the password contains a digit (any number), add `" + has number"`.
Hint: You can use `any(char.isdigit() for char in password)` — you'll learn how this works in Week 2.

---

## Challenge 5: Mini Quiz Game

Create a 3-question quiz:
1. Ask a question
2. Get the user's answer
3. Check if correct (case-insensitive!)
4. Track the score
5. Print final score at the end

Example questions (or make your own):
- "What is the capital of Texas?" → `"Austin"`
- "What language are you learning?" → `"Python"`
- "What does CPU stand for?" → `"Central Processing Unit"`

Hint: Use `.lower()` to make comparison case-insensitive: `answer.lower() == "austin"`

---

## Reflection

After completing these, ask yourself:

1. Can I create a variable and print it without looking anything up?
2. Can I get user input and convert it to a number?
3. Can I write an if/elif/else without errors on the first try?
4. Can I use f-strings comfortably?

If any answer is "no" — that's fine! Repeat those sections tomorrow.
If all "yes" — **you're ready for Week 2 (loops)!**
