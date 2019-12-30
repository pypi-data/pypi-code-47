class MovieNotFound(Exception):
    def __init__(self, movie_id):
        self.movie_id = movie_id

    def __str__(self):
        return '"%s" not found' % self.movie_id
