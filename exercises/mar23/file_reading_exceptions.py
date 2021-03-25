def getMovies():
    movies = []

    #get the moves from the file
    try:
        with open("mar23/movie.txt") as file:
            for line in file:
                movie = line.replace("\n", "")
                movies.append(movie)
            return movies
    except FileNotFoundError:
        print("The show could not be located. Check permissions.")
        return movies #this right here will return an empty list

#using the function
print("Amazing TV animes")
movies = getMovies()

for movie in movies:
    print(movie)











