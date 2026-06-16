# 156 program FIND DUPLICATES 
n = int(input("ENTER THE RANGE OF ELEMENTS IN A LIST : "))
lst = []

for i in range(n) :
    x = int(input("ENTER THE ELEMENTS : "))
    lst.append(x)

print("LIST :",lst)

duplicates = []

for i in lst :
   if lst.count(i) > 1 and i not in duplicates :
       duplicates.append(i)

print("DUPLICATES ELEMENT :",duplicates)
    