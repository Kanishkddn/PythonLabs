import sys

x=909
print(type(x))
print(id(x))
size=sys.getsizeof(x)
print(size)
print(sys.getsizeof(x))
y=[1,2,3]
y.append(5) #Adds 5 to the Array y 
'''Three quotes is used for multi line comments'''
print(y)