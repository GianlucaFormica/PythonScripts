import media
import fresh_tomatoes

hunger = media.Movie("Hunger Games",
                        "Hunger Games",
                        r"https://en.wikipedia.org/wiki/The_Hunger_Games_(film)#/media/File:HungerGamesPoster.jpg",
                        r"https://youtu.be/mfmrPu43DF8")
#print(toy_story.storyline)

furious = media.Movie("Furious 7",
                    "A movie about a marine",
                     r"..\Furious7.jpg",
                     r"https://youtu.be/Skpu5HaVkOc")
#print(avatar.storyline)

jackblack = media.Movie("Jack Black",
                        "best song in the world",
                        r"..\rock.jpg",
                        r"https://youtu.be/2Jvgbe9Kx0U")

toy_story = media.Movie("Toy Story",
                        "A story about toy",
                        r"https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        r"https://youtu.be/CI5eQm-0CUw")
#print(toy_story.storyline)

jurrasic = media.Movie("Jurrasic World",
                    "A movie about a marine",
                     r"https://en.wikipedia.org/wiki/Jurassic_World#/media/File:Jurassic_World_poster.jpg",
                     r"https://youtu.be/RFinNxS5KN4")
#print(avatar.storyline)

ultron= media.Movie("Age of Ultron Trailer 2",
                     " Age of Ultron Trailer 2",
                     r"http://www.google.co.uk/imgres?imgurl=http://t0.gstatic.com/images%3Fq%3Dtbn:ANd9GcRlGeugacRkKznDOtRhUCVt0AkrOTPbaaKwF9xgGZgNViyC_Xko&imgrefurl=http://google.com/search?tbm%3Disch%26q%3DAvengers:%2BAge%2Bof%2BUltron&h=1080&w=720&tbnid=uKmEUyEFBWkZlM:&zoom=1&tbnh=186&tbnw=124&usg=__JDyVwtOjELwiG5OHA_jlffzqC7E=&docid=thKGTUdidK0CkM&itg=1",
                     r"https://youtu.be/MZoO8QVMxkk")

#print(jackblack.storyline)
#avatar.show_trailer()
movies = [hunger, ultron,jurrasic ,furious,toy_story,jackblack]
fresh_tomatoes.open_movies_page(movies)

                     
