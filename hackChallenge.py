#2import numpy
myArray1=[]
myArray=[]
myArray3=[]
p=5
for y in range(p):
    N, M = input("Enter a two value: ").split()
    myArray1.append(N)
    myArray.append(M)
for i in range(p):
    if int(myArray1[i])<int(myArray[i]):
        myArray3.append(int(myArray1[i]))
    else:
       myArray3.append(int(myArray[i]))

for ma in myArray3 : 
    max=0
    if ma>max: max=ma  
print(myArray3)   
print(max)