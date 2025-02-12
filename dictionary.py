#if a empty set is initialised, the compiler will treat it as a dictionary
#so, to initialize an empty set, you need to initilise with typecaste
'''dictionary is a data structure which we store values as a pair of key and value.
Each key is separated from its value by a colon (:)'''

dict_1={'Name':'Sajid','SapId':'5900','age':21}

'''Accessing Values'''
#we access values using key
print("dict_1[Name]=",dict_1['Name'])
#here the key acts like index which is used to access values

'''Adding Elements and modification'''
dict_1['Dept']="SoCS"#new entry created because key named dept is not a part of dict_1
print(dict_1)

dict_1['Name']="KK"#updates value if same key is already present
print(dict_1)

'''Deleting an element'''
print(dict_1.pop('Name'))#deletes one value using key
print(dict_1)
print(dict_1.popitem())#randomly deletes item
#if you delete an item with key that is not present in the dictionary, it will give error]
print(dict_1.pop("SapId",-1)) #returns default value
print(dict_1.clear)#deletes all items in the dictionary so you are left with empty dictionary


'''Sorting and looping values'''
dict1={'age':21,'Name':'Sajid','SapId':5900}
print(sorted(dict1.keys())) #sorts elements
#print(sorted(dict1.values())) #sorts elements

'''Looping'''
for key in dict1:
    print(key)

for values in dict1.values():
    print(values, end=' ') #end helps in printing values in one line with a space between each

for key,val in dict1.items():
    print(key,val,"\t", end=' ')

'''Nested list'''
Students = {'Shiv' : {'CS':90, 'DS':89, 'CSA':92},
            'Sadhvi' : {'CS':91, 'DS':87, 'CSA':94},
            'Krish' : {'CS':93, 'DS':92, 'CSA':88}}
for key,val in Students.items():
    print(key,val)

'''WAP '''
credentials={'Name':'Sajid','SapId':'5900','age':21,'University':"UPES"}
print(credentials)
credentials['subjects']={'CS1':"Maths",'CS2':"Physics",'CS3':"Python",'CS4':"COA",'CS5':"DE",'CS6':"DSA"}
print(credentials)

'''Built in functions and methods'''
'''
1 sort
2 iterate all items
3 access any key,value
4 modify key, value
5 delete items using pop and clear
'''

copyd={}
copyd1={}
copyd2={}
#1
print(credentials)
copyd2=sorted(credentials.keys())
print(copyd2)
#2
print(credentials.items())
#3
print(credentials['Name'])
#4
credentials["Name"]="Kanishk"
#5
print(credentials.popitem())
credentials.clear()
print(credentials)

len(credentials)
str(credentials) #typecastes values as string. all elements
copyd=credentials.copy() #creates clone copy
credentials.clear()#deletes entries in dictionary
copyd1.fromkeys(copyd,-1)
copyd.get(key)
#copyd.has_key('Name')
copyd.items()
copyd.keys()
copyd.setdefault(key,values)

'''
1 sort
2 iterate all items
3 access any key,value
4 modify key, value
5 delete items using pop and clear
'''
