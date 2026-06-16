# 130 program SORT LIST ASCENDING
n = int(input("ENTER THE NUMBER OF ELEMENTS IN A LIST : "))
lst = []

for i in range(n) :
    x = input("ENTER THE ELEMENTS IN A LIST : ")
    lst.append(x)

print("ORIGINAL LIST :",lst)

lst.sort()

print("ASCENDING ORDER LIST :",lst)
