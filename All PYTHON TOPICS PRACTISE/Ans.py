"""
1-10: Basic Input/Output 

1. Write a Python program to print "Hello, World!" 
==> print("Hello, World!")

2. Write a Python program to take two integers as input and print their sum. 
==> num1 = int(input("Enter First Number"))
    num2 = int(input("Enter Second Number"))
    sum = num1 + num2
    print(sum)

3. Write a program to calculate the area of a rectangle. 
==> length = int(input("Enter Length of rectangle"))
    width  = int(input("Enter Width of rectangle"))
    print(length + width)

4. Write a Python program to check if a number is even or odd. 
==> num = int(input("Enter Number : "))
    print("Even" if num%2 == 0 else "Odd")

5. Write a Python program to take a string as input and print it in reverse order. 
==> text = input("Enter Text : ")
    print(text[:: -1])

6. Write a Python program to convert temperature from Celsius to Fahrenheit.
==> celcius = float(input("Enter Temprature in Celcius "))
  fehranheight = (1.8 * celcius) + 32
  print(fehranheight)

7. Write a program to take a list of numbers and print their sum.
==> li = [2,2,2,2,2]
    x = sum(li)
    print(x)

    And
    li = list(map(int , input("Enter Numbers : ").split()))
    print(sum(li))

8. Write a Python program to swap two variables without using a temporary variable.
==>   a = 10
      b = 20
      a , b = b ,a 
      print("A : ", a)
      print("B : " , b)

        OR

      a = 10 
      b = 20
      a= a+b
      b = a - b
      a = a - b
      print("A : ", a)
      print("B : " , b)

        OR

        a = 10
        b = 20
        b = a*b
        a = b / a
        b = b / a
        print("A : ", a)
        print("B : " , b)

9. Write a Python program to find the length of a string
  str = input("Enter Text : ")
  print( len(str))

10. Write a program that reads an integer and prints its multiplication table. 
  num = int(input("Enter Number : "))
  for  i in range (1 , 11):
    print(num * i)

================================================================================================================
11-20: Control Structures (if-else, loops) 


11. Write a Python program to check whether a number is positive, negative, or zero. 
  num = int(input("Enter Number : ")) 
  if  num > 0:
    print("Number is Positive ")
  elif num < 0:
    print("Number is Negative")
  else:
    print("Zero")

    
12. Write a program to find the largest among three numbers.
  a = float(input("Enter A Number : "))
  b = float(input("Enter B Number : "))
  c = float(input("Enter C Number : "))
  if a > b and a > c:
    print("A is greater")
  elif a<b and b>c:
      print("B is Greater")
  else :
    print("C is greater") 

13. Write a Python program to print all prime numbers between 1 and 100.
==> for i in range( 2, 101):
    for j in range(2, i):
      if i % j ==0 :
        break
    else:
      print(i) 

14. Write a Python program to calculate the factorial of a number. 
==> num = 5
    res = 1
    for a in range(1,num+1):
      print(a)
      res = res * a
    print(res)

    OR

    num  =  5
    for a in range(1, num):
      num = num * a
    print(num)

15. Write a Python program to print the Fibonacci sequence up to n terms.
==> n = 10
    a = 0
    b = 1
    for i in range(n):
      print(a)

      c = a+b
      a = b
      b = c

16. Write a program to check if a year is a leap year. 
==> year = int(input("Enter year: "))
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")
"""














