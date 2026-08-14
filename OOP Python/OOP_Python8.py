#whenever return come in fuction we use print to see data
class A:
    def sum(self):
        a=10
        b=5
        print(a+b)

    def sub(self):
        a=10
        b=5
        return (a-b)

    def mul(self, a, b):
        print(a*b)
    
    def div(self,a, b):
        return a/b

A1=A()
A1.sum()
print(A1.sub())
A1.mul(10, 5)
print(A1.div(10, 5))

        
