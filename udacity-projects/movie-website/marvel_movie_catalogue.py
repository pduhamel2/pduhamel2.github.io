import movie
import marvel_movie_webpage

'''Instanciate an object of class Movie for each movie to be on the web page'''
iron_man = movie.Movie("Iron Man",
                       "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",  # noqa
                       "https://youtu.be/8hYlB38asDY")

the_incredible_hulk = movie.Movie("The Incredible Hulk",
                                  "https://upload.wikimedia.org/wikipedia/en/8/88/The_Incredible_Hulk_poster.jpg",  # noqa
                                  "https://youtu.be/xbqNb2PFKKA")

iron_man2 = movie.Movie("Iron Man 2",
                        "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",  # noqa
                        "https://youtu.be/BoohRoVA9WQ")

thor = movie.Movie("Thor",
                   "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",  # noqa
                   "https://www.youtube.com/watch?v=JOddp-nlNvQ")

captain_america_tfa = movie.Movie("Captain America",
                                  "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",  # noqa
                                  "https://youtu.be/JerVrbLldXw")

the_avengers = movie.Movie("The Avengers",
                           "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",  # noqa
                           "https://youtu.be/eOrNdBpGMv8")

iron_man3 = movie.Movie("Iron Man 3",
                        "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",  # noqa
                        "https://youtu.be/oYSD2VQagc4")

thor_tdw = movie.Movie("Thor 2",
                       "https://upload.wikimedia.org/wikipedia/en/7/7e/Thor_-_The_Dark_World_poster.jpg",  # noqa
                       "https://youtu.be/npvJ9FTgZbM")

captain_america_tws = movie.Movie("Captain America 2",
                                  "https://upload.wikimedia.org/wikipedia/en/e/e8/Captain_America_The_Winter_Soldier.jpg",  # noqa
                                  "https://youtu.be/tbayiPxkUMM")

guardians_of_the_galaxy = movie.Movie("Guardians of the Galaxy",
                                      "https://upload.wikimedia.org/wikipedia/en/b/b5/Guardians_of_the_Galaxy_poster.jpg",  # noqa
                                      "https://youtu.be/d96cjJhvlMA")

the_avengers_aou = movie.Movie("The Avengers 2",
                               "https://upload.wikimedia.org/wikipedia/en/f/ff/Avengers_Age_of_Ultron_poster.jpg",  # noqa
                               "https://youtu.be/tmeOjFno6Do")

ant_man = movie.Movie("Ant Man",
                      "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg",  # noqa
                      "https://youtu.be/pWdKf3MneyI")

captain_america_cw = movie.Movie("Captain America 3",
                                 "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",  # noqa
                                 "https://youtu.be/dKrVegVI0Us")

doctor_strange = movie.Movie("Doctor Strange",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",  # noqa
                             "https://youtu.be/HSzx-zryEgM")

guardians_of_the_galaxy_vol2 = movie.Movie("Guardians of the Galaxy 2",
                                           "https://upload.wikimedia.org/wikipedia/en/a/ab/Guardians_of_the_Galaxy_Vol_2_poster.jpg",  # noqa
                                           "https://youtu.be/dW1BIid8Osg")

spider_man_hc = movie.Movie("Spider-Man",
                            "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",  # noqa
                            "https://youtu.be/39udgGPyYMg")

thor_ragnarok = movie.Movie("Thor 3",
                            "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",  # noqa
                            "https://youtu.be/ue80QwXMRHg")

black_panther = movie.Movie("Black Panther",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",  # noqa
                            "https://youtu.be/xjDjIWPwcPU")

'''Create a list that contains all the movie objects created'''
movies = [iron_man, the_incredible_hulk, iron_man2, thor, captain_america_tfa,
          the_avengers, iron_man3, thor_tdw, captain_america_tws,
          guardians_of_the_galaxy, the_avengers_aou, ant_man,
          captain_america_cw, doctor_strange, guardians_of_the_galaxy_vol2,
          spider_man_hc, thor_ragnarok, black_panther]

'''Pass the list of movie objects to the open_movies_page() function'''
marvel_movie_webpage.open_movies_page(movies)
