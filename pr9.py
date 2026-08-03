a=int(input("Enter Num1:"))
c=int(input("Enter Num2:"))
if(a<c):
    while(a<=c):
        if(a%2 != 0):
            b=1
        while(b<=10):
            print(a,"X",b,"=",a*b)
            b+=1
        a+=1
    c+=1
else:
    while(c<=a):
        if(c%2 == 0):
            b=1
            while(b<=10):
                print(c,"X",b,"=",c*b)
                b+=1
        c+=1
    