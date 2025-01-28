s = input("enter str list: ").split(",")
l = list(filter(lambda n: len(n) >= 5, s))
print(l)