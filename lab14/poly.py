class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Bird(Animal):
    def make_sound(self):
        return "Tweet"

def describe_animal(animal):
    print(animal.make_sound())

# Example usage
animals = [Dog(), Cat(), Bird()]

for animal in animals:
    describe_animal(animal)
