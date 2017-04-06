import media
import fresh_tomatoes
TOTAL =  6 #TOTAL:The total of movies

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