# 133 program COPY LIST
n = int(input("ENTER THE RANGE OF ELEMENTS IN A LIST : "))
lst = []

for i in range(n):
    x = input("ENTER THE ELEMENT IN A LIST : ")
    lst.append(x)

copy_lst = lst.copy()

print("ORIGINAL LIST :",lst)
print("COPY LIST",copy_lst)
