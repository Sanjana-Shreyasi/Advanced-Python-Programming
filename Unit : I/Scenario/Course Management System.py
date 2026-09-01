#Unit 1 : Question 9
#Course Management System
class Course:
    def __init__(self, name, duration, fee):
        # storing basic details of a course
        self.name = name
        self.duration = duration
        self.fee = fee

    def get_type(self):
        # deciding if course is short term or long term
        if self.duration <= 6:
            return "short term"
        else:
            return "long term"

    def show(self):
        # printing all details of one course
        print("Course name:", self.name)
        print("Duration:", self.duration, "months")
        print("Fee:", self.fee)
        print("Type:", self.get_type())


class Institute:
    def __init__(self, name):
        self.name = name
        # list to store all courses
        self.courses = []

    def add_course(self, course):
        # adding one course to the list
        self.courses.append(course)
        print(course.name, "added to institute")

    def show_all(self):
        # showing every course one by one
        print("All courses in", self.name)
        for c in self.courses:
            c.show()
            print()


# creating institute object
inst = Institute("Sunrise Computer Institute")

# creating course objects
c1 = Course("Python basics", 3, 5000)
c2 = Course("Data science", 12, 25000)
c3 = Course("Excel for beginners", 2, 2000)

# adding courses to institute
inst.add_course(c1)
inst.add_course(c2)
inst.add_course(c3)

print()

# showing all courses at the end
inst.show_all()

#Output
'''Python basics added to institute
Data science added to institute
Excel for beginners added to institute

All courses in Sunrise Computer Institute
Course name: Python basics
Duration: 3 months
Fee: 5000
Type: short term

Course name: Data science
Duration: 12 months
Fee: 25000
Type: long term

Course name: Excel for beginners
Duration: 2 months
Fee: 2000
Type: short term'''