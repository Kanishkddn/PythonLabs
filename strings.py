str1='hello' #Strings can be stored with single '' and double "" quotes
#print(str1)
str2="We1c0me To Py7h0N\nhellooo" #''' triple quotes can be used for multi line string'''
#print(str2) #\n is new line
str3='''Hello
i am kanishk kumar studying
B.tech CSE from UPES ''' #For triple quote text, \n is not needed. You can just type in next line inside the quote
#print(str3)              
'''Triple quote gives multi line comments
 when not specified as a string'''
a='hello'
print(a*5) #Prints string 5 times
print(len(a))
print(a[0])#Prints the letter  at pos0
print(a[0:5])#Prints the letters from pos 0 to 5
print(a[-1])#prints from the right side as negative count is from right side
print(a[-4:])#prints from -4 pos to the end i.e -1
b="HelloFromThePythonLab"
print(b[0:-1])#prints elements from the 0th letter i.e h to the -1 letter i.e b

#SLICING OF VARIABLeS
for i in b:
    print(i)
x="Hello"
y=" There"
print(x+y)
ml='''Hello
i am kanishk Kumar
and i am a part of B.Tech CSE Batch 49'''

#IMMUTABILITY OF STRINGAS
A="WE1C0ME TO PY7H0N"
#A[0:6]="HELLOO" #Gives error hence proves that strings are immutable