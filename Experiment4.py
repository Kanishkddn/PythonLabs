#Factorial
fac=int(input("Enter number whose factorial you want: "))
into,f,a=1,1,1
while into<=fac:
    a*=into
    into+=1
print("The Factorial will be: ",a)

#Find whether the given number is Armstrong number.
num=int(input("Enter a number to check if armstrong: "))
original=num
ans=0

num1=num
digits = 0
while num1 > 0:
    num1 //= 10
    digits += 1

num1= num
while num1 > 0:
    digit=num1 % 10
    ans+=digit ** digits
    num1//= 10

if ans==original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number.")

#Print Fibonacci series up to given term.

fibb = int(input("Enter the upper limit for the Fibonacci series: "))

a, b = 0, 1

print("Fibonacci series up to", fibb, ":")
while a <=fibb:
    print(a, end=" ")
    temp = a+b
    a=b
    b=temp

#Write a program to find if given number is prime number or not.
prime=int(input("\nEnter number to check prime: "))
x=2
ctr,z=0,0
while x<prime:
    if prime%x==0:
        ctr+=1
        x+=1
    else:
        z+=1
        x+=1
if ctr==0:
    print("Number is prime")
elif ctr!=0:
    print("Not prime")

#Check whether given number is palindrome or not.
pal=int(input("Enter a number to check if it is a palindrome: "))

origin=pal
reverse = 0

while pal > 0:
    digit = pal % 10 
    reverse = reverse * 10 + digit 
    pal = pal // 10 

if origin == reverse:
    print(f"{origin} is a palindrome num.")
else:
    print(f"{origin} is not a palindrome num.")

#sum of digits

no=int(input("Enter a number to calculate the sum of its digits: "))

sum = 0

# Calculate the sum of digits using a while loop
while no > 0:
    digit=no % 10 
    sum+= digit 
    no= no // 10  

print(f"The sum of the digits is: {sum}\n")

#Count and print all numbers divisible by 5 or 7 between 1 to 100.
n,ct1,ct2=1,0,0
while n<=100:
    if n%5==0:
        print(f"{n} is divisible by 5")
        ct1+=1
    elif n%7==0:
        print(f"{n} is divisible by 7")
        ct2+=1
    n+=1
    
print(f"\n{ct1} nos are divisible by 5")
print(f"{ct2} nos are divisible by 7")

#Convert all lower cases to upper case in a string.
str=input("Input string to convert lower case to upper case: ")
uc=str.upper()
print(uc)

#Print all prime numbers between 1 and 100.
# prime=1
# x=100
# ctr,z,n=1,0,0
# while prime<100:
#     if prime%n==0:
#         print(f"{prime} is prime!")
#         ctr+=1
#         n+=1
#     else:
#         z+=1
#         n+=1
num = 2
print("Prime numbers between 1 and 100:")

while num<=100:
    prime = True

    d = 2
    while d * d <= num:
        if num % d == 0:
            prime = False
            break
        d += 1
    if prime:
        print(f"{num} ")
    num+=1

# Print the table for a given number
tt=int(input("Enter no. to get the table: "))
var=1
while var<11:
    print(f"{tt} x {var} = {tt*var}")
    var+=1
