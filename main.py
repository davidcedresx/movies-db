from tabulate import tabulate
import json
import os

LOAD_SEED = True

seed = open("./seed.json").read()
seed = json.loads(seed)

# movies db indexed by movie name -- no hashing or ids
movies_db = {}

for movie in seed:
    if movie["Director"] == "N/A" or LOAD_SEED == False:
        continue

    movies_db[movie["Title"]] = {
        "title": movie["Title"],
        "director": movie["Director"],
        "genre": movie["Genre"].split(", "),
        "year": movie["Year"],
        "cast": movie["Actors"].split(", "),
    }


def clear():
    os.system("clear")


def print_movie(movie):
    print("Title: " + movie["title"])
    print("Director: " + movie["director"])
    print("Genre: " + ", ".join(movie["genre"]))
    print("Year: " + movie["year"])
    print("Cast: " + ", ".join(movie["cast"]))
    print("")


while True:
    table = []

    for movie in movies_db:
        table.append(
            [
                movies_db[movie]["title"],
                movies_db[movie]["director"],
                movies_db[movie]["genre"],
                movies_db[movie]["year"],
                movies_db[movie]["cast"],
            ]
        )

    clear()

    print("MOVIES")
    print(tabulate(table))

    print("")
    print("COMMANDS")
    print("ad: Agregar peliculas")
    print("st: Buscar películas por título")
    print("sg: Buscar películas por género")
    print("my: Mostrar películas por año")
    print("ma: Mostrar actores más populares")
    print("")

    key = input()

    valid = ["ad", "st", "sg", "my", "ma"].count(key) > 0

    if valid:
        clear()

    if key == "ad":
        title = input("Título: ")
        director = input("Director: ")
        genre = input("Géneros (separados por comas): ")
        year = input("Año: ")
        cast = input("Actores (separados por comas): ")

        movies_db[title] = {
            "title": title,
            "director": director,
            "genre": genre.split(", "),
            "year": year,
            "cast": cast.split(", "),
        }

    elif key == "st":
        title = input("Título: ")

        if movies_db.get(title) is None:
            print("Película no encontrada")

        else:
            print_movie(movies_db[title])

    elif key == "sg":
        genre = input("Género: ")

        for movie in movies_db:
            if genre in movies_db[movie]["genre"]:
                print_movie(movies_db[movie])

    elif key == "my":
        movies_by_year = sorted(movies_db.values(), key=lambda x: x["year"])

        for movie in movies_by_year:
            print_movie(movie)

    elif key == "ma":
        actors = {}

        for movie in movies_db:
            for actor in movies_db[movie]["cast"]:
                if actors.get(actor) is None:
                    actors[actor] = 1
                else:
                    actors[actor] += 1

        actors = sorted(actors.items(), key=lambda x: x[1], reverse=True)

        # mostrando los 5 actores mas populares
        for actor in actors[:5]:
            print(actor)

    if valid:
        input()
