class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def get_salary(self):
        return self.salary
    def set_salary(self, new_salary):
        self.salary = new_salary
    @classmethod
    def calculate_average_salary(cls, employees):
        total_salary = 0
        for employee in employees:
            total_salary += employee.salary
        return total_salary / len(employees)
employees = [
        Employee("John Doe", 123456, 100000),
        Employee("Jane Doe", 678901, 120000),
        Employee("Peter Smith", 987654, 140000)
]
average_salary = Employee.calculate_average_salary(employees)
print("The average salary is", average_salary)
