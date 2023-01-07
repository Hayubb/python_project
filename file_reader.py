def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
import function
def simple_ins(p,r,t):
     return function.simple_int(p,r,t)
import function
def quadratic(a,b,c):
     return function.quadratic_for(a,b,c)
print("list of the operatins:")
print("a.Addition")
print("b.Subtraction")
print("c.Multiplication")
print("d.Division")
print("e.Simple Insterest")
print("f.Quadratic Formular")
print("enter 'q' at anytime to quit")
while True:
    choice=input("please enter your choice(a/b/c/d/e/f): ")
 

    if choice == "a":
        num1=int(input("enter your first number: "))
        num2=int(input("enter your second number: "))
        print(num1, "+", num2,"=", add(num1,num2))
    elif choice == "b":
        num1=int(input("enter your first number: "))
        num2=int(input("enter your second number: "))
        print(num1, "-", num2,"=", subtract(num1,num2))
    elif choice == "c":
        num1=int(input("enter your first number: "))
        num2=int(input("enter your second number: "))
        print(num1, "*", num2,"=", multiply(num1,num2))
    elif choice == "d":
        num1=int(input("enter your first number: "))
        num2=int(input("enter your second number: "))
        print(num1, "/", num2,"=", divide(num1,num2))
    elif choice == "e":
        num1=int(input("enter your first number: "))
        num2=int(input("enter your second number: "))
        num3=int(input("enter your third number: "))
        print("the simple inerest of question","=", simple_ins(num1,num2,num3))
    elif choice == "f":
        num1=int(input("enter your first number: "))
        num2=int(input("enter your second number: "))
        num3=int(input("enter your third number: "))
        print("the root of equation of question","=", function.quadratic_for(num1,num2,num3))
    elif choice == "q":
        break
    else:
        print("invalid input")

 
 
     
     
    
    
        
    