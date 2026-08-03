a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
c=int(input("Enter num3:"))
if(a>b>c):
    print(a,"is big")
elif(b>a>c):
    print(b,"is big")
elif(c>a>b):
    print(c,"is big")    
else:
    print("num1 and num2 and num3 are equal")