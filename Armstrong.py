#Armstrong
a=int(input("Enter num:"))
s=0
b=0
l=len(str(a))
c=a
while(a>0):
    b=a%10
    s=s+(b**l)
    a=a//10
if(s==c):
    print("num is armstrong")
else:
    print("num is not armstrong")