class Employee:

    def __init__(self, e_name, e_salary, dept_no):
        self.name = e_name
        self.salary = e_salary
        self.department = dept_no

    def show_employee(self):
        print(f'Base/Parent Class : \n')
        print(
            f'Employee Name : {self.name}\nEmployee Salary : {self.salary}\nEmployee Department : {self.department}\n')


class Salesman(Employee):

    def __init__(self, e_name, e_salary, dept_no, comm):
        self.Commission = comm
        super().__init__(e_name, e_salary, dept_no)

    def show_employee(self):
        print(f'Calling parent class from inside Derived Class : \n')
        super().show_employee()
        print(f'Commission : {self.Commission}')


obj1 = Salesman('Pratik', '20000', '101', 25000)
obj1.show_employee()
# print(f'Commission : {obj1.Commission}')
