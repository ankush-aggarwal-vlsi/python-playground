# 164 program FIND MEDIAN
n = int(input("ENTER NUMBER OF ELEMENTS : "))
lst = []

for i in range(n):
    x = int(input("ENTER ELEMENT : "))
    lst.append(x)

print("LIST :", lst)

# sort without using sort()
for i in range(n):
    for j in range(i + 1, n):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("SORTED LIST :", lst)

# find median
if n % 2 != 0:
    median = lst[n // 2]
else:
    median = (lst[n // 2 - 1] + lst[n // 2]) / 2

print("MEDIAN :", median)
