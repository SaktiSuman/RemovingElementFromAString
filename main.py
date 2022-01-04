test_str = input("Enter the string: ")
n = int(input("Enter the index of the character you want to remove: "))
new_str = ""
for i in range(len(test_str)):
    if i != n:
        new_str = new_str + test_str[i]
print("The updated string is: ",new_str)