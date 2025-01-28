def count(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

s = input("Enter sentence: ")
print("No. of vowels:", count(s))