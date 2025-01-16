# ARITHMETIC OPERATORS
# add(+)
# sub(-)
# mul(*)
# div(/)
# floor div(//)
# exponent(**)
#modulus(%)
a=10
b=5
add=a+b
sub=a-b
mul=a*b
div=a/b
fld=a//b
exp=a**b
mod=a%b
print(add,sub,mul,div,fld,exp,mod)

#COMPARISON OPERATORS
a=10
b=5
print("==",a==b)
print("!=",a!=b)
print("> ",a>b)
print("< ",a<b)
print(">=",a>=b)
print("<=",a<=b)

#UNARY OPERANDS
#Unary operands can work with one element only as a=10 and b=-(a)
c=10
d=-(c)
print(c)
print(d)

#BITWISE OPERATORS
'''OR= |, AND= &, NOT= ~, XOR= ^
OR MEANS EITHER ONE,
AND MEANS ALL SHOULD BE 1
NOT EXCHANGES VALUE, I.E 1 BECOMES 0 AND 0 BECOMES 1
XOR MEANS ONLY 1 OF TWO SHOULD BE HIGH I.E 1. IF BOTH 1 OR 0, YOU GET OUTPUT 0
'''
a=10
b=5
print(a|b) #gives value 15 becsuse 10 is 1010 and 5 is 0101, so in binary, it becomes 1111 i.e 15 after or function
print(a^b) #gives
print(~a)
a=7
b=3
c=8
print(a&b) #gives 3 because 7 is 0111 and 3 is 0011 so and gives 0011
print(a^b)

#SHIFT OPERATORS
print(a>>1) #0111 becomes 0011 because 1 right shift. shift more than 4 gives 0
print(a<<1) #0111 becomes 1110 because 1 left shift. shift more than 4 doesn't give 0 instead increases value as it saves to next bit on left

#LOGICAL OPERATORS
'''
AND= and
OR= or
NOT= not 
'''

if((a>b)and(a!=b)):
    print("Yes")
if((a>b)or(a!=b)):
    print("Yes")
# if((a>b)not(a!=b)):
    # print("Yes")
