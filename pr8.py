a=int(input("Enter Num1:"))
c=int(input("Enter Num2:"))
if(a>c and a%2==0):
    while(a<=10 and a<=c):
        b=1
        while(b<=10):
            print(a,"X",b,"=",a*b)
            b+=1
        a+=1
    c+=1
else:
    while(a<=10 and a<=c):
        b=1
        while(b<=10):
            print(a,"X",b,"=",a*b)
            b+=1
        a+=1
    c+=1        