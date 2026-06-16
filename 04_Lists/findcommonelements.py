# 135 program FIND COMMON ELEMENTS
n1 = int(input("ENTER THE RANGE OF ELEMENTS IN A LIST 1 :"))
n2 = int(input("ENTER THE RANGE OF ELEMENTS IN A LIST 2 :"))
lst1 = []
lst2 = []

for i in range(n1) :
    x = input("ENTER THE ELEMENT IN A LIST 1 : ")
    lst1.append(x)

for i in range(n2) :
    y = input("ENTER THE ELEMENT IN A LIST 2 : ")
    lst2.append(y)

common = []

for i in lst1 :
    if i in lst2 and i not in common :
        common.append(i)

print("LIST 1 :",lst1)
print("LIST 2 :",lst2)
print("COMMON ELEMENT IN A LIST :",common)

