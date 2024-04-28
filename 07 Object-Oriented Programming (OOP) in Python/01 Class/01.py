class Car:
    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Method
    def drive(self):
        print(f"{self.brand} {self.model} is driving.")
        
# Creating instances of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Invoking the drive method for each car
car1.drive()  # Output: Toyota Camry is driving.
car2.drive()  # Output: Honda Civic is driving.
