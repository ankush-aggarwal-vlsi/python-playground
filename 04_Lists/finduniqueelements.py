# 136 program FIND UNIQUE ELEMENTS
n1 = int(input("ENTER THE RANGE OF ELEMENTS IN LIST 1 : "))
n2 = int(input("ENTER THE RANGE OF ELEMENTS IN LIST 2 : "))
lst1 = []
lst2 = []

for i in range(n1) :
    x = input("ENTER THE ELEMENTS IN LIST 1 : ")
    lst1.append(x)

for i in range(n2) :
    y = input("ENTER THE ELEMENT IN LIST 2 : ")
    lst2.append(y)

unique_elements = []
for i in lst1 :
    if i not in lst2 and i not in unique_elements :
        unique_elements.append(i)

for i in lst2 :
    if i not in lst1 and i not in unique_elements :
        unique_elements.append(i)

print("LIST 1 :",lst1)
print("LIST 2 :",lst2)
print("UNIQUE ELEMENTS LIST :",unique_elements)


