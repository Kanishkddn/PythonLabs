#set is a collection of items (numbers, strings)
# #set itself is mutable, but elements of set are immutable
# '''Operation of sets'''
# set1={1,2,3,4,5}
# set2={"one","two","three","three"}
# print(set2)
# set3={1,1,2,3,3,4,5,5}#removes duplicates automatically because immutable elments
# print(set3)
# #set4={1,2,3,[5,6,8],9,10}#lists are not allowed in set because lists are mutable and hence override the function of set not being mutable
# #print(set4)

# '''comprehension'''
# setcomp={n for n in range(10) if n%2==0}
# print(setcomp)
# '''converting list into set'''
# list=set([s for s in range(1,11)])
# print(list)

# '''Addition in set'''
# set1.add('Nine')
# print(type(set1))

# '''Update'''
# set1.update([56,'one',1])
# print(set1)

# '''remove and discard'''
# set3.remove(4) #works only if the element is present in the set
# print(set3)

# set3.discard(1) #works even if the element is not present. therefore use only when you are not sure if elemnt is present in set or not
# print(set3)

# '''set operations'''
# # #union
# # intersection
# # superset
# # subset
# #disjoint