a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
if(a==b==0):
    print(a,b,"both are zero")
elif(a>0 and b<0):
    print(a,"is positive",b,"is nagative")
elif(a<0 and b>0):
    print(a,"is nagative",b,"is positive")   
elif(a>b>0):
    print(a,b,"both are positive")
elif(a<b<0):
    print(a,b,"both are nagative")    
elif(a==0 and b<0):
    print(a,"is zero",b,"is nagative") 
elif(a<0 and b==0):
    print(a,"is negative",b,"is zero")
elif(a>0 and b==0):
    print(a,"is positive",b,"is zero")
else:
    print(a,"is zero",b,"is positive")            
    