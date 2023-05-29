class Company:
    def __init__(self, name) -> None:
        self.name = name
        self.employee_list = []
    def add_employee(self, employee):
        if employee not in self.employee_list:
            self.employee_list.append(employee)
            employee.add_company(self)
    def rem_employee(self, employee):
        if employee in self.employee_list:
            self.employee_list.remove(employee)
            employee.rem_company(self)
    def show_all_employees(self):
        return [str(employee) for employee in self.employee_list]
    def __str__(self) -> str:
        return f"{self.name}"
    
class Employee:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.company = None
        self.is_hired = False
    def add_company(self, company_name):
        if self.company != None and self.is_hired == True:
            if self.company != company_name:
                print(f"Employee {self.first_name} {self.last_name} already has a job in {self.company} you can't add him to {company_name}")
        else:
            self.is_hired = True
            self.company = company_name
            company_name.add_employee(self)
    def rem_company(self, company_name):
        if self.is_hired == True:
            self.is_hired = False
            company_name.rem_employee(self)
            self.company = None
    def show_info(self):
        return f"{self.first_name} {self.last_name} {self.company}"
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
emp1 = Employee("Jakub","Nowak")
emp2 = Employee("Maciej","Kowalski")

com = Company("ABC Company")
com2 = Company("XYZ Industries")

emp1.add_company(com)
emp2.add_company(com)

print(f"1st: {com.show_all_employees()}")

emp1.rem_company(com)
emp1.rem_company(com)

print(f"2st: {com.show_all_employees()}")

print(emp2.show_info())