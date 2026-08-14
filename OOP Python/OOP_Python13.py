class Number:
    def __init__(self):
        self.a=int(input("Enter num1: "))
        self.b=int(input("Enter num2: "))

class Arithmetic(Number):
    def sum(self):
        return(self.a + self.b)
    def sub(self):
        return(self.a-self.b)
    def mul(self):
        return(self.a*self.b)
    def div(self):
        return(self.a/self.b)
    
A1=Arithmetic()
print(A1.sum())
print(A1.sub())
print(A1.mul())
print(A1.div())