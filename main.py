movies = [
    {
        'name': 'The Matrix',
        'director': 'Wachowskis',
        'year': '1994'
    },
    {
        'name': 'The Inception',
        'director': 'Pritam',
        'year': '2010'
    },
    {
        'name': 'The Matrix Reloaded',
        'director': 'Shrestha',
        'year': '1998'
    }
]


def add_movie():
    name = input("Enter name of a movie: ")
    director = input("Enter name of director who directed the movie: ")
    year = input("Enter release date: ")
    movie = {
        'name': name,
        'director': director,
        'year': year
    }
    movies.append(movie)


def show_movies():
    for movie in movies:
        print("Name: ", movie["name"])
        print("Director: ", movie["director"])
        print("Year: ", movie['year'])
        print('\n')


def find_movie():
    attribute = input("Enter year or name of director to find the movie you are looking for: ")
    for movie in movies:
        if movie['year'] == attribute or movie['director'] == attribute:
            print(movie)


show_movies()
add_movie()
show_movies()
find_movie()