from Video import Video


class Movie(Video):
    def __init__(self, title, bio, posterURL, trailerURL):
        Video.__init__(self, title, bio)
        self.posterURL = posterURL
        self.trailerURL = trailerURL
