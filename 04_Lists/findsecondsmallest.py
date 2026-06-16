# 145 program FIND SECOND SMALLEST
n = int(input("ENTER THE RANGE OF THE ELEMENTS IN A LIST : "))
lst = []

for i in range(n) :
    x = int(input("ENTER THE ELEMENT : "))
    lst.append(x)

print("LIST :",lst)

lst = list(set(lst))   # remove duplicates
lst.sort()

if len(lst) < 2 :
    print("THE SECOND SMALLEST DOESN'T EXISTS.")
else :
    print("THE SECOND SMALLEST NUMBER WILL BE :",lst[1])