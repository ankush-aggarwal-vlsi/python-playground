# 128 program COUNT ODD NUMBER
n = int(input("ENTER THE NUMBER OF ELEMENTS IN A LIST : "))
lst = []

for i in range(n) :
    x = int(input("ENTER ELEMENTS IN A LIST : "))
    lst.append(x)

count = 0 
for j in lst :
    if j % 2 != 0 :
        count += 1

print("LIST :",lst)
print("NO OF ODD ELEMENTS IN LIST :",count)

