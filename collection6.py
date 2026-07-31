a=[]
b=[]
while(len(a)<3 or len(b)<3):
    c=input("Enter Choice: ")
    n=input("Enter name: ")
    if(c=="a" and len(a)!=3):
        if n not in a:
            a.append(n)
        else:
            b.append(n)
    elif(c=="b" and len(b)!=3):
        if n not in b:
            b.append(n)
        else:
            a.append(n)
    elif(len(a)==3 and len(b)!=3):
        b.append(n)
    print(a)
    print(b)
    
    
    