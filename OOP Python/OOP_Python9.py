class A:
    def sum(self):
        a=int(input("Enter num1: "))
        b=int(input("Enter num2: "))
        return(a+b)

    def sub(self):
        a=int(input("Enter num1: "))
        b=int(input("Enter num2: "))
        return(a-b)

    def mul(self):
        a=int(input("Enter num1: "))
        b=int(input("Enter num2: "))
        return(a*b)
    
    def div(self):
        a=int(input("Enter num1: "))
        b=int(input("Enter num2: "))
        return(a/b)

class B:
    def Armstrong(self):
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
            return("num is armstrong")
        else:
            return("num is not armstrong")

    def Fibonacci_Series(self):
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

    def Palindrome(self):
        a=int(input("Enter num:"))
        s=0
        b=0
        c=a
        while(a>0):
            b=a%10
            s=(s*10)+b
            a=a//10
        if(s==c):
            return("num is Palindrome")
        else:
            return("num is not Palindrome")

A1=A()
B1=B()
ans=[]
print("1.sum\n2.sub\n3.mul\n4.div\n5.Armstrong\n6.Fibonacci_Series\n7.Palindrome\n8.Exit")
choice="0"
while(choice!=8):
    choice=input("Enter choice:")
    if choice=="1":
        ans.append(A1.sum())
        print(ans)
    elif choice=="2":
        ans.append(A1.sub())
        print(ans)
    elif choice=="3":
        ans.append(A1.mul())
        print(ans)
    elif choice=="4":
        ans.append(A1.div())
        print(ans)
    elif choice=="5":
        ans.append(B1.Armstrong())
        print(ans)
    elif choice=="6":
        ans.append(B1.Fibonacci_Series())
        print(ans)
    elif choice=="7":
        ans.append(B1.Palinrome())
        print(ans)
    elif choice=="8":
        break
    else:
        print("Invalid Choice")


