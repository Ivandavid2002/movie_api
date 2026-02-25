class MovieDTO:

    def __init__(self, title, year, genre, director):

        self.title = title
        self.year = year
        self.genre = genre
        self.director = director


    def to_dict(self):

        return {
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "director": self.director
        }