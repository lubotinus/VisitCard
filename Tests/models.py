import json
import csv

class Tests:
    def __init__(self):
        try:
            with open("tests.json", "r", newline='') as f:
             self.tests = json.load(f)
        except FileNotFoundError:
            self.tests = []
    
    def all(self):
        return self.tests
    
    def get(self, id):
        return self.tests[id]
    
    def create(self, data):
        data.pop('csrf_token')
        self.tests.append(data)

    def save_all(self):
       with open("tests.json", "w") as f:
           json.dump(self.tests, f)
      

    def update(self, id, data):
        data.pop('csrf_token')
        self.tests[id]=data
        self.save_all()

tests = Tests()