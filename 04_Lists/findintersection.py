# 169 program FIND INTERSECTION
n1 = int(input("ENTER NUMBER OF ELEMENTS IN LIST 1 : "))
lst1 = []

for i in range(n1):
    x = int(input("ENTER ELEMENT FOR LIST 1 : "))
    lst1.append(x)

n2 = int(input("\nENTER NUMBER OF ELEMENTS IN LIST 2 : "))
lst2 = []

for i in range(n2):
    y = int(input("ENTER ELEMENT FOR LIST 2 : "))
    lst2.append(y)

print("\nLIST 1 :", lst1)
print("LIST 2 :", lst2)

intersection = []

for i in lst1:
    if i in lst2 and i not in intersection:
        intersection.append(i)

print("INTERSECTION OF LISTS :", intersection)
