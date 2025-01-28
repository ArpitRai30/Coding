# l = input("enter list: ").split()
# d = list(map(lambda n: n + '_done', l))
# print(d)


l = input("enter list: ").split()
d = list(map(lambda n: [n, '_done'], l))
print(d)