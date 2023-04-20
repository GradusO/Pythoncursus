class Car:
    def __init__(self):
        self.kilometers = 0

    def drive(self, distance):
        self.kilometers += distance
        print(f"Driving: {distance}")

    def __str__(self):
        return f"This car has driven {self.kilometers} kilometers"

if __name__=="__main__":
    car = Car()
    car.drive(10)
    car.drive(350)
    print(car)