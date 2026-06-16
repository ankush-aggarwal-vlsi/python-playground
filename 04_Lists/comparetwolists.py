# 162 program COMPARE TWO LISTS
# program COMPARE TWO LISTS

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

# 1. Check if both lists are exactly equal
if lst1 == lst2:
    print("\nBOTH LISTS ARE EXACTLY EQUAL")
else:
    print("\nLISTS ARE NOT EXACTLY EQUAL")

# 2. Check if both lists have same elements (order ignored)
if sorted(lst1) == sorted(lst2):
    print("BOTH LISTS HAVE SAME ELEMENTS (ORDER IGNORED)")
else:
    print("LISTS HAVE DIFFERENT ELEMENTS")

# 3. Find common elements
common = []

for i in lst1:
    if i in lst2 and i not in common:
        common.append(i)

print("COMMON ELEMENTS :", common)

# 4. Elements only in list 1
only_lst1 = []

for i in lst1:
    if i not in lst2:
        only_lst1.append(i)

print("ELEMENTS ONLY IN LIST 1 :", only_lst1)

# 5. Elements only in list 2
only_lst2 = []

for i in lst2:
    if i not in lst1:
        only_lst2.append(i)

print("ELEMENTS ONLY IN LIST 2 :", only_lst2)
