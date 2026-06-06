"""
                                        String Programming Questions Basic 

1. Write a program to count the number of vowels in a string. 
Name = "Aakash"
Name = Name.lower()
count = 0
for a in Name:
    if a in "aeiou":
      count= count + 1
print(count)
  
2. Reverse a string without using built-in functions. 
Name = "Aakash"
str = ""
for a in Name:
  str = a + str
print(str)

3. Check whether a string is a palindrome. 
str = input("Enter Text : ")
if str == str[::-1]:
  print("Palindorme")
else:
  print("Not palindrome")
  
4. Count uppercase and lowercase letters in a string.
str = "Aakash Tyagi"
small = 0
largest = 0
for a in str:
  a = ord(a)                      # converting value in ascii value 
  if a >96 and a<123:
    small = small+1
  elif a>64 and a <91:
    largest +=1
print(small)
print(largest)

or
str = "Aakash Tyagi"
upper = 0
small = 0
for a in str:
  if a.isupper():
    upper+=1
  elif a.islower():
    small += 1
print("Smaller : ",small)
print("Upper : ",upper)

or

str  = "Aakash Tyagi"
upper= 0
small=0
for a in str:
  if a >= "a" and a<="z":
    small+=1
  elif a>="A" and a<="Z":
    upper+=1
print(small)
print(upper)

5. Replace all spaces in a string with _. 
str  = "Aakash Kumar Tyagi"
str = str.replace(" " , "_")
print(str)


Intermediate 
6. Find the frequency of each character in a string.
str = "Tyagi"
for a in str:
  x = str.count(a)
  print(x) 

7. Remove duplicate characters from a string. 
str = "aakash"
str2 = ""
for a in str:
  if a not in str2:
    str2 = str2 + a
print(str2)

8. Find the first non-repeating character in a string. 
str = "tyagi"
str2 =""
for a in str:
  x = str.count(a)
  if x == 1 :
    str2 =  str2 +a
    print(str2)
    break
    
9. Check if two strings are anagrams. 
s1 =  "Listen"
s2 = "silent"
if  sorted(s1.lower())  ==  sorted(s2.lower()):
  print("Anagram")
else:
  print("Not Anagram")

  or 

s1 =  "Listen".lower()
s2 = "silent".lower()
count = 1
for a in s1:
  if s1.count(a) !=  s2.count(a):
   count = 0
   break
if count :
 print("Anagram")
else:
 print("Not")

10. Convert "hello world" → "Hello World" (title case without using .title()). 
str  = "hello World"
result = ""
for a in str.split():
  result = result + a[0].upper() + a[1:] +" "
print(result)
 ===================================================================================================================
Tricky 
11. Find the longest word in a sentence. 
str = " hello My name is Aakash Tyagi "
longest  = ""
for word in str.split():
  if len(word) > len(longest):
    longest = word
print(longest)

12. Compress a string like "aaabbc" → "a3b2c1". 
s= "aaabbc"
li = ""
c= 0
for a in s:
  if s.count(a)>=1 and (a not in li):
    c= s.count(a)
    li = li + a + str(c)
print(li)

13. Count words, characters, and digits in a string. 
s = "Aakash Tyagi 783822 ".lower()
res = 0
res1 = 0
res2 = 0
for word in s.split():
  res = res + s.count(word)
print("Word : " , res)

for ch in s:
  if ch >="a" and ch<="z":
    res1 = res1 + 1

  elif ch >= "0" and ch<="9":
    res2 = res2+1
print("Ch: " , res1)
print("Digit : " , res2)

14. Rotate a string left by n positions. 
s  = "python"
n =  2
str = ""
str =  s[n:] + s[:n]
print(str)

          Or

s  = "python"
n =  2
str = ""
for a in range(n , len(s)):
  str = str + s[a]
# print(str)
for a in range(n):
  str  = str + s[a]
print(str)


15. Find all substrings of a given string. 
s =  "abc"
#  str = "" agar ise yaha rakhege to string empty nahi hoga  usi mai element add hote rhege 
for k in range(len(s)):
  str = ""    # यहाँ str फिर से empty हो गया।
  for i in range(k , len(s)):
    str= str + s[i]
    print(str)
=============================================================================================================
Set Programming Questions 
Basic 
1. Create a set and add elements dynamically. 
s = set()
s.add(21)
s.add(22)
s.add(23)
s.add(24)
print(s)

2. Find the union and intersection of two sets. 
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print(s1&s2)  # intersection
print(s1|s2)  # union
print(s1.intersection(s2))  # intersection
print(s1.union(s2)) # union

3. Remove duplicate elements from a list using a set. 
li = [1,2,2,3,2,1,2,4,5]
li= list(set(li))
print(li)

4. Check if an element exists in a set. 
s =  {1,2,3,4,5}
x = 9
if x in s:
  print("Yes")
else:
  print("no")

5. Find the difference between two sets. 
s1=  {1,2,3,4,5}
s2=  {1,2,6,7,8}
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

Intermediate 
6. Find common elements in two lists using sets. 
s1=  {1,2,3,4,5}
s2=  {1,2,6,7,8}
print(s1.intersection(s2))

7. Check whether one set is a subset of another.
s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6,7,8,9}
print(s1.issubset(s2))

loop --
s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6,7,8,9}
flag = True
for i in s1:
  if i not in s2:
    flag= False
    break
if flag:
  print("subset")
else:
  print("not")

or 
s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6,7,8,9}
if s1 <= s2:
  print("subset")
else:
  print("not")
  
8. Find symmetric difference of two sets. 
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print(s1.symmetric_difference(s2))

9. Count unique elements in a list using a set. 
s1 = [1,2,3,4,5,6,1,2,3]
s1 = len(set(s1))
print(s1)

# if you want to find the unique element like 4,5,6 in list using set 
==> s1 = [1,2,3,4,5,6,1,2,3]
    s2 = []
    for a in s1:
      if s1.count(a) == 1:
        s2.append(a)
    s2 = set(s2)
    print(s2)

10. Remove all common elements from two sets. 
s1 = {1,2,3,4,5,6,"aakash"}
s2 = {4,5,6, 7,8,9, "aakash"}
print(s1.symmetric_difference(s2))

Tricky 
11. Find missing numbers from 1 to n using sets. 

"""





























      
  


  
    
    




  
