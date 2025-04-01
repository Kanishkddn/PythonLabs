class person:
    name="Kanishk"
    occupation="Musician"
    salary=10000

    def info(self): #self is first keyword of the class
        print(f"{self.name} is a {self.occupation}")

p1=person()
print(p1.name,p1.occupation)# Kanishk Musician

p1.info()#Kanishk is a Musician

p1.name="Keval" #modified previous entry
p1.salary=1000  #modified previous entry

print(p1.name,p1.salary)

class employee:
    def __init__(self,n,s):
        print("Hey, How are you doing")
        self.name=n
        self.salary=s
    def info(self):
        print(f"{self.name} salary is {self.salary}")
e1=employee() #Hey, How are you doing

e1=employee("Krishna",1000)
e2=employee("Abhinav",100)
e3=employee("marco",10000000)

e1.info()
e2.info()
e3.info()

#WAP to handle division by 0 exception
#WAP to handle multiple exceptions
#WAP to handle custom exceptions
#WAP to use finally and else exceptionality