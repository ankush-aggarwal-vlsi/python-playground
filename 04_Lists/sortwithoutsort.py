# 163 program SORT WITHOUT SORT()
n = int(input("ENTER NUMBER OF ELEMENTS : "))
lst = []

for i in range(n):
    x = int(input("ENTER ELEMENT : "))
    lst.append(x)

print("ORIGINAL LIST :", lst)

for i in range(n):
    for j in range(i + 1, n):
        if lst[i] > lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

print("SORTED LIST :", lst)

