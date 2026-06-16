# 126 program FIND SMALLEST NUMBER 
n = int(input("ENTER NUMBER OF ELEMENTS : "))
lst = []


for i in range(n) :
    x = int(input("ENTER THE ELEMENTS : "))
    lst.append(x)

smallest = lst[0]
for j in lst :
     if j < smallest :
         smallest = j

print ("LIST :",lst)
print("SMALLEST ELEMENT :",smallest)




