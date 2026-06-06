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
s = {1,2,3,5,6,8,12}
s2 = []
print(max(s))
for a in range(1 , max(s)):
  if a in s :
    pass
  else:
    s2.append(a)
print(set(s2))

or 
s = {1,2,3,5,6,8,12}
n = 12
s2 = set(range(1 , n+1))
print(s2-s)

12. Check if two lists have any common elements. 
s1 = [1,2,3,4,5,6]
s2 = [4,5,6,7,8,9]
for a in s1:
  if a in s2:
    print("Common element exist :" , a)

or
s1 = [1,2,3,4,5,6]
s2 = [4,5,6,7,8,9]
s1 = set(s1)
s2 = set(s2)
print(s1.intersection(s2))


13. Convert a set of strings into uppercase. 
s = {"hello" , "my "," name ", "is" , "aakash tyagi"}
for word in s:
  print(word.upper())

14. Identify unique vowels in a given string using a set. 
str = "aakash tyagi ".lower()
s = {"a","e", "i", "o","u"}
s1 = set()
for a in str:
  if a in s:
    s1.add(a)
print(s1)

15. Find elements that appear only once in a list. 
li = [1,2,3,4,1,2,3,4,5,6]
res = set()
for a in li:
  if li.count(a) == 1:
    res.add(a)
print(res)

====================================================================================================================
Basic 
1. Create a dictionary and print all keys and values. 
d = {1:"I am", 2:"Aakash", 3:"Tyagi"}
print(d)
print(d.values())
print(d.keys())
print(d.items())

2. Count frequency of each word in a sentence. 

s = "hello hi hello python hi hello"

d =  {}

for word in s.split():
  if word in d:
    d[word] = d[word] + 1   # like ==> 1 + 1 = 2
  else:
    d[word]= d[word] + 1
print(d)

or

s = "hello hi hello python hi hello"
d = {}
for word  in s.split():
  if word not in d:
    d[word] = 1
  else:
    d[word] = d[word]+1     # like ==> 1 + 1 = 2
print(d)

3. Merge two dictionaries. 
d1 = {1:"Aakash" , 2:"Tyagi"}
d2 = { 2:"Tyagi G" , 3: "783822"}
d1.update(d2)
print(d1)


4. Find the length of a dictionary. 
d = {1: " hello " , "aakash": 2, "3":"tygau"}
print(len(d))

5. Check if a key exists in a dictionary. 
d = {1: " hello " , "aakash": 2, "3":"tygau"}
print(d.get(3, "Not Available"))

or
d = {1: " hello " , "aakash": 2, "3":"tygau"}
x = 1
if d.get(x):
  print("Available")
else:
  print("Not Available ")

Intermediate 

6. Sort a dictionary by values. 
d = {'a': 50, 'b': 40, 'c': 30 , 'd' : 20 , 'e': 10}
res = sorted(d , key=d.get )      # Ascending
res = sorted(d , key=d.get , reverse=True)    # Desending

for v in res:
  print(v, d[v])



7. Find the key with the maximum value. 
d = {'a': 3, 'b': 1, 'c': 2}
x = max(d # yaha par ye d (dictionary par sorted lagaya hai to c dega lekin key =d.get hone par values jo aygi uske basis par sort krega )      , key=d.get)    # d.get ==> means ye values lata hai or yaha par ye values k basis par comapare krega 
print(x ,  " = " , d[x])

or 
x = max(d, key=d.get)
print(x, d.get(x))


8. Remove a key from a dictionary. 
d= {1:"Aakash" ,  2 : "Kumar " ,  3:"Tyagi"}
print(d.popitem())
print(d)

9. Convert two lists into a dictionary. 
li1 = [1,2,3,4,5]
li2 = ["Hello" , "my", "name" ,"is" , "Avi Tyagi"]
res = dict(zip(li1, li2))
print(res)


Or 

li1 = [1,2,3,4,5]
li2 = ["Hello" , "my", "name" ,"is" , "Avi Tyagi"]
res = {}
for a in range(len(li1)):
  print(a)
  res[li1[a]] = li2[a]

    # How to work ====>  {  1: "Hello" }
print(res)

10. Count character frequency using a dictionary. 
s = "aakash"
d = {}

for ch in s:
  if ch not in d:
    d[ch] = 1     # ==> {'a': 1}
  else:
    d[ch] = d[ch] + 1
print(d)


"""
































      
  


  
    
    




  
