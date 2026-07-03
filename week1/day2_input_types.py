age = input("What is your age?")
print (age)


money_lend = int(200)
money_spent = int(50)
# money = int(money_lend)
Remaining_money = money_lend - money_spent
print("Money you have is", Remaining_money)


salary = float(200.5)
week_salary = salary * 7
print ("My weekly salary is", week_salary)


name = "Sagar"
salary = float(input("what is your daily salary?"))
week_salary = salary * 7
print (f"My name is {name} and My weekly salary is {salary*7:.3f}")




name = "Sagar"
salary = input("What is your salary")
if salary.isdigit():
    salary = int(salary)
    print (f"{name} your salary is doubled {salary*2}")
else: 
    print (f"{name}, no bonus this year")


text = "Hello"
print("bello" in text) 
print(len(text))
print(text.strip())





Exercises:

name = input("what is your name")
birth_year = input("what is your birth year?")
if birth_year.isdigit():
    birth_year = int(birth_year)
    year = 2026 - birth_year
    print (f"Hello {name} you age is {year}")
else: 
    print("Go to Hell")



price = float(input("What is the cost of this puff"))
quantity = float(input("How many do I need?"))
print (f"The price for {quantity} puffs is {quantity * price}")


tempF = int(input("What is the temp in farenheit"))
tempC = int((tempF-32) * 5/9)
print (f"The temp you gave in Farenheit {tempF} in Celcius is {tempC}")


firstname = input("What is your first name")
lastname = input("What is your lastname")
print (firstname.upper(),lastname.upper())
print (firstname.lower(),lastname.lower())