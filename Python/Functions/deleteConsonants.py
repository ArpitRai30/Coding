s = input("Enter string: ")
new = ""
for char in s:
    if char in "aeiouAEIOU":
        new += char

print(new)