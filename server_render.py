import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Movie Trailer Website</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link href="https://fonts.googleapis.com/css?family=Inconsolata|Rancho|Handlee" rel="stylesheet"> 
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }

        /*Movie tiles design*/
        .movie-tile {
            margin: 28px;
            padding-left:0;
            padding-right:0;
            border: 1px solid grey;
            box-shadow: 10px 10px 15px #888888;
        }

        /* Changing the title Font & Size in the fixed Top Header*/
        .headerfont {
             font-family: 'Rancho', cursive;
             font-size:30px;
         }

         /* Comman Bckground color for Movie tiles header & details section*/
        .movie_tile_background {
        	background:rgba(36, 69, 97, 0.95);
            color:white;
        }

        /* Same font as Header font applied to the movie title but with smaller font-size & aligned left */  
        h3 {
            font-family: 'Rancho', cursive;
            padding:10px;
            margin:0px;
            font-size: 23px;
            border:1px solid;
        }

        /* Storyline div font set & aligned with justify*/
        .content{
            font-size:14px;
            font-family: 'Handlee', monospace;
            text-align:justify;
            padding:10px;
            border:1px solid;
        }

        /* Aligning the poster with margin & opacaity*/
        img {
            margin:5px;
            opacity: 0.85;
            position:relative;
        }

        /*For the play button icon on the poster*/
        .glyphicon {
           font-size:30px;
           position:absolute;
           right: 170px;
           top: 170px;
           color:white;
        }

        /* To highlight Read More click on option*/
        #readmore {
        	color: #8af0fb;
        	font-weight:bold;
       	}

       	#readmore:hover{
       		color:white;
       	}
        
        /* Modal dimensions*/
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }

        /* Close icon positioning to close the modal*/
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        

        .movie-trailer-play:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }

		/*To have all the cols with same height.. Tried display:table-row property, but did not work in Chrome*/
        .container.display-flex {
            display: flex;
          	flex-wrap: wrap;
        }
       
        /*Reducing the width of the movie tiles for 1200px and above*/
        @media (min-width: 1200px){
            .col-lg-4 {
            width: 28.333333%;
            }
        }

        /* FOr the Toggle effect achieved.. */
        .child{
        	display: none;
        }

		.child.visible {
		  display: block;
		}
        
    </style>
    <script type="text/javascript" charset="utf-8">
        //pause the video when the modal is closed
        $(document).on('click','.hanging-close, .modal-backdrop, .modal', function (event) {
         // Remove the src so the player itself gets removed, as this is the only
         // reliable way to ensure the video stops playing in IE
        $("#trailer-video-container").empty();
        });

        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-trailer-play', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });

        // To expand or hide the Read more info section
		$(document).on('click','.parent', function(e){
			e.preventDefault();
			var currentBox = $(this).parent().siblings(".child").toggleClass("visible");	
				$(".child.visible").not(currentBox).removeClass("visible");			
		});
    </script>

</head>
'''

# The main page layout and title bar
main_page_content='''
<body>
    <!--Trailer Video Modal-->
    <div class="modal" id="trailer">
        <div class="modal-dialog">
            <div class="modal-content">
                <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                    <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24" alt="X"/>
                </a>
                <div class="scale-media" id="trailer-video-container"></div>
            </div>
        </div>
    </div>

    <!--Main Page Content-->
    <div class="container">
        <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
            <div class="container">
                <div class="navbar-header">
                    <a class="navbar-brand headerfont" href="#">Movies Trailer Website</a>
                </div>
            </div>
        </div>
    </div>
    <div class="container display-flex">
      {movie_tiles}
    </div>
</body>
</html>
'''

# Single movie entry template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" >
    <header class="movie_tile_background">
        <h3>{movie_title}</h3>
    </header>
    <div class="movie-trailer-play" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
        <img src="{poster_image}" width="220" height="270">
        <span class="glyphicon glyphicon-play-circle"></span>
    </div>
    <div class="content movie_tile_background">
        <p>{movie_storyline}</p>
       	<a href="#" id="readmore" class="parent">Read more..</a>
    </div>
    <div class="movie_tile_background content child">
        <p><strong>Director :</strong> {movie_director} </p>
        <p><strong>Writer :</strong> {movie_writer} </p>
        <p><strong>Cast :</strong> {movie_cast} </p>
        <p><strong>Rating :</strong> {movie_rating} </p>
    </div>  
</div>
'''

def create_movie_tiles_content(movies):
    content = ''
    for movie in movies:
        #Extract the youtube id from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^#$]+',movie.youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^#$]+',movie.youtube_url)
        trailer_youtube_id =(youtube_id_match.group(0) if youtube_id_match
                             else None)

        #append title for movie with its content filled in
        #Format strings contain replacement fields surrounded by curly braces {}
        content += movie_tile_content.format(
            movie_title = movie.title,
            poster_image = movie.poster,
            trailer_youtube_id = trailer_youtube_id,
            movie_storyline = movie.storyline,
            movie_director = movie.director,
            movie_writer = movie.writer,
            movie_cast = ", ".join(map(str, movie.cast)),
            movie_rating = movie.rating
            )
    return content


'This file renders the HTML output for the movies instances created'
def open_movies_page(movies):
    #Create the output file
    output_file = open('MoviesTrailer.html','w')

    #Replace the movie titles placeholder generator content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    #Edit the output file or write to the empty file, main page layout + the rendered movie title content
    output_file.write(main_page_head + rendered_content)
    #close the output html file
    output_file.close()

    #open the output file in a new tab in the browser
    url = os.path.abspath(output_file.name)
    print url
    webbrowser.open('file://' + url, new=2)
