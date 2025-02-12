list1=[1,2,3,4,5]
list2=['a','b','c','d','d']

dict1={k:v for k,v in zip(list1,list2)}#zip combines 2 values which helps, because dictionary needs key and values
print(dict1)

mystr="welometodictionary"
dict2={w:W for w,W in zip(mystr,mystr)}
print(dict2)

mystr2="welometodictionary"
dict3={index:v for index,v in  enumerate(mystr2)}
print(dict3)

'''WAP to create emojis.
Take input from user and store this in words and create a dictionary
if message is 'i am happy' then we get :) if sad, we get :( '''
message=int(input("press 1 if you are happy and 2 if you are sad, press 3 if you are jolly and 4 if you are very very mad: "))
dict11={1:'😁',2:'😔',3:'😄',4:'😡'}
# if message==1 or message==3:
#     print("I am feeling",dict11[1])
# elif message==2 or message==4:
#     print("I am feeling",dict11[2])
print(dict11[message])