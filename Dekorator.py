
from timeit import default_timer as timer

def say_louder(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@say_louder
def say_hello():
    greeting = "Hello stranger!"
    return greeting

#say_hello = say_louder(say_hello)
print(say_hello())

from faker import Faker
class BaseContact:
     def __init__(self, name, telefon, email):
          self.name=name
          self.telefon=telefon
          self.email=email
     def __str__(self):
          return f"{self.name} {self.telefon} {self.email}"     
     
     def contact(self):
          return f"Wybieram numer {self.telefon} i dzwonię do {self.name}"
     
     def length(self):
          
          return f"Długość imieni oraz nazwiska: {len(self.name)}"
     
def time_measure(func):
     start = timer()
     func
     end = timer()
     print(end-start)

@time_measure
def create_contacts():
     faker=Faker()
     output=[]
     for i in range(0, 100):
            output.append(BaseContact(name = faker.name(), telefon=faker.phone_number(), email=faker.email()))
     return output





