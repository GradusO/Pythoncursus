class Car:
    def __init__(self, kilometers = 0):
        self.kilometers = kilometers
        self.last_maintenance = kilometers

    def drive(self, distance):
        self.kilometers += distance
        print(f"Driving: {distance}")
        if self.kilometers - self.last_maintenance > 30000:
            print("Your car needs maintenance!! ")

    def repair(self):
        print("Your car is being repaired")
        self.last_maintenance = self.kilometers

    def __str__(self):
        return f"This car has driven {self.kilometers} kilometers"

if __name__=="__main__":
    car = Car()
    car.drive(10)
    car.drive(350)
    car.drive(35000)
    car.repair()
    car.drive(100)
    car.drive(1000)
    print(car)
    car.drive(1)
    print(car)
