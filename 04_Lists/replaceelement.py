# 139 program REPLACE ELEMENT
n = int(input("ENTER THE RANGE OF ELEMENT IN  A LIST : "))
lst = []

for i in range(n) :
    x = input("ENTER THE ELEMENT : ")
    lst.append(x)

print("LIST :",lst)

y = input("ENTER THE ELEMENT THAT HAS TO REPLACE : ")
index = int(input("ENTER THE INDEX NUMBER THAT HAS TO REPLACE : "))

if index >= 0 and index < n-1 :
    lst[index] = y 

else :
    print("ENTER VALID INDEX NUMBER.")
print("NEW LIST WILL BE :",lst)



