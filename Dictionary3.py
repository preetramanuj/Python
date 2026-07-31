dic1={}
dic2={}
c=int(input("Enter number of key-value pairs:"))
while(len(dic1)<c):
    k=input("Enter key:")
    v=input("Enter value:")
    if k in dic1:       
        if k in dic2:
            print("key exists")
        else:
            dic2[k]=v
    else:
        dic1[k]=v    
print(dic1)
print(dic2)