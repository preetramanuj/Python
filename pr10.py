a=int(input("Enter Num1:"))
b=int(input("Enter Num2:"))
c=0
if(a<b and a!=b):
    while(a<=b):
        a+=1
        c+=1
    print(c)
else:
    while(a>=b):
        a-=1
        c+=1
    print(c)