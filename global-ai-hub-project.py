# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 21:11:00 2020

@author: iremdogan
"""

class Student:
    
    enrolledLecture = {}
    lectureCount = 0
    average = 0
    grade = {}
    count = 3
    
    def __init__(self, name = "", surname = ""):
        self.name = name;
        self.surname = surname
        
    def changeName(self, name, surname):
        self.count -= 1
        self.name = name
        self.surname = surname
        
    def calculateGrade(self):
        for x,y in self.enrolledLecture.items():
            if (y[0] * 0.3 + y[1] * 0.5 + y[2] * 0.2) >= 90:
                self.grade[x] = "AA"
            elif 70 <= int(y[0]* 0.30 + y[1] * 0.5 + y[2] * 0.2) < 90:
                self.grade[x] = "BB"
            elif 50 <= int(y[0] * 0.30 + y[1] * 0.5 + y[2] * 0.2) < 70:
                self.grade[x] = "CC"
            elif 30 <= int(y[0] * 0.30 + y[1] * 0.5 + y[2] * 0.2) < 50:
                self.grade[x] = "DD"
            elif int(y[0] * 0.30 + y[1] * 0.5 + y[2] * 0.2) < 30:
                self.grade[x] = "FF"
        for x,y in self.grade.items():
            print(f"Course : {x}, Grade : {y}")
        
    def createLecture(self, lecName, midterm, final, project):
        self.lectureCount += 1
        self.lecName = lecName
        self.midterm = midterm
        self.final = final
        self.project = project
        self.enrolledLecture[self.lecName] = [self.midterm, self.final, self.project]
        

    def printEnrolledLecture(self):
        return self.enrolledLecture
    
    def printEnrolledLectureKeys(self):
        count = 1
        for x in self.enrolledLecture.keys():
            print(f"Course {count} : {x}")
            count += 1


case={
    1:"1- Change Student",
    2:"2- Enroll Class",
    3:"3- Calculate Grade",
    4:"4- Show Courses",
    "Default":"Wrong input!"}


_name = "İrem"
_surname = "Doğan"
flag = False

for i in range(3):
    name = input("Enter Name :")
    surname = input("Enter Surname :")
    if _name == name.replace(" ", "") and _surname == surname.replace(" ", "") :
        student = Student(name,surname)
        print(f"Welcome {student.name} {student.surname} \n")
        flag = True
        break
    else :
        print("Wrong Student!")
        flag = False

if not flag:
    print("Please try again later")

while flag : 
    for i in case.values():
        if i in "Wrong input! \n":
            pass
        else:
            print(i)
    switch = int(input("Your selection :  \n"))

    if switch == 1:
        if(student.count > 0):
            newName = input(f"{student.count} times left Enter Name: \n")
            newSurname = input(f"{student.count} times left Enter Surname: \n")
            student.changeName(newName,newSurname)
            print(f"Name has changed as {student.name} {student.surname} \n")
        else:
            print("No more changes :( \n")
            
    elif switch == 2:
        if student.lectureCount > 5 :
            print("You can not enter new lecture \n")
        else:
            lecName = input("Enter Course Name: \n")
            midterm = int(input("Enter Midterm: \n"))
            final = int(input("Enter Final: \n"))
            project = int(input("Enter Project: \n"))
            student.createLecture(lecName,midterm,final,project)
            print("Successfull enrollment \n")
    elif switch == 3:
        if student.lectureCount > 2 :
              student.calculateGrade()
        else:
            print(f"You need to enroll at least 3 classes. You have {student.lectureCount} class \n")
    elif switch == 4:
        if student.lectureCount>0 :
            student.printEnrolledLectureKeys()
        else:
            print("Please enter lecture \n")
    else:
        case["Default"]
        
    flag = input("Would you like to continue Y/N \n")
    
    if flag == "y" or flag == "Y" :
        flag = True
    else:
        flag = False
        print("See you next time!")



















