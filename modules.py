#import fiboo #import works if a code with that name is present in your directory. i.e. here i have made a code fiboo which is being imported here
from calcc import*


a=float(input("Enter 1st num:"))
b=float(input("Enter 2nd number:"))
c=0
x=int(input("What function do you want to perform:( 1 for add, 2 for sub, 3 for mul, 4 for div, 5 for exp)"))

if x==1:
    print(addition(a,b,c))

elif x==2:
    print(sub(a,b,c))

elif x==3:
    print(mul(a,b,c))

elif x==4:
    print(div(a,b,c))

elif x==5:
    print(expo(a,b,c))
