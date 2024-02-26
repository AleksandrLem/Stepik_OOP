# 1. Реализуйте класс MovieGenres, описывающий флаг с жанрами кино.
# Флаг должен иметь пять элементов:

# ACTION
# COMEDY
# DRAMA
# FANTASY
# HORROR

# 2. Также реализуйте класс Movie, описывающий фильм.
# При создании экземпляра класс должен принимать два аргумента в следующем порядке:

# name — название фильма
# genres — жанр фильма (элемент флага MovieGenres)
# Класс Movie должен иметь один метод экземпляра:

# in_genre() — метод, принимающий в качестве аргумента жанр
# и возвращающий True, если фильм принадлежит данному жанру, или False в противном случае
# Экземпляр класса Movie должен иметь следующее неформальное строковое представление:

# <название фильма>


from enum import Flag, auto


class MovieGenres(Flag):

    ACTION = auto()
    COMEDY = auto()
    DRAMA = auto()
    FANTASY = auto()
    HORROR = auto()


class Movie:

    def __init__(self, name, genres=MovieGenres) -> None:
        self.name = name
        self.genres = genres

    def __str__(self) -> str:
        return self.name

    def in_genre(self, ganr):
        if ganr not in self.genres:
            return False
        return True


movie = Movie('Любовь и голуби', MovieGenres.DRAMA | MovieGenres.COMEDY)

print(movie.in_genre(MovieGenres.DRAMA))
print(movie.in_genre(MovieGenres.ACTION))
print(movie.in_genre(MovieGenres.DRAMA | MovieGenres.COMEDY))
print(movie)
