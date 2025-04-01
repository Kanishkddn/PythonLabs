# def sayhello():
#     print("good morning")

# def welcome(greet):
#     print(greet)

# #These functions can be run here OR be used in other codes using
# # from <codename> import*
# #  import <codename>
# #and can be done as-> import <codename> as gr which will help me call this in different code using gr 
# sayhello()



# #wap to create a package that defines some functions and based on the need, and based on the need, those functions are called by some other file in the same package
# from  calcc import*

# # a=float(input("Enter first number: "))
# # b=float(input("Enter second number: "))
# # c=0
# # print(addition(a,b,c))
# # print(sub(a,b,c))
# # print(mul(a,b,c))
# # print(div(a,b,c))
# # print(expo(a,b,c))

# '''
# There are 2 types of modules
# predefined
# userdefined'''
# import calendar

# print(calendar.january(2025,3))

# import random
# print(keywords.kwlist())

#random, calendar, keywords, os etc are examplex of predefined modules

#if i call a module eg 
# import abc
# abc.wish()
#and the code prints welcome twice then
#if __name__==__main__
#   wish()

import os
# os.mkdir("Data")
# if(not os.path.exists("Data")):
#     os.mkdir("Data")
 
'''Make 1000 folders in one go with for loop'''
for i in range(1000):
    os.rmdir(f"Data/day{i+1}") #makes folders in data directory 
    os.rename(f"Data/day{i+1}",f"Data/tutorial{i+1}") #renames folders

#WAP to put python code in every folder 
