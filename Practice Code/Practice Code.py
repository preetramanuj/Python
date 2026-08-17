a=int(input("Enter Num1:"))
b=int(input("Enter Num2:"))
if(a<b):
    for a in range(a,b+1):
        if(a%100==0 and a%400==0 or a%100!=0 and a%4==0):
            print(a)
else:
    for a in range(a,b+1,-1):
        if(a%100==0 and a%400==0 or a%100!=0 and a%4==0):
            print(a)
