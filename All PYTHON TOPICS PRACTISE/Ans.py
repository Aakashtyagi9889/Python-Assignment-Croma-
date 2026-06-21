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


"""



 








