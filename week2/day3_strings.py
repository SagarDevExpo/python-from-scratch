

s = "Hello Sagar"
print(s[0])
print(s[0:10].count(""))



s = "sagar"
rev = s[::-1]
print (f"Is palindrome: {s == rev}")



s = "I love AWS"
spl = s.split(" ")
rej = "^".join(spl)
print(rej)


s = "I love AWS"
print (s.replace("I", "We"))


for i in range(6,0,-1):
    for j in range(1, i+1):
        print(f"{j}", end= " ")
    print()


count = 0
for i in "sagar":
    if i == "a":
        count +=1
        continue
    print(i, end=" ")
print()
print (f"skipped a {count} times")



txt = "banana"
freq = {}
for i in txt:
    if i == "a":
        freq[i] = freq.get(i, 0)+1
print(f"Frequencies: {freq}")


for char in "sagar":
    print(char, end= " ")



print(ord('a'))
print(chr(98))

print(ord('A'))
print(chr(66))



for char in range(65, 100):
    if chr(char) == "Z":
        print(f"{char}:" , chr(char))
        break
    else:
        print(f"{char}:",  chr(char))


dick = {}
for char in "sagar":
        dick[char] = ord(char)
print(dick)





text = "shakalaka boom boom"
no_boom = {}
for word in text.split():
    if word == "shakalaka":
        no_boom[word] = len(word)
print(no_boom)





Exercises:


word = input("Enter word for palindrome testing?")
# reverse = word[::-1]
print (f"Reverse of your {word} : {word[::-1]}")
print()
if word == word[::-1]:
    print("Nice you have a palindrome baby!")



text = "Hello World 123"
count = {}
for char in text:
    if char.isupper():
        count["upper"] = count.get("upper", 0) + 1
    elif char.islower():
        count["lower"] = count.get("lower", 0) + 1
    elif char.isdigit():
        count["digits"] = count.get("digits", 0) + 1
print(count)



text = "the quick brown fox jumps over the lazy dog"
for word in text.split():
    count = 0
    for char in word:
        count += 1
    if count > 3:
        print(word, end = " ")
    else: continue


text = "the quick brown fox jumps over the lazy dog"
for word in text.split():
    if len(word) > 3:
        print(word, end = " ")
    else: continue


word = "programming"
vowels = "aeiou"
new_word = ""
for char in word:
    if char not in vowels:
        new_word += char
    elif char in vowels: 
        char = "*" 
        new_word += char
print(new_word)


word = "programming"
vowels = "aeiou"
new_word = ""
for char in word:
    if char in vowels:  
        new_word += "*"
    else:
        new_word += char
print(new_word)


word1 = "Listen".lower()
word2 = "Silent".lower()
if sorted(word1) == sorted(word2):
    print("Baby these are anagrams!")
else: print("They are distict")