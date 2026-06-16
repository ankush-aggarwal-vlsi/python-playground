# 167 program DELETE ELEMENT BY INDEX
n = int(input("ENTER NUMBER OF ELEMENTS : "))
lst = []

for i in range(n):
    x = int(input("ENTER ELEMENT : "))
    lst.append(x)

print("ORIGINAL LIST :", lst)

index = int(input("ENTER INDEX TO DELETE : "))

if index < 0 or index >= n:
    print("INVALID INDEX")
else:
    lst.pop(index)
    print("LIST AFTER DELETION :", lst)