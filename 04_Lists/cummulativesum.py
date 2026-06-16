# 160 program CUMMULATIVE SUM
n = int(input("ENTER NUMBER OF ELEMENTS : "))
lst = []

for i in range(n):
    x = int(input("ENTER ELEMENT : "))
    lst.append(x)

print("LIST :", lst)

cumulative_sum = []
total = 0

for i in lst:
    total += i
    cumulative_sum.append(total)

print("CUMULATIVE SUM :", cumulative_sum)