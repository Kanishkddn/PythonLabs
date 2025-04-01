# #WAP to handle division by 0 exception
# #WAP to handle multiple exceptions
# #WAP to handle custom exceptions
# #WAP to use finally and else exceptionality

# #Q01
# def div(x,y):
#     try:
#         ans = x/y 
#         print(f"Soln: {ans}")
    
#     except ZeroDivisionError: 
#         print("Dont divide with 0 (Undefined)")

#     finally:
#         print("finish")

# num = int(input("Enter numerator value: "))
# den = int(input("Enter denominator value: "))

# div(num, den)

# #Q02
# def div(x,y):
#     try:
#         ans = x / y 
#         print(f"Soln: {ans}")
#     except ZeroDivisionError: 
#         print("Dont divide with 0 (Undefined)")
#     except ValueError:
#         print("Pls enter numeric value")

# num = int(input("\nEnter numerator value: "))
# den = int(input("Enter denominator value: "))

# div(num, den)

# #Q03

# def numcheck(num1,num2):
#     if num1>100 or num2>100:
#         raise ValueError
#     else:
#         return False

# def div3(x,y):
#     try:
#         numcheck(num,den)
#         ans=x/y
#         print(f"soln= {ans}")
#     except ZeroDivisionError:
#         print("Dont divide with 0 (Undefined)")

#     except ValueError:
#         print("NUmber is above 100")
#     else:
#         print("Successful")
#     finally:
#         print("Execution done")

# print("\nThis part divides numbers below 100")
# num = int(input("Enter numerator value: "))
# den = int(input("Enter denominator value: "))

# div3(num,den)

# #Q04
# #WAP to use finally and else exceptionality
# def div(x,y):
#     try:
#         ans = x / y 
#         print(f"Result: {ans}")
#     except ZeroDivisionError: 
#         print("Error 101 (Division by zero is not permitted!!!)")
#     except ValueError:
#         print("Pls enter numeric value")
#     else:
#         print("Division was succesful!")
#     finally:
#         print("Done")

# num = int(input("\nEnter numerator value: "))
# den = int(input("Enter denominator value: "))

# div(num, den)

#Get a list from the user, ask for an index, and handle IndexError and ValueError.
mylist = [] 
num = int(input("Enter list size: "))

for i in range(num):
    val = int(input(f"Enter value {i}: ")) 
    mylist.append(val)

def printt(a):
    try:
        print(f"Element at index {a}: {mylist[a]}")
    except IndexError:
        print("Error: Invalid Index! Index out of range.")
    except ValueError:
        print("Error: Invalid Value! Please enter an integer.")

try:
    ind = int(input("Enter index to display: "))
    printt(ind)
except ValueError:
    print("Error: Please enter a valid integer index.")

#Problem: Keep asking for an integer until the user enters a valid one.
def iint(x):
    while True: 
        try:
            num = int(input(x))  
            return num 
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


num = iint("\nEnter a number value: ")
print(f"You entered: {num}")

#Problem: Take two numbers as input, perform division, and handle ZeroDivisionError and ValueError.
def div(x,y):
    try:
        ans = x / y 
        print(f"Soln: {ans}")
    except ZeroDivisionError: 
        print("Dont divide with 0 (Undefined)")
    except ValueError:
        print("Pls enter numeric value")

num = int(input("\nEnter numerator value: "))
den = int(input("Enter denominator value: "))

div(num, den)

#Problem: Read a file and handle FileNotFoundError.

#Problem: Ask for age and raise a custom exception for invalid values.
def agee(age):
    if age<0 or age>200:
        raise ValueError
    
def err(a):
    try:
        agee(age)
        print(age)
    except ValueError:
        print("Invalid Age")

age=int(input("\nAge"))
err(age)
