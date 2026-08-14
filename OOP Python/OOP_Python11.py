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

class Rectangle(A):
    def area_of_rectangle(self):
        l=int(input("Enter l: "))
        b=int(input("Enter b: "))
        print(l*b)

A1=Rectangle()
A1.sum()
A1.sub()
A1.mul()
A1.div()
A1.area_of_rectangle()