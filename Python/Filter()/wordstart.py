# s = input("enter list: ").split()
# ch = input("enter ch to search-: ")
# l = list(filter(lambda n: n.lower().startswith(ch.lower()), s))
# print(l)


s = input("enter list: ").split()
ch = input("enter ch to search: ")
l = list(filter(lambda n: n[0].lower() == ch.lower(), s))
print(l)