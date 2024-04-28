# Base class
class Animal:
    def speak(self):
        pass

# Derived classes
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Function demonstrating polymorphism
def animal_sound(animal):
    return animal.speak()

# Usage
dog = Dog()
cat = Cat()
cow = Cow()

print(animal_sound(dog))  # Output: Woof!
print(animal_sound(cat))  # Output: Meow!
print(animal_sound(cow))  # Output: Moo!
