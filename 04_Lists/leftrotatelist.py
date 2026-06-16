# 149 program LEFT ROTATE LIST
n = int(input("ENTER THE RANGE OF ELEMENT IN A LIST : "))
lst = []

for i in range(n) :
    x = input("ENTER THE ELEMENT : ")
    lst.append(x)

print("LIST :",lst)
\
k = int(input("ENTER THE NUMBER OF TIMES LIST NEED TO BE ROTATED : "))

if k <= n and k >= 0 :
    print("ROTATION IS POSSIBLE.")
    for i in range(k) :
        x = lst.pop(0)
        lst.append(x)
    
    print("LIST AFTER",k,"TIMES ROTATION WILL BE :",lst)

else :
    print("LIST ROTATION MAY NOT POSSIBLE.")