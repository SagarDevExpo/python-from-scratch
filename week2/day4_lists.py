

names = ["sagar","kavya","satya","lalitha"]
print(names[1])


names = ["sagar","kavya","satya","lalitha"]
print(len(names))
names[3] = "gundu"
print(names)


names = ["sagar","kavya","satya","lalitha"]
names.append("baby")
print(names)


names = ["sagar","kavya","satya","lalitha"]
names.insert(0,"we")
print(names)


names = ["sagar","kavya","satya","lalitha"]
names.insert(0,"we")
names.extend(["are","family"])
print(names)


names = ["sagar","kavya"] + ["satya","lalitha"]
names.insert(0,"we")
names.extend(["are","family"])
print(names)


names = ["sagar","kavya"] + ["satya","lalitha"]
names.insert(0,"we")
names.extend(["are","family"])
names.pop(0)
print(names)


names = ["sagar","kavya","satya","lalitha"]
names.remove("sagar")
print(names)


names = ["sagar","kavya","satya","lalitha"]
del names[0]
print(names)


names = ["sagar","kavya","satya","lalitha"]
print("sagar" in names)
print(names.count("lalitha"))


nums = [1,3,5,6,2,4,1,4]
# nums.sort()
newl = sorted(nums)
print(newl)


names = ["sagar","kavya","satya","lalitha"]
sis = [1,2]
# for name in names:
#     print(name)
# for i, name in enumerate(names):
#     print(f"{i} : {name}")

for name, rel in zip(names,sis):
    print(f"{rel}: {name}")



nums = [1,2,3,4,5]
left = 0
right = len(nums)-1
print(nums[left], nums[right])
while left <= right:
    print(f"Left: {nums[left]}, Right: {nums[right]}")
    left += 1
    right -= 1


nums = [7, 2, 9, 4, 1]
maxv = nums[0]
for num in nums:
    if num > maxv:
        maxv = num
print(maxv)


a = [1,2,3]
b = a
# b = a[:]
print(b)




Exercises:


nums = [7, 2, 9, 4, 1]
total = 0
largest = nums[0]

for num in nums:
    total += num
    if num > largest:
        largest = num
average = total/len(nums)
print(f"Sum: {sum}, Average: {average}, Largest: {largest}")




nums = [4, 2, 7, 1, 9, 3]
evens = []
for i in nums:
    if i%2 == 0:
        evens.append(i)
print(evens)



nums1 = [1, 2, 3, 4, 5]
nums2 = [4, 5, 6, 7, 8]
nums3 = []

for i in nums1:
    if i in nums2:
        nums3.append(i)
print(nums3)



nums = [1, 2, 3, 4, 5]
newl = []
for i in nums:
    newl.insert(0,i)
print(newl)


nums = [1, 2, 3, 4, 5, 6, 7]
left = 0
right = len(nums)-1
while left < right:
    nums[left],nums[right] = nums[right],nums[left]
    left += 1
    right -= 1
print(nums)


nums = [0, 1, 0, 3, 12]
newl = []
count = 0
for i in nums:
    if i == 0:
        count += 1
    else:
        newl.append(i)
for j in range(count):
    newl.append(0)
print(newl)



nums = [0, 1, 0, 3, 12]
newl = []
position = 0
for i in nums:
    if i != 0:
        newl.append(i)
        position += 1
while position < len(nums):
    newl.append(0)
    position += 1
print(newl)



nums = [0, 1, 0, 3, 12]
newl = []

for i in nums:
    if i != 0:
        newl.append(i)

while len(newl) < len(nums):
    newl.append(0)

print(newl)
