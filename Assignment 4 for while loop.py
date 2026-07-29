"""
1. Write a program to print numbers from 1 to 100. 
==>
for a in range(1,100+1,1):
    print(a)

2. Write a program to print all even numbers between 1 and 50. 
==>
for a in range (1 , 51):
    if a%2==0:
        print(a)

3. Write a program to print the sum of first n natural numbers.
==>
result =  0
for a in  range (0, 5):
    result= result+a
print(result)

4. Write a program to print the multiplication table of a given number.
==>
num = int(input("Enter Number "))
result = 0
for a in range(1, 11):
    result = num *a
    print(num , "*", a , "= ", result)

5. Write a program to print all elements of a list using a for loop.
==>
list = [1,2,3,4,5,6,78,89]
for a in list:
    print(a)

6. Write a program to count the number of vowels in a string.
==>
str = input("Enter Your Text : ")
res= "aeiouAEIOU"
count = 0
for a in str:
    if a in res:
        print(a)
        count = count+1
print("Total Count = " , count)

7. Write a program to find the largest number in a list.
==>
list = [1,2,4,2,68,3,6]
for a in list:
    continue
print(max(list))


or

list = [1, 2,3,4,56,8,9]
largest = list[0]
for a in list:
    if a > largest:
        largest = a
print(largest)

8. Write a program to print all prime numbers between 1 and 100.
==>
count = 0
n =  int(input("Enter Number"))
if n<100:
    for a in range(1, 101):
        if n%a==0:
            count = count+1
    if count==2:
        print("Prime")
    else:
        print("Not Prime")
else:
    print("Invalid Input")

or


n = int(input("Enter Number: "))
for a in range(2, n):
    if n % a == 0:
        print("Not Prime")
        break
else:
    print("Prime")


9. Write a program to calculate the factorial of a number using a for loop. 
==>
num = int(input("Enter A number"))
fact = 1
for a in range(1, num+1):
    fact = fact * a                                                                                                               
print(fact)

10. Write a program to print the reverse of a string using a for loop.
==>str = "hello"
reverse = ""
for a in str:
   reverse = a + reverse
print(reverse)

============================================================================================================
WHILE Loop – Programming Questions

11. Write a program to print numbers from 1 to 50 using a while loop.
==>
a= 1
while a<51:
    print(a)
    a = a+1

12. Write a program to print all odd numbers between 1 and 50.
==>
a = 1
while a<51:
    if a%2==0:
        print(a)
    else:
        print(a)
    a=a+1

    
13. Write a program to calculate the sum of digits of a number.
==>
n = int(input("Enter Number"))
sum = 0
a =1
while a<n+1:
    sum = sum+a
    a+=1
print(sum)

14. Write a program to reverse a number using a while loop.








Assignment 2.0


Q1. Print Numbers Use a for loop to print numbers from 1 to 10. 
for a in range(1, 11):
  print(a)
  
Q2. Print Even Numbers Print all even numbers between 1 and 20.
for a in range(1, 21):
  if a%2==0:
    print(a)
    
Q3. Find Sum Print the sum of numbers from 1 to 10 using a for loop. 
Sum = 0
for a in range(1,11):
  Sum = Sum + a
print(Sum)

Q4. Multiplication Table Take a number from the user and print its multiplication table up to 10.
num =  int(input("Enter A Number : "))
for a in range(1 , 11):
  print(num*a)

Q5. Count Characters Take a string and count the total number of characters using a for loop.
ch =  input("Enter Text : ")
count = 0
for a in ch:
  count+=1
print(count)

Q6. Stop at 5 Print numbers from 1 to 10. Stop the loop when the number becomes 5.
for a in range (1, 11):
  print(a)
  if a==5:
    break

Q7. Search in List Search for number 25 in a list. If found, print "Found" and stop the loop.
li = "1,2,5,8,25,4,30,31"
for a in li:
  if '25' in li:
    print("Found")
    break

li = [1,2,5,8,25,4,30,31]
for a in li:
  if a==25:
    print("Found")
    break

Q8. First Negative Number Given a list of numbers, print the first negative number and stop the loop.
li = [1,-2,3,-4,1]
for a in li:
  if a<0:
    print(a)
    break

Q9. Skip 5 Print numbers from 1 to 10. Skip number 5.
for a in range(1, 11):
  if a==5:
    continue
  print(a)

Q10. Skip Even Numbers Print numbers from 1 to 20. Skip all even numbers.
for a in range(1, 21):
  if a%2!=0:
    print(a)

for a in range(1, 21):
  if a%2==0:
    continue
  print(a)

Q11. Skip Letter Print each character of the string "PYTHON". Skip the letter "O".
ch ='PYTHON'
for a in ch:
  if a =='O':
    continue
  print(a)

Q12. Empty Loop Run a loop from 1 to 5 but do nothing inside the loop using pass.
for a in range(1,6):
  pass

Q13. Skip Using Pass Loop from 1 to 10. If number is 6, just use pass.
for a in range(1,11):
  if a==6:
    pass
  print(a)
  
Q14. Search Number Using for-else Search for number 100 in a list. If found, print "Found". If not found, print "Not Found". 
li = [1,2,11,100,22,11,33,44,55,100]
for a in li:
  if a==100:
    print("Found")
else:
  print("Not Found")

Q15. Prime Number Check Take a number from the user and check whether it is prime using for-else.
num = int(input("Enter a Number: "))

if num <= 1:
    print("Not Prime")
else:
    for a in range(2, num):
        if num % a == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

Q16. Star Pattern Print:
*
**
***
****
*****
for i in range(1,6):
  for j in range(1,i+1):
    print("*" , end = "")
  print()

Q17. Reverse Star Pattern Print:
*****
****
***
**
* 
for i in range(1,6):
  for j in range(6,i ,-1):
    print("*" , end= "" )
  print()

Q18. Number Pattern Print:
1
12
123
1234
12345
for i in range(1,6):
  for j in range(1,i+1):
    print(j, end="")
  print()

Q19. Same Number Pattern Print:
1
22
333
4444
55555 
for i in range(1 , 6):
  for j in range(1, i+1):
    print(i , end= "")
  print()

Q20. Pyramid Pattern Print:
    *
   ***
  *****
 *******
*********
for i in range(1,6):
  for j in range(1 , 6-i):
    print(" " , end="")

  for k in range(1,2*i):
    print('*' , end="")
  print()

Q21. Inverted Pyramid Print:
*********
 *******
  *****
   ***
    *
for i in range(1,6):
  for j in range(6,i+5): //   for j in range(i-1):
    print(' ' , end= "")
  for k in range(11, 2*i ,-1):
    print('*' , end = "")
  print()

Bonus Question
Q22. Break in Pattern Print a star pattern. Stop printing when the row number reaches 4.
for i in range(1, 6):
  if i==4:
    break
  for j in range(1,i+1):
    print("*" , end= "")
  print()

Q23. Star Pattern Print:
    *
   **
  ***
 ****
*****
for i in range(1,6):
    for k in range(5,i,-1):
        print(" " ,  end="")
    for j in range(1,i+1):
        print("*" , end="")
    print()

Q24. Star Pattern Print:
*****
 ****
  ***
   **
    *
for i in range(1,6):
    for k in range(1,i):
        print(" ", end="")
    for j in range(6,i,-1):
        print("* ",end="")
    print()

Q25. Star Pattern Print:
    *
   * *
  * * *
 * * * *
* * * * *
for i in range(1,6):
    for s in range(5,i,-1):
        print(" " , end="")
    for k in range(1,i+1):
        print("* " , end="")
    print()

Q26. Star Pattern Print:
* * * * * 
 * * * * 
  * * * 
   * * 
    *
for i in range(1,6):
    for k in range(1,i):
        print(" ", end="")
    for j in range(6,i,-1):
        print("* ",end="")
    print()

Q27. Star Pattern Print:
1
01
010
1010
10101
k = 1
m = -1
for i in range(1,6):
    for j in range(1,i+1):
        print(k , end="")
        k = k+m
        m=-m 
    print()

k=1
for i in range(1,6):
    for j in range(1, i+1):
        print(k%2 , end= "")
        k+=1
    print()

Q28. Star Pattern Print:
*
***
*****
*******
*********
for i in range(1,6):
    for j in range(1,i*2):
        print("*" , end= "")
    print()


Q28. Star Pattern Print:
*
***
*****
*******
*********
*******
*****
***
*
# Upper Half
for i in range(1, 6):
    for j in range(1, i * 2):
        print("*", end="")
    print()

# Lower Half
for i in range(4, 0, -1):
    for j in range(1, i * 2):
        print("*", end="")
    print()
    
 And
 
for i in range(1,6):
    for j in range(1 , i*2):
        print("*" , end = "")
    print()
    
for l in range(1,5):
    for m in range(9, (l*2), -1):
        print("*" , end = "")
    print()



Q29. Star Pattern Print:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
for i in range(1,6):
    for k in range(4,i-1,-1):
        print(" ", end="")
        
    for j in range(1,i*2):
        print("*", end="")
    print()
for i in range(1,5):
    for k in range(1,i+1):  #or  for k in range(0,i)
        print(" ", end="")
    for j in range(9,i*2,-1):
        print("*", end="")
    print()


FOR Loop – Programming Questions 
1. Write a program to print numbers from 1 to 100.
for a in range(1,101):
    print(a)

2. Write a program to print all even numbers between 1 and 50. 
for a in range(1,51):
    if a%2==0:
        print(a)

3. Write a program to print the sum of first n natural numbers. 
result = 0
n = int(input("Enter Number : "))
for a in range(1,n):
    if a>0:
        result = result+a
print(result)

4. Write a program to print the multiplication table of a given number.
n= 2
for i in range(1,11):
    print(n*i)

5. Write a program to print all elements of a list using a for loop
li = [1,2,3,4,5,6,12,13,141,1,3,1,1]
for i in li:
    print(i)

6. Write a program to count the number of vowels in a string.
st = input("Enter Text  :")
count= 0
for i in st:
    count+=1
print(count)

7. Write a program to find the largest number in a list.
li = [1,2,3,4,5,6,12,13,141,1,3,1,1, 142]
res = 0
for i in li:
    if i>res:
        res = i
print(res)

9. Write a program to calculate the factorial of a number using a for loop. 
num= 5
res= 1
for i in range(1,num+1):
    res = i*res
print(res)
And
num = 5
res= 1
for i in range(num , 0 , -1 ):
    res = res*i
print(res)

10. Write a program to print the reverse of a string using a for loop. 

st = "Aakash Tyagi"
res = ''
for i in st:
    res = i+res
print(res)

11. Write a program to print numbers from 1 to 50 using a while loop.
num = int(input("Enter Number : "))
a =1
while a<num:
    print(a)
    a= a+1

12. Write a program to print all odd numbers between 1 and 50.
a=1
while a<50:
    if a%2!=0:
        print(a)
    a+=1

13. Write a program to calculate the sum of digits of a number.
num = int(input("Enter Number : "))
a = 1
res = 0
while a<num+1:
    res = res+a
    a= a+1
print(res)

14. Write a program to reverse a number using a while loop.
num = 20
a = 20
while a>=1:
    print(a)
    a=a-1

15. Write a program to find the factorial of a number using a while loop.
num =int(input("Enter Number : "))
res= 1
a = 1
while a<num+1:
    res = res *a
    a= a+1
print(res)

16. Write a program to keep taking input from the user until the user enters 0.
a = True
while a:
    i = input("Enter Number : ")
    if i=='0':
        break

17. Write a program to find the largest digit in a number.
num = int(input("Enter a Number"))
max = 0
while num> 0 :
    res = num%10
    if max<res:
        max =res
    num = num//10
print("Largest Number : " , max)

18. Write a program to check whether a number is a palindrome.
num  = int(input("Enter a Number"))
original = num
reverse = 0
while num>0:
    digit = num%10
    reverse = reverse*10 + digit
    num = num//10
if  original==reverse:
    print("Palindrome")

19. Write a program to print the Fibonacci series up to n terms.
res = int(input("Enter Number : "))
start = 0
a = 0
b = 1
while start<=res:
    print(a)
    c = a + b
    a=b
    b=c
    start = start+1
    print(c)

20. Write a program to implement a number guessing game using a while loop.
print("\n\t\t\tWelcome To Number Guessing Game!")
res = 21
while True:
    ch= input("\nPress 1 For Playing game and 0 for exit : ")
    if ch=="1":
        num = int(input("Enter Your Number : "))
        if num==res:
            print("Congrats! You Have Won The Game")
            break
    elif ch == "0":
        print("You Have Exited Suceesfully !")
        break
"""


        

















    
