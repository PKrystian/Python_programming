class Cinema:
    def __init__(self, cinema_name) -> None:
        self.cinema_name = cinema_name
        self.movie_list = []
    
    def add_movie(self, movie_name):
        self.movie_list.append(movie_name)
        movie_name.add_cinema(self.cinema_name)

    def rem_movie(self, movie_name):
        self.movie_list.remove(movie_name)
        movie_name.rem_cinema(self.cinema_name)

    def show_all(self):
        for x in self.movie_list:
            print(x)


class Movie:
    def __init__(self, movie_name, year) -> None:
        self.movie_name = movie_name
        self.year = year
        self.cinema_name = None

    def add_cinema(self, cinema):
        self.cinema_name = cinema
        print (f"Movie: {self.movie_name} is added to {self.cinema_name}\n")

    def rem_cinema(self, cinema):
        self.cinema_name = None
        print (f"Movie: {self.movie_name} is removed from {cinema}\n")


    def __str__(self) -> str:
        return f"{self.movie_name} made in: {self.year} is played at {self.cinema_name}"

cin = Cinema("Multikino")
cin2 = Cinema("Helios")
mov1 = Movie("Hobbit", 2014)
mov2 = Movie("Manta", 2011)

cin.add_movie(mov1)
cin.add_movie(mov2)

cin.show_all()
cin.rem_movie(mov1)
cin.show_all()

cin2.add_movie(mov1)
cin2.add_movie(mov2)

cin2.rem_movie(mov1)

cin2.show_all()
cin.show_all()