#learn tuple
tuple2=(1,5,2,7.7,[1,2,3],"Hello",True)
#indexing is like list i.e. 0,1,2,3 from left and -1,-2,-3 from right
print(tuple2)
print(tuple2[2:5])#goes upto n-1, so if range is 2:5 it will print 2:4
print(tuple2[0::])# [starting point:ending point:step size]
print(tuple2[::-1])
print(tuple2[4][1]) #prints 1 element in the 4 element of tuple
tuple3=(1,21,4,3)
tuple4=tuple2+tuple3
print(tuple4)

'''print even numbers using tuple comprehension'''
# tupll=tuple(i for i in range(100) for x in range(2,i) if x%i==0) #tuple needs to be typecasted to do tuple comprehension
# print(tupll)