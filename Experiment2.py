x=9
y=7
print("Addition : ",x+y)
print("Subtraction : ",x-y)
print("Multiplication : ",x*y)
print("Division : ", x/y)
rad=float(input("Enter the radius of the circle : "))
area=3.14159*rad*rad
print("Area of Circle : ", area)
print("If x=",x," and y=",y)
eq=(x+y)*(x+y)
print("\nThe Solution of Equation (x+y)*(x+y) will be : ",eq)
base=float(input("Enter the base of the Right Triangle: "))
perp=float(input("\nEnter the perpendicular of the triangle: "))
hypo=((base*base)+(perp*perp))**0.5
print("\nThe Hypotenuse of the triangle will be : ",hypo)
print("\nLets Calculate Simple Intrest\n")
pri=float(input("Enter the principal: "))
rate=float(input("Enter rate of interest in percentage per annum: "))
time=float(input("Enter the Time period (In years): "))
si=(pri*rate*time)/100
print("The Simple Interest will be : ", si)

print("\nFinding area of triangle from length of sides\n")
s1=float(input("Enter Base: "))
s2=float(input("Enter Height: "))
tarea=(s1*s2)/2
print("The area of triangle will be: ",tarea)

sec=int(input("Enter seconds: "))
hours=sec/3600
mins=(sec-(hours*3600))/60
secs=(mins%60)/60
print("The time will be: ",hours, mins, secs)

#Number swap
a=3
b=4
print(a,b)
a,b=b,a
print(a,b)

#Sum of n natural nos
n = int(input("Enter the value of n: "))
sum_natural = n * (n + 1) // 2  # Using the formula n(n+1)/2
print(f"The sum of the first {n} natural numbers is {sum_natural}.")


#Write a program to find left shift and right shift values of a given number.
num = int(input("Enter a number: "))
shift = int(input("Enter the number of positions to shift: "))

left_shift = num << shift  # Left shift
right_shift = num >> shift  # Right shift

print(f"Left shift of {num} by {shift} positions: {left_shift}")
print(f"Right shift of {num} by {shift} positions: {right_shift}")

#Using membership operator find whether a given number is in sequence (10,20,56,78,89)
sequence = (10, 20, 56, 78, 89)
num = int(input("Enter a number: "))

if num in sequence:
    print(f"{num} is in the sequence {sequence}.")
else:
    print(f"{num} is not in the sequence {sequence}.")

string = input("Enter a string: ")
char = input("Enter a character to search for: ")

#Using membership operator find whether a given character is in a string.
if char in string:
    print(f"The character '{char}' is present in the string.")
else:
    print(f"The character '{char}' is not present in the string.")
