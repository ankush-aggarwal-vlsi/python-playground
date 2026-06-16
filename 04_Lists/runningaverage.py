# 161 program RUNNING AVERAGE
n = int(input("ENTER NUMBER OF ELEMENTS : "))
lst = []

for i in range(n):
    x = int(input("ENTER ELEMENT : "))
    lst.append(x)

print("LIST :", lst)

total = 0
running_avg = []

for i in range(len(lst)):
    total += lst[i]
    avg = total / (i + 1)
    running_avg.append(avg)

print("RUNNING AVERAGE :", running_avg)
