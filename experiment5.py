'''Strings and sets'''
#Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
# a) Fruits which are in both sets s1 and s2
# b) Fruits only in s1 but not in s2
# c) Count of all fruits from s1 and s2
n=int(input("enter the number of fruits for each set"))
s1=set()
s2=set()
print("enter the fruits for the set (s1):")
for i in range(n):
    fruit = input(f"Enter fruit{i+1}:")
    s1.add(fruit)
print("enter the fruits for the set (s2)")
for i in range(n):
    fruit=input(f"Enter fruit{i+1}:")
    s2.add(fruit)

print("The fruits in set 1 is\n",s1)
print("The fruits in set 2 is\n",s2)
print("The common elements in s1 and s2 is")
print(s1.intersection(s2))
print("The elements which are in ")
print("The number of elements in set is")
count=len(s1)+len(s2)
print(count)

# Take two sets and apply various set operations on them :
# S1 = {Red ,yellow, orange , blue }
# S2 = {violet, blue , purple}

S1 = {"Red", "yellow", "orange", "blue"}
S2 = {"violet", "blue", "purple"}
print("Union S1 and S2:",S1.union(S2))
print("Intersection S1 and S2:",S1.intersection(S2))
print("Difference S1 - S2:",S1.difference(S2))
print("Difference S2 - S1:",S2.difference(S1))
print("superset union S1, S2 is :",S1.issuperset(S2))
print("checking subset",S1.issubset(S2))
print("checking if both the sets have a common element:",S1.isdisjoint(S2))

# Scan n values in range 0-3 and print the number of times each value has
# occurred.
n = int(input("Enter the number of values for frequency check: "))

count = [0] * 4 

print(f"Enter {n} values in the range 0-3:")
for t in range(n):
    val = int(input())
    if 0 <= val <= 3:
        count[val] += 1
    else:
        print(f"invalid input: {val}")

print("occurrences of each:")
for i in range(4):
    print(f"{i}: {count[i]}")

#Create a tuple to store n numeric values and find average of all values.
u=int(input("Enter no. of values you want to enter: "))
values=tuple(float(input("Enter the numbers: ")) for a in range(u))

final=sum(values)/u
print(final)

#Print all the pallindrome and armstrong numbers between 0-1000 in two different lists, repeat the same for tuples and sets.
listarm = [num for num in range(1, 1001) if num==sum(int(digit)**len(str(num)) for digit in str(num))]
setarm = set(num for num in range(1, 1001) if num==sum(int(digit)**len(str(num)) for digit in str(num)))
tuplearm= tuple(num for num in range(1, 1001) if num==sum(int(digit)**len(str(num)) for digit in str(num)))

print(listarm)
print(setarm)
print(tuplearm)

palilist = [num for num in range(1001) if str(num) == str(num)[::-1]]
paliset= set(num for num in range(1001) if str(num) == str(num)[::-1])
palituple= tuple(num for num in range(1001) if str(num) == str(num)[::-1])


print(palilist)
print(paliset)
print(palituple)