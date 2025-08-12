class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self): #instance Method
        return f"Car Brand:{self.year},\nCar Model:{self.make},\nYear:{self.model}"

car=Car("Toyota", "Corolla", 2020)
print(car.display_info())