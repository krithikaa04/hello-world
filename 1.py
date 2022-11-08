#a simple calculator that performs addition,subtraction,multiplication and division of two numbers using python oops concepts
class calculate:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add_numbers(self):
        return self.a+self.b
    def diff_numbers(self):
        return self.a-self.b
    def product(self):
        return self.a*self.b
    def divide(self):
        return self.a/self.b
    def modulo(self):
        return self.a%self.b
print("CALCULATOR")
while True:
    print("Menu")
    print("1.Add")
    print("2.Difference")
    print("3.Multiply")
    print("4.Division")
    print("5.Modulo")
    print("6.Exit")
    ch = int(input("Enter your choice:"))
    if(ch==1):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        c1 = calculate(num1,num2)
        print("Sum:",c1.add_numbers())
    elif(ch==2):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        c2 = calculate(num1,num2)
        print("Difference:",c2.diff_numbers())
    elif(ch==3):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        c3 = calculate(num1,num2)
        print("Product:",c3.product())
    elif(ch==4):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        c4 = calculate(num1,num2)
        print("Division:",c4.divide())
    elif(ch==5):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        c5 = calculate(num1,num2)
        print("Modulo:",c5.modulo())
    elif(ch==6):
        break
    else:
        print("Invalid input,enter again!")
