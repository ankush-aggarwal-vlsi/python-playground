# 132 program REVERSE LIST
n = int(input("ENTER THE RANGE OF ELEMENTS IN A LIST : "))
lst = []

for i in range(n) :
    x = input("ENTER THE ELEMENTS IN A LIST : ")
    lst.append(x)

print("ORIGINAL LIST :",lst)

lst.reverse()

print("REVERSE LIST :",lst)
