class Rectangle:
    def __init__(self, side_a, side_b) -> None:
        self.side_a = side_a
        self.side_b = side_b
    
    def calculate_area(self):
        return self.side_a * self.side_b

    def calculate_circumference(self):
        return 2 * self.side_a + 2 * self.side_b
    
    def check_if_square(self):
        if (self.side_a == self.side_b):
            return f"Rectangle with a: {self.side_a} b: {self.side_b} is a Square"
        else:        
            return f"Rectangle with a: {self.side_a} b: {self.side_b} is NOT a Square"
        
# rec1 = Rectangle(4,5)
# rec2 = Rectangle(10,10)
# print(rec1.calculate_area())
# print(rec1.calculate_circumference())
# print(rec1.check_if_square())
# print(rec2.check_if_square())

class Student:
    def __init__(self, name, surname, year, grades_list) -> None:
        self.name = name
        self.surname = surname
        self.year = year
        self.grades_list = grades_list

    def add_grade(self, new_grade):
        self.grades_list.append(new_grade)

    def calculate_avg(self):
        avg = sum(self.grades_list)/len(self.grades_list)
        return f"The avg grade for {self.name} {self.surname} is {avg}"
    
    def check_if_last_year(self):
        if (self.year == 4):
            return f"The student {self.name} {self.surname} is at last year: {self.year}"
        else:
            return f"The student {self.name} {self.surname} is not at last year: {self.year}"
        
    def show_student_info(self):
        print (f"Student {self.name} {self.surname} at {self.year}, grades list: ")
        for x in self.grades_list:
            print(x)

# stu = Student("Jakub", "Nowak", 4, [2,2,6,6,3])
# stu.add_grade(1)
# print(stu.calculate_avg())
# print(stu.check_if_last_year())
# stu.show_student_info()

class Client:
    def __init__(self, first_name, last_name, account_number, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.balance = balance


class Bank:
    def __init__(self):
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)

    def remove_client(self, account_number):
        for client in self.clients:
            if client.account_number == account_number:
                self.clients.remove(client)
                print(f"Client with account number {account_number} removed.")
                return
        print(f"No client with account number {account_number} found.")

    def find_client(self, account_number):
        for client in self.clients:
            if client.account_number == account_number:
                return client
        return None

    def total_balance(self):
        total = sum(client.balance for client in self.clients)
        return f"Total balance of all clients: {total}"

# bank = Bank()

# client1 = Client("John", "Doe", "123456789", 1000)
# client2 = Client("Alice", "Smith", "987654321", 2000)

# bank.add_client(client1)
# bank.add_client(client2)

# print(bank.total_balance())

# client3 = bank.find_client("123456789")
# if client3:
#     print(f"Found client: {client3.first_name} {client3.last_name}")
# else:
#     print("Client not found.")

# bank.remove_client("987654321")

# print(bank.total_balance())