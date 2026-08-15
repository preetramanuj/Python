#Constructor with parameter
class Numbre:
    def __init__(self,a,b):
        self.a=a
        self.b=b

class Arithmetic(Numbre):
    def sum(self):
        return(self.a + self.b)
    def sub(self):
        return(self.a-self.b)
    def mul(self):
        return(self.a*self.b)
    def div(self):
        return(self.a/self.b)
A1=Arithmetic(10,5)
print(A1.sum())
print(A1.sub())
print(A1.mul())
print(A1.div())