Name=input("Enter Name:")
a=int(input(F"Enter  age of {Name}: "))
if(a>=18):
    print(Name,"are eligible for vote")
if(a<18 and a>0):
    print(Name,"are eligible not vote,",Name,"need",18-a,"for voting")
if(a<=0):
    print(Name,"invalid age")