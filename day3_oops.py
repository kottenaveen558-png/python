class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_info(self):
        print(f"Brand: {self.brand}, Speed: {self.speed}")

class Car(Vehicle):
    def __init__(self, brand, speed, num_doors):
        super().__init__(brand, speed)
        self.num_doors = num_doors

    def drive(self):
        print(f"Car is driving with {self.num_doors} doors")

class Bike(Vehicle):
    def __init__(self, brand, speed, has_sidecar):
        super().__init__(brand, speed)
        self.has_sidecar = has_sidecar

    def ride(self):
        print(f"Bike is riding, has sidecar: {self.has_sidecar}")

class Truck(Vehicle):
    def __init__(self, brand, speed, cargo_capacity):
        super().__init__(brand, speed)
        self.cargo_capacity = cargo_capacity

    def haul(self):
        print(f"Truck is hauling {self.cargo_capacity}kg cargo")

c = Car("Toyota", 180, 4)
b = Bike("Yamaha", 120, True)
t = Truck("Volvo", 90, 5000)

c.show_info()
c.drive()
b.show_info()
b.ride()
t.show_info()
t.haul()

print(Car.__mro__)
print(Bike.__mro__)
print(Truck.__mro__)
