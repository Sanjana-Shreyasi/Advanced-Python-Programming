#OOPS concept

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

    def result(self):
        if self.marks >= 40:
            print(self.name, "has passed")
        else:
            print(self.name, "has failed")


#Creating objects
s1 = Student("Sanjana", 101, 78)
s2 = Student("Yash", 102, 35)

s1.display()
s1.result()
s2.display()
s2.result()

'''Name: Sanjana
Roll No: 101
Marks: 78
Sanjana has passed
Name: Yash
Roll No: 102
Marks: 35
Yash has failed'''