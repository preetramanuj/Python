#Inheritance
class A:
    def sum(self):
        a=10
        b=5
        print(a+b)

class B(A):
    def sub(self):
        a=10
        b=5
        print(a-b)
B1=B()
B1.sum()
B1.sub()