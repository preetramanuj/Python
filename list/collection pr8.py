a=int(input("Enter the size of array:"))
b=[]
c=[]
d=[]
while(len(b)<a):
    n=int(input("Enter num:"))
    b.append(n)
print(b)

#odd and even finding

for i in range(a):
    if(b[i]%2==0):#even
        c.append(b[i])
    else:#odd        
        d.append(b[i])               
print(c)
print(d)

#sorting

for i in range(len(c)):
    for j in range(i+1,len(c)):
        if(c[i]>c[j]):
            temp=c[i]
            c[i]=c[j]
            c[j]=temp
print("Sorted even numbers:",c)
for i in range(len(d)):
    for j in range(i+1,len(d)):
        if(d[i]>d[j]):
            d[j],d[i]=d[i],d[j]
print("Sorted odd numbers:",d)