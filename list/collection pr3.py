a=[]
c=int(input("Enter size of array:"))
sum=0
for i in range(0,c):
    b=int(input("Enter Num:"))
    a.append(b)
print(a)
if(a[0]%2==0):   #even
    for i in range(0,c):
        if(a[i]%2!=0):
            sum+=a[i]
    print(sum)
else:   #odd
    for i in range(0,c):
        if(a[i]%2==0):
            sum+=a[i]
    print(sum)
