# Function to get student names
def Student_name(num):
    a=[]
    for i in range(5):
        num=int(input("Enter the name of student: "))
        a.append(num)
    return a
print(Student_name("num"))