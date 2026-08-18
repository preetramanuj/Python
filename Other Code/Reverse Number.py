a=int(input("Enter num:"))
s=0
b=0
c=a
while(a>0):
    b=a%10
    s=(s*10)+b
    a=a//10
print(s)