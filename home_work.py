class Employee:
    emp_count = 0
    work_rate = 2

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_count(self):
       pass

    def display_employee(self):
        print('Имя:'+ self.name + '   ' 'Зарплата:' + self.salary)

    def change_name(self, name):
        self.name = name

    def total_salary(self, salary):
        return self.salary

emp = Employee('', '200000')
emp.display_employee()
emp.change_name('Раильбджановрамиль')
emp.display_employee()