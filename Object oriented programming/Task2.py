from abc import ABC, abstractmethod


class Checker(Exception):

    def check_grade(self, grade):
        if grade < 0 or grade > 100:
            raise Checker("Grade must be between 0 and 100.")
        elif grade < 40:
            raise Checker("Not Passed")
        return grade

    def check_salary(self, salary):
        if salary < 0:
            raise Checker("Salary must be positive.")
        return salary

    def check_details(self, name, age, phone_number):
        if not name.isalpha():
            raise Checker("Name must contain only letters.")
        elif age < 18 or age > 65:
            raise Checker("Age must be between 18 and 65.")
        elif not phone_number.isdigit() or len(phone_number) != 10:
            raise Checker("Phone number must be 10 digits.")
        return name, age, phone_number


class Details(ABC):

    @abstractmethod
    def __init__(self, name, age, phone_number):
        pass


class Student(Details, Checker):

    Students = []

    def __init__(self, name, age, phone_number, grade):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.grade = grade
        Student.Students.append(self)

    @staticmethod
    def view_details(details):
        for detail in details:
            print(f"Name: {detail.name}, Age: {detail.age}, Phone: {detail.phone_number}, Grade: {detail.grade}")


class Employee(Details, Checker):

    Employees = []

    def __init__(self, name, age, phone_number, salary):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.salary = salary
        Employee.Employees.append(self)

    @staticmethod
    def view_details(details):
        for detail in details:
            print(f"Name: {detail.name}, Age: {detail.age}, Phone: {detail.phone_number}, Salary: {detail.salary}")


checker = Checker()

while True:
    try:
        ch = int(input("""
1. Add Student
2. Add Employee
3. View Student Details
4. View Employee Details
5. Exit
Choice: """))

        if ch == 1:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            phone = input("Enter phone number: ")
            grade = int(input("Enter grade: "))

            checker.check_details(name, age, phone)
            checker.check_grade(grade)

            Student(name, age, phone, grade)

        elif ch == 2:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            phone = input("Enter phone number: ")
            salary = int(input("Enter salary: "))

            checker.check_details(name, age, phone)
            checker.check_salary(salary)

            Employee(name, age, phone, salary)

        elif ch == 3:
            Student.view_details(Student.Students)

        elif ch == 4:
            Employee.view_details(Employee.Employees)

        elif ch == 5:
            print("Exiting...")
            break

    except Checker as e:
        print("Error:", e)