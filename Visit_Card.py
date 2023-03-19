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
     

class BusinessContact(BaseContact):
     def __init__(self, job, company, job_telefon, *args, **kwargs):
          super().__init__( *args, **kwargs)
          self.job=job
          self.company=company
          self.job_telefon=job_telefon
      
     def contact(self):
          return f"Wybieram numer {self.job_telefon} i dzwonię do {self.name}"  
     def __str__(self):
          return f"{self.name} {self.telefon} {self.email} {self.job} {self.company} {self.job_telefon}" 

               
def create_contacts(type, quant):
     faker=Faker()
     output=[]
     if type=='regular':
          for i in range(0, quant):
            output.append(BaseContact(name = faker.name(), telefon=faker.phone_number(), email=faker.email()))
     if type=='business':
          for i in range(0, quant):
            output.append(BusinessContact(name = faker.name(), telefon=faker.phone_number(), email=faker.email(), job=faker.job(), company=faker.company(), job_telefon=faker.phone_number()))
     return output

contact=create_contacts('business', 5)

for i in range(0, len(contact)):
     print(contact[i])

print()
print(contact[1].contact())
print()
print(contact[2].length())