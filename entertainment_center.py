import media
import fresh_tomatoes


kill_bill = media.Movie("Kill Bill",
                        "The story of a woman's revenge",
                        "https://en.wikipedia.org/wiki/Kill_Bill:_Volume_1#/media/File:Kill_bill_vol_one_ver.jpg",
                        "https://www.youtube.com/watch?v=ot6C1ZKyiME")

twelve_angry_men = media.Movie("12 Angry Men",
                        "A jury made up of 12 men as they deliberate the guilt or acquittal of a defendant.",
                        "https://en.wikipedia.org/wiki/12_Angry_Men_(1957_film)#/media/File:12_angry_men.jpg",
                        "https://www.youtube.com/watch?v=G8EEimdMsFg")

crouching_tiger_hidden_dragon = media.Movie("Crouching Tiger, Hidden Dragon",
                        "A young warrior steals a sword from a famed swordsman and then escapes into a world of romantic adventure.",
                        "https://www.google.co.jp/search?q=Crouching+Tiger,+Hidden+Dragon&tbm=isch&source=lnms&sa=X&ved=0ahUKEwiXmK_7_Y7TAhULl1QKHefPDfoQ_AUIBigB&biw=1296&bih=754#imgrc=N-4WwjzEC14XtM:",
                        "https://www.youtube.com/watch?v=4xPC1lEJ6Mg")

perfect_strangers = media.Movie("Perfect Strangers",
                        "Seven long-time friends play a game that put each one's phone and reveal every message or phone call received.",
                        "https://en.wikipedia.org/wiki/Perfect_Strangers_(2016_film)#/media/File:Perfetti-Sconosciuti-Poster-Locandina-2016.jpg",
                        "https://www.youtube.com/watch?v=kqX0-xn8j1g")

the_last_samurai = media.Movie("The Last Samurai",
                        "An American military advisor embraces the Samurai culture he was hired to destroy after he is captured.",
                        "https://en.wikipedia.org/wiki/The_Last_Samurai#/media/File:The_Last_Samurai.jpg",
                        "https://www.youtube.com/watch?v=T50_qHEOahQ")

ring = media.Movie("Ring",
                        "Reiko Asakawa is researching into a 'Cursed Video' interviewing teenagers about it. ",
                        "https://www.google.co.jp/imgres?imgurl=http://a0.att.hudong.com/53/91/300001349927131734919314440_950.jpg&imgrefurl=http://kbdy.h.baike.com/article-75359.html&h=800&w=600&tbnid=s_5N-6pJW7MO_M:&tbnh=186&tbnw=139&usg=__9gs4X_zl67YuNRmX6uAOd0z_064=&vet=10ahUKEwjK2IWcko_TAhWqv1QKHSc-BAAQ_B0IfzAK..i&docid=iAhCXCTFR_CoYM&itg=1&sa=X&ved=0ahUKEwjK2IWcko_TAhWqv1QKHSc-BAAQ_B0IfzAK&ei=BdjlWIrCPKr_0gKn_BA#h=800&imgrc=s_5N-6pJW7MO_M:&tbnh=186&tbnw=139&vet=10ahUKEwjK2IWcko_TAhWqv1QKHSc-BAAQ_B0IfzAK..i&w=600",
                        "https://www.youtube.com/watch?v=WcgCM2FyU8s")

#print(toy_story.storyline)

movies = [kill_bill,twelve_angry_men,crouching_tiger_hidden_dragon,perfect_strangers,the_last_samurai,ring]
fresh_tomatoes.open_movies_page(movies)