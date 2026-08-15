a=int(input("Enter num1:"))
b=1
for i in range(a,0,-1):
    b*=i
print("Factorial of",a,"is",b)