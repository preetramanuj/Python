c=""
while(c=="" or c==3):
    c=input("Enter Coice(1.login/n2.register/n3.reenter /n4.invalid): ")
    if(c=="1"):
        print("Login ")
        u=input("Enter username: ")
        p=input("Enter Password: ")
    elif(c=="2"):
        print("Register")
        u=input("Enter username: ")
        e=input("Enter Email: ")
        p=input("Enter Password: ")
    elif(c=="3"):
        print("reenter choice")
    else:
        print("invalid")
        break
