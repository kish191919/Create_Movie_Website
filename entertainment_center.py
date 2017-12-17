# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes


# Four instances of Movies
The_Matrix = media.Movie(
    "The Matrix",
    "http://cdn.it.chosun.com/data/photos/cdn/20170316/2832075_11024317608900.jpg",
    "https://youtu.be/m8e-FF8MsqU",
    "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
    "AGE : 15+")

The_Lord_of_the_Rings = media.Movie(
    "The Lord of the Rings",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_SY999_CR0,0,673,999_AL_.jpg",
    "https://youtu.be/V75dMMIW2B4",
    "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle Earth from the Dark Lord Sauron.",
    "Age : 12+")

Notting_Hill = media.Movie(
    "Notting Hill",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTE5OTkwYzYtNDhlNC00MzljLTk1YTktY2IxZjliZmNjMjUzL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,671,1000_AL_.jpg",
    "https://youtu.be/4RI0QvaGoiI",
    "The life of a simple bookshop owner changes when he meets the most famous film star in the world.",
    "AGE : 15+")

The_Notebook = media.Movie(
    "The Notebook",
    "http://twirlit.com/wp-content/uploads/2013/02/the-notebook-honest-trailer.jpg",
    "https://youtu.be/FC6biTjEyZw",
    "The Notebook is a 2004 American romantic drama film directed by Nick Cassavetes and based on the novel of the same name by Nicholas Sparks.",
    "AGE : 15+")

movies = [The_Matrix, The_Lord_of_the_Rings, Notting_Hill, The_Notebook]

# Open the movie website
fresh_tomatoes.open_movies_page(movies)