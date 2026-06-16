# Check if any element in a list is a palindrome

n = int(input("Enter the number of elements in the list: "))
lst = []

for i in range(n):
    x = input("Enter an element: ")
    lst.append(x)

print("LIST:", lst)

found = False  # To track if we found any palindrome

for i in range(n):
    if lst[i] == lst[i][::-1]:  # Reverse the element and check
        print("Palindrome found:", lst[i], "at index", i)
        found = True

if not found:
    print("No palindrome exists in the list.")
