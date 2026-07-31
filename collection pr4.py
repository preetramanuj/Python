a=[]
c=int(input("Enter size of array:"))

for i in range(0,c):
    b=int(input("Enter num:"))
    a.append(b)
print(a)
for i in range(0,c):
    num=a[i]
    d=0
    r_num=0
    while(num>0):
        d=num%10
        r_num=(r_num*10)+d
        num=num//10
        if(a[i]==r_num):
            print(a[i])

        
