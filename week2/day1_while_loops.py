

count = 0
loop = int(0)
while count <= 5:
    print (f"Count: {count}")
    count += 1
    loop += 1
print (f"Process Completed {loop} times")



n = 0
while n <= 10:
    if n < 10:
        print (n, end=",")
    else:    print (n, end="")
    n += 2
print ()


num = 1
total = 0
while num <=100:
    total += num
    num += 1
print(total)


while True:
    name = input("Enter first name:").strip().lower()
    if name == "sagar":
        break
    print(f"Wrong first name: {name}")
print(f"Hi {name.capitalize()}")




while True:
    a = int(input("Enter number"))
    if a%2 == 0:
        print(f"Thanks for the even number {a}")
        break
    else:
        print("I need even number")



i = 0
while i < 10:
    i += 1
    if i%2 == 0:
        print("even", end=" ")
        continue
    print(i, end=" ")



import random

game = random.randint(1,5)
tries = 0

while True:
    num = int(input("Enter the number: Let's play"))
    tries += 1
    if num == game:
        print(f"you won in {tries} attempts")
        break
    elif num < game:
        print("you have lesser number")
    else:
        print("you have greater number")



Exercises:

num = int(input("Enter the number for the table you want?"))
i = 1
while i <= 10:
    result = num*i
    print(f"{num} x {i} = {result}")
    i += 1



list = int()

while True:
    num = int(input("keep entering numbers you want... :)"))
    list = list+num
    if num == 0:
        print(f"sum of all numbers you gave.. {list}")
        break


total = 0 

while True:
     num = int(input("keep entering numbers you want... :)"))

     if num == 0:
         break
     
     total += num
print(total)



n = 1
while True:
    j = 2**n
    if j > 1000:
        break
    n += 1
print (f"the 2 power of {n} is {j}")


n = 1
count = 0
while n <= 1000:
    n *= 2
    count += 1
print(n)
print(count)



num = 10
while num >= 1:
    if num % 3 != 0:
        if num > 1:
            print(num, end = ", ")
        else:
            print(num, end=" ")
    num -= 1


num = 10
first = True
while num >= 1:
    if num % 3 != 0:
        if not first:
            print(", ", end = "")
        print(num, end="")
        first = False
    num -= 1


num = 10
while num >= 1:
    if num % 3 == 0:
        num -= 1
        continue
    elif num > 1:
            print(num, end = ", ")
    else:
        print(num, end=" ")
    num -= 1
    
    # if num > 1:
    #     print(num, end = ", ")
    # else:
    #     print(num, end=" ")
    