class Student:
    def __init__(self, name, surname, avg_grade) -> None:
        self.name = name
        self.surname = surname
        self.avg_grade = avg_grade
    def show_info(self):
        return f"Student {self.name} {self.surname} has {self.avg_grade} AVG grade"
    
st1 = Student("Jakub", "Nowak", 3.20)
st2 = Student("Maciej", "Kowal", 5.50)
st3 = Student("Jerzy", "Polak", 2.40)

print(st1.show_info())
print(st2.show_info())
print(st3.show_info())