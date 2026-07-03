


name = "  Sagar  "
print(name.strip().lower().capitalize())


count = 0
if count:
    print("yes")
else:
    print("no")



user = input("enter username?").strip()
passw = input("enter password?")
if not user and not passw:
    print("Enter username and password..!")
elif not user:
    print("Enter username..!")
elif not passw:
    print("Enter password..!")
elif len(passw) < 8:
    print("Password must be atleast 8 characters..!")
else:
    print("Login Succeed..!")



num = float(input("Enter Number.."))
label = ""
if num != 0:
    if num%2 == 0:
        label += "even"
    else:
        label += "odd"
    if num < 0:
        label += ", negative"
    elif num > 0:
        label += ", positive"
    if num%3 == 0:
        label += ", divisible by 3"
    if num%5 == 0:
        label += ", divisible by 5"
else:
    label += "zero"
print(label)



cmd = input("Enter command..").strip().lower()

match cmd:
    case "start":
        print("Started")
    case "stop":
        print("Stopped")
    case "restart":
        print("Restarted")
    case "status":
        print("Status")
    case _:
        print("Invalid command")




total = 0
count = 0
while True:
    num = int(input("Enter number.."))
    if num == 0:
        break
    else: 
        total += num
        count += 1
print(total)
print(count)
print(f"average : {(total/count):.2f}")




basenum = int(input("Enter base number"))
limit = int(input("Enter limit"))
n = 1
power = 0

while n<=limit:
    n = basenum * n
    power += 1

print(f"{basenum}^{power} = {n}")




word = input("Enter a word..").lower().strip()
vowels = "aeiou"
newword = ""
for char in word:
    if char in vowels:
        newword += "*"
    else:
        newword += char
print(newword)


##slicing
nums = [1, 2, 3, 4, 5]
rotate1 = nums[-2:] + nums[:-2]
rotate2 = nums[2:] + nums[:2]
print(rotate1, rotate2)


##pop() / insert() / append()
nums = [1, 2, 3, 4, 5]
right = []
left = []
k = 2
for i in range(k):
    last = nums.pop(-1)
    nums.insert(0,last)
right.append(nums)
print(right)
nums = [1, 2, 3, 4, 5]
for i in range(k):
    first = nums.pop(0)
    nums.insert(4,first)
left.append(nums)
print(left)






txt = "The checkout flow no longer calls the internal monolith payment method".lower()
newt = txt.split()
best = ""
for i in range(len(newt)):
    if len(newt[i]) > len(best):
        best = newt[i]
print(best)



txt = "The checkout flow no longer calls the internal monolith payment method".lower()
best = ""
for word in txt.split():
    if len(word) > len(best):
        best = word
print(best)



##Idea is dictionary[key] = dictionary.get(key, 0) + 1
text = "Hello World 123"
newt = {}
for char in text:
    if char.isupper():
        newt["upper"] = newt.get("upper",0) + 1
    elif char.islower():
        newt["lower"] = newt.get("lower",0) + 1
    elif char.isdigit():
        newt["digits"] = newt.get("digits",0) + 1
print(newt)



#logic is
#Compare with next: use range(len(txt) - 1)
#Compare with previous: use range(1, len(txt))
txt = "abcd"
newt = ""
count = 1
for i in range(1, len(txt)):
    if txt[i] == txt[i-1]:
        count += 1
    else: 
        newt += txt[i-1]+str(count) 
        count = 1
newt += txt[-1]+str(count) 
if len(txt) > len(newt):
    print(newt)
else: print(txt)