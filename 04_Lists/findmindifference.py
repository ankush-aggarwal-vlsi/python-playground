# 159 program FIND MIN DIFFERENCE
n = int(input("ENTER THE RANGE OF ELEMENTS IN A LIST : "))
lst = []

for i in range(n) :
    lst.append(int(input("ENTER THE ELEMENTS : ")))

print("LIST :",lst)

lst.sort()

min_difference = lst[1] - lst[0]

for i in range(len(lst) - 1):
    diff = lst[i+1] - lst[i]
    if diff < min_diff:
        min_diff = diff

print("MIN DIFFERENCE :", min_diff)
