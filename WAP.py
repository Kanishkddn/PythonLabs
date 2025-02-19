#Q01
list1=[1,2,3,54,32,234,128]
print(max(list1))

#Q02
listn=list1
listn1=list1
list1.sort()
listn.sort(reverse=True)
if listn1==listn or list1==listn1:
    print("List is non-Monotonic.i.e not in order")

else:
    print("List is non monotonic.i.e. ordered")
#Q03
l11=[1,42,12,122,1,4,3]
list2=[1,5,2,3,2,32,1]
list3=[]
l4=[]
if len(l11)==len(list2):
    for i in range(len(list1)):
        e1=(l11[i]*list2[i])
        l4.append(e1)
    print(l4)
else:
    print("Lists not equal length")

#Q04
dict1={1:"1",2:"2",3:"12",4:"12",5:"2"}
set1=set(dict1.values())
print(f"The Unique values are: {set1}")

#Q05
dict2={1:"2",2:"23",3:"42",4:"11",5:"2"}
dict3={}
for t in range(len(dict2)):
    el1=(dict1["t"]*dict2[t])
    dict3[t]=el1
print(dict3)