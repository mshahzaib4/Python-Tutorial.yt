class Animal:
    def make_sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def make_sound(self):
        print("Dog barks")


class Cat(Animal):
    def make_sound(self):
        print("Cat meows")


# Creating objects
animal = Animal()
dog = Dog()
cat = Cat()

animal.make_sound()  # Output: Animal makes a sound
dog.make_sound()     # Output: Dog barks
cat.make_sound()     # Output: Cat meows
