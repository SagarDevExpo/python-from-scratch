

def sagar():
    print("I love you sagar")
    print("I love baby")
sagar()
sagar()


def kick(name):
    print(f"name: {name}")
kick("sagar")


def kick(a,b):
    result = a+b
    print(f"{a} + {b} = {result}")
kick(2,3)


def say_hi():
    return "Hi"

x = say_hi() 
print(f"{x}")



age = int(input("Enter age"))
def check(age):
    
    if age < 0:
        return "Invalid age"
    if age >= 18:
        return "Adult"
    return "Minor"
x = check(age)
print(x)



def power(base, exp=2):
    return base ** exp
print(power(5))
print(power(2,4))


def min_max(numbers):
    return max(numbers), min(numbers)
a, b = min_max([1,2,3,4,5,6,7])
print(f"{a}, {b}")



def divide(a, b):
    return a//b, a%b
q, r = divide(17, 5)
print(f"17 % 5 = {q} {r}")



def my_func():
    local_v = "I exist inside"
    print(local_v)
my_func()
# print(f"{local_v}")



def my_fuc(x):
    x = x * 2
    return x
num = 5
result = my_fuc(num)
print(f"{result}")



def find_target(nums, target):
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1 