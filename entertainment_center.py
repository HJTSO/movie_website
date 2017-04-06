import media
import fresh_tomatoes
TOTAL =  6 #TOTAL:The total of movies

kill_bill = media.Movie("Kill Bill",
                        "The story of a woman's revenge",
                        "http://i1.piimg.com/1949/5ee3f55ea72054a3.jpg",
                        #"https://en.wikipedia.org/wiki/Kill_Bill:_Volume_1#/media/File:Kill_bill_vol_one_ver.jpg",
                        "https://www.youtube.com/watch?v=ot6C1ZKyiME")

twelve_angry_men = media.Movie("12 Angry Men",
                        "A jury made up of 12 men as they deliberate the guilt or acquittal of a defendant.",
                        "http://i4.buimg.com/1949/badd92466e320acd.jpg",
                        #"https://en.wikipedia.org/wiki/12_Angry_Men_(1957_film)#/media/File:12_angry_men.jpg",
                        "https://www.youtube.com/watch?v=G8EEimdMsFg")

crouching_tiger_hidden_dragon = media.Movie("Crouching Tiger, Hidden Dragon",
                        "A young warrior steals a sword from a famed swordsman and then escapes into a world of\n"
                        " romantic adventure.",
                        "http://i4.buimg.com/1949/15ea8ff36ce6b7a7.jpg",
                        #"https://www.google.co.jp/search?q=Crouching+Tiger,+Hidden+Dragon&tbm=isch&source=lnms&sa\n
                            # =X&ved=0ahUKEwiXmK_7_Y7TAhULl1QKHefPDfoQ_AUIBigB&biw=1296&bih=754#imgrc=N-4WwjzEC14XtM:",
                        "https://www.youtube.com/watch?v=4xPC1lEJ6Mg")

perfect_strangers = media.Movie("Perfect Strangers",
                        "Seven long-time friends play a game that put each one's phone and reveal every message or\n"
                        " phone call received.",
                        "http://i4.buimg.com/1949/f0df5fb3a9662fd5.jpg",
                        #"https://en.wikipedia.org/wiki/Perfect_Strangers_(2016_film)#/media/File:Perfetti\n
                                # -Sconosciuti-Poster-Locandina-2016.jpg",
                        "https://www.youtube.com/watch?v=kqX0-xn8j1g")

the_last_samurai = media.Movie("The Last Samurai",
                        "An American military advisor embraces the Samurai culture he was hired to destroy after\n"
                        " he is captured.",
                        "http://i4.buimg.com/1949/59648ac48e5ed61a.jpg",
                        #"https://en.wikipedia.org/wiki/The_Last_Samurai#/media/File:The_Last_Samurai.jpg",
                        "https://www.youtube.com/watch?v=T50_qHEOahQ")

ring = media.Movie("Ring",
                        "Reiko Asakawa is researching into a 'Cursed Video' interviewing teenagers about it.",
                        "http://i4.buimg.com/1949/bf084de0ce534c92.jpg",
                        #"https://en.wikipedia.org/wiki/Ring_(film)#/media/File:Ringu_(1998)_Japanese\n
                        # _theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=WcgCM2FyU8s")

#print(toy_story.storyline)
#movies = [kill_bill,twelve_angry_men,crouching_tiger_hidden_dragon,perfect_strangers,the_last_samurai,ring]

#movie_title
movies_names = ["Kill Bill",
                "12 Angry Men",
                "Crouching Tiger",
                "Hidden Dragon",
                "Perfect Strangers",
                "The Last Samurai",
                "Ring"]

#movie_storyline
storyline = ["The story of a woman's revenge",
             "A jury made up of 12 men as they deliberate the guilt or acquittal of a defendant.",
             "A young warrior steals a sword from a famed swordsman and then escapes into a world of\n"
             " romantic adventure.",
             "Seven long-time friends play a game that put each one's phone and reveal every message or\n"
             " phone call received.",
             "An American military advisor embraces the Samurai culture he was hired to destroy after\n"
             " he is captured.",
             "Reiko Asakawa is researching into a 'Cursed Video' interviewing teenagers about it.",
             "http://i4.buimg.com/1949/bf084de0ce534c92.jpg",
             ]

#poster_image
pics = ['http://i1.piimg.com/1949/5ee3f55ea72054a3.jpg',
                'http://i4.piimg.com/1949/badd92466e320acd.jpg',
                'http://i4.piimg.com/1949/15ea8ff36ce6b7a7.jpg',
                'http://i4.piimg.com/1949/f0df5fb3a9662fd5.jpg',
                'http://i4.piimg.com/1949/59648ac48e5ed61a.jpg',
                'http://i4.piimg.com/1949/bf084de0ce534c92.jpg']

#trailer_youtube
head = 'https://www.youtube.com/watch?v='
suffixes = ['ot6C1ZKyiME',
            'G8EEimdMsFg',
            '4xPC1lEJ6Mg',
            'kqX0-xn8j1g',
            'T50_qHEOahQ',
            'WcgCM2FyU8s']
urls = [head+suffix for suffix in suffixes]

movies = []
i = 0
while i < TOTAL: #TOTAL:The total of movies
    movies.append(media.Movie(movies_names[i],storyline[i],pics[i],urls[i]))
    i += 1

fresh_tomatoes.open_movies_page(movies)