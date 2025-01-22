def get_initials(fullName):
    names = fullName.split()
    initials = "".join(name[0] for name in names).upper()
    return initials

n = input("Enter full name: ")
print("Initials:", get_initials(n))