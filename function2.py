# # def func1(a,b,c,d):
# #     return sum(a,b,c,d)

# # print(func1(1,2,3,6))

# #-> * args
# def func11(*args): #*args means length can be anything
#     return sum(args) #Helps when we dont know how many variables we want to use

# print(func11(1,2,3))

# lst1=[1,2,3,4,5,6]
# lst2=[1,2,3,4,5,6]
# print(func11(*lst1,*lst2)) #adds all elements of list

# t1=(1,2,3,4)
# t2=(1,2,3,4)
# print(func11(*t1,*t2))

# #-> *kwargs i.e. *keyword arguments
# dict1={name='Sajid',Sap='5900'}
# def biodata(**kwargs,c,d):
#     for key,value in kwargs.items():
#         print(key,value)

# biodata(**dict1,10,9)

# '''WAP to take values fromm a list and store them in a dictionary using functions using *args and **kwargs'''
# lst1=[1,2,3,4,5]
# dict1={}

# def func2(*args,**kwargs):
#     for i in range(len(lst1)):
#         x=0
#         dict1[x+1]=lst1[x]
#         x+=1
#     print(dict1)

# func2(*lst1,**dict1)

lst1 = [1, 2, 3, 4, 5]
dict1 = {}

def func2(*args, **kwargs):
    temp_dict = {} 
    for i in range(len(args)):  
        temp_dict[i + 1] = args[i] 

    temp_dict.update(kwargs)  
    print(temp_dict)

func2(*lst1)
