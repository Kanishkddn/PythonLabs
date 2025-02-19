#q=sq root 2CD/H

c=50
h=30
v=input("Enter 3 values for D (Comma Separated): ")
x=v.split(',')
lst=[int(((2*c*int(i))/h)**0.5) for i in x]
# for i in x:
#     q=int(((2*c*int(i))/h)**0.5)
print(f"The answers according to Root(2CD/H) will be: {lst}")
