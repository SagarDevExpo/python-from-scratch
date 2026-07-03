

for char in "Satish":
    print(char, end = ", ")


names = ["priyanka", "keerthi", "nayan"]
for name in names:
    print (f"I love {name}")


for i in range(5):
    print(i)

for i in range(50, 0, -5):
    print(i)

for i in range(10, 0, -1):
    print(i)


for _ in range(10):
    print("Sagar!")


names = ["","priyanka", "keerthi", "nayan"]
for i in range(len(names)):
    print(f"{i}: {names[i]}")


names = ["","priyanka", "keerthi", "nayan"]
for i, babe in enumerate(names):
    print(f"{i}: {babe}")


names = ["priyanka", "keerthi", "nayan"]
for i, babe in enumerate(names, start=1):
    print(f"{i}: {babe}")
print()


for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i,j}", end=" ")
    print()
        
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()


for babe in range(1,6):
    print(" ^" * babe)



numbers = [11, 13, 14, 15, 16]
target = 12
found = False
for i in numbers:
    if i == target:
        found = True
        break
if found: print(f"Target- {target}: {found}")

else: print(f"{target} not found : {found}")



text = "jabalakadi"
count = 0
for char in text:
    if char == 'a':
        count += 1
print(f"a is {count} times in {text}")



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = []
for i in numbers:
    if i%2 != 0:
        odd.append(i)
print(f"Odd Numbers: {odd}")


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for i in range(1, 20):
    if i%2 == 0:
        evens.append(i)
total = sum(evens)
print(f"sum of {evens} : {total}")




Exercises:


numbers = []
for i in range(1, 50):
    if i%7 == 0:
        numbers.append(i)
print(numbers)




text = "programming is fun"
vowels = ["a","e","i","o","u"]
count = 0

for i in text:
    if i in vowels:
        count += 1
print(count)



for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()



num = [3, 7, 2, 9, 1, 5]
large = num[0]

for i in num:
    if i > large:
        large = i
print(large)


num = [3, 7, 2, 9, 1, 5]
small = num[0]
for i in num:
    if i < small:
        small = i
print(small)



for i in range(1, 31):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i)