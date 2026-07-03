

a = "sagar"
b = 10
print (len(a) != b)


a = "sagar nagireddi"
b = 15
if (len(a) != b):
    print ("Add initial")
else:
    print(f"Your name is {a}")



number = 11
if number % 2 == 0:
    print("even")
else:
    print("odd")


grade = float(input("What is your Grade Buddy?"))
if grade >= 90:
    print("Grade A")
elif grade >= 80:
    print("Grade B")
elif grade >= 70:
    print("Grade C")
else:
    print("Better Luck Next Time")



jobsapplied = int(input("How many jobs applied?"))
isenough = True
nojob = False
if jobsapplied < 100 and isenough and not nojob:
    print("you need to apply more jobs")






Exercises:


number = int(input("Enter Number"))
if  0 <= number or 0 >= number:
    print(f"your {number}")



age = int(input("what is your age buddy?"))
if 0 <= age <= 12:
    print("Child")
elif 13 <= age <= 17:
    print("Teen")
elif 18 <= age <= 64:
    print("Adult")
elif age >= 65:
    print("Senior")



year = int(input("Enter an year.."))
if year % 100 == 0:
   if year % 400 == 0:
       print("Leap year")
   else:
       print("not leap year")
elif year % 4 ==0:
    print("Leap year")
else:
    print("not leap year")


year = int(input("Enter an year.."))
if (year % 400 == 0) or (year%4 == 0 and year%100 !=0):
    print("leap year")
else: print("not a leap year")


a = int(input("enter a"))
b = int(input("enter b"))
op = input("Operator: ")
if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    if b==0:
        print("Cannot divide by zero")
    else:
        print("Division: ", a/b)
else:
    print("invalid operator")