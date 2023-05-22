class Student:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.school = None
        self.is_student = False

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def add_school(self, school_name):
        if (self.is_student == True):
            if (self.school != school_name):
                print(f"Student {self.first_name} {self.last_name} already attends to: {self.school} you can't add him to {school_name}")
        else:
            self.is_student = True
            self.school = school_name
            school_name.add_student(self)
    
    def rem_school(self):
        if self.is_student != None:
            self.is_student = None
            self.school.rem_student(self)
            self.school = None

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.students_list = []

    def __str__(self) -> str:
        return f"{self.name}"

    def add_student(self, student):
        if ((student not in self.students_list)):
            if((student.is_student == False) | (str(student.school) == str(self.name))):
                self.students_list.append(student)
                student.add_school(self)
            else: print(f"Student {student.first_name} {student.last_name} already attends to {student.school} you can't add him to {self.name}")

    def rem_student(self, student):
        if student in self.students_list:
            self.students_list.remove(student)
            student.rem_school()

    def get_student_list(self):
        return [str(student) for student in self.students_list]

sch1 = School("XYZ School")
sch2 = School("ABC School")

stud1 = Student("Jakub", "Nowak")
stud2 = Student("Maciej", "Keqwa")

sch1.add_student(stud1)
sch1.add_student(stud2)

sch2.add_student(stud1)
stud1.add_school(sch1)
stud1.add_school(sch2)

print(f"1: {sch1.get_student_list()}")

sch1.rem_student(stud1)
stud1.rem_school()

print(f"2: {sch1.get_student_list()}")