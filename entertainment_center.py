#import media
import os
import webbrowser
import time

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

toy_story = media.Movie("Toy Story",
                        "A story about toy",
                        r"https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        r"https://youtu.be/CI5eQm-0CUw")
print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A movie about a marine",
                     r"https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     r"https://youtu.be/teyhlo_cDGo")
print(avatar.storyline)                   
toy_story.show_trailer()                 
                     
