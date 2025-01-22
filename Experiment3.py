#divisiblility by 3 and 5
x=int(input("Enter a number to check if it is divisible by 3 and 5: "))
if x%3==0 and x%5==0:
    print("Number is divisible by 3 and 5 both!")

elif x%3==0 and x%5!=0:
    print("Number is divisible by 3 only")

elif x%5==0 and x%3!=0:
    print("Number is divisible by 5 only")

#number Multiple 5
y=int(input("Enter the number: "))
if y%5==0:
    print("Number is multiple of 5!")

else:
    print("Number is not multiple of 5")

#Greatest among 2 numbers
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
if(a>b):
    print(a ,"is greater than ", b)
elif(b>a):
    print(b ,"is greater than ", a)
elif(b==a):
    print("Both numbers are equal")
    
#greatest among 3 values
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter the 3rd number: "))
if a>b:
    if a>c:
        print(a, " Is the Greatest!")
    elif c>a:
        print(c," is greatest of all!")
elif b>a:
    if b>c:
        print(b ," is the greatest!")
    elif c>b:
        print(c," is the greatest")

#roots of a formula
a=float(input("If the equation is represented as Ax^2+Bx+C=0, then enter the value of A: "))
b=float(input("If the equation is represented as Ax^2+Bx+C=0, then enter the value of B: "))
c=float(input("If the equation is represented as Ax^2+Bx+C=0, then enter the value of C: "))


d=((b*b)-4*a*c)
if d>0:
    print("The Eq has distinct and real roots")
elif d<0:
    print("The Eq has Imaginary roots")
elif d==0:
    print("The Eq has Equal and real roots")



q1=(-b+(d)**0.5)/2*a
q2=(-b-(d)**0.5)/2*a

print("The 1st root will be: ", q1)
print("The 2nd root will be: ", q2)

#Check if leap year or not
year=int(input("Enter the year to check if leap or not: "))
if year%4==0 and year%100!=0:
    print(year, " is a Leap Year!!!\n")
else:
    print("Year is not a leap year...\n")

#printing next date
days=[31,28,31,30,31,30,31,31,30,31,30,31]
da=int(input("Enter day:"))
mo=int(input("Enter month:"))
ye=int(input("Enter year:"))
if y%4==0:
    days[1]+=1
    if mo<12:
        if da<days[mo-1]:
            da+=1
        elif da==days[mo-1]:
            mo+=1
    elif mo==12:
        if da<days[mo-1]:
            da+=1
        elif da==days[mo-1]:
            mo=1
            da=1
            ye+=1
else:
    if mo<12:
        if da<days[mo-1]:
            da+=1
        elif da==days[mo-1]:
            mo+=1
    elif mo==12:
        if da<days[mo-1]:
            da+=1
        elif da==days[mo-1]:
            mo=1
            da=1
            ye+=1
print("next date is", da,mo,ye)

#8. Gradesheet
name=input("Enter the name: ")
roll=input("Enter the roll no.: ")
SAP=input("Enter SAP ID: ")
sem=input("Which sem are you in: ")
course="B.Tech CSE"
pds=float(input("Enter  marks of PDS: "))
python=float(input("Enter  marks of Python: "))
chemistry=float(input("Enter  marks of chemistry: "))
english=float(input("Enter  marks of english: "))
physics=float(input("Enter  marks of Physics: "))
total=pds+python+chemistry+english+physics
per=(total/500)*100
cgpa=per/10
if cgpa>0 and cgpa<=3.4:
     grade="F"
elif cgpa>3.4 and cgpa<=5:
     grade="C+"
elif cgpa>5 and cgpa<=6:
     grade="B"
elif cgpa>6 and cgpa<=7:
     grade="+"
elif cgpa>7 and cgpa<=8:
     grade="A"
elif cgpa>8 and cgpa<=9:
     grade="A+"
elif cgpa>9 and cgpa<=10:
     grade="O"
print("\nGRADESHEET")
print("Name: ",name)
print("Roll No: ",roll,"                               SAP ID: ", SAP)
print("Course: ",course)
print("\nMARKS BELOW\n")
print("PDS: ",pds)
print("Python: ",python)
print("Chemistry: ",chemistry)
print("English: ",english)
print("Physics: ",physics)
print("Percentage: ",per,"%")
print("CGPA: ", cgpa)
print("Grade: ", grade)