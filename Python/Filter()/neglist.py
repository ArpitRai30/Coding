s = input("enter num list: ").split()
s = [int(i) for i in s]
l = list(filter(lambda n: n >= 0, s))
print(l)