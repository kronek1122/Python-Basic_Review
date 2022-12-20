

class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):

        self.sound = sound

        return f'{self.name} says {self.sound}'


class Car():

    def __init__(self, color, km):

        self.color = color
        self.km = km

    def __str__(self):
        return f"The {self.color} car has {self.km} km"

    def drive(self, how_many):
        self.km = self.km + how_many

blue = Car("blue", 20000)
red = Car("red", 30000)
zero = Car('white',0)
print(zero)
zero.drive(100)
print(zero)
print(red)
print(blue)
""""
philo = Dog("Philo", 5, "brown")

print(f"{philo.name}'s coat is {philo.coat_color}.")
"""
