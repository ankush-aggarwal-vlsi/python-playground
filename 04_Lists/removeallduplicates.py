# 157 program REMOVE ALL DUPLICATES
n = int(input("ENTER THE RANGE OF ELEMENTS IN A LIST : "))
lst = []

for i in range(n):
    x = int(input("ENTER THE ELEMENT : "))
    lst.append(x)

print("LIST :", lst)

unique_lst = []

for i in lst:
    if i not in unique_lst:
        unique_lst.append(i)

print("LIST AFTER REMOVE DUPLICATES :", unique_lst)
