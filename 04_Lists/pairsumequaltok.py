# 155 program PAIR SUM EQUAL TO K
n = int(input("ENTER THE RANGE OF ELEMENTS IN A LIST : "))
lst = []

for i in range(n) :
    x = int(input("ENTER THE ELEMENT : "))
    lst.append(x)

print("LIST :",lst)

k = int(input("ENTER THE VALUE OF K : "))

found = False 

for i in range(n) :
    for j in range((i + 1) , n) :
        if lst[i] + lst[j] == k :
            print("PAIR FOUND :",lst[i],lst[j])
            found = True

if found == False :
    print("PAIR NOT FOUND.")

