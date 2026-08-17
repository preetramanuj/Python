a=0
b=1
e=int(input("Enter Num:"))
print(a)
print(b)
d=1
while(d<=e):
    c=a+b
    if(c<e):
        print(c)
        a=b
        b=c
    d+=1