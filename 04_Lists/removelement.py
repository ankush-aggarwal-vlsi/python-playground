# 140 program REMOVE ELEMENT
n = int(input("ENTER THE RANGE OF THE ELEMENT IN A LIST : "))
lst = []
y = 0
for i in range(n) :
    x = input("ENTER THE ELEMENT : ")
    lst.append(x)

print("LIST WILL BE :",lst)

index = int(input("ENTER THE INDEX NUMBER THAT HAS TO REMOVE : "))

if index >= 0 and index < n :
    lst.pop(index)
else :
    print("PLEASE ENTER A VALID INDEX NUMBER.")

print("NEW LIST AFTER REMOVAL OF ELEMENT WILL BE :",lst)