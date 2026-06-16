# 144 program FIND SECOND LARGEST
n = int(input("ENTER THE RANGE OF ELEMENT IN A LIST :"))
lst = []

for i in range(n) :
    x = int(input("ENTER THE ELEMENT :"))
    lst.append(x)

print("LIST :",lst)

lst = list(set(lst))   #remove duplicates
lst.sort()

if len(lst) < 2 :
    print("THE SECOND LARGEST DOESN'T EXISTS.")
else :
    print("THE SECOND LARGEST NUMBER WILL BE :",lst[-2])
    
    

