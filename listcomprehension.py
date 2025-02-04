# my_str="Welcome Python"
# list_1=[]
# for i in my_str:
#     list_1.append(i)

# #Same thing in a shorter way would be
# list_2=[i for i in my_str]
# #example 2
# #print all even number from 1 to 200
# list_3=[]
# for i in range(200):
#     if i%2==0:
#         list_3.append(i)

# #same thing with comprehension will be
# list_4=[i for i in range(200) if i%2==0]

# #example 3
# #print powers of numbers
# list_5=[]
# for num in range(100):
#     list_5.append(num**2)
#     print(list_5)

# list_6=[num**2 for num in range(100)]
list_3=[i for i in range(200) if i%3==0]
list_5=[i for i in range(200) if i%5==0]
list_7=[i for i in range(200) if i%7==0]
print(list_3,"\n")
print(list_5,"\n")
print(list_7,"\n")
 #or we can do
listmix=[]
listmix.append(list_3)
listmix.append(list_5)
listmix.append(list_7)
print(listmix)
listall=[i for i in range(200) if i%3==0 if i%5==0 if i%7==0]
listmix2=[i for i in range(200) if i%3==0 or i%5==0 or i%7==0]
print(listmix2)
print(listall)

mystr="one 1 two 2 three 3 four 4"
l1=[item for item in mystr if item.isdigit]

'''wap to print all armstrong numbers between 1 to 1000 using list comprehension'''
listarm = [num for num in range(1, 1001) if num == sum(int(digit) ** len(str(num)) for digit in str(num))]

print(listarm)