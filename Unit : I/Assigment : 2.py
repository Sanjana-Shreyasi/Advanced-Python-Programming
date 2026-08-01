#Assigment : 2
def payslip_header(func):
    def wrapper(*args, **kwargs):
        print("*" * 40)
        print("   EMPLOYEE PAYSLIP")
        print("*" * 40)
        func(*args, **kwargs)
        print("*" * 40)
    return wrapper


class Payslip:
    company = "Sunrise Pvt Ltd"

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    def __str__(self):
        return f"Name : {self.name}\nEmp ID : {self.emp_id}\nSalary : {self.salary}"

    @payslip_header
    def show_payslip(self):
        print("Company :", Payslip.company)
        print(self)
        if self.salary >= 20000:
            print("Grade : A")
        else:
            print("Grade : B")


emp1 = Payslip("Rahul", 1, 25000)
emp1.show_payslip()

print()

Payslip.change_company("Global Tech Solutions")
emp2 = Payslip("Priya", 2, 18000)
emp2.show_payslip()

#Output
'''****************************************
   EMPLOYEE PAYSLIP
****************************************
Company : Sunrise Pvt Ltd
Name : Rahul
Emp ID : 1
Salary : 25000
Grade : A
****************************************

****************************************
   EMPLOYEE PAYSLIP
****************************************
Company : Global Tech Solutions
Name : Priya
Emp ID : 2
Salary : 18000
Grade : B
****************************************'''