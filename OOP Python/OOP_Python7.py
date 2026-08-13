def sumation():
    a=int(input("Enter number you entered: "))
    sum=0
    for i in range(0,a):
        sum=int(input("Enter number: "))
        sum+=sum
    sum_list=[]
    sum_list.append(sum)
    print(sum_list)
    return sum
    
def subtraction():
    a=int(input("Enter number you entered: "))
    sub=0
    for i in range(0,a):
        sub=int(input("Enter number: "))
        sub-=sub
    sub_list=[]
    sub_list.append(sub)
    print(sub_list)
    return sub        
    
def multiplication():
    a=int(input("Enter number you entered: "))
    mul=1
    for i in range(0,a):
        mul=int(input("Enter number: "))
        mul*=mul
    mul_list=[]
    mul_list.append(mul)
    print(mul_list)
    return mul 

def divison():
    a=int(input("Enter number you entered: "))
    b=int(input("Enter number you entered: "))
    div=a/b
    div_list=[]
    div_list.append(div)
    print(div_list)
    return div

ans=[]
print("Enter Coice(1.sumation/n2.subtraction/n3.multiplication /n4.divison): ")
choice=input("Enter your choice: ")
while (choice!="5"):
    if choice=="1":
        ans.append(sumation())
        print(ans)
    elif choice=="2":
        ans.append(subtraction())
        print(ans)
    elif choice=="3":
        ans.append(multiplication())
        print(ans)
    elif choice=="4":
        ans.append(divison())
        print(ans)
    elif choice=="5":
        break
    else:
        print("Invalid choice")