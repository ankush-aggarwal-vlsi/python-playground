# 141 program INSERT ELEMENT 
n = int(input("ENTER THE RANGE OF ELEMENTS IN A LIST : "))
lst = []

for i in range(n) :
    x = input("ENTER THE ELEMENT : ")
    lst.append(x)

print("LIST :",lst)

new_element = input("ENTER THE NEW ELEMENT THAT HAS TO BE INSERTED IN A LIST : ")
index = int(input("ENTER THE INDEX NUMBER WHERE THE NEW ELEMENT NEED TO BE INSERTED : "))

if index >= 0 and index <= n :
    lst.insert(index,new_element)

else :
    print("ENTER A VALID INDEX NUMBER")

print("THE LIST AFTER NEW ELEMENT WILL BE :",lst)
