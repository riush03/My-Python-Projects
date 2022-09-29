def add(num1,num2):
    result = num1+num2
    return print(result)
def minus(num1,num2):
    result = num1-num2
    return print(result)
def divide(num1,num2):
    result = num1/num2
    return print(result)
def multiply(num1,num2):
    result = num1*num2
    return  print(result)

print("A, Addition")
print("S, Substraction")
print("D, Division")
print("M, Multiplication")

choine = input("Enter your choice")

if choine == 'a' or choine == 'A':
    print("Addition")
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    add(num1,num2)
elif choine == 's' or choine == 'S':
    print("Substraction")
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    minus(num1, num2)
elif choine == 'd' or choine == 'D':
    print("Division")
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    divide(num1, num2)
elif choine == 'm' or choine == 'S':
    print("Multiplicaton")
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    multiply(num1, num2)
else:
    print("Invalid input")

