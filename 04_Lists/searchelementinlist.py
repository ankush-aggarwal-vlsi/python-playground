#137 program SEARCH ELEMENT IN LIST
n = int(input("ENTER THE RANGE OF ELEMENTS IN A LIST : "))
lst = []

for i in range(n) :
    x = input("ENTER THE ELEMENTS IN A LIST : ")
    lst.append(x)

print("LIST : ",lst)

y = input("ENTER THE ELEMENT THAT HAS TO BE CHECK IN LIST : ")

if y in lst :
    print("THE GIVEN ELEMENT IS PRESENT IN LIST.")
    print("PRESENT AT INDEX :",lst.index(y))
else :
    print("THE GIVEN ELEMENT IS NOT IN LIST")






