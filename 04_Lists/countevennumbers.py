# 127 program COUNT EVEN NUMBERS
n = int(input("ENTER NUMBER OF ELEMENTS : "))
lst = []

for i in range(n) :
    x = int(input("ENTER ELEMENTS : "))
    lst.append(x)

count = 0
for j in lst :
    if j % 2 == 0 :
        count += 1

print("LIST :",lst)
print("THE NUMBER OF EVEN ELEMENTS :",count)
        