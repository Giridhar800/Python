users_dict = {}

while True:
    print("1.signup")
    print("2.signin")
    print("3.exit")

    opt = int(input("enter your option"))
    if opt == 1:
        uname = input("username")
        pwd = input("password")
        if uname in users_dict:
            print(uname,"exists")
        else:
            users_dict[uname] = pwd
            print("registered sucussfully")

    elif opt == 2:
        uname = input("user name")
        pwd = input("password")
        if uname in users_dict:
            p = users_dict[uname]
            if pwd == p:
                print(uname,"Wellcome...")
            else:
                print("invallid password")

    elif opt == 3:
        break
    
        
