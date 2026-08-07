#no arguments and no return value
def sum():
    a=10
    b=5
    print(a+b)
sum()

#no arguments and return value
def sub():
    a=10
    b=5
    return (a-b)
print(sub())

#arguments and no return value
def mul(a, b):
    print(a*b)
mul(10, 5)

#arguments and return value
def div(a, b):
    return a/b
print(div(10, 5))
