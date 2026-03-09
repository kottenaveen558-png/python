class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def show_vehicle(self):
        print("Brand",self.brand,"speed",self.speed)


class Car(Vehicle):
    def __init__(self,brand,speed,fuel_type):
        super().__init__(brand,speed)
        self.fuel_type  = fuel_type
        
    def show_car(self):
        print("Fuel type",fuel_type)

class ElectricCar(Car):
    def __init__(self,brand,speed,fuel_type,battery_capacity):
        super().__init__(brand,speed,fuel_type)
        self.battery_capacity = battery_capacity

    
    def show_details(self):
        print(f"Brand: {self.brand} \n speed :{self.speed} \n  fuel_type:{self.fuel_type} \n  Battery:{self.battery_capacity}")


obj = ElectricCar("Tesla",200,"petrol","4hrs")
obj.show_details()
