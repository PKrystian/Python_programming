class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2
    
    def calculate_cir(self):
        return 2 * 3.14 * self.radius
    
# c = Circle(5)
# print("Area of circle is: ", c.calculate_area())
# print("Circumference of circle is: ", c.calculate_cir())

class Employee:
    def __init__(self, name, surname, job, salary):
        self.name = name
        self.surname = surname
        self.job = job
        self.salary = salary

    def change_salary(self, new_salary):
        self.salary = new_salary
    
    def show_info(self):
        print(f"Employee: {self.name} {self.surname} is working at: {self.job} and his salary is: {self.salary}")

# e = Employee("Jakub","Nowak","HR", 4500)
# e.show_info()
# e.change_salary(1000)
# e.show_info()

class Bank_Account:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, deposit_value):
        self.balance += deposit_value
        print(f"Salary for {self.acc_num} is now {self.balance}")

    def withdraw(self, withdraw_value):
        if self.balance >= withdraw_value:
            self.balance -= withdraw_value
            print(f"Balance for account {self.acc_num} is now {self.balance}")
        else:
            print("Insufficient funds")
        

# b = Bank_Account(123, 1000)
# b.deposit(1000)
# b.withdraw(1500)

class Car:
    def __init__(self, mark, model, year_of_production, max_speed) -> None:
        if mark and model and year_of_production and max_speed:
            self.mark = mark
            self.model = model
            self.year_of_production = year_of_production
            self.max_speed = max_speed
        else:
            print("Error, wrong input")

    def increase_max_speed(self, ims):
        self.max_speed += ims
        print(f"Max speed is now: {self.max_speed}")

    def decrease_max_speed(self, dms):
        if self.max_speed > dms:
            self.max_speed -= dms
            print(f"Max speed is now: {self.max_speed}")
        else:
            print("Speed can't be under 0")

    def show_car_info(self):
        print(f"The car {self.mark} {self.model} made in {self.year_of_production} have {self.max_speed} km/h max speed")

# cc = Car("Toyota", "Gnu", 1999, 200)
# cc.show_car_info()
# cc.increase_max_speed(30)
# cc.decrease_max_speed(100)

class Animal:
    def __init__(self, name, species) -> None:
        if name and species:
            self.name = name
            self.species = species
        else:
            print("Error, wrong input")
    
    def give_sound(self):
        match self.species:
            case "Dog":
                return f"Woof woof, My name is {self.name} and I am a {self.species}"
            case "Cat":
                return f"Miau miau, My name is {self.name} and I am a {self.species}"
            case "Cow":
                return f"Moo moo, My name is {self.name} and I am a {self.species}"
            case _:
                return f"My name is {self.name} and I am a {self.species}"
            
# ani1 = Animal("Borek", "Dog")
# ani2 = Animal("Mirek", "Cat")
# ani3 = Animal("Muczka", "Cow")
# print(ani1.give_sound())
# print(ani2.give_sound())
# print(ani3.give_sound())

class Animal:
    def __init__(self, name, species):
        if name and species:
            self.name = name
            self.species = species
        else:
            print("Error, wrong input")

    def give_sound(self):
        raise NotImplementedError("Subclass must implement the 'give_sound' method")


class Dog(Animal):
    def give_sound(self):
        return f"Woof woof, My name is {self.name} and I am a {self.species}"


class Cat(Animal):
    def give_sound(self):
        return f"Miau miau, My name is {self.name} and I am a {self.species}"


class Cow(Animal):
    def give_sound(self):
        return f"Moo moo, My name is {self.name} and I am a {self.species}"


class UnknownAnimal(Animal):
    def give_sound(self):
        return f"My name is {self.name} and I am a {self.species}"


# ani1 = Dog("Borek", "Dog")
# ani2 = Cat("Mirek", "Cat")
# ani3 = Cow("Muczka", "Cow")
# ani4 = UnknownAnimal("John", "Elephant")

# print(ani1.give_sound())
# print(ani2.give_sound())
# print(ani3.give_sound())
# print(ani4.give_sound())