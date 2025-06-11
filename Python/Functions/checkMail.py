def check_mail(s):
    if '@' in s and '.' in s:
        for i in s:
            if i.isalnum():
                return True
            elif i == '_':
                return True
            else:
                return False
    else:
        return False
    
m = input("Enter mail: ")
print(check_mail(m))