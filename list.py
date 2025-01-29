'''List'''
l1=[1,2,3,4,5] #0,1,2,3,4 index left to right and -1,-2,-3,-4,-5 index from right to left
print(type(l1))
print(l1[:]) #prints whole list
print(l1[2:]) #prints whole list after index 2 
print(l1[2:3]) # prints upto onle n-1th term, i.e it will print only 2nd index element i.e 3
print(l1[::]) #this is start : this is stop : this is step size
print(l1[::2]) #print with step size 2 i.e 1,3,5

'''Adding elements to a list'''
l1.append(30) #used to add element at the end of list
print(l1) #prints with 30 added
l1.insert((2),(10)) #adds 10 to index number 2
l1.extend([10,20,30]) #can add more than one element at once
print(l1)

'''WAP to add elements using append, insert, and extend'''
l2=[]
l2.append(1)
print("\n",l2)
l2.append("Sajid")
print(l2)
l2.insert((2),("True"))
print(l2)
l2.extend([7.5,"Abhi"])
print(l2)
l2.extend([7,"x"])

'''Deleting Elements'''
l2.remove("Sajid")#Deletes single element
print("\n",l2)
l2.pop(1) #deletes according to index number
print(l2)
del l2 [1:3] #deletes multiple 
print(l2)

'''Update Operations'''
'''Inserting changes the index of the value previously there, but update replaces the value completely'''
#l2.update(3,12)
print(l2)

'''list()'''
a=list((0,2,4,12,21,"abc")) #will make a list a
print("\n",a) #1 dimensional list

'''2D list'''
