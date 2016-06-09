#umdbapi
UMDb API

This api provides the functionality to retrieve IMDb information
about the movies provided in the url. The results are returned in
JSON format.

Replace the name of the movie you want to search in the given url:

https://umdb.herokuapp.com/moviesearch/?t=moviename&q=number

Example:

https://umdb.herokuapp.com/moviesearch/?t=matrix&q=3

The above url would return the first 3 search results for movie names matching
the keyword "matrix"
