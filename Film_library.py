class Films:
    def __init__(self, title, year, ganre):
          self.title = title
          self.year = year
          self.ganre = ganre
          
          self.play_number = 0



    def __str__(self):
         return f"{self.title} ({self.year})"
    
     
    def play(self, step=1):
         self.play_number +=step

    
class Serial(Films):
     def __init__(self, seria_number, season_number, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.seria_number = seria_number
          self.season_number = season_number
     def __str__(self):
          return f"{self.title} S{self.season_number:0>2d}E{self.seria_number:0>2d}"

collection = []

collection.append(Films(title="Matrix", year=2001, ganre="sci-fi"))
collection.append(Films(title="2001: A Space Odyssey", year=1968, ganre="sci-fi"))
collection.append(Films(title="The Godfather", year=1972, ganre="thriller"))
collection.append(Films(title="Citizen Kane", year=1941, ganre="drama"))
collection.append(Films(title="Raiders of the Lost Ark", year=1981, ganre="action"))
collection.append(Films(title="In the Mood for Love", year=2000, ganre="drama"))

collection.append(Serial(title="Wednesday", year=2022, ganre="sci-fi", seria_number=5, season_number=1))
collection.append(Serial(title="Breaking Bad", year=2008, ganre="drama", seria_number=70, season_number=5))
collection.append(Serial(title="The Sopranos", year=1999, ganre="thriller", seria_number=94, season_number=8))
collection.append(Serial(title="Game of Thrones", year=2011, ganre="fantasy", seria_number=56, season_number=8))

def get_movies(collection):
     film_list=[]
     for i in range(0, len(collection)):
          if isinstance(collection[i], Serial):
               pass
          else:
            film_list.append(collection[i])
          
     return film_list

def get_series(collection):
     film_list=[]
     for i in range(0, len(collection)):
          if isinstance(collection[i], Serial):
            film_list.append(collection[i])
         
     return film_list

def search(title, collection):
     for i in range(0, len(collection)):
        if title==collection[i].title:
             return collection[i]            

movie = sorted(get_movies(collection), key=lambda collection: collection.title)
series = sorted(get_series(collection), key=lambda collection: collection.title)

for i in range(0, len(movie)):
     print(movie[i])
print()
for i in range(0, len(series)):
     print(series[i])
print()

print(search("Matrix", collection))

