# 129 program REMOVE DUPLICATES
n = int(input("ENTER NUMBER OF ELEMENTS IN  A LIST : "))
lst = []

for i in range(n) :
    x = input("ENTER ELEMENTS IN LIST : ")
    lst.append(x)

unique_lst = []
for j in lst :
    if j not in unique_lst :
        unique_lst.append(j)

print("ORIGINAL LIST :",lst)
print("LIST AFTER REMOVING DUPLICATES :",unique_lst)
    