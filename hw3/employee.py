class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def increase_salary(self, percentage):
        self.salary = self.salary + self.salary * percentage
employee1 = Employee("John", 5000)
employee1.increase_salary(0.10)
print(employee1.salary)