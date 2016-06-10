#umdbapi
UMDb API

This api provides two functionalities. One is to search all the movies matching 
the given moviename. You can also provide the number of queries you wish to
retrieve. If number of queries is not provided, only one result is shown.

Example:
https://umdb.herokuapp.com/movies/search/?t=matrix&q=3


You can also get all the details of a movie by providing the movie id.

Example:
https://umdb.herokuapp.com/movies/details/tt0133093

The api returns a JSON Response.
