# 147 program SPLIT POSITIVE AND NEGATIVE
n = int(input("ENTER THE RANGE OF ELEMENTS IN A LIST : "))
lst = []
positive_lst = []
negative_lst = []

for i in range(n) :
    x = int(input("ENTER THE ELEMENTS : "))
    lst.append(x)

print("LIST :",lst)

for i in lst :
    if i < 0 :
        positive_lst == x < 0
    else :
        negative_lst == x >= 0
    
print("POSITIVE LIST :",positive_lst)
print("NEGATIVE LIST :",negative_lst)
