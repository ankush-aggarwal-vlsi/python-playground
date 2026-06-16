# 148 program ROTATE LIST
n = int(input("ENTER THE RANGE OF ELEMENT IN A LIST : "))
lst = []

for i in range(n):
    x = int(input("ENTER THE ELEMENT : "))
    lst.append(x)

print("LIST :",lst)

k = int(input("ENTER THE NUMBER OF TIMES THE LIST NEED TO ROTATE : "))

if k <= n and k >= 0 :
    print("ROTATION IS POSSIBLE.")
    for i in range(k) :
        x = lst.pop(0)
        lst.append(x)
    
    print("ROTATED LIST WILL BE :",lst)

else :
    print("ROTATION IS NOT POSSIBLE.")
        
