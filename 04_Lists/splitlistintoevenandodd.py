# 146 program SPLIT LIST INTO EVEN & ODD
n = int(input("ENTER THE RANGE OF ELEMENT IN A LIST : "))
lst = []
even_lst = []
odd_lst = []

for i in range(n) :
    x = int(input("ENTER THE ELEMENTS : "))
    lst.append(x)

for x in lst :
    if x % 2 == 0 :
        even_lst.append(x)
    else : 
        odd_lst.append(x)

print("EVEN LIST :",even_lst)
print("ODD LIST",odd_lst)
