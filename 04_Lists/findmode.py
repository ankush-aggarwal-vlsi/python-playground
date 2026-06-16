# 165 program FIND MODE
n = int(input("ENTER NUMBER OF ELEMENTS : "))
lst = []

for i in range(n):
    x = int(input("ENTER ELEMENT : "))
    lst.append(x)

print("LIST :", lst)

max_count = 0
mode = lst[0]

for i in lst:
    count = lst.count(i)
    if count > max_count:
        max_count = count
        mode = i

print("MODE :", mode)
