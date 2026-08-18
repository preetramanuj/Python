a=[]
f=[]
c=int(input("Enter size of list:"))
while(len(a)<c):
    b=input("Enter student name:")
    if b in a:
        print("Name exist")
        f.append(b)
    else:
        a.append(b)    
print("Your data entered")
print(a)
verify=input("You want to find student:")
if(verify=="yes"):
    Name=input("Enter name:")
    for i in range(0,c):
        if(Name==a[i]):
            print("Find sucessfull")
        else:
            print("Student not found")
elif(verify=="No"):
    print("Ok,No problem")
else:
    print("Invalid Input")    