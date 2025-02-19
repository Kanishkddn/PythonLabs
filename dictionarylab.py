# 1.Create a dictionary of n persons where key is name and value is city.
# a) Display all names
# b) Display all city names
# c) Display student name and city of all students.
# d) Count number of students in each city

mess=int(input("How many numbers do you want: "))
dictionary1={}

for x in range(mess):
    name=input("Enter Name: ")
    city=input("Enter city: ")
    dictionary1[name]=city


print("\n All Names are: ", dictionary1.keys())
print("\n All city names are: ", dictionary1.values())
print("\n",dictionary1)

# Store details of n movies in a dictionary by taking input from the user. Each
# # movie must store details like name, year, director name, production cost,
# # collection made (earning) & perform the following :-
# # a) print all movie details
# # b) display name of movies released before 2015
# # c) print movies that made a profit.
# # d) print movies directed by a particular director.

# num=int(input("How many movies do you want to enter: "))
# name=[num]
# year=[num]
# dn=[num]
# pc=[num]
# col=[num]

# for t in range(num):
#     name[t]=input(f"Enter Name{t}: ")
#     year[t]=input(f"Enter year{t}: ")
#     dn[t]=input(f"Enter director {t} name: ")
#     pc[t]=input(f"Enter production cost{t}: ")  
#     col[t]=input(f"Enter earnings for movie {t}: ")
# dictionarymov={1:name,2:year,3:dn,4:pc,5:col}

# print(dictionarymov)
# for x in range(num):
#     if year[x]<=2015:
#         print(name[x])

#     if col[x]>pc[x]:
#         print(f"\n{name[x]} made a profit")



    