class Employee:

    def __init__(self, e_name, e_salary, dept_no):
        self.name = e_name
        self.salary = e_salary
        self.department = dept_no

    def show_employee(self):
        print(
            f'Employee Name : {self.name}\nEmployee Salary : {self.salary}\n Employee Department :{self.department}\n')


class Salesman(Employee):

    def __init__(self, e_name, e_salary, dept_no, comm):
        self.Commission = comm
        super().__init__(e_name, e_salary, dept_no)

    def show_employee(self):
        super().show_employee()
        print(
            f'Employee Name : {self.name}\nEmployee Salary : {self.salary}\n Employee Department :{self.department}\n '
            f'Commission : {self.Commission}')


obj1 = Salesman('Pratik', '75000', '101', 25000)
obj1.show_employee()
# print(f'Commission : {obj1.Commission}')

obj2 = Employee('Pratik', '76000', '102')
obj2.show_employee()
