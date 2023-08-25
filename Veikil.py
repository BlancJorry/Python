
class Vehicule():

    def __init__(self, make, model, year:int, daily_rate:float):
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate

class Car(Vehicule):

    def __init__(self, make, model, year:int, daily_rate:float, num_seats:int):
        super().__init__(make, model, year, daily_rate)
        self.num_seats = num_seats

    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nDaily Rental Price: {self.daily_rate}\nNumber of Seats: {self.num_seats}")

class Motorcycle(Vehicule):

    def __init__(self, make, model, year:int, daily_rate:float, engine_type):
        super().__init__(make, model, year, daily_rate)
        self.engine_type = engine_type

    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nDaily Rental Price: {self.daily_rate}\nEngine Type: {self.engine_type}")

class Bicycle(Vehicule):

    def __init__(self, make, model, year:int, daily_rate:float, frame_type):
        super().__init__(make, model, year, daily_rate)
        self.frame_type = frame_type

    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nDaily Rental Price: {self.daily_rate}\nFrame Type: {self.frame_type}")

class Rental:
    
    def __init__(self, vehicle, rentals_day):
        self.vehicle = vehicle
        self.rentals_day = rentals_day
        self.prix_total = self.calculate_total_cost()
        
    def calculate_total_cost(self):
        return self.vehicle.daily_rate * self.rentals_day
         
    def display_receipt(self):
        print("--------------------------Resime_locasyon an---------------------------:")
        self.vehicle.display_info()
        print(f"kou total locasyon an : {self.prix_total}")



car = Car("Toyota", "Camry", 2023, 50, 5)
car.display_info()
rental_car = Rental(car, 3)
rental_car.display_receipt()

motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2023, 80, "V-twin")
motorcycle.display_info()
rental_motorcycle = Rental(motorcycle, 2)
rental_motorcycle.display_receipt()

bicycle = Bicycle("Trek", "FX", 2023, 15, "Hybrid")
bicycle.display_info()
rental_bicycle = Rental(bicycle, 1)
rental_bicycle.display_receipt()