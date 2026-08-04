#Sorting
def student_num(a):
    a=[]
    for i in range(5):
        num=int(input("Enter the number of student: "))
        a.append(num)
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a

