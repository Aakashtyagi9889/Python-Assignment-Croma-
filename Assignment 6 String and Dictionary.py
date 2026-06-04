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
"""



      
  


  
    
    




  
