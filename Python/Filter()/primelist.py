def is_prime(x):
    if x <= 1:
        return False
    else:
        for i in range(2, (x // 2) + 1):
            if x % i == 0:
                return False
        else:
            return True

s = input("enter num list: ").split()
s = [int(i) for i in s]
p = list(filter(lambda n: is_prime(n), s))
print(p)