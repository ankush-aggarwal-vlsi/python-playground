# 131 program SORT LIST DESCENDING
n = int(input("ENTER NUMBER OF ELEMENTS IN LIST : "))
lst = [0]

for i in range(n) :
    x = input("ENTER THE ELEMENTS IN A LIST : ")
    lst.append(x)

print("ORIGINAL LIST :",lst)

lst.sort(reverse = True) 

print("LIST IN DESCENDING ORDER :",lst)