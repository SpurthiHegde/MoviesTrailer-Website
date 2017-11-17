class Movie():
    """
    Movie Class helps create instances of Movie. We define the Movie title,poster 
    picture, yourtube trailer url, storyline and names of the director, writer & 
    the cast in this Class.
    """
    RATINGS = [1,2,3,4,5]
    def __init__(self, title, poster, youtube_url, storyline, director, writer, cast, rating):
        self.title = title
        self.poster = poster
        self.youtube_url = youtube_url
        self.storyline = storyline
        self.director = director
        self.writer = writer
        self.cast = cast
        self.rating = rating
