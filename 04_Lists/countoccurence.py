# 142 program COUNT OCCURENCE
n = int(input("ENTER THE RANGE OF THE ELEMENT IN A LIST : "))
lst = []

for i in range(n) :
    x = input("ENTER THE ELEMENTS : ")
    lst.append(x)

print("LIST :",lst)

y = input("ENTER THE ELEMENT WHOSE OCCURENCE NEED TO COUNT IN A LIST : ")

if y in lst :
    count = lst.count(y)
    print("NO OF OCCURENCE OF ELEMENT :",count)

else :
    print("THE ELEMENT IS NOT PRESENT IN LIST.")
