# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():
    #This class indicates a way to have movie information

    # Initialize instance of class Movie
    def __init__(self, movie_title, poster_image, trailer_youtube,
                 movie_review, audience_age):
        """
          Behavior:Create and define the Movie class. Each movie will be created by this class.

            Args:
                movie_title (str): The name of Movie.
                poster_image : The movie's poster or image
                trailer_youtube : the movie trailer or movie clip
                movie_review (str) : Audience's review
                audience_age (str) : Allowance age

        """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.review = movie_review
        self.age = audience_age