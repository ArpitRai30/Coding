l = input("enter list: ").split()
l = [int(i) for i in l]
sq = list(map(lambda n: n ** 2, l))
print(sq)