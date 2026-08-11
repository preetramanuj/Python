dic={"Roll_no":1,"Name":"Preet","Marks":85}
print(dic.keys())
print(dic.values())
print(dic.items())
dic["Marks"]=96
print(dic)  
dic["Name"]="Dax"
print(dic)
k=input("Enter key:")
v=input("Enter value:")
dic[k]=v
print(dic)