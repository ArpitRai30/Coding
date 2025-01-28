s = input("enter num list: ").split()
s = [int(i) for i in s]
even = list(filter(lambda n: n % 2 == 0, s))
print(even)