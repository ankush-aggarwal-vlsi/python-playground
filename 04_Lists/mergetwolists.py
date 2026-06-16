# 134 program MERGE TWO LISTS
n1 = int(input("ENTER THE RANGE OF ELEMENT IN A LIST 1 : "))
n2 = int(input("ENTER THE RANGE OF ELEMENT IN A LIST 2 : "))
lst1 = []
lst2 = []

for i in range(n1) :
    x = input("ENTER THE ELEMENTS FOR LIST 1 ")
    lst1.append(x)

for i in range(n2) :
    y = input("ENTER THE ELEMENTS FOR LIST 2")
    lst2.append(y)

print("LIST 1 :",lst1)
print("LIST 2 :",lst2)

merge = lst1 + lst2

print("LSIT AFTER MERGE :",merge)
