# 170 program FIND DIFFERENCE OF LISTS
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

# Elements in lst1 but not in lst2
difference1 = []

for i in lst1:
    if i not in lst2 and i not in difference1:
        difference1.append(i)

# Elements in lst2 but not in lst1
difference2 = []

for i in lst2:
    if i not in lst1 and i not in difference2:
        difference2.append(i)

print("ELEMENTS IN LIST 1 BUT NOT IN LIST 2 :", difference1)
print("ELEMENTS IN LIST 2 BUT NOT IN LIST 1 :", difference2)
