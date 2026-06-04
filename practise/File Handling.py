a = int(input("Enter a number"))
b = int(input("Enter b number"))

try:
    print("division", a // b)
except SyntaxError as e:
    print(" error", e)
