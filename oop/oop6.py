class Automobile:
    def __init__(self, number, mark, capacity) -> None:
        self.number = number
        self.mark = mark
        self.capacity = capacity

    def show_info(self):
        return f"I am an {self.__class__.__name__} my number is {self.number} and {self.mark} made me"
    
    def calculate_distance(self):
        return self.capacity / 30
    
class Car(Automobile):
    def show_info(self):
        return f"I am an {self.__class__.__name__} my number is {self.number} and {self.mark} made me"
    
    def calculate_distance(self):
        return self.capacity / 15
    
class Bus(Automobile):
    def show_info(self):
        return f"I am an {self.__class__.__name__} my number is {self.number} and {self.mark} made me"
    
    def calculate_distance(self):
        return self.capacity / 50


thing = Automobile(123, "Gertq", 100)
thing2 = Car(111, "Toyota", 100)
thing3 = Bus(3456, "Sant", 100)

print(thing2.show_info())
print(thing2.calculate_distance())
print(thing3.calculate_distance())