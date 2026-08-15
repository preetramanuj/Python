a=int(input("Enter num1:"))
c=int(input("Enter num2:"))
if(a%2==0):
    for a in range(a,c+1):
        if(a%2!=0):
            for b in range(1,11):
                print(a,"X",b,"=",c*b)
else:
    if(a%2!=0):
        for a in range(a+1,c):
                if(a%2==0):
                    for b in range(1,11):
                        print(a,"X",b,"=",c*b)    


