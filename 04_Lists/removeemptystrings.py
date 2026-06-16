# 153 program REMOVE EMPTY STRINGS
n = int(input("ENTER THE RANGE OF ELEMENTS IN A LIST : "))
lst = []

for i in range(n) :
    x = input("ENTER THE ELEMENTS : ")
    lst.append(x)

print("LIST :",lst)

new_lst = []

for i in lst : 
    if i != "" :
        new_lst.append(i)

print("LIST AFTER REMOVING EMPTY ELEMENT WILL BE :",new_lst)
    
