'''Functions-
    organized, well written, modular code to perform a task'''

'''There are 3 types of functions in python
1. predefined. i.e. sum, print, input
2. used.defined
3. Anonymous i.e. lamda functions'''
'''
#syntax
#Write function to find square of a number
def func1(n): #here n is a parameter
    n=n*n
    print(n)

n=int(input("Enter the number to find the square: "))
func1(n)

a=int(input("Enter first number for mul: "))
b=int(input("Enter second number: "))

#multiply 2 numbers
def funcmul(a,b):
    t=a*b
    print(t)
funcmul(a,b)

#write a function to check whether a number is even or odd
def funceo(x):
    if x%2==0:
        print("Even number")
    elif x%2!=0:
        print("Odd number")

x=int(input("Enter num: "))
funceo(x)
'''

# v1=100
# def f1():
#     print(v1)

# f1()
# v1=100
# def f2():
#     v2=465
#     print(v1)

# f2()

#write function to add 2 numbers
def add2(a,b):
    """this function adds 2 numbers""" #this is called docstream
    c=a+b
    return c
print(add2(2,3))
print(add2.__doc__) #prints docstream

