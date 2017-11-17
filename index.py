import server_render
import movies

# Creating movies by creating the instances of the Class Movie
spiderman = movies.Movie("Spider-Man: Homecoming (2017)"
    ,"http://www.cinema.com.my/images/movies/2017/7amazingspider300_450.jpg"
    ,"https://www.youtube.com/watch?v=U0D3AOldjMU"
    ,"""Peter Parker balances his life as an ordinary high school student in Queens 
    with his superhero alter-ego Spider-Man, and finds himself on the trail of a 
    new menace prowling the skies of New York City."""
    ,"Jon Watts"
    ,"Jonathan Goldstein (screenplay by), John Francis Daley (screenplay by)"
    ,['Tom Holland','Michael Keaton','Robert Downey Jr.','Marisa Tomei','Zendaya'
    ,'Gwyneth Paltrow']
    ,movies.Movie.RATINGS[3])

lion = movies.Movie("Lion (2016)"
    ,"https://cdn.traileraddict.com/content/the-weinstein-company/lion-2016-poster-3.jpg"
    ,"https://www.youtube.com/watch?v=-RNI9o06vqo"
    ,"""A five-year-old Indian boy gets lost on the streets of Calcutta, thousands of
    kilometers from home. He survives many challenges before being adopted by a 
    couple in Australia. 25 years later, he sets out to find his lost family"""
    ,"Garth Davis "
    ,"""Saroo Brierley (adapted from the book \"A Long Way Home\" by), Luke Davies 
    (screenplay by)"""
    ,[ 'Dev Patel', 'Nicole Kidman', 'Rooney Mara' ]
    ,movies.Movie.RATINGS[4])

thewalk = movies.Movie("The Walk (2015)"
    ,"http://www.justknow.in/cinema_images/1813088342the-walk-3d.jpg"
    ,"https://www.youtube.com/watch?v=GR1EmTKAWIw"
    ,"""In 1974, high-wire artist Philippe Petit recruits a team of people to help him
    realize his dream: to walk the immense void between the World Trade Center towers."""
    ,"Robert Zemeckis"
    ," Robert Zemeckis (screenplay), Christopher Browne (screenplay)"
    ,['Joseph Gordon-Levitt', 'Charlotte Le Bon', 'Guillaume Baillargeon']
    ,movies.Movie.RATINGS[4])

pink = movies.Movie("Pink (2016)"
    ,"https://upload.wikimedia.org/wikipedia/en/a/ae/Pinkmovieposter.jpg"
    ,"https://www.youtube.com/watch?v=AL2TShb6fFs"
    ,"""When three young women are implicated in a crime, a retired lawyer steps forward
    to help them clear their names."""
    ,"Aniruddha Roy Chowdhury"
    ,"""Shoojit Sircar , Aniruddha Roy Chowdhury & Ritesh Shah(story), Ritesh Shah (
    dialogue & screenplay )"""
    ,['Tapsee Pannu','Andrea Tariang','Kirti Kulhari','Amitabh Bachchan','Piyush Mishra']
    ,movies.Movie.RATINGS[3])

despicableme = movies.Movie("Despicable Me (2010)"
    ,"http://img.moviepostershop.com/despicable-me-movie-poster-2010-1010678700.jpg"
    ,"https://www.youtube.com/watch?v=sUkZFetWYY0"
    ,"""When a criminal mastermind uses a trio of orphan girls as pawns for a grand 
    scheme, he finds their love is profoundly changing him for the better."""
    ,"Pierre Coffin, Chris Renaud"
    ,"Cinco Paul (screenplay), Ken Daurio (screenplay)"
    ,['Steve Carell', 'Jason Segel', 'Russell Brand' ]
    ,movies.Movie.RATINGS[3])

avatar = movies.Movie("Avatar (2009)"
    ,"https://mrmoviefiend.files.wordpress.com/2010/06/avatar-poster-10.jpg"
    ,"https://www.youtube.com/watch?v=6ziBFh3V1aM"
    ,"""A paraplegic marine dispatched to the moon Pandora on a unique mission becomes 
    torn between following his orders and protecting the world he feels is his home."""
    ,"James Cameron"
    ,"James Cameron"
    ,['Sam Worthington', 'Zoe Saldana', 'Sigourney Weaver']
    ,movies.Movie.RATINGS[3])

neerja = movies.Movie("Neerja (2016)"
    ,"http://media.glamsham.com/download/poster/images/neerja/01-neerja.jpg"
    ,"https://www.youtube.com/watch?v=7779JrWy04g"
    ,"""Neerja is the story of the courageous Neerja Bhanot, who sacrificed her life 
    while protecting the lives of 359 passengers on the Pan Am flight 73 in 1986. 
    The flight was hijacked by a terrorist organization."""
    ,"Ram Madhvani"
    ,"""Saiwyn Quadras (story and screenplay) (as Saiwyn Qadras), Sanyukta Shaikh 
    Chawla (dialogue)"""
    ,['Sonam Kapoor', 'Shabana Azmi', 'Yogendra Tikku']
    ,movies.Movie.RATINGS[3])

# Movie_list array, contains the list of movies as input, which
# is passed to the function "open_movies_page". This function
# translates this list into a web page when we run the
# "index.py" file.
movie_list=[
    spiderman,
    lion,
    thewalk,
    pink,
    despicableme,
    avatar,
    neerja
]
server_render.open_movies_page(movie_list)


