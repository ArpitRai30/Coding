s1 = input("enter list 1: ").split()
s2 = input("enter list 2: ").split()
l = list(map(lambda n1, n2: n1 + ' ' + n2, s1, s2))
print(l)