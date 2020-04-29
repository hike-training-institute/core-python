class Human:
    eyes = 2


class Employee(Human) :
    total_employee = 0
    basic_salary = 2000

    def __init__(self):
        self.increase_total_employee_count()

    @classmethod
    def increase_total_employee_count(cls):
        cls.total_employee += 1

    @classmethod
    def increase_basic_salary(cls, increment_amount):
        cls.basic_salary += increment_amount

    @staticmethod
    def increase_basic_salary(increment_amount):
        Employee.basic_salary += increment_amount

    def increment_emp_salary(self, salary_increment_amount):
        self.basic_salary += salary_increment_amount

ram = Employee()
ravi = Employee()

print(ram.basic_salary)
print(ravi.basic_salary)

ram.increase_basic_salary(1000)

gopal = Employee()
print(gopal.basic_salary)
