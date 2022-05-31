class Person:

    def __init__(self, name, lastname, age, gender):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.gender = gender
        if self.gender == 'w':
            print(f'{self.name.title()} is a woman, and she can have a child')

    def walk(self):
        if 10 < self.age <= 30:
            print(f'{self.name.title()} in one hour can walk 5 km')
        elif 30 < self.age < 50:
            print(f'{self.name.title()} in one hour can walk 3 km')
        else:
            print(f'{self.name.title()} in one hour can walk 1 km')

    def voice(self):
        if self.gender == 'w':
            print(f'{self.name.title()} have a soft voice')
        else:
            print(f'{self.name.title()} have a tough voice')


p1 = Person('shushan', 'sargsyan', 29, 'w')
p2 = Person('mukuch', 'shmavonyan', 55, 'm')
p1.walk()
p2.voice()
p1.voice()
print(p1.gender)
p2.walk()