#set is a collection of items (numbers, strings)
#set itself is mutable, but elements of set are immutable
'''Operation of sets'''
set1={1,2,3,4,5}
set2={"one","two","three","three"}
print(set2)
set3={1,1,2,3,3,4,5,5}#removes duplicates automatically because immutable elments
print(set3)
#set4={1,2,3,[5,6,8],9,10}#lists are not allowed in set because lists are mutable and hence override the function of set not being mutable
#print(set4)

'''comprehension'''
setcomp={n for n in range(10) if n%2==0}
print(setcomp)
'''converting list into set'''
list=set([s for s in range(1,11)])
print(list)

'''Addition in set'''
set1.add('Nine')
print(type(set1))

'''Update'''
set1.update([56,'one',1])
print(set1)

'''remove and discard'''
set3.remove(4) #works only if the element is present in the set
print(set3)

set3.discard(1) #works even if the element is not present. therefore use only when you are not sure if elemnt is present in set or not
print(set3)

'''set operations'''
# #union
# intersection
# superset
# subset
#disjoint

'''union'''
a={1,2,3,4}
b={4,5,6,7}
c={5,23,77,8}
print(a.union(b)) #removes duplicates in final set
print(a.union(b,c))
#a.union_update(b)

'''intersection'''
print(a.intersection(b)) #prints element present in both sets
a.intersection_update(b)
print(a)

'''subset'''
print(b.issubset(a))#all elements of b are in a

'''disjoint'''
print(a.isdisjoint(c))# no common elements

'''superset'''
print(a.issuperset(b))

'''WAP to convert a list of odd numbers into a set using list comprehension'''
list=set([n for n in range(1000) if n%2!=0])
print(list)
print(type(list))
list=tuple([n for n in range(1000) if n%2!=0])
print(list)
print(type(list))
for i in enumerate(list): #shows index number with the element
    print(i)
