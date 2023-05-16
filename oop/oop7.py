class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.hired = False
        self.company = None
    def hire(self, company):
        if not self.hired:
            self.hired = True
            self.company = company
            self.company.add_employee(self)
            print(f"Employee {self.first_name} {self.last_name} has been hired by {company.name}.")
        else:
            print(f"Employee {self.first_name} {self.last_name} is already hired.")
    
    def fire(self):
        if self.hired:
            self.hired = False
            self.company.remove_employee(self)
            print(f"Employee {self.first_name} {self.last_name} has been fired from {self.company.name}.")
            self.company = None
        else:
            print(f"Employee {self.first_name} {self.last_name} is not currently employed.")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Company:
    def __init__(self, name):
        self.name = name
        self.employee_list = []
    
    def add_employee(self, employee):
        if employee not in self.employee_list:
            self.employee_list.append(employee)
            print(f"Employee {employee.first_name} {employee.last_name} has been added to the employee list at {self.name}.")
        else:
            print(f"Employee {employee.first_name} {employee.last_name} is already in {self.name}.")
    
    def remove_employee(self, employee):
        if employee in self.employee_list:
            self.employee_list.remove(employee)
            print(f"Employee {employee.first_name} {employee.last_name} has been removed from the employee list at {self.name}.")
        else:
            print(f"Employee {employee.first_name} {employee.last_name} is not in {self.name}.")
    
    def get_employee_list(self):
        return [str(employee) for employee in self.employee_list]
    
    def __str__(self):
        return self.name

company = Company("XYZ Industry")
employee1 = Employee("Jakub", "Kowalski")
employee2 = Employee("Daria", "Nowak")

employee1.hire(company)
employee2.hire(company)
print(company.get_employee_list())

employee1.fire()
print(company.get_employee_list())