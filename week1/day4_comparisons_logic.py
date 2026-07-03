
count = [1,2]
if count:
    print (f"list is not empty, {count}")


money = int(input("How much do you have"))
result = "you are safe" if money >= 2000 else "danger"
print (f"{result} you have {money}")



command = input("input command to the server").strip().lower()

match command:
    case "start":
        print ("starting the server...")
    case "stop":
        print ("stopping the server..")
    case _:
        print ("invalid command")



a = 11
b = 12
c = 9

print (f"Maximum {max(a,b,c)}")



value = 90
clamped = max(0, min(100, value))  # Keep between 0 and 100
print(f"{value} clamped to 0-100: {clamped}")  # 100



value = -1
clamp = min(max(-5, value), 20)
print(f"{clamp}")


flag = True
flag = not flag
print (f"flag is now {flag}")


char = "100"
print(f"'{char}' is a letter: {char.isalpha()}")
print(f"'{char}' is a digit:  {char.isdigit()}")
print(f"'{char}' is uppercase: {char.isupper()}")
print(f"'{char}' is lowercase: {char.islower()}")


result = 90
if result is not None:
    print (f"result is {result}")



Exercises:

number = float(input("enter number"))
result = "fizz" if number % 3 == 0 else "not fizz"
print (f"{result}")


Day = input("Enter day").strip()
match Day:
    case "monday" | "tuesday":
        print("Weekday")
    case "sunday":
        print("Weekend")
    case _:
        print("Invalid")



a = 14
b = 16
c = 12
if a>b and a>c:
    print(f"{a}")
elif b>a and b>c:
    print(f"{b}")
else:
    print(f"{c}")


username = input("Enter username")
password = input("Enter password")
if not username.strip() and not password.strip():
    print("Enter username and password")
elif not username.strip():
    print("Enter username")
elif not password.strip():
    print("Enter password")
elif len(password)<8:
    print("Password too short")
else:
    print("login succeed")
