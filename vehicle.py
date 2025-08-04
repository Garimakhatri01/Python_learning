class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, door):
        super().__init__(brand, model)
        self.door = door

    def display(self):
        print(f"Brand: {self.brand},Model: {self.model},Door: {self.door}")

class Cycle(Vehicle):
    def __init__(self,brand, model,cc):
        super().__init__(brand, model)
        self.cc = cc

    def display(self):
        print(f"Brand: {self.brand},Model: {self.model},CC: {self.cc}")

car1 = Car("Honda", "Ranger", 21)        
car1.display()

cycle1 = Cycle("Hero","Civic", 4)
cycle1.display()

        