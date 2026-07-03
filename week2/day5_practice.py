

user = input("Give me a sentence...").lower().strip()
dick = {}
for i in user:
    if i == " ":
        continue
    dick[i] = dick.get(i,0) + 1

for j, num in dick.items():
    print(f"{j} : {num}")


ls = [11, 12, 13, 14, 15]
k = 3
for i in range(k):
    last = ls.pop()
    ls.insert(0,last)
print(ls)


ls = [11, 12, 13, 14, 15]
k = 2
print(ls[-2:]+ls[:-2])
k=3
print(ls[-3:]+ls[:-3])



text = "The quick brown fox jumped over the lazy dog"
sli = text.split()
longest = ""
for word in sli:
    if len(word) > len(longest):
        longest = word
print(longest)



nums = [2, 7, 11, 15, 12, 4, 2, 3, 1, 6]
target = 9
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j] == target:
            print(f"{nums[i]} + {nums[j]} = {target}")



for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i*j}", end= " ")
    print()


for i in range(1, 4):
    for j in range(1, i+1):
        print(f"{j}", end= " ")
    print()





matrix = []
for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(i*j)
    matrix.append(row)
for z in matrix:
    for num in z:
        print(f"{num}", end= " ")
    print()



txt1 = "aaabbbccca"
comp = ""

for i in range(1, len(txt1)): 
    count = 1
    for j in range(i+1, len(txt1)):
        if txt1[i] == txt1[j]:
            count += 1
        else:
            comp += txt1[j-1]+str(count)
            count = 1
print(comp)



txt1 = "aaabbbccca"
compressed1 = ""
count = 1

for i in range(1, len(txt1)):
    if txt1[i] == txt1[i-1]:
        count += 1
    else:
        compressed1 += txt1[i-1] + str(count)
        count = 1

compressed1 += txt1[-1] + str(count)

if len(compressed1) < len(txt1):
    print(compressed1)
else:
    print(txt1)