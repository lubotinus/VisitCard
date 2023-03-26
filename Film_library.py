import random
from datetime import datetime


class Films:
    def __init__(self, title, year, ganre):
        self.title = title
        self.year = year
        self.ganre = ganre

        self.play_number = 0

    def __str__(self):
        return f"{self.title} ({self.year})"

    def play(self, step=1):
        self.play_number += step


class Serial(Films):
    def __init__(self, seria_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.seria_number = seria_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.season_number:0>2d}E{self.seria_number:0>2d}"


def get_movies(collection):
    film_list = []

    for i in range(0, len(collection)):
        if isinstance(collection[i], Serial):
            pass
        else:
            film_list.append(collection[i])

    return film_list


def get_series(collection):
    film_list = []
    for i in range(0, len(collection)):
        if isinstance(collection[i], Serial):
            film_list.append(collection[i])

    return film_list


def search(title, collection):
    for i in range(0, len(collection)):
        if title == collection[i].title:
            return collection[i]


def generate_func(collection):
    for r in range(10):
        generate_views(collection)
    return collection

    # def gen():
    #      result = func()
    #      return result
    # out_view.append(gen)


def generate_views(collection):
    i = random.randint(0, (len(collection) - 1))
    n = random.randint(0, 100)
    collection[i].play(n)
    return collection


def top_titles(top, collection):
    sort_collection = sorted(
        collection, key=lambda collection: collection.play_number, reverse=True
    )
    out_put = []
    for i in range(top):
        out_put.append(sort_collection[i])
    return out_put


collection = []
view_now = []
top_view = []
work = ""

while work != "exits":
    work = input("Biblioteka filmów, co robimy: _")

    if work == "add":
        collection.append(Films(title="Matrix", year=2001, ganre="sci-fi"))
        collection.append(
            Films(title="2001: A Space Odyssey", year=1968, ganre="sci-fi")
        )
        collection.append(Films(title="The Godfather", year=1972, ganre="thriller"))
        collection.append(Films(title="Citizen Kane", year=1941, ganre="drama"))
        collection.append(
            Films(title="Raiders of the Lost Ark", year=1981, ganre="action")
        )
        collection.append(Films(title="In the Mood for Love", year=2000, ganre="drama"))

        collection.append(
            Serial(
                title="Wednesday",
                year=2022,
                ganre="sci-fi",
                seria_number=5,
                season_number=1,
            )
        )
        collection.append(
            Serial(
                title="Breaking Bad",
                year=2008,
                ganre="drama",
                seria_number=70,
                season_number=5,
            )
        )
        collection.append(
            Serial(
                title="The Sopranos",
                year=1999,
                ganre="thriller",
                seria_number=94,
                season_number=8,
            )
        )
        collection.append(
            Serial(
                title="Game of Thrones",
                year=2011,
                ganre="fantasy",
                seria_number=56,
                season_number=8,
            )
        )

        print("Films an Series added:")

        movie = sorted(get_movies(collection), key=lambda collection: collection.title)
        print("Movies added:")
        for i in range(len(movie)):
            print(movie[i])
        print()
        series = sorted(get_series(collection), key=lambda collection: collection.title)

        print("Series added:")
        for i in range(len(series)):
            print(series[i])
        print()

    if work == "generate view":
        view_now = generate_func(collection)
        print("Views generated")
        print()

    if work == "show top":
        top_view = top_titles(5, view_now)
        x = datetime.now()
        date = x.strftime("%d:%m:%Y")
        print(f"Najpopularniejsze filmy i seriale dnia {date}")
        print()
        for i in range(1, 4):
            print(f"{i}: {top_view[i]}, obejrzany: {top_view[i].play_number} razy")
