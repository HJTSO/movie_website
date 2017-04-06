class Movie():
 """Description of Movie: Build a movie which included title,storyline and other information"""

 def __init__(self,movie_title,movie_storyline,poster_image,
                 trailer_youtube):
  """Method description
        Args:
            self => string, argument self
            movie_title => string, title
            movie_storyline => string, storyline
            poster_image => string, poster_image_url
            trailer_youtube => string, trailer_youtube_url
        Return:
             None
  """
  self.title = movie_title
  self.storyline = movie_storyline
  self.poster_image_url = poster_image
  self.trailer_youtube_url = trailer_youtube