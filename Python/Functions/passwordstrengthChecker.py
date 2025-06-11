def pass_str_chk(s):
    if len(s) >= 8:
        for i in s:
            if i in '!@#$%&*,./?;:<>':
                for j in s:
                    if j.isupper():
                        for k in s:
                            if k.isdigit():
                                print("Password accepted")
        print("Not accepted")
    else:
        print("Password not accepted")
            
p = input("Enter password: ")
pass_str_chk(p)