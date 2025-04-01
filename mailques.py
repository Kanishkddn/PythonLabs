def diamond(n):
    if n % 2 == 0:
        print("Please enter an odd number.")
        return
    for i in range (21):
        n+=2
        mid = n // 2
        for i in range(n):
            for j in range(n):
                if abs(mid - i) + abs(mid - j) == mid:
                    print("*", end="")
                else:
                    print(" ", end="")
            
            print()


n = int(input("Enter an odd number: "))
diamond(n)


#002
def stringy(s, n):
    if n <= 0 or n > len(s):
        print("Invalid value of n. Please enter a number between 1 and the length of the string.")
        return
    
    result = "".join(s[i].upper() if (i + 1) % n == 0 else s[i].lower() for i in range(len(s)))
    print(result)


s = input("Enter a string: ")
n = int(input("Enter an integer n: "))
stringy(s, n)

#003
def bitwiseee(a, b, op):
    if op == '&':
        result = a & b
    elif op == '|':
        result = a | b
    elif op == '^':
        result = a ^ b
    elif op == '<<':
        result = a << b
    elif op == '>>':
        result = a >> b
    else:
        print("Invalid operator. Please use &, |, ^, <<, or >>.")
        return
    
    print(f"Result: {result}")

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
op = input("Enter a bitwise operator (&, |, ^, <<, >>): ")
bitwiseee(a, b, op)

#004
def numberpyramid(n):
    if n % 2 == 0:
        print("Please enter an odd number.")
        return
    
    num = 1
    for i in range(1, n + 1, 2): 
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

n = int(input("Enter an odd number: "))
numberpyramid(n)

#005
def palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]  # Check if string is equal to its reverse

# Take input from the user
s = input("Enter a string: ")
if palindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")