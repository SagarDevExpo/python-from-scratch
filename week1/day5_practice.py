"""
DAY 5: Week 1 Practice — Reinforce Everything
Time: ~30 minutes

NO new concepts today! Just practice.
Try to solve these WITHOUT looking at previous files.
If stuck for 5+ minutes, peek at the relevant day's file.

Run: python3 day5_practice.py
"""

# ============================================================
# WARM-UP: Fill in the blanks (uncomment and fix)
# ============================================================

# 1. Store your name and print a greeting
name = "sagar"
print(f"Hello, {name}!")

# 2. Get a number from user, double it, print result
num = int(input("Enter a number: "))
print(f"Doubled: {num * 2}")

# 3. Check if a number is positive or negative
x = -7
if x > 0:
    print("Positive")
else:
    print("Negative or zero")


# ============================================================
# CHALLENGE 1: Temperature Advisor
# ============================================================

"""
Ask the user for the temperature (as a number).
Print advice based on the temperature:
- Below 0: "Freezing! Stay inside."
- 0-15: "Cold. Wear a jacket."
- 16-25: "Nice weather!"
- 26-35: "Warm. Stay hydrated."
- Above 35: "Too hot! Find shade."

Your code here:
"""

temp = float(input("What is the today temparature?"))
if temp < 0:
    print("Freezing! Stay inside.")
elif temp <= 15:
    print("Cold. Wear a jacket.")
elif temp <= 25:
    print("Nice weather!")
elif temp <= 35:
    print("Warm. Stay hydrated.")
else:
    print("Too hot! Find shade.")


# ============================================================
# CHALLENGE 2: Simple Tip Calculator
# ============================================================

"""
Ask for:
1. The bill amount (decimal number)
2. The tip percentage (whole number, like 15 or 20)
3. Number of people splitting the bill

Calculate and print:
- Tip amount
- Total (bill + tip)
- Amount per person

Example: bill=$100, tip=20%, people=4
→ Tip: $20.00, Total: $120.00, Per person: $30.00

Use f-strings with :.2f for money formatting.

Your code here:
"""

bill = float(input("Enter bill amount?"))
tip = int(input("tip percentage?"))
people_count = int(input("How of you are there?"))
tip_amount = float((bill*tip)/100)
Total = float(bill+tip_amount)
print (f"Amount per person: {Total/people_count:.2f}")


# ============================================================
# CHALLENGE 3: Number Classifier
# ============================================================

"""
Ask for a number. Print ALL that apply:
- "Even" or "Odd"
- "Positive", "Negative", or "Zero"
- "Divisible by 5" (if it is)
- "Divisible by 3" (if it is)

Example: 15 → "Odd, Positive, Divisible by 5, Divisible by 3"
Example: -4 → "Even, Negative"

Your code here:
"""

num = int(input("Enter a number.."))

output = ""
if num < 0:
    output = output + "Negative"
elif num >0:
    output = output + ", Positive"
else:
    output += ", zero"
if num%2 == 0:
    output = output + ", Even"
else:
    output = output + ", Odd"
if num%5 == 0:
    output = output + ", Divisible by 5"
if num%3 == 0:
    output = output + ", Divisible by 3"

print (output)





# ============================================================
# CHALLENGE 4: Password Strength Checker
# ============================================================

"""
Ask the user to create a password. Rate its strength:

- Less than 6 characters: "Weak"
- 6-9 characters: "Medium"
- 10+ characters: "Strong"

BONUS: If the password contains a digit (any number), add " + has number"
Hint: You can loop through characters OR use any() with .isdigit()
      But we haven't learned loops yet — so just try:
      has_digit = any(char.isdigit() for char in password)
      (You'll learn how this works in Week 2)

Your code here:
"""

passw = input("Enter password")
has_digit = any(letter.isdigit() for letter in passw)
if len(passw)<6:
    if has_digit:
        print("Weak + has number")
    else: print("Weak")
if 6<=len(passw)<=9:
    if has_digit:
        print("Medium + has number")
    else: print("Medium")
if len(passw)>=10:
    if has_digit:
        print("Strong + has number")
    else: print("Strong")



passw = input("Enter password")
has_digit = any(letter.isdigit() for letter in passw)
if len(passw)<6:
    output = "Weak"
elif 6<=len(passw)<=9:
    output = "Medium"
else:
    output = "Strong"

if has_digit:
    output = output + " + has number"

print(output)




# ============================================================
# CHALLENGE 5: Mini Quiz Game
# ============================================================

"""
Create a 3-question quiz:
1. Ask a question
2. Get the user's answer
3. Check if correct (case-insensitive!)
4. Track the score
5. Print final score at the end

Example questions (or make your own):
- "What is the capital of Texas?" → "Austin"
- "What language are you learning?" → "Python"
- "What does CPU stand for?" → "Central Processing Unit"

Hint: Use .lower() to make comparison case-insensitive
      answer.lower() == "austin"

Your code here:
"""

ques1 = input("Who is the president of America?").strip().lower()
ques2 = input("Who is the president of India?").strip().lower()
ques3 = input("Who is the president of Russia?").strip().lower()

count = 0

if ques1 == "trump":
    count += 1
if ques2 == "modi":
    count += 1
if ques3 == "putin":
    count += 1

print(count)
    



# ============================================================
# REFLECTION (answer in comments or out loud)
# ============================================================

"""
After completing these, ask yourself:

1. Can I create a variable and print it without looking anything up?
2. Can I get user input and convert it to a number?
3. Can I write an if/elif/else without errors on the first try?
4. Can I use f-strings comfortably?

If any answer is "no" — that's fine! Repeat those sections tomorrow.
If all "yes" — you're ready for Week 2 (loops)!
"""

1. yes
2. yes
3. yes
4. yes