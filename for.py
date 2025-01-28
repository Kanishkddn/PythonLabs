s1="For loop first time!!!"
x=0
for x in s1:
    if x=="l" or x=="p":
        #x+=1 this is not required in for loop as continue 
        continue
        #break
    print(x) #Prints separate elements of string

    #print(s1) #Prints the whole strings n times where n is the no. of elements in string, i.e. letters
else:
    print("Bye")
    #else statement can be used with for but will not work if we use break in the for loop as it will be skipped
for i in range(10,20,2):#will work from i=10 to i=20. 2 means difference of 2 i.e 10 12 14 16 18 20
    print("Hello")

# l1=["Apple",1,"c","new"]
# for i  in l1: #Prints separate elements of string
#     print(i)
'''Wap to calculate the factorial of a number'''
num=input("Enter number for finding factorial: \n")
n=1
x=1
intt=1
# while intt<=num:
#     n*=intt
#     intt+=1
# print(n)
l1=["Apple",1,"c","new"]
s1="We1c0me"

for i in s1:
    for j in l1:
        print(i,j)
# for i in num:
#     n=intt*num
#     intt+=1
# print(n)