def reverse(text):
    words = text.split()
    reverse = " ".join(reversed(words))
    return reverse

s = input("Enter sentence: ")
print("Reversed sentence:", reverse(s))