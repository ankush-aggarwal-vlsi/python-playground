# 158 program FIND MAX DIFFERENCE
n = int(input("ENTER THE RANGE OF ELEMENTS IN A LIST : "))
lst = []

for i in range(n) :
    x = int(input("ENTER THE ELEMENTS : "))
    lst.append(x)

print("LIST :",lst)

max_val = max(lst) 
min_val = min(lst)
max_difference = max_val - min_val

print("MAX DIFFERENCE :",max_difference)