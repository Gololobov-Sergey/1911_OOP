class Student:
    count_of_Student = 0

    def __init__(self, name=None, height=160, mental_ability=10.0):
        self.name = name
        self.height = height
        self.mental_ability = mental_ability
        Student.count_of_Student += 1
        print('Привіт, я з`явився')

    def study(self, mental_ability=0.5):
        self.mental_ability += mental_ability
        print('Я підвищів свій рівень знань')

    def grow(self, height=1):
        self.height += height

    def __str__(self):
        return f'Я {self.name}, мій зріст {self.height} см.\nМоя розумова здібність - {self.mental_ability}.'

    def __del__(self):
        print(f'Привіт, я {self.name}, і я пішов ((')


#serg = Student(height=180)
#print(serg)
#print(serg.name)
# print(serg.count_of_Student)

Artur = Student(name='Artur', height=165)
print(Artur)
#print(Artur.name)
Artur.grow(10)
Artur.study(2)
print(Artur)

# print(Artur.count_of_Student)
# print(Serg.count_of_Student)
# print(Student.count_of_Student)
