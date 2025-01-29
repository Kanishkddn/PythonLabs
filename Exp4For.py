import sys
# 1.Factorial
num = int(input("Enter a number for factorial: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)

#Find weather the given number is armstrong number
num = int(input("Enter a number for armstrong check: "))
order = len(str(num))
sum_digits = 0

for digit in str(num):  
    sum_digits += int(digit) ** order  

if sum_digits == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

#Print Fibonacci series up to given term.
limit = int(input("Enter the limit for last fib term: "))

a, b = 0, 1 

for x in range(limit):  
    if a > limit:
        break
    print(a, end=" ")
    a, b = b, a + b 

#Write a program to find if given number is prime number or not.
n = int(input("\nEnter a number for prime: "))
is_prime = 1

if n < 2:
    is_prime = 0 

for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = 0 
        break  

if is_prime == 1:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

#Check whether given number is palindrome or not.
n = int(input("Enter a num to check palindrome: "))
temp = n 
rev = 0 

for i in str(n): 
    rev = rev * 10 + int(i) 

if temp==rev:
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")

#sum of digits
n = int(input("Enter num to find sum of digits: "))
summ = 0 

for digi in str(n): 
    summ += int(digi) 

print(f"Sum of digits of {n} is {summ}.")

#Count and print all numbers divisible by 5 or 7 between 1 to 100.
d5=0
d7=0
for i in range(1,101):
    if i%5==0:
        d5+=1
        print("Divisible by 5: ",i)
    elif i%7==0:
        d7+=1
        print("Divisible by 7: ",i)

print(f"{d5} numbers between 1 and 100 are divisible by 5")
print(f"{d7} numbers between 1 and 100 are divisible by 7")


#Convert all lower cases to upper case in a string.
str=input("Input string to convert lower case to upper case: ")
uc=str.upper()
print(f"{uc}\n")

#Print all prime numbers between 1 and 100.
print("\nAll prime numbers between 1 and 100 are: ")
for n in range(2, 101): 
    is_prime = 1
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0: 
            is_prime = 0
            break 
    if is_prime==1:
        print(n) 

#Print the table for a given number
table=int(input("\nEnter number to get a multiplication table: "))
for i in range(1,11):
    print(f"{table} x {i} = {table*i}")
