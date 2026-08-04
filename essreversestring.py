print("Now We Will Reverse The String")
string = input()
print("The Original String is:", string)

# Reversing the string using slicing
reversed_string = string[::-1]

# Printing the reversed string
print("The Reversed String is:", reversed_string)

# Printing characters at even indexes using slicing
new_string = string[0::2]
print("Characters at even indexes are:", new_string)
# Printing the character at index 6 using simple indexing
print("The character at index 6 is:", string[6])