class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car = Car("Toyota", "Corolla")
# print(car.brand)
# print(car.model)

class Cat:
    def __init__(self, name):
        self.name = name

kitty = Cat("Mruczek")
# print(kitty.name)

class Figure:
    def calculate_area(self):
        pass
    def calculate_volume(self):
        pass

class Square(Figure):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2
    
    def calculate_volume(self):
        return self.side ** 3  

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2
    
    def calculate_volume(self):
        return (4/3) * 3.14 * self.radius ** 3


sq = Square(5)
print("Volume of Square", sq.calculate_volume())
cr = Circle(5)
print("Volume of circle", cr.calculate_volume())