class Animal:
    def __init__(self, name) -> None:
        self.name = name
class Cow(Animal):
    def sound(self):
        print (f"moo i am a: {self.__class__.__name__} my name is: {self.name}")
class Dog(Animal):
    def sound(self):
        print (f"warf warf i am a: {self.__class__.__name__} my name is: {self.name}")\
        
cw = Cow("Mucka")
dg = Dog("Burek")

cw.sound()
dg.sound()