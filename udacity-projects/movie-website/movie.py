import webbrowser


class Movie():
    def __init__(self, movie_title, poster_image, trailer_youtube):
        """Initializes the movie object
        Args:
            movie_title (str): title of the movie
            poster_image(str): the url to the movies poster image
            trailer_youtube(str): the url to the trailer on youtube
        """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
