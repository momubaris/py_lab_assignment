class Car:
    number_of_cars=0
    def __init__(self,model,color,price):
        self.model=model
        self.color=color
        self.price=price
        Car.number_of_cars=Car.number_of_cars+1
    def start(self):
        print("Starting the car...")
    def stop(self):
        print("Stopping the car...")
    def accelerate(self):
        print("Accelerating the car...")
    @staticmethod
    def get_number_of_cars():
        return Car.number_of_cars
car = Car("Honda","Red",20000)
car.start()
car.stop()
car.accelerate()
print(Car.get_number_of_cars())
