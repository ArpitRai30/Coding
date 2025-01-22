def palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

s = input("Enter a string: ")
if palindrome(s) == True:
    print(f"\"{s}\" is palindrome")
else:
    print("String is not a palindrome")