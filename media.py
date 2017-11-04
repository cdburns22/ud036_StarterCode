import movie
import fresh_tomatoes

#Create instances of movie class for movies with required properties
iron_man = movie.Movie("Iron Man", "ironManPoster.jpeg", "https://www.youtube.com/watch?v=8hYlB38asDY")
forrest_gump = movie.Movie("Forrest Gump", "forrestGumpPoster.jpg", "https://www.youtube.com/watch?v=uPIEn0M8su0")
school_of_rock = movie.Movie("School of Rock", "schoolOfRockPoster.jpg", "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

#Add movie instances to list of movies to be displayed on movie site
movieList = [iron_man, forrest_gump, school_of_rock]

#Call method to open webpage and input list of movies
fresh_tomatoes.open_movies_page(movieList)
