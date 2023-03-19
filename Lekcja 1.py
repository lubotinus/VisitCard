
class Car:
    def __init__(self, make, model_name, top_speed, color):
          self.make = make
          self.model_name = model_name
          self.top_speed = top_speed
          self.color = color

          self._current_speed = 0
    def __str__(self):
         return f'{self.color} {self.make} {self.model_name}'
    
    def __repr__(self):
         return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"
    
    def __eq__(self, other):
         return (
              
              self.make == other.make and
              self.model_name == other.model_name and
              self.top_speed == other.top_speed and
              self.color == other.color
           )
    def __gt__(self, other):
         return self.top_speed > other.top_speed
    
    def accelerate(self, step=10):
         self.current_speed +=step
    def decelerate(self, step=10):
         self.current_speed -= step

    @property
    def current_speed(self):
         return self._current_speed
    
    @current_speed.setter
    def current_speed(self, value):
         if value <=self.top_speed:
              self._current_speed=value
         else:
              raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")

mustang = Car(make="Ford", model_name="Mustang", color="Yellow", top_speed=250)
car=Car(make="Ford", model_name="Mustang", top_speed=250, color="Yellow")


#print(mustang.make)


print(dir(Car))
print(mustang)
print(car)

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Mustang", top_speed=350, color="Red")
car_three = Car(make="Ford", model_name="Mustang", top_speed=250, color="Yello")
print(car_one < car_two)

print(car_one == car_three)

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Fiesta", top_speed=200, color="Blue")
car_three = Car(make="Porsche", model_name="911", top_speed=320, color="Black")
cars = [car_one, car_two, car_three]
by_speed = sorted(cars, key=lambda car:car.top_speed)
by_make= sorted(cars, key=lambda car: car.make)
print(by_speed)
print(by_make)

print()
print(car.current_speed)
print()
car.accelerate()
print(car.current_speed)
print()
car.accelerate(50)
print(car.current_speed)
print()
#print(car.current_speed)
car.current_speed=100
print()

class Truck(Car):
     def __init__(self, max_load, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.max_load = max_load

truck = Truck(make="Mercedes", model_name="Actos", color="Black", top_speed=90, max_load=1200)
print(truck)

print(truck.current_speed)
truck.accelerate()
print(truck.current_speed)
print()
print(isinstance(car, Truck))
print(isinstance(car, Car))
print(isinstance(truck, Car))
print()
print(issubclass(Truck, Car))
print(issubclass(Car, Truck))