

class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):

        self.sound = sound

        return f'{self.name} says {self.sound}'

class JackRussellTerrier(Dog):

    def speak(self, sound="Arf"):
        self.sound = sound
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

class GoldenRetriever(Dog):

    def speak(self, sound="Bark"):
        self.sound = sound
        return f"{self.name} says {self.sound}"

jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
buddy = Dachshund("Buddy", 9)
miles = JackRussellTerrier("Miles", 4)
rick = GoldenRetriever("Rick", 1)

a = miles.speak()
b = rick.speak()
print(a)
print(b)


class Rectangle():

    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Square(Rectangle):

    def __init__(self, side_length):
        self.length = side_length
        self.width = side_length

area = Square(4)

print(area.area())