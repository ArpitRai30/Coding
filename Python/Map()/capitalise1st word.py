# s = input("enter list of strings:").split(",")
# new = list(map(lambda n: ' '.join(word[0].upper() + word[1:] for word in n.split()), s))
# print(new)


s = input("enter list of strings:").split(",")
new = list(map(lambda n: n.title(), s))
print(new)