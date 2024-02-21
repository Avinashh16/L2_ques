class Student:

    def __init__(self,name,id,total,std):
        self.studentName = name
        self.studentId = id
        self.studentTotal = total
        self.studentClass = std


def sort(arr,parameter):
    n = len(arr)
    if parameter == "id":
        for i in range(n):
            for j in range(i+1,n):
                if arr[j].studentId < arr[i].studentId:
                    arr[i],arr[j] = arr[j],arr[i]
    elif parameter == "name":
        for i in range(n):
            for j in range(i+1,n):
                if arr[j].studentName < arr[i].studentName:
                    arr[i],arr[j] = arr[j],arr[i]

    elif parameter == "total":
        for i in range(n):
            for j in range(i+1,n):
                if arr[j].studentTotal < arr[i].studentTotal:
                    arr[i],arr[j] = arr[j],arr[i]
    
    elif parameter == "class":
        for i in range(n):
            for j in range(i+1,n):
                if arr[j].studentClass < arr[i].studentClass:
                    arr[i],arr[j] = arr[j],arr[i]
    
    return arr


    

        
n = int(input("Enter Number of students: "))
students = []

while n :
    name = input("Enter Student Name: ")
    id = input("Enter Student Id: ")
    total =  tudentTotal = input("Enter student Total: ")
    std = input("Enter Student Class: ")
    print()

    s = Student(name,id,total,std)

    students.append(s)

    n-=1
    
while True:
    parameter = input("Enter Sort Parameter : ")

    out = sort(students,parameter)

    for i in out:
        output = f"Name : {i.studentName} id : {i.studentId} total : {i.studentTotal} class : {i.studentClass}"
        print(output)

