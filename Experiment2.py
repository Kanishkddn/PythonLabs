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

# a=(input("Enter first number: "))
# b=(input("Enter second number: "))
# b[2]=a
# a=b[1]
# print("Swapped first num is: ",a)
# print("Swapped second num is: ",b[1])

