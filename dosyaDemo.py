def AverageGrade(line):
    line=line[:-1]
    myList=line.split(":")
    studentName=myList[0]
    grades=myList[1]

    grade1=int(grades[0])
    grade2=int(grades[1])
    grade3=int(grades[2])

    average=(grade1+grade2+grade3)/3
    return average

def SeeGrades():
    with open("examGrades.txt","r",encoding="utf-8") as file:
        for line in file: print(AverageGrade(line))

def InsertGrade():
    name=input("Student name: ")
    surname=input("Student surname: ")
    grade1=input("Grade 1: ")
    grade2=input("Grade 2: ")
    grade3=input("Grade 3: ")

    with open("examGrades.txt","a",encoding="utf-8") as file: #If there isn't that file, "a" will create it
        file.write(name+" "+surname+":"+grade1+","+grade2+","+grade3+"\n")

def SaveGrades():
    pass

while True:
    selectTransaction=int(input("\n1) See grades\n2) Insert new grade\n3) Save grades\nOTHERS) Exit the program\nYour selection: "))
    print()
    if selectTransaction==1:
        SeeGrades()
    elif selectTransaction==2:
        InsertGrade()
    elif selectTransaction==3:
        SaveGrades()
    else: break
