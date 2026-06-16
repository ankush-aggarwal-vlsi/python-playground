# 150 program RIGHT ROTATE LIST
n = int(input("ENTER THE RANGE OF ELEMENTS IN A LIST : "))
lst = []

for i in range(n) :
    x = input("ENTER THE ELEMENT : ")
    lst.append(x)

print("LIST :",lst)

k = int(input("ENTER THE NUMBER OF TIMES LIST NEED TO ROTATE : "))

if k >= 0 and k <= n :
    print("ROTATION IS POSSIBLE.")
    for i in range(k) :
        x = lst.pop(n-1)
        lst.insert(0,x)
    print("LIST AFTER",k,"TIMES WILL BE :",lst)

else :
    print("ROTATION IS NOT POSSIBLE.")