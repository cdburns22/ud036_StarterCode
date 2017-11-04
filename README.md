# Movie Trailer Website

This is a python tool to launch a website that displays a minimum of three movies with their title, poster, and link to trailer.

## Directions


To launch this website, run the media.py file. There are default movies already added or you can add your own.

### Default Movies

There are three movies seeded by default. These movies are Iron Man, Forrest Gump, and School of Rock.

### Adding Additional Movies

To add additional movies to the website, you must open the media.py file in an editor and create a new instance of the movie class with the following properties:

movie_variable = movie.Movie(“Movie Title”, “MoviePoster.png”, "https://www.youtube.com/watch?v=ABC12345678”)

*Movie poster image file must be a .png or .jpg in same directory as media.py*
*Movie trailer must be a youtube link*

After creating an instance of the movie class, append the new variable to the movieList array.
