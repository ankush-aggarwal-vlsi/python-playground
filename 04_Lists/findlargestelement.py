# 135 program FIND LARGEST ELEMENT
lst = [12,15,17,12,14,19,17,18,32,90,99,23,45,43,45,65]
largest = lst[0]
for i in lst :
    if i > largest :
        largest = i

print("LIST :",lst)
print("LARGEST ELEMENT :",largest)
