a=int(input("Enter the size of array:"))
b=[]
c=[]
d=[]
while(len(b)<a):
    n=int(input("Enter num:"))
    b.append(n)
print(b)
for i in range(0,a):
    if(b[i]%2==0):#even
        c.append(b[i])
    else:#odd        
        d.append(b[i])               
print(c)
print(d)